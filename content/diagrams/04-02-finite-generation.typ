#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proof of Theorem 4.2.1: the vertical edge homomorphism of the spectral
// sequence of the central extension is the restriction to Z.
#let edge-restriction = grid-diagram(
  (
    (
      $H^* (P, R)$,
      $H^0 (P, H^* (Z, R))$,
      $H^* (Z, R)$,
    ),
    ($E_infinity^(0*) (R)$, $E_2^(0*) (R)$, none),
  ),
  across: (
    ((label: $res_(P, Z)$), "="),
    ("hook->",),
  ),
  down: (("->", "=", none),),
  gap: 7mm,
  row: 12mm,
)

// Proof of Corollary 4.2.7: the long exact sequence of Ext for
// 0 -> Ker(|G| on M) -> M -> |G|.M -> 0 runs down the column of
// Ext(C, |G|.M), the one for 0 -> |G|.M -> M -> M/|G|.M -> 0 along the
// row; the composite of M -> |G|.M -> M is multiplication by |G|, the map 0.
#let multiplication-sequences = {
  let ext(coefficients) = $Ext^n_(R G) (bold(C), #coefficients)$
  let column(object) = (none, object, none, none, none)
  grid-diagram(
    (
      column($dots.v$),
      column(ext($Ker(|G| "on" M)$)),
      column(ext($M$)),
      (
        $dots.c$,
        ext($abs(G) . M$),
        ext($M$),
        ext($M slash abs(G) . M$),
        $dots.c$,
      ),
      column($dots.v$),
    ),
    across: (none, none, none, "->", none),
    down: range(4).map(_ => (none, "->", none, none, none)),
    extra: (edge((1, 2), (2, 3), $0$, "->", label-side: left),),
    gap: 4mm,
    row: 9mm,
  )
}
