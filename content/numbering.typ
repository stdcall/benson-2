// Chapters are numbered 1–6 and their sections 1.1, 1.2, ...: the native
// heading counter. The numbered statements of a section (definitions,
// lemmas, theorems, propositions, corollaries, questions) share one series,
// restarted at each section and printed with the chapter and the section:
// Theorem 1.1.3. Numbered displays, where the book has them, share the same
// series: (2.8.1). The bibliography is numbered [1], [2], ... through.
#let item-counter = counter("book-item")
#let exercise-counter = counter("book-exercise")
#let bibliography-counter = counter("book-bibliography")
#let case-counter = counter("book-case")
#let case-number-format = state("case-number-format", "(1)")

// The section in force at a location, as (chapter, section); the section is
// 0 in the introduction of a chapter.
#let section-key(location) = {
  let numbers = counter(heading).at(location)
  (numbers.at(0, default: 0), numbers.at(1, default: 0))
}

#let family-counter(family) = if family == "exc" {
  exercise-counter
} else if family == "case" { case-counter } else if family == "bib" {
  bibliography-counter
} else { item-counter }

#let restart-counters(level) = if level in (1, 2) {
  item-counter.update(0)
  exercise-counter.update(0)
}

#let object-number(family, location, tag: none, series: none) = {
  let own = if tag != none { tag } else {
    family-counter(family).at(location).first()
  }
  if family in ("bib", "case", "tag") { (own,) } else {
    (..section-key(location), own)
  }
}

#let numbered-record(target) = {
  if query(target).len() != 1 { return none }
  query(selector(<numbered>).within(target)).at(0, default: none)
}

#let record-number(item) = {
  let value = item.value
  if value.kind in ("hint", "variant") { value.number } else if (
    value.kind == "unnumbered"
  ) {
    none
  } else if value.family == "heading" {
    let numbers = counter(heading).at(item.location())
    numbers.slice(0, value.level)
  } else {
    object-number(
      value.family,
      item.location(),
      tag: value.at("tag", default: none),
    )
  }
}

#let record(family, ..flags) = context [#metadata((
  kind: "numbered",
  family: family,
  ..flags.named(),
  number: object-number(
    family,
    here(),
    tag: flags.named().at("tag", default: none),
  ),
))<numbered>]
