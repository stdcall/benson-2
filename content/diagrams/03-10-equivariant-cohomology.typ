#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Section 3.10: the square commuting up to homotopy that compares the
// Borel constructions; the top and the left-hand maps are homotopy
// equivalences, and the dotted map at the bottom is filled in.
#let borel-square = grid-diagram(
  (
    ($(E G times E G') times_G X$, $E G' times_G X$),
    ($E G times_G X$, $E G' times_(G') X'$),
  ),
  across: (((label: $tilde.eq$),), "..>"),
  down: (((label: $tilde.eq$), "->"),),
  gap: 9mm,
  row: 9mm,
)

// Proof of Theorem 3.10.1: the map of spectral sequences, each row
// converging to its right-hand entry.
#let spectral-sequence-map = grid-diagram(
  (
    ($H^* (B U(n); H^* ("point"; R))$, $H^* (B U(n); R)$),
    ($H^* (B U(n); H^* (U(n) times_G X; R))$, $H_G^* (X; R)$),
  ),
  across: "=>",
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)
