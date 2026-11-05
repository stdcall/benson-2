#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-01-spectral-sequences-intro.typ": (
  pullback-fibrations, second-homology-page, second-page, third-page,
  topic-guide,
)

== Introduction to spectral sequences <sec:spectral-sequences-intro>

A _spectral sequence_#idx("spectral sequence")#idx("sequence", "spectral") is a
fairly complicated algebraic gadget for making calculations in homological
algebra. In this chapter, we shall introduce the machinery of spectral
sequences, and show how to apply them in a number of different situations. The
most important spectral sequence for us will be the Lyndon–Hochschild–Serre
spectral sequence#idx("Lyndon–Hochschild–Serre", "spectral sequence")#idx(
  "spectral sequence",
  "Lyndon–Hochschild–Serre",
) associated to a group extension. The reader who wishes to avoid topology can
read the sections on the spectral sequence of a filtered complex, a double
complex and a group extension for an account of this spectral sequence. As
always, we shall only give a sketchy account of the topological aspects of the
material anyway, and make the algebraic aspects as self-contained as possible.

This introduction is designed for the orientation of the reader, and is not
necessary for the logical structure of what follows.

Here is a guide to the interconnections between the various topics introduced in
this chapter.#idx("fibration", "Hurewicz")#idx("Hurewicz", "fibration")#idx(
  "bundle",
  "fibre",
)#idx("fibre", "bundle")#idx("group", "extension")#idx(
  "composite functor",
)#idx("functor", "composite")#idx("pullback", "of fibrations")#idx(
  "Eilenberg",
  "–Moore spectral sequence",
)#idx("spectral sequence", "Eilenberg–Moore")#idx("fibration", "Serre")#idx(
  "Serre",
  "fibration",
)#idx("complex", "double")#idx("double", "complex")#idx(
  "complex",
  "filtered",
)#idx("filtered complex")#idx("exact", "couple")
$ #topic-guide $

Thus we shall be interested in the following spectral sequences. $R$ will always
denote a commutative ring of coefficients.

+ If $F -> E -> B$ is a Serre fibration then there are spectral sequences in
  cohomology and homology,
  $
    H^p (B; H^q (F; R)) => H^(p+q) (E; R), quad
    H_p (B; H_q (F; R)) => H_(p+q) (E; R).
  $
  This notation is meant to suggest that the left-hand side is the initial data
  for the calculation and the right-hand side is what we wish to calculate.
  There are certain "differentials"#idx("differential") and "extension
  problems"#idx("extension", "problem") involved in going from the left to the
  right, and this makes up the inner workings of the spectral sequence, of which
  more later.

  #source(106)In fact there is a technical difficulty here. The group $pi_1 (B)$
  acts in a natural way on $H^* (F; R)$, and if the action is not trivial, we
  should really regard $H^* (F; R)$ as a _local system of coefficients_#idx(
    "local",
    "system of coefficients",
  ) $cal(H)^* (F; R)$ on $B$, and the spectral sequence takes the form
  $ H^p (B; cal(H)^q (F; R)) => H^(p+q) (E; R) $
  (and similarly in homology). We shall simplify the exposition by making the
  assumption that $pi_1 (B)$ acts trivially on $H^* (F; R)$.

  If one wishes to develop the spectral sequence of a group extension
  topologically, one has to treat these more general local systems, unless the
  normal subgroup is central. Thus we shall be content to set up the spectral
  sequence of a group extension algebraically. This is our next topic.
+ If $N$ is a normal subgroup of a (not necessarily finite) group $G$ then the
  fibration $B N -> B G -> B(G slash N)$ gives rise to spectral sequences
  $
    H^p (G slash N, H^q (N, R)) => H^(p+q) (G, R), quad
    H_p (G slash N, H_q (N, R)) => H_(p+q) (G, R).
  $

  More generally, if $M$ is an $R G$-module (not necessarily trivial!) then
  there are spectral sequences
  $
    H^p (G slash N, H^q (N, M)) => H^(p+q) (G, M), quad
    H_p (G slash N, H_q (N, M)) => H_(p+q) (G, M).
  $
  The latter is known as the Lyndon–Hochschild–Serre spectral sequence of the
  group extension. We set up these spectral sequences algebraically, using the
  theory of double complexes, and concentrate on the case of cohomology. This is
  because in cohomology the spectral sequence $H^* (G slash N, H^* (N, R))$ has
  a ring structure over which the spectral sequence
  $H^* (G slash N, H^* (N, M))$ is a module.
+ We shall give a brief sketch of the Eilenberg–Moore spectral sequence
  $
    Tor^(**)_(H^* (B; R)) (H^* (B'; R), H^* (E; R)) => H^* (E'; R)
  $
  associated to a pullback of fibrations
  $ #pullback-fibrations $
  in which $pi_1 (B)$ acts trivially on $H^* (F; R)$.

  In the case where $B'$ consists of just the basepoint of $B$, we have
  $E' = F$, and so the spectral sequence takes the form
  $ Tor^(**)_(H^* (B; R)) (R, H^* (E; R)) => H^* (F; R) $
  so that it computes the cohomology of the fibre from that of the base space
  and total space.

  One situation of interest in which we can apply this spectral sequence is the
  case of the fibration
  $ K(G, 1) -> K(G slash Z, 1) -> K(Z, 2) $
  #source(107)of Eilenberg–Mac~Lane spaces, where $Z$ is a central subgroup#idx(
    "central extension",
  )#idx("group", "central extension")#idx(
    "group",
    "extension",
    "central",
  ) of $G$. Dave Rusin [@bib:Rusin1989] has used this to calculate the mod 2
  cohomology of all groups of order 32 (there are 51 of them!). The point is
  that there are fewer non-zero differentials (and very often none at all) than
  in the Lyndon–Hochschild–Serre spectral sequence associated to the same group
  extension.
+ Using the Bott periodicity theorem in $K$-theory, one can obtain a spectral
  sequence
  $ H^* (G, ZZ) => R(G)^and $
  due to Atiyah, going from the integral cohomology ring to the completion of
  the ordinary character ring at the augmentation ideal. Again, we shall only
  sketch the construction of this spectral sequence.

We now explain in a little more detail how spectral sequences arise.

#enum(numbering: "(1)")[Given a CW-complex $X$ and a sequence of subcomplexes
  $ X_0 subset.eq X_1 subset.eq dots.c subset.eq X = union.big X_i $
  we get a long exact sequence for each adjacent pair
  $
    dots.c -> H^n (X_(p-1); R) -> H^n (X_p; R) -> H^n (X_p, X_(p-1); R) \
    -> H^(n+1) (X_(p-1); R) -> dots.c
  $
  $
    dots.c -> H_n (X_(p-1); R) -> H_n (X_p; R) -> H_n (X_p, X_(p-1); R) \
    -> H_(n-1) (X_(p-1); R) -> dots.c
  $
  which interlock in a way we shall examine more closely later. What we wish to
  do is to assemble all this data in a sensible fashion and use it to calculate
  $H^* (X; R)$.
][We did not really need a CW-complex in order to carry this out. All we needed
  was a (co)chain complex $bold(X)$ (which might be the (co)chains on a
  CW-complex, or might arise from projective resolutions of modules, or anything
  else), and a sequence of subcomplexes
  $
    bold(X) = F^0 bold(X) supset.eq F^1 bold(X) supset.eq dots.c supset.eq
    inter.big F^i bold(X) = {0}. \
    F_0 bold(X) subset.eq F_1 bold(X) subset.eq dots.c subset.eq bold(X) =
    union.big F_i bold(X).
  $
][If $p : E -> B$ is a Serre fibration of CW-complexes, we take as our
  subcomplexes of $E$ the preimages of the skeletal filtration of $B$.
  $
    p^(-1) (B^0) subset.eq p^(-1) (B^1) subset.eq dots.c subset.eq E =
    union.big p^(-1) (B^i).
  $
  By taking (co)chains we have filtrations as above:
  $
    F^i bold(X) = Ker(C^* (E) -> C^* (p^(-1) (B^(i-1)))), quad
    F_i bold(X) = C_* (p^(-1) (B^i)).
  $
  In this case it turns out that under suitable hypotheses, the initial data for
  the spectral sequence amounts to knowing $H^* (B; H^* (F; R))$, and so we can
  use this to calculate $H^* (E; R)$.
]

#source(108)Before we set up spectral sequences in detail, we now try to give
some of the flavour of what a spectral sequence looks like. You are not expected
to understand yet where all the information is coming from.

The initial data usually comes as a doubly indexed set of abelian groups (or
$R$-modules). This is written as $E_2^(p q)$ in cohomology or $E^2_(p q)$ in
homology#idx("$E_n^(p q)$, $E^n_(p q)$") (the reason for the 2 will only become
apparent when we come to study the spectral sequence of a double complex). For
example for a group extension we have
$
  E_2^(p q) = H^p (G slash N, H^q (N, R)), quad
  E^2_(p q) = H_p (G slash N, H_q (N, R)).
$
These are examples of _first quadrant_#idx("first quadrant") spectral sequences,
where $E_2^(p q)$ (resp. $E^2_(p q)$) is zero whenever $p < 0$ or $q < 0$.

The next piece of data is that there is a naturally defined _differential_
$d_2 : E_2^(p q) -> E_2^(p+2,q-1)$ satisfying $d_2 compose d_2 = 0$. This
information is usually depicted diagrammatically as follows.
$ #second-page $ <fig:second-page>
Thus we may form the homology of this complex
$
  E_3^(p q) = H(E_2^(p q), d_2) = frac(
    Ker(d_2 : E_2^(p q) -> E_2^(p+2,q-1)),
    Im(d_2 : E_2^(p-2,q+1) -> E_2^(p q)),
  ).
$

On $E_3^(p q)$ there is a naturally defined differential
$d_3 : E_3^(p q) -> E_3^(p+3,q-2)$ satisfying $d_3 compose d_3 = 0$ as in the
following diagram, and we define $E_4^(p q) = H(E_3^(p q), d_3)$, and continue
in this way.
$ #third-page $ <fig:third-page>

#source(109)Now for a given $p$ and $q$, for $n$ large enough (e.g.
$n > max(p, q + 1)$) we have
$
  d_n : E_n^(p q) -> E_n^(p+n,q-n+1) = 0, quad
  d_n : 0 = E_n^(p-n,q+n-1) -> E_n^(p q)
$
and so $E_(n+1)^(p q) = E_n^(p q)$. Thus we may define $E_infinity^(p q)$ to be
the common value of $E_n^(p q)$ for $n$ large. If the spectral sequence is not
first quadrant, there are slightly more delicate convergence problems, but the
reader should not worry about that at this stage.

The way $E_infinity^(p q)$ is related to what we are trying to calculate is as
follows. There is a filtration
$
  H^(p+q) (G, R) = F^0 H^(p+q) (G, R) supset.eq F^1 H^(p+q) (G, R) supset.eq \
  dots.c supset.eq F^(p+q+1) H^(p+q) (G, R) = 0
$
such that
$
  boxed(
    F^p H^(p+q) (G, R) slash
    F^(p+1) H^(p+q) (G, R) tilde.equiv E_infinity^(p q).
  )
$
In other words, the group $H^n (G, R)$ has a filtration in which the quotients
are the groups going down a trailing diagonal $p + q = n$ of the $E_infinity$
term of the spectral sequence.

Similarly in homology we have
$
  d^n : E^n_(p q) -> E^n_(p-n,q+n-1), wide d^n compose d^n = 0, \
  E^(n+1)_(p q) = frac(
    Ker(d^n : E^n_(p q) -> E^n_(p-n,q+n-1)),
    Im(d^n : E^n_(p+n,q-n+1) -> E^n_(p q)),
  )
$
and a filtration
$
  0 = F_(-1) H_(p+q) (G, R) subset.eq F_0 H_(p+q) (G, R) subset.eq dots.c
  subset.eq F_(p+q) H_(p+q) (G, R) = H_(p+q) (G, R)
$
such that
$
  F_p H_(p+q) (G, R) slash F_(p-1) H_(p+q) (G, R) tilde.equiv
  E^infinity_(p q).
$
Here is a picture of $E^2_(p q)$.
$ #second-homology-page $

We refer to $E_n^(p q)$ (resp. $E^n_(p q)$) as the $n$th _page_#idx("page") of
the spectral sequence.
