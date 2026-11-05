#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Section 3.7: a pullback diagram of fibrations.
#let pullback-square = grid-diagram(
  (($E'$, $E$), ($B'$, $B$)),
  down: (("->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// Section 3.7: the singular cochains of the pullback square as DG modules
// over the cochains of the base; the maps go the other way.
#let cochain-square = grid-diagram(
  (($Delta^* (E')$, $Delta^* (E)$), ($Delta^* (B')$, $Delta^* (B)$)),
  across: "<-",
  down: (("<-", "<-"),),
  gap: 9mm,
  row: 9mm,
)
