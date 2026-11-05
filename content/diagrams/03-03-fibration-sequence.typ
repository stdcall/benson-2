#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Section 3.3: the lifting problem for the fibration E -> B over the path
// from the basepoint to the simplex Δ_α; the dotted map is the lift.
#let simplex-lift = grid-diagram(
  (($0 times F$, $E$), ($(Delta_alpha or I) times F$, $B$)),
  down: (("->", "->"),),
  extra: (edge((0, 1), (1, 0), "..>"),),
  gap: 9mm,
  row: 10mm,
)

// Section 3.3: the differential d_1 followed through the isomorphisms of
// E_1 with the relative cohomology of the filtration of E, with the
// homomorphisms from the cellular homology of B, and with the cellular
// cochains of B.
#let cellular-differential = grid-diagram(
  (
    ($E_1^(p q)$, $E_1^(p+1,q)$),
    ($H^(p+q) (E^p, E^(p-1))$, $H^(p+q+1) (E^(p+1), E^p)$),
    (
      $Hom(H_p (B^p, B^(p-1)), H^q (F))$,
      $Hom(H_(p+1) (B^(p+1), B^p), H^q (F))$,
    ),
    ($C^p (B; H^q (F))$, $C^(p+1) (B; H^q (F))$),
  ),
  across: (
    ((label: $d_1$),),
    ((label: $delta$),),
    ((label: $partial^*$),),
    ((label: $delta$),),
  ),
  down: range(3).map(_ => (
    (label: $tilde.equiv$),
    (label: $tilde.equiv$),
  )),
  gap: 5mm,
  row: 8mm,
)
