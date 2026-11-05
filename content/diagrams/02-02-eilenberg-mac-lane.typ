#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Proof of Theorem 2.2.2: the end of the homotopy exact sequence of the pair
// (X², X¹), with π₁(X¹, x₀) identified with F.
#let skeleton-sequence = grid-diagram(
  (
    (
      $dots.c$,
      $pi_2 (X^2, X^1, x_0)$,
      $pi_1 (X^1, x_0)$,
      $pi_1 (X^2, x_0)$,
      $0.$,
    ),
    (none, none, $F$, none, none),
  ),
  across: ("->", none),
  down: ((none, none, "=", none, none),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Theorem 2.2.2: the fundamental groups of the coverings of X¹ and
// X² with fibre F/R mapping to those of X¹ and X².
#let covering-groups = grid-diagram(
  (
    ($R$, $pi_1 (tilde(X)^1, x_0)$, $pi_1 (tilde(X)^2, x_0)$, $0$),
    ($F$, $pi_1 (X^1, x_0)$, $pi_1 (X^2, x_0)$, $0$),
    (none, none, $F slash R$, none),
  ),
  across: (("=", "->", "->"), ("=", "->", "->"), none),
  down: ((none, "->", "->", none), (none, none, "->", none)),
  gap: 6mm,
  row: 9mm,
)
