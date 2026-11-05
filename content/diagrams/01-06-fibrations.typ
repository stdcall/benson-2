#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// A map labelled `label` (`[]` unlabelled) in the style `style`.
#let map(label: [], style: "->") = (style: style, label: label)

// The dotted lift from the place `from` to the place `to`, named on its
// upper left.
#let lift(from, to, name: []) = edge(from, to, name, "..>", label-side: left)

// A lifting square: the corners `a → b` over `c → d` with the maps `top`
// and `bottom` across, `left` and `right` down (labels on the right), and
// the dotted lift from c to b.
#let lifting-square(
  a,
  b,
  c,
  d,
  top: map(),
  bottom: map(),
  left: map(),
  right: map(),
  name: [],
) = grid-diagram(
  ((a, b), (c, d)),
  across: ((top,), (bottom,)),
  down: ((left, right),),
  extra: (lift((0, 1), (1, 0), name: name),),
  gap: 8mm,
  row: 10mm,
)

// Definition 1.6.1: the homotopy lifting property.
#let homotopy-lifting = lifting-square(
  $X times 0$,
  $E$,
  $X times I$,
  $B$,
  top: map(label: $f$),
  bottom: map(label: $h$),
  left: map(style: "hook->"),
  right: map(label: $p$),
  name: $H$,
)

// Lemma 1.6.4: lifting over a strong deformation retract.
#let retract-lifting = lifting-square($A$, $E$, $X$, $B$)

// Proof of Lemma 1.6.4: the deformation h of X into A, lifted, and the
// inclusion i_0 at the end 0 of the homotopy.
#let retract-lifting-proof = grid-diagram(
  (($A times I union X times 1$, $A$, $E$), ($X times I$, $X$, $B.$)),
  across: ((map(label: $h$), map()), (map(label: $h$), map())),
  down: ((map(), map(), map()),),
  extra: (
    lift((0, 1), (2, 0)),
    edge((1, 1), (0, 1), $i_0$, "->", bend: 25deg, label-side: left),
  ),
  gap: 8mm,
  row: 10mm,
)

// Proof of Theorem 1.6.5 (i): an element α of π_n(B, B', b_0) lifts to γ.
#let cube-lifting = lifting-square(
  $C^(n-1)$,
  $E$,
  $I^n$,
  $B$,
  bottom: map(label: $alpha$),
  name: $gamma$,
)

// Proof of Theorem 1.6.5 (ii): a homotopy h : p_*(α) ≃ p_*(β) lifts to H.
#let homotopy-lifting-cube = lifting-square(
  $(I^n times 0) union (C^(n-1) times I) union (I^n times 1)$,
  $E$,
  $I^n times I$,
  $B$,
  top: map(label: $alpha union (e_0) union beta$),
  bottom: map(label: $h$),
  name: $H$,
)

// Proof of Proposition 1.6.7: the path ω lifted to a map α from F × I,
// whose end gives α_1 : F → F'.
#let fibre-transport = grid-diagram(
  (($F times 0$, none, $E$), ($F times I$, $I$, $B$)),
  across: (none, (map(style: "->>"), map(label: $omega$))),
  down: ((map(), none, map()),),
  extra: (
    edge((0, 0), (2, 0), "->"),
    lift((0, 1), (2, 0), name: $alpha$),
  ),
  gap: 8mm,
  row: 10mm,
)

// Proof of Proposition 1.6.7: a homotopy of paths ω ≃ ω′ lifted to a
// homotopy between α and α′.
#let transport-homotopy = grid-diagram(
  (
    ($F times (I times 0 union 0 times I union I times 1)$, none, $E$),
    ($F times I times I$, $I times I$, $B$),
  ),
  across: (
    none,
    (map(style: "->>"), map(label: $omega tilde.eq omega'$)),
  ),
  down: ((map(), none, map()),),
  extra: (
    edge((0, 0), (2, 0), $alpha union pi_F union alpha'$, "->"),
    lift((0, 1), (2, 0)),
  ),
  // The long label ω ≃ ω′ of the last map needs a longer arrow.
  gap: 12mm,
  row: 10mm,
)

// Definition 1.6.8: a local trivialisation of a fibre bundle.
#let local-trivialisation = grid-diagram(
  (($U_alpha times F$, $p^(-1) (U_alpha)$), ($U_alpha$, $U_alpha$)),
  across: ((map(label: $phi.alt_alpha$),), ("=",)),
  down: ((map(label: $pi_1$), map(label: $p$)),),
  gap: 8mm,
  row: 10mm,
)

// Proof of Lemma 1.6.9: lifting to a product, with the inclusion i of
// X × 0 and the projection π_X onto it.
#let product-lifting = grid-diagram(
  (($X times 0$, $B times F$), ($X times I$, $B$)),
  across: ((map(label: $f$),), (map(label: $h$),)),
  down: ((none, map(label: $pi_B$)),),
  extra: (
    edge((0, 0), (0, 1), $i$, "->", bend: 25deg, label-side: left),
    edge((0, 1), (0, 0), $pi_X$, "->", bend: 25deg, label-side: left),
    lift((0, 1), (1, 0), name: $H$),
  ),
  gap: 8mm,
  row: 10mm,
)

// Lemma 1.6.10: the homotopy extension lifting property.
#let extension-lifting = lifting-square(
  $X times 0 union A times I$,
  $E$,
  $X times I$,
  $B$,
  top: map(label: $f$),
  bottom: map(label: $h$),
  name: $H$,
)

// Proof of Lemma 1.6.10: the extension over one simplex.
#let simplex-lifting = lifting-square(
  $Delta times 0 union dot(Delta) times I$,
  $E$,
  $Delta times I$,
  $B$,
  top: map(label: $g$),
  bottom: map(label: $h$),
  name: $H$,
)

// Proof of Theorem 1.6.11: the homotopy lifting property for I^n.
#let bundle-lifting = lifting-square(
  $I^n times 0$,
  $E$,
  $I^n times I$,
  $B$,
  top: map(label: $g$),
  bottom: map(label: $h$),
  name: $H$,
)

// Section 1.6: the pullbacks defining P_f and the homotopy fibre F_f.
#let pullback-square(a, b) = grid-diagram(
  ((a, b), ($Y$, $X.$)),
  across: ((map(),), (map(),)),
  down: ((map(), map()),),
  gap: 8mm,
  row: 10mm,
)
#let path-pullback = pullback-square($P_f$, $X^I$)
#let fibre-pullback = pullback-square($F_f$, $P X$)
