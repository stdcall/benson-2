#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-04-classifying-spaces.typ": (
  bundle-retraction, classifying-map, homotopy-cover, path-fibrations,
  path-pullback, projections,
)

== Classifying spaces <sec:classifying-spaces>

We now describe the classification of principal $G$-bundles over a paracompact
base space. Fuller details may be found in Husemoller [@bib:Husemoller1975].

#proposition[
  If $B'$ is paracompact, $f, g : B' -> B$ are homotopic, and $xi$ is a
  principal $G$-bundle over $B$ then $f^* (xi) tilde.equiv g^* (xi)$ as
  principal $G$-bundles over $B'$.
] <prop:homotopic-pullbacks>

#proof[
  Let $rho : B' times I -> B' times I$ be defined by $rho(x, t) = (x, 1)$. We
  claim that given any bundle $xi' = (E' -> B' times I)$, there is a map
  $theta : E' -> E'$ such that the diagram
  $ #bundle-retraction $
  #source(50)commutes, and gives a bundle isomorphism
  $xi' tilde.equiv rho^* (xi')$. If $h : B' times I -> B$ is a homotopy from $f$
  to $g$, then applying this claim with $xi' = h^* (xi)$ proves the proposition.

  To prove the claim, we argue as follows. Since $I$ is compact we may choose an
  open cover ${U_alpha}$ of $B'$ so that the restriction of $xi'$ to each
  $U_alpha times I$ is a product bundle. Since $B'$ is paracompact, we may
  assume that ${U_alpha}$ is locally finite. Choose a partition of unity
  ${f_alpha}$ subordinate to ${U_alpha}$. Set
  $f'_alpha (x) = f_alpha (x) slash max_beta f_beta (x)$, so that the equation
  $sum_alpha f_alpha (x) = 1$ is replaced by $max_alpha f_alpha (x) = 1$. Choose
  isomorphisms
  $ phi.alt_alpha : U_alpha times I times G -> p^(-1) (U_alpha times I). $
  For each $alpha$, define maps $theta_alpha : E' -> E'$,
  $rho_alpha : B' times I -> B' times I$ fitting into a commutative square as
  above, by the formulae
  $
    theta_alpha (phi.alt_alpha (x, t, g))
    & = phi.alt_alpha (x, max(f'_alpha (x), t), g) \
    rho_alpha (x, t) & = (x, max(f'_alpha (x), t))
  $
  inside $U_alpha$, and the identity outside. Since ${U_alpha}$ is locally
  finite, if we totally order the $alpha$’s, then the infinite composites of
  these maps have only finitely many non-identity maps in a neighbourhood of
  each point. So the infinite composites make sense, and give the required maps
  $theta$ and $rho$.
]

#corollary(closed: true)[
  If $B$ is paracompact and contractible then every principal $G$-bundle over
  $B$ is isomorphic to the product bundle $B times G$.
] <cor:contractible-base>

#definition[
  A *universal $G$-bundle*#idx("bundle", "universal")#idx(
    "universal",
    "bundle",
  ) $xi_G$ is a principal $G$-bundle $E G -> B G$#idx("$E G$")#idx("$B G$") such
  that for all paracompact spaces $B$ the map
  $
    [B; B G] -> Princ_G (B) \
    f |-> f^* (xi_G)
  $
  #idx("$\"Princ\"_G (B)$")from homotopy classes of maps $B -> B G$ to principal
  $G$-bundles over $B$ is a bijection.
] <def:universal-bundle>

#lemma[
  If $xi_G = (E -> B)$ and $xi'_G = (E' -> B')$ are universal $G$-bundles with
  $B$ and $B'$ paracompact then there is a homotopy equivalence $f : B -> B'$
  with $xi_G = f^* (xi'_G)$. In particular $E$ is homotopy equivalent to $E'$ by
  a map commuting with the $G$-action.
] <lem:universal-bundle-unique>

#proof[
  Let $f : B -> B'$ correspond to $xi_G$ under the bijection
  $[B; B'] -> Princ_G (B)$, and $f' : B' -> B$ correspond to $xi'_G$ under the
  bijection $[B'; B] -> Princ_G (B')$. Then $f compose f' tilde.eq id_(B')$ and
  $f' compose f tilde.eq id_B$.
]

To prove existence of a classifying space, we use Milnor’s construction#idx(
  "construction",
  "Milnor's",
)#idx("Milnor", "'s construction").

#definition[
  If $X$ and $Y$ are topological spaces then the *join*#idx("join") $X * Y$ is
  the quotient of the product space $X times I times Y$ by the equivalence
  relation
  $
    (x, 0, y) & tilde (x', 0, y) && quad forall x, x' in X, y in Y \
    (x, 1, y) & tilde (x, 1, y') && quad forall x in X, y, y' in Y.
  $
] <def:join>

#source(51)We now define $E G$ to be the infinite join $G * G * dots.c$. Thus
$E G$ consists of formal elements
$ (t_1 g_1, t_2 g_2, dots) $
with $t_i in [0, 1]$, $t_i = 0$ for all but finitely many $i$, and
$sum t_i = 1$, modulo the equivalence relation given by
$ (t_1 g_1, t_2 g_2, dots) tilde (t_1 g'_1, t_2 g'_2, dots) $
provided $g_i = g'_i$ whenever $t_i != 0$. In case $G$ is a CW-complex, we may
give the infinite join the weak topology with respect to the union of the finite
joins, so that it is again a CW-complex, and hence paracompact. The free right
$G$-action on $E G$ is given by
$ (t_1 g_1, t_2 g_2, dots) g = (t_1 g_1 g, t_2 g_2 g, dots). $
The base space $B G$ is simply the quotient space $B G = E G slash G$. It is
easy to check that with the above definitions $xi_G = (p_G : E G -> B G)$ is a
(locally trivial) principal $G$-bundle.

#remark[
  All the topological groups we are interested in are CW-complexes. If the group
  $G$ is not a CW-complex, then the weak topology on $E G$ is not necessarily
  the right one, as it is not clear that the action of $G$ is continuous. One
  needs to use the *strong topology*#idx(
    "strong",
    "topology",
  )#idx("topology", "strong"), namely use as few open sets as possible so that
  the coordinate functions $t_i : E G -> [0, 1]$ and
  $g_i : t_i^(-1) (0, 1] -> G$ are continuous. Since $B G$ is no longer
  necessarily paracompact, one is forced to discuss numerable bundles over an
  arbitrary base space, since otherwise one loses the uniqueness argument of
  Lemma~@lem:universal-bundle-unique. One also loses local triviality of the
  bundle (see Segal [@bib:Segal1968] for a discussion of this point). In
  Husemoller [@bib:Husemoller1975], you will find the theory developed using
  numerable bundles, and without using the local triviality condition.
]

#theorem(title: [Milnor [@bib:Milnor1956b]])[
  The above bundle $xi_G = (p_G : E G -> B G)$ is a universal $G$-bundle.
] <th:milnor-universal>

#proof[
  If $xi = (p : E -> B)$ is a principal $G$-bundle over a paracompact base space
  $B$, then by Corollary~@cor:countable-cover, we may choose a countable open
  cover ${U_j}$ such that the restriction to each $U_j$ is a product bundle.
  Choose a partition of unity ${f_j}$ subordinate to ${U_j}$. Choose
  isomorphisms
  $ phi.alt_j : p^(-1) (U_j) -> U_j times G $
  and denote by $q_j : U_j times G -> G$ the second projection. Define a map
  $tilde(f) : E -> E G$ via
  $
    tilde(f) (x) = (f_1 (p(x)) q_1 (phi.alt_1 (x)),
      f_2 (p(x)) q_2 (phi.alt_2 (x)), dots).
  $
  #source(52)Then $tilde(f)$ commutes with the $G$-action, and so we get a map
  $f : B -> B G$. The square
  $ #classifying-map $
  is a pullback square, and so $xi tilde.equiv f^* (xi_G)$.

  Next, we must show that if $f, f' : B -> B G$ are maps with
  $f^* (xi_G) tilde.equiv (f')^* (xi_G)$ then $f tilde.eq f'$. Define inclusions
  $
    E G limits(arrow.r.long)^(i_"odd") E G \
    (t_1 g_1, t_2 g_2, dots) |-> (t_1 g_1, 0, t_2 g_2, 0, dots)
  $
  and
  $
    E G limits(arrow.r.long)^(i_"even") E G \
    (t_1 g_1, t_2 g_2, dots) |-> (0, t_1 g_1, 0, t_2 g_2, 0, dots).
  $
  The inclusion $i_"odd"$ is homotopic to the identity map via the $G$-map
  $ t.i_"odd" + (1 - t).id_(E G) : E G times I -> E G $
  and similarly for $i_"even"$. Thus we may pass down to maps
  $i_"odd", i_"even" : B G -> B G$ homotopic to the identity map.

  Let $xi = f^* (xi_G) tilde.equiv (f')^* (xi_G)$. Then we have maps $alpha$,
  $beta : E(xi) -> E G$ lying over $f compose i_"odd"$ and $f' compose i_"even"$
  respectively. Then the map
  $
    gamma : E(xi) times I & -> E G \
                   (x, t) & |-> t alpha(x) + (1 - t) beta(x)
  $
  lies over a homotopy $h$ from $f compose i_"odd"$ to $f' compose i_"even"$
  $ #homotopy-cover $
  So we have $f tilde.eq f compose i_"odd" tilde.eq f' compose i_"even"
  tilde.eq f'$.
]

#lemma[
  The total space $E G$ of Milnor’s construction is weakly contractible. In
  particular, if $G$ has the homotopy type of a CW-complex then $E G$ is
  contractible.
] <lem:milnor-contractible>

#proof[
  If $f : S^n -> E G = G * G * dots.c$ then since $S^n$ is compact, the image is
  contained in some finite join $G * dots.c * G$ ($r$ times). But
  $G * dots.c * G$ ($r + 1$ times) contains the cone $G * dots.c * G * (id_G)$,
  which is contractible. Hence $f$ is homotopic to a constant map in
  $G * dots.c * G$ ($r + 1$ times). The result now follows from Whitehead’s
  Theorem~@th:whitehead-cw.
]

#theorem[
  #source(53)If $G$ has the homotopy type of a CW-complex then a principal
  $G$-bundle $xi$ (over a base space $B(xi)$ having the homotopy type of a
  CW-complex) is universal if and only if the total space $E(xi)$ is
  contractible.
] <th:universal-contractible>

#proof[
  If $xi$ is universal then by Lemma~@lem:universal-bundle-unique $E(xi)$ is
  homotopy equivalent to Milnor’s $E G$, and is hence contractible. Conversely,
  if $E(xi)$ is contractible then we have a diagram
  $ #projections $
  The horizontal arrows are fibrations with contractible fibres, so the long
  exact homotopy sequence (Theorem~@th:fibration-long-exact-sequence) shows that
  they are weak homotopy equivalences, and hence homotopy equivalences by
  Theorem~@th:whitehead-cw. Hence $xi$ is universal.
]

#exercise(kind: "Exercises")[
  + If $G = ZZ slash 2$ then $G * dots.c * G$ ($r$ times) is homeomorphic to the
    $(r - 1)$-sphere $S^(r-1)$ with $G$ acting as the map taking each point to
    the antipodal point. Thus we have $E G tilde.equiv S^infinity$ and
    $B G tilde.equiv RR P^infinity$.
  + Similarly if $G = S^1 = {z in CC | |z| = 1}$ is the circle group then
    $G * dots.c * G$ ($r$ times) is the unit sphere $S^(2r-1)$ in $CC^r$ with
    $G$ acting by scalar multiplication. Thus we have $E G = S^infinity$ and
    $B G = CC P^infinity = K(ZZ, 2)$.
  + If $G$ is the orthogonal group $O(n)$ then we claim that the principal
    $O(n)$-bundle $V^n (RR^infinity) -> G^n (RR^infinity)$ is universal. Since
    $G^n (RR^infinity)$ and $V^n (RR^infinity)$ are CW-complexes, by the theorem
    it suffices to prove that $V^n (RR^infinity)$ is weakly contractible. If
    $f : S^r -> V^n (RR^infinity)$ then the image of $f$ lies in some
    $V^n (RR^m)$. But $V^n (RR^(n+m))$ contains the cone on $V^n (RR^m)$, and so
    $f$ is homotopic to a constant map inside $V^n (RR^(n+m))$. We thus write
    $B O(n)$#idx("$B O(n)$") for the space $G^n (RR^infinity)$ and $E O(n)$#idx(
      "$E O(n)$",
    ) for the space $V^n (RR^infinity)$.

    If in the definition of the Stiefel variety $V^n (RR^infinity)$ we replace
    the orthogonal $n$-frames by _all_ (linearly independent) $n$-frames, we
    still find that we have a contractible space $hat(V)^n (RR^infinity)$#idx(
      "$hat(V)^n (RR^infinity)$",
    ), by the same argument, and hence
    $hat(V)^n (RR^infinity) -> G^n (RR^infinity)$ is a universal
    $GL_n (RR)$-bundle. So we have
    $B GL_n (RR) = G^n (RR^infinity) = B O(n)$#idx("$B GL_n (RR)$").

  Now recall that there is a one–one correspondence between principal
  $GL_n (RR)$-bundles over $B$ and rank $n$ vector bundles over $B$ (see
  Section~@sec:principal-bundles), given by $xi |-> xi[RR^n]$. If we apply this
  to the bundle $hat(V)^n (RR^infinity) -> G^n (RR^infinity)$, we obtain a
  canonical rank $n$ vector bundle over $G^n (RR^infinity)$ whose total space
  $(hat(V)^n (RR^infinity) times RR^n) slash GL_n (RR)
  = (V^n (RR^infinity) times RR^n) slash O(n)$ has as its points the ordered
  pairs consisting of an $n$-dimensional subspace of $RR^infinity$ and a point
  in it. We write $hat(G)^n (RR^infinity) -> G^n (RR^infinity)$ for this
  *canonical bundle*#idx("canonical bundle")#idx("bundle", "canonical"). We have
  thus proved the following:
]

#theorem(closed: true)[
  There is a natural one–one correspondence between rank $n$ real vector bundles
  over a paracompact base space $B$ and homotopy classes #source(54)of maps
  $f : B -> G^n (RR^infinity)$. The vector bundle corresponding to $f$ is given
  by pulling back the canonical bundle
  $ hat(G)^n (RR^infinity) -> G^n (RR^infinity). $
] <th:real-vector-bundles>

In exactly the same way, the space $V^n (CC^infinity)$ is also contractible, so
that $V^n (CC^infinity) -> G^n (CC^infinity)$ is a universal bundle for the
unitary group $U(n)$#idx("$U(n)$"). The space $hat(V)^n (CC^infinity)$#idx(
  "$hat(V)^n (CC^infinity)$",
) is again contractible. We thus write $B U(n) = B GL_n (CC)$#idx(
  "$B U(n)$",
)#idx("$B GL_n (CC)$") for the space $G^n (CC^infinity)$ and $E U(n)$#idx(
  "$E U(n)$",
) for the space $V^n (CC^infinity)$. We write $hat(G)^n (CC^infinity)$ for the
total space
$
  (hat(V)^n (CC^infinity) times CC^n) slash GL_n (CC)
  = (V^n (CC^infinity) times CC^n) slash U(n)
$
of the canonical rank $n$ vector bundle over $G^n (CC^infinity)$, whose points
are ordered pairs consisting of an $n$-dimensional subspace of $CC^infinity$ and
a point in it. The corresponding theorem is as follows.

#theorem(closed: true)[
  There is a natural one–one correspondence between rank $n$ complex vector
  bundles over a paracompact base space $B$ and homotopy classes of maps
  $f : B -> G^n (CC^infinity)$. The vector bundle corresponding to $f$ is given
  by pulling back the canonical bundle
  $ hat(G)^n (CC^infinity) -> G^n (CC^infinity). $
] <th:complex-vector-bundles>

We now return to the general situation.

#theorem[
  + There is a homotopy equivalence $Omega B G tilde.eq G$#idx("$Omega B G$").
  + $pi_i (B G) tilde.equiv pi_(i-1) (G)$.
  + If $G$ is discrete then Milnor’s $B G$ is an Eilenberg–Mac~Lane space
    $K(G, 1)$#idx("$K(G, 1)$") with universal cover $E G$.
] <th:loop-space-classifying>

#proof[
  + We form a pullback diagram
    $ #path-pullback $
    where $P B G -> B G$ is the path fibration on $B G$, see the exercise in
    Section~@sec:fibrations. We thus have a diagram of fibrations
    $ #path-fibrations $
    and since $P B G$ and $E G$ are contractible we have
    $
      Omega B G tilde.eq Omega B G times E G tilde.eq X tilde.eq G times P B G
      tilde.eq G.
    $
  + This follows from the long exact sequence of the fibration $E G -> B G$.
  + #source(55)This follows from the fact that $E G$ is contractible and
    $pi_1 (B G) tilde.equiv G$, by the remark after the definition of
    Eilenberg–Mac~Lane space.
]

It follows from the above theorem that cohomology of the classifying space
$H^n (B G; R)$ is a generalisation to arbitrary topological groups of group
cohomology $H^n (G, R)$ of discrete groups. In the discrete case, there is an
obvious CW decomposition of Milnor’s $E G$ for which the cellular chains form
the standard (bar) resolution of the trivial $R G$-module $R$. Thus for a
topological group Milnor’s $E G$ may be thought of as a sort of continuous bar
resolution.

#theorem[
  + If $N$ is a closed normal subgroup of $G$, then there is a fibration
    $B G -> B(G slash N)$ with fibre $B N$.
  + If $H$ is a closed subgroup of $G$ there is a fibration $B H -> B G$ with
    fibre the coset space $G slash H$.
] <th:classifying-fibrations>

#proof[
  + Let $E(G slash N)$ and $E G$ be contractible spaces on which $G slash N$ and
    $G$ act freely. Then $N$ also acts freely on $E G$, and we may take for
    $B N$ the quotient space $(E G) slash N$. Thus $G slash N$ acts on $B N$ and
    we may take for $B G$ the space $(E(G slash N) times E G) slash G
    = (E(G slash N) times B N) slash (G slash N)$. There is then an obvious
    fibration $B G -> B(G slash N) = E(G slash N) slash (G slash N)$ given by
    the first projection, and the fibre is $B N$.
  + Let $E G$ be a contractible space on which $G$ acts freely. Then $H$ also
    acts freely on $E G$ and so we take $B G = (E G) slash G$,
    $B H = (E G) slash H$. The fibre of the obvious map $B H -> B G$ is the
    coset space $G slash H$.
]

More generally, if $rho : G -> G'$ is any group homomorphism, we may take for
$B G$ the quotient space $(E G times E G') slash G$, where $G$ acts on $E G'$
through $rho$, and for $B G'$ the quotient space $E G' slash G'$. Then we write
$B rho$ for the obvious map from $B G$ to $B G'$.

#exercises[
  + Show that every real vector bundle on a paracompact space may be given an
    orthogonal inner product, and that every complex vector bundle on a
    paracompact space may be given a unitary inner product.
  + Using Yoneda’s lemma, show that there is a map
    $B U(n) times B U(m) -> B U(n + m)$ (or $B O(n) times B O(m) -> B O(n + m)$
    in the real case) corresponding to the Whitney sum of vector bundles, and a
    map $B U(n) times B U(m) -> B U(n m)$ (resp.
    $B O(n) times B O(m) -> B O(n m)$) corresponding to tensor product of vector
    bundles.
  + If $G$ is a (discrete) group, define the *Cayley category*#idx(
      "Cayley category",
    ) of $G$ to be the category $cal(C)(G)$ whose objects are the elements of
    $G$, and whose arrows are the left multiplications by elements of $G$, so
    that there is a unique arrow between each pair of objects. $G$ acts on
    $cal(C)(G)$ by right multiplication (which commutes with left
    multiplication). Show that the nerve#idx("nerve", "of Cayley category")
    $N cal(C)(G)$ of this category (see the exercise at the end of
    Section~@sec:simplicial-sets) is a simplicial set whose topological
    realisation is Milnor’s model of $E G$.

    #source(56)If we regard the group $G$ as a category with one object, in
    which every arrow is an isomorphism, show that $N G = N cal(C)(G) slash G$
    so that $B G = |N G|$ is Milnor’s model of the classifying space $B G$.

    Define the notion of a topological category (with the topology on the
    arrows, not the objects) and show that its nerve is a simplicial
    (topological) space. Define the topological realisation of a simplicial
    space. Show that if $G$ is a topological group regarded as a topological
    category with one object, then the topological realisation of its nerve is
    Milnor’s model for $B G$.

    For further remarks on these points, see Segal [@bib:Segal1968].
]
