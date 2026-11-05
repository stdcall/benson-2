#import "numbering.typ": (
  case-counter, case-number-format, family-counter, item-counter,
  numbered-record, object-number, record, record-number,
)
#import "note-layout.typ": contains-note, keep-note-runs

// The paragraph indent of the book; statement heads, proofs and new
// paragraphs after a display or a block are indented by it.
#let paragraph-indent = 1.1em

// Parenthetical comments retain the author's roman text inside a statement.
#let statement-comment(body) = text(style: "normal", body)

// Preserve a deliberately vacant position in the shared statement series.
#let numbering-gap() = item-counter.step()

#let sequence = [].func()
#let join-pieces(pieces) = sequence(
  pieces
    .map(it => {
      if it.func() == sequence and not it.has("label") { it.children } else {
        (it,)
      }
    })
    .flatten(),
)

// Paragraphs as in the book. Typst indents a paragraph only after another
// paragraph; the book indents every new paragraph, also the first one after
// a heading and one after a display, a list or a statement, while text
// continuing a sentence after a display stays flush left. In the source a
// new paragraph is a blank line: text after a heading or a block and a
// blank line gets the paragraph indent, text after a block without one
// continues the sentence. Applied to every chapter (main.typ) and to the
// bodies of statements and proofs.
#let new-paragraphs(body) = {
  if type(body) != content or body.func() != sequence { return body }
  // A statement is a sequence of a counter update and its block; a styled
  // helper wraps its block.
  let block-like(it) = {
    if it.func() == sequence { return it.children.any(block-like) }
    if it.has("child") { return block-like(it.child) }
    (
      it.func()
        in (
          block,
          enum,
          enum.item,
          list,
          list.item,
          terms,
          terms.item,
          table,
          grid,
          figure,
          place,
          align,
        )
        or (it.func() == math.equation and it.block)
    )
  }
  let context-element = (context none).func()
  let subhead-start(it) = (
    it.func() == sequence
      and it.children.len() > 0
      and it.children.first().func() == metadata
      and it.children.first().value == "subhead"
  )
  let out = ()
  let after-block = false
  let broken = false
  let run = none
  // A subhead with text after it is an ordinary paragraph and may break
  // across pages; a subhead alone stays with what follows.
  let flush-run(run) = block(
    width: 100%,
    above: 1.2em,
    below: 0.6em,
    sticky: run.slice(1).all(it => it.func() in ([ ].func(), parbreak)),
    par(
      first-line-indent: (amount: paragraph-indent, all: true),
      sequence(
        run,
      ),
    ),
  )
  for child in body.children {
    let kind = child.func()
    if run != none {
      if kind != parbreak and not block-like(child) {
        run.push(child)
        continue
      }
      out.push(flush-run(run))
      run = none
      after-block = true
      broken = false
    }
    if subhead-start(child) {
      run = (child,)
      continue
    }
    if kind == heading {
      // The first paragraph after a heading is indented.
      after-block = true
      broken = true
      out.push(child)
      continue
    }
    if block-like(child) {
      after-block = true
      broken = false
    } else if kind == parbreak {
      if after-block { broken = true }
    } else if kind not in ([ ].func(), metadata, context-element, label) {
      if after-block and broken { out.push(h(paragraph-indent)) }
      after-block = false
      broken = false
    }
    out.push(child)
  }
  if run != none { out.push(flush-run(run)) }
  sequence(out)
}

// A statement or a list that begins with a list of parts runs its first
// part on after the head, "Lemma 1.3.3. (i) If M …": the head waits in this
// state for the list (book-style.typ, `run-in-list`).
#let list-lead = state("list-lead", none)
// A statement whose parts begin on a new line after its head, "Proposition
// 3.3.1 (Nakayama relations). / (i) … / (ii) …": `#part-lines[+ … + …]`
// (by default the first part runs on after the head).
#let list-style = state("list-style", "paragraphs")
#let part-lines(body) = {
  list-style.update("lines")
  body
  list-style.update("paragraphs")
}

#let prepend-heading(body, head) = {
  let flatten(it) = {
    if it.func() == sequence and not it.has("label") {
      it.children.map(flatten).flatten()
    } else { (it,) }
  }
  let pieces = flatten(body)
  let invisible = (
    [ ].func(),
    parbreak,
    metadata,
    counter("heading-probe").update(0).func(),
    state("heading-probe", 0).update(0).func(),
  )
  let first = pieces.position(it => it.func() not in invisible)
  if first == none { return join-pieces((head, body)) }
  let opening = pieces.at(first)
  // Markup items `+ …` are `enum.item`s, grouped into a list only at
  // layout.
  if opening.func() in (enum, enum.item) and head != [] {
    return join-pieces((
      ..pieces.slice(0, first),
      list-lead.update(head),
      ..pieces.slice(first),
    ))
  }
  let block-opening = (
    opening.func()
      in (
        block,
        list,
        terms,
        table,
        grid,
        figure,
        heading,
        align,
      )
      or (opening.func() == math.equation and opening.block)
  )
  let lead = if block-opening and head != [] {
    context block(above: 0pt, below: par.leading, sticky: true, head)
  } else { head }
  join-pieces((..pieces.slice(0, first), lead, ..pieces.slice(first)))
}

#let keep-opening-display(body) = {
  if body.func() != sequence { return body }
  let children = body.children
  let first = children.position(it => (
    it.func() == math.equation and it.block
  ))
  if first == none { return body }
  let lead = children.slice(0, first)
  if lead.any(it => (
    it.func() in (parbreak, block, table, list, enum, heading)
  )) {
    return body
  }
  // Only a short opening (about three lines) is kept with its display; a
  // longer one may break across pages like any paragraph.
  // Characters of the lead; a formula counts three times its symbols, as
  // it is wider than its text.
  let text-length(it) = {
    if type(it) == str { return it.len() }
    if type(it) != content { return 0 }
    if it.func() == math.equation { return 3 * text-length(it.body) + 2 }
    if it.has("text") { return text-length(it.text) }
    if it.has("children") {
      return it.children.map(text-length).sum(default: 0)
    }
    if it.has("child") { return text-length(it.child) }
    if it.has("body") { return text-length(it.body) }
    0
  }
  if text-length(sequence(lead)) > 240 { return body }
  join-pieces((
    context block(
      width: 100%,
      above: 0pt,
      below: par.leading,
      sticky: true,
      sequence(lead),
    ),
    ..children.slice(first),
  ))
}

// The end of a proof: an open square at the right margin, on the last line
// of the proof, also on the last line of a closing display.
#let end-mark = box(width: 1fr, align(right, sym.square.stroked))
#let proof-ending = [#sym.wj#h(1em)#end-mark]
#let aligned-math(it) = (
  it.func() in (linebreak, $&$.body.func())
    or (it.has("children") and it.children.any(aligned-math))
    or (
      it.has("body") and type(it.body) == content and aligned-math(it.body)
    )
)
// The last of the aligned lines of a formula.
#let last-row(it) = {
  if it.has("children") {
    let children = it.children
    let breaks = range(children.len()).filter(i => (
      children.at(i).func() == linebreak
    ))
    if breaks.len() > 0 {
      return [].func()(children.slice(breaks.last() + 1))
    }
    for child in children.rev() {
      if aligned-math(child) { return last-row(child) }
    }
  }
  if it.has("body") and type(it.body) == content { return last-row(it.body) }
  it
}
#let with-ending(body, ending) = {
  if body.func() == enum.item {
    let finished = with-ending(body.body, ending)
    if body.at("number", default: none) != none {
      enum.item(body.number, finished)
    } else { enum.item(finished) }
  } else if body.func() == enum {
    let fields = body.fields()
    let children = fields.remove("children")
    let _ = fields.remove("label", default: none)
    let last = children.pop()
    let finished = with-ending(last.body, ending)
    children.push(if last.at("number", default: none) != none {
      enum.item(last.number, finished)
    } else { enum.item(finished) })
    enum(..fields, ..children)
  } else if body.func() == terms.item {
    terms.item(body.term, with-ending(body.description, ending))
  } else if body.func() == terms {
    let fields = body.fields()
    let children = fields.remove("children")
    let _ = fields.remove("label", default: none)
    let last = children.pop()
    children.push(terms.item(last.term, with-ending(last.description, ending)))
    terms(..fields, ..children)
  } else if body.func() == math.equation and body.block {
    // The display keeps its spacing; the square stands at the right margin
    // on the baseline of its last line (below which may hang the limits of
    // a sum or the depth of a fraction).
    // A last line that fills the measure leaves no room: the square then
    // stands below it, at the right margin.
    block(width: 100%, above: 0.85em, below: 0.85em, layout(size => {
      let last = last-row(body.body)
      let line(edge) = {
        measure({
          set text(top-edge: "bounds", bottom-edge: edge)
          math.equation(block: false, math.display(last))
        }).height
      }
      let depth = line("bounds") - line("baseline")
      let room = measure(sym.square.stroked).width + 1.5em.to-absolute()
      let full = measure(body).width
      // The last line of an aligned display shorter than its widest line
      // leaves room at its end.
      let last-width = measure(math.equation(
        block: false,
        math.display(last),
      )).width
      if full + 2 * room > size.width and last-width + room > full {
        body
        block(above: 0.3em, width: 100%, align(right, sym.square.stroked))
      } else if body.at("numbering", default: none) == none {
        // Set as the number of the display, the square stands on the
        // baseline of its last line, above the limits hanging below it.
        [#math.equation(
          block: true,
          numbering: _ => sym.square.stroked,
          number-align: end + bottom,
          body.body,
        )<end-mark-display>]
      } else {
        body
        place(bottom + right, dy: -depth, sym.square.stroked)
      }
    }))
  } else if body.func() == sequence and body.children.len() > 0 {
    let last = body
      .children
      .rev()
      .position(it => (
        it.func()
          not in (
            [ ].func(),
            parbreak,
            metadata,
            state("probe").update(0).func(),
            counter("probe").update(0).func(),
          )
      ))
    if last == none { body + ending } else {
      let index = body.children.len() - last - 1
      sequence((
        ..body.children.slice(0, index),
        with-ending(body.children.at(index), ending),
        ..body.children.slice(index + 1),
      ))
    }
  } else { body + ending }
}

// A statement in the style of the book: the name in small capitals and the
// number, "Theorem 1.1.3", indented like a paragraph; an attribution in
// parentheses, "(Zassenhaus isomorphism theorem)", in roman; the text of a
// theorem, lemma, proposition, corollary, question or definition in italics
// (defined terms bold upright), that of the unnumbered remarks, examples and
// exercises in roman.
#let statement(
  kind,
  family,
  body,
  italic: false,
  title: none,
  numbered: true,
  variant: none,
  note: none,
  suffix: "′",
  closed: false,
  punct: ".",
  head-break: false,
) = {
  if numbered and variant == none { family-counter(family).step() }
  let head = context {
    let base = if variant != none {
      let refs(it) = {
        if it.func() == ref { (it.target,) } else if it.has("children") {
          it.children.map(refs).flatten()
        } else if it.has("body") { refs(it.body) } else { () }
      }
      let targets = refs(variant)
      assert(
        targets.len() == 1,
        message: "A statement variant names its base by one native reference",
      )
      let base = numbered-record(targets.first())
      assert(
        base != none and base.value.kind != "unnumbered",
        message: "A statement variant requires a numbered statement",
      )
      (target: targets.first(), record: base)
    }
    if variant != none {
      [#metadata((
        kind: "variant",
        family: family,
        number: record-number(base.record),
        base: str(base.target),
        suffix: suffix,
      ))<numbered>]
    } else if numbered { record(family) } else {
      [#metadata((
        kind: "unnumbered",
        family: family,
        number: none,
        name: kind,
      ))<numbered>]
    }
    let number = if variant != none {
      record-number(base.record).map(str).join(".") + suffix
    } else if numbered {
      object-number(family, here()).map(str).join(".")
    }
    let name = smallcaps(kind)
    if number != none { name += [ #number] }
    // An author's footnote on the name of the statement.
    if note != none { name += footnote(note) }
    let title-part = if title != none { [ (#title)] } else { [] }
    text(style: "normal", h(paragraph-indent) + name + title-part + punct + [ ])
  }
  // Full width: a block shrinks to its content, which would push a display
  // after only short lines to the left.
  // `closed: true`: a statement printed with the end mark of a proof and
  // no proof after it.
  let body = new-paragraphs(body)
  if closed { body = with-ending(body, proof-ending) }
  block(width: 100%, above: 1em, below: 1em, breakable: true, {
    set text(style: "italic") if italic
    // A defined term in an italic statement is bold upright, as printed.
    show strong: set text(style: "normal") if italic
    // `head-break: true`: the text begins on a new line after the head, as
    // the book prints some statements with a long attribution. The text
    // starts at the paragraph indent.
    if head-break {
      context block(above: 0pt, below: par.leading, sticky: true, head)
      keep-note-runs(prepend-heading(body, h(paragraph-indent)))
    } else {
      // A short opening stays on the page of its first display, as in a
      // proof: "Definition 3.2.2. If" never ends a page alone.
      keep-opening-display(keep-note-runs(prepend-heading(body, head)))
    }
  })
}

#let theorem(
  title: none,
  note: none,
  closed: false,
  head-break: false,
  body,
) = statement(
  "Theorem",
  "th",
  body,
  italic: true,
  title: title,
  note: note,
  closed: closed,
  head-break: head-break,
)
#let lemma(
  title: none,
  note: none,
  closed: false,
  head-break: false,
  body,
) = statement(
  "Lemma",
  "lem",
  body,
  italic: true,
  title: title,
  note: note,
  closed: closed,
  head-break: head-break,
)
#let proposition(
  title: none,
  note: none,
  closed: false,
  head-break: false,
  body,
) = statement(
  "Proposition",
  "prop",
  body,
  italic: true,
  title: title,
  note: note,
  closed: closed,
  head-break: head-break,
)
#let corollary(
  title: none,
  note: none,
  closed: false,
  head-break: false,
  body,
) = statement(
  "Corollary",
  "cor",
  body,
  italic: true,
  title: title,
  note: note,
  closed: closed,
  head-break: head-break,
)
#let question(title: none, body) = statement(
  "Question",
  "qu",
  body,
  italic: true,
  title: title,
)
#let definition(title: none, closed: false, body) = statement(
  "Definition",
  "def",
  body,
  italic: true,
  title: title,
  closed: closed,
)
// A statement numbered after another one, "1.2.3′": names its base by one
// native reference, `variant: [@th:…]`; the series is not advanced.
#let theorem-variant(base, suffix: "′", body) = statement(
  "Theorem",
  "th",
  body,
  italic: true,
  variant: base,
  suffix: suffix,
)
// Unnumbered paragraphs with a head in small capitals: "Remark.",
// "Remarks.", "Example.", "Examples.", "Exercise.", "Exercises.";
// `kind:` gives the printed word.
#let remark(kind: "Remark", title: none, punct: ".", body) = (
  statement(kind, "rem", body, title: title, numbered: false, punct: punct)
)
#let example(kind: "Example", title: none, punct: ".", body) = (
  statement(kind, "exm", body, title: title, numbered: false, punct: punct)
)
#let exercise(kind: "Exercise", title: none, punct: ".", body) = (
  statement(kind, "exc", body, title: title, numbered: false, punct: punct)
)
// An unnumbered heading inside a section, "Representable functors.", in
// small capitals: the text after it in the same paragraph runs on after
// it, as printed; set off by space above and kept with what follows
// (`new-paragraphs`).
#let subhead(body) = [#metadata("subhead")#smallcaps(body).#h(0.6em)]
// "Exercises. 1. … 2. …": a numbered list of exercises after one head.
#let exercises(body) = {
  set enum(numbering: "1.")
  exercise(kind: "Exercises", body)
}
// A proof: "Proof." in small capitals, indented, and the open square at the
// right margin after the last line. `head:` for another head ("Proof of
// Theorem 4.5.8."); `closed: false` when the book prints no square.
#let proof(body, head: smallcaps[Proof], closed: true) = {
  let contents = new-paragraphs(body)
  if closed { contents = with-ending(contents, proof-ending) }
  contents = keep-opening-display(keep-note-runs(prepend-heading(
    contents,
    [#h(paragraph-indent)#head. ],
  )))
  if contains-note(body) {
    // A split enclosing block can defer a note until a later page. Keep
    // note-bearing proofs in the native page flow, with their note runs
    // grouped before layout.
    parbreak()
    contents
    parbreak()
  } else {
    block(width: 100%, above: 1em, below: 1em, breakable: true, contents)
  }
}

// Named cases retain native list numbering. Their separate counter lets
// references follow an inserted case without changing theorem numbers.
#let case-list(numbering: "(1)", ..items) = {
  // Context hides its resulting enum from structural opening detection.
  metadata((kind: "block-opening"))
  context {
    let previous = case-counter.get()
    let previous-format = case-number-format.get()
    case-counter.update(0)
    case-number-format.update(if type(numbering) == str { numbering } else {
      "(1)"
    })
    // Markers upright, also in italic statements, as printed.
    let marker = if type(numbering) == str {
      (..n) => text(style: "normal", std.numbering(numbering, ..n))
    } else { numbering }
    enum(numbering: marker, ..items.pos())
    case-counter.update(previous)
    case-number-format.update(previous-format)
  }
}
#let case(body) = {
  case-counter.step()
  text(context {
    record("case", number-format: case-number-format.get())
    body
  })
}

// `variant: true` marks the display of a `display-variant`: its number
// follows the label of the base display (checked by the lint, T013).
#let tagged-display(body, tag, variant: false) = {
  let natural = measure(math.equation(math.display(body))).width
  let reserve = measure(tag).width + 0.75em.to-absolute()
  layout(size => {
    // Wide displays use the right side of the available line so that
    // the left-hand number remains separate from the mathematical body.
    let alignment = if natural > size.width - 2 * reserve { right } else {
      center
    }
    show math.equation: set align(alignment)
    let display = math.equation(
      block: true,
      numbering: _ => tag,
      number-align: start + horizon,
      body,
    )
    if variant [#display<display-variant>] else { display }
  })
}

// A display numbered after a preceding one, "(9.6a)":
// `#display-variant([@eq:…], suffix: "a", $ … $) <eq:…>`. The series is not
// advanced; the number follows the base display.
#let display-variant(variant, suffix: "a", it) = context {
  let refs(it) = {
    if it.func() == ref { (it.target,) } else if it.has("children") {
      it.children.map(refs).flatten()
    } else if it.has("body") { refs(it.body) } else { () }
  }
  let targets = refs(variant)
  assert(
    targets.len() == 1,
    message: "A display variant names its base by one native reference",
  )
  let base = numbered-record(targets.first())
  assert(
    base != none and base.value.family == "eq",
    message: "A display variant requires a numbered display",
  )
  [#metadata((
    kind: "variant",
    family: "eq",
    number: record-number(base),
    base: str(targets.first()),
    suffix: suffix,
  ))<numbered>]
  let number = record-number(base).map(str).join(".") + suffix
  tagged-display(it.body, [(#number)], variant: true)
}

// A display marked with a symbol instead of a number: the symbol stands at
// the right of its last line, "†", and the text cites it in parentheses,
// "(†)": `#symbol-display("†", $ … $) <eq:…>`; `@eq:…` prints "(†)".
// With `parens: true` the display shows its symbol in parentheses as well,
// "(∗)": `#symbol-display("∗", parens: true, $ … $) <eq:…>`.
#let symbol-display(tag, it, parens: false) = block(
  width: 100%,
  above: 0.85em,
  below: 0.85em,
  context {
    [#metadata((
      kind: "numbered",
      family: "tag",
      tag: tag,
      number: (tag,),
    ))<numbered>]
    let display = math.equation(
      block: true,
      numbering: _ => if parens { "(" + tag + ")" } else { tag },
      number-align: end + bottom,
      it.body,
    )
    [#display<display-variant>]
  },
)

#let numbered-display(it) = {
  family-counter("eq").step()
  context {
    record("eq")
    let number = object-number("eq", here()).map(str).join(".")
    tagged-display(it.body, [(#number)])
  }
}

// An entry of the bibliography: its number in brackets, right aligned in
// the margin column, and the description hanging after it, as printed.
// The descriptions are set ragged right: long titles and DOIs, which
// cannot be broken, would otherwise leave very loose lines.
#let bib-row(number, body) = grid(
  columns: (2.3em, 1fr),
  column-gutter: 0.45em,
  align(right)[[#number]], par(justify: false, body),
)
#let bib-item(body, tag: none) = {
  if tag == none { family-counter("bib").step() }
  block(above: 0.4em, below: 0.4em, breakable: false, context {
    record("bib", tag: tag)
    bib-row(object-number("bib", here(), tag: tag).last(), body)
  })
}
// An entry of the editorial references, the works cited only in the
// editorial notes: numbered [E1], [E2], … and cited the same way.
#let editorial-bib-counter = counter("book-editorial-bibliography")
#let editorial-bib-item(body) = block(
  above: 0.4em,
  below: 0.4em,
  breakable: false,
  {
    editorial-bib-counter.step()
    context {
      let tag = "E" + str(editorial-bib-counter.get().first())
      record("bib", tag: tag)
      bib-row(tag, body)
    }
  },
)
#let bib-group(body) = {
  family-counter("bib").update(0)
  heading(level: 2, numbering: none, outlined: false, body)
}
