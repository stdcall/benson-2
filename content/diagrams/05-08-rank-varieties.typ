#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// The Bockstein and cyclic shifted subgroups: the resolution of k over the
// cyclic shifted subgroup T = ⟨1 + v⟩ mapped into the beginning of the
// resolution of k over kE; kT is included in P_0 = kE.
#let shifted-resolution = grid-diagram(
  (
    ($0$, $k$, $k T$, $k T$, $k$, $0$),
    ($0$, $Omega^2 k$, $P_1$, $P_0$, $k$, $0$),
  ),
  across: (
    ("->", "->", (label: $v$), "->", "->"),
    ("->", "->", (label: $delta$), "->", "->"),
  ),
  down: ((none, "->", "->", "hook->", "=", none),),
  gap: 7mm,
  row: 11mm,
)

// Tensoring with M need not commute with restriction to a shifted
// subgroup E'. The label "⊗M" is set close, as printed.
#let tensor-restriction = {
  let tensor = (label: $class("unary", times.o) M$)
  let restriction = (label: $res_(E, E')$)
  grid-diagram(
    (
      ($Ext^*_(k E) (k, k)$, $Ext^*_(k E) (M, M)$),
      ($Ext^*_(k E') (k, k)$, $Ext^*_(k E') (M, M)$),
    ),
    across: ((tensor,), (tensor,)),
    down: ((restriction, restriction),),
    gap: 6mm,
    row: 11mm,
  )
}
