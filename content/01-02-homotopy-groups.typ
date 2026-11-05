#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-02-homotopy-groups.typ": (
  commutative-law, open-square, theta-figure,
)

== Homotopy groups <sec:homotopy-groups>

In this section we give an extremely compressed account of the homotopy groups
$pi_n$ of a space. The interested reader is advised to refer to a standard
source, for example Mosher and Tangora [@bib:Mosher1968], Spanier
[@bib:Spanier1966], Switzer [@bib:Switzer1973], Whitehead [@bib:Whitehead1978],
for a more extensive account of this topic.

#definition[
  If $f, f' : X -> Y$ are (continuous) maps of topological spaces, then we say
  $f$ is *homotopic*#idx("homotopy") to $f'$ (written $f tilde.eq f'$#idx(
    "$tilde.eq$",
  )) if there exists a map $F : X times I -> Y$ (where $I$#idx("$I$") is the
  unit interval $[0, 1]$) such that $F(x, 0) = f(x)$ and $F(x, 1) = f'(x)$. It
  is clear that homotopy is an equivalence relation on maps. We write
  $[X; Y]$#idx("$[X; Y]$") for the homotopy classes#idx(
    "class",
    "homotopy",
  )#idx("homotopy", "class") of maps from $X$ to $Y$.

  We say $X$ and $Y$ are *homotopy equivalent*#idx(
    "equivalence",
    "homotopy",
  )#idx("homotopy", "equivalence") if there are maps $f : X -> Y$ and
  $f' : Y -> X$ such that the composites are homotopic to the identity maps
  $f compose f' tilde.eq id_Y$ and $f' compose f tilde.eq id_X$.

  We say $X$ is *contractible*#idx("contractible") if it is homotopy equivalent
  to a single point. In particular, note that a contractible space must be
  non-empty.
] <def:homotopic>

We write $[X, x_0; Y, y_0]$ for homotopy classes of maps respecting basepoints.
The homotopies should respect basepoints in the sense that
$F(x_0 times I) = y_0$. If $A$ is a subspace of $X$ containing $x_0$ and $B$ is
a subspace of $Y$ containing $y_0$, we write $f : (X, A, x_0) -> (Y, B, y_0)$ to
indicate that $f(A) subset.eq B$. We write $[X, A, x_0; Y, B, y_0]$ for homotopy
classes of maps $f : X -> Y$ such that $f(A) subset.eq B$ and $f(x_0) = y_0$. Of
course, the homotopies $F : X times I -> Y$ should also have the property that
$F(A times I) subset.eq B$ and $F(x_0 times I) = y_0$. If $F$ is constant on
$A$, so that $f$ and $f'$ agree on $A$, we say that $f$ is homotopic to $f'$
*relative to* $A$.

#definition[
  The *homotopy groups*#idx("group", "homotopy")#idx(
    "homotopy",
    "group",
  )#idx("$pi_n (X, x_0)$") of a based space $(X, x_0)$ are defined to be
  $ pi_n (X, x_0) = [S^n, s_0; X, x_0] $
  where $(S^n, s_0)$#idx("$S^n$") is an $n$-sphere with basepoint.
] <def:homotopy-groups>

Thus for example $pi_1 (X, x_0)$ is the set of equivalence classes of paths from
the basepoint to itself (*loops*#idx("loop")), where two such are equivalent if
one can #source(15)be deformed to the other while keeping the two ends fixed. If
$X$ is path connected and $pi_1 (X, x_0) = 0$ then we say $(X, x_0)$ is *simply
connected*#idx("simply connected").

Since $S^0$ consists of two points, one of which is the basepoint,
$pi_0 (X, x_0)$ is the set of path components of $X$.

#subhead[Group structure] The set $pi_n (X, x_0)$ ($n >= 1$) can be given the
structure of a group as follows. We regard $(S^n, s_0)$ as an $n$-cube with its
boundary identified to a single point, $(I^n, dot(I)^n)$. Now to compose two
elements $[f]$ and $[g]$ of $pi_n (X, x_0)$, we "divide and stretch" along the
first coordinate:
$ f * g : I^n -> X $
#symbol-display(
  "(1)",
  $
    (f * g)(s_1, dots, s_n) = cases(
      f(2 s_1, s_2, dots, s_n) & quad 0 <= s_1 <= 1/2,
      g(2 s_1 - 1, s_2, dots, s_n) & quad 1/2 <= s_1 <= 1.
    )
  $,
) <eq:divide-and-stretch>
It is easy to check that if $f tilde.eq f'$ and $g tilde.eq g'$ then
$f * g tilde.eq f' * g'$, so that this induces a well defined multiplication on
$pi_n (X, x_0)$.

#proposition[
  The above defined multiplication makes $pi_n (X, x_0)$ into a group for
  $n >= 1$, and an abelian group for $n >= 2$.
] <prop:homotopy-group-structure>

#proof[
  The identity element is given by the constant map. The inverse in
  $pi_n (X, x_0)$ of an element $[f]$ is given by $[f']$, where
  $ f'(s_1, s_2, dots, s_n) = f(1 - s_1, s_2, dots, s_n). $
  The associative law corresponds to the "obvious" homotopy from
  $(f_1 * f_2) * f_3$ to $f_1 * (f_2 * f_3)$ given by
  $
    F((s_1, dots, s_n), t) = cases(
      f_1 ((4 s_1)/(1 + t), s_2, dots, s_n) & quad 0 <= s_1 <= (1 + t)/4,
      f_2 lr((4 s_1 - 1 - t, s_2, dots, s_n))
      & quad frac(1 + t, 4) <= s_1 <= frac(2 + t, 4),
      f_3 lr((frac(4 s_1 - 2 - t, 2 - t), s_2, dots, s_n))
      & quad frac(2 + t, 4) <= s_1 <= 1
    )
  $
  (Draw a diagram!) Similarly for $n >= 2$, the commutative law corresponds to
  the following diagram:
  $ #commutative-law $
  Here, the horizontal and vertical directions are the first and second
  coordinates in $I^n$, and the areas marked with an asterisk all go to the
  basepoint in $X$.
]

#remark[
  It is sometimes convenient to work with the (homotopy equivalent) space of
  maps from $[0, a] times I^(n-1)$ to $X$ (sending the boundary to $x_0$) rather
  than $I^n$ to $X$, where $a$ is regarded as a variable. Composition of a map
  from $[0, a] times I^(n-1)$ and a map from $[0, b] times I^(n-1)$ gives a map
  from $[0, a + b] times I^(n-1)$. This composition has the advantage of being
  strictly associative rather than just homotopy associative. For $n = 1$, such
  maps are called *Moore loops*#idx("Moore loops")#idx("loop", "Moore") on $X$.
]

#figure([#source(16)#theta-figure], caption: [The map $theta$]) <fig:theta>

#definition[
  The group $pi_1 (X, x_0)$ is called the *fundamental group*#idx(
    "fundamental group, groupoid",
  )#idx(
    "group",
    "fundamental",
  ) of the space $(X, x_0)$.
] <def:fundamental-group>

#remark[
  The set of homotopy classes of paths in $X$ with possibly different ends,
  where the homotopies are required to fix both ends of the path, form a
  groupoid. Namely, we can only compose one path with another if the endpoint of
  the first equals the starting point of the second. This groupoid is called the
  *fundamental groupoid*#idx("groupoid, fundamental") of $X$, and does not
  depend on choice of basepoint.
]

#subhead[Relative homotopy groups] If $(X, A, x_0)$ is a based pair, we define
its *relative homotopy groups*#idx("group", "relative homotopy")#idx(
  "homotopy",
  "group",
  "relative",
)#idx("relative", "homotopy group")#idx("$pi_n (X, A, x_0)$") to be
$
  pi_n (X, A, x_0) = [D^n, S^(n-1), s_0; X, A, x_0]
  = [I^n, dot(I)^n, C^(n-1); X, A, x_0].
$
Here $D^n$ is the $n$ dimensional disc, with boundary $S^(n-1)$, and
$C^(n-1) = dot(I)^n without circle(I)^(n-1)$#idx("$C^n$") is the boundary of
$I^n$ with the interior of the face $I^(n-1)$ (with the _last_ coordinate zero)
removed. This subspace is identified to a point and regarded as the basepoint.

For example if $n = 2$ then
$ C^(n-1) = #open-square $

#proposition[
  Suppose $pi_n (X, A, x_0) = 0$. Then any map
  $ f : (D^n, S^(n-1), s_0) -> (X, A, x_0) $
  is homotopic relative to $S^(n-1)$ (i.e., via a homotopy which is constant on
  $S^(n-1)$) to a map $f'$ with $f'(D^n) subset.eq A$.
] <prop:relative-compression>

#proof[
  Regard $f$ as a map $(I^n, dot(I)^n, C^(n-1)) -> (X, A, x_0)$. There is a
  homotopy $F : I^n times I -> X$ with $F(u, 0) = f(u)$ and $F(u, 1) = x_0$ for
  all $u in I^n$, $F(u, t) in A$ for all $u in dot(I)^n$, and $F(u, t) = x_0$
  for all $u in C^(n-1)$. Composing $F$ with the map
  $theta : I^n times I -> I^n times I$ given in Figure~@fig:theta we obtain the
  required homotopy from $f$ to a suitable $f'$.
]

#source(17)For $n >= 2$, we can give $pi_n (X, A, x_0)$ a multiplication
according to Formula~@eq:divide-and-stretch[1].

#proposition(closed: true)[
  The set $pi_n (X, A, x_0)$ is a pointed set#idx("pointed set") (i.e., a set
  with a distinguished element, namely the constant map at the basepoint) for
  $n = 1$, a group for $n >= 2$, and an abelian group for $n >= 3$.
] <prop:relative-homotopy-groups>

#remark(kind: "Warning")[
  There is no excision#idx("excision") in homotopy, so that in general
  $ pi_n (X, A, x_0) != pi_n (X\/A, A\/A). $
]

#subhead[Boundary map]#idx("boundary map") If
$f : (I^n, dot(I)^n, C^(n-1)) -> (X, A, x_0)$ then we define
$ partial_n (f) = f|_(I^(n-1)) : (I^(n-1), dot(I)^(n-1)) -> (A, x_0) $
(note that $I^(n-1) subset.eq dot(I)^n$ and
$C^(n-1) inter I^(n-1) = dot(I)^(n-1)$). It is easy to check that if
$f tilde.eq f'$ as maps of based pairs then
$partial_n (f) tilde.eq partial_n (f')$ as maps of based spaces, so that
$partial_n$ induces a well defined map
$ partial_n : pi_n (X, A, x_0) -> pi_(n-1) (A, x_0) quad (n >= 1). $

#subhead[Long exact sequence]

#proposition[
  Given a based pair $(X, A, x_0)$, the natural maps
  $i : (A, x_0) arrow.r.hook (X, x_0)$ and $j : (X, x_0) -> (X, A, x_0)$
  together with the boundary map defined above give rise to a long exact
  sequence#idx("exact", "sequence", "homotopy")#idx(
    "homotopy",
    "exact sequence",
  )
  $
    dots.c limits(arrow.r.long)^(j_*) pi_(n+1) (X, A, x_0)
    limits(arrow.r.long)^(partial_*) pi_n (A, x_0)
    limits(arrow.r.long)^(i_*) pi_n (X, x_0) limits(arrow.r.long)^(j_*)
    pi_n (X, A, x_0) limits(arrow.r.long)^(partial_*) dots.c
  $
] <prop:homotopy-long-exact-sequence>

#remark[
  Exactness of the above sequence should be interpreted as follows. For
  $n >= 1$, it is an exact sequence of groups, and the image of $pi_2 (X, x_0)$
  lies in the centre of $pi_2 (X, A, x_0)$. For $n = 0$, these are only pointed
  sets (sets with a distinguished basepoint). The sequence is exact everywhere
  in the sense that the kernel of each map (pre-image of the basepoint) is the
  image of the previous map. Also, the map $pi_1 (X, x_0) -> pi_1 (X, A, x_0)$
  extends to an action of $pi_1 (X, x_0)$ on $pi_1 (X, A, x_0)$, and elements
  are in the same orbit if and only if they have the same image in
  $pi_0 (A, x_0)$.#ed-note[The book states that the image of $pi_2 (X, A, x_0)$
    lies in the centre of $pi_1 (A, x_0)$, and that $pi_1 (X, A, x_0)$ acts on
    $pi_0 (A, x_0)$. For $A = S^1 or S^1$ and $X$ the cone on $A$, the image of
    $pi_2 (X, A, x_0)$ is the whole free group $pi_1 (A, x_0)$ of rank two, and
    $pi_1 (X, A, x_0)$ is in general only a pointed set; see tom Dieck
    [@bib:TomDieck2008, (6.2.7) and Section 6.2, Problem 2].]
]

#proof[
  We shall assume that $n >= 2$ for the proof, and leave the reader to make the
  necessary changes for $n = 0$ and $1$. There are six separate checks to be
  made here.

  / $j_* compose i_* = 0$\:: If $f : (I^n, dot(I)^n, C^(n-1)) -> (X, A, x_0)$
    with $f(I^n) subset.eq A$ then we have a homotopy $F : I^n times I -> X$
    given by $F(t_1, dots, t_n, t) = f(t_1, dots, t_(n-1), t + (1 - t) t_n)$,
    showing that $[f] = 0$ in $pi_n (X, A, x_0)$.
  / $Ker(j_*) subset.eq Im(i_*)$\:: If $f : (I^n, dot(I)^n) -> (X, x_0)$ and
    $j_* [f] = 0$ then there is a homotopy $F : I^n times I -> X$ such that
    $F(u, 0) = f(u)$ and $F(u, 1) = x_0$ for all $u in I^n$, $F(u, t) in A$ for
    all $u in dot(I)^n$, and $F(u, t) = x_0$ for all $u in C^(n-1)$. Compose $F$
    with the map $theta : I^n times I -> I^n times I$ given in
    Figure~@fig:theta, to obtain a homotopy from $f$ to a map
    $(I^n, dot(I)^n) -> (A, x_0)$.
  / $i_* compose partial_* = 0$\:: If
    $f : (I^(n+1), dot(I)^(n+1), C^n) -> (X, A, x_0)$ then
    $i_* partial_* [f] = [f|_(I^n)]$. The map $f$ provides a homotopy from
    $f|_(I^n)$ to the constant map at $x_0$.
  / #source(18)$Ker(i_*) subset.eq Im(partial_*)$\:: If
    $f : (I^n, dot(I)^n) -> (A, x_0)$ with $i_* [f] = 0$ in $pi_n (X, x_0)$,
    then there is a homotopy $F : (I^n times I, dot(I)^n times I) -> (X, x_0)$
    with $F(u, 0) = f(u)$ and $F(u, 1) = x_0$. Regarding $F$ as a map
    $I^(n+1) -> X$, $[F]$ is an element of $pi_(n+1) (X, A, x_0)$ with
    $partial_* [F] = [f]$.
  / $partial_* compose j_* = 0$\:: If $f : (I^n, dot(I)^n) -> (X, x_0)$ then
    $partial_* j_* [f] = [f|_(I^(n-1))]$. Since $f$ sends $I^(n-1)$ to $x_0$,
    $partial_* j_* [f] = 0$.
  / $Ker(partial_*) subset.eq Im(j_*)$\:: For this, we need the following fact.
    Given any map from $dot(I)^n times I union I^n times {0}$ to $X$, we may
    extend it to a map from $I^n times I$ to $X$. In other words, any partial
    homotopy may be extended to a homotopy. We express this by saying that the
    pair $(I^n, dot(I)^n)$ has the *homotopy extension property*#idx(
      "homotopy",
      "extension property (HEP)",
    ) (HEP) with respect to $X$. A space which has the homotopy extension
    property with respect to all spaces $X$ is called a *cofibration*#idx(
      "cofibration",
    ). The reason why $(I^n, dot(I)^n)$ is a cofibration is because there is a
    *retraction*#idx("retraction")
    $I^n times I -> dot(I)^n times I union I^n times {0}$, i.e., a map whose
    composite with the inclusion is the identity map on
    $dot(I)^n times I union I^n times {0}$.

    Now if $f : (I^n, dot(I)^n, C^(n-1)) -> (X, A, x_0)$ with
    $partial_* [f] = [f|_(I^(n-1))] = 0$, then there is a homotopy
    $F : (I^(n-1) times I, dot(I)^(n-1) times I) -> (A, x_0)$ with
    $F(u, 0) = f(u)$ and $F(u, 1) = x_0$. Thus there is a partially defined
    homotopy
    $
                dot(I)^n times I union I^n times 0 & -> X \
                         (u, t) in I^(n-1) times I & |-> F(u, t) \
      (u, t) in (dot(I)^n without I^(n-1)) times I & |-> x_0 \
                             (u, t) in I^n times 0 & |-> f(u).
    $
    Extend to a homotopy $I^n times I -> X$, and restrict to $I^n times 1$ to
    obtain a map $alpha : I^n -> X$ with $f tilde.eq j(alpha)$, so that
    $[f] = j_* [alpha]$.
]

#subhead[Action of $pi_1$ on $pi_n$, and invariance of basepoint] If $x_0$ and
$x_1$ are two different basepoints in $X$, and $omega : I -> X$ is a path with
$omega(0) = x_0$ and $omega(1) = x_1$, we define a map
$ omega^* : pi_n (X, x_1) -> pi_n (X, x_0) $
as follows. Given a map $f : (S^n, s_0) tilde.equiv (D^n, S^(n-1)) -> (X, x_1)$
we define
$
  omega^* (f) : (D^n, S^(n-1)) -> (X, x_0) \
  u |-> cases(
    f(2 u) & quad "if" 0 <= |u| <= 1/2,
    omega(2 - 2|u|) & quad "if" 1/2 <= |u| <= 1
  )
$
where $|u|$ is the distance from the origin to $u$ in $D^n subset.eq RR^n$, and
$2 u$ is calculated inside the vector space $RR^n$. In words, the part of the
disk from radius $1$ to radius $1/2$ is sent along the path $omega$. The part of
the disk with radius at most $1/2$ is homeomorphic to the whole disk, and is
sent into $X$ by composing the original map with this homeomorphism.

If $f tilde.eq f'$ then $omega^* (f) tilde.eq omega^* (f')$ so that this map is
well defined.

#source(19)Similarly if $x_0, x_1 in A subset.eq X$ are two different basepoints
in $(X, A)$, and $omega : I -> A$ is a path with $omega(0) = x_0$ and
$omega(1) = x_1$, we define an isomorphism
$ omega^* : pi_n (X, A, x_1) -> pi_n (X, A, x_0) $
as follows. Given a map $f : (D^n, S^(n-1), (1, 0, dots, 0)) -> (X, A, x_1)$,
the map $omega^* (f) : (D^n, S^(n-1), (1, 0, dots, 0)) -> (X, A, x_0)$ is given
by sending $(x_0, dots, x_n)$ to $omega(1 - x_0)$ if $0 <= x_0 <= 1$. We choose
a homeomorphism between the half of the disk with $x_0 <= 0$ with the points
with $x_0 = 0$ identified to a single point $*$, and the entire disk $D^n$ with
basepoint $(1, 0, dots, 0)$. We compose this homeomorphism with the original map
$f$ to define $omega^* (f)$ for $x_0 <= 0$.

Again if $f tilde.eq f'$ then $omega^* (f) tilde.eq omega^* (f')$, so that this
map is well defined.

#proposition[
  If $omega$, $omega' : I -> X$ are homotopic relative to ${0, 1}$, then
  $omega^* = (omega')^* : pi_n (X, x_1) -> pi_n (X, x_0)$. For $x_0 = x_1$, this
  constitutes a group action of $pi_1 (X, x_0)$ on $pi_n (X, x_0)$.

  If $omega tilde.eq omega' : I -> A$ then
  $omega^* = (omega')^* : pi_n (X, A, x_1) -> pi_n (X, A, x_0)$. For
  $x_0 = x_1$, this constitutes a group action of $pi_1 (A, x_0)$ on
  $pi_n (X, A, x_0)$.

  The long exact homotopy sequence
  $
    dots.c -> pi_(n+1) (X, A, x_0) -> pi_n (A, x_0) -> pi_n (X, x_0)
    -> pi_n (X, A, x_0) -> dots.c
  $
  is a long exact sequence of $pi_1 (A, x_0)$-modules.
] <prop:basepoint-change>

#proof[
  This is a long but straightforward exercise in keeping your head. See Spanier
  [@bib:Spanier1966, Section~7.3] for the details.
]

#remark(kind: "Notation")[
  We write $pi'_n (X, x_0)$#idx("$pi'_n (X, x_0)$") for the quotient of
  $pi_n (X, x_0)$ obtained by identifying $omega^* (f)$ with $f$ for each
  $[omega] in pi_1 (X, x_0)$, and $pi'_n (X, A, x_0)$#idx("$pi'_n (X, A, x_0)$")
  for the quotient of $pi_n (X, A, x_0)$ obtained by identifying $omega^* (f)$
  with $f$ for each $[omega] in pi_1 (A, x_0)$. Note that the action of
  $pi_1 (X, x_0)$ on itself is by conjugation, so that $pi'_1 (X, x_0)$ is its
  abelianisation.

  We say that $(X, x_0)$ is a *simple space*#idx("simple space")#idx(
    "space",
    "simple",
  ) if $pi_1 (X, x_0)$ acts trivially on $pi_n (X, x_0)$ for all $n$, so that
  $pi'_n (X, x_0) = pi_n (X, x_0)$, and in particular $pi_1 (X, x_0)$ is
  abelian.
]

Elements of $pi_n (X, x_0)$ may be thought of as obstructions to extending maps
$S^n -> X$ to maps $D^(n+1) -> X$ as shown by the following proposition:

#proposition[
  Suppose $X$ is path connected and $pi_n (X, x_0) = 0$. Then any map
  $f : S^n -> X$ may be extended to a map $tilde(f) : D^(n+1) -> X$.
] <prop:extension-obstruction>

#proof[
  Since $X$ is path connected, $pi_n (X, f(s_0)) = 0$, so the map
  $f : (S^n, s_0) -> (X, f(s_0))$ is homotopic to the constant map at $f(s_0)$.
  Such a homotopy is a map $S^n times I -> X$ sending
  $S^n times 0 union s_0 times I$ to $f(s_0)$ and equal to $f$ on $S^n times 1$.
  Since $(S^n times I, S^n times 0 union S^n times 1 union s_0 times I,
    S^n times 0 union s_0 times I) tilde.equiv (D^(n+1), S^n, s_0)$ the
  proposition follows.
]

The theory of obstructions#idx("obstruction theory") was developed by Eilenberg
and others, and an account of it may be found, for example, in Mosher and
Tangora [@bib:Mosher1968, Chapter~1].

#subhead[#source(20)Loop spaces] There is an alternative approach to homotopy
groups based on the concept of a loop space.

#definition[
  We define the *loop space*#idx("loop", "space")#idx("space", "loop")
  $Omega X$#idx(
    "$Omega X$",
  ) of a based space $X$ to be
  $ Omega X = Map_* (S^1, X), $
  with the constant path at $x_0$ (written $*$) as basepoint.
] <def:loop-space>

Now a path in $Omega X$ is the same thing as a homotopy between loops in $X$ (by
the correspondence given in Proposition~@prop:exponential), and so we have
$ pi_1 (X, x_0) tilde.equiv pi_0 (Omega X, *). $

By Proposition~@prop:based-exponential, we have
$
  Omega^2 X = Map_* (S^1, Map_* (S^1, X)) tilde.equiv Map_* (S^1 and S^1, X)
  tilde.equiv Map_* (S^2, X).
$
Continuing in this way, and using the fact that $S^(n-1) and S^1 tilde.equiv
S^n$, we have
$ Omega^n X tilde.equiv Map_* (S^n, X). $
A path in $Omega^n X$ is the same as a homotopy between maps $S^n -> X$, and so
we have proved the following:

#proposition(closed: true)[
  $pi_n (X, x_0) tilde.equiv pi_0 (Omega^n X, *)$.
] <prop:loop-space-homotopy>

In a similar way, if $(X, A, x_0)$ is a based pair, we define $P(X, A, x_0)$ to
be the space of paths in $X$ beginning at $x_0$ and ending in $A$. By a similar
argument to the above, we have the following:

#proposition(closed: true)[
  $pi_n (X, A, x_0) tilde.equiv pi_0 (Omega^(n-1) P(X, A, x_0), *)$.
] <prop:path-space-homotopy>

For further details see for example Switzer [@bib:Switzer1973, Chapter~3], where
the long exact sequence (Proposition~@prop:homotopy-long-exact-sequence) is
developed from this point of view.

#exercise[
  The (reduced) *suspension*#idx("suspension") $S X$ of a space $X$ is defined
  to be $S^1 and X$. The $n$th suspension of $X$ is
  $S^n X = S dots.c S X = S^n and X$. Show that if $X$ is Hausdorff then there
  is a natural homeomorphism
  $ Map_* (S X, Y) -> Map_* (X, Omega Y). $
  Deduce that there is a natural bijection
  $ [S^n X; Y] tilde.equiv [X; Omega^n Y]. $
  Thus $S$ and $Omega$ are adjoint functors.
]
