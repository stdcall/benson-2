#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proof of Theorem 2.10.1: the pushout of f and the inclusion i.
#let plus-pushout = grid-diagram(
  (($(X, x_0)$, $(X^+, x_0)$), ($(Z, z_0)$, $(Z^+, z_0).$)),
  across: (
    ((style: "hook->", label: $i$),),
    ((style: "hook->", label: $i'$),),
  ),
  down: (((label: $f$), (label: $f^+$)),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Proposition 2.10.4 (ii): the long exact sequence of homotopy
// groups of the homotopy fibre F, with its terms identified.
#let fibre-homotopy-sequence = grid-diagram(
  (
    (
      $dots.c$,
      $pi_2 (B GL(Lambda))$,
      $pi_2 (B GL(Lambda)^+)$,
      $GL(Lambda)$,
      $GL(Lambda) slash E(Lambda)$,
      none,
    ),
    (
      none,
      $0$,
      $pi_1 (F)$,
      $pi_1 (B GL(Lambda))$,
      $pi_1 (B GL(Lambda)^+)$,
      $0$,
    ),
  ),
  across: (("->", "->", none, none, none), (none, none, "->", "->", "->")),
  down: ((none, "=", "->", "=", "=", none),),
  gap: 4mm,
  row: 7mm,
)

// Proof of Proposition 2.10.4 (ii): the five term exact sequence of the
// fibration with fibre F'.
#let fibration-five-term = grid-diagram(
  (
    (
      $H_2 (F)$,
      $H_2 (B pi_1 (F))$,
      $H_1 (F')$,
      $H_1 (F)$,
      $H_1 (B pi_1 (F))$,
      $0$,
    ),
    ($0$, none, $0$, $0$, $0$, none),
  ),
  across: ("->", none),
  down: (("=", none, "=", "=", "=", none),),
  gap: 4mm,
  row: 5mm,
)

// Proof of Proposition 2.10.4 (ii): the five term exact sequence of the
// central extension, printed in smaller type to fit the line.
#let extension-five-term = grid-diagram(
  (
    (
      $H_2 (pi_1 (F), ZZ)$,
      $H_2 (E(Lambda), ZZ)$,
      $H_1 (pi_2 (B GL(Lambda)^+), ZZ)$,
      $H_1 (pi_1 (F), ZZ)$,
      $H_1 (E(Lambda), ZZ)$,
    ),
    ($0$, none, $pi_2 (B GL(Lambda)^+)$, $H_1 (F; ZZ) = 0$, none),
  ),
  across: ("->", none),
  down: (("=", none, "=", "=", none),),
  gap: 4mm,
  row: 7mm,
  inset: 0.5mm,
  size: 0.85em,
)

// The composite of two arrows of Q(_Λ Proj), formed by pulling back.
#let pullback-composition = grid-diagram(
  (
    (none, none, $P''$, none, none),
    ($P$, $P'$, none, $Q'$, $R$),
    (none, none, $Q$, none, none),
  ),
  across: (none, ("<-", none, none, "->"), none),
  extra: (
    edge((2, 0), (1, 1), "->"),
    edge((2, 0), (3, 1), "->"),
    edge((1, 1), (2, 2), "->"),
    edge((3, 1), (2, 2), "->"),
  ),
  gap: 6mm,
  row: 6mm,
)
