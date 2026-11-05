#import "main-defs.typ": *
#import "statements.typ": *

== The variety of an indecomposable $k G$-module is connected
<sec:connectedness>

This section is devoted to a generalisation of
Corollary~@cor:periodic-variety-line to arbitrary (not necessarily periodic)
finitely generated modules.

#theorem(title: [Carlson [@bib:Carlson1984]])[
  If $M$ is a finitely generated $k G$-module and $V_G (M) = V_1 union V_2$ with
  $V_1 inter V_2 = {0}$ then $M tilde.equiv M_1 plus.o M_2$ with
  $V_G (M_1) = V_1$ and $V_G (M_2) = V_2$.
] <th:carlson-connectedness>
#idx(
  "Carlson's",
  "connectedness theorem",
  target: [@th:carlson-connectedness],
)#idx(
  "connectedness theorem, Carlson's",
  target: [@th:carlson-connectedness],
)#idx(
  "theorem",
  "Carlson's connectedness",
  target: [@th:carlson-connectedness],
)

#proof[
  We prove this theorem by induction on $dim V_1 + dim V_2$. The case where
  either $V_1$ or $V_2$ is ${0}$ is clear, so we shall assume both are non-zero.
  Thus we may choose homogeneous elements $zeta_1$ of degree $r$ and $zeta_2$ of
  degree $s$ such that $V_1 subset.eq V_G chevron.l zeta_1 chevron.r$,
  $dim(V_2 inter V_G chevron.l zeta_1 chevron.r) = dim V_2 - 1$,
  $V_2 subset.eq V_G chevron.l zeta_2 chevron.r$ and
  $dim(V_1 inter V_G chevron.l zeta_2 chevron.r) = dim V_1 - 1$. Since
  $V_G chevron.l zeta_1 zeta_2 chevron.r = V_G chevron.l zeta_1 chevron.r
  union V_G chevron.l zeta_2 chevron.r supset.eq V_1 union V_2 = V_G (M)$, some
  power of $zeta_1 zeta_2$ lies in $I_G (M)$. So by replacing $zeta_1$ and
  $zeta_2$ by suitable powers if necessary we may assume that $zeta_1 zeta_2$
  annihilates $Ext^*_(k G) (M, M)$. Thus by
  Proposition~@prop:annihilator-criterion we have
  $
    L_(zeta_1 zeta_2) times.o M tilde.equiv Omega M plus.o Omega^(r+s) M
    plus.o ("projective").
  $
  Also, by Lemma~@lem:l-zeta-product-sequence there is a short exact sequence
  $
    0 -> Omega^r L_(zeta_2) -> L_(zeta_1 zeta_2) plus.o ("projective")
    -> L_(zeta_1) -> 0
  $
  #source(207)so that tensoring with $M$ we obtain a sequence of the form
  $
    0 -> Omega^r L_(zeta_2) times.o M -> Omega^(r+s) M plus.o Omega M plus.o
    ("projective") -> L_(zeta_1) times.o M -> 0.
  $
  By Proposition~@prop:variety-dual-omega, Proposition~@prop:l-zeta-variety and
  Theorem~@th:variety-tensor-product,
  $V_G (Omega^r L_(zeta_2) times.o M) = V_G chevron.l zeta_2 chevron.r
  inter V_G (M) = (V_1 inter V_G chevron.l zeta_2 chevron.r) union V_2$, so that
  by the inductive hypothesis
  $Omega^r L_(zeta_2) times.o M tilde.equiv N_1 plus.o N_2$ with
  $V_G (N_1) = V_1 inter V_G chevron.l zeta_2 chevron.r$ and $V_G (N_2) = V_2$.
  Similarly
  $V_G (L_(zeta_1) times.o M) = V_G chevron.l zeta_1 chevron.r inter V_G (M)
  = V_1 union (V_2 inter V_G chevron.l zeta_1 chevron.r)$
  so that by the inductive hypothesis
  $L_(zeta_1) times.o M tilde.equiv N'_1 plus.o N'_2$ with $V_G (N'_1) = V_1$
  and $V_G (N'_2) = V_2 inter V_G chevron.l zeta_1 chevron.r$.

  Since $V_G (N'_1) inter V_G (N_2) = V_1 inter V_2 = {0}$, it follows from
  Corollary~@cor:ext-vanishing that we have $Ext^1_(k G) (N'_1, N_2) = 0$.
  Similarly $V_G (N'_2) inter V_G (N_1) subset.eq V_1 inter V_2 = {0}$ so that
  we have $Ext^1_(k G) (N'_2, N_1) = 0$. It is easy to see that this forces the
  above sequence to decompose as a direct sum of two sequences of the form
  $0 -> N_1 -> N''_1 -> N'_1 -> 0$ and $0 -> N_2 -> N''_2 -> N'_2 -> 0$ with
  $V_G (N''_1) subset.eq V_1$ and $V_G (N''_2) subset.eq V_2$. By the
  Krull–Schmidt theorem and the invariance of varieties under $Omega$, the
  decomposition
  $
    Omega^(r+s) M plus.o Omega M plus.o ("projective") tilde.equiv N''_1
    plus.o N''_2
  $
  forces $M$ to decompose as $M_1 plus.o M_2$ with $V_G (M_1) subset.eq V_1$ and
  $V_G (M_2) subset.eq V_2$. Since $V_G (M) = V_1 union V_2$ this forces
  $V_G (M_1) = V_1$ and $V_G (M_2) = V_2$.
]

#corollary(closed: true)[
  If $M$ is a finitely generated indecomposable $k G$-module, then the
  projective variety $macron(V)_G (M)$ is connected in the Zariski topology.
] <cor:projective-variety-connected>
