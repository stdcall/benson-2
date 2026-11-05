#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-02-eilenberg-mac-lane.typ": (
  covering-groups, skeleton-sequence,
)

== Eilenberg–Mac~Lane spaces <sec:eilenberg-mac-lane>

#definition[
  A space $(X, x_0)$ is of *type* $(pi, n)$ if $pi_n (X, x_0) tilde.equiv pi$,
  and $pi_i (X, x_0) = 0$ for $i != n$. If $X$ has the homotopy type of a
  CW-complex then it is an *Eilenberg–Mac~Lane space*#idx(
    "Eilenberg",
    "–Mac Lane",
    "space",
  )#idx(
    "space",
    "Eilenberg–Mac Lane",
  ) $K(pi, n)$#idx("$K(pi, n)$").
] <def:eilenberg-mac-lane-space>

#remark[
  By Theorem~@th:whitehead-cw, a CW-complex $X$ is a $K(pi, 1)$ if and only if
  $pi_1 (X, x_0) tilde.equiv pi$ and the universal cover of $X$ is contractible.
]

#example(kind: "Examples")[
  Take $X = RR P^infinity$, the union of the real projective spaces
  $RR P^n subset.eq RR P^(n+1) subset.eq dots.c$ with the weak topology. The
  sphere is a 2-fold cover of $RR P^n$, and so $S^infinity$ is a 2-fold cover of
  $RR P^infinity$. We claim that $pi_i (S^infinity) = 0$ for all $i$, so that
  $S^infinity$ is contractible. This is because any map from an $i$-sphere to
  $S^infinity$ has image lying in some finite sphere $S^n$, by compactness.
  Taking $n$ greater than $i$, we see that the map is homotopic to zero already
  in $S^n$. It follows that $RR P^infinity$ is a $K(ZZ slash 2, 1)$.

  In a similar way, we see from the long exact homotopy sequence of the
  fibration $S^1 -> S^(2n+1) -> CC P^n$ that
  $pi_2 (CC P^n, x_0) tilde.equiv ZZ$, and $pi_i (CC P^n, x_0) = 0$ for $i = 1$
  and $2 < i < n$. Thus $pi_2 (CC P^infinity, x_0) tilde.equiv ZZ$ and
  $pi_i (CC P^infinity, x_0) = 0$ for $i != 2$, so that $CC P^infinity$ is a
  $K(ZZ, 2)$.

  Another easy example is that $S^1$ is a $K(ZZ, 1)$.
]

#theorem[
  Given $n gt.eq 1$ and $pi$ a group, with $pi$ abelian if $n gt.eq 2$, then
  there exists an Eilenberg–Mac~Lane space $K(pi, n)$.
] <th:eilenberg-mac-lane-existence>

#proof[
  We start with the case $n = 1$. Choose a free presentation
  $ 1 -> R -> F -> pi -> 1 $
  with $F$ free and $R$ a normal subgroup of $F$. We construct a CW-complex $X$
  as follows. We take as the 1-skeleton $X^1$ of $X$ a wedge sum of copies of
  the circle $S^1_alpha$, indexed over generators $alpha$ of $F$ as a free
  group. Thus we have $pi_1 (X^1, x_0) tilde.equiv F$. Now choose elements
  $beta in R$ generating $R$ as a normal subgroup of $F$. Each element $beta$
  corresponds to an element of $pi_1 (X^1, x_0)$ and is hence represented by a
  map
  $ hat(beta) : (S^1, s_0) -> (X^1, x_0). $
  We take for the 2 skeleton of $X$
  $ X^2 = X^1 union_(hat(beta)) union.big (sigma^2_beta), $
  the space formed by attaching 2-cells to $X^1$, using the $hat(beta)$ as
  attaching maps.

  #source(45)We have $pi_1 (X^2, X^1, x_0) = 0$, and so the homotopy exact
  sequence is
  $ #skeleton-sequence $
  For each generator $beta$ of $R$ there is an obvious corresponding element in
  the group $pi_2 (X^2, X^1, x_0)$, which goes to $beta in pi_1 (X^1, x_0)$.
  Thus the kernel of $pi_1 (X^1, x_0) -> pi_1 (X^2, x_0)$ contains $R$. To show
  that it is exactly $R$, we notice that the covering $tilde(X)^1$ of $X^1$
  corresponding to the subgroup $R$ of $F$ (as in Section~@sec:fibrations) has
  $pi_1 (tilde(X)^1, x_0) tilde.equiv R$, and the fibre of $tilde(X)^1 -> X^1$
  is $F slash R$. Thus for each 2-cell $sigma^2_beta$ of $X^2$ and each element
  of $F slash R$ we attach a 2-cell to $tilde(X)^1$ in the obvious way, we
  obtain a space $tilde(X)^2$ covering $X^2$, with fibre $F slash R$. The
  commutative diagram
  $ #covering-groups $
  now shows that $pi_1 (X^2, x_0) = F slash R$ and $pi_1 (tilde(X)^2, x_0) = 0$.

  We now kill the higher homotopy groups by induction. Suppose we have
  constructed the $m$-skeleton $X^m$ with
  $ pi_r (X^m, x_0) = cases(pi & quad r = 1, 0 & quad 1 < r < m.) $
  We choose generators $gamma$ for $pi_m (X^m, x_0)$ and representatives
  $ hat(gamma) : (S^m, s_0) -> (X^m, x_0) $
  and form
  $ X^(m+1) = X^m union_(hat(gamma)) union.big sigma^(m+1)_gamma $
  by using the $hat(gamma)$ as attaching maps. We have
  $ pi_(m+1) (X^(m+1), X^m, x_0) tilde.equiv plus.o.big_gamma ZZ_gamma, $
  a free abelian group on generators corresponding to the elements $gamma$. The
  boundary map
  $
    pi_(m+1) (X^(m+1), X^m, x_0) limits(->)^partial pi_m (X^m, x_0)
  $
  sends the generator of $ZZ_gamma$ to $gamma$ and is hence surjective, so that
  $pi_m (X^(m+1), x_0) = 0$. The lower homotopy groups are unaltered, and so we
  have constructed #source(46)$X^(m+1)$. We now set
  $X = union.big_(m gt.eq 1) X^m$ with the weak topology, so that $X$ is a
  $K(pi, 1)$.

  The construction of a $K(pi, n)$ for $n gt.eq 2$ is the same only easier.
  Begin with a presentation
  $ 1 -> R -> F -> pi -> 1 $
  of $pi$ as an abelian group, so that $F$ is free abelian and $R lt.eq F$.
  Choose generators $alpha$ for $F$ as a free abelian group and take as the
  $n$-skeleton $X^n$ a wedge sum of copies of a sphere $S^n_alpha$ indexed over
  the generators $alpha$. Then $pi_i (X^n, x_0) = 0$ for $i < n$ and
  $pi_n (X^n) tilde.equiv F$. Choose generators $beta$ for $R$ and attach
  $(n + 1)$-cells corresponding to the generators $beta$. Kill higher homotopy
  exactly as before.
]

#remark[
  If $pi$ is abelian then the set of homotopy classes of maps from $X$ to
  $K(pi, n)$ is in natural bijection with $H^n (X; pi)$ via the map
  $
    [X; K(pi, n)] -> H^n (X; pi) \
    f |-> f^* (i_n)
  $
  where
  $i_n in H^n (K(pi, n); pi) tilde.equiv Hom(H_n (K(pi, n)), pi)$
  corresponds to the inverse of the Hurewicz homomorphism
  $ pi = pi_n (K(pi, n), x_0) -> H_n (K(pi, n)). $

  If $n = 1$ and $pi$ is not necessarily abelian, then $[X; K(pi, 1)]$ is in
  natural bijection with $Hom(pi_1 (X, x_0), pi)$ via the map $f -> f_*$. These
  statements are proved by obstruction theory, and may be found for example in
  Mosher and Tangora [@bib:Mosher1968].

  In either case it follows that $K(pi, n)$ is unique up to homotopy, since if
  $X$ and $Y$ are both $K(pi, n)$’s, then there are maps $X -> Y$ and $Y -> X$
  corresponding to the isomorphism $pi_n (X) tilde.equiv pi_n (Y)$. The
  composite in either direction induces the identity map on $pi_n$ and is hence
  homotopic to it by again applying the bijection. It also follows that
  $[K(pi, n); K(pi', n)] tilde.equiv Hom(pi, pi')$.

  The above statements may be phrased by saying that $H^n (-; pi)$ is a
  _representable functor_#idx("representable functor")#idx(
    "functor",
    "representable",
  ) (see Section~2.1 of Volume~I) represented by $K(pi, n)$. Thus for example
  Yoneda’s lemma shows that the natural transformations
  $ H^n (-; pi) arrow.r.squiggly H^m (-; pi') $
  are in one–one correspondence with homotopy classes of maps
  $ [K(pi, n); K(pi', m)] $
  or equivalently with elements of
  $ H^m (K(pi, n); pi'). $

  In particular the Hurewicz theorem shows that there can be no non-zero natural
  transformations if $m < n$, and if $m = n$ the natural transformations are in
  one–one correspondence with $Hom(pi, pi')$. For $m > n$ the natural
  transformations can be quite interesting. For example if $pi = ZZ slash p$
  then there are #source(47)the Steenrod operations, which we shall discuss from
  a much more algebraic point of view in Chapter~@ch:evens-steenrod.
]

#theorem[
  + $H_n (G, R) tilde.equiv H_n (K(G, 1); R)$
  + $H^n (G, R) tilde.equiv H^n (K(G, 1); R)$.
] <th:cohomology-of-k-g-1>

#proof[
  Let $X$ be a $K(G, 1)$ which is a CW-complex, and let $tilde(X)$ be its
  universal cover, so that $tilde(X)$ is contractible (see the remark after the
  definition). $G$ acts freely on $tilde(X)$ permuting the cells. So the
  cellular chains $C_* (tilde(X); R)$ on $tilde(X)$ form an exact sequence of
  free $R G$-modules, and the quotient by the $G$-action is $C_* (X; R)$.
  Together with the augmentation $C_0 (tilde(X); R) -> R -> 0$ we obtain a free
  resolution of $R$ as an $R G$-module.

  We have
  $ C_i (tilde(X); R) times.o_(R G) R tilde.equiv C_i (X; R) $
  and so using this resolution to calculate Tor, we have
  $ H_i (G, R) = Tor^(R G)_i (R, R) tilde.equiv H_i (X; R). $
  Similarly
  $
    Hom_(R G) (C_i (tilde(X); R), R) tilde.equiv Hom_R (C_i (X; R), R)
    = C^i (X; R)
  $
  and so
  $ H^i (G, R) = Ext^i_(R G) (R, R) tilde.equiv H^i (X; R). $
]

#exercise[
  If $X$ is a $K(pi, n)$, show that the loop space $Omega X$ is a
  $K(pi, n - 1)$.
]
