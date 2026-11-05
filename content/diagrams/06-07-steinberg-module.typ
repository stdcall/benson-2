#import "common.typ": maps-grid
#import "../main-defs.typ": *

// The square of Conlon's induction theorem, recalled from Volume I: the
// Burnside ring mapped by φ to the representation ring A(G, Triv), each with
// the sum of its ring homomorphisms to ℂ along the rows and the map λ
// between the direct sums of copies of ℂ, as printed.
#let copies(index) = $display(plus.o.big_#index CC)$
#let conlon-square = maps-grid(
  (
    ($B(G)$, copies($H lt.eq_G G$)),
    ($A(G, Triv)$, copies($"ccl’s of" \ "pairs" (H, g)$)),
  ),
  (([],), ([],)),
  (($phi.alt$, $lambda$),),
  gap: 10mm,
)
