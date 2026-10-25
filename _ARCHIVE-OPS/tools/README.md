# Archive Tools

Working tools for the A.C.T archive. Not fiction, not canon.

| File | What it is |
|---|---|
| [engine.py](engine.py) | The archive rendering engine: per-column word wrapping, the ASCII box renderer, the Markdown table renderer, the 118-character width gate, and the markdown-to-box converter |

## Why this folder is tracked

These tools used to live in an untracked `.arena/` directory. That directory has been wiped
repeatedly by workspace resets, and the engine had to be rebuilt from shipped output twice.
It is tracked here so that the renderer and its limits survive.

The `never commit .arena/` rule still applies to `.arena/` itself, which holds scratch
scripts. Anything worth keeping moves here.

## Running it

```
PYTHONPATH=_ARCHIVE-OPS/tools python3 _ARCHIVE-OPS/tools/engine.py
```

Run without arguments it executes its self-test: the box renderer, the Markdown table
renderer, the converter, and the width gate.

## The specification it is held to

- Every line of a `.txt` archive file, box rule included, is at most **118 characters**.
- Markdown pipe tables are exempt, because they render wrapped.
- Column widths are `[28, 87]` for two-column registry tables and `[28, 43, 43]` for
  three-column tables. Column 1 is 26 usable characters in both.
- The rule immediately below a box header is `=`. Every other rule is `-`.

## Verified against

The renderer reproduces the shipped reference twin
`TECH-GOI-055-1-Cairn-and-Lintel-Threshold-Stone-Marking-System.txt` **byte-identically**,
24 lines against 24. Across the archive, 1,136 of 1,243 boxes round-trip exactly. The 104
that do not carry correct widths and differ only because the readback joins a wrapped cell
with a space before re-wrapping it.
