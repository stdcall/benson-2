#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Proof of Lemma 4.1.1: the map ψ_(r+1) is constructed as the dotted arrow
// at the left-hand end, from I_1 ⊗ P_r up to degree r + 1 below it.
#let psi-step = grid-diagram(
  (
    (
      $I_1 times.o P_r$,
      $(bold(I) times.o bold(P))_r$,
      $(bold(I) times.o bold(P))_((r-1))$,
    ),
    (
      $(bold(I)^(times.o n) times.o bold(Q)^(times.o n))_(r+1)$,
      $(bold(I)^(times.o n) times.o bold(Q)^(times.o n))_r$,
      $(bold(I)^(times.o n) times.o bold(Q)^(times.o n))_(r-1)$,
    ),
  ),
  across: (
    ((label: $partial$), (label: $partial$)),
    ((label: $partial$), (label: $partial$)),
  ),
  down: (
    (
      "..>",
      (label: $psi_r$),
      (label: $psi_(r-1)$),
    ),
  ),
  gap: 6mm,
  row: 9mm,
)
