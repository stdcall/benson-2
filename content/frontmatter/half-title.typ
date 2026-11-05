#import "../main-defs.typ": source

// The half-title: the series, its number and editorial board, and the
// title of the book.
#let half-title() = {
  set page(header: none, footer: none)
  set par(justify: false, first-line-indent: 0pt, leading: 0.45em)
  source(1)
  v(52mm)
  text(size: 9.5pt)[
    CAMBRIDGE STUDIES IN \
    ADVANCED MATHEMATICS 31
  ]
  v(1.5mm)
  text(size: 7.5pt)[
    EDITORIAL BOARD \
    D.J.H. GARLING, W. FULTON, T. TOM DIECK, P. WALTERS
  ]
  v(4mm)
  align(center, text(size: 15pt)[
    REPRESENTATIONS AND \
    COHOMOLOGY II
  ])
  pagebreak()
}
