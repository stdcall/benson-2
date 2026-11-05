#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-04-double-complex.typ": double-complex, layer-sequence

== The spectral sequence of a double complex <sec:double-complex>
#idx(
  "spectral sequence",
  "of a double complex",
  target: [@sec:double-complex],
)

In this section we set up the spectral sequence of a double complex. We shall
work in cohomology rather than homology, and again the theory works equally well
in either. We shall see that the $E_2$ term is easier to understand in this case
than in the case of a filtered complex.

#definition[
  A *double complex*#idx("complex", "double")#idx("double", "complex") is a
  collection of abelian groups (or modules, etc.) and maps arranged as in the
  following diagram:
  $ #double-complex $
  such that the following conditions are satisfied:
  + Each row satisfies $d_1 compose d_1 = 0$.
  + Each column satisfies $d_0 compose d_0 = 0$.
  + $d_0 compose d_1 + d_1 compose d_0 = 0$.

  The *total complex*#idx("complex", "total")#idx("total", "complex") of a
  double complex, $bold(X)^n = Tot(bold(E))$ is given by
  $ bold(X)^n = plus.o.big_(i+j=n) E_0^(i j) $
  with differential
  $ d = d_0 + d_1 : bold(X)^n -> bold(X)^(n+1). $
  Note that the above conditions imply that $d compose d = 0$.
] <def:double-complex>

Given a double complex $bold(E)$, its total complex is _filtered_ as follows.
$
  D_0^(p q) = F^p bold(X)^(p+q) = plus.o.big_(i+j=p+q \ i >= p) E_0^(i j)
$
Thus
$
  F^p bold(X)^(p+q) slash F^(p+1) bold(X)^(p+q) tilde.equiv E_0^(p q)
$
#source(119)and so each layer in the filtration should be thought of as a single
_column_ of the double complex. The differential on this quotient is just
$d_0 : E_0^(p q) -> E_0^(p,q+1)$, since $d_1$ maps into a lower layer. So we
have
$
  E_1^(p q) = H(E_0^(p q), d_0), quad
  D_1^(p q) = H(E_0^(p q) plus.o E_0^(p+1,q-1) plus.o dots.c, d_0 + d_1)
$

Now we have two things called $d_1$, and so we had better check that their
meanings are related in some obvious way. Until we have done so, we shall refer
to the horizontal differential in the double complex as $d_1$, and to
$j_1 compose k_1$ as "$d_1$".

If $x in E_0^(p q)$ with $d_0 (x) = 0$, so that $x$ represents a class
$[x] in E_1^(p q)$, then we compute $k_1 [x]$ as follows. Recall that $k_1$ is
defined as the boundary homomorphism associated to the short exact sequence of
chain complexes
$
  0 -> F^(p+1) bold(X) -> F^p bold(X) -> F^p bold(X) slash F^(p+1) bold(X)
  -> 0
$
i.e.,
$ #layer-sequence $
Since $d_0 (x) = 0$ we have $(d_0 + d_1)(x, 0, dots) = (0, d_1 (x), 0, dots)$,
and so by the definition of the boundary homomorphism (switchback map) we have
$k_1 [x] = [(d_1 (x), 0, dots)]$. Hence
$ “d_1” [x] = j_1 k_1 [x] = [d_1 (x)], $
and so from now on we omit the inverted commas. Thus we have
$ E_2^(p q) = H^p (H^q (bold(E)_0, d_0), d_1) $
where the $d_1$ is the map induced by the $d_1$ of the double complex.

We summarise this in the following theorem:

#theorem[
  Given a double complex $(E_0^(p q), d_0, d_1)$ there is a spectral sequence
  with
  $
           E_1^(p q) & = H(E_0^(p q), d_0) \
           E_2^(p q) & = H^p (H^q (bold(E)_0, d_0), d_1) \
    E_infinity^(p q) & = F^p H^(p+q) (Tot(bold(E)_0)) slash
                       F^(p+1) H^(p+q) (Tot(bold(E)_0)).
  $
] <th:double-complex-sequence>

#source(120)The shorthand for this theorem is
$
  H^p (H^q (bold(E)_0, d_0), d_1) =>
  H^(p+q) (Tot(bold(E)_0), d_0 + d_1).
$

It may now be seen that $(E_0, d_0)$ and $(E_1, d_1)$ are natural precursors of
the remaining pages $(E_n, d_n)$, $n >= 2$, and $d_0$ and $d_1$ have the "right"
degrees.

The vertical edge homomorphism for the spectral sequence of a double complex may
be described as follows. There is a restriction map
$ H^q (Tot(bold(E)_0)) -> H^q (E_0^(0 *), d_0) $
whose image lies in the kernel of $d_1$, and hence this defines a map
$ H^q (Tot(bold(E)_0)) limits(arrow.r)^(e') E_2^(0 q), $
which is just the edge homomorphism.

#remark[
  By reversing the rôles of $p$ and $q$ in the double complex (and multiplying
  all the maps by the appropriate signs) we see that there are actually two
  distinct spectral sequences associated to a double complex, and both
  converging to $H^* (Tot(bold(E)_0))$. These are sometimes written
  $attach(E, bl: I, br: n, tr: p q)$ and $attach(E, bl: I I, br: n, tr: p q)$.
  It is often useful to compare these two spectral sequences, especially in case
  one has $E_2 = E_infinity$ and the other does not. See for example the Künneth
  spectral sequence in Section~@sec:kunneth-sequence.
]

As an example of the spectral sequence of a double complex, we have the
*hypercohomology spectral sequence*#idx(
  "hypercohomology spectral sequence",
)#idx("spectral sequence", "hypercohomology"). Recall from Section~2.7 of
Volume~I that hypercohomology is just Ext for chain complexes.

#proposition[
  Suppose that $bold(C)$ and $bold(D)$ are chain complexes of $Lambda$-modules,
  with $bold(C)$ bounded below and $bold(D)$ bounded above. Then there are
  spectral sequences
  $
    Ext^p_Lambda (H_q (bold(C)), bold(D)) =>
    Ext^(p+q)_Lambda (bold(C), bold(D)),
    quad
    Ext^p_Lambda (bold(C), H_(-q) (bold(D))) =>
    Ext^(p+q)_Lambda (bold(C), bold(D)).
  $
] <prop:hypercohomology>

#proof[
  If $bold(P)$ is a projective resolution of $bold(C)$, and $bold(I)$ is an
  injective resolution of $bold(D)$, then these are the spectral sequences
  coming from the double complexes $bold(Hom)_Lambda (bold(C), bold(I))$ and
  $bold(Hom)_Lambda (bold(P), bold(D))$.
]

As an example of the homology spectral sequence of a double complex, we prove
the following, which should be compared with the Künneth Theorem (Section~2.7 of
Volume~I).

#proposition[
  Suppose $bold(C)$ and $bold(D)$ are chain complexes of right, resp. left
  $Lambda$-modules, concentrated in non-negative degrees, such that $bold(C)$
  consists of projective $Lambda$-modules and $bold(D)$ is exact in positive
  degrees with $H_0 (bold(D))$ flat. Then
  $H_* (bold(C) times.o_Lambda bold(D)) tilde.equiv
  H_* (bold(C)) times.o_Lambda H_0 (bold(D))$. In particular, if $bold(C)$ is
  also exact in positive degrees, then so is $bold(C) times.o_Lambda bold(D)$,
  and $H_0 (bold(C) times.o_Lambda bold(D)) tilde.equiv
  H_0 (bold(C)) times.o_Lambda H_0 (bold(D))$.#ed-note[The book states the
    proposition without the hypothesis that $H_0 (bold(D))$ be flat, and then
    both conclusions fail: for $Lambda = ZZ$, $bold(C) = (ZZ limits(->)^2 ZZ)$
    in degrees one and zero and $bold(D) = ZZ slash 2$ in degree zero,
    $H_1 (bold(C) times.o bold(D)) tilde.equiv ZZ slash 2$ while
    $H_1 (bold(C)) times.o H_0 (bold(D)) = 0$. In general the argument gives
    $H_* (bold(C) times.o_Lambda bold(D))
    tilde.equiv H_* (bold(C) times.o_Lambda H_0 (bold(D)))$; see Weibel
    [@bib:Weibel1994, Application 5.7.8 and Theorem 3.6.2].]
] <prop:tensor-homology>

#proof[
  Consider the spectral sequence of the double complex
  $bold(C) times.o_Lambda bold(D)$. Since $bold(C)$ consists of projective
  modules and $bold(D)$ is exact in positive degrees, the #source(121)columns of
  $bold(C) times.o_Lambda bold(D)$ are exact in positive degrees. So
  $E^1_(p q) = 0$ for $q > 0$, and hence $E^2_(p q) tilde.equiv
  E^infinity_(p q)$. So we have
  $
    H_p (bold(C) times.o_Lambda bold(D)) tilde.equiv E^infinity_(p 0)
    tilde.equiv E^2_(p 0)
    tilde.equiv H_p (bold(C) times.o_Lambda H_0 (bold(D)))
    tilde.equiv H_p (bold(C)) times.o_Lambda H_0 (bold(D)).
  $
]
