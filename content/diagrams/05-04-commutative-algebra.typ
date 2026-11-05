#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The homogeneous affine variety over its projective variety: the rows are
// joined by the relations printed between their objects, the columns by the
// obvious maps.
#let projective-quotient = grid-diagram(
  (
    (
      $max(A) without {0}$,
      $=$,
      $V(I_A) without {0}$,
      $subset.eq$,
      $AA^n (k) without {0}$,
    ),
    ($proj(A)$, $=$, $macron(V)(I_A)$, $subset.eq$, $PP^(n-1) (k).$),
  ),
  across: none,
  down: (("->", none, "->", none, "->"),),
  gap: 4mm,
  row: 12mm,
)
