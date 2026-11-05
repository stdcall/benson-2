#import "common.typ": edge, grid-diagram, ladder
#import "../main-defs.typ": *

// Section 1.3: the long exact sequence of the triple
// (I^(n+1), İ^(n+1), C^n), whose outer terms vanish, and the isomorphism
// j_* from H_n(I^n, İ^n), by which the generators are chosen inductively.
#let generator-choice = grid-diagram(
  (
    (
      $H_(n+1) (I^(n+1), C^n)$,
      $H_(n+1) (I^(n+1), dot(I)^(n+1))$,
      $H_n (dot(I)^(n+1), C^n)$,
      $H_n (I^(n+1), C^n)$,
    ),
    ($0$, none, $H_n (I^n, dot(I)^n)$, $0$),
  ),
  across: (("->", (style: "->", label: $partial_*$), "->"), none),
  down: (("=", none, (style: "<-", label: $j_*$), "="),),
  // The name of the isomorphism on the other side of j_*.
  extra: (
    edge((2, 0), (2, 1), $tilde.equiv$, label-side: right, stroke: none),
  ),
  row: 7mm,
)

// Theorem 1.3.2: the Hurewicz maps from the long exact homotopy sequence of
// a based pair to its long exact homology sequence.
#let hurewicz-ladder = ladder(
  (
    $dots.c$,
    $pi_(n+1) (X, A, x_0)$,
    $pi_n (A, x_0)$,
    $pi_n (X, x_0)$,
    $pi_n (X, A, x_0)$,
    $dots.c$,
  ),
  ($dots.c$, $H_(n+1) (X, A)$, $H_n (A)$, $H_n (X)$, $H_n (X, A)$, $dots.c$),
  (none, $h_(n+1)$, $h_n$, $h_n$, $h_n$, none),
  down-side: right,
  gap: 3mm,
)
