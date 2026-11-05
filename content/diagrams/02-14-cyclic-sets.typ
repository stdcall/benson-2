#import "02-13-cyclic-homology.typ": (
  b-bicomplex, cyclic-bicomplex, homology-across, homology-down,
)
#import "../main-defs.typ": *

// Section 2.14: the double complex CC_*(X; R) of a cyclic set X.
#let cyclic-set-bicomplex = cyclic-bicomplex(
  (
    ($R X_2$, $R X_2$, $R X_2$),
    ($R X_1$, $R X_1$, $R X_1$),
    ($R X_0$, $R X_0$, $R X_0$),
  ),
  homology-across,
  homology-down,
)

// Section 2.14: the double complex B_*(X; R).
#let cyclic-set-b-bicomplex = b-bicomplex((
  ($R X_2$, $R X_1$, $R X_0$),
  ($R X_1$, $R X_0$, none),
  ($R X_0$, none, none),
))
