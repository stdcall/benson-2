#import "common.typ": *

// Section 7.2: posets with three elements. An arrow denotes an inequality in
// which the head of the arrow is less than the tail.

// The largest element above two others: the direct limit is a pushout.
#let pushout-poset = grid-diagram(
  (($bullet$, $bullet$), ($bullet$, none)),
  down: (("->", none),),
)

// The smallest element below two others: the inverse limit is a pullback.
#let pullback-poset = grid-diagram(
  ((none, $bullet$), ($bullet$, $bullet$)),
  down: ((none, "->"),),
)
