#import "main-defs.typ": *
#import "statements.typ": *

== Example: dihedral 2-groups <sec:dihedral-example>

In this section, we go through the example of the dihedral 2-groups#idx(
  "dihedral 2-groups",
)#idx("group", "dihedral") in detail. Recall that the classification of the
indecomposable modules was described in Section~4.11 of Volume~I. We shall
continue with the notation introduced there, so that
$
  G = D_(4q)#idx("$D_(4q)$") = chevron.l x, y | x^2 = y^2 = 1, (x y)^q
  = (y x)^q chevron.r
$
($q$ a power of two). The $k G$-modules are given by:
+ The modules $M(C)$ of the first kind corresponding to words $C$ which
  alternate in $a^(plus.minus 1)$ and $b^(plus.minus 1)$ and which do not
  contain $(a b)^q$, $(b a)^q$ or their inverses.
+ The modules $M(C, phi.alt)$ of the second kind corresponding to words $C$
  which are not non-trivial powers, and no power of which contains $(a b)^q$,
  $(b a)^q$ or their inverses.
+ The projective indecomposable module $M((a b)^q (b a)^(-q), id_k)$ of the
  second kind.

We shall assume that $k$ is algebraically closed, so that we may apply the
theory of varieties for modules.

We first deal with the case $q = 1$, since this is quite different from $q > 1$,
and a lot easier. In this case, we have $H^* (G, k) = k[x_1, x_2]$ with
$deg(x_1) = deg(x_2) = 1$ so that $V_G = AA^2 (k)$ and $macron(V)_G = PP^1 (k)$.
The indecomposable modules in this case (cf. Section~4.3 of Volume~I) are the
modules $Omega^n (k)$ #source(208)for $n in ZZ$, for which we have
$V_G (Omega^n (k)) = V_G$ by Proposition~@prop:variety-dual-omega, and the
modules $L_(zeta^m)$ for $m >= 1$ and $0 != zeta in H^1 (G, k)$, for which we
have
$V_G (L_(zeta^m)) = V_G chevron.l zeta^m chevron.r
= V_G chevron.l zeta chevron.r$
by Proposition~@prop:l-zeta-variety. Note that
$macron(V)_G chevron.l zeta chevron.r$ is the point in $PP^1 (k)$ parametrising
the module, as in the remark after Theorem~4.3.3 of Volume~I.

In case $q > 1$, we may find $H^* (G, k)$ by repeated application of the
spectral sequence of a central extension, and we find that
$ H^* (G, k) = k[x_1, x_2, z] slash (x_1 x_2) $
with $deg(x_1) = deg(x_2) = 1$ and $deg(z) = 2$. We choose the labelling in such
a way that the generator $x_1$ corresponds to the subgroup
$chevron.l x y x, y chevron.r$ of index two, while $x_2$ corresponds to
$chevron.l x, y x y chevron.r$. Thus
$ macron(V)_G = proj k[x_1, x_2, z] slash (x_1 x_2) = PP^1_a union PP^1_b $
where $PP^1_a$ and $PP^1_b$ are projective lines over $k$ intersecting in the
common point at infinity
$PP^1_a inter PP^1_b = {infinity_a = infinity = infinity_b}$. We choose the
notation so that $PP^1_a = proj k[x_1, z]$ and $PP^1_b = proj k[x_2, z]$, and so
that $lambda x_1^2 + mu x_2^2 + z = 0$ is the equation of the pair of points
${lambda_a, mu_b} subset.eq (PP^1_a union PP^1_b) without {infinity}$.

#theorem[
  The varieties for the $k G$-modules, $G = D_(4q)$, $q >= 1$, are given as
  follows:
  + $macron(V)_G (M(C)) = topcases(
      PP^1_a union PP^1_b
      & "if" C tilde.op a^(plus.minus 1) dots b^(plus.minus 1),
      PP^1_b & "if" C tilde.op a^(plus.minus 1) dots a^(plus.minus 1) "but",
      & quad C tilde.not (a b)^(q-1) a (b^(-1) (a b)^(q-1) a)^r\, r >= 0,
      PP^1_a & "if" C tilde.op b^(plus.minus 1) dots b^(plus.minus 1) "but",
      & quad C tilde.not (b a)^(q-1) b (a^(-1) (b a)^(q-1) b)^r\, r >= 0,
      {0_b} & "if" C tilde.op (a b)^(q-1) a (b^(-1) (a b)^(q-1) a)^r\, r >= 0,
      {0_a} & "if" C tilde.op (b a)^(q-1) b (a^(-1) (b a)^(q-1) b)^r\, r >= 0,
    )$
  + $macron(V)_G (M(C, mat(
          lambda, 1, , 0;
          , dots.down, dots.down, ;
          , , lambda, 1;
          0, , , lambda;
        ))) = topcases(
      {infinity} & "unless" C tilde.op a^(-1) b (a b)^(q-1)\,,
      & b^(-1) a (b a)^(q-1) "or" (a b)^q (b a)^(-q),
      {lambda_a} & "if" C tilde.op a^(-1) b (a b)^(q-1),
      {lambda_b} & "if" C tilde.op b^(-1) a (b a)^(q-1),
    )$
  + $macron(V)_G (M((a b)^q (b a)^(-q), id_k)) = emptyset$.
] <th:dihedral-varieties>

#proof[
  + The first case follows from Corollary~@cor:variety-dimension-prime-to-p. For
    the remaining cases, we need to calculate the dimension of $V_G (M(C))$
    (which is of course one greater than the dimension of $macron(V)_G (M(C))$).
    By Proposition~@prop:variety-dimension-complexity, $dim V_G (M(C)) = 1$ if
    and only if $M(C)$ has complexity one, which by Theorem~@th:eisenbud happens
    if and only if $M(C)$ is periodic. In this case, by
    Corollary~@cor:periodic-variety-line, $macron(V)_G (M(C))$ is a single point
    in $macron(V)_G$, and by Corollary~@cor:period-divides-degree, $M(C)$
    #source(209)has period dividing two. Recall from Section~4.17 of Volume~I
    that $Omega^2 M(C) tilde.equiv M(L_q R_q C)$, and that
    $C tilde.op L_q R_q C$ if and only if
    $C tilde.op (R_q)^r (a b)^(q-1) a = (a b)^(q-1) a (b^(-1) (a b)^(q-1) a)^r$
    or
    $C tilde.op (R_q)^r (b a)^(q-1) b = (b a)^(q-1) b (a^(-1) (b a)^(q-1) b)^r$
    for some $r >= 0$.

    Now if $C tilde.op a^(plus.minus 1) dots a^(plus.minus 1)$ then it follows
    from the explicit description of the actions of $x$ and $y$ that
    $M(C) down_(chevron.l x chevron.r)$ is free, while
    $M(C) down_(chevron.l y chevron.r)$ is not free. Thus $macron(V)_G (M(C))$
    does not contain $0_a$ but does contain $0_b$. By
    Theorem~@th:carlson-connectedness, $macron(V)_G (M(C))$ is connected, so if
    $M(C)$ is periodic then $macron(V)_G (M(C)) = {0_b}$ and if $M(C)$ is not
    periodic then $macron(V)_G (M(C)) = PP^1_b$. Similarly for
    $C tilde.op b^(plus.minus 1) dots b^(plus.minus 1)$, if $M(C)$ is periodic
    then $macron(V)_G (M(C)) = {0_a}$ and if $M(C)$ is not periodic then
    $macron(V)_G (M(C)) = PP^1_a$.
  + According to Section~4.17 of Volume~I, these modules $M(C, phi.alt)$ are all
    periodic, so that by Corollary~@cor:periodic-variety-line,
    $macron(V)_G (M(C, phi.alt))$ is a single point in
    $macron(V)_G$.#ed-note[Here and in part (ii) of the theorem, the band schema
      of Volume I is read with $X$ acting from $V_0$ to $V_1$ by $phi.alt$. With
      the schema as given there, a band beginning with an inverse letter has
      $phi.alt^(-1)$ in that place, and the varieties in the last two cases are
      ${(lambda^(-1))_a}$ and ${(lambda^(-1))_b}$; the set of varieties is the
      same.] If $macron(V)_G (M(C, phi.alt)) != {infinity}$ then either
    $macron(V)_G (M(C, phi.alt)) inter PP^1_a = emptyset$ or
    $macron(V)_G (M(C, phi.alt)) inter PP^1_b = emptyset$.

    If $macron(V)_G (M(C, phi.alt)) inter PP^1_b = emptyset$ then by
    Corollary~@cor:variety-restriction we have
    $macron(V)_H (M(C, phi.alt)) = emptyset$, where $H$ is the subgroup
    $chevron.l x y x, y chevron.r$ of index two in $G$. Thus by
    Proposition~@prop:variety-dimension-complexity, $M(C, phi.alt) down_H$ is
    projective, and so the rank of the matrix $tilde(H) = sum_(h in H) h$ (which
    is a generator for $Soc(k H)$) on $M(C, phi.alt)$ is equal to
    $dim_k M(C, phi.alt) slash |H|$. Setting $X = 1 + x$ and $Y = 1 + y$ in
    $k G$, so that $X^2 = Y^2 = 0$, we have (cf. Lemma~4.11.1 of Volume~I)
    $
      tilde(H) & = ((1 + x y x)(1 + y))^(q slash 2)
                 = ((Y + X Y + Y X + X Y X) Y)^(q slash 2) \
               & = (Y X Y + X Y X Y)^(q slash 2) = (Y X)^(q-1) Y + (X Y)^q.
    $
    Since $M(C, phi.alt)$ is a non-projective indecomposable $k G$-module,
    $ tilde(G) = sum_(g in G) g = (X Y)^q $
    acts as zero on $M(C, phi.alt)$, and so $tilde(H)$ acts in the same way as
    $(Y X)^(q-1) Y$. Looking at the way in which $X$ and $Y$ act on
    $M(C, phi.alt)$ (Section~4.11 of Volume~I), we see that the only way
    $(Y X)^(q-1) Y$ can act with rank equal to $dim_k M(C, phi.alt) slash 2q$ is
    to have $C tilde.op (a^(-1) b (a b)^(q-1))^r$ for some $r >= 1$ (recall that
    $(b a)^q$ must not appear in any power of $C$). Since $C$ is not allowed to
    be a power of a word of smaller length, we have $r = 1$, and
    $C tilde.op a^(-1) b (a b)^(q-1)$. Similarly, if
    $macron(V)_G (M(C, phi.alt)) inter PP^1_a = emptyset$ then
    $C tilde.op b^(-1) a (b a)^(q-1)$.

    To complete the proof, we must determine the varieties
    $
      macron(V)_G (M(a^(-1) b (a b)^(q-1), phi.alt)) quad "and" quad
      macron(V)_G (M(b^(-1) a (b a)^(q-1), phi.alt)).
    $
    Let $zeta = (lambda x_1^2 + mu x_2^2 + z)^r in H^(2r) (G, k)$. We claim that
    $
      L_zeta tilde.equiv M(a^(-1) b (a b)^(q-1), mat(
          lambda, 1, , 0;
          , dots.down, dots.down, ;
          , , lambda, 1;
          0, , , lambda;
        )) plus.o M(b^(-1) a (b a)^(q-1), mat(
          mu, 1, , 0;
          , dots.down, dots.down, ;
          , , mu, 1;
          0, , , mu;
        )),
    $
    where the matrices on the right-hand side are $r times r$ matrices. Given
    this claim, it follows from Proposition~@prop:l-zeta-variety that the
    variety of this direct sum is #source(210)${lambda_a, mu_b}$, so that by
    applying Proposition~@prop:variety-direct-sum and comparing for different
    values of $lambda$ and $mu$, we see that the second and third cases of part
    (ii) are proved.

    To prove the claim, we argue as follows. We have
    $
      Omega^(2r) (k) tilde.equiv
      M((b^(-1) a (b a)^(q-1))^(-r) (a^(-1) b (a b)^(q-1))^r),
    $
    a module of dimension $4q r + 1$. According to the schema described in
    Section~4.11 of Volume~I, we have an ordered basis $z_0, dots, z_(4q r)$ of
    $Omega^(2r) (k)$ corresponding to this word. With respect to this basis, the
    element
    $x_1^(2(r-s)) z^s in H^(2r) (G, k)
    tilde.equiv Hom_(k G) (Omega^(2r) (k), k)$
    corresponds to the homomorphism sending $z_(2q(2r-s))$ to 1 and all other
    $z_i$ to zero, while $x_2^(2(r-s)) z^s in H^(2r) (G, k)$ corresponds to the
    homomorphism sending $z_(2q s)$ to 1 and all other $z_i$ to zero. We shall
    show that#ed-note[The two intersections below are not submodules when
      $lambda$ and $mu$ are non-zero, so the following argument does not prove
      the isomorphisms as stated. The decomposition of $L_zeta$ into the two
      modules on the right is nevertheless correct, as a direct computation
      confirms for $D_8$ and $D_16$, and the varieties in the second part of the
      theorem follow from Proposition~@prop:l-zeta-variety and
      Theorem~@th:carlson-connectedness.]
    $
      #aligned-rows(
        (
          $L_zeta inter chevron.l z_(2q r), dots, z_(4q r) chevron.r$,
          $tilde.equiv M(a^(-1) b (a b)^(q-1), mat(
              lambda, 1, , 0;
              , dots.down, dots.down, ;
              , , lambda, 1;
              0, , , lambda;
            ))$,
        ),
        (
          $L_zeta inter chevron.l z_0, dots, z_(2q r) chevron.r$,
          $tilde.equiv M(b^(-1) a (b a)^(q-1), mat(
              mu, 1, , 0;
              , dots.down, dots.down, ;
              , , mu, 1;
              0, , , mu;
            )).$,
        ),
      )
    $
    We concentrate on the first of these isomorphisms, as the second follows by
    symmetry. Let
    $
      V_0 & = L_zeta inter chevron.l z_(2q r), z_(2q(r+1)), dots, z_(4q r)
            chevron.r \
      V_i & = chevron.l z_(2q r+i), z_(2q(r+1)+i), dots, z_(2q(2r-1)+i)
            chevron.r quad 1 <= i <= 2q - 1.
    $
    and take as basis for $V_0$ the preimages of $z_(2q(r+1)), dots, z_(4q r)$
    under the projection onto these basis vectors of $Omega^(2r) (k)$. In terms
    of these bases, we see that
    $L_zeta inter chevron.l z_(2q r), dots, z_(4q r) chevron.r$ has been given
    as the schema for $M(a^(-1) b (a b)^(q-1), phi.alt)$ as described in
    Section~4.11 of Volume~I, where
    $
      phi.alt = mat(
        r lambda, binom(r, 2) lambda^2, dots.c, , lambda^r;
        1, 0, dots.c, , 0;
        0, 1, dots.c, , 0;
        dots.v, , , , dots.v;
        0, 0, dots.c, 1, 0;
      ).
    $
    Some elementary linear algebra shows that this matrix is conjugate to the
    matrix $mat(
      lambda, 1, , 0;
      , dots.down, dots.down, ;
      , , lambda, 1;
      0, , , lambda;
    )$. Thus we have produced two submodules of $L_zeta$ of the appropriate
    isomorphism types, which intersect in ${0}$ and span $L_zeta$. This
    completes the identification of $L_zeta$.
  + This follows from Proposition~@prop:variety-dimension-complexity, since
    $M((a b)^q (b a)^(-q), id_k)$ is projective.
]
