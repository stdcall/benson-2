#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proposition 5.17.2: the complex C_ζ mapped to its dual.
#let dual-truncation = grid-diagram(
  (
    (
      $0$,
      $P_(n-1) slash L_zeta$,
      $P_(n-2)$,
      $dots.c$,
      $P_1$,
      $P_0$,
      $0$,
    ),
    (
      $0$,
      $P_0^*$,
      $P_1^*$,
      $dots.c$,
      $P_(n-2)^*$,
      $(P_(n-1) slash L_zeta)^*$,
      $0$,
    ),
  ),
  down: ((none, "->", "->", none, "->", "->", none),),
  gap: 5mm,
  row: 10mm,
)

// Proof of Proposition 5.17.2: the resolution of Ω^n k tensored with the
// dual of ζ̂, and the dual resolution below it.
#let dual-cocycle-diagram = {
  let dual = $Omega^(-n) k$
  let tensor = $hat(zeta)^* times.o 1$
  grid-diagram(
    (
      ($0$, $Omega^n k$, $P_(n-1)$, $dots.c$, $P_0$, $k$, $0$),
      (
        $0$,
        $dual times.o Omega^n k$,
        $dual times.o P_(n-1)$,
        $dots.c$,
        $dual times.o P_0$,
        dual,
        $0$,
      ),
      ($0$, $k$, $P_0^*$, $dots.c$, $P_(n-1)^*$, dual, $0.$),
    ),
    down: (
      (
        none,
        (label: tensor),
        (label: tensor),
        none,
        (label: tensor),
        (label: $hat(zeta)^*$),
        none,
      ),
      (none, (label: $gamma$), "->", none, "->", "=", none),
    ),
    gap: 5mm,
    row: 9mm,
  )
}

// Proof of Proposition 5.17.2: the quotient of the top row and the
// subcomplex of the bottom row, the left-hand map a sign.
#let dual-quotient = grid-diagram(
  (
    (
      $0$,
      $k$,
      $P_(n-1) slash L_zeta$,
      $P_(n-2)$,
      $dots.c$,
      $P_1$,
      $P_0$,
      $k$,
      $0$,
    ),
    (
      $0$,
      $k$,
      $P_0^*$,
      $P_1^*$,
      $dots.c$,
      $P_(n-2)^*$,
      $(P_(n-1) slash L_zeta)^*$,
      $k$,
      $0$,
    ),
  ),
  down: ((none, none, "->", "->", none, "->", "->", "=", none),),
  extra: (
    edge((1, 0), (1, 1), $(-1)^(n(n+1) slash 2)$, "->", label-side: right),
  ),
  gap: 4mm,
  row: 10mm,
)
