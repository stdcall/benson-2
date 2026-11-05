#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proof of Theorem 1.5.4: the long exact sequences of the pairs and triples
// of skeleta that interlock: the row of the triple (X^(p), X^(p-1), A), the
// columns of the triples (X^(p+1), X^(p), A) and (X^(p-1), X^(p-2), A), and
// the boundary maps ∂ of the cellular chains as diagonals.
#let interlocking-sequences = grid-diagram(
  (
    (none, $H_(p+1) (X^((p+1)), X^((p)))$, none, $0 = H_(p-1) (X^((p-2)), A)$),
    (
      $H_p (X^((p-1)), A)$,
      $H_p (X^((p)), A)$,
      $H_p (X^((p)), X^((p-1)))$,
      $H_(p-1) (X^((p-1)), A)$,
    ),
    ($0$, $H_p (X^((p+1)), A)$, $H_p (X, A)$, $H_(p-1) (X^((p-1)), X^((p-2)))$),
    (none, $H_p (X^((p+1)), X^((p))) = 0$, none, none),
  ),
  across: (none, ("->", "->", (style: "->", label: $i_*$)), none, none),
  down: (
    (none, (style: "->", label: $partial'$), none, "->"),
    ("=", (style: "->", label: $j_*$), none, "->"),
    (none, "->", none, none),
  ),
  extra: (
    edge((1, 0), (2, 1), $partial$, "->", label-side: left),
    edge((2, 1), (3, 2), $partial$, "->", label-side: left),
    edge((1, 2), (2, 2), $tilde.equiv$, label-side: center, stroke: none),
  ),
  gap: 3mm,
  row: 9mm,
  size: 0.85em,
)
