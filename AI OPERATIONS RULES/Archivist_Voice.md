# Archivist Voice

Rules for the vocabulary and stance of any in-world document in this repository. They exist because
a document can avoid every cliché on an AI-tell list and still read like a summary written from
outside the institution rather than a record written from inside it.

| FIELD | VALUE |
|---|---|
| Rule type | Voice and vocabulary gate |
| Applies to | Every in-world document in `A.C.T Universe Document/` |
| Authority | Archive owner |
| Reference voice | The doctrine documents in `A.C.T .md Document/` |

## The test

The writer of an A.C.T document is an archivist inside the Facility. Not a journalist describing it,
not an assistant summarising it, not an intern filling in a form. Every rule below follows from
that single fact.

## Measured markers

Figures are occurrences per document. "Owner" is the mean across 40 original doctrine documents
taken from the repository's base commit, before any generated work.

| Marker | Owner doctrine | 229 technology records | 13 generated records |
|---|---|---|---|
| `not recorded` | 0.00 | 0.26 | **8.31** |
| `this record` | 0.08 | 1.44 | **3.31** |
| `the archive` | 1.10 | 0.71 | **0.00** |
| `must be` | 1.20 | 0.49 | **0.23** |
| `must not` | 0.73 | 0.34 | 0.38 |
| `mandate` | 0.30 | 0.08 | **0.00** |
| `personnel` | 8.35 | 3.98 | 3.31 |

The generated records are the outlier on every marker. 181 of the 242 technology records contain no
instance of `not recorded` at all, and all twelve records containing five or more were generated.
101 technology records say `the archive`; none of the thirteen generated ones did.

## The rules

**Never write `not recorded` to fill a field.** If the source is silent on a point, either leave the
point out or say what the silence means. Eight instances in one document is the sound of a form
being completed. An archivist with nothing to enter does not enter anything.

**Say `the archive` when the institution is the actor.** The archive holds, refers, retains, files
and refuses. A document that only ever says *this record* is describing itself from outside.

**Write obligations as `must be`.** An archivist states what is required. `is not established` and
`is unknown` report a gap; `must be` and `must not` carry authority. Use the reporting forms only
where the gap is genuinely the subject.

**Use the institutional nouns** — personnel, division, clearance, mandate, restricted — at the rate
the doctrine uses them. These are not decoration; they are how the Facility talks about itself.

**End a section on a line that lands.** The doctrine closes sections with a sentence that states a
consequence rather than summarising what was just said:

> The narrative status is not decorative. It tells future personnel what lie civilians are living
> inside.

## What this rule is not

It is not a vocabulary substitution list. Replacing *this record* with *the archive* mechanically
produces a worse document. The stance comes first: a person responsible for these files, writing to
colleagues who will have to act on them.

## Structure follows content

A document's structure is not chosen from a template. It follows what the document contains and
what vocabulary it needs. A record covering one unopened container of unknown contents is not the
same length as a record covering an operating system, and its chapters are not the same chapters.

Measured across the original doctrine: 627 to 13,040 words, one to fourteen H1 headings, zero to
113 H3s, numbered sections in half the documents and none in the other half, most using no tables
at all. Uniform length and uniform chapter count across a set of records is itself an AI signature,
because a real archive grows documents of whatever size their subject requires.
