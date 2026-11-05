#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-01-cohomology-overview.typ": yoneda-product

== Overview of group cohomology <sec:cohomology-overview>

A good introduction to the history of the cohomology of groups can be found in
Mac~Lane [@bib:MacLane1978]. He traces the history back to the works of Hurewicz
(1936) on aspherical spaces and Hopf (1942) on the relationship between the
fundamental group and the second homology group of a space. We shall not dwell
here on the historical development, but refer the reader to Mac~Lane's article
for further information and comments.

The purpose of this chapter is to give a survey of group cohomology and how it
is connected to various other parts of mathematics, and in particular to
topological and algebraic K-theory. In the first few sections, where we provide
several definitions of group cohomology and show how they are related, we give
fairly complete proofs. Later on, we lapse into description and give enough
references so that the interested reader may chase up the proofs (we trust that
the reader will also excuse some forward references to
Chapter~@ch:spectral-sequences on spectral sequences during the later sections
of this chapter). We hope that this romp through large chunks of mathematics
will be taken as a joy ride, and not as an indigestible pill.

The first approach to group cohomology, which we have already examined in some
detail in Volume~I, is the algebraic approach. Recall from Section~2.4 of
Volume~I that if $Lambda$ is an augmented algebra over a commutative ring of
coefficients $R$, then we define homology and cohomology groups
$
  H_n (Lambda, R) = Tor^Lambda_n (R, R), quad
  H^n (Lambda, R) = Ext^n_Lambda (R, R).
$
More generally, if $M$ is a right $Lambda$-module, we define
$ H_n (Lambda, M) = Tor^Lambda_n (M, R) $
while if $M$ is a left $Lambda$-module we define
$ H^n (Lambda, M) = Ext^n_Lambda (R, M). $

These are both covariant functors in $M$, and from Section~2.5 of Volume~I we
have long exact sequences
$
  dots.c -> H_n (Lambda, M') -> H_n (Lambda, M) -> H_n (Lambda, M'')
  -> H_(n-1) (Lambda, M') -> dots.c \
  dots.c -> H^n (Lambda, M') -> H^n (Lambda, M) -> H^n (Lambda, M'')
  -> H^(n+1) (Lambda, M') -> dots.c
$
#source(42)associated to a short exact sequence of modules (right in the first
case and left in the second)
$ 0 -> M' -> M -> M'' -> 0. $

In the case where $Lambda = R G$, the group algebra of $G$ over $R$, we write
$H_n (G, M)$ and $H^n (G, M)$#idx("$H^n (G, M)$; $H_n (G, M)$") for
$H_n (R G, M)$ and $H^n (R G, M)$ respectively. Of course, by the comments in
Section~3.1 of Volume~I, we may regard right $R G$-modules as left $R G$-modules
via $g m = m g^(-1)$ and vice-versa.

Recall also from Section~2.6 of Volume~I that Yoneda composition#idx(
  "Yoneda composition",
)#idx("composition, Yoneda") defines a product structure#idx(
  "cohomology",
  "product structure",
) on cohomology
$ #yoneda-product $

We saw in Section~3.1 of Volume~I that in the case of a group algebra, this
product is _graded commutative_ in the sense that if $a in H^m (G, R)$ and
$b in H^n (G, R)$ then $a b = (-1)^(m n) b a$. The reader is warned that the
same is not true for more general augmented algebras, even for augmented
symmetric algebras. It is also not true that the ring $Ext^*_(R G) (M, M)$ is
graded commutative for an arbitrary (even simple) $R G$-module $M$.

It is often convenient for theoretical purposes, although seldom for practical
computation, to use a standard projective resolution of $R$ as an $R G$-module.
In Section~3.3 of Volume~I, we introduced the _standard resolution_#idx(
  "standard resolution",
)#idx("resolution", "standard") or _bar resolution_#idx("bar resolution")#idx(
  "resolution",
  "bar",
) and in Section~3.4 of Volume~I we used it to interpret low degree cohomology
in terms of group extensions.

The second approach to cohomology we shall examine in
Section~@sec:eilenberg-mac-lane is that of Eilenberg–Mac~Lane spaces. If $G$ is
a group, then there is a CW-complex $K(G, 1)$#idx("$K(G, 1)$") whose fundamental
group is $G$ and whose higher homotopy vanishes. This space is unique up to
homotopy equivalence, and is characterised by the contractibility of its
universal cover. Our second definition of group cohomology is
$
  H_n (G, R) = H_n (K(G, 1); R), quad H^n (G, R) = H^n (K(G, 1); R)
$
for $R$ a commutative ring of coefficients. We shall show that this agrees with
the algebraic definition by regarding the cellular chains of the universal cover
of $K(G, 1)$ as a projective resolution of $R$ as an $R G$-module.

The third definition, which we shall examine in Section~@sec:classifying-spaces,
comes via the theory of principal $G$-bundles. Roughly speaking, a principal
$G$-bundle is a fibre bundle where each fibre is a copy of the group $G$. This
definition makes sense for an arbitrary _topological group_ $G$, and it turns
out that the functor $Princ_G (X)$ assigning to a CW-complex $X$ the set of
principal $G$-bundles over #source(43)$X$ is a representable contravariant
functor. In other words, there is a CW-complex written $B G$ with the property
that there is a natural isomorphism
$ [X; B G] limits(tilde.equiv)^"nat" Princ_G (X). $
This space comes equipped with a _universal_ principal $G$-bundle, written
$xi_G : E G -> B G$, with the property that the above correspondence is given by
$ [f] |-> f^* (xi_G). $
The universal bundle is unique up to homotopy, and we give Milnor's construction
to provide a concrete model of this space. For Milnor's model, it turns out that
$E G$ is contractible, and so if $G$ has the discrete topology then $B G$ is an
Eilenberg–Mac~Lane space $K(G, 1)$. Thus if we define
$ H_n (G, R) = H_n (B G; R), quad H^n (G, R) = H^n (B G; R) $
then this definition will agree with our previous definitions in case $G$ is
discrete. In some sense, Milnor's model for $E G$ corresponds to the bar
resolution in the algebraic approach.

In case $G$ is the unitary group $U(n)$ (or the orthogonal group $O(n)$), we
shall see that principal $G$-bundles correspond naturally to complex (or real)
vector bundles, and in this way we shall see that the Grassmannians $G r_n (CC)$
and $G r_n (RR)$ are models for $B U(n)$ and $B O(n)$.

One of the benefits of the topological approach is that we have a natural
definition of _characteristic classes_ of representations. Namely if $M$ is a
$CC G$-module (resp. $RR G$-module) then $E G times_G M$ is a vector bundle over
$B G$ and hence corresponds to a map from $B G$ to $B U(n)$ (resp. $B O(n)$).
Thus pulling back cohomology classes of $B U(n)$ (resp. $B O(n)$) gives
naturally defined Chern classes (resp. Stiefel–Whitney classes) of
representations. In Chapter~@ch:spectral-sequences, we shall see that these
characteristic classes are related to the Atiyah spectral sequence, which is a
device for comparing the ordinary representation ring with the cohomology ring.

It is also worth knowing about the Kan–Thurston Theorem#idx(
  "Kan",
  "–Thurston theorem",
)#idx("theorem", "Kan–Thurston") [@bib:Kan1976], which we now state without
proof. Roughly speaking, the Kan–Thurston theorem says that every topological
space is homologically the same as some group (usually infinitely generated,
even if the space has only finitely many cells). More precisely, given any path
connected space $X$ with base point, there exists an Eilenberg–Mac~Lane space
$K(pi, 1)$ and a map $K(pi, 1) -> X$ which induces an isomorphism on (singular)
homology and cohomology with any local coefficients. In fact, the space $X$ may
be recovered up to (weak) homotopy from the group $pi$ and the kernel of the map
$pi -> pi_1 (X)$, which is a perfect normal subgroup of $pi$. Namely, there is a
construction due to Quillen, called the plus construction, which we describe in
Section~@sec:plus-construction, which kills a perfect normal subgroup of $pi_1$
of a space without affecting the homology or cohomology. The map $K(pi, 1) -> X$
gives rise to a map $K(pi, 1)^+ -> X$ which is a weak homotopy equivalence.

#source(44)It follows from the Kan–Thurston theorem that any operations one can
define on the cohomology of groups, such as for example the Steenrod operations
discussed in Chapter~@ch:evens-steenrod, are automatically operations on the
cohomology of all topological spaces. Of course, Steenrod operations were first
defined for spaces.
