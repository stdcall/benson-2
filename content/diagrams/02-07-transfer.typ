#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The principal Σ_n-bundle of ordered fibres as a pullback of the universal
// bundle.
#let ordered-fibres = grid-diagram(
  (($macron(X)$, $E Sigma_n$), ($B$, $B Sigma_n.$)),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// The bundle ξ as a pullback of the universal bundle along f.
#let classifying-square = grid-diagram(
  (($E$, $E G$), ($B$, $B G.$)),
  across: ("->", ((label: $f$),)),
  down: (((label: $p$), "->"),),
  gap: 9mm,
  row: 9mm,
)

// Naturality of the transfer: a pullback of fibrations.
#let transfer-naturality = grid-diagram(
  (($X'$, $X$), ($B'$, $B$)),
  across: (((label: $mu$),), ((label: $lambda$),)),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Proposition 2.7.4: the fibre over a point.
#let fibre-square = grid-diagram(
  (($F$, $X$), ($*$, $B$)),
  down: (("->", (label: $p_F$)),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Proposition 2.7.4: the graph of the projection.
#let graph-square = grid-diagram(
  (($X$, $B times X$), ($B$, $B times B$)),
  across: (((label: $(p_F, 1)$),), ((label: $Delta$),)),
  down: (((label: $p_F$), (label: $1 times p_F$)),),
  gap: 9mm,
  row: 9mm,
)
