#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Section 4.6: the two ways of norming from G to ℤ/p × ℤ/p × G agree.
#let norm-square = grid-diagram(
  (
    ($H^* (G, FF_p)$, $H^* (1 times ZZ slash p times G, FF_p)$),
    (
      $H^* (ZZ slash p times 1 times G, FF_p)$,
      $H^* (ZZ slash p times ZZ slash p times G, FF_p)$,
    ),
  ),
  across: (label: $norm$),
  down: (((label: $norm$), (label: $norm$)),),
  gap: 9mm,
  row: 9mm,
)
