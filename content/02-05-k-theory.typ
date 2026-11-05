#import "main-defs.typ": *
#import "statements.typ": *

== K-theory <sec:k-theory>
#idx("K-theory", target: [@sec:k-theory])

In the last section, we saw that there is a natural one–one correspondence
between complex vector bundles of dimension $n$ over a paracompact space $B$ and
homotopy classes of maps from $B$ to $B U(n) = G^n (CC^infinity)$. Now the
obvious maps $G^n (CC^m) arrow.r.hook G^(n+1) (CC^(m+1))$ give us a map
$B U(n) arrow.r.hook B U(n + 1)$, which corresponds to adding a trivial one
dimensional summand to an $n$ dimensional vector bundle to give an $(n + 1)$
dimensional bundle. We set $B U = union.big_(n gt.eq 1) B U(n)$#idx("$B U$") via
the above maps, with the weak topology with respect to the union. Thus a
homotopy class of maps from $B$ to $B U$ corresponds to an equivalence class of
vector bundles, where two vector bundles are regarded as equivalent if they can
be made equal by adding trivial bundles on both sides.

If we restrict to the case where $B$ is compact, then given any vector bundle
over $B$, the corresponding map $B -> G^n (CC^infinity)$ has image lying in some
$G^n (CC^m)$. So there is some $(m - n)$ dimensional vector bundle the addition
of which forms an $m$ dimensional trivial bundle.

#definition[
  If $B$ is a compact space, we write $K(B)$#idx("$K(B)$") for the additive
  group whose generators $[E]$ correspond to the complex vector bundles
  $E -> B$, and whose relators say that $[E] + [E'] = [E'']$ whenever $E'' -> B$
  is the Whitney sum of $E -> B$ and $E' -> B$.
] <def:k-group>

Note that in $K(B)$, a typical element is of the form $[E_1] - [E_2]$, and that
$[E_1] - [E_2]$ is equal to $[E_3] - [E_4]$ if and only if for some $E_5$ the
Whitney sums $E_1 plus.o E_4 plus.o E_5$ and $E_2 plus.o E_3 plus.o E_5$ are
isomorphic. By the above remarks, we may always assume $E_2$, $E_4$ and $E_5$
are trivial bundles.

#proposition[
  If $B$ is a compact space, then $K(B) tilde.equiv [B; B U times ZZ]$.
] <prop:k-representable>

#proof[
  Since both sides are additive on connected components, we may assume that $B$
  is connected. Thus a map $B -> B U times ZZ$ corresponds to a map $B -> B U$
  and an integer, which we think of as giving the dimension. The map $B -> B U$
  has image lying in some $B U(n)$, and hence corresponds to some vector bundle
  $E -> B$ of dimension $n$. We add or subtract a suitable trivial bundle to
  make the dimension correspond to the image of $B -> ZZ$, and hence obtain an
  element of $K(B)$. It is easy to check that the element of $K(B)$ obtained in
  this way is well defined. There is an obvious map the #source(57)other way,
  from $K(B)$ to $[B; B U times ZZ]$, taking a generator $[E]$ of dimension $n$
  to the map given by $B -> B U(n) -> B U$ and the constant map $B -> ZZ$ with
  image $n$.
]

If $f : B' -> B$ is a map of compact spaces, the pullback of vector bundles
gives a map $f^* : K(B) -> K(B')$. If $B$ has a basepoint $x$, then the maps
${x} arrow.r.hook B arrow.r.twohead {x}$ gives us maps
$ZZ = K({x}) -> K(B) -> K({x}) = ZZ$, whose composite is the identity. Thus if
we write $tilde(K)(B)$ for the kernel of $K(B) -> ZZ$ then
$K(B) tilde.equiv tilde(K)(B) plus.o ZZ$. Note that every element of
$tilde(K)(B)$ is represented by an actual vector bundle.

The tensor product of vector bundles induces a multiplication which makes $K(B)$
(or $K O(B)$) into a commutative ring. $tilde(K)(B)$ is a ring without unit, and
the canonical process of adjoining a unit yields $K(B)$.

Using the action of a cyclic group#idx("cyclic", "group")#idx(
  "group",
  "cyclic",
) of order $n$ on the tensor $n$th power of a vector bundle, one may copy the
construction described in Section~5.9 of Volume~I to obtain operations
$psi^n$#idx("$psi^n$") on $K(B)$ or $tilde(K)(B)$. Exactly the same proof as
given in Proposition~5.9.1 of Volume~I shows that these $psi^n$ are ring
homomorphisms from $K(B)$ or $tilde(K)(B)$ to itself. In this context, the
operations $psi^n$ are called the *Adams operations*#idx(
  "Adams operations",
)#idx("operations", "Adams").

We think of $tilde(K)(B)$ as the zeroth part of a (reduced) *generalised
cohomology theory*#idx("generalised", "cohomology theory")#idx(
  "cohomology",
  "theory, generalised",
) as follows. A (reduced) generalised cohomology theory consists of
contravariant functors $tilde(h)^n$, $n in ZZ$, and natural isomorphisms
$tilde(h)^n tilde.equiv tilde(h)^(n+1) S$ ($S$ denotes suspension) from a
suitable category of spaces and maps to abelian groups, satisfying the usual
Eilenberg–Steenrod axioms#idx("Eilenberg", "–Steenrod axioms")#idx(
  "axioms, Eilenberg–Steenrod",
) for (reduced) cohomology, except the axiom giving the value on a point. These
axioms are the *homotopy axiom*#idx("homotopy", "axiom")#idx(
  "axiom",
  "homotopy",
): each $tilde(h)^n$ takes homotopic maps to the same map; and the *exactness
axiom*#idx("exactness axiom")#idx("axiom", "exactness"): if $f : X -> Y$ is a
map with mapping cone $C_f$, then the sequence
$
  tilde(h)^n (C_f) limits(->)^(j^*) tilde(h)^n (Y) limits(->)^(f^*)
  tilde(h)^n (X)
$
is exact. Note that the mapping cone of the inclusion $Y -> C_f$ is homotopy
equivalent to the suspension $S X$, so that this implies we have a long exact
sequence
$
  dots.c -> tilde(h)^(n-1) (X) = tilde(h)^n (S X) -> tilde(h)^n (C_f)
  -> tilde(h)^n (Y) -> tilde(h)^n (X) -> dots.c
$
Note also that corresponding to a reduced generalised cohomology theory, there
is a corresponding unreduced theory
$h^n (X) = tilde(h)^n (X dot(union) ("point"))$ and relative theory
$h^n (X, Y) = tilde(h)^n (C_i)$, where $C_i$ is the mapping cone of the
inclusion $i : Y -> X$ of a subspace. This relative theory satisfies the
*excision axiom*#idx("excision", "axiom")#idx("axiom", "excision"): if $Z$ is a
subspace of $Y$ whose closure is in the interior of $Y$, then the mapping cone
of the inclusion $Y without Z -> X without Z$ is homotopy equivalent to $C_i$,
and so $h^n (X without Z, Y without Z) -> h^n (X, Y)$ is an isomorphism. For
further information about generalised cohomology theories, see Switzer
[@bib:Switzer1973], Chapter~7. Other examples include cobordism and stable
cohomotopy.

#lemma[
  #source(58)If $B'$ is a closed subspace of a compact space $B$, then the
  sequence
  $ tilde(K)(B slash B') -> tilde(K)(B) -> tilde(K)(B') $
  is exact.
] <lem:k-exact-sequence>

#proof[
  The composite map is clearly zero. Conversely, every element of $tilde(K)(B)$
  is represented by an actual vector bundle. If $E -> B$ is a vector bundle
  whose restriction to $B'$ represents the zero element of $tilde(K)(B')$, then
  after adding a suitable trivial bundle we may assume that the restriction to
  $B'$ is trivial. A given trivialisation enables us to form a vector bundle
  over $B slash B'$ whose pullback to $B$ is the required bundle. (But be warned
  that different trivialisations may give rise to different elements of
  $tilde(K)(B slash B')$, so the first map in this sequence is not necessarily
  injective).
]

So to make $tilde(K)(B)$ into part of a generalised cohomology theory, for
$n gt.eq 0$ we set
$
  tilde(K)^(-n) (B) = tilde(K)(S^n B), wide
  K^(-n) (B) = tilde(K)^(-n) (B dot(union) ("point")).
$
In a similar way, if we work with real instead of complex vector bundles, we
write $B O$#idx("$B O$") for $union.big_(n gt.eq 1) B O(n)$, and $K O(B)$#idx(
  "$K O(B)$",
), $tilde(K O)(B)$, $K O^(-n) (B)$, $tilde(K O)^(-n) (B)$ for the corresponding
functors. Thus for example the analogue of Proposition~@prop:k-representable is
the statement that if $B$ is compact then
$K O(B) tilde.equiv [B; B O times ZZ]$.

#theorem(title: [Bott periodicity theorem [@bib:Bott1959]], head-break: true)[
  We have natural isomorphisms
  $
    K^(-n-2) (B) tilde.equiv K^(-n) (B), wide
    K O^(-n-8) (B) tilde.equiv K O^(-n) (B).
  $
] <th:bott-periodicity>
#idx("Bott periodicity theorem", target: [@th:bott-periodicity])#idx(
  "periodicity",
  "theorem, Bott",
  target: [@th:bott-periodicity],
)#idx("theorem", "Bott periodicity", target: [@th:bott-periodicity])

#proof[
  It is beyond the scope of this book to include a proof of the Bott periodicity
  theorem. There are now several good references available for the complex case.
  For example, see Atiyah [@bib:Atiyah1967], Husemoller [@bib:Husemoller1975],
  Milnor [@bib:Milnor1963] or Switzer [@bib:Switzer1973]. These last two
  references also contain a proof for the real case. Note that it is an easy
  exercise using the adjunction between $S$ and $Omega$ (see the exercise in
  Section~@sec:homotopy-groups) and Proposition~@prop:k-representable, to show
  that the Bott periodicity theorem is equivalent to the statements
  $ Omega^2 B U tilde.eq B U times ZZ, quad Omega^8 B O tilde.eq B O times ZZ. $
  In fact these homotopy equivalences are part of a larger pattern:
  $
    & Omega B U tilde.eq U && Omega U tilde.eq B U times ZZ \
    & Omega B O tilde.eq O && Omega O tilde.eq O slash U \
    & Omega (O slash U) tilde.eq U slash Sp wide
    && Omega (U slash Sp) tilde.eq B Sp times ZZ \
    & Omega B Sp tilde.eq Sp && Omega Sp tilde.eq Sp slash U \
    & Omega (Sp slash U) tilde.eq U slash O
    && Omega (U slash O) tilde.eq B O times ZZ
  $
  where $U$, $O$ and $Sp$ are the infinite unitary, orthogonal and symplectic
  groups, regarded as embedded in each other via the obvious maps, which double
  dimension where necessary.
]

#source(59)The Bott periodicity theorem allows us to define the functors $K^n$
and $K O^n$ for all $n in ZZ$. The following table shows the values of these
functors on a single point, as can easily be seen from the above homotopy
equivalences.

#table(
  columns: 3,
  align: center,
  [$n (mod 2)$], [0], [1],
  [$K^(-n) ("point") = tilde(K)(S^n)$], [$ZZ$], [0],
)

#table(
  columns: 9,
  align: center,
  [$n (mod 8)$], [0], [1], [2], [3], [4], [5], [6], [7],
  [$K O^(-n) ("point") = tilde(K O)(S^n)$],
  [$ZZ$],
  [$ZZ slash 2$],
  [$ZZ slash 2$],
  [0],
  [$ZZ$],
  [0],
  [0],
  [0],
)
The point here is really that to give a generalised cohomology theory $h^*$, it
suffices to define $h^n$ for $n$ (sufficiently) positive, since the isomorphisms
$tilde(h)^n tilde.equiv tilde(h)^(n+1) S$ extend the definition in the negative
direction. It is the periodicity which allows us to make the definition of $K^n$
and $K O^n$ for $n$ positive.

We next describe Atiyah’s calculation [@bib:Atiyah1961] of the K-theory of $B G$
for $G$ a finite group (or more generally, Atiyah and Segal [@bib:Atiyah1969a],
for $G$ a compact Lie group). Suppose $M$ is a finite dimensional (real or
complex) representation of $G$. Then we may form the space
$ E G times_G M = (E G times M) slash G $
where $G$ acts on $E G$ on the right and on $M$ on the left. There is an obvious
map
$ E G times_G M -> E G times_G ("point") = B G $
with fibre $M$, and making $E G times_G M$ into a (real or complex) vector
bundle over $B G$. The idea is that these vector bundles are sufficient to
determine the K-theory of $B G$. In practice, there are a few technical
difficulties, which we now describe.

The first problem is that we have only defined $K(B)$ for a compact space $B$.
However, Proposition~@prop:k-representable gives us a way to extend this
definition to all paracompact spaces, and in particular to all CW-complexes. We
define
$ K(B) = [B; B U times ZZ]. $
In general, if $B^n$ is the $n$-skeleton of $B$, it is not true that
$K(B) = invlim K(B^n)$, but we have the Milnor exact sequence
(Theorem~@th:milnor-exact-sequence)
$
  0 -> attach(invlim, tr: 1) K^(-1) (B^n) -> K(B) -> invlim K(B^n) -> 0
$
It turns out that for $B$ the classifying space of a finite (or compact Lie)
group, the $attach(invlim, tr: 1)$ term vanishes, so that an element of $K(B G)$
can be thought of as being given by a consistent family of elements of K-theory
of the skeleta. Note also that for $B$ non-compact, the Grothendieck group of
vector bundles, as defined in Definition~@def:k-group, need not coincide with
either $K(B)$ or $invlim K(B^n)$. #source(60)But a vector bundle on $B$ does
give rise to an element of $K(B)$, so we have by the above construction a
natural map
$ cal(R) (CC G) -> K(B G) $
#idx("$K(B G)$")#idx("$cal(R)(CC G)$")where $cal(R) (CC G)$ is the Grothendieck
ring of finite dimensional complex representations, as in Section~5.2 of
Volume~I.

#theorem(title: [Atiyah Completion Theorem])[
  Let $I_G$ be the kernel of the augmentation map $cal(R) (CC G) -> ZZ$ sending
  a representation to its dimension, and denote by $cal(R) (CC G)^and$ the
  completion
  $ cal(R) (CC G)^and = invlim cal(R) (CC G) slash I_G^n. $
  Then the above map $cal(R) (CC G) -> K(B G)$ induces an isomorphism
  $ cal(R) (CC G)^and tilde.equiv K(B G). $
  Moreover, $K^1 (B G) = 0$.
] <th:atiyah-completion>
#idx("Atiyah", "completion theorem", target: [@th:atiyah-completion])#idx(
  "completion theorem, Atiyah",
  target: [@th:atiyah-completion],
)#idx("theorem", "Atiyah completion", target: [@th:atiyah-completion])

#proof[
  There are two proofs available for this theorem. Atiyah’s original proof
  [@bib:Atiyah1961] for finite groups involves starting with cyclic groups,
  going up to solvable groups by induction, and then treating the arbitrary
  finite group using the Brauer induction theorem. Atiyah and Segal
  [@bib:Atiyah1969a] produced a more conceptual proof for all compact Lie
  groups. Their proof starts with the circle group $S^1$, then with the general
  torus $(S^1)^n$. The next step, involving the theory of elliptic operators,
  reduces the unitary group $U(n)$ to its maximal torus. The final step reduces
  an arbitrary compact Lie group to the unitary group by means of a faithful
  unitary representation.
]
