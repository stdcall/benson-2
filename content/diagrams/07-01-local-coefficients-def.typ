#import "common.typ": *

// Definition 7.1.3: a morphism of coefficient systems commutes with the
// restriction maps whenever $x < y$.
#let morphism-square = ladder(
  ($cal(F)(y)$, $cal(G)(y)$),
  ($cal(F)(x)$, $cal(G)(x)$),
  ([], []),
)
