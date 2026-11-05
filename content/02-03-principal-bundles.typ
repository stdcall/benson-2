#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-03-principal-bundles.typ": (
  local-trivialisation, whitney-pullback,
)

== Principal $G$-bundles <sec:principal-bundles>

#definition[
  A *topological group*#idx("topological", "group")#idx(
    "group",
    "topological",
  ) $G$ is a group which is simultaneously a Hausdorff topological space#idx(
    "Hausdorff space",
  )#idx("space", "Hausdorff"), in such a way that the multiplication map
  $G times G -> G$ and the inverse map $G -> G$ are continuous.
] <def:topological-group>

Examples of topological groups are the general linear group $GL_n (RR)$#idx(
  "general linear group",
  "$GL_n (RR)$",
)#idx(
  "$GL_n (RR)$",
)#idx("group", "general linear", "$GL_n (RR)$"), the unitary group#idx(
  "unitary group",
)#idx("group", "unitary") $U(n)$, the orthogonal group $O(n)$#idx(
  "orthogonal group",
  "$O(n)$",
)#idx(
  "group",
  "orthogonal",
  "$O(n)$",
), the group $Diff^+ (M)$#idx("$\"Diff\"^+ (M)$") of orientation preserving
self-diffeomorphisms of a manifold $M$ (with the compact-open topology), any
group with the discrete topology, and so on.

#definition[
  A (locally trivial) *principal $G$-bundle*#idx("principal bundle")#idx(
    "bundle",
    "principal",
  ) $xi$ is a fibre bundle $p : E -> B$ with fibre homeomorphic to $G$, and a
  *right* $G$-action $E times G -> E$ such that there exists an open cover
  ${U_alpha}$ of $B$ and homeomorphisms commuting with the right $G$-actions
  $ #local-trivialisation $
] <def:principal-bundle>

#example(kind: "Examples")[
  + #source(48)The covering $S^n -> RR P^n$ discussed in the last section is a
    principal $ZZ slash 2$-bundle.
  + According to a theorem of Chevalley, if $G$ is a Lie group and $H$ is a
    closed subgroup, then $G -> G slash H$ is a principal $H$-bundle.
  + Let $V^n (RR^m)$#idx("$V^n (RR^m)$, $V^n (CC^m)$") denote the Stiefel
    variety;#idx("Stiefel", "variety")#idx("variety", "Stiefel") namely the set
    whose elements are ordered $n$-tuples of orthonormal vectors in $RR^m$
    (these are called *$n$-frames*#idx("frame, orthonormal")#idx(
      "orthonormal frame",
    ) in $RR^m$), topologised as a subset of $(RR^m)^n$. Let $G^n (RR^m)$#idx(
      "$G^n (RR^m)$, $G^n (CC^m)$",
    ) denote the Grassmann variety;#idx("Grassmann variety")#idx(
      "variety",
      "Grassmann",
    ) namely the set whose elements are $n$-dimensional subspaces of $RR^m$,
    topologised as a subset of the projective space corresponding to
    $Lambda^n (RR^m)$. It is not hard to check that the natural map
    $V^n (RR^m) -> G^n (RR^m)$ associating to each $n$-frame its linear span, is
    a fibre bundle. There is a right action of the orthogonal group $O(n)$#idx(
      "$O(n)$",
    )#idx(
      "orthogonal group",
      "$O(n)$",
    )#idx("group", "orthogonal", "$O(n)$") on $V^n (RR^m)$, namely an
    $n times n$ orthogonal matrix tells you how to go from one $n$-frame in
    $RR^m$ to another, by linear substitutions. The orbits of $O(n)$ are the
    fibres of the map $V^n (RR^m) -> G^n (RR^m)$, making it a principal
    $O(n)$-bundle.

    Similarly, we write $V^n (CC^m) -> G^n (CC^m)$ for the principal $U(n)$#idx(
      "$U(n)$",
    )#idx("unitary group")#idx("group", "unitary")-bundle formed by performing
    the same construction with orthonormal $n$-frames in $CC^m$.

    There is an inclusion $V^n (RR^m) arrow.r.hook V^n (RR^(m+1))$ given by the
    inclusion $RR^m arrow.r.hook RR^(m+1)$, and we write $V^n (RR^infinity)$ for
    the union of the $V^n (RR^m)$, with the weak topology with respect to the
    union. We construct $G^n (RR^infinity)$ in a similar way, so that
    $V^n (RR^infinity) -> G^n (RR^infinity)$ is again a principal $O(n)$-bundle.
]

#definition[
  If $xi = (p : E -> B)$ is a principal $G$-bundle and $F$ is a left $G$-space
  (i.e., $G$ acts on $F$ in such a way that the action is given by a continuous
  map $G times F -> F$), we form a bundle $xi[F]$ as follows. The total space of
  $xi[F]$ is $E times_G F = (E times F) slash tilde$, where $tilde$ is the
  equivalence relation given by $(x g, y) tilde (x, g y)$ for all $x in E$,
  $y in F$, $g in G$. The base space is again $B$, and the map
  $p_F : E times_G F -> B$ given by $p_F (x, y) = p(x)$ makes $xi[F]$ a fibre
  bundle with fibre $F$. We say $xi[F]$ is a bundle with *structure group*#idx(
    "structure group",
  )#idx("group", "structure") $G$ and fibre $F$.
] <def:associated-bundle>

Thus for example if $G = GL_n (CC)$#idx(
  "general linear group",
  "$GL_n (CC)$",
)#idx("$GL_n (CC)$")#idx("group", "general linear", "$GL_n (CC)$") (resp.
$GL_n (RR)$) and $F = CC^n$ (resp. $RR^n$) then $xi[F]$ is a fibre bundle whose
fibres are complex (resp. real) vector spaces and where the maps
$phi.alt_alpha : p^(-1) (U_alpha) -> U_alpha times F$ are linear on each fibre.
Such a fibre bundle is called a rank#idx("rank") $n$ *vector bundle*#idx(
  "vector bundle",
)#idx("bundle", "vector"). Conversely, given a vector bundle $p : E -> B$ with
fibre $F tilde.equiv CC^n$ (resp. $RR^n$), we may recover $xi$ as follows. We
may form in a canonical way a vector bundle whose fibres are
$Hom(F, F) tilde.equiv Mat_n (CC)$ (resp. $Mat_n (RR)$). The subbundle whose
fibres are the isomorphisms from $F$ to $F$ is the principal $GL_n (CC)$-bundle
(resp. $GL_n (RR)$-bundle) $xi$. Thus there is a one–one correspondence between
rank $n$ complex (resp. real) vector bundles over $B$ and principal
$GL_n (CC)$-bundles (resp. $GL_n (RR)$-bundles) over $B$.

#definition[
  If $f : B' -> B$ is a map of base spaces and $xi = (p : E -> B)$ is a fibre
  bundle over $B$, we define $f^* (xi)$ to be the *pullback bundle*#idx(
    "bundle",
    "pullback",
  )#idx("pullback", "bundle") #source(49)over $B'$ with total space
  $ E' = {(x, y) in B' times E | f(x) = p(y)} $
  and with $p' : E' -> B'$ given by $p'(x, y) = x$.
] <def:pullback-bundle>

It is easy to see that $f^* (xi)$ is a fibre bundle with the same fibre as $xi$.
If $xi$ is a principal $G$-bundle then so is $f^* (xi)$.

#exercises[
  + If $E -> B$ and $E' -> B$ are $n$ and $m$ dimensional vector bundles, show
    that the pullback
    $ #whitney-pullback $
    constructs an $(n + m)$-dimensional vector bundle $E'' -> B$, called the
    *Whitney sum*#idx("Whitney sum")#idx("sum, Whitney") of the two bundles.
  + Tensor products of vector bundles#idx(
      "tensor product",
      "of vector bundles",
    )#idx("vector bundle", "tensor product of") are harder to define. We begin
    with product bundles. If $V$ and $W$ are vector spaces then the tensor
    product of the bundles $B times V$ and $B times W$ is the bundle
    $B times (V times.o W)$. Using the fact that the map
    $Hom(V, V') times.o Hom(W, W') -> Hom(V times.o W, V' times.o W')$ is
    continuous, show that if $B times V -> B times V'$ and
    $B times W -> B times W'$ are maps of vector bundles over $B$ then we obtain
    a map of vector bundles $B times (V times.o W) -> B times (V' times.o W')$.
    Deduce that the topology on $B times (V times.o W)$ does not depend on the
    choice of product structure. Now define tensor products of bundles
    $E times.o E' -> B$ using an open cover on which both bundles are products.
  + In a similar way, if $E -> B$ and $E' -> B$ are vector bundles of dimension
    $m$ and $n$, construct a vector bundle $Hom(E, E') -> B$ of dimension $m n$.
    Construct exterior power bundles $Lambda^i (E) -> B$ and symmetric powers
    $S^i (E) -> B$ and show that
    $E times.o E tilde.equiv Lambda^2 (E) plus.o S^2 (E)$.
]
