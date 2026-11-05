#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// The double complexes of cyclic homology: three columns under a row of
// vertical dots, continued to the right by dots. `rows` lists the objects of
// the rows from the top; `across` the maps between the columns, the same in
// every row; `down` the maps from each row to the next one below, the same
// in every column pattern (labels on the right of the vertical maps).
#let cyclic-bicomplex(rows, across, down) = grid-diagram(
  (($dots.v$, $dots.v$, $dots.v$, none), ..rows.map(row => (..row, $dots.c$))),
  across: (none, ..rows.map(_ => across)),
  down: rows.map(_ => (..down, none)),
  gap: 8mm,
  row: 9mm,
)

// The double complexes B: columns under a row of vertical dots, each column
// starting one row higher than the one on its left. `rows` lists the
// objects of the rows from the top (`none` for an empty place); the
// horizontal maps are B, the vertical ones b.
#let b-bicomplex(rows) = grid-diagram(
  (($dots.v$, $dots.v$, $dots.v$), ..rows),
  across: (
    none,
    ..rows.map(_ => (
      (style: "<-", label: $B$),
      (style: "<-", label: $B$),
    )),
  ),
  down: rows.map(row => row.map(object => if object == none { none } else {
    (style: "->", label: $b$)
  })),
  gap: 8mm,
  row: 9mm,
)

// The maps of the double complex defining cyclic homology: ε and N between
// the columns, b and −b′ in the columns.
#let homology-across = (
  (style: "<-", label: $epsilon$),
  (style: "<-", label: $N$),
  (style: "<-", label: $epsilon$),
)
#let homology-down = (
  (style: "->", label: $b$),
  (style: "->", label: $-b'$),
  (style: "->", label: $b$),
)

// Proof of Proposition 2.13.1: the double complex CC_*(Λ).
#let connes-bicomplex = cyclic-bicomplex(
  (
    ($Lambda^(times.o 3)$, $Lambda^(times.o 3)$, $Lambda^(times.o 3)$),
    ($Lambda^(times.o 2)$, $Lambda^(times.o 2)$, $Lambda^(times.o 2)$),
    ($Lambda$, $Lambda$, $Lambda$),
  ),
  homology-across,
  homology-down,
)

// Proof of Theorem 2.13.2: the map α_* of the long exact Connes sequences
// of Λ and Γ; the labels α_* on the left of the vertical maps, the
// isomorphisms already known on their right.
#let connes-ladder = {
  let sequence(ring) = (
    $dots.c$,
    $H C_(n-1) (#ring)$,
    $H H_n (#ring)$,
    $H C_n (#ring)$,
    $H C_(n-2) (#ring)$,
    $H H_(n-1) (#ring)$,
    $dots.c$,
  )
  let maps = (
    "->",
    (style: "->", label: $B$),
    (style: "->", label: $I$),
    (style: "->", label: $S$),
    (style: "->", label: $B$),
    "->",
  )
  grid-diagram(
    (sequence($Lambda$), sequence($Gamma$)),
    across: (maps, maps),
    extra: (
      ..range(1, 6).map(x => edge(
        (x, 0),
        (x, 1),
        $alpha_*$,
        "->",
        label-side: right,
      )),
      ..(1, 2, 4, 5).map(x => edge(
        (x, 0),
        (x, 1),
        $tilde.equiv$,
        label-side: left,
        stroke: none,
      )),
    ),
    gap: 4mm,
    row: 12mm,
  )
}

// The double complex B_*(Λ).
#let lambda-b-bicomplex = b-bicomplex((
  ($Lambda^(times.o 3)$, $Lambda^(times.o 2)$, $Lambda$),
  ($Lambda^(times.o 2)$, $Lambda$, none),
  ($Lambda$, none, none),
))

// The double complex of the reduced complex B̄(Λ).
#let reduced-b-bicomplex = b-bicomplex((
  (
    $macron(Lambda)^(times.o 2) times.o Lambda$,
    $macron(Lambda) times.o Lambda$,
    $Lambda$,
  ),
  ($macron(Lambda) times.o Lambda$, $Lambda$, none),
  ($Lambda$, none, none),
))

// The double complex CC^*(Λ) of cyclic cohomology: the duals of the maps
// of CC_*(Λ), upwards in the columns and to the right between them.
#let cohomology-bicomplex = cyclic-bicomplex(
  (
    (
      $(Lambda^(times.o 3))^*$,
      $(Lambda^(times.o 3))^*$,
      $(Lambda^(times.o 3))^*$,
    ),
    (
      $(Lambda^(times.o 2))^*$,
      $(Lambda^(times.o 2))^*$,
      $(Lambda^(times.o 2))^*$,
    ),
    ($Lambda^*$, $Lambda^*$, $Lambda^*$),
  ),
  (
    (style: "->", label: $epsilon$),
    (style: "->", label: $N$),
    (style: "->", label: $epsilon$),
  ),
  (
    (style: "<-", label: $b$),
    (style: "<-", label: $-b'$),
    (style: "<-", label: $b$),
  ),
)
