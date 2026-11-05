#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The definition of the modules L_ζ: the restriction of the sequence of
// ζ̂ to a subgroup H, with the projective summand P of the restriction of
// Ωⁿk, over the sequence of the restricted class.
#let l-zeta-restriction = grid-diagram(
  (
    (none, $0$, $0$, none, none),
    (none, $P$, $P$, none, none),
    ($0$, $L_zeta down_H$, $Omega^n k plus.o P$, $k$, $0$),
    ($0$, $L_(res_(G, H) (zeta))$, $Omega^n k$, $k$, $0$),
    (none, $0$, $0$, none, none),
  ),
  across: (
    none,
    "=",
    ("->", "->", (label: $hat(zeta) down_H$), "->"),
    ("->", "->", (label: $hat(res_(G, H) (zeta))$), "->"),
    none,
  ),
  down: (
    (none, "->", "->", none, none),
    (none, "->", "->", none, none),
    (none, "->", "->", "=", none),
    (none, "->", "->", none, none),
  ),
  gap: 11mm,
  row: 7mm,
)

// Proof of Lemma 5.9.3: the sequence of L_{ζ₁ζ₂} over the sequence of
// Ωʳ(ζ̂₂), and the maps of both to k.
#let l-zeta-product = grid-diagram(
  (
    (none, none, $0$, $0$, none),
    (
      $0$,
      $Omega^r L_(zeta_2) plus.o ("projective")$,
      $L_(zeta_1 zeta_2) plus.o ("projective")$,
      $L_(zeta_1)$,
      $0$,
    ),
    (
      $0$,
      $Omega^r L_(zeta_2) plus.o ("projective")$,
      $Omega^(r+s) k plus.o ("projective")$,
      $Omega^r k$,
      $0$,
    ),
    (none, none, $k$, $k$, none),
    (none, none, $0$, $0$, none),
  ),
  across: (
    none,
    "->",
    ("->", "->", (label: $Omega^r (hat(zeta)_2)$), "->"),
    "=",
    none,
  ),
  down: (
    (none, none, "->", "->", none),
    (none, "=", "->", "->", none),
    (none, none, (label: $hat(zeta_1 zeta_2)$), (label: $hat(zeta)_1$), none),
    (none, none, "->", "->", none),
  ),
  gap: 7mm,
  row: 7mm,
)

// Proof of Lemma 5.9.4: the sequence of ζ̂ mapped into the (n − 1)st
// projective module of the minimal resolution.
#let l-zeta-snake = grid-diagram(
  (
    ($0$, $L_zeta$, $Omega^n k$, $k$, $0$),
    ($0$, $P_(n-1)$, $P_(n-1)$, $0$, $0$),
  ),
  across: (("->", "->", (label: $hat(zeta)$), "->"), "->"),
  down: ((none, "->", "->", "->", none),),
  gap: 7mm,
  row: 9mm,
)

// Proof of Proposition 5.9.5: tensoring with M, in degree n and after
// dimension shifting to degree one. The label "⊗M" is set close, as printed.
#let tensor-ext-square = {
  let tensor = (label: $class("unary", times.o) M$)
  grid-diagram(
    (
      ($Ext^n_(k G) (k, k)$, $Ext^n_(k G) (M, M)$),
      ($Ext^1_(k G) (Omega^(n-1) k, k)$, $Ext^1_(k G) (Omega^(n-1) M, M)$),
    ),
    across: (tensor, tensor),
    down: (((label: $tilde.equiv$), (label: $tilde.equiv$)),),
    gap: 7mm,
    row: 9mm,
  )
}
