#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-06-fibrations.typ": (
  bundle-lifting, cube-lifting, extension-lifting, fibre-pullback,
  fibre-transport, homotopy-lifting, homotopy-lifting-cube,
  local-trivialisation, path-pullback, product-lifting, retract-lifting,
  retract-lifting-proof, simplex-lifting, transport-homotopy,
)

== Fibrations and fibre bundles <sec:fibrations>

#source(28)A fibre bundle is a sort of twisted product of one space by another,
like for example a Möbius band#idx("Möbius band"). A fibration is a homotopy
theoretic generalisation of this concept. The main homotopy theoretic properties
of fibrations are the long exact sequence in homotopy and the spectral sequence
in homology.

#definition[
  A map $p : E -> B$ has the *homotopy lifting property*#idx(
    "homotopy",
    "lifting property (HLP)",
  ) (HLP) with respect to a space $X$ if given the following commutative diagram
  of spaces, a map $H$ can always be found.
  $ #homotopy-lifting $
] <def:homotopy-lifting>

#remark[
  You should think of this as saying that a lift $f$ of one end of the homotopy
  $h$ can be extended to a lift $H$ of the entire homotopy.
]

#definition[
  A map $p : E -> B$ is a *Hurewicz fibration*#idx("fibration", "Hurewicz")#idx(
    "Hurewicz",
    "fibration",
  ) if it has HLP with respect to all spaces $X$. It is a *Serre fibration*#idx(
    "fibration",
    "Serre",
  )#idx("Serre", "fibration") if it has HLP with respect to all simplicial
  complexes.
] <def:fibration>

#remark(kind: "Remarks")[
  + The reason why it is convenient to work with the larger class of Serre
    fibrations rather than Hurewicz fibrations is that in general fibre bundles
    are only Serre fibrations, and this condition is strong enough for homotopy
    theoretic constructions. Note however that fibre bundles with $B$
    paracompact are known to be Hurewicz fibrations. The proof is quite
    involved, and is due to Hurewicz.
  + Note that taking $X$ to be a single point in the definition shows that the
    image of $p$ is a union of path components of $B$.
  + The space $B$ is called the *base space*#idx("base space")#idx(
      "space",
      "base",
    ) of the fibration, while $E$ is called the *total space*#idx(
      "space",
      "total",
    )#idx("total", "space"). The inverse image in $E$ of a point in $B$ is
    called a *fibre*#idx("fibre") and is usually denoted $F$. We shall see that
    all fibres in a path component of $B$ are homotopy equivalent.
]

The definition of fibration is easier to use in a slightly stronger form, as
given in the next lemma.

#definition[
  A subspace $A subset.eq X$ is called a *strong deformation retract*#idx(
    "deformation retract, strong",
  )#idx(
    "strong",
    "deformation retract",
  ) of $X$ if there is a homotopy $h : X times I -> X$ with $h(x, 0) = x$,
  $h(a, t) = a$ and $h(x, 1) in A$ for all $x in X$, $a in A$ and $t in I$.
] <def:strong-deformation-retract>

#lemma[
  If $(X, A)$ is a simplicial pair with $A$ a strong deformation retract of $X$
  and $p : E -> B$ is a Serre fibration then we can lift maps as in the
  following diagram:
  $ #retract-lifting $
] <lem:retract-lifting>

#proof[
  #source(29)This follows from the diagram
  $ #retract-lifting-proof $
]

The following is one of the important properties of fibrations:

#theorem(title: [Fibring property])[
  Suppose $p : E -> B$ is a Serre fibration with basepoints $p(e_0) = b_0$. If
  $B' subset.eq B$ and $E' = p^(-1) (B')$, then for $n >= 1$,
  $p_* : pi_n (E, E', e_0) -> pi_n (B, B', b_0)$ is an isomorphism.
] <th:fibring-property>
#idx("fibring property", target: [@th:fibring-property])

#proof[
  + $p_*$ is onto:\
    Elements of $pi_n$ lift as in the following diagram, in which
    $p_* (gamma) = alpha$:
    $ #cube-lifting $
  + $p_*$ is one--one:\
    If $h : p_* (alpha) tilde.eq p_* (beta)$ is a homotopy then we may lift it
    to a homotopy $H : alpha tilde.eq beta$ as in the following diagram:
    $ #homotopy-lifting-cube $
    where $(e_0)$ is the map sending the whole of $C^(n-1) times I$ to the
    basepoint $e_0$.
]

In the particular case where $B' = {b_0}$ we have $E' = F = p^(-1) (b_0)$ and
$
  p_* : pi_n (E, F, e_0) limits(arrow.r.long)^tilde.equiv pi_n (B, b_0, b_0)
  = pi_n (B, b_0).
$
Thus the long exact sequence (Proposition~@prop:homotopy-long-exact-sequence) of
the pair $(E, F)$ and Proposition~@prop:basepoint-change give us the following
theorem.

#theorem(closed: true)[
  If $F limits(->)^i E limits(->)^p B$ is a Serre fibration then there is a long
  exact sequence of homotopy groups
  $
    dots.c -> pi_n (F, e_0) limits(arrow.r.long)^(i_*) pi_n (E, e_0)
    limits(arrow.r.long)^(p_*) pi_n (B, b_0)
    limits(arrow.r.long)^(d_*) pi_(n-1) (F, e_0) -> dots.c
  $
  where the map $d_*$ is given by the composite
  $
    pi_n (B, b_0) limits(arrow.r.long)^(p_*^(-1)) pi_n (E, F, e_0)
    limits(arrow.r.long)^(partial_*) pi_(n-1) (F, e_0).
  $
  The above is a long exact sequence of modules for $pi_1 (F, e_0)$.
] <th:fibration-long-exact-sequence>

#source(30)Note that in homology, one does not obtain a long exact sequence, but
rather a spectral sequence. This is the subject of
Section~@sec:fibration-sequence.

#proposition[
  Suppose $p : E -> B$ is a fibration, and $omega : I -> B$ is a path in $B$.
  Then the fibres $p^(-1) (omega(0))$ and $p^(-1) (omega(1))$ at the two ends of
  the paths are homotopy equivalent by a map whose homotopy class only depends
  on the homotopy class of $omega$ (relative to its ends).
] <prop:fibre-transport>

#proof[
  Let $F = p^(-1) (omega(0))$ and $F' = p^(-1) (omega(1))$ be the fibres. Then
  the diagram
  $ #fibre-transport $
  gives us a map $F tilde.equiv F times 1 limits(arrow.r.long)^(alpha_1) F'$,
  and the diagram
  $ #transport-homotopy $
  shows that any two maps $alpha$, $alpha'$ obtained in this way from homotopic
  paths $omega$, $omega'$ are homotopic. If we do the same for the opposite path
  $macron(omega)(t) = omega(1 - t)$ we obtain a map $F' -> F$, again well
  defined up to homotopy. Since $omega * macron(omega)$ is homotopic to the
  identity path, the composite of these maps $F -> F' -> F$ is homotopic to the
  identity map. The same applies to $F' -> F -> F'$, and so $F tilde.eq F'$.
]

Note that the proof of the above proposition gives us an action of the
fundamental groupoid of $B$ on the fibres, up to homotopy. In particular, for
example, it shows that $pi_1 (B, b_0)$ acts on homotopy invariants such as the
homology and cohomology groups of $F$.

#definition[
  A *fibre bundle*#idx("bundle", "fibre")#idx("fibre", "bundle") with base $B$,
  total space $E$ and fibre $F$ consists of a surjective map $p : E -> B$ such
  that there is an open covering ${U_alpha}$ of $B$ and homeomorphisms
  $phi.alt_alpha$ making the following square commute:
  $ #local-trivialisation $
] <def:fibre-bundle>

In other words, a fibre bundle is locally like a product of $B$ and $F$, but may
be globally twisted. Examples are given by the Möbius band#idx(
  "Möbius band",
), and by tangent and cotangent bundles on a smooth manifold.

If $xi = (p : E -> B)$ is a fibre bundle, we write $E(xi)$ for the total space
$E$, and $B(xi)$ for the base space $B$.

#lemma[
  #source(31)If $E = B times F$, $p = pi_B : E -> B$ then $p : E -> B$ has HLP
  with respect to all $X$. Thus $p : E -> B$ is a Hurewicz fibration.
] <lem:product-fibration>

#proof[
  $ #product-lifting $
  Take $H = h times (pi_F compose f compose pi_X)$.
]

In order to show that fibre bundles are Serre fibrations, we need the following
lemma.

#lemma[
  If $p : E -> B$ has the homotopy lifting property with respect to all
  $n$-cubes $I^n$, then $p : E -> B$ has the *homotopy extension lifting
  property*#idx("homotopy", "extension lifting property (HELP)") (HELP) with
  respect to simplicial pairs $(X, A)$. In other words, partial lifts of
  homotopies can be extended to lifts as in the following diagram.
  $ #extension-lifting $
  In particular, $p : E -> B$ is a Serre fibration.
] <lem:homotopy-extension-lifting>

#proof[
  We proceed by induction on the skeleta of $X$, the zero skeleton being easy to
  handle. Suppose we have extended the lift to
  $X times 0 union X^((n-1)) times I$ and suppose $Delta$ is an $n$-simplex of
  $X$, so that the boundary $dot(Delta) subset.eq X^((n-1))$. Then we can extend
  $H$ to $X times 0 union (X^((n-1)) union Delta) times I$ as in the following
  diagram:
  $ #simplex-lifting $
  Fitting together these extensions for the various $n$-simplices of $X$, we
  have extended to $X times 0 union X^((n)) times I$. By the weak topology we
  may continue and extend to $X times I$.
]

#theorem[
  If $p : E -> B$ is a fibre bundle then it is a Serre fibration.
] <th:bundle-serre-fibration>

#proof[
  By Lemma~@lem:homotopy-extension-lifting, we only need show that $p$ has HLP
  for the $n$-cube $I^n$.
  $ #bundle-lifting $
  #source(32)Let ${U_alpha}$ be as in the definition of fibre bundle. Then
  ${h^(-1) (U_alpha)}$ is an open covering of $I^n times I$, and so by
  compactness we can choose $epsilon > 0$ such that the image under $h$ of every
  ball of diameter less than $epsilon$ in $I^n times I$ lies in some $U_alpha$
  ($epsilon$ is called the *Lebesgue covering number*#idx(
    "covering",
    "number, Lebesgue",
  )#idx("Lebesgue covering number") of this open covering). Cut $I^n times I$
  into subcubes $I_(i_1, dots, i_n) times I_j$ each small enough to fit into a
  ball of radius $epsilon$. We order these subcubes lexicographically and define
  $H$ on them by induction. At each stage, we need to know that products
  $U_alpha times F$ have HELP with respect to pairs of finite simplicial
  complexes made up out of cubes. This follows from the above two lemmas.
]

#subhead[Covering spaces]

#definition[
  If $p : E -> B$ is a fibre bundle in which the fibres are discrete sets, then
  $E$ is called a *covering space*#idx("covering", "space")#idx(
    "space",
    "covering",
  ) of $B$. By Proposition~@prop:fibre-transport, there is an action of
  $pi_1 (B, b_0)$ on $F = p^(-1) (b_0)$. If $E$ and $B$ are path connected then
  the homotopy sequence
  $
    & (0 =) pi_n (F, e_0) -> pi_n (E, e_0) -> pi_n (B, b_0)
      -> pi_(n-1) (F, e_0) (= 0) quad (n >= 2) \
    & (0 =) pi_1 (F, e_0) -> pi_1 (E, e_0) -> pi_1 (B, b_0)
      -> pi_0 (F, e_0) (= F) -> pi_0 (E, e_0) (= 0)
  $
  shows that $pi_n (E, e_0) tilde.equiv pi_n (B, b_0)$ for $n >= 2$,
  $pi_1 (B, b_0)$ acts transitively on $F$, and $pi_1 (E, e_0)$ is the
  stabiliser of the point $e_0 in F$. If $E$ and $B$ are path connected and
  $pi_1 (E, e_0) = 0$, then $E$ is called the *universal cover*#idx(
    "cover, universal",
  )#idx("universal", "cover") of $B$. Under these conditions $F$ is the regular
  permutation representation of $pi_1 (B, b_0)$.
] <def:covering-space>

#theorem[
  Suppose $B$ is path connected, and every neighbourhood of a point in $B$
  contains a simply connected neighbourhood. Then $B$ has a universal cover
  $p : (E, e_0) -> (B, b_0)$. In particular, every connected CW-complex has a
  universal cover.

  If $p' : (E', e'_0) -> (B, b_0)$ is any other cover then there is a unique map
  $(E, e_0) -> (E', e'_0)$ whose composite with $p'$ gives $p$. In particular,
  the universal cover is unique up to isomorphisms of fibre bundles over $B$.

  There is a one--one correspondence between isomorphism classes of path
  connected covering spaces $p' : (E', e'_0) -> (B, b_0)$ and conjugacy classes
  of subgroups $H <= pi_1 (B, b_0)$, given by
  $(E', e'_0) tilde.equiv (E, e_0)\/H$.
] <th:universal-cover>

#proof[
  See Spanier [@bib:Spanier1966, Sec.~2.5], where this theorem is proved under
  slightly weaker hypotheses. The idea of the proof is as follows. We construct
  $E$ as the set of ordered pairs $(x, [omega])$ consisting of a point $x$ in
  $B$ and a homotopy class $[omega]$ of paths from $b_0$ to $x$. This set is
  topologised by taking as a base for the topology sets of the following form.
  If $U$ is open in $B$, and $[omega]$ is a path from $b_0$ to $x in U$, let
  $chevron.l U, omega chevron.r$ be the set consisting of the pairs
  $(u, [omega * omega'])$ where $omega'$ is a path inside $U$. It is easy to
  check that this gives a fibre bundle, and hence a Serre fibration.

  If $p' : (E', e'_0) -> (B, b_0)$ is another cover, then we construct a map
  $(E, e_0) -> (E', e'_0)$ using the homotopy lifting property with respect to
  the unit interval. Such a lift is, of course, unique, since otherwise at the
  point #source(33)of bifurcation there is no neighbourhood in $B$ whose
  pre-image in $E'$ is a product.

  If $E'$ is path connected then the map $(E, e_0) -> (E', e'_0)$ is surjective.
  Letting $H = Im(pi_1 (E', e'_0) -> pi_1 (B, b_0))$, the long exact homotopy
  sequence shows that $H$ is the stabiliser of a point of $F'$ and so
  $(E', e'_0) tilde.equiv (E, e_0)\/H$.
]

#example(kind: "Examples")[
  + The universal cover of the circle $S^1$ is the real line $RR$. The pre-image
    of the basepoint is $pi_1 (S^1, s_0) tilde.equiv ZZ$.
  + The universal cover of the projective space $RR P^n$ ($n >= 2$) is the
    sphere $S^n$. The pre-image of the basepoint is
    $pi_1 (RR P^n, x_0) tilde.equiv ZZ\/2$.
  + The universal cover of the torus $T^2$ is the plane $RR^2$. The pre-image of
    the basepoint is $pi_1 (T^2, x_0) tilde.equiv ZZ^2$.
]

#exercise(kind: "Exercise: The path fibration")[
  #idx("path fibration")If $X$ is a based space, denote by $P X$ the path space
  $Map_* ((I, 0), (X, x_0))$ of paths in $X$ starting at the basepoint $x_0$.
  Show that the map $P X -> X$ sending a path $omega : (I, 0) -> (X, x_0)$ to
  $omega(1)$ is a Hurewicz fibration, with fibre $Omega X$. Show that $P X$ is
  contractible.
]

#subhead[Replacing a map by a fibration] If $f : Y -> X$ is a map of based
spaces, denote by $P_f$ the space of ordered pairs $(y, omega)$ consisting of a
point $y$ in $Y$ and an unbased map $omega : I -> X$ with $omega(1) = f(y)$; in
other words, the pullback
$ #path-pullback $
Show that $P_f$ is homotopy equivalent to $Y$ via the first projection
$(y, omega) |-> y$. Show that the composite map $P_f -> Y -> X$ is homotopic to
the map $P_f -> X$ sending $(y, omega)$ to $omega(0)$, and that the latter map
is a Hurewicz fibration. In this way we have replaced the original map $Y -> X$
by the fibration $P_f -> X$. The fibre $F_f$ of the map $P_f -> X$ is called the
*homotopy fibre*#idx("fibre", "homotopy")#idx("homotopy", "fibre") of $f$, and
consists of ordered pairs $(y, omega)$ as above with $omega(1) = f(y)$ and
$omega(0) = x_0$; in other words, the pullback
$ #fibre-pullback $
