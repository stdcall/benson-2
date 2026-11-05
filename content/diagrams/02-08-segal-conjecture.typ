#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// The composite of two basis elements ζ: the transfers upwards, the maps
// induced by homomorphisms to the right.
#let mackey-composite = grid-diagram(
  (
    (
      $B((phi.alt')^(-1) (K' inter lconj(x, H')))$,
      none,
      none,
      none,
      none,
    ),
    ($B H''$, none, $B(K' inter lconj(x, H'))$, $B H'$, none),
    ($B G''$, none, $B K'$, $B G'$, $B G$),
  ),
  across: (
    none,
    (none, none, (label: $B(i' compose c_(x^(-1)))$), none),
    (none, none, (label: $B(i')$), none),
  ),
  down: (
    ((style: "<-", label: $Tr$), none, none, none, none),
    (
      (style: "<-", label: $Tr$),
      none,
      (style: "<-", label: $Tr$),
      (style: "<-", label: $Tr$),
      none,
    ),
  ),
  extra: (
    edge((0, 0), (2, 1), $B(phi.alt')$, "->", label-side: left),
    edge((0, 1), (2, 2), $B(phi.alt')$, "->", label-side: left),
    edge((3, 1), (4, 2), $B(phi.alt)$, "->", label-side: left),
  ),
  gap: 8mm,
  row: 10mm,
)
