#import "common.typ": cd, edge, node
#import "../main-defs.typ": *

// The term F^(p+k) X of the filtration, for an integer k.
#let filtration(k) = if k == 0 { $F^p bold(X)$ } else if k > 0 {
  $F^(p+#k) bold(X)$
} else { $F^(p-#(-k)) bold(X)$ }

// Section 3.2: the long exact sequences of the pairs (F^(p+k) X,
// F^(p+k+1) X) for k = 1, 0, -1, one to a row, each from H^(n-1)(F^(p+k) X)
// to H^n(F^(p+k+1) X, F^(p+k+2) X), fitted together by the maps i_1 between
// the groups H^*(F^(p+k) X) of consecutive rows: the sequences go
// alternately down one and to the right two places. One instance of each of
// the maps i_1, j_1 and k_1 is labelled, as printed.
#let interlocking-sequences = {
  let rows = (1, 0, -1).map(k => (
    $H^(n-1) (#filtration(k))$,
    $H^(n-1) (#filtration(k), #filtration(k + 1))$,
    $H^n (#filtration(k + 1))$,
    $H^n (#filtration(k + 1), #filtration(k + 2))$,
  ))
  // Labels of the maps along each row, from the arrow coming in at the left
  // to the arrow going out at the right.
  let across = (
    ($k_1$, [], [], [], []),
    ([], $j_1$, $k_1$, [], []),
    ([], [], [], $j_1$, $k_1$),
  )
  // Labels of the maps i_1 down the two columns of the groups H^*(F^(p+k) X),
  // from the arrow coming in at the top to the arrow going out at the bottom.
  let down = (([], $i_1$, [], []), ([], [], $i_1$, []))
  let items = ()
  for (y, objects) in rows.enumerate() {
    for (x, object) in objects.enumerate() {
      items.push(node((x + 1, y + 1), object))
    }
    for (x, label) in across.at(y).enumerate() {
      items.push(edge((x, y + 1), (x + 1, y + 1), label, "->"))
    }
  }
  for (column, labels) in (1, 3).zip(down) {
    for (y, label) in labels.enumerate() {
      items.push(edge(
        (column, y),
        (column, y + 1),
        label,
        "->",
        label-side: left,
      ))
    }
  }
  cd(spacing: (2mm, 7mm), node-inset: 0.6mm, ..items)
}

// An exact couple: the map i from D to D across the top, j from D down to
// E and k from E back up to D, the labels outside the triangle.
#let exact-couple(d, e, i, j, k) = cd(
  spacing: (1mm, 5mm),
  node((0, 0), d),
  node((2, 0), d),
  node((1, 1), e),
  edge((0, 0), (2, 0), i, "->", label-side: left),
  edge((2, 0), (1, 1), j, "->", label-side: left),
  edge((1, 1), (0, 0), k, "->", label-side: left),
)

// The proofs of Proposition 3.2.4: a column of terms (`dots.v` standing for
// the omitted ones) joined by maps i_1 from the term `maps.at(0)` down to
// the term `maps.at(1)`, with the composite (i_1)^(n-1) curving past them
// from `power.at(0)` to `power.at(1)`; k_1 comes into the term `foot` from
// E_1 on its left, j_1 goes out of the term `head` to E_1 on its right, and
// d_(n-1) runs round below the foot from the left E_1 up to the right one.
// `extra` adds the maps ∂_* and the other arrows of each diagram.
#let differential-diagram(
  column,
  left-term,
  right-term,
  maps: (0, 0),
  power: (0, 0),
  head: 0,
  foot: 0,
  extra: (),
) = cd(
  spacing: (3mm, 5mm),
  size: 0.9em,
  ..column.enumerate().map(((y, term)) => node((1, y), term)),
  node((0, foot), left-term),
  node((2, head), right-term),
  ..range(..maps).map(y => edge(
    (1, y),
    (1, y + 1),
    $i_1$,
    "->",
    label-side: left,
  )),
  edge((1, head), (2, head), $j_1$, "->", label-side: left),
  edge((0, foot), (1, foot), $k_1$, "->", label-side: left),
  edge(..power.map(y => (1, y)), $(i_1)^(n-1)$, "->", bend: -75deg),
  edge(
    (0, foot),
    (0, foot + 0.4),
    (2, foot + 0.4),
    (2, head),
    $d_(n-1)$,
    "->",
    corner-radius: 5pt,
    label-pos: (2, 50%),
    label-side: right,
  ),
  ..extra,
)

// Proof of Proposition 3.2.4 (i): the column runs from H^(p+q+1)(F^(p+n) X)
// down to H^(p+q+1)(F^(p+1) X), and ∂_* goes to the relative group of the
// pair (F^(p+1) X, F^(p+n) X) under it.
#let cycles-diagram = differential-diagram(
  (
    $H^(p+q+1) (F^(p+n) bold(X))$,
    $H^(p+q+1) (F^(p+n-1) bold(X))$,
    $dots.v$,
    $H^(p+q+1) (F^(p+2) bold(X))$,
    $H^(p+q+1) (F^(p+1) bold(X))$,
    $H^(p+q+1) (F^(p+1) bold(X), F^(p+n) bold(X))$,
  ),
  $H^(p+q) (F^p bold(X), F^(p+1) bold(X))$,
  $H^(p+q+1) (F^(p+n-1) bold(X), F^(p+n) bold(X))$,
  maps: (0, 4),
  power: (0, 4),
  head: 1,
  foot: 4,
  extra: (
    edge((1, 4), (1, 5), "->", bend: 8deg),
    edge((0, 4), (1, 5), $partial_*$, "->", label-side: right),
  ),
)

// Proof of Proposition 3.2.4 (ii): the column runs from H^(p+q)(F^p X) down
// to H^(p+q)(F^(p-n+1) X), under the group of the pair
// (F^(p-n+1) X, F^p X), from which ∂_* goes to E_1^(pq).
#let boundaries-diagram = differential-diagram(
  (
    $H^(p+q-1) (F^(p-n+1) bold(X), F^p bold(X))$,
    $H^(p+q) (F^p bold(X))$,
    $dots.v$,
    $H^(p+q) (F^(p-n+3) bold(X))$,
    $H^(p+q) (F^(p-n+2) bold(X))$,
    $H^(p+q) (F^(p-n+1) bold(X))$,
  ),
  $H^(p+q-1) (F^(p-n+1) bold(X), F^(p-n+2) bold(X))$,
  $H^(p+q) (F^p bold(X), F^(p+1) bold(X))$,
  maps: (1, 5),
  power: (1, 5),
  head: 1,
  foot: 4,
  extra: (
    edge((1, 0), (1, 1), "->", bend: 8deg),
    edge((1, 0), (2, 1), $partial_*$, "->", label-side: left),
  ),
)

// Lemma 3.2.5 and its applications: a row A -> B -> C under a group D with
// maps A -> D, D -> B and D -> C; `labels` names the maps f : A -> B,
// g : B -> C, h : D -> B and k : D -> C where they are printed.
#let lemma-diagram(top, row, labels: (:), spacing: (3mm, 7mm)) = {
  let label(name) = labels.at(name, default: none)
  cd(
    spacing: spacing,
    node((1, 0), top),
    ..row.enumerate().map(((x, term)) => node((x, 1), term)),
    edge((0, 1), (1, 0), "->"),
    edge((1, 0), (1, 1), label("h"), "->", label-side: left),
    edge((1, 0), (2, 1), label("k"), "->", label-side: left),
    edge((0, 1), (1, 1), label("f"), "->", label-side: left),
    edge((1, 1), (2, 1), label("g"), "->", label-side: left),
  )
}

// Lemma 3.2.5.
#let image-lemma = lemma-diagram(
  $D$,
  ($A$, $B$, $C$),
  labels: (f: $f$, g: $g$, h: $h$, k: $k$),
  spacing: (7mm, 9mm),
)

// Proof of Theorem 3.2.6, with the author's correction of the last term.
#let page-image = lemma-diagram(
  $H^(p+q) (F^p bold(X), F^(p+n) bold(X))$,
  (
    $H^(p+q-1) (F^(p-n+1) bold(X), F^p bold(X))$,
    $H^(p+q) (F^p bold(X), F^(p+1) bold(X))$,
    $H^(p+q) (F^(p-n+1) bold(X), F^(p+1) bold(X)).$,
  ),
  spacing: (2.5mm, 9mm),
)

// Proof of Theorem 3.2.9.
#let limit-image = lemma-diagram(
  $H^(p+q) (F^p bold(X))$,
  (
    $H^(p+q) (F^(p+1) bold(X))$,
    $H^(p+q) (bold(X))$,
    $H^(p+q) (bold(X), F^(p+1) bold(X)).$,
  ),
  spacing: (5mm, 9mm),
)
