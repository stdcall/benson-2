#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Section 5.14: the pushout of the projective resolution of R along the
// cocycle ζ̂, with its kernel L_ζ above the first two columns.
#let pushout-sphere = grid-diagram(
  (
    (none, $0$, $0$, none, none, none, none, none),
    (none, $L_zeta$, $L_zeta$, none, none, none, none, none),
    (
      $0$,
      $tilde(Omega)^n R$,
      $P_(n-1)$,
      $P_(n-2)$,
      $dots.c$,
      $P_0$,
      $R$,
      $0$,
    ),
    (
      $0$,
      $R$,
      $P_(n-1) slash L_zeta$,
      $P_(n-2)$,
      $dots.c$,
      $P_0$,
      $R$,
      $0.$,
    ),
    (none, $0$, $0$, none, none, none, none, none),
  ),
  across: (none, "=", "->", "->", none),
  down: (
    (none, "->", "->", none, none, none, none, none),
    (none, "->", "->", none, none, none, none, none),
    (none, (label: $hat(zeta)$), "->", "->", none, "->", "=", none),
    (none, "->", "->", none, none, none, none, none),
  ),
  gap: 7mm,
  row: 9mm,
)

// Section 5.14: the minimal resolution of the trivial module for GL₃(𝔽₂)
// in characteristic two, a double complex of the projective covers of the
// three simple modules k, M, N, its rows and columns periodic of period
// three.
#let gl3-resolution = {
  let pattern = ($P_k$, $P_N$, $P_M$)
  let place(row, column) = pattern.at(calc.rem(row + column, 3))
  let rows = range(4).map(row => (
    ..range(5).map(column => place(row, column)),
    $dots.c$,
  ))
  grid-diagram(
    ((..range(5).map(_ => $dots.v$), none), ..rows),
    across: (none, ..rows.map(_ => "<-")),
    down: range(4).map(_ => (..range(5).map(_ => "->"), none)),
    gap: 8mm,
    row: 7mm,
  )
}

// Section 5.14: the minimal resolution of the trivial module for A₆ in
// characteristic three, as the book sets it: an array of the projective
// covers joined by arrows ← along the rows and ↓ down the columns. Each row
// gives its first column, its entries and whether an arrow leaves its right
// end; `downs` lists for each row the columns of the arrows reaching it from
// above (the first row from the dots).
#let a6-resolution = {
  let (k, L, M, N) = ($P_k$, $P_L$, $P_M$, $P_N$)
  let dots-columns = (4, 5, 6)
  let rows = (
    (3, (M, N, k, k), true),
    (3, (N, N, k, k), true),
    (2, (M, k, k, N, N, k, k), true),
    (2, (N, k, k, N, N, k, k), true),
    (2, (k, N, N, k, k, N, N, k, k), true),
    (2, (k, N, N, k, k, N, N, k, k), true),
    (1, (M, N, k, k, N, N, k, k, N, N), true),
    (1, (N, N, k, k, N, N, k, k, N, L), false),
    (0, (M, k, k, N, N, k, k, N, L), false),
    (0, (N, k, k, N, L), false),
    (0, (k, N, L), false),
  )
  let downs = (
    (4, 5, 6),
    (3, 4, 5, 6),
    (3, 4, 5, 6, 7, 8),
    (2, 3, 4, 5, 6, 7, 8),
    range(2, 11),
    range(2, 11),
    range(2, 11),
    range(1, 11),
    range(1, 9),
    range(0, 5),
    range(0, 3),
  )
  let width = 11
  let cells = ()
  for column in dots-columns {
    cells.push(grid.cell(x: 2 * column, y: 0, $dots.v$))
  }
  for (r, (first, entries, open)) in rows.enumerate() {
    let y = 2 * r + 2
    for column in downs.at(r) {
      cells.push(grid.cell(x: 2 * column, y: y - 1, $arrow.b$))
    }
    for (i, entry) in entries.enumerate() {
      let x = 2 * (first + i)
      cells.push(grid.cell(x: x, y: y, entry))
      if i + 1 < entries.len() or open {
        cells.push(grid.cell(x: x + 1, y: y, $arrow.l$))
      }
    }
  }
  grid(
    columns: 2 * width,
    rows: 1.45em,
    column-gutter: 0.12em,
    align: center + horizon,
    ..cells,
  )
}

// Proof of Lemma 5.14.4: the map of the resolution P ⊗ C_ζ^(∞) to its shift
// by n, through the degree zero part, onto the extension representing ζ.
#let resolution-shift = {
  let term(index) = $(bold(P) times.o bold(C)_zeta^((infinity)))_#index$
  grid-diagram(
    (
      ($dots.c$, term($n$), term($n-1$), $dots.c$, term($0$), $R$, $0$),
      ($dots.c$, term($0$), none, none, none, none, none),
      ($0$, $R$, $P_(n-1) slash L_zeta$, $dots.c$, $P_0$, $R$, $0$),
    ),
    down: (
      (none, "->", none, none, none, none, none),
      (none, "->", none, none, none, none, none),
    ),
    extra: (2, 4, 5).map(x => edge((x, 0), (x, 2), "->")),
    gap: 5mm,
    row: 9mm,
  )
}
