#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Definition 2.3.2: a local trivialisation of a principal G-bundle.
#let local-trivialisation = grid-diagram(
  (
    ($U_alpha times G$, $p^(-1) (U_alpha)$),
    ($U_alpha$, $U_alpha$),
  ),
  across: (((label: $phi.alt_alpha$),), ("=",)),
  down: (("->", (label: $p$)),),
  gap: 6mm,
  row: 9mm,
)

// Exercise 1 of Section 2.3: the pullback of two vector bundles over B.
#let whitney-pullback = grid-diagram(
  (($E''$, $E'$), ($E$, $B$)),
  down: (("->", "->"),),
  gap: 6mm,
  row: 9mm,
)
