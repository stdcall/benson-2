#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Section 1.4: the inclusion i of X in the mapping cylinder is f up to the
// homotopy equivalence j.
#let cylinder-square = grid-diagram(
  (($X$, $Y$), ($X$, $M_f$)),
  across: (
    ((style: "->", label: $f$),),
    ((style: "->", label: $i$),),
  ),
  down: (("=", (style: "->", label: $j$)),),
  // The homotopy equivalence j, marked on the other side of its arrow.
  extra: (edge((1, 0), (1, 1), $tilde.eq$, label-side: right, stroke: none),),
  gap: 8mm,
  row: 10mm,
)
