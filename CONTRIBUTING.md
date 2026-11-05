# Building and editing

Run `just build` to create the PDF, `just check` for the complete validation
suite, and `just fmt` to format Typst with the editor settings. Machine
settings belong in an untracked `.env` file. Fonts and their licences are
included under `assets/fonts`; system fonts are not used.

The mathematical checks are described in `checks/README.md`:
`just check-sage` runs the exact computations with SageMath, and
`just check-lean` compiles and audits the Lean proofs, against a prebuilt
mathlib checkout of the pinned commit given by `LEAN_MATHLIB` in `.env`, or
in `checks/lean` after `lake build` there. A change of mathematics in a
passage listed in `checks/lean-proofs.json` calls for a review of the proof
linked to it.

## Structure and numbering

Chapter files contain plain markup included by `content/main.typ`, one file
per section: `content/CC-SS-slug.typ` (chapter, section); the chapter's own
heading and introduction are in `content/CC-00-slug.typ`. Import
`main-defs.typ` and `statements.typ`.

- Chapters (`= Title <ch:…>`) are numbered 1–7, sections (`== Title
  <sec:…>`) 1.1, 1.2, … within their chapter. No number is typed in a
  heading.
- Definitions, lemmas, theorems, propositions, corollaries and questions
  share one counter within each section and print chapter.section.item:
  Theorem 1.1.3. A numbered display, if any, is an equation followed by an
  `eq:` label and takes its number from the same series, "(2.8.1)".
- Remarks, examples and exercises are unnumbered.
- Every numbered object carries a literal, stable semantic label
  immediately after it. References use native `@label` syntax and print
  the computed number; the word before it is typed in the text, tied with
  `~`: `Theorem~@th:whitehead-cw` prints "Theorem 1.5.8",
  `Section~@sec:fibrations` "Section 1.6", `Chapter~@ch:group-cohomology`
  "Chapter 2". A part of a statement is `@th:…[(iv)]`, printed
  "4.5.8 (iv)"; a display `@eq:…` prints "(2.8.1)" with its parentheses.
  In mathematics write `#[@label]`.
- Volume I is cited by its printed numbers, "Section 2.2 of Volume I":
  these references are text, listed with their reason under
  `literal_references` in `config/lint.json`, as are the places in other
  works, "May [@bib:May1967], Theorem~17.1".

## Statements

- `#theorem[…]`, `#lemma[…]`, `#proposition[…]`, `#corollary[…]`,
  `#question[…]`: the name in small capitals with its number, the text in
  italics. `title:` gives the attribution in parentheses, in roman:
  `#theorem(title: [Fibring property])[…] <th:fibring-property>`.
- `#definition[…]`: the head in small capitals with its number, the text
  in italics, as printed in this volume. Defined terms are bold:
  `*Moore loops*`.
- `#remark[…]`, `#example[…]`, `#exercise[…]`: unnumbered heads in small
  capitals, text in roman; `kind: "Remarks"`, `"Examples"` and so on as
  printed. A numbered list of exercises after one head is
  `#exercises[+ … + …]`, printed "Exercises. 1. … 2. …".
- `#proof[…]` prints "Proof." and the open square at the right margin
  after the last line, also after a closing display or list item; another
  head is `head: [Proof of Theorem~@th:…]`. A statement printed with the
  square and no proof takes `closed: true`; one whose text begins on a new
  line after the head takes `head-break: true`.
- An unnumbered heading inside a section, "Representable functors.", is
  `#subhead[Representable functors]`: small capitals, indented, kept with
  what follows; text in the same paragraph runs on after it.
- Lists of parts "(i)", "(ii)" are native items `+ …`. They are set as
  paragraphs beginning with the label, as printed: each part is a new
  indented paragraph; a statement or proof that begins with a list runs
  its first part on after the head, or, where the book begins the parts
  on a new line after the head, `#part-lines[+ … + …]`. Other labels:
  `enum(numbering: "(a)", …)`.
- A figure is `#figure([…], caption: [The map $theta$]) <fig:…>`, printed
  "Figure 1. The map θ" below it; figures are numbered through the book
  and cited `Figure~@fig:…`.
- The author's footnotes are native footnotes. Editorial notes use
  `#ed-note[…]`: marked *1, *2, … and ending "— Ed."; a paragraph with a
  note is kept on the page of its note. A work cited only in the notes is
  described in `editorial.bib` and listed, numbered [E1], [E2], …, in
  `content/81-editorial-references.typ` after the Bibliography; it is
  cited as `[@bib:Key]` like the works of the book.

## Paragraphs

A blank line in the source is a paragraph break. Text after a display, a
list or a statement following a blank line is a new paragraph and gets the
paragraph indent; text following a display without a blank line continues
the sentence, flush left. Do not type indents or spaces for layout.

## Notation

Operators of the book are defined in `main-defs.typ`: `Hom`, `End`, `Aut`,
`Ext`, `Tor`, `Ker`, `Coker`, `Im`, `Rad`, `Soc`, `Tr`, `Res`, `Ind`,
`Inf`, `rank`, `Mat`, `Nat`, `Map`, `Princ`, `Diff`, `Sing`, `Ch`, `grad`,
`Id`, `Stab`, `Link`; in lower case as printed, `norm` (the Evens norm),
`tr`, `coker`, `spec`, `proj`. Groups and modules set as letters of the
formula, so that "BGL(Λ)" is tight: `GL`, `SL`, `PGL`, `Sp`, `St`; `Tot`
for the total complex, "F^p Tot"; `Sq^i` for the Steenrod squares, in
italics as printed; `Ex` for Kan's functor, `$Ex^infinity$`. The limits
`invlim_n` and `dirlim_n` carry their arrow, with the index below it also in
running text. Left primes of the two filtrations of a double complex are
`lprime(E)_0`, `ldprime(E)_0` (′E₀, ″E₀). `op` gives the roman "op" of the
opposite ring, `$Lambda^op$` (another operator is `math.op("…")`);
`bold("Set")` the boldface categories; the number systems are blackboard
bold, `ZZ`, `QQ`, `CC`, as printed; `lmodule(Lambda, M)` gives
${}_Lambda M$; `lconj(g, H)` the left conjugate ${}^g H$; `M down_H`,
`N up^G`, `N Up^G` restriction, induction and co-induction; `res`. A display
marked with a symbol, "(†)", is `#symbol-display("†", $ … $) <eq:…>`; with
`parens: true` the symbol stands in parentheses at the display as well,
"(∗)". A framed display is `$ boxed(…) $`. A table of cases in running
text whose first row stands on the line of the text before it is
`topcases(…)` (Theorem 5.13.1). A display line too long for the source is
given as pairs of sides: `$ #aligned-rows(($A$, $= B$), ($$, $= C$)) $`.
Commutative diagrams use the helpers of `content/diagrams/common.typ`
(`cd`, `ladder`, `maps-grid`, `grid-diagram`, with `size:` for a diagram
the book prints in smaller type); spectral-sequence pages are drawn from
their data in CeTZ. Keep visible function arguments outside subscripts,
for example `$f_i lr((x))$` or `$h_i (X)$`. Do not type numbers or layout
adjustments in chapter files; fix typography in the common style.

## Index and bibliography

The index is generated from `#idx(...)` marks beside the passages. Its
arguments are the entry and its subentries as printed: `#idx("radical",
"Jacobson")`. For a named object use `#idx("Term", target: [@th:name])`;
the locator then follows the beginning of that object. Mathematics in an
entry is written between dollars: `#idx("$lmodule(Lambda, Lambda)$")`.

Bibliographic descriptions are stored only in `references.bib`, with stable
surname-and-year keys. Citations keep the brackets of the book: "[143]" is
`[@bib:Kan1955]`, "[143, 145]" is `[@bib:Kan1955, @bib:Kan1958]`, a range
"[a]–[b]" is `[@bib:…]–[@bib:…]` followed by `#bib-mentions(<bib:…>, …)` for
the works inside it. The generated bibliography lists for each work the
pages of this edition that cite it.

A record gives the printed description in its `annotation` field: the text
after the names, with `{field}` for a field of the record and `{Key.field}`
for a field of a related component, such as an erratum or a translation.
The names come from `author`, or `editor` with `editortype`; a suffix is
written `Arnold, Jr, J. E.`, and `nameaddon` follows the names. `journal`
is the full title, `shortjournal` the verified abbreviation and `userb`
the book's own abbreviation where it differs; `{journal}` prints `userb`,
else `shortjournal`. `usera` is the word joining the last two authors
where the book does not use "and", and `userc` names the component a DOI
belongs to. The comment at the top of `content/bibliography-style.typ`
describes every field.

## Pagination

The cover is outside the page count. The preliminary pages i–xii are those
of the printed book: half-title, list of the series, title page and its
back, the contents, a blank page, the Introduction and a blank page. The
text begins a new arabic series at 1. Chapters, the bibliography, the
editorial references and the index open on right-hand pages; a page left
blank before them has neither running head nor folio. Typesetting reflows
the text: its folios need not match those of the printed book.

## Corrections

Confirmed textual emendations are recorded in `corrections.json`, which
also supplies the separate corrections PDF; its entries quote the printed
page numbers. The author's own corrections are applied in the text and
recorded there without editorial notes.
