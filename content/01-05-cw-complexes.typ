#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-05-cw-complexes.typ": interlocking-sequences

== CW-complexes and cellular homology <sec:cw-complexes>

#idx("cellular", "homology", target: [@sec:cw-complexes])For many purposes in
algebraic topology one needs to have a "good" category of spaces to work with,
because an arbitrary topological space is too badly behaved. For the most part
we shall be interested in homotopy properties of spaces, and it turns out that
an appropriate category of spaces to work in is that of CW-complexes#idx(
  "CW-complex",
). These are built up by an inductive procedure of adding on cells, which we now
describe.

#definition[
  Let $D^n$ denote an $n$-cell, i.e., a closed unit ball in $RR^n$, and let
  $S^(n-1) = dot(D)^n$ be its boundary, an $(n - 1)$-sphere. Suppose $A$ is a
  Hausdorff#idx("Hausdorff space")#idx("space", "Hausdorff") topological space
  and ${f_alpha : S^(n-1) -> A}$ is a family of maps *(attaching maps)*#idx(
    "attaching",
    "map",
  )#idx("map", "attaching"). Let $Z = dot(union.big)_alpha D^n_alpha$ be a
  disjoint union of $n$-cells indexed by $alpha$. Then ${f_alpha}$ induces a map
  $f : dot(Z) -> A$. Let
  $ X = A union_f Z = (A dot(union) Z)\/(z tilde f(z) "for" z in dot(Z)) $
  with the quotient topology. Then we say $X$ is *obtained from $A$ by attaching
  $n$-cells*#idx("attaching", "cells").

  Let $sigma^n_alpha$ be the image of $D^n_alpha$ in $X$. Then we have a map
  $ g_alpha : (D^n, S^(n-1)) -> (X, A) $
  whose image is $sigma^n_alpha$. This is called the *characteristic map*#idx(
    "characteristic",
    "map",
  )#idx("map", "characteristic") of the *cell*#idx("cells") $sigma^n_alpha$.
] <def:attaching-cells>

Note that the space automatically has the _weak topology:_#idx(
  "topology",
  "weak",
)#idx("weak", "topology") $K subset.eq X$ is closed if and only if $K inter A$
is closed and $K inter sigma^n_alpha$ is closed for each $alpha$.

#definition[
  A *relative CW-complex*#idx("relative", "CW-complex") $(X, A)$ is a pair
  $A subset.eq X$ with $A$ Hausdorff, and a filtration
  $A = X^((-1)) subset.eq X^((0)) subset.eq X^((1)) subset.eq dots.c subset.eq
  X$ such that
  + #source(25)$X^((k))$ is obtained from $X^((k-1))$ by attaching $k$-cells,
  + $X = union.big_k X^((k))$, and
  + $X$ has the *weak topology*: $K subset.eq X$ is closed if and only if
    $K inter X^((k))$ is closed in $X^((k))$ for all $k$.

  The subspace $X^((k)) subset.eq X$ is called the *$k$-skeleton*#idx(
    "skeleton",
  ) of $(X, A)$.
] <def:relative-cw-complex>

#subhead[Closure finiteness]#idx("closure finite") Note that the boundary of a
cell $dot(sigma)^k_alpha$ is _compact_, and is hence contained in the union of
$A$ and a _finite number_ of the attached cells.

#remark[
  "CW" stands for "Closure finite, Weak topology".
]

#definition[
  A *CW-complex* is as above with $A = emptyset$. A CW-complex is *finite* if it
  has only finitely many cells, and *of finite type*#idx("finite", "type")#idx(
    "type",
    "finite",
  ) if it has only finitely many cells in each dimension.
] <def:cw-complex>

#example[
  A simplicial complex#idx("complex", "simplicial")#idx("simplicial", "complex")
  is a CW-complex in which each cell is a simplex and the attaching maps take
  the boundary of a cell (linearly) to the union of the faces of the simplex. In
  particular the boundary maps here are injective, which sometimes simplifies
  arguments. It turns out that every CW-complex is homotopy equivalent to a
  simplicial complex.
]

#remark[
  According to a theorem of Milnor [@bib:Milnor1959], if $X$ is a compact
  topological space and $Y$ has the homotopy type of a CW-complex then the space
  of maps from $X$ to $Y$ (with the compact-open topology) has the homotopy type
  of a CW-complex.

  Note that with the usual product topology, the product of two CW-complexes is
  not necessarily a CW-complex, unless one of them is finite, or both of them
  are countable (see Milnor [@bib:Milnor1956a], p.~272). The problem is that the
  product does not have the weak topology with respect to its finite
  subcomplexes. To solve this problem, we take products in the category of
  compactly generated spaces. This is the same as using the weak topology with
  respect to the products of finite subcomplexes.
]

#subhead[Cellular chains]#idx("cellular", "chain")#idx("chain", "cellular") In
the case of a CW-complex, there is a very efficient way of calculating homology
and cohomology, via _cellular chains_. If $(X, A)$ is a relative CW-complex, we
define
$
  C_p (X, A; R) = H_p (X^((p)), X^((p-1)); R)
  = plus.o.big_(p"-cells " alpha) R_alpha
$
the free $R$-module on the $p$-cells. Then the short exact sequence of chain
complexes
$
  0 -> Delta_* (X^((p-1)), X^((p-2)); R) -> Delta_* (X^((p)), X^((p-2)); R) \
  -> Delta_* (X^((p)), X^((p-1)); R) -> 0
$
gives rise to the _boundary map of the triple_
$ partial : H_p (X^((p)), X^((p-1)); R) -> H_(p-1) (X^((p-1)), X^((p-2)); R). $
#source(26)It is easy to check that $partial^2 = 0$, so we use this map
$ partial : C_p (X, A; R) -> C_(p-1) (X, A; R) $
to make a chain complex $(C_* (X, A; R), partial)$, the _complex of cellular
chains._

Similarly in cohomology the coboundary map
$ delta : H^(p-1) (X^((p-1)), X^((p-2)); R) -> H^p (X^((p)), X^((p-1)); R) $
gives us a cochain complex $(C^* (X, A; R), delta)$. This is the same as the
complex obtained by dualising the complex of cellular chains. It is called the
_complex of cellular cochains._

Note that for a CW-complex of finite type, the cellular chains and cellular
cochains form complexes of _finitely generated_ $R$-modules.

Since a sphere only has reduced homology in one degree, we have
$ H_q (X^((p)), X^((p-1))) = 0 $
for $q != p$. It is easy to deduce by induction from this that
$H_q (X^((p)), A) = 0$ for $q > p$, and that $H_q (X^((p)), A) = H_q (X, A)$ for
$q < p$.

It is worth reading the proof of the following theorem before trying to read the
section on spectral sequences, since in some sense the argument is a thinly
disguised collapsing spectral sequence argument. We shall reprove the theorem as
an easy application of the spectral sequence of a filtered chain complex in
Section~@sec:filtered-complex.

#theorem[
  We have natural isomorphisms
  $
    H_p (X, A; R) tilde.equiv H_p (C_* (X, A; R), partial), quad
    H^p (X, A; R) tilde.equiv H^p (C^* (X, A; R), delta).
  $
] <th:cellular-homology>

#proof[
  We have various long exact sequences which interlock as in the following
  diagram.
  $ #interlocking-sequences $
  In this diagram, the rows and columns are exact. Thus we have
  $
    #aligned-rows(
      ($H_p (C_* (X, A; R), partial)$, $= Ker(partial)\/Im(partial)
      = Ker(i_*)\/Im(partial)$),
      ($$, $tilde.equiv H_p (X^((p)), A)\/Im(partial')
      = H_p (X^((p)), A)\/Ker(j_*)$),
      ($$, $tilde.equiv H_p (X^((p+1)), A) tilde.equiv H_p (X, A).$),
    )
  $

  Similarly for cohomology we use the dual of the above argument.
]

#subhead[#source(27)Cellular approximation]

#definition[
  A map $f : (X, A) -> (Y, B)$ of relative CW-complexes is said to be
  *cellular*#idx("cellular", "map") if it maps the $k$-skeleton of $(X, A)$ into
  the $k$-skeleton of $(Y, B)$ for each $k >= 0$.
] <def:cellular-map>

#theorem(title: [Cellular Approximation Theorem])[
  Every map
  $ f : (X, A) -> (Y, B) $
  of relative CW-complexes is homotopic (relative to $A$) to a cellular map.
] <th:cellular-approximation>
#idx("approximation, cellular", target: [@th:cellular-approximation])#idx(
  "cellular",
  "approximation",
  target: [@th:cellular-approximation],
)#idx(
  "theorem",
  "cellular approximation",
  target: [@th:cellular-approximation],
)

#proof[
  See Spanier [@bib:Spanier1966, Section~7.6, Cor.~18].
]

#subhead[Weak homotopy equivalences]

#definition[
  A map $f : X -> Y$ is a *weak homotopy equivalence*#idx(
    "equivalence",
    "weak homotopy",
  )#idx("homotopy", "equivalence", "weak")#idx(
    "weak",
    "homotopy equivalence",
  ) if
  $ f_* : pi_n (X, x) -> pi_n (Y, f(x)) $
  is an isomorphism for all $n >= 0$, and for all $x in X$. Note that if $X$ is
  path connected then it is sufficient to check this for a single choice of
  basepoint, by Section~@sec:homotopy-groups.

  A space $X$ is *weakly contractible*#idx("contractible", "weakly")#idx(
    "weakly contractible",
  ) if $pi_n (X, x) = 0$ for all $n >= 0$ and for all $x in X$.
] <def:weak-homotopy-equivalence>

It is clear that a homotopy equivalence is a weak homotopy equivalence. We shall
show that for CW-complexes, the converse is true.

#theorem(title: [Whitehead])[
  If $X$ and $Y$ are CW-complexes and $f : X -> Y$ is a weak homotopy
  equivalence, then $f$ is a homotopy equivalence. In particular if $X$ is a
  weakly contractible CW-complex then $X$ is contractible.
] <th:whitehead-cw>
#idx("theorem", "Whitehead", target: [@th:whitehead-cw])#idx(
  "Whitehead theorems",
  target: [@th:whitehead-cw],
)

#proof[
  By the cellular approximation theorem, we may assume that $f$ is cellular.
  This has the effect that the mapping cylinder $M_f$ is a CW-complex. Since $f$
  is a weak homotopy equivalence, the long exact sequence
  $
    dots.c -> pi_(n+1) (M_f, X, x_0) -> pi_n (X, x_0)
    limits(arrow.r.long)^(f_*) pi_n (Y, y_0) -> pi_n (M_f, X, x_0) -> dots.c
  $
  of Section~@sec:whitehead shows that $pi_n (M_f, X, x_0) = 0$ for all
  $n >= 0$.

  Now suppose $(K, L)$ is a relative CW-complex and $g : (K, L) -> (M_f, X)$ is
  a map. By induction, it is clear that the restriction of $g$ to the
  $n$-skeleton of $(K, L)$ is homotopic relative to $L$ to a map sending
  $K^((n))$ into $X$. Namely, once the $(n - 1)$-skeleton is in, the obstruction
  to pushing the $n$-skeleton in lies in $pi_n (M_f, X, x_0) = 0$. We may fit
  these homotopies together by doing the first skeleton in the interval
  $[0, 1/2]$, the second in $[1/2, 3/4]$, and so on, to show that $g$ is
  homotopic relative to $L$ to a map sending $K$ into $X$.

  Applying the above statement to the identity map from $(M_f, X)$ to itself, we
  see that the inclusion $X subset.eq M_f$ is a homotopy equivalence. Hence by
  the discussion in Section~@sec:whitehead, so is $f$.
]
