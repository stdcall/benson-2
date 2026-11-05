#import "common.typ": cd, edge, grid-diagram, node
#import "../main-defs.typ": *

// Definition 3.4.1: the groups E_0^(ij) of a double complex for
// i, j = 0, 1, 2, the differentials d_0 up the columns and d_1 along the
// rows; the columns go on upwards and the rows to the right.
#let double-complex = {
  let n = 3
  let items = ()
  for i in range(n) {
    items.push(node((i, 0), $dots.v$))
    for j in range(n) {
      let place = (i, n - j)
      items.push(node(place, $E_0^#(str(i) + str(j))$))
      items.push(edge(place, (i, n - j - 1), $d_0$, "->", label-side: right))
      items.push(edge(
        place,
        (i + 1, n - j),
        if i < n - 1 { $d_1$ },
        "->",
        label-side: left,
      ))
    }
  }
  for j in range(n) { items.push(node((n, n - j), $dots.c$)) }
  cd(spacing: (8mm, 9mm), ..items)
}

// Section 3.4: the short exact sequence of complexes
// 0 -> F^(p+1) X -> F^p X -> F^p X / F^(p+1) X -> 0 in the degrees p + q and
// p + q + 1, the rows being the three complexes.
#let layer-sequence = grid-diagram(
  (
    (none, $0$, $0$, none),
    (
      $dots.c$,
      $E_0^(p+1,q-1) plus.o dots.c$,
      $E_0^(p+1,q) plus.o dots.c$,
      $dots.c$,
    ),
    (
      $dots.c$,
      $E_0^(p,q) plus.o E_0^(p+1,q-1) plus.o dots.c$,
      $E_0^(p,q+1) plus.o E_0^(p+1,q) plus.o dots.c$,
      $dots.c$,
    ),
    ($dots.c$, $E_0^(p,q)$, $E_0^(p,q+1)$, $dots.c$),
    (none, $0$, $0$, none),
  ),
  across: (
    none,
    ("->", (label: $d_0 + d_1$), "->"),
    ("->", (label: $d_0 + d_1$), "->"),
    ("->", (label: $d_0$), "->"),
    none,
  ),
  down: range(4).map(_ => (none, "->", "->", none)),
  gap: 7mm,
  row: 7mm,
)
