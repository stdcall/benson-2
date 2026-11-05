#import "main-defs.typ": *
#import "statements.typ": *

== The spectral sequence of a group extension <sec:group-extension>
#idx(
  "spectral sequence",
  "of a group extension",
  target: [@sec:group-extension],
)#idx(
  "group",
  "extension",
  "spectral sequence of",
  target: [@sec:group-extension],
)

Suppose $N$ is a normal subgroup of $G$ and $M$ is an $R G$-module. Our goal in
this section is to construct the Lyndon–Hochschild–Serre spectral sequences
$
  H_p (G slash N, H_q (N, M)) => H_(p+q) (G, M), quad
  H^p (G slash N, H^q (N, M)) => H^(p+q) (G, M)
$
and we shall concentrate on the latter. The former is treated dually.

We take a projective resolution of $R$ as an $R(G slash N)$-module
$
  dots.c -> P_1 limits(arrow.r.long)^(partial_1) P_0
  limits(arrow.r.long)^(partial_0) R -> 0
$
and as an $R G$-module
$
  dots.c -> Q_1 limits(arrow.r.long)^(partial'_1) Q_0
  limits(arrow.r.long)^(partial'_0) R -> 0.
$
We form the double complex
$ E_0^(p q) = Hom_(R(G slash N)) (P_p, Hom_(R N) (Q_q, M)). $
Note that $Hom_(R N) (Q_q, M)$ admits a $G$-action whose restriction to $N$ is
trivial, so that we may regard it as an $R(G slash N)$-module. The differentials
in this double complex are given by taking $d_0$ to be $(-1)^p$ times the
differential induced by $partial'_q$ and $d_1$ to be the differential induced by
$partial_p$. The signs ensure that $d_0 compose d_1 = -d_1 compose d_0$.

By Theorem~@th:double-complex-sequence we have a spectral sequence with
$
  E_1^(p q) & = Hom_(R(G slash N)) (P_p, H^q (N, M)) \
  E_2^(p q) & = H^p (G slash N, H^q (N, M)).
$

#remark[
  The above double complex is the algebraic analogue of the construction of the
  fibration $B G -> B(G slash N)$ with fibre $B N$, given in
  Theorem~@th:classifying-fibrations, using the space $E(G slash N) times E G$.
]

It remains to identify $E_infinity^(p q)$.

#lemma[
  $
    Hom_(R(G slash N)) (P_p, Hom_(R N) (Q_q, M)) tilde.equiv
    Hom_(R G) (P_p times.o_R Q_q, M)
  $
  (In the right hand side of this formula, $P_p$ is regarded as an $R G$-module
  with $N$ acting trivially).
] <lem:hom-tensor>

#proof[
  We define maps
  $
    phi.alt : Hom_(R(G slash N)) (P_p, Hom_(R N) (Q_q, M))
    -> Hom_(R G) (P_p times.o Q_q, M) \
    phi.alt(f)(x times.o y) = f(x)(y) \
    psi : Hom_(R G) (P_p times.o Q_q, M)
    -> Hom_(R(G slash N)) (P_p, Hom_(R N) (Q_q, M)) \
    psi(alpha)(x)(y) = alpha(x times.o y).
  $
  #source(122)It is easy to check that these maps are well defined and inverses
  to each other.
]

Now by Corollary~2.7.3 of Volume~I, the total complex of
$bold(P) times.o bold(Q)$ is exact, and is hence a projective resolution of $R$
by $R G$-modules. So by the above lemma we have
$
  H^* (Tot(E_0), d_0 + d_1) tilde.equiv
  H^* (Hom_(R G) (Tot(bold(P) times.o bold(Q)), M), partial + partial')
  tilde.equiv H^* (G, M).
$

Thus the spectral sequence of Theorem~@th:double-complex-sequence becomes
$ H^p (G slash N, H^q (N, M)) => H^(p+q) (G, M). $

In exactly the same way, if $M_1$ is an $R(G slash N)$-module (which we also
regard as an $R G$-module with $N$ acting trivially) and $M_2$ and $M_3$ are
$R G$-modules, with $M_1$ or $M_2$ flat as an $R$-module, we let $bold(P)$ be a
resolution of $M_1$ as an $R(G slash N)$-module and $bold(Q)$ be a resolution of
$M_2$ as an $R G$-module. We obtain a spectral sequence
$
  Ext^p_(R(G slash N)) (M_1, Ext^q_(R N) (M_2, M_3)) =>
  Ext^(p+q)_(R G) (M_1 times.o_R M_2, M_3).
$

#exercise[
  Show that in the spectral sequence
  $ H^* (G slash N, H^* (N, M)) => H^* (G, M) $
  the horizontal edge homomorphism
  $ H^* (G slash N, M^N) limits(arrow.r)^e H^* (G, M) $
  is the composite of the inflation
  $ inf_(G, N) : H^* (G slash N, M^N) -> H^* (G, M^N) $
  with the map $H^* (G, M^N) -> H^* (G, M)$ induced by the inclusion. This
  composite is also called the inflation map.

  Show that the vertical edge homomorphism
  $ H^* (G, M) limits(arrow.r)^(e') H^* (N, M)^(G slash N) $
  is the restriction map $res_(G, N)$.
]

Thus the five term sequence associated to this spectral sequence
(Proposition~@prop:five-term-cohomology) is
$
  0 -> H^1 (G slash N, M^N) limits(arrow.r.long)^inf H^1 (G, M)
  limits(arrow.r.long)^res H^1 (N, M)^(G slash N) \
  limits(arrow.r.long)^(d_2) H^2 (G slash N, M^N) limits(arrow.r.long)^inf
  H^2 (G, M).
$
This is called the *inflation-restriction sequence*#idx(
  "inflation-restriction sequence",
)#idx("sequence", "inflation-restriction").

Dually, we have a homology spectral sequence
$ H_p (G slash N, H_q (N, M)) => H_(p+q) (G, M) $
and a five term sequence (Proposition~@prop:five-term-homology) is
$
  H_2 (G, M) -> H_2 (G slash N, M_N) -> H_1 (N, M)_(G slash N) \
  -> H_1 (G, M) -> H_1 (G slash N, M_N) -> 0.
$
#source(123)Here, $M_G$ denotes the quotient of $M$ given by identifying $m$
with $g m$ for all $m in M$ and $g in G$.
