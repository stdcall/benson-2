#import "main-defs.typ": *
#import "statements.typ": *

== Poincaré series and complexity <sec:poincare-series>

Let $V$ be a graded vector space of *finite type*#idx("finite", "type") over
$k$. In other words,
$ V = plus.o.big_(r gt.eq 0) V_r $
with each $V_r$ a finite dimensional vector space over $k$. We define the
*Poincaré series*#idx("Poincaré", "series")#idx("series, Poincaré") of $V$ to be
$ p(V, t) = sum_(r gt.eq 0) t^r dim_k V_r $
#idx("$p(V, t)$")as a formal power series in the indeterminate $t$. Thus for
example if $V = k[x_1, dots, x_n]$ is a polynomial ring#idx(
  "polynomial",
  "ring",
)#idx("ring", "polynomial") in generators $x_i$ of degree one, then $V_r$ is the
$r$th symmetric power#idx("symmetric", "power")#idx("power, symmetric") of the
$n$ dimensional vector space $V_1$, and so
$ p(V, t) = 1 + n t + n(n + 1)t^2 slash 2 + dots.c = 1 slash (1 - t)^n. $
As another example, if $V = k{x_1, x_2}$ is the free ring#idx(
  "free",
  "ring",
)#idx("ring", "free") on two non-commuting generators $x_1$ and $x_2$ of degree
one, then
$ p(V, t) = 1 + 2t + 4t^2 + 8t^3 + dots.c = 1 slash (1 - 2t). $

The following proposition shows that if $V$ is a finitely generated graded
module over a finitely generated commutative graded ring of finite type, then
$p(V, t)$ is a rational function of $t$ whose poles are at roots of unity.

#proposition(title: [Hilbert, Serre])[
  (see Atiyah–Macdonald [@bib:Atiyah1969], Theorem~11.1) Suppose that $A$ is a
  commutative graded ring of finite type over $k$, finitely generated over $A_0$
  by homogeneous elements $x_1, dots, x_s$ in degrees $k_1, dots, k_s$. Suppose
  $V$ is a finitely generated graded $A$-module (i.e., we have
  $A_i . A_j subset.eq A_(i+j)$ and $A_i . V_j subset.eq V_(i+j)$). Then the
  Poincaré series $p(V, t)$ is of the form
  $ f(t) slash product_(j=1)^s (1 - t^(k_j)) $
  where $f(t)$ is a polynomial in $t$ with integer coefficients.
] <prop:hilbert-serre>

#proof[
  #source(170)We work by induction on $s$. If $s = 0$ then $p(V, t)$ is a
  polynomial, so suppose $s > 0$. Denoting by $K$ and $L$ the kernel and
  cokernel of multiplication by $x_s$, we have an exact sequence
  $ 0 -> K_r -> V_r limits(->)^(x_s) V_(r+k_s) -> L_(r+k_s) -> 0. $
  Now $K$ and $L$ are finitely generated graded modules for
  $A_0 [x_1, dots, x_(s-1)]$, and so by induction their Poincaré series have the
  given form. We have from the above exact sequence
  $ t^(k_s) p(K, t) - t^(k_s) p(V, t) + p(V, t) - p(L, t) + g(t) = 0 $
  where $g(t)$ is a polynomial of degree less than $k_s$ with integer
  coefficients. Thus
  $ p(V, t) = (p(L, t) - t^(k_s) p(K, t) - g(t)) slash (1 - t^(k_s)) $
  has the given form.
]

#remark[
  It doesn't matter for the proof of the above proposition whether the ring $A$
  is strictly commutative or only commutative in the graded sense
  $x y = (-1)^(deg(x) deg(y)) y x$. Of course, in the latter case $A$ is
  finitely generated as a module over the subring $A^"ev"$ of elements of even
  degree, and so we may always work with $A^"ev"$ if it makes us feel more
  comfortable. This will become a real issue when we come to study varieties,
  since most algebraic geometry texts are written for strictly commutative
  rings. The proofs usually carry over verbatim to the graded commutative case,
  but it is often not worth the trouble of saying so.
]

The following proposition shows that the rate of growth of the dimensions in a
graded module is determined by the order of the pole of the Poincaré series at
$t = 1$.

#proposition[
  Suppose
  $ p(t) = f(t) slash product_(j=1)^s (1 - t^(k_j)) = sum_(r gt.eq 0) a_r t^r $
  where $f(t)$ is a polynomial with integer coefficients and the $a_r$ are
  non-negative integers. Let $gamma$ be the order of the pole of $p(t)$ at
  $t = 1$. Then
  + there exists a constant $kappa > 0$ such that
    $a_n lt.eq kappa . n^(gamma - 1)$ for $n > 0$, but
  + if $gamma gt.eq 1$, there does not exist a constant $kappa > 0$ such that
    $a_n lt.eq kappa . n^(gamma - 2)$ for $n > 0$.
] <prop:pole-order-growth>

#proof[
  The hypothesis and conclusion remain unaltered if we replace $p(t)$ by
  $p(t) . (1 + t + dots.c + t^(k_j - 1))$, and so without loss of generality
  each $k_j = 1$. So we may suppose $p(t) = f(t) slash (1 - t)^gamma$ with
  $f(1) != 0$. Suppose $f(t) = alpha_m t^m + dots.c + alpha_0$. We have
  $
    a_n = alpha_0 binom(n + gamma - 1, gamma - 1)
    + alpha_1 binom(n + gamma - 2, gamma - 1) + dots.c
    + alpha_m binom(n + gamma - m - 1, gamma - 1).
  $
  #source(171)The condition $f(1) != 0$ implies that
  $alpha_0 + dots.c + alpha_m != 0$, so this expression is a polynomial of
  degree exactly $gamma - 1$ in $n$.
]

#definition[
  Suppose $V$ is a graded vector space of finite type whose Poincaré series
  $p(V, t)$ has the form $f(t) slash product_(j=1)^s (1 - t^(k_j))$ where $f(t)$
  is a polynomial with integer coefficients. Then we write $gamma(V)$#idx(
    "$gamma(V)$",
  ) for the order of the pole of $p(V, t)$ at $t = 1$. By the proposition, this
  measures the polynomial rate of growth of the $V_r$, so we call it the
  *growth*#idx("growth") of $V$.
] <def:growth>

If $V$ is a finitely generated graded module over a commutative graded ring $A$,
finitely generated and of finite type over $k$, then
Proposition~@prop:hilbert-serre shows that $gamma(V)$ is well defined. Clearly
if $0 -> V'' -> V' -> V -> 0$ is a short exact sequence of finitely generated
graded $A$-modules then $gamma(V')$ is equal to the maximum of $gamma(V)$ and
$gamma(V'')$. In particular, any finitely generated graded module $V$ is a
quotient of a direct sum of finitely many copies of $A$ by a graded ideal, and
so we have $gamma(V) lt.eq gamma(A)$.

Now suppose $M$ is a finitely generated $k G$-module with minimal resolution
$ dots.c -> P_2 -> P_1 -> P_0 -> M -> 0. $
Then the multiplicity of the projective cover $P_S$ of a simple $k G$-module $S$
as a summand of $P_r$ is equal to
$ dim_k Hom_(k G) (P_r, S) slash dim_k End_(k G) (S). $
Since the resolution is minimal, every homomorphism $P_r -> S$ is a cocycle, and
every coboundary is zero, so that
$ Hom_(k G) (P_r, S) tilde.equiv Ext^r_(k G) (M, S). $
Thus we have
$
  dim_k P_r = sum_(S "simple") dim_k P_S . dim_k Ext^r_(k G) (M, S) slash
  dim_k End_(k G) (S).
$
Since $Ext^*_(k G) (M, S)$ is a finitely generated graded module over the
finitely generated graded commutative ring $H^* (G, k) = Ext^*_(k G) (k, k)$, it
follows from Proposition~@prop:hilbert-serre that the Poincaré series
$p(Ext^*_(k G) (M, S), t)$ is of the form
$f(t) slash product_(j=1)^s (1 - t^(k_j))$, where $f(t)$ is a polynomial with
integer coefficients and the $k_j$ are the degrees of generators of
$H^* (G, k)$. Thus by the above formula for the dimension of $P_r$, the graded
vector space $P_*$ also has a Poincaré series of this form.

#definition[
  The *complexity*#idx("complexity") $c_G (M)$#idx("$c_G (M)$") of a finitely
  generated $k G$-module $M$ is the growth $gamma(P_*)$ of the minimal
  resolution $P_*$ of $M$.
] <def:complexity>

Now if $N$ is another finitely generated $k G$-module, then $Ext^r_(k G) (M, N)$
is a subquotient of $Hom_(k G) (P_r, N)$, and this is a subspace of
$Hom_k (P_r, N)$. Thus
$ dim_k Ext^r_(k G) (M, N) lt.eq dim_k P_r . dim_k N $
#source(172)and so
$ gamma(Ext^*_(k G) (M, N)) lt.eq gamma(P_*) = c_G (M). $

#proposition[
  We have
  $
    c_G (M) = gamma(Ext^*_(k G) (M, M)) = gamma(Z Ext^*_(k G) (M, M))
    = max_(S "simple") gamma(Ext^*_(k G) (M, S)).
  $
] <prop:complexity-ext>

#proof[
  Since $Ext^*_(k G) (M, M)$ is finitely generated as a graded module over its
  centre $Z Ext^*_(k G) (M, M)$ (Corollary~@cor:ext-noetherian), we have
  $ gamma(Ext^*_(k G) (M, M)) = gamma(Z Ext^*_(k G) (M, M)). $
  If $S$ is a simple $k G$-module, then $Ext^*_(k G) (M, S)$ is finitely
  generated as a module over $Ext^*_(k G) (M, M)$, and so we have
  $
    max_(S "simple") gamma(Ext^*_(k G) (M, S))
    & lt.eq gamma(Ext^*_(k G) (M, M)) lt.eq gamma(P_*) = c_G (M) \
    & lt.eq max_(S "simple") gamma(Ext^*_(k G) (M, S))
  $
  by our formula for $dim_k P_r$.
]

#lemma[
  Suppose $A$ is a finitely generated commutative graded ring of finite type
  over $k$. Then the nilpotent elements in $A$ form an ideal $J$ with $J^n = 0$
  for some $n$. We have $gamma(A) = gamma(A slash J)$.
] <lem:nilpotent-growth>

#proof[
  Since $A$ is Noetherian, $J$ is finitely generated by nilpotent elements
  $x_i$. If $x_i^(n_i) = 0$ then $J^n = 0$ with $n = sum_i n_i$.

  Now each $J^k slash J^(k+1)$ is a finitely generated module for $A slash J$,
  and so
  $ gamma(A slash J) gt.eq gamma(J^k slash J^(k+1)). $
  Hence $gamma(A slash J) = gamma(A slash J^2) = dots.c = gamma(A)$.
]

#theorem(title: [Alperin, Evens [@bib:Alperin1981]])[
  The complexity $c_G (M)$ is equal to the maximum complexity $c_E (M)$ of the
  restriction of $M$ to an elementary abelian subgroup#idx(
    "elementary",
    "abelian group",
  )#idx(
    "group",
    "elementary abelian",
  ) $E lt.eq G$.
] <th:alperin-evens>
#idx("Alperin", "–Evens theorem", target: [@th:alperin-evens])#idx(
  "theorem",
  "Alperin–Evens",
  target: [@th:alperin-evens],
)

#proof[
  By Proposition~@prop:complexity-ext and Lemma~@lem:nilpotent-growth we have
  $
    c_G (M) = gamma(Ext^*_(k G) (M, M)) = gamma(Z Ext^*_(k G) (M, M))
    = gamma(Z Ext^*_(k G) (M, M) slash J).
  $
  Now by Theorem~@th:nilpotent-restriction the map
  $
    Z Ext^*_(k G) (M, M) slash J -> plus.o.big_(E lt.eq G \ "elemab")
    Z Ext^*_(k E) (M, M) slash J
  $
  is injective, and so
  $
    c_G (M) & lt.eq gamma(
                plus.o.big_(E lt.eq G \ "elemab")
                Z Ext^*_(k E) (M, M) slash J
              ) \
            & = max_(E lt.eq G \ "elemab") gamma(Z Ext^*_(k E) (M, M) slash J)
              = max_(E lt.eq G \ "elemab") c_E (M).
  $
  Conversely, it is clear that $c_E (M) lt.eq c_G (M)$ for any such $E$.
]

#source(173)We now define the *Krull dimension*#idx("Krull dimension")#idx(
  "dimension",
  "Krull",
) of a finitely generated commutative graded ring $A$ of finite type over $k$ to
be its rate of growth $gamma(A)$ as a graded vector space. We shall give other
equivalent (but more general) definitions in Section~@sec:commutative-algebra;
the definition we have given is designed to make the following theorem a direct
corollary of the Alperin–Evens Theorem (of course, it came historically
earlier).

#theorem(title: [Quillen [@bib:Quillen1971b, @bib:Quillen1971c]])[
  The Krull dimension of $H^dot (G, k)$ is equal to the $p$-rank $r_p (G)$#idx(
    "$r_p (G)$",
  ) (i.e., the maximal rank of an elementary abelian $p$-subgroup of $G$).
] <th:quillen-krull-dimension>
#idx(
  "Quillen",
  "'s Krull dimension theorem",
  target: [@th:quillen-krull-dimension],
)#idx("theorem", "Quillen", "'s Krull dimension", target: [
  @th:quillen-krull-dimension
])

#proof[
  The Krull dimension of $H^dot (G, k) = Ext^*_(k G) (k, k)$ is equal to
  $c_G (k)$, by Proposition~@prop:complexity-ext. By the Alperin–Evens Theorem,
  this is equal to the maximal value of $c_E (k)$ as $E$ ranges over the
  elementary abelian $p$-subgroups of $G$. If $E$ is an elementary abelian group
  of order $p^n$, then the Poincaré series of $H^* (E, k)$ is
  $1 slash (1 - t)^n$ (see Section~3.5 of Volume~I) and so
  $c_E (k) = gamma(H^* (E, k)) = n$.
]

#exercise[
  Let $E$ be an elementary abelian $p$-group of order $p^r$, and let $k$ be a
  field of characteristic $p$. Denote by $Lambda$ the algebra
  $k E slash J^2 (k E)$ of dimension $r + 1$. Show that
  $ H^* (Lambda, k) = Ext^*_Lambda (k, k) tilde.equiv k{x_1, dots, x_r}, $
  the free ring on non-commuting generators $x_1, dots, x_r$ of degree one, so
  that
  $ p(H^* (Lambda, k), t) = 1 slash (1 - r t). $
]
