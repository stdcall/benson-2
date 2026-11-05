#import "main-defs.typ": *
#import "statements.typ": *

== Paracompact spaces <sec:paracompact>

In the next chapter, we shall be discussing a particular class of fibre bundles,
called principal $G$-bundles, where $G$ is a topological group. We shall
classify principal $G$-bundles over a paracompact#idx("paracompact space")#idx(
  "space",
  "paracompact",
) base space. In preparation for this, we include here a brief discussion of
paracompact spaces.

#definition[
  #source(34)Suppose ${U_alpha}$ is an open cover of a space $X$. A (locally
  finite) *partition of unity*#idx("partition of unity")#idx(
    "unity, partition of",
  ) subordinate to ${U_alpha}$ consists of functions $f_alpha : X -> RR$ such
  that
  + $f_alpha (x) >= 0$ for all $alpha$ and $x$.
  + $f_alpha (x) = 0$ if $x in.not U_alpha$.
  + For each $x in X$, ${alpha | f_alpha (x) != 0}$ is a finite set.
  + For each $x in X$, $sum_alpha f_alpha (x) = 1$.

  If ${U_alpha}$ and ${V_beta}$ are two open covers of $X$, we say ${U_alpha}$
  is a *refinement*#idx("refinement") of ${V_beta}$ if each $U_alpha$ is
  contained in some $V_beta$.

  An open cover ${U_alpha}$ is said to be *locally finite*#idx(
    "finite",
    "locally",
  )#idx("locally finite") if every point has a neighbourhood which intersects
  only a finite number of the $U_alpha$ non-trivially.

  A Hausdorff space $X$ is *paracompact* if every open cover has a locally
  finite refinement.
] <def:partition-of-unity>

#example[
  It is shown in Lundell and Weingram [@bib:Lundell1969, p.~54–55] that every
  CW-complex is paracompact.
]

The main facts we shall need about paracompact spaces are contained in the
following two theorems.

#theorem[
  A Hausdorff space $X$ is paracompact if and only if there is a partition of
  unity subordinate to any given open cover of $X$.
] <th:paracompact-partition>

#proof[
  This is proved in Appendix~1 of Lundell and Weingram [@bib:Lundell1969]. In
  fact they use the above property as the definition of a paracompact space, and
  show that it is equivalent to the definition given above.
]

#theorem[
  Suppose $X$ is a paracompact space and ${U_alpha}$ is an open cover of $X$.
  Then there is a countable open cover ${W_j}$ of $X$ such that each $W_j$ is a
  disjoint union of open sets, each of which is contained in some $U_alpha$.

  If each $x in X$ is in at most $n$ of the $U_alpha$ then we may choose a
  finite open cover ${W_j, 1 <= j <= n}$ with the above property.
] <th:paracompact-countable-cover>

#proof[
  Let ${f_alpha}$ be a partition of unity subordinate to ${U_alpha}$. For each
  $x in X$, let $S(x)$ be the set of indices $alpha$ such that
  $f_alpha (x) != 0$ (so that $S(x)$ is finite for all $x in X$). If $S$ is a
  subset of the set of indices $alpha$, let
  $
    W(S) = {x in X | f_alpha (x) > 0 "and" f_alpha (x) > f_beta (x)
      "for all" alpha in S, beta in.not S}.
  $
  It is clear that $W(S)$ is open in $X$, and that if $S subset.eq.not S'$,
  $S' subset.eq.not S$ then $W(S) inter W(S') = emptyset$. Thus if we let
  $ W_j = union.big_(abs(S(x)) = j) W(S(x)) $
  then $W_j$ is a disjoint union of sets $W(S(x))$, and each
  $W(S(x)) subset.eq U_alpha$ whenever $alpha in S(x)$.

  Under the last hypothesis, $W_j = emptyset$ for $j > n$.
]

#corollary(closed: true)[
  Suppose $p : E -> B$ is a fibre bundle with paracompact base space $B$. Then
  there is a countable open cover ${U_j}$ of $B$ such that
  $p : p^(-1) (U_j) -> U_j$ is a product bundle for each $U_j$.
] <cor:countable-cover>
