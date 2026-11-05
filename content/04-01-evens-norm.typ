#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-01-evens-norm.typ": psi-step

== The Evens norm map <sec:evens-norm>

We now define the Evens norm map
$
  norm_(H, G) : Ext^r_(R H) (M_1, M_2)
  -> Ext^(n r)_(R G) (M_1 tensorup^G, M_2 tensorup^G)
$
#idx("$\"norm\"_(H, G)$")\(with a slight twist in case $r$ is odd, to be
explained later), where $H lt.eq G$ and $n = |G : H|$. This bears the same
relation to transfer that tensor induction does to induction.

Recall from Section~3.15 of Volume~I that if $M$ is an $R H$-module then
$M^(times.o n)$ is an $R(Sigma_n wreath H)$-module, which restricts via
$i : G arrow.r.hook Sigma_n wreath H$ to the tensor induced module
$M tensorup^G$. Similarly if $bold(C)$ is a chain complex of $R H$-modules then
$bold(C) times.o_R bold(C)$ is a chain complex of $R(H times H)$-modules, and so
on. Since tensor product is graded commutative, we must be careful about signs
in order to make $bold(C)^(times.o n)$ into a chain complex of
$R(Sigma_n wreath H)$-modules. The action of $Sigma_n wreath H$ on
$bold(C)^(times.o n)$ is given as follows:
$
  (pi; h_1, dots, h_n)(x_1 times.o dots.c times.o x_n)
  = (-1)^nu h_(pi^(-1)(1)) x_(pi^(-1)(1)) times.o dots.c times.o
  h_(pi^(-1)(n)) x_(pi^(-1)(n))
$
where
$ nu = sum_(j < k \ pi(j) > pi(k)) deg(x_j) deg(x_k). $
In other words, we write $pi$ as a product of standard transpositions
$(j, j + 1)$, and for each one we multiply by a sign of
$(-1)^(deg(x_j) deg(x_(j+1)))$.

By restricting to $G$ via $i : G arrow.r.hook Sigma_n wreath H$, we obtain a
chain complex $bold(C) tensorup^G = i^* (bold(C)^(times.o n))$ of $R G$-modules.
If $bold(C)$ is exact and the $C_r$ are projective as $R$-modules then
Proposition~@prop:tensor-homology shows that $bold(C)^(times.o n)$ and
$bold(C) tensorup^G$ are also exact.

Now if $alpha : C_r -> M$ is a map of $R H$-modules, then in order to make
$alpha^(times.o n) : (C_r)^(times.o n) -> M^(times.o n)$ a map of
$R(Sigma_n wreath H)$-modules, we need to be a little careful with the signs. If
$r$ is even, there is no problem, but if $r$ is odd we must make odd
permutations in $Sigma_n$ act with a minus sign. We define $R^((r))$#idx(
  "$R^((r))$",
) to be the $R(Sigma_n wreath H)$-module $R$ on which $H times dots.c times H$
acts trivially, and $Sigma_n$ acts trivially if $r$ is even, and via the sign
representation if $r$ is odd. Thus $alpha^(times.o n)$ is really a map from
$(C_r)^(times.o n)$ to $M^(times.o n) times.o R^((r))$. We define
$1 wreath alpha$ to be the composite map
$
  1 wreath alpha : (bold(C)^(times.o n))_(n r) -> (C_r)^(times.o n)
  -> M^(times.o n) times.o R^((r))
$
#source(134)as a map of $R(Sigma_n wreath H)$-modules, and hence a map of
$R G$-modules
$ 1 wreath alpha : (bold(C) tensorup^G)_(n r) -> M tensorup^G times.o R^((r)). $

We have
$
  delta(1 wreath alpha) = sum_(j=1)^n (-1)^((j-1)r) alpha^(times.o (j-1))
  times.o delta alpha times.o alpha^(times.o (n-j))
$
so that if $delta alpha = 0$ then $delta(1 wreath alpha) = 0$.

If $M_1$ is flat as an $R$-module and $bold(Q)$ is a projective resolution of
$M_1$ over $R H$ then $bold(Q)^(times.o n)$ is an exact sequence of not
necessarily projective modules for $R(Sigma_n wreath H)$, resolving
$M_1^(times.o n)$. If $bold(P)$ is a projective resolution of $M_1^(times.o n)$
(for example we could take $bold(P)$ to be the tensor product of a projective
resolution of $R$ for $R Sigma_n$ with $bold(Q)^(times.o n)$) then by the remark
after Theorem~2.4.2 of Volume~I, there is a map of chain complexes
$phi.alt : bold(P) -> bold(Q)^(times.o n)$ lifting the identity map on
$M_1^(times.o n)$, and any two such maps are chain homotopic. Thus if
$zeta in Ext^r_(R H) (M_1, M_2)$ is represented by a cocycle
$hat(zeta) : Q_r -> M_2$ then $(1 wreath hat(zeta)) compose phi.alt$ is also a
cocycle. We must check that the cohomology class it defines is independent of
the choice of $bold(Q)$ and of the representative cocycle $hat(zeta)$.

#lemma[
  Suppose $bold(C)$ is a chain complex of $R H$-modules, and $f$,
  $g : bold(Q) -> bold(C)$ are homotopic chain maps. Then
  $
    f^(times.o n) compose phi.alt, quad g^(times.o n) compose phi.alt :
    bold(P) -> bold(C)^(times.o n)
  $
  are homotopic chain maps of $R(Sigma_n wreath H)$-modules.
] <lem:tensor-power-homotopy>

#proof[
  Denote by $bold(I)$ the chain complex of $R$-modules with $I_0 = R plus.o R$
  with basis $a$ and $b$, $I_1 = R$ with basis $c$ and $partial c = a - b$, and
  $I_n = 0$ for $n != 0, 1$ (in other words, $bold(I)$ is the cellular chain
  complex of the unit interval). Then a homotopy from $f$ to $g$ is really just
  a map of chain complexes of $R H$-modules
  $bold(h) : bold(I) times.o bold(Q) -> bold(C)$ with
  $bold(h)(a times.o q) = f(q)$ and $bold(h)(b times.o q) = g(q)$ (so that
  $bold(h)(c times.o q) = h(q)$ satisfies
  $f - g = partial compose h + h compose partial$). If we can construct a chain
  map of $R(Sigma_n wreath H)$-modules
  $
    psi : bold(I) times.o bold(P) -> bold(I)^(times.o n) times.o
    bold(Q)^(times.o n)
  $
  with $psi(a times.o p) = a^(times.o n) times.o phi.alt(p)$ and
  $psi(b times.o p) = b^(times.o n) times.o phi.alt(p)$, then the composite
  $
    bold(I) times.o bold(P) limits(->)^psi
    bold(I)^(times.o n) times.o bold(Q)^(times.o n)
    tilde.equiv (bold(I) times.o bold(Q))^(times.o n)
    limits(arrow.r.long)^(bold(h)^(times.o n)) bold(C)^(times.o n)
  $
  will be a homotopy from $f^(times.o n) compose phi.alt$ to
  $g^(times.o n) compose phi.alt$.

  We construct the map $psi$ by induction on degree. Note that $psi$ is already
  defined on $I_0 times.o bold(P)$ by the given conditions. If $psi$ has been
  constructed up to degree $r$, then we construct $psi_(r+1)$ by filling in the
  left-hand end of the following diagram with a vertical arrow, using the fact
  that $bold(P)$ consists of #source(135)projective modules and
  $partial compose psi_r compose partial = 0$.
  $ #psi-step $
  The resulting map $psi$ is clearly a chain map with the desired properties.
]

By taking $bold(C)$ to be the module $M_2$ concentrated in degree $r$, we see
that $(1 wreath hat(zeta)) compose phi.alt$ is independent of the choice of
cocycle $hat(zeta)$ representing $zeta$. By taking $bold(C) = bold(Q)'$ to be
another resolution of $M_1$, we see that the definition is independent of the
choice of resolution. So we obtain a well defined cohomology class
$
  1 wreath zeta in Ext^(n r)_(R(Sigma_n wreath H))
  (M_1^(times.o n), M_2^(times.o n) times.o R^((r))).
$
We define the *Evens norm map*#idx("Evens norm map")#idx("map", "Evens norm")
via
$
  norm_(H, G) (zeta) = i^* (1 wreath zeta)
  in Ext^(n r)_(R G) (M_1 tensorup^G, M_2 tensorup^G times.o R^((r))).
$
Note that if $r$ is odd, the exact sign of this norm depends on the order chosen
for the coset representatives.

If we tensor induce the trivial module $R$ we obtain $R tensorup^G = R$ and so
this also defines a map
$
  norm_(H, G) : H^r (H, M) -> H^(n r) (G, M tensorup^G times.o R^((r))).
$
In particular for $r$ even we have a map
$ norm_(H, G) : H^r (H, R) -> H^(n r) (G, R). $

The following properties of the Evens norm map are direct consequences of the
corresponding properties of tensor induction given in Proposition~3.15.1 of
Volume~I, with suitable attention paid to the signs.

#proposition(closed: true)[
  Suppose $H < G$ with $|G : H| = n$.
  + If $zeta in Ext^r_(R H) (M_1, M_2)$ and $zeta' in Ext^s_(R H) (M_3, M_4)$
    then
    $
      norm_(H, G) (zeta . zeta')
      & = (-1)^(frac(n(n-1), 2) r s) norm_(H, G) (zeta) . norm_(H, G) (zeta') \
      & in Ext^(n(r+s))_(R G) ((M_1 times.o M_3) tensorup^G,
        (M_2 times.o M_4) tensorup^G times.o R^((r+s))).
    $
  + If $H' lt.eq H$ and $zeta in Ext^r_(R H') (M_1, M_2)$ then
    $
      norm_(H, G) norm_(H', H) (zeta)
      = norm_(H', G) (zeta)
    $
    (where the coset representatives of $H'$ in $G$ have been chosen in the
    order coming from the choices of coset representatives of $H'$ in $H$ and
    $H$ in $G$).
  + If $zeta$, $zeta' in Ext^r_(R H) (M_1, M_2)$ then
    $
      norm_(H, G) (zeta + zeta') = norm_(H, G) (zeta)
      + norm_(H, G) (zeta')
    $
    $+$ a sum of transfers from proper subgroups $K$ containing the intersection
    of the conjugates of $H$.
  + #source(136)If $H' lt.eq H$ and $zeta in Ext^r_(R H') (M_1, M_2)$ then
    $norm_(H, G) tr_(H', H) (zeta)$ is a sum of transfers from subgroups $K$
    containing the intersection of the conjugates of $H'$, and with
    $K inter H lt.eq H'$.
  + (Mackey formula#idx("Mackey formula for norm")) If $K$, $H lt.eq G$ and
    $zeta in Ext^r_(R K) (M_1, M_2)$ then
    $
      res_(G, H) norm_(K, G) (zeta) = product_(H backslash G slash K)
      norm_(H inter lconj(g, K), H)
      res_(lconj(g, K), H inter lconj(g, K)) (g zeta).
    $
  + If $N$ is a normal subgroup of $G$ contained in $H$, and $M_1$ and $M_2$ are
    $R H$-modules on which $N$ acts trivially, then for
    $zeta in Ext^r_(R(H slash N)) (M_1, M_2)$ we have
    $
      inf_(G slash N, G) norm_(H slash N, G slash N) (zeta)
      = norm_(H, G) inf_(H slash N, H) (zeta).
    $
] <prop:norm-properties>

#remark[
  Graeme Segal [@bib:Segal1975] has constructed a generalised cohomology theory
  whose degree zero part (additively) is the multiplicative group of formal
  series ${a_(2i)}$, $a_(2i) in H^(2i) (X; R)$ and $a_0$ invertible. The
  transfer map (see Section~@sec:transfer) in this theory gives the Evens norm
  map
  $ norm_(H, G) : H^r (B H; R) -> H^(n r) (B G; R) $
  for $r$ even. Fulton and MacPherson [@bib:Fulton1987] give a direct
  description of the norm map for finite coverings of topological spaces, and
  describe the Chern classes of an induced representation (or more generally a
  direct image bundle) in terms of this construction.
]

#theorem[
  If $p$ divides $|G|$ and $p$ is not invertible in $R$ then for some $r > 0$,
  $H^r (G, R) != 0$. Moreover, if $g != 1$ is an element of order $p$ in $G$,
  such an element can be chosen to restrict to a non-zero element of
  $H^r (chevron.l g chevron.r, R)$.
] <th:cohomology-nonvanishing>

#proof[
  Let $g != 1$ be an element of $G$ of order $p$, and let
  $H = N_G chevron.l g chevron.r$. By Corollary~3.5.4 of Volume~I, there is a
  non-nilpotent element $sigma in H^2 (chevron.l g chevron.r, R)$. For $x in H$,
  conjugation by $x$ sends $sigma$ to $lambda sigma$ for some $lambda$ with
  $lambda^(p-1) = 1$ (since the action of conjugation by $x$ on
  $chevron.l g chevron.r$ has order dividing $p - 1$). Thus, letting
  $alpha = sigma^(p-1)$, $alpha$ is an $H$-invariant non-nilpotent element of
  $H^(2(p-1)) (chevron.l g chevron.r, R)$. Let
  $|N_G (chevron.l g chevron.r) : chevron.l g chevron.r| = p^a h$ with $p$ not
  dividing $h$, and set
  $ z = norm_(chevron.l g chevron.r, G) (1 + alpha). $
  Then the Mackey formula~@prop:norm-properties[(v)] shows that
  $
    res_(G, chevron.l g chevron.r) (z) = (1 + alpha)^(p^a h)
    & = (1 + alpha^(p^a))^h \
    & = 1 + h alpha^(p^a) + "terms of higher degree".
  $
  Thus $z$ has a non-zero homogeneous part in degree $2(p - 1)p^a$.
]

#example[
  Let $G = ZZ slash p times ZZ slash p$ with $p$ odd, and
  $H = 1 times ZZ slash p subset.eq G$. Then by Section~3.5 of Volume~I,
  $H^* (G, FF_p)$ has generators $y_1$ and $y_2$ in degree one with
  $y_1^2 = y_2^2 = 0$, and generators $x_1$ and $x_2$ in degree two.
  $H^* (H, FF_p)$ is generated by $y_2$ and $x_2$, which are the restrictions of
  the elements of the #source(137)same name in $H^* (G, FF_p)$, while $y_1$ and
  $x_1$ restrict to zero. We shall calculate $norm_(H, G) (y_2)$ and
  $norm_(H, G) (x_2)$. We first deal with the latter.

  Since
  $ res_(G, H) norm_(H, G) (x_2) = x_2^p $
  and $norm_(H, G) (x_2)$ is invariant under automorphisms of the first copy of
  $ZZ slash p$, we have
  $
    norm_(H, G) (x_2) = x_2^p + lambda x_1^(p-1) x_2
    + mu x_1^(p-2) y_1 x_2 y_2
  $
  for some values of the scalars $lambda$ and $mu$. The norm of $x_2$ is also
  invariant under the automorphism of $ZZ slash p times ZZ slash p$ which fixes
  the second generator and sends the first to its product with the second. This
  automorphism sends $y_2$ to $y_1 + y_2$, $x_2$ to $x_1 + x_2$, and fixes $y_1$
  and $x_1$. Thus we have
  $
    norm_(H, G) (x_2) = (x_1 + x_2)^p + lambda x_1^(p-1) (x_1 + x_2)
    + mu x_1^(p-2) y_1 (x_1 + x_2)(y_1 + y_2).
  $
  Equating this with the previous expression we find that $lambda = -1$ and
  $mu = 0$, so that
  $ norm_(H, G) (x_2) = x_2^p - x_1^(p-1) x_2. $
  Thus by multiplicativity of the norm we have
  $ norm_(H, G) (x_2^r) = (x_2^p - x_1^(p-1) x_2)^r. $

  Applying the same reasoning to $y_2$, we see that $norm_(H, G) (y_2)$ is of
  the form
  $ lambda x_1^((p-1) slash 2) y_2 + mu x_1^((p-3) slash 2) y_1 x_2. $
  Note that since $y_2$ has odd degree, the action of the automorphisms of
  $ZZ slash p$ on cohomology has to be tensored with the sign representation.
  The invariants of this action are discussed in Section~3.6 of Volume~I.

  Again applying the automorphism fixing the first generator and sending the
  second to its product with the first, we see that $lambda = -mu$. However,
  this reasoning does not allow us to evaluate $lambda$ explicitly. Of course,
  the sign of $lambda$ depends on which ordering is chosen for the cosets of $H$
  in $G$, as is always true in odd degree. We shall see in
  Section~@sec:steenrod-proof that for a suitable choice of this order we have
  $lambda = 1 slash (frac(p - 1, 2))!$, so that
  $
    norm_(H, G) (y_2) = x_1^((p-3) slash 2) (x_1 y_2 - y_1 x_2) slash
    (inline(frac(p - 1, 2)))!
  $
]

We summarise the results of this calculation for future reference. The
corresponding result for $p = 2$ is easy to check by the same method.

#proposition(closed: true)[
  Let $G = ZZ slash p times ZZ slash p$ with $p$ odd, and
  $H = 1 times ZZ slash p lt.eq G$. Then using the above notation for elements
  of $H^* (H, FF_p)$ and $H^* (G, FF_p)$ we have
  + $norm_(H, G) (x_2) = x_2^p - x_1^(p-1) x_2$
  + $norm_(H, G) (y_2)
    = lambda x_1^((p-3) slash 2) (x_1 y_2 - y_1 x_2)$,
  where $lambda$ is a multiplicative constant which will be seen in
  Section~@sec:steenrod-proof to be $1 slash (frac(p - 1, 2))!$.

  #source(138)If $G = ZZ slash 2 times ZZ slash 2$ and
  $H = 1 times ZZ slash 2 lt.eq G$ then $H^* (G, FF_2)$ is generated by elements
  $y_1$ and $y_2$ of degree one. If $H$ is the subgroup corresponding to the
  element $y_1$, then writing $y_2$ for the restriction of $y_2$ to $H$ we have
  $ norm_(H, G) (y_2) = y_2^2 + y_1 y_2. $
] <prop:norm-rank-two>

#exercise[
  (Nakaoka's Theorem#idx("Nakaoka's theorem")#idx("theorem", "Nakaoka's")
  [@bib:Nakaoka1961], see also Quillen [@bib:Quillen1971e] §3) Suppose that
  $R = k$ is a field, and $G subset.eq Sigma_n$ and $H$ are finite groups with
  wreath product $G wreath H$. If $bold(P)$ is a minimal resolution of $k$ as a
  $k G$-module and $bold(Q)$ is a minimal resolution of $k$ as a $k H$-module,
  show that $bold(Q)^(times.o n)$ is a minimal projective resolution of $k$ as a
  $k(H^n)$-module. Show that if we use $bold(P) times.o bold(Q)^(times.o n)$ as
  a resolution for $G wreath H$, then the differential on
  $
    Hom_(k(G wreath H)) (bold(P) times.o bold(Q)^(times.o n), k)
    tilde.equiv Hom_(k G) (bold(P), Hom_(k H) (bold(Q), k)^(times.o n))
  $
  comes entirely from the differential on $bold(P)$. Deduce that the cohomology
  of $G wreath H$ is given by
  $ H^* (G wreath H, k) = H^* (G, H^* (H^n, k)). $
  In other words, in the Lyndon–Hochschild–Serre spectral sequence for the
  normal subgroup $H^n$, converging to $H^* (G wreath H, k)$, all the
  differentials from the $E_2$ page onwards are zero, and the filtered graded
  ring $H^* (G wreath H, k)$ is isomorphic to its associated double graded ring
  $E_infinity^(**)$. Use this to give another proof of
  Lemma~@lem:tensor-power-homotopy in case $R = k$.
]
