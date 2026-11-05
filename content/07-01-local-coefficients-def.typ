#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/07-01-local-coefficients-def.typ": morphism-square

== Local coefficients <sec:local-coefficients-def>

In this Chapter we present a version of the theory of Mark Ronan and Steve
Smith#idx("Ronan–Smith") [@bib:Ronan1989, @bib:Ronan1985, @bib:Ronan1986,
@bib:Smith1985] in which representation theoretic information about a group is
obtained in a natural way from constructions involving local coefficients#idx(
  "coefficients, local",
)#idx("local", "coefficients") on $G$-simplicial complexes. The results are most
comprehensible for the case where $G$ is a Chevalley group over a field of the
same characteristic, mostly because of a theorem of Steve Smith on
irreducibility of fixed point sets. Note that in some of their papers, Ronan and
Smith use the word _sheaf_#idx("sheaf") or _presheaf_#idx("presheaf") to
describe what we refer to as a local coefficient system. We refrain from using
the word sheaf because the usual gluing condition for sheaves plays no rôle. I
hope this does not cause too much confusion.

All the material of this Chapter is due to Ronan and Smith unless otherwise
explicitly stated; any reformulation that has occurred, and all mistakes that
have crept in, are my responsibility.

#definition[
  A *$G$-equivariant local coefficient system*#idx(
    "equivariant",
    "local coefficients",
  )#idx("local", "coefficients", "equivariant") (or just an equivariant
  coefficient system) $cal(F)$#idx("$cal(F)$") of vector spaces (abelian groups,
  sets, etc.) on a $G$-poset#idx("poset") $X$ assigns to each $x in X$ a vector
  space (abelian group, set, etc.), to each inequality $x <= y$ a *restriction
  map*#idx("restriction map")#idx("map", "restriction")
  $ res_(y, x) : cal(F)(y) -> cal(F)(x) $
  satisfying
  + $res_(x, x) = id : cal(F)(x) -> cal(F)(x)$
  + If $x <= y <= z$ then $res_(y, x) compose res_(z, y) = res_(z, x)$
  and for each $g in G$, $x in X$ a map $g_* : cal(F)(x) -> cal(F)(g x)$ in such
  a way that these maps constitute a group action. In other words,
  $g_* h_* = (g h)_* : cal(F)(x) -> cal(F)(g h x)$, and
  $1_* = id : cal(F)(x) -> cal(F)(x)$.
] <def:equivariant-coefficient-system>

If you like, $cal(F)$ is an "equivariant functor"#idx(
  "equivariant",
  "functor",
)#idx("functor", "equivariant") on $X$ considered as a "$G$-category". Note that
the $G$-action makes $cal(F)(x)$ into a representation of $Stab_G (x)$.

#definition[
  A *$G$-equivariant local coefficient system* on a $G$-simplicial complex
  $Delta$ is the same as an equivariant local coefficient system on the poset of
  simplices $S(Delta)$. In other words, to each simplex $sigma$ we assign
  #source(250)a vector space $cal(F)(sigma)$, and to each inclusion
  $tau subset.eq sigma$ a restriction map $cal(F)(sigma) -> cal(F)(tau)$
  (satisfying transitivity etc. as before) together with a $G$-action.
] <def:coefficient-system-on-complex>

Conversely, given an equivariant coefficient system on a $G$-poset $X$, we
obtain an equivariant coefficient system on $|X|$ via
$ (x_0 < dots.c < x_n) |-> cal(F)(x_n) $
with the obvious restriction maps and $G$-action. Thus on the barycentric
subdivision of a $G$-complex, we assign to each simplex the value on the
smallest simplex of the original complex which contains it (thinking of the
simplicial complex and its barycentric subdivision as having the same underlying
topological space via the natural homeomorphism).

#example[
  If $M$ is a $k G$-module and $X$ is any $G$-poset or $G$-simplicial complex,
  then we have the *constant coefficient system*#idx(
    "constant coefficient system",
  )#idx("coefficient system", "constant") $kappa_M$#idx("$kappa_M$") which
  assigns $M$ to each element (resp. simplex), and where all the restriction
  maps are the identity. The $G$-action is the same as it is on $M$.
]

The coefficient systems we shall be most interested in are the *fixed point
coefficient systems*#idx("fixed point", "coefficient system")#idx(
  "coefficient system",
  "fixed point",
) of $k G$-modules. If $M$ is a $k G$-module, then the fixed point coefficient
system $cal(F)_M$#idx("$cal(F)_M$") on the $G$-poset $cal(B)_p (G)$ (or any
other $G$-poset of subgroups of $G$; see Section~@sec:g-posets) is defined by
$ cal(F)_M (P) = M^P, $
the space of fixed points of the $p$-subgroup $P$ on $M$. The $G$-action is
given via the $G$-action on $M$, and the restriction maps are inclusions. Note
that if $m in M^P$ then $g m in M^(g P g^(-1))$.

#remark[
  If $G$ is a Chevalley group, $cal(B)_p (G)$ is the barycentric subdivision of
  the building of $G$, and then this is the fixed point sheaf in the sense of
  Ronan and Smith (see for example [@bib:Ronan1985, @bib:Ronan1986]).
]

#definition[
  A *morphism*#idx("coefficient system", "morphism of")#idx(
    "morphism",
    "of coefficient systems",
  ) $cal(F) -> cal(G)$ of $G$-equivariant coefficient systems over $X$ consists
  of maps of vector spaces $cal(F)(x) -> cal(G)(x)$, for each element (resp.
  simplex) $x$ of $X$, in such a way that the following diagram commutes
  whenever $x < y$
  $ #morphism-square $
  and also commuting with the $G$-action. We write
  $Hom_(X, G) (cal(F), cal(G))$#idx("$Hom_(X, G)$") for the vector space of
  morphisms from $cal(F)$ to $cal(G)$.

  The coefficient system $cal(F)$ is a *sub-coefficient system*#idx(
    "sub-coefficient system",
  )#idx("coefficient system", "sub-") of $cal(G)$ if
  $cal(F)(x) subset.eq cal(G)(x)$ for all $x$. The *quotient coefficient
  system*#idx("quotient coefficient system")#idx(
    "coefficient system",
    "quotient",
  ) is $(cal(G) slash cal(F))(x) = cal(G)(x) slash cal(F)(x)$.

  There are also obvious notions of *direct sum, exact sequence,
  indecomposability*, etc.
] <def:coefficient-system-morphism>

#example(kind: "Examples")[
  + #source(251)The fixed point coefficient system $cal(F)_M$ is a
    sub-coefficient system of the constant coefficient system $kappa_M$, and so
    we may form the quotient coefficient system $kappa_M slash cal(F)_M$.
  + Let $G = GL_3 (FF_2)$#idx("$GL_3 (FF_2)$")#idx(
      "general linear group",
      "$GL_3 (FF_2)$",
    )#idx("group", "general linear", "$GL_3 (FF_2)$"), the group of three by
    three matrices over $FF_2$. The permutation representation on the seven
    points of the projective plane#idx("projective", "plane") over $FF_2$
    decomposes as a direct sum of a trivial one dimensional module and an
    indecomposable module $X$ of dimension six. The module $X$ is a non-split
    extension
    $ 0 -> V -> X -> V^* -> 0 $
    where $V$ is the natural three dimensional module and $V^*$ is its dual. It
    happens that taking the fixed point space of any non-trivial $p$-subgroup in
    the above sequence yields a split short exact sequence of modules for the
    normaliser. However, the splittings cannot be done in a way consistent with
    the restriction maps, and so the short exact sequence of fixed point
    coefficient systems is not split. In general, for a short exact sequence of
    modules, we only get a long exact sequence of fixed point coefficient
    systems, since taking fixed points is left exact but not right exact.
]

#definition[
  A coefficient system $cal(F)$ is *non-degenerate*#idx("non-degenerate") if
  $cal(F)(x) != 0$ for all $x$.
] <def:non-degenerate-coefficient-system>

For example, the fixed point coefficient systems discussed above are
non-degenerate, since a $p$-group always has a fixed point on any module in
characteristic $p$.
