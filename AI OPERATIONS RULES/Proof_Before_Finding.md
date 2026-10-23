# Proof Before Finding

No finding about this archive ships until the instrument that produced it has been proven against
a case whose answer is already known. This rule exists because three false findings were shipped
from unproven instruments, and one of them was a false retraction of a true number.

| FIELD | VALUE |
|---|---|
| Rule type | Verification gate |
| Applies to | Every measurement, audit, count, comparison and retraction |
| Owner ruling | 2026-10-22 |
| Status | Binding on any AI agent working in this repository |

## The rule

Before reporting any number, any absence, or any discrepancy:

1. **Prove the instrument.** Run it against at least one case whose correct answer you already
   know, and show that it returns that answer. A census of designation families must be run
   against a file you have opened and read.
2. **Prove it finds what exists.** An instrument that returns zero proves nothing until it has
   returned non-zero on a case you know is present. Zero is a result, not a verification.
3. **Read the slice you measured.** Print the character count and the first lines of whatever
   region the instrument operated on. A search that silently lands in the wrong section produces
   clean output about the wrong text.
4. **State the instrument with the finding.** A finding is incomplete without the pattern, path
   and filter that produced it, so a reader can re-run it.

## Why this rule exists

Three real failures, all shipped as findings before the instrument was checked.

**A chapter slice taken from the contents list.** `ACT_Complete_Designation_and_Class_Reference.md`
carries a `## Contents` list repeating every chapter title. `s.find("PART I")` matched the
contents entry and sliced 2,588 characters of front matter instead of the 63,966-character
chapter. Every extraction against that slice returned nothing, and the emptiness was reported as
a property of the doctrine.

**A format the chapter does not use.** PART I holds zero table rows; its 9,314 words are prose
across 17 numbered sections. Table-shaped extractors returned nothing and the nothing was read as
a gap in the doctrine.

**A three-segment pattern against a four-segment designation.** `ANM` records use
`ANM-XX-XX-0000`. The pattern looked for `XXX-XX-000`, matched the inner `QU-AS-0003` of
`ANM-QU-AS-0003`, and reported `QU` as a designation family. `QU` is a type code. The instrument
then reported `ANM` absent, and a true count of four was retracted on that evidence.

## The sharper lesson

A retraction is a finding like any other and needs the same proof. Retracting a true number on a
bad instrument leaves the reader holding two wrong statements instead of one. Withdraw the
retraction in the same place it was recorded, say which statement was false, and give the
corrected measurement.

## Splice anchors and clean exit codes

**Search a splice anchor after the section start.** A section is replaced by slicing from a start
index to an end index. If the end anchor is searched from the beginning of the file and that
string appears more than once, the end index can land *before* the start index, and the splice
then duplicates everything between them instead of replacing anything.

```
s.index(anchor)          # wrong: finds the first occurrence anywhere in the file
s.index(anchor, start)   # right: finds the first occurrence at or after the section start
```

This happened for real. `**Reading examples.**` appears twice in
`ACT_Complete_Designation_and_Class_Reference.md`, once in PART I and once in PART II. The
unanchored search gave `old_start=70020, old_end=36574`, and the resulting splice inserted 863
lines and a second copy of a chapter heading.

**A clean exit code is not a pass.** That splice exited zero and wrote the file. What caught it
was counting afterwards:

```
git diff --numstat   ->  863  0     (863 insertions and no deletions is a duplication)
chapter count        ->  PART II listed twice
line count           ->  3053 against a known 2190
```

After any edit that splices, replaces or rewrites a region, verify the result by counting
something the edit should not have changed — total lines, chapter headings, word count — and
compare against the figure measured before the edit. Report both numbers.

## Tool output is formatted, not raw

A tool that lists paths, counts things or renders text applies its own formatting, and that
formatting can look like a defect in the data. Read tool output through the tool's own options
before treating anything in it as a finding.

```
git ls-files                          # quotes and escapes any path with a non-ASCII character
git -c core.quotepath=false ls-files  # prints the real filename
```

This produced a false finding. Two tracked files appeared as:

```
HIGENMARU-K\305\214RIN-AFD-OB-221.txt"
```

The trailing quote read as a corrupted filename left by a bad shell command. It was git's closing
quote, and `\305\214` was the character `Ō` in octal. Re-measured with quoting disabled, the
filenames were clean and zero files carried a quote character. Nothing needed renaming.

The same trap covers wrapped terminal lines that read as over-length lines, table borders that
count as data rows, and any census whose tool silently truncates. When a measurement looks wrong,
change the tool's output settings before changing the data.

## Never commit while your own output contains a failing number

Read the whole verification block before committing, not the exit status and not the last line. A
failing number sitting among passing ones is still a failure, and the commit message will be
wrong in the same breath as it.

This happened. A dossier correction was verified, the block printed

```
GOI-HY-N-074-Ninefold-Ark.txt | lines>118: 1 | prose>118: 1
```

and the commit shipped anyway, because the number was one line among several clean results and was
read past. The defect was a 164-character prose line in a file with a 118-character limit, created
by inserting replacement text without re-wrapping it.

The rule that follows from it:

1. Print every check in one block and read every line of it before committing.
2. If any line reports a non-zero count of defects, fix it in the same turn. Do not commit and
   fix afterwards.
3. Any inserted or replaced prose must be re-wrapped to the house limit before the file is
   written. Insertion is not wrapping.
4. Where a defect is found after a commit has shipped, say which commit carried it and what the
   number was. Do not let the correction commit imply the defect was only just discovered.

## No number in a commit message that has not been measured

A commit message is a claim about the change. Every figure in it must come from the verification
block that ran on the change, and a message drafted before the block must be reconciled against it
before the push.

This failed. A rebuild commit message stated 1,177 words and that a repeated phrase had dropped
from eleven occurrences to four. The verification block, which ran in the same command, reported
1,153 words and one occurrence. The message was drafted from expectation and pushed without being
checked against the numbers printed above it.

The rule:

1. Run the verification block first.
2. Write the message from its output, not from what the change was intended to do.
3. Where a message has already been drafted, read it against the block line by line before
   committing.
4. Where a wrong figure has been pushed, state the correct one in the next report and name the
   commit that carried the error. Do not let the correction pass silently.

## Related standing gates

- Compare `git rev-parse HEAD` against `git ls-remote origin <branch>` before the first edit of
  any batch. Workspace resets return HEAD to the session base and wipe `.arena/`.
- A checker must test the post-change form of the text, never the pre-change form.
- Count records, not files. A recursive census must actually recurse.
- Never state a number without re-measuring it in the same breath.
