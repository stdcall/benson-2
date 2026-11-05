#import "bibliography-data.typ": bibliography-data, editorial-data

// The Bibliography as printed: "[1] J. F. Adams. _Infinite loop spaces._
// Ann. of Math. Studies 90, Princeton 1978." The works are numbered through,
// in two alphabetical runs: the list of the first edition, [1]–[286], and
// the further references added in the second, [287]–[412]. Every
// description is generated from references.bib.
//
// A description is the names of the authors, a full stop, and the record's
// annotation: the printed text after the names, in which {field} stands for
// a field of the record and {Key.field} for a field of a related component
// (a translation, an erratum). As printed, the title is in italics and the
// rest is roman, the volume of a journal included.
// - The names are those of the authors; a record without authors names its
//   editors, followed by editortype: "C. T. C. Wall, Ed.". A name with a
//   suffix, "Arnold, Jr, J. E.", is printed "J. E. Arnold, Jr"; nameaddon
//   follows the names: "D. Grayson (after D. Quillen)".
// - {journal} prints userb, the journal as the book abbreviates it, where
//   that differs from the verified abbreviation shortjournal; otherwise
//   shortjournal, or the full title journal.
// - {language} prints the language of the cited edition, "Russian".
// - {editor} prints the editors as the authors, "R. Piccinini and
//   D. Sjerve"; {editor|surname} their surnames only, "Aschbacher et al.".
// - usera is the word joining the last two authors where the book does not
//   use "and": "C. Kratzer et J. Thévenaz".
// - userc names the component that a DOI belongs to, "DOI (erratum)".
// `_..._` is italics and `$...$` mathematics in Typst notation, in any
// field; "--" is an en dash and "'" an apostrophe.
#let rich-bib-text(value) = {
  // An abbreviation stays with the number or word after it: "No. 49".
  let value = value
    .replace("'", "’")
    .replace("--", "–")
    .replace(
      regex("\\b(No|no|Ch|Vol|vol|Vols|pp|p|ed)\\. "),
      m => m.text.slice(0, -1) + "\u{00a0}",
    )
  let position = 0
  for match in value.matches(regex("_[^_]+_|\\$[^$]+\\$")) {
    value.slice(position, match.start)
    let part = match.text
    if part.starts-with("_") { emph(part.slice(1, -1)) } else {
      eval(part, mode: "markup")
    }
    position = match.end
  }
  value.slice(position)
}
// "Adams, J. F." is printed "J. F. Adams"; "tom Dieck, T." "T. tom Dieck";
// "Arnold, Jr, J. E." "J. E. Arnold, Jr". Three or more names: "A. Adem,
// J. Maginnis and R. J. Milgram"; "others" at the end: "Aschbacher et al.".
#let print-names(value, conjunction: "and", surname-only: false) = {
  let names = value.split(" and ").map(name => name.trim())
  let others = names.last() == "others"
  if others { names = names.slice(0, -1) }
  let shown = names.map(name => {
    let (surname, ..given) = name.split(", ")
    if surname-only or given.len() == 0 { surname } else if given.len() == 2 {
      given.last() + " " + surname + ", " + given.first()
    } else { given.first() + " " + surname }
  })
  let text = if others { shown.join(", ") + " et\u{00a0}al." } else if (
    shown.len() == 1
  ) { shown.first() } else {
    shown.slice(0, -1).join(", ") + " " + conjunction + " " + shown.last()
  }
  rich-bib-text(text)
}
#let bib-backlinks(target) = context {
  let refs = query(metadata.where(value: (
    kind: "bibliographic-mention",
    target: target,
  ))).filter(mention => {
    let loc = mention.location()
    let enters = query(
      selector(metadata.where(value: (
        kind: "bibliography-boundary",
        enter: true,
      ))).before(loc),
    ).len()
    let exits = query(
      selector(metadata.where(value: (
        kind: "bibliography-boundary",
        enter: false,
      ))).before(loc),
    ).len()
    enters <= exits
  })
  let seen = ()
  let pages = ()
  for mention in refs {
    let loc = mention.location()
    if not seen.contains(loc.page()) {
      seen.push(loc.page())
      let position = loc.position()
      let destination = (
        page: position.page,
        x: position.x,
        y: calc.max(0pt, position.y - 8pt),
      )
      let pattern = loc.page-numbering()
      let folio = counter(page).at(loc)
      let shown = if pattern == none { str(folio.first()) } else {
        numbering(pattern, ..folio)
      }
      pages.push(box({
        metadata((
          kind: "page-reference",
          resolved: true,
          target: "bib-mention:" + target,
          target-position: position,
          // Typst adds 10pt above the coordinate destination as well.
          destination-offset-pt: 18,
          description: shown,
        ))
        link(destination, shown)
      }))
    }
  }
  if pages.len() > 0 { [ #text(size: 9pt)[\[#pages.join(", ")\]]] }
}
#let month-names = (
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
)
#let short-month-names = (
  "Jan.",
  "Feb.",
  "Mar.",
  "Apr.",
  "May",
  "June",
  "July",
  "Aug.",
  "Sept.",
  "Oct.",
  "Nov.",
  "Dec.",
)
// One field of a record, printed as the book prints it. Besides the forms
// above: a month "12" is printed "December", {month|short} "Dec."; an event
// date "1976-03" "March 1976", a range of days in one month
// "1968-06-17/1968-06-28" "June 17–28 1968"; {edition|ordinal} "2nd" with
// the suffix as a superscript in mathematical italics.
#let bib-field(entry, key, field) = {
  let (name, ..form) = field.split("|")
  assert(name in entry, message: "No field " + name + " in " + key)
  let value = entry.at(name)
  let days = value.match(
    regex(
      "^(\d{4})-(\d{2})-(\d{2})/(\d{4})-(\d{2})-(\d{2})$",
    ),
  )
  if name == "title" { emph(rich-bib-text(value)) } else if name == "journal" {
    rich-bib-text(entry.at("userb", default: entry.at(
      "shortjournal",
      default: value,
    )))
  } else if name == "language" {
    upper(value.first()) + value.slice(1)
  } else if (
    name in ("editor", "author")
  ) {
    print-names(value, surname-only: form == ("surname",))
  } else if name == "month" {
    let names = if form == ("short",) { short-month-names } else {
      month-names
    }
    names.at(int(value) - 1)
  } else if (
    name == "eventdate" and value.match(regex("^\d{4}-\d{2}$")) != none
  ) {
    let (year, month) = value.split("-")
    month-names.at(int(month) - 1) + " " + year
  } else if name == "eventdate" and days != none {
    let (y1, m1, d1, y2, m2, d2) = days.captures
    assert(y1 == y2 and m1 == m2, message: "Event dates in " + key)
    (
      month-names.at(int(m1) - 1)
        + " "
        + str(int(d1))
        + "–"
        + str(int(d2))
        + " "
        + y1
    )
  } else if form == ("ordinal",) {
    let n = int(value)
    let suffix = if calc.rem(n, 100) in (11, 12, 13) { "th" } else {
      ("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th").at(calc.rem(
        n,
        10,
      ))
    }
    eval(
      "$" + value + "^(" + suffix.clusters().join(" ") + ")$",
      mode: "markup",
    )
  } else { rich-bib-text(value) }
}
// The heading of the further references added in the second edition, in
// small capitals at the beginning of the text column.
#let bib-part(body) = block(
  above: 1.6em,
  below: 0.9em,
  sticky: true,
  pad(left: 2.75em, smallcaps(body)),
)

// `editorial: true`: a work of editorial.bib, cited in the editorial notes.
#let bib-description(key, editorial: false) = {
  let data = if editorial { editorial-data } else { bibliography-data }
  let entry = data.at(key)
  let related = entry.at("related", default: "").split(",").map(k => k.trim())
  related = related.filter(k => k != "")
  if "author" in entry {
    print-names(entry.author, conjunction: entry.at("usera", default: "and"))
  } else {
    print-names(entry.editor, conjunction: entry.at("usera", default: "and"))
    if "editortype" in entry [, #rich-bib-text(entry.editortype)]
  }
  if "nameaddon" in entry [ #rich-bib-text(entry.nameaddon)]
  [. ]
  let template = entry.annotation
  let position = 0
  for match in template.matches(regex("\\{([^{}]+)\\}")) {
    rich-bib-text(template.slice(position, match.start))
    let token = match.captures.first()
    let (record, record-key, field) = if token.contains(".") {
      let (component, field) = token.split(".")
      assert(
        component in related,
        message: "Template of " + key + " uses an unrelated record",
      )
      (data.at(component), component, field)
    } else { (entry, key, token) }
    bib-field(record, record-key, field)
    position = match.end
  }
  rich-bib-text(template.slice(position))
  // The DOIs of the work and of its related components.
  let dois = ()
  for component in (key,) + related {
    let record = data.at(component)
    if "doi" in record {
      let part = if "userc" in record { " (" + record.userc + ")" } else { "" }
      // A DOI may break after a slash, also before a digit, but not after a
      // hyphen: "90091-" at the end of a line would read as a hyphenated
      // word.
      let shown = record.doi.replace("-", "-\u{2060}").replace("/", "/\u{200b}")
      dois.push(link(
        "https://doi.org/" + record.doi,
        "DOI" + part + ": " + shown,
      ))
    }
  }
  if dois.len() > 0 [ #dois.join("; ")]
  bib-backlinks("bib:" + key)
}
