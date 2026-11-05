#import "numbering.typ": numbered-record, record-number

#let editorial-notes = sys.inputs.at("editorial-notes", default: "on") != "off"

// Page anchors of the printed edition: `n` is the page of the source file,
// the folio is that of the printed book (twelve preliminary pages i–xii,
// then the arabic series).
#let source(n, printed: none) = context {
  let front = (
    "i",
    "ii",
    "iii",
    "iv",
    "v",
    "vi",
    "vii",
    "viii",
    "ix",
    "x",
    "xi",
    "xii",
  )
  let folio = if printed != none { str(printed) } else if n <= 12 {
    front.at(n - 1)
  } else { str(n - 12) }
  metadata((
    kind: "source",
    file-page: n,
    printed-page: folio,
    position: here().position(),
  ))
}

#let number-text(body) = text(weight: "semibold", style: "normal", body)

// A reference names its target by a native label. A supplement in
// parentheses, such as `@th:flat[(iv)]`, is a part of the cited statement
// and is printed inside its number: (2.21(iv)). Any other supplement is a
// descriptive reference and is printed as given.
// A part "(iv)", a range of parts "(i)–(iv)" or two parts "(ii), (iii)".
#let part-pattern = regex(
  "^\(([ivxl]+|[a-z]|[0-9]+)\)((–|, ?)\(([ivxl]+|[a-z]|[0-9]+)\))?$",
)
#let plain-text(body) = {
  if type(body) == str { return body }
  if type(body) != content { return "" }
  if body.has("text") { return body.text }
  if body.has("children") { return body.children.map(plain-text).join() }
  if body.has("child") { return plain-text(body.child) }
  if body.has("body") { return plain-text(body.body) }
  ""
}

#let reference-body(it, caption) = context {
  let target = str(it.target)
  let prefix = target.split(":").first()
  if prefix == "bib" {
    metadata((kind: "bibliographic-mention", target: target))
  }
  let supplement = if caption { plain-text(it.supplement).trim() } else { "" }
  // `@th:…[(iv)]`: a part of the cited statement, "Theorem 4.5.8 (iv)".
  let part = if caption and supplement.match(part-pattern) != none {
    supplement
  }
  // A figure is cited by its own counter: "Figure 1".
  if it.element != none and it.element.func() == figure {
    let n = it.element.counter.at(it.element.location())
    return link(
      it.element.location(),
      number-text(numbering(it.element.numbering, ..n)),
    )
  }
  // `page~@…[page]` also cites an object without a number, such as a
  // picture in a display: "the pictures on page 96".
  if (
    caption
      and supplement == "page"
      and it.element != none
      and numbered-record(it.target) == none
  ) {
    let place = it.element.location()
    let printed = str(counter(page).at(place).first())
    let record = metadata((
      kind: "cross-reference",
      target: target,
      resolved: true,
      printed: printed,
      position: here().position(),
      target-position: place.position(),
    ))
    return record + link(place, printed)
  }
  let item = if it.element != none { numbered-record(it.target) }
  let number = if item != none { record-number(item) }
  let unnumbered = item != none and item.value.kind == "unnumbered"
  let pending = item == none
  let printed = if pending { "?" } else if unnumbered {
    item.value.name
  } else if prefix == "case" {
    let format = item.value.at("number-format", default: "(1)")
    numbering(format.trim(".", at: end, repeat: false), ..number)
  } else if prefix == "bib" {
    str(number.last())
  } else {
    number.map(str).join(".") + item.value.at("suffix", default: "")
  }
  // A numbered display is cited with its parentheses, "(2.8.1)"; every
  // other object by its number, the word before it typed in the text:
  // `Theorem~@th:…` prints "Theorem 1.1.3".
  let body = if caption and part == none and supplement != "page" {
    it.supplement
  } else if unnumbered {
    printed
  } else if prefix == "eq" {
    [(#number-text(printed)#if part != none { it.supplement })]
  } else if part != none {
    [#number-text(printed)~#it.supplement]
  } else { number-text(printed) }
  let destination = if pending { none } else if (
    it.element.func() == math.equation
  ) {
    it.element.location()
  } else { item.location() }
  // `page~@…[page]` gives the page of the object in this edition, as in
  // "see page 55".
  if caption and supplement == "page" and not pending {
    body = str(counter(page).at(destination).first())
  }
  metadata((
    kind: "cross-reference",
    target: target,
    resolved: not pending,
    printed: printed,
    position: here().position(),
    target-position: if not pending { destination.position() },
  ))
  if pending { body } else { link(destination, body) }
}

#let reference-rules(body) = {
  show ref: it => {
    let caption = it.supplement not in (auto, none, [])
    // The text font also inside a formula ("by (9.12)" in a chain of
    // equalities), so that the number is semibold as everywhere else.
    let shown = text(font: "Libertinus Serif", reference-body(it, caption))
    // A reference stays on one line: a number, also with a part "(2.8(i))"
    // or a name "Theorem 2.6", and a descriptive one ("Nakayama's Lemma").
    // The box also fixes the position recorded by `reference-body`: an
    // unboxed one in a short paragraph kept with the next display does not
    // converge.
    box(shown)
  }
  body
}

#let idx(target: none, ..path) = {
  assert(path.named().len() == 0 and path.pos().len() > 0)
  let refs(body) = {
    if body.func() == ref { (body.target,) } else if body.has("children") {
      body.children.map(refs).flatten()
    } else if body.has("body") { refs(body.body) } else { () }
  }
  let destination = if target == none { () } else { refs(target) }
  assert(
    target == none or destination.len() == 1,
    message: "An index target must contain one native reference",
  )
  let value = (kind: "index-mark", path: path.pos())
  if target != none { value.insert("target", str(destination.first())) }
  [#metadata(value)<index-mark>]
}

#let editorial-note-counter = counter("editorial-note")
#let ed-note(body) = if editorial-notes {
  // The marker lets `contains-note` see the note inside the context below:
  // a paragraph with a note is kept on the page of its footnote.
  metadata("editorial-note")
  editorial-note-counter.step()
  context {
    let mark = "*" + str(editorial-note-counter.get().first())
    footnote(numbering: _ => mark)[#body~—~_Ed._]
    counter(footnote).update(n => n - 1)
  }
}

// Operators and names of the book: text operators in roman type, with
// their indices at the side. A thin space separates an argument without
// parentheses, "Rad g(S₀)", "Ker α"; none comes before parentheses. The
// quotient slash and parenthesised groups with indices are spaced in the
// book style, so "Rad(P)/Rad²(P)" and "End_Λ(P)^op" stay tight.
#let name(word) = math.op(word)
// Galois fields, written GF(q) in the list of corrections.
#let GF = name("GF")
#let Hom = name("Hom")
#let Map = name("Map")
#let Princ = name("Princ")
#let Diff = name("Diff")
#let Sing = name("Sing")
// Kan's functor Ex, in italics as printed: $Ex^infinity$.
#let Ex = math.italic("Ex")
#let End = name("End")
#let Aut = name("Aut")
#let Ext = name("Ext")
#let Tor = name("Tor")
#let Ker = name("Ker")
#let Coker = name("Coker")
#let Im = name("Im")
#let Rad = name("Rad")
#let Soc = name("Soc")
#let Tr = name("Tr")
#let Res = name("Res")
#let Ind = name("Ind")
#let Inf = name("Inf")
#let rank = name("rank")
#let Mat = name("Mat")
#let res = name("res")
#let grad = name("grad")
// The Evens norm map and the transfer written in lower case, as printed:
// `norm_(H, G)`, `tr_(H, G)`. The book has no norm bars ‖x‖, so `norm`
// replaces Typst's `math.norm` here.
#let norm = name("norm")
#let tr = name("tr")
// Steenrod squares, in italics as printed: `Sq^i`.
#let Sq = math.class("normal", $S q$)
// Chapter 5 prints these in lower case: `coker`, `spec`, `proj`.
#let coker = name("coker")
#let spec = name("spec")
#let proj = name("proj")
// The Chern map of Connes and Karoubi: `Ch_(n,r)`.
#let Ch = name("Ch")
#let Id = name("Id")
#let Stab = name("Stab")
#let Link = name("Link")
// The symplectic group and the Steinberg module, letters of the formula
// like GL: `Sp_(2n) (FF_q)`, `St_p (G)`.
#let Sp = math.class("normal", $S p$)
#let St = math.class("normal", $S t$)
// The total complex, set close to a filtration before it as printed,
// "F^p Tot(E_0)": a letter of the formula, not an operator with spacing.
#let Tot = math.class("normal", $upright(T o t)$)
// Left primes of the two filtrations of a double complex: `lprime(E)_0`,
// `ldprime(E)_0` print ′E₀, ″E₀.
#let lprime(body) = math.attach(body, tl: sym.prime)
#let ldprime(body) = math.attach(body, tl: sym.prime.double)
// Restriction, induction and co-induction of modules, with their subscript
// and superscript at the side of the arrow: `M down_H`, `N up^G`, `N Up^G`.
#let down = math.scripts(sym.arrow.b)
#let up = math.scripts(sym.arrow.t)
#let Up = math.scripts(sym.arrow.t.double)
// Tensor induction, a small tensor sign with an up arrow through it, its
// index at the usual height: `M tensorup^G`.
#let tensorup = math.accent(
  text(size: 0.8em, sym.times.o),
  sym.arrow.t,
)
#let Nat = name("Nat")
#let Aus = name("Aus")
#let Irr = name("Irr")
#let ind = name("ind")
#let Triv = name("Triv")
#let Syl = name("Syl")
#let Gal = name("Gal")
#let Br = name("Br")
#let diag = name("diag")
#let Uni = name("Uni")
// The inverse limit, "lim" with a left arrow under it; an index goes under
// both: `invlim_n`.
// The index stands under the arrow also in running text, as printed.
#let invlim = math.limits(
  math.op(
    math.attach(math.limits(math.upright("lim")), b: sym.arrow.l.long),
    limits: true,
  ),
  inline: true,
)
// The direct limit, "lim" with a right arrow under it: `dirlim_m`.
#let dirlim = math.limits(
  math.op(
    math.attach(math.limits(math.upright("lim")), b: sym.arrow.r.long),
    limits: true,
  ),
  inline: true,
)
// The groups are letters of the formula, so that "BGL(Λ)" is set tight:
// a word of text would take a space after "B".
#let GL = math.class("normal", $G L$)
#let SL = math.class("normal", $S L$)
#let PGL = math.class("normal", $P G L$)
// Operators written before their argument without parentheses keep a thin
// space after them: "char k", "inf".
#let char = math.op("char")
#let inf = math.op("inf")
// Delimiters that grow with their contents, where the book prints them
// so (all others keep their size, as printed): `scaled((a/b))`.
#let scaled(body) = math.lr(body, size: 100%)
// A table of cases in running text whose first row stands on the line of
// the text before it, as printed: "(i) V(M) = P¹ if …, P² if …" (Theorem
// 5.13.1); `cases` would centre the table on that line.
#let topcases(..rows) = context {
  let all = math.equation(math.cases(delim: none, ..rows.pos()))
  let one = math.equation(math.cases(delim: none, rows.pos().first()))
  let shift = (measure(all).height - measure(one).height) / 2
  box(baseline: shift, all)
}
// A display formula in a frame, as printed: `$ boxed(a = b) $`.
#let boxed(body) = box(
  stroke: 0.45pt,
  inset: (x: 0.6em, y: 0.5em),
  math.equation(math.display(body)),
)
// The opposite ring, in the roman type of the book: $Lambda^op$. A name
// missing here is written `name("…")`.
#let op = math.upright("op")
// Upright bold letters and words, as the categories Set, Ab are printed.
#let bold(body) = math.upright(math.bold(body))
// A module written with its ring on the left: ${}_Lambda M$.
#let lmodule(ring, module) = math.attach(module, bl: ring)
// The works inside a cited range, "[101]–[105]": invisible mentions for
// the page lists of the bibliography.
#let bib-mentions(..keys) = for key in keys.pos() {
  metadata((kind: "bibliographic-mention", target: str(key)))
}

// Aligned lines of a display given as pairs (left side, right side), for a
// line too long for the source with the formatter's alignment:
// `$ #aligned-rows(($A$, $= B$), ($$, $= C$)) $`.
#let aligned-rows(..rows) = {
  rows.pos().map(((left, right)) => $#left & #right$.body).join(linebreak())
}

// The signature closing the Introduction, at the right margin.
#let signature(body) = block(width: 100%, above: 1em, align(right, body))

// Left conjugation, as in the book: $lconj(g, h) = g h g^(-1)$.
#let lconj(g, x) = math.attach(x, tl: g)

// The names of the typesetting systems in the Introduction, in the form of
// their logos.
#let LaTeX = box[L#h(-0.32em)#text(size: 0.72em, baseline: -0.24em)[A]#h(
    -0.12em,
  )T#h(-0.14em)#text(baseline: 0.22em)[E]#h(-0.11em)X]
#let AMS = box($cal(A) #h(-0.08em) cal(M) #h(-0.08em) cal(S)$)
#let XYpic = box[X#h(-0.12em)#text(size: 0.85em, baseline: 0.1em)[Y]-pic]

#let editorial-bibliography = context if (
  editorial-notes and query(cite).len() > 0
) {
  bibliography("../editorial.bib", title: [Editorial references])
}
