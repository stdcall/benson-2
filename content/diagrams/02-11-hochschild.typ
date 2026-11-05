#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Section 2.11, the Dennis trace map: the maps from the group algebras of
// the general linear groups to the matrix rings, and the Morita isomorphisms
// with the Hochschild homology of Λ, printed between the last two columns.
#let matrix-trace = grid-diagram(
  (
    (
      $H H_n (ZZ GL_r (Lambda))$,
      $H H_n (Mat_r (Lambda))$,
      $H H_n (Lambda)$,
    ),
    (
      $H H_n (ZZ GL_(r+1) (Lambda))$,
      $H H_n (Mat_(r+1) (Lambda))$,
      $H H_n (Lambda)$,
    ),
  ),
  across: (("->", none), ("->", none)),
  down: (("->", "->", "="),),
  extra: range(2).map(y => edge(
    (1, y),
    (2, y),
    $tilde.equiv$,
    label-side: center,
    stroke: none,
  )),
  gap: 8mm,
  row: 12mm,
)
