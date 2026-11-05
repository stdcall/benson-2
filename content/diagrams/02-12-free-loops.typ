#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Proof of Lemma 2.12.1: the map ρ̃ and the map ρ it induces on the
// quotients by G.
#let free-loop-square = grid-diagram(
  (($Y$, $E G times G$), ($Y slash G$, $E G times_G G,$)),
  across: (
    ((style: "->", label: $tilde(rho)$),),
    ((style: "->", label: $rho$),),
  ),
  down: (("->", "->"),),
  gap: 9mm,
  row: 12mm,
)
