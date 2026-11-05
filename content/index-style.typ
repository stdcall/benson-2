// Index. The entries are those of the printed index. Every entry comes from
// an `#idx(...)` mark placed in the text where the term is introduced or
// used, so the page numbers are those of this edition and follow any
// reflow. A mark's arguments are the entry and its subentries as printed:
// `#idx("radical", "Jacobson")`, `#idx("Auslander", "-Reiten", "quiver")`.
//
// Layout as in the book: two columns; a main entry with its pages, its
// subentries indented under it (and theirs further), a little space before
// each letter. Mathematical entries come first in their letter, then the
// words; signs without a letter (arrows) open the index.
#import "main-defs.typ": *
#import "main-defs.typ" as book-defs
#import "numbering.typ": numbered-record

// Mathematical parts of entry names use the same notation and fonts as
// the text. Outside dollar pairs, names are ordinary literal strings.
#let index-text(value) = {
  let position = 0
  // Literal parts take the typographic apostrophe, as the text does.
  let literal(text) = text.replace("'", "’")
  for part in value.matches(regex("\\$[^$]+\\$")) {
    literal(value.slice(position, part.start))
    eval(part.text, mode: "markup", scope: dictionary(book-defs))
    position = part.end
  }
  literal(value.slice(position))
}

// The letters of a name as it sorts: mathematics without its markup
// (`$tilde(A)_n$` sorts as "An"), words without punctuation, case and a
// parenthetical qualifier.
#let wrappers = regex(
  "\\b("
    + (
      "tilde",
      "hat",
      "bar",
      "bold",
      "cal",
      "frak",
      "upright",
      "scripts",
      "lmodule",
      "op",
      "overline",
      "limits",
      "attach",
      "sym",
      "lt",
      "eq",
      "in",
      "slash",
      "infinity",
      "oo",
    ).join("|")
    + ")\\b",
)
#let letters(value) = {
  // Named signs (`arrow.b`, `arrow.squiggly`) are not letters.
  let text = value.replace(regex("\\$[^$]+\\$"), m => (
    m
      .text
      .replace(regex("[a-z]+(\\.[a-z]+)+"), "")
      .replace(wrappers, "")
      .replace(regex("[^A-Za-z0-9\\p{Greek}]"), "")
  ))
  text = text.replace(regex("\\s*\\([^)]*\\)"), "")
  lower(text.replace(regex("[^\\p{L}\\p{N} ]"), "").trim())
}
#let greek-latin = (
  "α": "a",
  "β": "b",
  "γ": "g",
  "δ": "d",
  "ε": "e",
  "λ": "l",
  "μ": "m",
  "π": "p",
  "ρ": "r",
  "σ": "s",
  "τ": "t",
  "φ": "p",
  "χ": "c",
  "ψ": "p",
  "ω": "o",
  "θ": "t",
  "ξ": "x",
  "ζ": "z",
  "η": "e",
  "ι": "i",
  "κ": "k",
  "ν": "n",
)
// The letter group of an entry: its first letter, a Greek one by its
// Latin initial (Λ under L, Ω under O); none for a sign.
#let initial(name) = {
  let first = letters(name).clusters().at(0, default: none)
  if first == none { return none }
  let latin = greek-latin.at(first, default: first)
  if latin.match(regex("^[a-z]$")) == none { none } else { latin }
}
#let sort-key(path) = {
  let main = path.first()
  let group = initial(main)
  (
    if group == none { "" } else { group },
    if main.starts-with("$") { 0 } else { 1 },
    ..path.map(letters),
  )
}

// The evaluator reads the metadata element's own position after layout;
// no nested context depends on the position of the generated index.
#let locator(location) = box({
  metadata((
    kind: "cross-reference",
    target: "index-mark",
    resolved: true,
    target-position: location.position(),
  ))
  let folio = counter(page).at(location)
  let pattern = location.page-numbering()
  let shown = if pattern == none { str(folio.first()) } else {
    numbering(pattern, ..folio)
  }
  link(location, shown)
})

#let index-entries = context {
  // Only the marks, by their label: querying all metadata would include
  // the locators this index itself adds, and the layout would not settle.
  let marks = query(<index-mark>)
  // Collect the marks of each entry; one locator per page. Every prefix of
  // a path is an entry too (a heading without pages of its own).
  let entries = (:)
  for mark in marks {
    let destination = mark.location()
    if "target" in mark.value {
      let target = label(mark.value.target)
      let record = numbered-record(target)
      if record == none {
        metadata((
          kind: "cross-reference",
          target: mark.value.target,
          resolved: false,
          printed: "?",
          position: here().position(),
        ))
        continue
      }
      destination = record.location()
    }
    let path = mark.value.path
    for depth in range(1, path.len()) {
      let key = path.slice(0, depth).join("\u{1f}")
      if key not in entries {
        entries.insert(key, (path: path.slice(0, depth), at: ()))
      }
    }
    let key = path.join("\u{1f}")
    let record = entries.at(key, default: (path: path, at: ()))
    let number = destination.page()
    if record.at.all(l => l.page() != number) {
      record.at.push(destination)
    }
    entries.insert(key, record)
  }
  let sorted = entries.values().sorted(key: e => sort-key(e.path))
  let group = none
  for (i, entry) in sorted.enumerate() {
    let letter = sort-key(entry.path).first()
    if letter != group {
      if group != none or letter != "" { v(0.9em, weak: true) }
      group = letter
    }
    let depth = entry.path.len() - 1
    let pages = entry.at.sorted(key: loc => loc.page()).map(locator)
    // An entry with subentries stays with its first subentry, not alone at
    // the foot of a column.
    let next = sorted.at(i + 1, default: none)
    block(
      above: 0pt,
      below: 0.25em,
      sticky: next != none and next.path.len() > entry.path.len(),
      par(hanging-indent: 1em, {
        h(depth * 1em)
        index-text(entry.path.last())
        if pages.len() > 0 [, #pages.join([, ])]
      }),
    )
  }
}

#let subject-index = {
  heading(level: 1, numbering: none)[Index]
  set par(first-line-indent: 0pt, justify: false, leading: 0.45em)
  set text(size: 9pt)
  columns(2, gutter: 8mm, index-entries)
}
