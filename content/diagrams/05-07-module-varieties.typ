#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Proof of Corollary 5.7.9: the quotient by the smaller group maps onto the
// quotient by the larger one, and both are inseparably isogenous to the
// strata of the restriction map.
#let strata-restriction = grid-diagram(
  (
    ($V_E^+ (M) slash W_H (E)$, $V_E^+ (M) slash W_G (E)$),
    ($V_(H, E)^+ (M)$, $V_(G, E)^+ (M)$),
  ),
  across: ("->>", ((label: $res^*_(G, H)$),)),
  down: (((label: $tilde$), (label: $tilde$)),),
  gap: 8mm,
  row: 11mm,
)
