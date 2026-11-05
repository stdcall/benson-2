#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Definition 2.15.1: the pushout defining the extended centraliser; just
// above the top map, the generator 1 of ℤ and its image g. The vertical maps
// span two rows, so that the top line stands close to the square.
#let extended-pushout = grid-diagram(
  (($1$, $g$), ($ZZ$, $C_G (g)$), (none, none), ($RR$, $hat(C)_G (g).$)),
  across: (none, "->", none, "->"),
  extra: (
    edge((0, 0), (1, 0), $|->$, label-side: center, stroke: none),
    edge((0, 1), (0, 3), "->"),
    edge((1, 1), (1, 3), "->"),
  ),
  gap: 9mm,
  row: 5mm,
)
