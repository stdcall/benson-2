#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-14-multiple-complexes.typ": (
  a6-resolution, gl3-resolution, pushout-sphere, resolution-shift,
)

== Multiple complexes <sec:multiple-complexes>
#idx("multiple complex", target: [@sec:multiple-complexes])#idx(
  "complex",
  "multiple",
  target: [@sec:multiple-complexes],
)

#source(211)The main theorem of this section is a generalisation of
Theorem~@th:eisenbud to arbitrary (not necessarily periodic) finitely generated
modules. Namely, we shall show that in a suitable sense, a module of complexity
$c$ possesses a $c$-fold periodic projective resolution. The hard part of the
proof is involved in checking that certain modules are projective. We shall give
two proofs of this, one involving the machinery of varieties and the other using
a hypercohomology argument. The latter is more opaque, but works in greater
generality.

We begin by recalling from Section~2.6 of Volume~I the basic construction we
shall be using. Suppose $zeta in H^n (G, R) tilde.equiv Ext^n_(R G) (R, R)$. We
choose a cocycle $hat(zeta) : tilde(Omega)^n R -> R$ representing $zeta$, where
$tilde(Omega)^n R$ is the $n$th kernel in a projective resolution $bold(P)$ of
$R$ as an $R G$-module. By making $bold(P)$ large enough, we may assume
$hat(zeta)$ is surjective. We denote its kernel by $L_zeta$, and form the
pushout diagram
$ #pushout-sphere $
The bottom row of this diagram is an $n$-fold extension#idx(
  "extension",
  "$n$-fold",
) representing the element $zeta in Ext^n_(R G) (R, R)$. We denote by
$bold(C)_zeta$#idx("$bold(C)_zeta$") the chain complex
$ 0 -> P_(n-1) slash L_zeta -> P_(n-2) -> dots.c -> P_0 -> 0 $
formed by truncating the bottom row of this diagram. Thus we have
$
  H_i (bold(C)_zeta) tilde.equiv cases(
    R & "if" i = 0\, n - 1,
    0 & "otherwise."
  )
$
We write $tilde(zeta)$ for the generator of degree $n - 1$, and $1$ for the
generator of degree zero.

The complex $bold(C)_zeta$ should be thought of as a sort of algebraic analogue
of a sphere with $G$-action, with $zeta$ being the transgression of the
fundamental class of the sphere.

We also write $bold(C)_zeta^((infinity))$#idx("$bold(C)_zeta^((infinity))$") for
the chain complex
$
  dots.c -> P_1 -> P_0 -> P_(n-1) slash L_zeta -> P_(n-2) -> dots.c -> P_1
  -> P_0 -> 0
$
#source(212)obtained by splicing together infinitely many copies of
$bold(C)_zeta$ in positive degree. It is an exact complex except in degree zero,
where the homology is $R$.

#definition[
  We say that homogeneous elements $zeta_1, dots, zeta_c$ of the ring
  $H^dot (G, k)$ *cover the variety*#idx("covering", "the variety")#idx(
    "variety",
    "covering the",
  ) of a finitely generated $k G$-module $M$ of complexity $c$ if
  $
    V_G chevron.l zeta_1 chevron.r inter dots.c inter
    V_G chevron.l zeta_c chevron.r inter V_G (M) = {0}.
  $
] <def:cover-variety>

Note that by Proposition~@prop:variety-dimension-complexity, $dim V_G (M) = c$,
so that by the Noether Normalisation Lemma~@lem:noether-normalisation there
exist homogeneous elements $zeta_1, dots, zeta_c$ generating a polynomial
subalgebra
$ k[zeta_1, dots, zeta_c] subset.eq H^dot (G, k) slash I_G (M) $
over which $H^dot (G, k) slash I_G (M)$ is finitely generated as a module. Thus
the corresponding map $V_G (M) -> AA^c (k)$ is finite, so that the preimage of
the origin is a finite set. But this map is also homogeneous, and so the
preimage of the origin is the origin. Therefore for such a choice of
$zeta_1, dots, zeta_c$ we have
$
  V_G chevron.l zeta_1 chevron.r inter dots.c inter
  V_G chevron.l zeta_c chevron.r inter V_G (M) = {0}.
$

#theorem[
  #statement-comment[[@bib:Benson1987a]] Suppose $zeta_1, dots, zeta_c$ cover
  the variety of a finitely generated $k G$-module $M$ of complexity $c$. Then
  the complex
  $ bold(C)_(zeta_1) times.o dots.c times.o bold(C)_(zeta_c) times.o M $
  is a finite complex of projective $k G$-modules. The complex
  $
    bold(C)_(zeta_1)^((infinity)) times.o dots.c times.o
    bold(C)_(zeta_c)^((infinity)) times.o M
  $
  is a projective resolution of $M$ of growth $c$.
] <th:multiple-complex-resolution>

#proof[
  All the modules in $bold(C)_(zeta_i)$ are projective except possibly the
  module $P_(n_i - 1) slash L_(zeta_i)$. Since the tensor product of any module
  with a projective module is projective, it remains to examine the module
  $
    P_(n_1 - 1) slash L_(zeta_1) times.o dots.c times.o
    P_(n_c - 1) slash L_(zeta_c) times.o M.
  $
  By Proposition~@prop:variety-dual-omega, Theorem~@th:variety-tensor-product
  and Proposition~@prop:l-zeta-variety, the variety of this module is
  $
    V_G chevron.l zeta_1 chevron.r inter dots.c inter
    V_G chevron.l zeta_c chevron.r inter V_G (M)
  $
  which is ${0}$ by the choice of $zeta_1, dots, zeta_c$. It thus follows from
  Proposition~@prop:variety-dimension-complexity that this module is also
  projective.

  It now follows by Proposition~@prop:tensor-homology that
  $bold(C)_(zeta_1)^((infinity)) times.o dots.c times.o
  bold(C)_(zeta_c)^((infinity)) times.o M$ is a projective resolution of $M$.
  Since each $bold(C)_(zeta_i)^((infinity))$ is a periodic complex, the rate of
  growth of the tensor product is exactly $c$.
]

#remark[
  The above theorem shows that a finitely generated module always has a
  projective resolution which may be expressed as a tensor product of periodic
  complexes, and of the same polynomial rate of growth as the minimal
  resolution. However, in general the minimal resolution may not be written as a
  tensor product in this way. But it appears in all the examples #source(
    213,
  )calculated that the minimal resolution of a module of complexity $c$ can
  always be written as the total complex of a $c$-fold complex in which the
  rows, columns, etc. are all eventually periodic. For example, if
  $G = GL_3 (FF_2)$#idx("general linear group", "$GL_3 (FF_2)$")#idx(
    "$GL_3 (FF_2)$",
  )#idx("group", "general linear", "$GL_3 (FF_2)$") and $char(k) = 2$, then
  there are three simple modules in the principal block, namely the trivial
  module $k$, the natural three dimensional simple module $M$ and its dual $N$.
  The minimal resolution of the trivial module is the total complex of a double
  complex of the form given as follows.
  $ #gl3-resolution $

  As another example, if $G$ is the alternating group $A_6$#idx(
    "alternating group",
    "$A_6$",
  )#idx("group", "alternating", "$A_6$") and $char(k) = 3$, then there are four
  simple modules in the principal block, namely the trivial module $k$, two
  distinct three dimensional modules $L$ and $M$, and a four dimensional module
  $N$. The minimal resolution of the trivial module is the #source(214)total
  complex of a double complex of the form given as follows.
  $ #a6-resolution $
]

We now give an alternative proof of the above theorem using hypercohomology.
This proof works in greater generality, and so we must first generalise the
appropriate definitions.

#definition[
  Suppose $R$ is Noetherian and $M$ is a finitely generated $R G$-module. We say
  that homogeneous elements $zeta_1, dots, zeta_c$ of $H^* (G, R)$ *cover the
  variety* of $M$ if the images of $zeta_1, dots, zeta_c$ under the map
  $
    H^* (G, R) = Ext^*_(R G) (R, R) limits(arrow.r.long)^(times.o M)
    Ext^*_(R G) (M, M)
  $
  generate a subring over which $Ext^*_(R G) (M, M)$ is finitely generated as a
  module.
] <def:cover-variety-ring>

#remark(kind: "Remarks")[
  In case $R = k$ is a field, this agrees with the previous definition of
  covering the variety of $M$. By Corollary~@cor:ext-noetherian to Evens'
  theorem, a set of homogeneous elements covering the variety of $M$ always
  exists. We shall see below that under some moderately weak hypotheses, $M$ has
  a projective resolution which is a tensor product of $c$ periodic complexes,
  and which therefore has growth exactly $c$. Thus a minimal such $c$ may be
  thought of as the complexity of $M$. Note that in this generality there is no
  unique minimal resolution, so that our previous definition over a field does
  not work.
]

We begin with a lemma. Recall from Proposition~@prop:hypercohomology that if
$bold(D)$ is a chain complex of $R G$-modules, bounded above, then we have a
hypercohomology#idx("hypercohomology spectral sequence")#idx(
  "spectral sequence",
  "hypercohomology",
) #source(215)spectral sequence
$
  Ext^p_(R G) (H_q (bold(C)_zeta), bold(D)) =>
  Ext^(p+q)_(R G) (bold(C)_zeta, bold(D)).
$
Since $H_q (bold(C)_zeta)$ is only non-zero for $q = n - 1$ ($n = deg(zeta)$)
and $q = 0$, the only possible non-zero differential in the above spectral
sequence is $d_n$.

#lemma[
  Suppose $bold(D)$ is a chain complex of $R G$-modules, bounded above. In the
  two row spectral sequence
  $
    E_2^(p q) (zeta) = Ext^p_(R G) (H_q (bold(C)_zeta), bold(D)) =>
    Ext^(p+q)_(R G) (bold(C)_zeta, bold(D))
  $
  the differential $d_n$ is given by
  $
    d_n (alpha . tilde(zeta)) = alpha . zeta in E_n^(p+n, 0) (zeta) =
    H^(p+n) (G, bold(D)).
  $
] <lem:two-row-differential>

#proof[
  We first remark that since $H_q (bold(C)_zeta) = R$ if $q = 0$ or $n - 1$ and
  is zero elsewhere, we have
  $
    E_2^(p q) (zeta) = cases(
      H^p (G, bold(D)) & "if" q = 0 "or" n - 1,
      0 & "otherwise."
    )
  $

  The differential $d_n$ may be obtained as follows. We have a short exact
  sequence of chain complexes
  $
    0 -> bold(C)_zeta -> bold(C)_zeta^((infinity)) ->
    bold(C)_zeta^((infinity)) [n] -> 0.
  $
  If $bold(P)$ is a projective resolution of $R$ as an $R G$-module, we have a
  short exact sequence
  $
    0 -> bold(P) times.o bold(C)_zeta ->
    bold(P) times.o bold(C)_zeta^((infinity)) ->
    bold(P) times.o bold(C)_zeta^((infinity)) [n] -> 0
  $
  and hence a short exact sequence of cochain complexes
  $
    0 -> bold(Hom)_(R G) (bold(P) times.o bold(C)_zeta^((infinity)), bold(D))
    [-n]
    -> bold(Hom)_(R G) (bold(P) times.o bold(C)_zeta^((infinity)), bold(D)) \
    -> bold(Hom)_(R G) (bold(P) times.o bold(C)_zeta, bold(D)) -> 0.
  $
  Now $bold(P) times.o bold(C)_zeta^((infinity))$ is again a projective
  resolution of $R$ as an $R G$-module, so the long exact sequence in cohomology
  of this short exact sequence of cochain complexes is
  $
    dots.c -> Ext^(r-1)_(R G) (bold(C)_zeta, bold(D)) -> H^(r-n) (G, bold(D))
    limits(arrow.r.long)^(d_n) H^r (G, bold(D)) ->
    Ext^r_(R G) (bold(C)_zeta, bold(D)) -> dots.c
  $
  This is the long exact sequence associated to the above two-row spectral
  sequence, and so the marked homomorphism is $d_n$.

  To identify this map as multiplication by $zeta$, we argue as follows. In
  general, multiplication by $zeta$ may be thought of in the following way. A
  cocycle representing the element $zeta$ lifts to a map of projective
  resolutions $bold(P) -> bold(P) [n]$. If $alpha in H^(r-n) (G, bold(D))$ is
  represented by a chain map $bold(P) -> bold(D) [r - n]$ then the product
  $alpha . zeta$ is represented by shifting and composing
  $ bold(P) -> bold(P) [n] -> bold(D) [r]. $
  So all we need check is that the map of resolutions
  $
    bold(P) times.o bold(C)_zeta^((infinity)) ->
    bold(P) times.o bold(C)_zeta^((infinity)) [n]
  $
  #source(216)given above represents the element $zeta$ in cohomology. But this
  follows from the diagram
  $ #resolution-shift $
  since the bottom row is an exact sequence representing $zeta$.
]

If $zeta_1, dots, zeta_c in H^* (G, R)$ are homogeneous elements, then
Corollary~2.7.2 of the Künneth Theorem in Volume~I shows that
$H_* (times.o.big_(i=1)^c bold(C)_(zeta_i))$ has a basis consisting of elements
of the form $x_1 times.o dots.c times.o x_c$ where each $x_i$ is equal to either
$1$ or $tilde(zeta)_i$. We also write $tilde(zeta)_i$ for the element
$1 times.o dots.c times.o tilde(zeta)_i times.o dots.c times.o 1$ of
$H_* (times.o.big_(i=1)^c bold(C)_(zeta_i))$.

#theorem[
  #statement-comment[[@bib:Benson1994a]] Suppose $R$ is a Noetherian ring with
  the property that for each prime $p$ dividing $|G|$, either $p$ is invertible
  in $R$ or $R slash p R$ is Artinian, and $M$ is an $R G$-lattice (i.e., a
  finitely generated $R G$-module which is projective as an $R$-module). If
  $zeta_1, dots, zeta_c in H^* (G, R)$ cover the variety of $M$, then the
  complex
  $ bold(C)_(zeta_1) times.o dots.c times.o bold(C)_(zeta_c) times.o M $
  is a finite complex of projective $R G$-modules. The complex
  $
    bold(C)_(zeta_1)^((infinity)) times.o dots.c times.o
    bold(C)_(zeta_c)^((infinity)) times.o M
  $
  is a projective resolution of $M$.
] <th:multiple-complex-lattice>

#proof[
  As in the proof of Theorem~@th:multiple-complex-resolution, it suffices to
  show that the module
  $
    P_(n_1 - 1) slash L_(zeta_1) times.o dots.c times.o
    P_(n_c - 1) slash L_(zeta_c) times.o M
  $
  is projective. We first show that it is sufficient to prove that
  $bold(C) times.o M$ has a finite projective resolution, where
  $bold(C) = bold(C)_(zeta_1) times.o dots.c times.o bold(C)_(zeta_c)$. For if
  $bold(P) -> bold(C) times.o M$ is a finite projective resolution, then by
  enlarging $bold(P)$ if necessary, we may assume this map is surjective. The
  kernel is therefore a finite exact sequence of modules, all except possibly
  one of which is projective. Moreover, as $R$-modules, all the modules involved
  are projective, and so by Corollary~3.6.5 of Volume~I,
  $P_(n_1 - 1) slash L_(zeta_1) times.o dots.c times.o
  P_(n_c - 1) slash L_(zeta_c) times.o M$ is projective as an $R G$-module.

  By Corollary~@cor:finite-projective-resolution, in order to prove that
  $bold(C) times.o M$ has a finite projective resolution, it suffices to prove
  that $Ext^n_(R G) (bold(C) times.o M, bold(C) times.o M) = 0$ for all
  sufficiently large $n$. We start by showing that
  $Ext^n_(R G) (bold(C) times.o M, M) = 0$ for all sufficiently large $n$. Since
  $M$ is an $R G$-lattice, $Ext^n_(R G) (bold(C) times.o M, M)
  tilde.equiv Ext^n_(R G) (bold(C), Hom_R (M, M))$, so we have a spectral
  sequence
  $
    E_2^(p q) = Ext^p_(R G) (H_q (bold(C)), Hom_R (M, M)) =>
    Ext^(p+q)_(R G) (bold(C) times.o M, M).
  $
  #source(217)The map $bold(C) -> bold(C)_(zeta_i)$ given by the augmentation
  $bold(C)_(zeta_j) -> R$ for $j != i$ gives rise to a map of spectral sequences
  to the above spectral sequence from
  $
    E_2^(p q) (zeta_i) = Ext^p_(R G) (H_q (bold(C)_(zeta_i)), Hom_R (M, M))
    => Ext^(p+q)_(R G) (bold(C)_(zeta_i) times.o M, M).
  $
  The latter spectral sequence was examined in the lemma, where it was shown
  that the differential $d_(n_i)$ is given by
  $d_(n_i) (alpha . tilde(zeta)_i) = alpha . zeta_i$. It follows that the same
  formula holds in the original spectral sequence $E_j^(p q)$.

  Now $E_2^(**)$ is finitely generated as a module over $E_2^(* 0)$ (it is
  $E_2^(* 0)$ tensored with a free $R$-module dual to $H_* (bold(C))$). Since
  the differentials are $E_2^(* 0)$-module homomorphisms, it follows that
  $E_infinity^(**)$ is also finitely generated as a module over $E_2^(* 0)$. But
  the elements $zeta_1, dots, zeta_c$ in the kernel of
  $E_2^(* 0) -> E_infinity^(* 0)$ act as zero on $E_infinity^(**)$, and so
  $E_infinity^(**)$ is finitely generated as a module over
  $
    E_2^(* 0) slash (zeta_1, dots, zeta_c) =
    Ext^*_(R G) (M, M) slash (zeta_1, dots, zeta_c).
  $
  Since $Ext^*_(R G) (M, M)$ is finitely generated as a module over the subring
  generated by the images of $zeta_1, dots, zeta_c$, the quotient by the images
  of multiplication by these elements is a finitely generated $R$-module. It
  follows that $E_infinity^(**)$ is a finitely generated $R$-module, and hence
  so is $Ext^*_(R G) (bold(C) times.o M, M)$.

  Finally, the spectral sequence
  $
    Ext^p_(R G) (bold(C) times.o M, H_(-q) (bold(C)) times.o M) =>
    Ext^(p+q)_(R G) (bold(C) times.o M, bold(C) times.o M)
  $
  has as its $E_2$ term a finite number of non-zero rows, each isomorphic to a
  finite direct sum of copies of $Ext^*_(R G) (bold(C) times.o M, M)$. So the
  $E_2$ term is a finitely generated $R$-module, and hence so are the
  $E_infinity$ term and $Ext^*_(R G) (bold(C) times.o M, bold(C) times.o M)$.
]

#corollary(closed: true)[
  Suppose $zeta_1, dots, zeta_c in H^* (G, ZZ)$ are homogeneous elements
  generating a subring over which $H^* (G, ZZ)$ is finitely generated as a
  module. Then for any (commutative) coefficient ring $R$,
  $bold(C) = R times.o_ZZ bold(C)_(zeta_1) times.o dots.c times.o
  bold(C)_(zeta_c)$ is a finite complex of projective $R G$-modules with
  $H_0 (bold(C)) tilde.equiv R$, and $H_i (bold(C))$ is a direct sum of copies
  of $R$ for all $i$.
] <cor:finite-complex-integral>

#remark[
  The existence of a finite complex $bold(C)$ of projective $R G$-modules with
  $H_i (bold(C))$ a direct sum of copies of $R$ for all $i$, as in the theorem,
  can also be proved topologically as follows. A faithful complex representation
  of $G$ gives rise to an embedding into a compact unitary group
  $G arrow.r.hook U(n)$. If we choose a cellular division of $U(n)$ such that
  the image of a cell under the action of $G$ is always a cell, then the complex
  of cellular chains with values in $R$ is a chain complex of free
  $R G$-modules. Since $U(n)$ is connected, every element of $G$ acts in a way
  which may be deformed to the identity, and hence trivially on homology.
]
