#import "common.typ": cd, edge, grid-diagram, node
#import "../main-defs.typ": *

// The exact couple of the Bockstein spectral sequence: multiplication by p
// across the top, π_* down to the mod p cohomology and the connecting map
// β̂ back up, the labels outside the triangle.
#let bockstein-couple = cd(
  spacing: (8mm, 9mm),
  node((0, 0), $H^* (G, ZZ)$),
  node((2, 0), $H^* (G, ZZ)$),
  node((1, 1), $H^* (G, FF_p)$),
  edge((0, 0), (2, 0), $p$, "->", label-side: left),
  edge((2, 0), (1, 1), $pi_*$, "->", label-side: left),
  edge((1, 1), (0, 0), $hat(beta)$, "->", label-side: left),
)

// Proof of Lemma 4.3.3: the connecting homomorphism, from the reduction
// modulo p in degree r through δ to the inclusion in degree r + 1.
#let connecting-chase = grid-diagram(
  (
    (
      none,
      $Hom_(ZZ G) (P_r, ZZ slash p^2)$,
      $Hom_(ZZ G) (P_r, FF_p)$,
    ),
    (
      $Hom_(ZZ G) (P_(r+1), FF_p)$,
      $Hom_(ZZ G) (P_(r+1), ZZ slash p^2)$,
      none,
    ),
  ),
  down: ((none, (label: $delta$), none),),
  gap: 5mm,
  row: 9mm,
)
