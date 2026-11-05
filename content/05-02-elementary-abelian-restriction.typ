#import "main-defs.typ": *
#import "statements.typ": *

== Restriction to elementary abelian subgroups
<sec:elementary-abelian-restriction>

#source(167)In this section, we show that an element of $Ext^*_(k G) (M, M)$ is
nilpotent if and only if its restriction to every elementary abelian
subgroup#idx("elementary", "abelian group")#idx("group", "elementary abelian")
is nilpotent.

In the case where $M$ is the trivial module, this theorem is due to Quillen
[@bib:Quillen1971b, @bib:Quillen1971c], see also Quillen and Venkov
[@bib:Quillen1972b]. In the general case it is due to Carlson
[@bib:Carlson1981b]. The proof uses Serre's Theorem~@th:serre-bocksteins
together with the following theorem. This theorem is due to Quillen and Venkov
[@bib:Quillen1972b] in case $M$ is the trivial module and Alperin and Evens
[@bib:Alperin1981] in the general case. The proof we give is due to Kroll
[@bib:Kroll1984].

#theorem(title: [Quillen, Venkov, $dots$])[
  Suppose $k$ is a field of characteristic $p$, $M$ is a $k G$-module and $H$ is
  a normal subgroup of index $p$ in $G$. If $zeta$ is an element of positive
  degree in $Ext^*_(k G) (M, M)$ with $res_(G, H) (zeta) = 0$, then
  $ zeta^2 = beta(x) . zeta' $
  for some $zeta' in Ext^*_(k G) (M, M)$, where $x$ is the inflation to $G$ of a
  non-zero element $macron(x) in H^1 (G slash H, FF_p)$.
] <th:quillen-venkov>
#idx("Quillen", "–Venkov theorem", target: [@th:quillen-venkov])#idx(
  "theorem",
  "Quillen",
  "–Venkov",
  target: [@th:quillen-venkov],
)

#proof[
  We have short exact sequences
  $
    0 -> M limits(->)^eta M down_H up^G -> M' -> 0 \
    0 -> M' -> M down_H up^G limits(->)^(eta') M -> 0
  $
  where $eta$ and $eta'$ are the natural maps described in Section~2.8 of
  Volume~I, and $M' tilde.equiv coker(eta) tilde.equiv Ker(eta')$ is the tensor
  product of $M$ with $Omega_(G slash H) (k)$ regarded as a $k G$-module of
  dimension $p - 1$ with $H$ in the kernel. Denote by
  $rho in Ext^1_(k G) (M', M)$ and $rho' in Ext^1_(k G) (M, M')$ the elements
  corresponding to these sequences.

  Recall from Section~2.8 of Volume~I that the composite
  $
    Ext^n_(k G) (M, M) limits(arrow.r.long)^(eta_*)
    Ext^n_(k G) (M, M down_H up^G) limits(->)^tilde.equiv
    Ext^n_(k H) (M down_H, M down_H)
  $
  of $eta_*$ with the Eckmann–Shapiro isomorphism is equal to $res_(G, H)$, as
  also is the composite
  $
    Ext^n_(k G) (M, M) limits(arrow.r.long)^((eta')^*)
    Ext^n_(k G) (M down_H up^G, M) limits(->)^tilde.equiv
    Ext^n_(k H) (M down_H, M down_H).
  $
  So the condition $res_(G, H) (zeta) = 0$ implies that $eta_* (zeta) = 0$ and
  $(eta')^* (zeta) = 0$.

  The above short exact sequences give rise to long exact sequences
  $
    dots.c -> Ext^(n-1)_(k G) (M, M') -> Ext^n_(k G) (M, M)
    limits(arrow.r.long)^(eta_*) Ext^n_(k G) (M, M down_H up^G) -> dots.c \
    dots.c -> Ext^(n-1)_(k G) (M', M) -> Ext^n_(k G) (M, M)
    limits(arrow.r.long)^((eta')^*) Ext^n_(k G) (M down_H up^G, M) -> dots.c
  $
  whose connecting homomorphisms are given by Yoneda composition with $rho$,
  resp. $rho'$. So the conditions $eta_* (zeta) = 0$ and $(eta')^* (zeta) = 0$
  imply that there are elements $zeta_0 in Ext^(n-1)_(k G) (M, M')$ and
  $zeta'_0 in Ext^(n-1)_(k G) (M', M)$ such that
  $zeta = rho compose zeta_0 = zeta'_0 compose rho'$. Now by the discussion
  following Lemma~@lem:bockstein-squared-zero, the element #source(
    168,
  )$rho' compose rho in Ext^2_(k G) (M', M')$ is equal to the element
  $beta(x)_(M')$ obtained by tensoring $M'$ with the exact sequence representing
  $beta(x)$. Since Yoneda product with $beta(x)_(M')$ equals cup product with
  $beta(x)$, and hence commutes with other Yoneda compositions (see Section~3.2
  of Volume~I) we have
  $
    zeta^2 = zeta compose zeta = zeta'_0 compose rho' compose rho compose zeta_0
    = zeta'_0 compose beta(x)_(M') compose zeta_0
    = beta(x) . (zeta'_0 compose zeta_0).
  $
]

#theorem(title: [Quillen, Carlson])[
  Suppose $k$ is a field of characteristic $p$, and $M$ is a $k G$-module. Then
  an element $zeta in Ext^*_(k G) (M, M)$ of positive degree is nilpotent (under
  Yoneda product) if and only if $res_(G, E) (zeta)$ is nilpotent for all
  elementary abelian subgroups $E$ of $G$.
] <th:nilpotent-restriction>

#proof[
  Since restriction from $G$ to a Sylow $p$-subgroup is injective on
  $Ext^*_(k G) (M, M)$ (Corollary~3.6.18 of Volume~I), without loss of
  generality $G$ is a $p$-group. We may suppose that $G$ is not elementary
  abelian, so that by Serre's Theorem~@th:serre-bocksteins we may choose
  elements $x_1, dots, x_n in H^1 (G, FF_p)$ with
  $ beta(x_1) . dots . beta(x_n) = 0. $
  Working by induction, we may assume that for each maximal subgroup $H$ of $G$,
  $res_(G, H) (zeta)$ is nilpotent. Denoting by $H_i$ the maximal subgroup
  corresponding to $x_i$, we suppose that $res_(G, H_i) (zeta^(r_i)) = 0$. Thus
  by the Quillen–Venkov Theorem~@th:quillen-venkov, we have
  $ zeta^(2r_i) = beta(x_i) . zeta'_i. $
  So letting $r = 2 sum_i r_i$, we have
  $
    zeta^r & = zeta^(2r_1) compose dots.c compose zeta^(2r_n)
             = (beta(x_1) . zeta'_1) compose dots.c compose
             (beta(x_n) . zeta'_n) \
           & = beta(x_1) . dots . beta(x_n) .
             (zeta'_1 compose dots.c compose zeta'_n) = 0.
  $
  We have used here the fact that cup product with $beta(x_i)$ commutes with
  Yoneda products (Corollary~3.2.2 of Volume~I).
]

Using the finite generation of cohomology, we may now deduce Chouinard's
Theorem.

#lemma[
  Suppose $k$ is a field of characteristic $p$ and $M$ is a finitely generated
  $k G$-module. Then the following are equivalent:
  + $M$ is projective.
  + $Ext^n_(k G) (M, M) = 0$ for all $n > 0$.
  + $Ext^n_(k G) (M, M) = 0$ for all $n$ large enough.
  + Every element of $Ext^*_(k G) (M, M)$ of positive degree is nilpotent.
] <lem:projective-nilpotent>

#proof[
  Since $Ext^*_(k G) (M, M)$ is finitely generated as a module over its centre
  (Corollary~@cor:ext-noetherian), (iii) is equivalent to (iv). It is clear that
  (i) $=>$ (ii) $=>$ (iii), so we shall prove that (iii) $=>$ (i).

  Now by Corollary~@cor:ext-noetherian, if $N$ is another finitely generated
  $k G$-module, then $Ext^*_(k G) (M, N)$ is finitely generated as a module over
  $Ext^*_(k G) (M, M)$. So if we have $Ext^n_(k G) (M, M) = 0$ for all $n$ large
  enough, then the same is true of $Ext^n_(k G) (M, N)$ for any finitely
  generated module $N$. In particular, taking $N$ to be a simple module $S$,
  this shows that the projective cover of $S$ appears #source(169)only finitely
  often in the minimal projective resolution of $M$. Since there are only
  finitely many simple modules, this means that the minimal projective
  resolution of $M$ stops. By Corollary~3.6.5 of Volume~I, this forces $M$ to be
  projective.
]

#theorem(title: [Chouinard])[
  A finitely generated $k G$-module $M$ is projective if and only if $M down_E$
  is projective for every elementary abelian subgroup $E$ of $G$.
] <th:chouinard>
#idx("Chouinard's theorem", target: [@th:chouinard])#idx(
  "theorem",
  "Chouinard's",
  target: [@th:chouinard],
)

#proof[
  If $M$ is projective, it is clear that $M down_E$ is projective. Conversely,
  if $M down_E$ is projective for every elementary abelian subgroup $E$ of $G$,
  then $Ext^n_(k E) (M, M) = 0$ for every $E$ and $n > 0$. Thus by
  Theorem~@th:nilpotent-restriction, every element of $Ext^*_(k G) (M, M)$ of
  positive degree is nilpotent, and so by the lemma $M$ is projective.
]
