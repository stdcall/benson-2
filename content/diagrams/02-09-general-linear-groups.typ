#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The fixed points of φ as a pullback of the diagonal.
#let fixed-points = grid-diagram(
  (($X^phi.alt$, $X$), ($X$, $X times X$)),
  across: ("->", ((label: $(1, phi.alt)$),)),
  down: (("->", (label: $Delta$)),),
  gap: 9mm,
  row: 9mm,
)

// The homotopy fixed points of φ as a pullback of the path fibration.
#let homotopy-fixed-points = grid-diagram(
  (($X^(h phi.alt)$, $X^I$), ($X$, $X times X$)),
  across: ("->", ((label: $(1, phi.alt)$),)),
  down: (("->", (label: $tilde(Delta)$)),),
  gap: 9mm,
  row: 9mm,
)

// The homotopy fixed points as the homotopy fibre of 1 − φ.
#let homotopy-fibre = grid-diagram(
  (($X^(h phi.alt)$, $X^I$, $P X$), ($X$, $X times X$, $X$)),
  across: ("->", ((label: $(1, phi.alt)$), (label: $d$))),
  down: (("->", (label: $tilde(Delta)$), "->"),),
  gap: 9mm,
  row: 9mm,
)

// The addition on the space of paths P_{1−φ} over the addition on X.
#let path-addition = grid-diagram(
  (
    ($P_(1 - phi.alt) times P_(1 - phi.alt)$, $P_(1 - phi.alt)$),
    ($X times X$, $X$),
  ),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Lemma 2.9.1: lifting a homotopy to the fibration.
#let homotopy-lifting = grid-diagram(
  (($Y times 0$, $X^(h phi.alt)$), ($Y times I$, $X$)),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// The map from the representation ring to reduced K-theory.
#let reduced-k-theory = grid-diagram(
  (
    ($cal(R)(CC G)$, $K^0 (B G)$, $=$, $[B G; B U times ZZ]$),
    (none, $tilde(K)^0 (B G)$, $=$, $[B G; B U]$),
  ),
  across: (("->", none, none), none),
  down: ((none, "->", none, none),),
  gap: 6mm,
  row: 9mm,
)

// The pullback square to which the Eilenberg–Moore spectral sequence is
// applied.
#let brauer-pullback = grid-diagram(
  (($F psi^q$, $B U^I$), ($B U$, $B U times B U$)),
  across: ("->", ((label: $(1, psi^q)$),)),
  down: (("->", (label: $tilde(Delta)$)),),
  gap: 9mm,
  row: 9mm,
)
