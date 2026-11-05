#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proof of Proposition 2.4.1: the map θ of total spaces over ρ.
#let bundle-retraction = grid-diagram(
  (($E'$, $E'$), ($B' times I$, $B' times I$)),
  across: (((label: $theta$),), ((label: $rho$),)),
  down: (((label: $p$), (label: $p$)),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Theorem 2.4.6: the bundle ξ as a pullback of the universal
// bundle; the label of the left map stands on its left.
#let classifying-map = grid-diagram(
  (($E$, $E G$), ($B$, $B G$)),
  across: (((label: $tilde(f)$),), ((label: $f$),)),
  down: ((none, (label: $p_G$)),),
  extra: (edge((0, 0), (0, 1), $p$, "->", label-side: right),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Theorem 2.4.6: the map γ of total spaces over the homotopy h.
#let homotopy-cover = grid-diagram(
  (($E(xi) times I$, $E G$), ($B times I$, $B G$)),
  across: (((label: $gamma$),), ((label: $h$),)),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Theorem 2.4.8: the two projections from the product of the total
// spaces and the induced maps of base spaces.
#let projections = grid-diagram(
  (
    ($E(xi)$, $E(xi) times E G$, $E G$),
    ($B(xi)$, $(E(xi) times E G) slash G$, $B G.$),
  ),
  across: (("<-", "->"), ("<-", "->")),
  down: (("->", "->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Theorem 2.4.11 (i): the pullback of the universal bundle along
// the path fibration.
#let path-pullback = grid-diagram(
  (($X$, $E G$), ($P B G$, $B G$)),
  down: (("->", "->"),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Theorem 2.4.11 (i): the diagram of fibrations.
#let path-fibrations = grid-diagram(
  (
    (none, $G$, $G$),
    ($Omega B G$, $X$, $E G$),
    ($Omega B G$, $P B G$, $B G$),
  ),
  across: ((none, "="), "->", "->"),
  down: ((none, "->", "->"), ("=", "->", "->")),
  gap: 6mm,
  row: 9mm,
)
