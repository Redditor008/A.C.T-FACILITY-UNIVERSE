"""A.C.T archive rendering engine.

Rebuilt 2026-10-22 after repeated workspace resets wiped the original. The original
module was inferred from the shipped output it produced, so the shipped reference
twins are the specification and this file is checked against them.

House limits
------------
Every line of a .txt archive file, box rule included, is at most 118 characters.
Markdown pipe tables are exempt because they render wrapped.

Width sets
----------
W2 = [28, 87]      two-column registry tables
W3 = [28, 43, 43]  three-column tables
Column 1 is 26 usable characters in both sets (width minus the two padding spaces).
"""

MAXC = 118          # hard line limit for .txt
W2 = [28, MAXC - 31]
W3 = [28, 43, 43]


def wrap(text, maxc):
    """Greedy word wrap. Never emits a line longer than maxc unless a single word is."""
    out, cur = [], ""
    for w in str(text).split():
        if cur and len(cur) + 1 + len(w) > maxc:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w) if cur else w
    if cur:
        out.append(cur)
    return out or [""]


def widths(n):
    if n == 2:
        return list(W2)
    if n == 3:
        return list(W3)
    if n == 1:
        return [MAXC - 2]
    base = max(12, (MAXC - n - 1) // n)
    return [base] * n


def _rule(w, ch):
    return "+" + "+".join(ch * c for c in w) + "+"


def box(header, rows, w=None):
    """Render an ASCII box. Every returned line is <= MAXC characters.

    header : list[str]
    rows   : list[list[str]]
    """
    n = len(header)
    w = list(w) if w else widths(n)
    if len(w) != n:
        raise ValueError("width set %r does not match %d columns" % (w, n))

    def cells(r):
        r = list(r) + [""] * (n - len(r))
        return [wrap(str(c).strip(), w[i] - 2) for i, c in enumerate(r[:n])]

    blocks = [cells(header)] + [cells(r) for r in rows]
    heights = [max(len(b[i]) for i in range(n)) for b in blocks]
    if any(h * (sum(w) + n + 1) for h in heights) and sum(w) + n + 1 > MAXC:
        raise ValueError("width set sums beyond the line limit")

    out = [_rule(w, "-")]
    for j, b in enumerate(blocks):
        for k in range(heights[j]):
            line = "|"
            for i in range(n):
                text = b[i][k] if k < len(b[i]) else ""
                line += (" " + text).ljust(w[i]) + "|"
            out.append(line)
        # the rule below the header is '=', every other rule is '-'
        out.append(_rule(w, "=" if j == 0 else "-"))
    return out


def mdtable(header, rows):
    """Render a Markdown pipe table. Cells are not width-limited; they render wrapped."""
    out = ["| " + " | ".join(str(c).strip() for c in header) + " |",
           "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        r = list(r) + [""] * (len(header) - len(r))
        out.append("| " + " | ".join(str(c).strip() for c in r[:len(header)]) + " |")
    return out


def check_widths(lines, label=""):
    """Return every (index, length, text) over MAXC. Used as a gate before writing."""
    bad = [(i, len(l), l) for i, l in enumerate(lines, 1) if len(l) > MAXC]
    if bad and label:
        raise AssertionError("%s: %d lines over %d, longest %d"
                             % (label, len(bad), MAXC, bad[0][1]))
    return bad


# --- parsing a markdown pipe table out of a plain-text file -------------------

def _is_sep(line):
    s = line.strip()
    return bool(s) and set(s) <= set("|-: ") and "-" in s and s.startswith("|")


def _is_rule(line):
    s = line.strip()
    return s.startswith("+") and set(s) <= set("+-=")


def split_cells(line):
    return [c.strip().strip("`") for c in line.strip().strip("|").split("|")]


def convert_md_tables(lines, w=None):
    """Rewrite markdown pipe tables in a plain-text file as ASCII boxes.

    A block is any run of consecutive lines that start with '|' or that are stray
    box rules, so hybrid files - a markdown header sitting on a '+===+' rule - are
    handled as one table rather than two half-tables. Separator rows are dropped.
    Returns (new_lines, n_tables_converted).
    """
    out, i, n = [], 0, 0
    while i < len(lines):
        line = lines[i]
        starts = line.startswith("|") or (_is_rule(line) and i + 1 < len(lines)
                                          and lines[i + 1].startswith("|"))
        if not starts:
            out.append(line)
            i += 1
            continue
        rows = []
        while i < len(lines) and (lines[i].startswith("|") or _is_rule(lines[i])):
            if lines[i].startswith("|") and not _is_sep(lines[i]):
                rows.append(split_cells(lines[i]))
            i += 1
        if not rows:
            continue
        cols = max(len(r) for r in rows)
        rows = [r + [""] * (cols - len(r)) for r in rows]
        out.extend(box(rows[0], rows[1:], w))
        n += 1
    return out, n


if __name__ == "__main__":
    # self-test against the documented house limits
    b = box(["REGISTRY FIELD", "CURRENT VALUE"],
            [["TECHNOLOGY DESIGNATION", "TECH-GOI-055-1"],
             ["TECHNOLOGY NAME", "Cairn and Lintel Threshold Stone Marker"],
             ["LONG DESCRIPTION", " ".join(["word"] * 60)]])
    assert not check_widths(b, "box self-test"), check_widths(b)
    assert b[0].startswith("+-") and b[2].startswith("+="), b[:4]
    assert all(len(l) <= MAXC for l in b)
    m = mdtable(["A", "B"], [["1", "2"]])
    assert m[1] == "|---|---|", m
    conv, k = convert_md_tables(["| A | B |", "|---|---|", "| 1 | 2 |"])
    assert k == 1 and conv[0].startswith("+-"), conv
    assert not check_widths(conv, "convert self-test")
    conv2, k2 = convert_md_tables(["| A | B |", "+===+===+", "| 1 | 2 |"])
    assert k2 == 1 and sum(1 for l in conv2 if l.startswith("| A")) == 1, conv2
    print("engine self-test passed: box, mdtable, convert_md_tables")
    print("widest box line produced: %d (limit %d)" % (max(len(l) for l in b), MAXC))
