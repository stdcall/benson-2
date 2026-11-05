#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Section 1.8: a Kan fibration E → B, the dotted diagonal filling in a map
// from the horn Δ[n, i].
#let kan-fibration = grid-diagram(
  (($Delta[n, i]$, $E$), ($Delta[n]$, $B$)),
  down: (("->", "->"),),
  extra: (edge((0, 1), (1, 0), "..>"),),
  gap: 8mm,
  row: 10mm,
)
