#import "statements.typ": editorial-bib-item
#import "bibliography-style.typ": bib-description

// The works cited only in the editorial notes, after the Bibliography of the
// book; descriptions are generated from editorial.bib.
#metadata((kind: "bibliography-boundary", enter: true))
#heading(level: 1, numbering: none)[Editorial references]

#editorial-bib-item[
  #bib-description("Eisenbud1995", editorial: true)
] <bib:Eisenbud1995>

#editorial-bib-item[
  #bib-description("May2012", editorial: true)
] <bib:May2012>

#editorial-bib-item[
  #bib-description("McCleary2001", editorial: true)
] <bib:McCleary2001>

#editorial-bib-item[
  #bib-description("TomDieck2008", editorial: true)
] <bib:TomDieck2008>

#editorial-bib-item[
  #bib-description("Weibel1994", editorial: true)
] <bib:Weibel1994>

#metadata((kind: "bibliography-boundary", enter: false))
