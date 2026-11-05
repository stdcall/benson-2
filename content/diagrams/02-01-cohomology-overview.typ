#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The product structure on cohomology given by Yoneda composition: the
// products of cohomology groups are those of Ext groups.
#let yoneda-product = grid-diagram(
  (
    ($H^m (G, R) times H^n (G, R)$, $H^(m+n) (G, R)$),
    (
      $Ext^m_(R G) (R, R) times Ext^n_(R G) (R, R)$,
      $Ext^(m+n)_(R G) (R, R).$,
    ),
  ),
  down: (("=", "="),),
  gap: 8mm,
  row: 12mm,
)
