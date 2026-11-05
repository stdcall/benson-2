#import "numbering.typ": restart-counters
#import "statements.typ": (
  list-lead, list-style, new-paragraphs, numbered-display, paragraph-indent,
)
#import "main-defs.typ": reference-rules
#import "note-layout.typ": bookmark-title, contains-note, keep-note-runs
#import "note-layout.typ": without-notes
#import "note-layout.typ": heading-above, paragraph-context

// The page of the book: 6 × 9 in, the text block of the printed edition.
#let body-margin = (inside: 20mm, outside: 20mm, top: 26mm, bottom: 21mm)
#let running-chapter = state("running-chapter", [])
#let running-section = state("running-section", [])
// Pages that open a chapter, the bibliography or the index print no running
// head; their folio stands at the foot of the page.
// The Introduction begins under the running head of its page.
#let opening-page() = {
  query(heading.where(level: 1))
    .filter(it => it.body != [Introduction])
    .map(it => it.location().page())
    .contains(here().page())
}
#let folio() = counter(page).display()
// A break to the next right-hand page. The cover precedes page i, so a
// right-hand page is an even page of the file. A page left empty by the
// break carries neither running head nor folio, as printed.
#let recto-break() = {
  metadata((kind: "recto-break", side: "before"))
  pagebreak(weak: true, to: "even")
  metadata((kind: "recto-break", side: "after"))
}
#let blank-page() = {
  let marks(side) = query(metadata.where(value: (
    kind: "recto-break",
    side: side,
  )))
  let befores = marks("before")
  let afters = marks("after")
  let page = here().page()
  range(befores.len()).any(i => {
    let before = befores.at(i).location()
    let after = afters.at(i).location()
    // Strictly between the two marks, or a page whose text ended just
    // before it (the mark stands at the top of an otherwise empty page).
    (
      page < after.page()
        and (
          before.page() < page
            or (
              before.page() == page
                and before.position().y <= body-margin.top + 1pt
            )
        )
    )
  })
}
#let head-text(body) = text(size: 7.5pt, tracking: 0.04em, body)
// Running heads as printed: on even pages the folio and the chapter, "2
// 1. BACKGROUND MATERIAL FROM RINGS AND MODULES"; on odd pages the first
// section that begins on the page, or else the section in force, and the
// folio, "1.2. THE JACOBSON RADICAL 3".
#let running-header = context {
  if opening-page() or blank-page() { return }
  let row(outer-left, middle, outer-right) = grid(
    columns: (3em, 1fr, 3em),
    align: (left + bottom, center + bottom, right + bottom),
    outer-left, middle, outer-right,
  )
  let here-page = here().page()
  // The Introduction begins under its own running head.
  let opening = query(heading.where(level: 1)).find(it => (
    it.location().page() == here-page
  ))
  let chapter = if opening == none { running-chapter.get() } else {
    without-notes(opening.body)
  }
  if calc.even(counter(page).get().first()) {
    row(text(size: 9pt, folio()), head-text(chapter), [])
  } else {
    let beginning = query(heading.where(level: 2)).find(it => (
      it.numbering != none and it.location().page() == here-page
    ))
    let section = if beginning != none {
      let n = counter(heading).at(beginning.location())
      upper[#n.at(0).#n.at(1). #without-notes(beginning.body)]
    } else if opening != none or running-section.get() == [] {
      chapter
    } else { running-section.get() }
    row([], head-text(section), text(size: 9pt, folio()))
  }
}
// An inline formula taller than the text line takes the room it needs, so
// that it does not run into the neighbouring lines; also used by the
// corrections list.
#let inline-equation(it) = context {
  // As in TeX, a line is opened up only where the formula would otherwise
  // reach into the lines above or below: above about 0.85em (a fraction, a
  // tall superscript) or more than 0.38em below the baseline. Parentheses
  // with a subscript fit in the usual leading.
  let ink = measure({
    set text(top-edge: "bounds", bottom-edge: "bounds")
    it
  })
  let above = measure({
    set text(top-edge: "bounds", bottom-edge: "baseline")
    it
  }).height
  let tall = above > 0.85em.to-absolute()
  let deep = ink.height - above > 0.38em.to-absolute()
  let equation = if tall or deep {
    text(
      top-edge: if tall { "bounds" } else { "cap-height" },
      bottom-edge: if deep { "bounds" } else { "baseline" },
      it,
    )
  } else { it }
  // Keep short inline relations intact at line/page boundaries; long
  // equations retain native mathematical line breaking. Letters joined to
  // a formula ("$p$th", "$G$-module") stay on its line.
  if ink.width <= 6em.to-absolute() { box(equation) } else { equation }
  sym.wj
}

// "(mod …)" keeps its distance from the term before it, as \pmod does in
// TeX: 8mu in a line of text, 18mu in a display; also used by the
// corrections list.
#let mod-spacing(it) = {
  let gap = if it.block { 1em } else { 8em / 18 }
  let starts-with-mod(lr) = {
    if not lr.body.has("children") { return false }
    let parts = lr.body.children.filter(c => c.func() != [ ].func())
    (
      parts.len() > 1
        and parts.at(1).func() == math.op
        and parts.at(1).text == [mod]
    )
  }
  // A "mod" in the line is spaced as a binary operator, as \bmod: also
  // next to the bars of "|X^H| ≡ |X^H'| mod |H' : H|".
  show math.op: o => if o.text == [mod] { math.class("binary", o) } else {
    o
  }
  // A space after "mod" too, as with \pmod: "(mod |G|)".
  show math.lr: lr => if starts-with-mod(lr) {
    show math.op: o => if o.text == [mod] { o + h(6em / 18) } else { o }
    h(gap) + lr
  } else { lr }
  it
}


// Lists of parts, "(i)", "(ii)", are paragraphs that begin with the label,
// as printed: each part is a new paragraph with the paragraph indent, and
// its lines after the first run back to the margin. A list that opens a
// statement runs its first part on after the head.
// Nested lists keep the native layout.
#let list-depth = state("list-depth", 0)
#let run-in-list(it) = context {
  if list-depth.get() > 0 { return it }
  let lead = list-lead.get()
  let lines = list-style.get() == "lines"
  list-lead.update(none)
  list-depth.update(d => d + 1)
  // `part-lines`: the head of a statement stands alone, the parts begin on
  // the next line.
  if lines and lead != none {
    block(above: 0pt, below: par.leading, sticky: true, lead)
    lead = none
  }
  let n = if it.start == auto { 1 } else { it.start }
  let first = true
  for item in it.children {
    let explicit = item.at("number", default: none)
    if explicit not in (none, auto) { n = explicit }
    let label = if type(it.numbering) == function {
      (it.numbering)(n)
    } else { text(style: "normal", numbering(it.numbering, n)) }
    let opening = if first and lead != none { lead } else {
      h(paragraph-indent)
    }
    block(
      width: 100%,
      above: if first { par.spacing } else { par.leading },
      below: par.leading,
      breakable: true,
      [#opening#label#h(0.45em)#new-paragraphs(item.body)],
    )
    first = false
    n += 1
  }
  list-depth.update(d => d - 1)
}

#let book-style(body) = {
  set page(
    width: 6in,
    height: 9in,
    margin: body-margin,
    header: text(size: 9pt, running-header),
    header-ascent: 35%,
    footer: context if opening-page() {
      align(center, text(size: 9pt, folio()))
    },
  )
  set text(font: "Libertinus Serif", size: 10.5pt, lang: "en", region: "gb")
  // Interword spaces shrink less than Typst's default allows: a squeezed
  // space vanishes next to an italic letter ("IfU").
  set par(
    justify: true,
    leading: 0.47em,
    first-line-indent: paragraph-indent,
    spacing: 0.47em,
    justification-limits: (spacing: (min: 80%, max: 150%)),
  )
  // Short unfinished prose introduces the next block. Keep its native par
  // with that block; complete sentences and longer prose retain normal flow.
  show selector.or(
    block,
    enum,
    list,
    terms,
    table,
    figure,
    heading,
    outline,
    math.equation.where(block: true),
  ): it => {
    it
    paragraph-context.update("flush")
  }
  show par: it => context {
    let before = paragraph-context.get()
    let words(body) = {
      if type(body) == str { return body }
      if type(body) != content { return "" }
      if body.has("text") { return words(body.text) }
      if body.has("children") { return body.children.map(words).join() }
      if body.has("child") { return words(body.child) }
      if body.has("body") { return words(body.body) }
      ""
    }
    let has-math(body) = {
      if type(body) != content { return false }
      if body.func() == math.equation { return true }
      if body.has("children") { return body.children.any(has-math) }
      if body.has("child") { return has-math(body.child) }
      if body.has("body") { return has-math(body.body) }
      false
    }
    let plain = words(it.body).trim()
    // Only text set at the left: a line set at the right (a signature)
    // keeps its alignment.
    if (
      before != "paragraph"
        and align.alignment in (start, left)
        and plain != ""
        and plain.len() <= 80
        and plain.split(regex("\\s+")).len() <= 12
        and not plain.ends-with(regex("[.!?;][)\\]\"”’]*$"))
        and not has-math(it.body)
    ) {
      block(above: par.spacing, below: par.spacing, sticky: true, it)
    } else { it }
    paragraph-context.update("paragraph")
  }
  show link: set text(fill: black)
  // A hyphen joined to the preceding word or formula ("-module",
  // "$Lambda$-$Gamma$-bimodule") never begins a line.
  show regex("^-(\p{L}|$)"): it => sym.wj + it
  show "–": it => sym.wj + it + sym.wj
  // Lists of parts are numbered (i), (ii), ... in upright type, also in
  // italic statements, as in the book; other forms are given by
  // `enum(numbering: ...)`.
  set enum(numbering: (..n) => text(style: "normal", numbering("(i)", ..n)))
  show enum: run-in-list
  // Bookmarks and the contents carry the printed numbers: "Chapter 1." and
  // "1.1." for a section.
  set heading(numbering: (..n) => {
    let numbers = n.pos()
    if numbers.len() == 1 {
      "Chapter " + str(numbers.first()) + "."
    } else {
      numbers.map(str).join(".") + "."
    }
  })
  show heading.where(level: 1): it => {
    bookmark-title(it)
    // Chapters, the contents, the bibliography and the index begin on a
    // right-hand page, as printed.
    recto-break()
    let numbered = it.numbering != none
    // Running heads are in capitals, "1. BACKGROUND MATERIAL FROM RINGS
    // AND MODULES", "BIBLIOGRAPHY"; that of the Introduction is not.
    let introduction = it.body == [Introduction]
    running-chapter.update(if numbered {
      context upper[#counter(heading).at(it.location()).first(). #without-notes(
          it.body,
        )]
    } else if introduction { without-notes(it.body) } else {
      upper(without-notes(it.body))
    })
    running-section.update([])
    restart-counters(1)
    if numbered {
      context {
        let chapter = counter(heading).at(it.location()).first()
        [#metadata((
          kind: "numbered",
          family: "heading",
          level: 1,
          number: (chapter,),
        ))<numbered>]
      }
    }
    if introduction {
      block(width: 100%, above: 0mm, below: 5mm, align(center, text(
        size: 12pt,
        weight: "bold",
        it.body,
      )))
      return
    }
    block(width: 100%, above: 30mm, below: 9mm, align(center, {
      set par(first-line-indent: 0pt, justify: false)
      if numbered {
        block(below: 9mm, text(
          size: 10.5pt,
          weight: "regular",
          tracking: 0.02em,
          [CHAPTER #context counter(heading).at(it.location()).first()],
        ))
      }
      text(size: 14.5pt, weight: "bold", it.body)
    }))
  }
  show heading.where(level: 2): it => {
    bookmark-title(it)
    if it.numbering != none {
      restart-counters(2)
      context {
        let n = counter(heading).at(it.location())
        [#metadata((
          kind: "numbered",
          family: "heading",
          level: 2,
          number: (n.at(0), n.at(1)),
        ))<numbered>]
        running-section.update(upper[#n.at(0).#n.at(1). #without-notes(
            it.body,
          )])
        block(
          width: 100%,
          above: heading-above(2),
          below: 3.5mm,
          sticky: true,
          align(center, text(
            size: 10.5pt,
            weight: "bold",
            [#n.at(0).#n.at(1).#h(0.5em)#it.body],
          )),
        )
      }
    } else {
      block(
        width: 100%,
        above: heading-above(2, numbered: false),
        below: 3.5mm,
        sticky: true,
        align(center, text(weight: "bold", it.body)),
      )
    }
  }
  show heading: set par(first-line-indent: 0pt, justify: false)
  // The contents as printed: "Chapter 1." and its title, the sections
  // indented under it, the pages at the right margin without leaders.
  show outline: set par(first-line-indent: 0pt)
  show outline.entry: set block(breakable: false)
  show outline.entry.where(level: 1): set block(above: 1.1em)
  show outline.entry: it => {
    let title = without-notes(it.body())
    let numbers = if it.element.numbering != none {
      counter(heading).at(it.element.location())
    }
    let prefix = if numbers == none { [] } else if it.level == 1 {
      [Chapter #numbers.first().]
    } else { [#numbers.slice(0, 2).map(str).join(".").] }
    link(it.element.location(), grid(
      columns: if it.level == 1 { (auto, 1fr, 2em) } else {
        (1.2em, 2.6em, 1fr, 2em)
      },
      column-gutter: if it.level == 1 { 0.6em } else { 0.2em },
      ..if it.level == 1 {
        (
          if numbers == none { title } else { prefix },
          if numbers == none { [] } else { title },
        )
      } else { ([], prefix, title) },
      align(right, it.page()),
    ))
  }
  set math.equation(numbering: none, supplement: none)
  // Libertinus Math, the companion of the text font (STIX Two Math sets the
  // subscripts of V and W apart, "V i"); STIX supplies the few signs it
  // lacks.
  show math.equation: set text(font: ("Libertinus Math", "STIX Two Math"))
  // A display is set off by about half a line above and below, as printed.
  show math.equation.where(block: true): set block(
    above: 0.85em,
    below: 0.85em,
  )
  // Delimiters keep their size, as in the book, in the text and in
  // displays: a prime or a big sum inside "(M′ⱼ + Mᵢ)" or "(⊕ nᵢPᵢ, S′)"
  // does not enlarge the parentheses (`scaled` where the book enlarges
  // them).
  show math.equation: set math.lr(size: 1em)
  // Subscripts of relations stand at their side, "H ≤_G K", "h ∈_G K",
  // "X ≃_G Y".
  show math.equation: it => {
    show "≤": math.scripts
    show "∈": math.scripts
    show "≃": math.scripts
    // Libertinus Math draws ⇄ (U+21C4) with the left arrow on top, the
    // shape of ⇆; STIX Two Math draws it as printed.
    show "⇄": set text(font: "STIX Two Math")
    // No thin space between "/" and an operator after it, as printed:
    // "P/Rad(P)". The slash is spaced as an opening delimiter, which
    // keeps it tight on both sides.
    show sym.slash: math.class("opening", sym.slash)
    // A parenthesised group with indices directly after an operator,
    // "End_Λ(P)^op": as in TeX, where the index hangs on the closing
    // parenthesis, no thin space comes before the group.
    show math.attach: a => if a.base.func() == math.lr {
      math.class("opening", box(width: 0pt)) + a
    } else { a }
    it
  }
  // Cases in the text are set in the size of a display, as printed.
  show math.equation.where(block: false): it => {
    show math.cases: math.display
    it
  }
  show math.equation.where(block: false): inline-equation
  show math.equation: mod-spacing
  show math.equation.where(block: true): it => {
    if (
      it.has("label")
        and str(it.label).starts-with("eq:")
        and it.numbering == none
    ) {
      numbered-display(it)
    } else { it }
  }
  // A figure caption as printed: "Figure 1." in small capitals, then the
  // text in roman.
  show figure.caption: it => context [#smallcaps[Figure]
    #it.counter.display(it.numbering). #it.body]
  set table(stroke: 0.4pt, inset: (x: 0.4em, y: 0.45em))
  show table: set align(center)
  set table.cell(breakable: false)
  // A table is kept whole on its page, as in the book, with the space of
  // a display above and below it.
  show table: it => block(
    above: 1.1em,
    below: 1.1em,
    breakable: false,
    it,
  )
  show footnote.entry: it => {
    context metadata((
      kind: "footnote-placement",
      marker-page: it.note.location().page(),
      entry-page: it.location().page(),
    ))
    it
  }
  show: reference-rules
  keep-note-runs(body)
}
