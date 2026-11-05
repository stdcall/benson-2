#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-05-steenrod-proof.typ": norm-factorisation, norm-naturality

== Proof of the properties <sec:steenrod-proof>

In this section we shall prove most of Theorems~@th:steenrod-squares
and~@th:steenrod-powers in parallel. The main differences between the two cases
come from the difference in the multiplicative structure of cohomology of cyclic
groups (Proposition~3.5.5 of #source(151)Volume~I) and symmetric groups of
degree $p$ (example at end of Section~3.7 of Volume~I).

Our approach is essentially the same as in Steenrod and Epstein
[@bib:Steenrod1962], with minor modifications. For the benefit of the reader who
wishes to compare, we shall indicate the parallel results in
[@bib:Steenrod1962].

Property (i) of the Steenrod operations follows from the remark following the
definition of the maps $D_j$, together with the following lemma.

#lemma(title: [cf. [@bib:Steenrod1962] VII.3.3])[
  The maps $D_j$, and hence also $Sq^i$ and $P^i$, are natural transformations
  of functors on the category of groups.
] <lem:steenrod-naturality>

#proof[
  If $phi.alt : G -> G'$ is a group homomorphism, then the following diagram
  commutes.
  $ #norm-naturality $
  The composite of each of the horizontal rows is the norm map.
]

Property (iv) of the Steenrod operations follows from the fact that $D_j = 0$
for $j < 0$, while property (iii) follows from the next lemma.

#lemma(title: [cf. [@bib:Steenrod1962] VII.3.4])[
  $D_0 (x) = x^p$.
] <lem:d-zero-power>

#proof[
  We have
  $
    D_0 (x) = res_(ZZ slash p times G, G) norm_(G, ZZ slash p times G)
    (x) = x^p
  $
  by the Mackey Formula~@prop:norm-properties[(v)].
]

For $p$ odd, we appear not to have used all the $D_j$ in our definition of the
Steenrod operations. However, the following two lemmas show that the only
non-zero maps $D_j$ are multiples of the $P^i$ or $beta P^i$ for some $i$.

#lemma(title: [cf. [@bib:Steenrod1962] VII.3.5])[
  For $p$ odd and $x in H^r (G, FF_p)$,
  + if $r$ is even then $D_j (x) = 0$ unless $j = 2k(p - 1)$ or
    $j = 2k(p - 1) - 1$ for some $k$; and
  + if $r$ is odd then $D_j (x) = 0$ unless $j = (2k + 1)(p - 1)$ or
    $j = (2k + 1)(p - 1) - 1$ for some $k$.
] <lem:vanishing-d-j>

#proof[
  The map
  $
    norm_(G, ZZ slash p times G) : H^r (G, FF_p)
    -> H^(p r) (ZZ slash p times G, FF_p)
  $
  #source(152)may be factored as follows
  $ #norm-factorisation $
  Now by the example at the end of Section~3.6 of Volume~I, the map
  $
    res_(Sigma_p, ZZ slash p) : H^j (Sigma_p, FF_p^((r)))
    -> H^j (ZZ slash p, FF_p)
  $
  is injective, and its image has a basis consisting of the $a_j$ where
  + $j = 2k(p - 1)$ or $2k(p - 1) - 1$ for some $k$ if $r$ is even, and
  + $j = (2k + 1)(p - 1)$ or $(2k + 1)(p - 1) - 1$ for some $k$ if $r$ is odd.
  Thus $D_j (x) = 0$ unless $j$ has one of these values.
]

The following lemma shows that for $p = 2$, $Sq^(2i+1) = beta Sq^(2i)$, so that
in particular property (vi) follows from property (ii).

#lemma(title: [cf. [@bib:Steenrod1962] VII.4.6 and errata])[
  We have $beta compose D_0 = 0$, $beta compose D_(2j) = D_(2j-1)$, and
  $beta compose D_(2j-1) = 0$ on $H^r (G, FF_p)$ if $p$ is odd or $r$ is even,
  while $beta compose D_(2j+1) = D_(2j)$ and $beta compose D_(2j) = 0$ on
  $H^r (G, FF_2)$ if $r$ is odd.#ed-note[The book states the first set of
    relations for all $p$ and $r$. For $p = 2$ and $r$ odd they fail: for
    $y in H^1 (ZZ slash 2, FF_2)$, $D_1 (y) = y$ while
    $beta D_1 (y) = y^2 != 0$.]
] <lem:bockstein-d-j>

#proof[
  We apply Lemma~@lem:twisted-bockstein-norm, and notice that
  + when $p = 2$ and $r$ is even, $tilde(beta)$ and $beta$ agree on
    $H^* (ZZ slash 2 times G, FF_2)$, while for $r$ odd the generator of
    $ZZ slash 2$ acts as $-1$ on $(ZZ slash 4)^((r))$ and
    $tilde(beta)(z) = beta(z) + a_1 z$ for
    $z in H^* (ZZ slash 2 times G, FF_2)$, and
  + when $p$ is odd, $ZZ slash p$ consists of even permutations, so that
    $tilde(beta) = beta$ on $H^* (ZZ slash p times G, FF_p)$.

  Since the transfer map from $G$ to $ZZ slash p times G$ is zero, it now
  follows that
  $ tilde(beta) norm_(G, ZZ slash p times G) (x) = 0. $
  Since by definition
  $ norm_(G, ZZ slash p times G) (x) = sum_j a_j times.o D_j (x), $
  by Lemma~@lem:bockstein-product we have
  $
    sum_j ((-1)^j a_j times.o beta D_j (x) + beta(a_j) times.o D_j (x)) = 0,
  $
  with the further terms $a_(j+1) times.o D_j (x)$ in the sum when $p = 2$ and
  $r$ is odd. The result now follows by comparing coefficients of $a_j$, since
  $beta(a_(2j-1)) = -a_(2j)$ and $beta(a_(2j)) = 0$.
]

The Cartan formula (property (v) of the Steenrod operations) follows from the
next lemma, together with Lemma~@lem:vanishing-d-j in case $p$ is odd. It is an
easy exercise to show that the signs work out right.

#lemma(title: [cf. [@bib:Steenrod1962] VII.4.7])[
  #part-lines[
    + #source(153)If $p = 2$ then
      $ D_k (x y) = sum_(i+j=k) D_i (x) D_j (y). $
    + If $p$ is odd then
      $
        D_(2k) (x y) = (-1)^(frac(p(p-1), 2) deg(x) deg(y))
        sum_(i+j=k) D_(2i) (x) D_(2j) (y).
      $
  ]
] <lem:cartan-d-j>

#proof[
  By the multiplicativity of norm (Proposition~@prop:norm-properties[(i)]) we
  have
  $
    sum_k a_k times.o D_k (x y)
    & = norm_(G, ZZ slash p times G) (x y) \
    & = (-1)^(frac(p(p-1), 2) deg(x) deg(y))
    norm_(G, ZZ slash p times G) (x)
    norm_(G, ZZ slash p times G) (y) \
    & = (-1)^(frac(p(p-1), 2) deg(x) deg(y))
    (sum_i a_i times.o D_i (x)) (sum_j a_j times.o D_j (y)).
  $
  + If $p = 2$ then $a_i a_j = a_(i+j)$ and the formula follows by comparing
    coefficients of $a_k$.
  + If $p$ is odd then $a_i a_j = a_(i+j)$ when either $i$ or $j$ is even, while
    $a_i a_j = 0$ if $i$ and $j$ are odd. So the formula follows by comparing
    coefficients of $a_(2k)$.
]

It is somewhat more subtle to show that $Sq^0$ (resp. $P^0$) is the identity
operation, and that $Sq^n = 0$ (resp. $P^n = 0$) for $n$ negative. This is
really because Steenrod operations are defined more generally than for group
algebras, for example they are defined for cocommutative Hopf algebras, Lie
algebras, and so on, and in general these properties do not hold. So we need to
make particular use of the fact that we are working with groups. There are (at
least) two possible approaches here. One approach is to use the fact that group
cohomology may be defined as cohomology of Eilenberg–Mac~Lane spaces, and
Steenrod operations are defined for all topological spaces. The required
properties are true in this context, as is explained at the end of
Section~@sec:eilenberg-mac-lane. For further details see Steenrod and Epstein
[@bib:Steenrod1962]. The approach we shall use is to construct specific chain
maps for the standard resolution, and use these to check the required
properties.

We recall that if $bold(T)$ is a projective resolution of $FF_p$ as an
$FF_p (ZZ slash p)$-module, and $bold(C)(G)$ denotes the standard resolution of
$FF_p$ as an $FF_p G$-module (see Section~3.4 of Volume~I) then the norm map
$norm_(G, ZZ slash p times G)$ may be computed using a map of complexes of
$ZZ slash p times G$-modules
$ psi : bold(T) times.o bold(C)(G) -> bold(C)(G)^(times.o p) $
lifting the identity map on $FF_p$. Namely if $hat(zeta) : C_r (G) -> FF_p$ is
an $r$-cocycle representing $zeta in H^r (G, FF_p)$ then the composite of $psi$
with $1 wreath hat(zeta) : (bold(C)(G)^(times.o p))_(p r) -> FF_p^((r))$ is a
$p r$-cocycle on $ZZ slash p times G$ representing
$norm_(G, ZZ slash p times G) (zeta)$. We shall construct an explicit map $psi$
and use it to calculate $Sq^0$ and $Sq^(-n)$ (resp. $P^0$ and $P^(-n)$).

#source(154)We first deal with the case $p = 2$, because this is easier than the
odd case. In this case we take $bold(T)$ to be the resolution given in
Section~3.5 of Volume~I consisting of one copy of $FF_2 (ZZ slash 2)$ in each
degree $j$, with generator $alpha_j$. We then take the map $psi$ given by
$
  psi(alpha_n times.o (x_0, dots, x_r))
  & = sum_(0 <= i_1 < dots.c < i_(n+1) <= r)
  \(x_0, x_1, dots, x_(i_1), x_(i_2), x_(i_2+1), dots, \
  & quad x_(i_3), x_(i_4), dots, x_r\) times.o
  (x_(i_1), x_(i_1+1), dots, x_(i_2), x_(i_3), dots, x_(i_4), x_(i_5),
    dots, x_(i_(n+1)))
$
if $n$ is odd, and
$
  psi(alpha_n times.o (x_0, dots, x_r))
  & = sum_(0 <= i_1 < dots.c < i_(n+1) <= r)
  \(x_0, x_1, dots, x_(i_1), x_(i_2), x_(i_2+1), dots, \
  & quad x_(i_3), x_(i_4), dots, x_(i_(n+1))\) times.o
  (x_(i_1), x_(i_1+1), dots, x_(i_2), x_(i_3), dots, x_(i_4), x_(i_5),
    dots, x_r)
$
if $n$ is even. Note that for $n = 0$ this is the Alexander–Whitney map, which
confirms that for $deg(zeta) = r$ we have $Sq^r (zeta) = zeta^2$. For $n = r$ we
have
$
  psi(alpha_r times.o (x_0, dots, x_r)) = (x_0, dots, x_r) times.o
  (x_0, dots, x_r)
$
so that $Sq^0 (zeta) = zeta$. For $n > r$ we have
$ psi(alpha_n times.o (x_0, dots, x_r)) = 0 $
so that the $Sq^i$ with $i$ negative give the zero operation.

For general $p$ we must make a more complicated construction which generalises
the above construction for $p = 2$. We construct an exact sequence $bold(X)$ of
free modules for $FF_p (ZZ slash p)$ as follows. In degree $n$, the basis
elements are sequences $(lambda_1, dots, lambda_(p+n))$ such that each
$lambda_i in {1, dots, p}$, $lambda_i != lambda_(i+1)$, and each
$j in {1, dots, p}$ appears as some $lambda_i$. The generator of $ZZ slash p$
acts via
$
  (lambda_1, dots, lambda_(p+n)) |-> (lambda_1 + 1, dots, lambda_(p+n) + 1),
$
where the addition is taken modulo $p$. The differential in this complex is
given by
$
  d(lambda_1, dots, lambda_(p+n)) = sum_(i=1)^(p+n) (-1)^(i-1)
  (lambda_1, dots, lambda_(i-1), lambda_(i+1), dots, lambda_(p+n)),
$
where such a sequence is to be thought of as the zero element if it does not
satisfy the required properties. The map
$
  h(lambda_1, dots, lambda_(p+n)) = cases(
    (1, lambda_1, dots, lambda_(p+n)) & "if" lambda_1 != 1,
    0 & "if" lambda_1 = 1
  )
$
satisfies $d compose h + h compose d = 1$ on the sequences of length at least
two of the larger complex $tilde(bold(X))$ in which not every $j$ need appear,
so that $tilde(bold(X))$ has the homology of a point (see Section~2.3 of
Volume~I). The sequences in which some $j$ does not appear span a subcomplex
$bold(X)'$ of $tilde(bold(X))$ with quotient $bold(X)$. Now $bold(X)'$ is the
sum of the $p$ subcomplexes of sequences avoiding a given $j$; by the same
argument, with a letter which is not avoided in place of $1$, each intersection
of fewer than $p$ of them has the homology of a point, while all $p$ of them
intersect in zero, so the Mayer–Vietoris sequence shows that $bold(X)'$ has the
homology of a $(p - 2)$-sphere.#ed-note[The book asserts that $h$ satisfies
  $d compose h + h compose d = 1$ on $bold(X)$ itself. For $p$ odd it does not:
  for $p = 3$ the two sides differ on $(1, 2, 3, 2)$, since putting $1$ in front
  of a sequence in which every $j$ appears may give one in which some $j$ is
  repeated next to itself.] Thus $bold(X)$ is an exact sequence of free
$FF_p (ZZ slash p)$-modules. Its homology in degree zero is the trivial module.

Let $bold(T)$ be the resolution of $FF_p$ as an $FF_p (ZZ slash p)$-module
described in Section~3.5 of Volume~I, consisting of one copy of
$FF_p (ZZ slash p)$ in each degree $j$. Then the map $T_0 -> X_0$ sending the
generator to the sequence $(1, dots, p)$ #source(155)extends to a chain map
$phi.alt : bold(T) -> bold(X)$, unique up to chain homotopy. So for example
$phi.alt$ can be chosen to take the generator in degree one to
$(1, dots, p, 1)$, but in higher degrees it is rather hard to write down an
explicit chain map, except in the case $p = 2$. In this case $bold(X)$ has two
basis elements in each degree, and $phi.alt$ is an isomorphism.

We now construct a canonical map
$
  xi : bold(X) times.o bold(C)(G) -> bold(C)(G)^(times.o p) \
  (lambda_1, dots, lambda_(n+p)) times.o (x_0, dots, x_r) |->
  sum_(0 = i_0 <= i_1 <= dots.c <= i_(n+p) = r)
  (-1)^sigma u_1 times.o dots.c times.o u_p
$
where $u_j$ is defined as follows. If $lambda_(k_1), lambda_(k_2), dots$ are the
$lambda_k$ which are equal to $j$, then
$
  u_j = (x_(i_(k_1 - 1)), x_(i_(k_1 - 1) + 1), dots, x_(i_(k_1)),
    x_(i_(k_2 - 1)), dots, x_(i_(k_2)), dots).
$
The sign $sigma$ is defined as follows. Each sequence
$(x_(i_(k-1)), dots, x_(i_k))$ represents an element in degree $i_k - i_(k-1)$.
Take the permutation which takes these sequences making up
$u_1 times.o dots.c times.o u_p$ and puts them in their natural order, express
it as a product of transpositions, and for each transposition multiply by minus
one to the power of the product of the degrees.

The above sum should only be taken over those sequences satisfying
$i_(k_(j-1)) < i_(k_j - 1)$, which is the same as saying that each $u_j$ has no
repeated index.

Thus for example if $p = 3$, $n = 2$ and
$(lambda_1, dots, lambda_(n+p)) = (3, 1, 3, 1, 2)$ then
$ d(3, 1, 3, 1, 2) = (1, 3, 1, 2) - (3, 1, 3, 2). $
If $r = 2$, the only permitted sequence of $i$'s is $i_0 = 0$, $i_1 = 0$,
$i_2 = 1$, $i_3 = 2$, $i_4 = 2$, $i_5 = 2$. The corresponding term is
$(x_0, x_1, x_2) times.o (x_2) times.o (x_0, x_1, x_2)$. The corresponding
permutation sends $(x_0, x_1)$, $(x_2)$, $(x_2)$, $(x_0)$, $(x_1, x_2)$ to
$(x_0)$, $(x_0, x_1)$, $(x_1, x_2)$, $(x_2)$, $(x_2)$, so no pair of elements of
odd degree has been swapped and the sign is plus.

A straightforward but tedious combinatorial argument shows that $xi$ is a chain
map of modules for $ZZ slash p times G$ (even over the integers),#ed-note[With
  the signs described above this is not so for $p$ odd: for $p = 3$ the two
  composites differ on $(1, 2, 1, 3) times.o (x_0)$, so the signs must also
  depend on the order of the letters. The argument below uses only which terms
  occur in $xi$.] and hence the map
$
  bold(T) times.o bold(C)(G) -> bold(C)(G)^(times.o p) \
  t times.o x |-> xi(phi.alt(t) times.o x)
$
is a chain map of modules for $ZZ slash p times G$ which may be used to compute
the norm. Again for $n = 0$ this is the iterated Alexander–Whitney map (because
of the choice of $phi.alt_0$), which confirms that for $deg(zeta) = r$ we have
$P^r (zeta) = zeta^p$.

If $r > p r - n$ then there are no available sequences of $i$'s and so
$ xi((lambda_1, dots, lambda_(n+p)) times.o (x_0, dots, x_r)) = 0. $
It follows that $D_n (zeta) = 0$ for an element $zeta$ of degree $r$ with
$n > (p - 1)r$, and so $P^i = 0$ for $i$ negative.

#source(156)Similarly if $r = p r - n$, every possibility for the $i$'s gives
$(x_0, dots, x_r)^(times.o p)$, and so for every sequence of $lambda_i$'s,
$xi((lambda_1, dots, lambda_(n+p)) times.o (x_0, dots, x_r))$ is either zero or
$plus.minus (x_0, dots, x_r)^(times.o p)$. It follows that for some constant
$theta_r$ depending only on $p$ and $r$, we have
$ D_((p-1)r) (zeta) = theta_r . zeta $
for $zeta$ an element of degree $r$, so that $P^0$ is some multiple of the
identity map.

To evaluate $theta_r$, it suffices to work with any particular group $G$. If we
choose for $G$ a cyclic group of order $p$, then the calculation at the end of
Section~@sec:evens-norm shows that $theta_(2r) = (-1)^r$, while
$theta_(2r+1) = (-1)^r theta_1$. Since for an element of odd degree the exact
sign of the norm depends on the order chosen for the coset representatives of
$G$ in $ZZ slash p times G$, we are free to choose the sign of $theta_1$ as we
wish, once and for all. We calculate $theta_1$ up to sign as follows. Choose for
$G$ an elementary abelian group of order $p^2$, so that there are two elements
of cohomology in degree one whose product is non-zero. Applying the formula for
the norm of a product to these elements, we see that
$(-1)^(p(p-1) slash 2) theta_1^2 = theta_2 = -1$. Since
$(frac(p - 1, 2))!^2 = -(-1)^((p-1) slash 2)$ we may take
$theta_1 = (-1)^((p-1) slash 2) (frac(p - 1, 2))!$.#ed-note[The book takes
  $theta_1 = (frac(p - 1, 2))!$, and correspondingly the factor
  $(frac(p - 1, 2))!^(-1)$ in the norm of $y_2$ in Section~@sec:adem-relations.
  With Definition~@def:steenrod-powers the first gives $P^0 = -1$ in odd degrees
  when $p equiv 3 mod 4$, and the second leads to $beta P^j P^i + P^j beta P^i$
  in place of the commutator in the proof of the Adem relations; the value
  above, which equals $-(frac(p - 1, 2))!^(-1)$, makes both right; compare
  McCleary [@bib:McCleary2001, Theorem 4.45].]

With these values of $theta_r$ it is now easy to check that $P^0$ is the
identity map. It only remains to prove the Adem relations, and this we do in the
next section.
