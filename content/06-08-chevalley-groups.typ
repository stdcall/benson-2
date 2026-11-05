#import "main-defs.typ": *
#import "statements.typ": *

== Chevalley groups: a crash course <sec:chevalley-groups>

In the case where $G$ is a Chevalley group#idx("Chevalley group")#idx(
  "group",
  "Chevalley",
) in characteristic $p$, we wish to compare $St_p (G)$ with the usual definition
via the Tits building. We begin with a quick review of Chevalley groups, and we
shall illustrate with the example of $GL_n (FF_q)$.

#subhead[Linear algebraic groups] In Section~@sec:commutative-algebra, we gave a
quick review of varieties and commutative algebra. We briefly recall the
definition, and then define linear algebraic groups.

#definition[
  An *affine variety*#idx("affine", "variety")#idx("variety", "affine") is a set
  of points in an affine space, given by the simultaneous vanishing of a set of
  polynomials. A *linear algebraic group*#idx("linear algebraic group")#idx(
    "algebraic",
    "group",
    "linear",
  )#idx("group", "linear algebraic") over an algebraically closed field $k$ of
  characteristic $p$ is an affine variety $V$ together with a compatible group
  structure. This means that the multiplication map $V times V -> V$ and the
  inverse map $V -> V$ are morphisms of varieties (i.e., the coordinates of the
  map are given by polynomials).
] <def:linear-algebraic-group>

For example, $SL_n (k)$#idx("$SL_n (k)$")#idx(
  "special",
  "linear group",
  "$SL_n (k)$",
)#idx("group", "special linear", "$SL_n (k)$") can be regarded as the set of
zeroes of the determinant function minus one. The group $GL_n (k)$#idx(
  "$GL_n (k)$",
)#idx("general linear group", "$GL_n (k)$")#idx(
  "group",
  "general linear",
  "$GL_n (k)$",
) can be viewed as a linear algebraic group by taking coordinates
$x_11, dots, x_(n n), y$, and using the polynomial equation
$y det(x_(i j)) = 1$. It turns out that every linear algebraic group is
isomorphic to a closed subgroup of $GL_n (k)$ for some $n$.

Other examples of linear algebraic groups are the orthogonal groups
$O_n (k)$#idx("$O_n (k)$")#idx("orthogonal group", "$O_n (k)$")#idx(
  "group",
  "orthogonal",
  "$O_n (k)$",
), the special orthogonal groups $S O_n (k)$#idx("$S O_n (k)$")#idx(
  "special",
  "orthogonal group $S O_n (k)$",
)#idx("group", "special orthogonal", "$S O_n (k)$"), the symplectic groups
$Sp_(2n) (k)$#idx("$Sp_(2n) (k)$")#idx(
  "symplectic group",
  "$Sp_(2n) (k)$",
)#idx("group", "symplectic", "$Sp_(2n) (k)$"), and the unitriangular groups
$Uni_n (k)$#idx("$Uni_n (k)$")#idx("unitriangular group")#idx(
  "group",
  "unitriangular",
) consisting of all $n times n$ upper triangular matrices with ones on the
diagonal.

A good background reference for the theory of linear algebraic groups is
Humphreys [@bib:Humphreys1975].

#definition[
  A linear algebraic group is called *connected*#idx(
    "connected algebraic group",
  )#idx("algebraic", "group", "connected") if it is connected in the Zariski
  topology (in other words, the underlying variety cannot be written as a
  disjoint union of two proper subvarieties each defined by the vanishing of
  some polynomials). It is called *unipotent*#idx("unipotent", "group")#idx(
    "group",
    "unipotent",
  ) if it is isomorphic to a subgroup of $Uni_n (k)$ for some value of $n$. It
  is called *reductive*#idx("reductive group")#idx("group", "reductive") if it
  has no non-trivial normal closed connected unipotent subgroups. Thus all the
  examples given above, with the exception of $Uni_n (k)$ are reductive linear
  algebraic groups. Of these, $O_n (k)$ is not connected, but the rest are.

  #source(241)An algebraic group is *defined*#footnote[Actually, if $k_0$ is not
    perfect, the situation is more subtle, but that need not concern us here as
    we are primarily interested in the case where $k_0$ is finite.] *over*
  $k_0 <= k$ if the equations defining it as a variety and the equations giving
  the multiplication and inversion can be written with coefficients in $k_0$.
  For example, $GL_n (k)$ is defined over the ground field $FF_p$.
] <def:reductive-group>

#subhead[Classification] The classification of reductive linear algebraic
groups#idx("classification of reductive groups")#idx(
  "reductive group",
  "classification of",
) depends on the notion of a root system. A *torus*#idx("torus") is a linear
algebraic group isomorphic to a direct product of copies of the multiplicative
group of the field. For example, the group of diagonal matrices of a given size
is a torus. It turns out that in a reductive group $G$, the maximal subgroups
isomorphic to a torus (the *maximal tori*#idx("maximal", "torus")) are all
conjugate. The *Lie rank*#idx("Lie", "rank")#idx("rank", "Lie") of $G$ is the
dimension of a maximal torus. The *semisimple rank* of $G$ is defined to be the
Lie rank of the derived group of $G$. Now, the characters (i.e., one-dimensional
representations) of a torus $T$ form a free abelian group $chi(T)$#idx(
  "$chi(T)$",
)#idx("character of a torus") under tensor product, whose rank is equal to the
dimension of the torus. Inside $chi(T)$, the *root system*#idx(
  "root system",
)#idx("system", "root") of $G$ is the set of non-zero characters of $T$
occurring in the restriction to $T$ of the action of $G$ by (the derivative of)
conjugation on its Lie algebra#idx("Lie", "algebra")#idx(
  "algebra",
  "Lie",
) (i.e., the tangent space at the identity element).

For example, if $G = GL_n (k)$ then $T$ can be taken to be the subgroup of
diagonal matrices (commuting diagonalisable matrices are simultaneously
diagonalisable), and the characters of $T$ correspond to sequences
$r_1, dots, r_n$ of integers, the corresponding character of $T$ being given by
$ diag(x_1, dots, x_n) |-> x_1^(r_1) dots x_n^(r_n). $
The Lie algebra of $G$ is the Lie algebra $g l_n (k)$ of all $n times n$
matrices. The eigenspaces of $T$ with non-zero eigenvalues, in its conjugation
action on $g l_n (k)$, are the matrices with a non-zero entry in only one
(given) position, off the diagonal. If this entry is in the $(i j)$th place,
then the corresponding character is the one with $r_i = +1$, $r_j = -1$, and all
other $r_k = 0$. These roots lie in the hyperplane $sum r_i = 0$ of $chi(T)$.

It turns out that the root system of a connected reductive group determines the
isomorphism type of the group modulo its largest normal abelian subgroup. The
root system is an (abstract) root system in the sense of Humphreys
[@bib:Humphreys1972, Chapter~3] where it is also explained how to classify root
systems. Every root system is a direct sum of indecomposable root systems, and
the indecomposable root systems are classified by their *Dynkin diagram*#idx(
  "Dynkin diagram",
)#idx("diagram, Dynkin"). A list of the Dynkin diagrams is given in the above
reference on p.~58, or in Chapter~4 of Volume~I. Their names are $A_l$,
$l >= 1$; $B_l$, $l >= 2$; $C_l$, $l >= 3$; $D_l$, $l >= 4$; $E_6$, $E_7$,
$E_8$, $F_4$ and $G_2$. The subscript refers to the (semisimple) rank.

For example, the root system described above for $GL_n (k)$ is an indecomposable
root system of type $A_(n-1)$. The root system for $S O_(2n+1) (k)$ is of type
$B_n$, for $Sp_(2n) (k)$ it is of type $C_n$, and for $S O_(2n) (k)$ it is of
type $D_n$. The remaining Dynkin diagrams correspond to the so-called
"exceptional types"#idx("exceptional", "type")#idx(
  "type",
  "exceptional",
) of connected reductive group.

#subhead[#source(242)The Frobenius morphism] If a linear algebraic group $G$ is
defined over the finite field of $q = p^e$ elements, then the *Frobenius
morphism*#idx("Frobenius", "morphism")#idx("morphism", "Frobenius") $F$ with
respect to this finite field is the morphism of algebraic groups given by
raising the coordinates to the $q$th power. If $G$ is connected and reductive
then the *Chevalley group*#idx("Chevalley group")#idx("group", "Chevalley")
$G(FF_q)$#idx("$G(FF_q)$") is defined to be the group $G^F$#idx("$G^F$") of
fixed points of $F$ on $G$. Note that there are also Chevalley groups over
infinite fields or rings, defined in a related fashion. We shall not be
concerned with these here.

For example, if $G = GL_n (k)$, then $G^F = GL_n (FF_q)$#idx(
  "$GL_n (FF_q)$",
)#idx(
  "general linear group",
  "$GL_n (FF_q)$",
)#idx("group", "general linear", "$GL_n (FF_q)$"), since $F$ acts by raising the
matrix entries to the $q$th power, and $FF_q$ is exactly the set of solutions of
the equation $x^q = x$.

#subhead[Parabolic subgroups] If $H$ is a closed subgroup of a linear algebraic
group $G$, then there is a theorem of Chevalley (see Humphreys
[@bib:Humphreys1975, p.~80]) which says that there is a finite dimensional
representation of $G$ with the property that $H$ is exactly the stabiliser of
some one-dimensional subspace. Taking the orbit of the corresponding point in
projective space gives the coset space $G slash H$ the structure of a
quasiprojective variety.

#definition[
  A *parabolic subgroup*#idx("parabolic subgroup")#idx("subgroup", "parabolic")
  of a reductive group $G$ is a proper subgroup $P$ with the property that the
  orbit space $G slash P$ is a projective variety.

  A *Borel subgroup*#idx("Borel", "subgroup")#idx("subgroup", "Borel") $B$ of
  $G$ is a maximal connected solvable closed subgroup.
] <def:parabolic-subgroup>

It turns out that a subgroup is parabolic if and only if it contains a Borel
subgroup, and that the Borel subgroups are all conjugate. The parabolic
subgroups containing a given Borel subgroup are in one-one correspondence with
the proper subsets of the set of vertices of the Dynkin diagram. If $G$ is
defined over $FF_q$ then there is always an $F$-stable Borel subgroup, and the
parabolic subgroups containing it are also $F$-stable. If $P$ is an $F$-stable
parabolic then we call $P^F$ a parabolic subgroup of $G^F$.

For example, in the case $G = GL_n (k)$, the Borel subgroups are the conjugates
of the group of upper triangular matrices, i.e., the stabilisers of complete
flags. A *flag*#idx("flag") in the vector space $V$ on which $G$ acts is a chain
of proper subspaces
$ 0 < V_1 < dots.c < V_s < V. $
A flag is *complete*#idx("complete flag")#idx("flag", "complete") if there is
one subspace of each possible dimension. The parabolic subgroups containing a
given Borel subgroup are the stabilisers of subflags of the corresponding
complete flag. Thus with respect to a suitable basis the parabolics look
something like this:
$
  mat(augment: #(hline: (1, 2), vline: (1, 2)), *, *, *; 0, *, *; 0, 0, *)
$
In the case of $Sp_(2n) (k)$ and $S O_n (k)$ the corresponding concepts are the
flags of isotropic subspaces. In the case of $S O_(2n) (k)$, the fact that there
are two types #source(243)of maximal isotropic subspaces is reflected in the
fact that the $D_n$ diagram has a bifurcation at one end.

The *unipotent radical*#idx("unipotent", "radical")#idx("radical", "unipotent")
of a parabolic subgroup is the largest normal unipotent subgroup. In the above
example, the unipotent radical has the form:
$
  mat(augment: #(hline: (1, 2), vline: (1, 2)), I, *, *; 0, I, *; 0, 0, I)
$
If $P$ is $F$-stable, then so is its unipotent radical $U$, and we call $U^F$
the unipotent radical of $P^F$. In fact these are related by $U^F = O_p (P^F)$.

#subhead[The poset $cal(B)_p (G)$#idx("$cal(B)_p (G)$")]

#theorem(title: [Borel, Tits])[
  If $G^F$ is a Chevalley group then a $p$-subgroup $U$ is equal to
  $O_p N_(G^F) (U)$ if and only if $N_(G^F) (U)$ is parabolic and $U$ is its
  unipotent radical.
] <th:borel-tits>
#idx("Borel", "–Tits theorem", target: [@th:borel-tits])

#proof[
  This was first proved in A.~Borel and J.~Tits [@bib:Borel1971]. A simpler
  proof (but one which only applies to the finite Chevalley groups, which is no
  inconvenience to us here!) may be found in N.~Burgoyne and C.~Williamson
  [@bib:Burgoyne1976]. We shall give a proof for the particular case where
  $G^F = GL_n (FF_q)$. Suppose $U$ is a $p$-subgroup of $G^F$. Denote by $V_1$
  the fixed space of $U$ (which is automatically non-trivial since we are in
  characteristic $p$), and inductively define $V_i$ to be the subspace
  containing $V_(i-1)$ with the property that $V_i slash V_(i-1)$ is the fixed
  space of $U$ on $V slash V_(i-1)$. It is clear by induction that $V_i$ is
  $U$-invariant, so that the definition makes sense at the next stage. Now let
  $H$ denote the set of all elements of $G^F$ which stabilise the $V_i$ and act
  trivially on the $V_i slash V_(i-1)$. Then $H$ is a $p$-group (since it is
  contained in $Uni_n (FF_q)$ with respect to a suitable basis) and it contains
  $U$ and is normalised by $N = N_(G^F) (U)$ since it is defined in an invariant
  way in terms of $U$. If $U != H$ then $U < N_H (U) <= O_p (N)$. Thus $U = H$
  is the unipotent radical of the parabolic subgroup $N$ corresponding to the
  flag $0 < V_1 < dots.c < V_s < V$.
]

Thus the poset $cal(B)_p (G^F)$ is the opposite poset to the poset of parabolic
subgroups ordered by inclusion.

#subhead[The Tits Building] The Tits building#idx("Tits building")#idx(
  "building, Tits",
) of a Chevalley group $G^F$ is defined to be the simplicial complex whose
simplices are indexed by the parabolic subgroups of $G^F$, and where the
inclusion relation between simplices is the opposite of the inclusion relation
between parabolic subgroups. Thus the vertices (0-simplices) correspond to the
maximal parabolics, the edges (1-simplices) to "sub-maximal" parabolics, and so
on. The simplices of maximal dimension have dimension $(r - 1)$, where $r$ is
the semisimple rank, and correspond to the Borel subgroups. Every simplex is
contained in one of maximal dimension. It is clear that $cal(B)_p (G^F)$ is the
poset of simplices of the Tits building, and so $|cal(B)_p (G^F)|$ is the
barycentric subdivision of the Tits building, and is hence homeomorphic to it.

#source(244)For example, in the case $G^F = GL_n (FF_q)$, the parabolic
subgroups correspond to the chains of proper subspaces (i.e., subspaces which
are non-zero and not equal to the whole space) of the space $V^F$ over $FF_q$ on
which $G^F$ acts, and so the Tits building is the simplicial realisation of the
poset $italic("Subsp")(V^F)$#idx("$italic(\"Subsp\")(V^F)$") of proper subspaces
of $V^F$. Similarly in the symplectic and orthogonal cases, but with proper
subspaces replaced by proper isotropic subspaces. In general, it is possible to
realise the building as the simplicial realisation of a poset, but this involves
making a choice of an orientation for each of the edges of the Dynkin diagram.

#theorem(title: [Solomon [@bib:Solomon1969], Tits])[
  The Tits building of $G^F$ is homotopy equivalent to a bouquet of spheres#idx(
    "bouquet of spheres",
  )#idx("spheres, bouquet of") of the same dimension (i.e., take some spheres,
  and identify a point in each sphere, to give a single base-point, like a bunch
  of balloons; this construction is called the *wedge product*#idx("wedge")).
  The dimension of the spheres is $(r - 1)$, and the number of spheres is $q$ to
  the power of half the number of roots in the corresponding root system.
] <th:solomon-tits>
#idx("Solomon–Tits theorem", target: [@th:solomon-tits])#idx(
  "theorem",
  "Solomon–Tits",
  target: [@th:solomon-tits],
)

#proof[
  We shall give Quillen's proof [@bib:Quillen1973b] of this fact, in the case
  where $G^F = GL_n (FF_q)$. The proof goes by induction on $n$. For $n = 2$ the
  building is clearly a collection of disjoint points, which is a bouquet of
  0-spheres (a 0-sphere is just two disjoint points), so suppose $n >= 3$.
  Choose a line (one-dimensional subspace) $L$ in $V^F$, and denote by $cal(H)$
  the set of hyperplanes complementary to $L$.

  We claim that the poset $Y = italic("Subsp")(V^F) without cal(H)$ is
  contractible. To show this, consider the quotient map
  $q : Y -> underbrace(italic("Subsp"))(V^F slash L)$, where
  $underbrace(italic("Subsp"))$ denotes the poset of all proper subspaces,
  together with the zero subspace. This poset has a unique minimal element, and
  is hence contractible. Thus by Quillen's Lemma~@lem:quillen, it suffices to
  show that $q slash W$ is contractible for each element $W$ of
  $underbrace(italic("Subsp"))(V^F slash L)$. But this is clear, since this
  sub-poset has a unique maximal element, namely the preimage in $V^F$ of $W$.

  It follows that the building is homotopy equivalent to the complex obtained by
  contracting the subcomplex corresponding to $Y$ down to a point. The latter
  complex may be described as follows. For $H in cal(H)$, let $Link(H)$#idx(
    "link",
  ) denote the subcomplex of the building consisting of those simplices not
  containing $H$, but which are contained in simplices containing $H$. Then the
  contracted complex is the wedge product of the unreduced suspensions#idx(
    "unreduced suspension",
  )#idx(
    "suspension",
    "unreduced",
  ) of the complexes $Link(H)$ (the unreduced suspension of a space is formed by
  taking a direct product with the unit interval, and identifying each end of
  the resulting "cylinder" to a point). But $Link(H)$ is just the complex of
  proper subspaces of $H$.

  The number and dimension of the spheres is easy to calculate from this
  argument.
]

#remark(kind: "Remarks")[
  + With a bit of work, this proof may be made to generalise to the remaining
    classes of Chevalley groups. It simply needs to be expressed #source(245)in
    the language of parabolic subgroups. This is left as a (difficult) exercise
    for the interested reader.
  + Of course, there is nothing special about the finiteness of the field for
    this argument. In fact it even works for non-commutative division rings.
]

#subhead[The Steinberg module] It follows from the above theorem that the
building has only one non-trivial reduced homology group, and this occurs in
degree $(r - 1)$. This reduced homology group is what is usually referred to as
the Steinberg module#idx("Steinberg module")#idx("module", "Steinberg") of a
Chevalley group. The preceding discussion makes it clear that it differs from
our definition of $St_p (G^F)$ only by a sign $(-1)^(r-1)$.

#remark[
  It has been shown by Lusztig that the ideal of virtual projective modules in
  the representation ring of a Chevalley group is the principal ideal generated
  by the Steinberg module. Note, however, that for a general group, this ideal
  is not necessarily principal.
]
