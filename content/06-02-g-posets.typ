#import "main-defs.typ": *
#import "statements.typ": *

== $G$-posets <sec:g-posets>

#definition[
  A *$G$-poset* is a partially ordered set#idx("poset") together with a
  $G$-action which preserves the partial order (i.e., $a < b$ implies
  $g a < g b$).
] <def:g-poset>

If $X$ is a $G$-poset, then we form a $G$-simplicial complex $|X|$#idx("$|X|$"),
called the *simplicial realisation*#idx("realisation", "simplicial")#idx(
  "simplicial",
  "realisation",
) of $X$, as follows. The $n$-simplices are the totally ordered subsets
$ x_0 < x_1 < dots.c < x_n. $
This can be viewed as the topological realisation of a simplicial set (see
Section~@sec:simplicial-sets) in which there are also degenerate simplices where
equalities are allowed:
$ x_0 <= x_1 <= dots.c <= x_n. $
The face and degeneracy maps are given by omitting and repeating elements in the
obvious way.

The *boundary* of such a simplex is
$ sum_(i=0)^n (-1)^i (x_0 < dots.c < x_(i-1) < x_(i+1) < dots.c < x_n). $

Conversely, given a $G$-simplicial complex $Delta$, we form a $G$-poset
$S(Delta)$#idx("$S(Delta)$") whose elements are the simplices of $Delta$, and
where $a < b$ if and only if the vertices of the simplex $a$ are a subset of the
vertices of $b$.

Any invariant defined for simplicial complexes or $G$-simplicial complexes is
defined for posets or $G$-posets by passing to the simplicial realisation. So
for example we define $H_n (X; k) = H_n (|X|, k)$ and
$pi_n (X, x_0) = pi_n (|X|, x_0)$.

#definition[
  The *barycentric subdivision*#idx("barycentric subdivision")#idx(
    "subdivision, barycentric",
  ) $s d(Delta)$#idx("$s d(Delta)$") is defined as the simplicial realisation of
  the poset of simplices, $|S(Delta)|$.
] <def:barycentric-subdivision>

#exercise[
  Show that the underlying topological space of $s d(Delta)$ is homeomorphic to
  that of $Delta$ by a homeomorphism which preserves the $G$-action.
]

#example(kind: "Examples")[
  The following are examples of $G$-posets defined using the subgroup
  structure#idx("complex", "subgroup")#idx("subgroup", "complex") of $G$.
  #enum(numbering: "1.")[
    $cal(S)_p (G) = {$non-trivial $p$-subgroups of $G$$}$#idx(
      "$cal(S)_p (G)$",
    )
  ][
    $cal(A)_p (G) = {$non-trivial elementary abelian $p$-subgroups of
    $G$$}$#idx("$cal(A)_p (G)$")
  ][
    $cal(B)_p (G) = {$non-trivial $p$-subgroups $P$ of $G$ satisfying
    $P = O_p (N_G (P))}$#idx("$cal(B)_p (G)$")
  ]
]

#source(230)We demand that the subgroups be non-trivial, since otherwise the
corresponding simplicial complex would be a cone#idx("cone"), and hence
contractible (see the next section but one for further details). In fact, these
complexes turn out to be homotopy equivalent in a way which preserves the
$G$-action, as we shall see in the next few sections.

We discuss coverings of posets (cf. Definition~@def:covering-space) via
invertible local coefficient systems (or invertible systems for short). This is
a special case of the concept of a local coefficient system, discussed in detail
in the next chapter.

#definition[
  An *invertible system*#idx("invertible system")#idx("system", "invertible") of
  sets (abelian groups, etc.) $cal(F)$ on a poset $X$ is a functor from $X$,
  regarded as a category, to the category of sets (abelian groups, etc.) with
  the property that every map $cal(F)(x) -> cal(F)(x')$ associated to an
  inequality $x <= x'$ is an isomorphism. Invertible systems on $X$ form a
  category, in which the morphisms are the natural transformations.
] <def:invertible-system>

Given an invertible system of sets $cal(F)$ on $X$, we obtain a poset $tilde(X)$
whose elements are pairs $(x, u)$ with $x in X$, $u in cal(F)(x)$, and with
$(x, u) <= (x', u')$ if and only if $x <= x'$, and $u'$ is the image of $u$
under the map $cal(F)(x) -> cal(F)(x')$ corresponding to this inequality. There
is an obvious map of posets $tilde(X) -> X$ whose simplicial realisation is a
covering map $|tilde(X)| -> |X|$.

Conversely, given a covering space $E -> |X|$, we obtain an invertible system
$cal(F)$ by setting $cal(F)(x)$ equal to the inverse image in $E$ of the point
in $|X|$ corresponding to $x$.

It is easy to check that the above describes an equivalence of categories
between covering spaces of $|X|$ and invertible systems on $X$. In particular,
if $X$ is simply connected (i.e., $X$ is connected and $pi_1 (X, x_0) = {1}$),
then every invertible system is isomorphic to a constant functor with values in
some set. By the same token, there is an invertible system $cal(F)$ on $X$ such
that the corresponding poset $tilde(X)$ is the *universal cover*#idx(
  "cover, universal",
)#idx("universal", "cover") of the poset $X$. By Theorem~@th:universal-cover,
for this $cal(F)$ we have $cal(F)(x) tilde.equiv pi_1 (X, x)$.
