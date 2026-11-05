#import "main-defs.typ": *
#import "statements.typ": *

== Quillen's lemma <sec:quillen-lemma>

Our main tool for proving that complexes are homotopy equivalent is a lemma of
Quillen, which we now discuss.

#definition[
  If $f : X -> Y$ is a map of posets and $y in Y$, we define#idx(
    "$f slash y$",
  )#idx("$y class(\"normal\", backslash) f$")
  $
                              f\/y & = {x in X | f(x) <= y} subset.eq X \
    y class("normal", backslash) f & = {x in X | f(x) >= y} subset.eq X
  $
] <def:poset-fibres>

#lemma(title: [Quillen])[
  Suppose that $f : X -> Y$ is a map of posets with the property that $f\/y$
  (resp. $y class("normal", backslash) f$) is contractible for all $y in Y$.
  Then the corresponding map $|f|$ of simplicial complexes is a homotopy
  equivalence.
] <lem:quillen>
#idx("lemma", "Quillen's", target: [@lem:quillen])#idx(
  "Quillen",
  "'s lemma",
  target: [@lem:quillen],
)

#proof[
  #source(235)We shall describe the proof given in Quillen [@bib:Quillen1978],
  Section~7. Another proof may be found in Quillen [@bib:Quillen1973a],
  Theorem~A.

  It suffices to prove that $f_* : pi_1 (X, x_0) -> pi_1 (Y, f(x_0))$ is an
  isomorphism, so that $f$ lifts to a map of universal covers
  $tilde(f) : tilde(X) -> tilde(Y)$, and that
  $ tilde(f)_* : H_* (tilde(X)) -> H_* (tilde(Y)) $
  is an isomorphism. For then by the Whitehead Theorems~@th:whitehead-homology
  and~@th:whitehead-cw, $tilde(f)$ is a homotopy equivalence. Then by
  Theorem~@th:g-homotopy-equivalence, $tilde(f)$ is a $pi_1 (X, x_0)$-homotopy
  equivalence and so $f$ is a homotopy equivalence.

  To show that $f_* : pi_1 (X, x_0) -> pi_1 (Y, f(x_0))$ is an isomorphism, by
  Theorem~@th:universal-cover and the discussion following
  Definition~@def:invertible-system, it suffices to show that $f$ induces an
  equivalence of categories between invertible systems on $X$ and $Y$. If
  $cal(F)$ is an invertible system on $Y$, then the pullback $f^* cal(F)$ is the
  invertible system on $X$ defined by $f^* cal(F)(x) = cal(F)(f(x))$. If
  $x <= x'$ then the map $f^* cal(F)(x) -> f^* cal(F)(x')$ is the map
  $cal(F)(f(x)) -> cal(F)(f(x'))$ associated to the inequality $f(x) <= f(x')$.

  Conversely, if $cal(F)'$ is an invertible system on $X$, then we define an
  invertible system on $Y$ as follows. Given $y in Y$, the poset $f\/y$ is
  contractible, and hence simply connected. So $cal(F)'$ is isomorphic to a
  constant functor on $f\/y$, and so one can identify the set associated to each
  point in $f\/y$ with the set $dirlim_(x in f\/y) cal(F)'(x)$. We set
  $ f_! cal(F)'(y) = dirlim_(x in f\/y) cal(F)'(x). $
  It is easy to check that $f^*$ and $f_!$ give an equivalence of categories.

  Now the morphism $tilde(f) : tilde(X) -> tilde(Y)$ satisfies the same
  hypothesis as $f$, so we now assume $X$ and $Y$ are simply connected, and we
  must show that $f_* : H_* (X) -> H_* (Y)$ is an isomorphism. We do this by
  examining the spectral sequence of the double complex (see
  Section~@sec:double-complex) $E^0_(**)$ defined as follows. We let $E^0_(p q)$
  be the vector space over $k$ whose basis consists of pairs of chains of
  inequalities, $(y_0 < dots.c < y_p)$ in $Y$ and $(x_0 < dots.c < x_q)$ in
  $f\/y_0$. The horizontal differential $d_1$ is given by the boundary map (see
  Section~@sec:g-simplicial-complexes) on $(y_0 < dots.c < y_p)$ and the
  identity map on $(x_0 < dots.c < x_q)$. The vertical differential $d_0$ is
  given by the identity map on $(y_0 < dots.c < y_p)$ and the boundary map on
  $(x_0 < dots.c < x_q)$, multiplied by $(-1)^p$ to make the squares anticommute
  rather than commute.

  With respect to the horizontal differential, this double complex has, for each
  chain $(x_0 < dots.c < x_q)$ in $X$, the chain complex of the subposet of $Y$
  consisting of those $y$ with $y >= f(x_q)$. This poset has a minimal element,
  and is hence contractible. So if we do the horizontal differential first, we
  get $E^1 = C_* (X)$ concentrated on the vertical axis, and
  $E^infinity = E^2 = H_* (X)$.

  #source(236)On the other hand, if we do the vertical differential first, since
  $f\/y$ is contractible for each $y in Y$, we have $E^1 = C_* (Y)$ concentrated
  on the horizontal axis, and $E^infinity = E^2 = H_* (Y)$. One can verify that
  the horizontal edge homomorphism is $f_* : H_* (X) -> H_* (Y)$, which is hence
  an isomorphism.

  The proof with $y class("normal", backslash) f$ contractible is given by
  replacing $X$ and $Y$ by the opposite posets.
]

#example[
  If $X$ is a $G$-poset, we can make a simplicial complex $Delta(X)$ by allowing
  chains of not necessarily strict inequalities
  $ x_0 <= x_1 <= dots.c <= x_n. $
  This poset is in general much larger than $|X|$, and is usually infinite even
  when $X$ is finite. However, the inclusion
  $ cal(S)(|X|) arrow.r.hook cal(S)(Delta(X)) $
  is a $G$-homotopy equivalence since for each subgroup $H <= G$ a non-strict
  $H$-invariant chain has a unique maximal strict subchain, so that the strict
  subchains of such a chain form a conically contractible poset.
]

#remark(kind: "Conjecture", title: smallcaps[Webb])[
  #idx("conjecture", "Webb's")#idx("Webb's conjecture")The quotient complex
  $cal(S)_p \/G$ is contractible.
]

(Warning: one might be tempted to think this follows immediately from Sylow's
theorems, but the point is that $cal(S)_p$ needs to be barycentrically
subdivided before the quotient may be thought of as a simplicial complex.)

#exercise(kind: "Exercises")[
  Prove the following.
  + The inclusion of a $G$-poset $X$ into its barycentric subdivision
    $cal(S)(|X|)$ is a $G$-homotopy equivalence. Of course, Quillen's lemma is
    not by any means the most elementary way of proving this!
  + The inclusion of a $G$-poset $X$ into the $G$-poset of open subsets of $|X|$
    is a $G$-homotopy equivalence. Thus in particular the homology groups of a
    $G$-simplicial complex are "$G$-topological" invariants.
]
