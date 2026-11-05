#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/06-01-g-simplicial-complexes.typ": barycentric-subdivision

== $G$-simplicial complexes <sec:g-simplicial-complexes>

We shall be interested in group actions on topological spaces. Since we shall be
interested in homotopical properties of group actions, and every topological
space has the same weak homotopy type as its simplicial complex of singular
chains, it is no real restriction to limit our attention to simplicial
complexes#idx("complex", "simplicial")#idx("simplicial", "complex") with $G$
acting _simplicially_, i.e., in such a way that the image of a simplex under a
group element is always a simplex. Mostly our attention will be focused on the
action of $G$ on various finite simplicial complexes arising in a natural way
from the subgroup structure of $G$. We shall be interested in representation
theoretic invariants of these actions, and we shall concentrate on a definition
for an arbitrary finite group of a _generalised Steinberg module_, which will be
a virtual projective module which agrees for a Chevalley group (up to sign) with
the usual Steinberg module.

#definition[
  Suppose $G$ acts simplicially on a simplicial complex $Delta$#idx("$Delta$").
  We say that $Delta$ is a *$G$-simplicial complex*#idx(
    "$G$-simplicial complex",
  ) if whenever an element of $G$ stabilises a simplex of $Delta$ setwise, then
  it stabilises it pointwise.
] <def:g-simplicial-complex>

Note that if the action does not satisfy this last condition, we can take a
_barycentric subdivision_#idx("barycentric subdivision")#idx(
  "subdivision, barycentric",
) and then it will.
$ #barycentric-subdivision $
We'll define barycentric subdivision formally below, but informally you should
think of it as being obtained inductively from the original simplicial complex
by inserting a new vertex in the middle of each simplex, and joining it to the
previously subdivided simplices. In particular, the underlying topological space
is unchanged by this process.

#source(228)If $Delta$ is a $G$-simplicial complex, and $k$ is a commutative
ring of coefficients (we are mostly interested in the case where $k$ is a
field), we obtain a chain complex as follows. First we need to say a word or two
about orientations.

#definition[
  An *oriented simplex*#idx("oriented simplex")#idx("simplex", "oriented") is a
  simplex together with a total ordering on the set of vertices, where two
  orderings are regarded as giving the same orientation if and only if they
  differ by an even permutation. The *opposite orientation*#idx(
    "orientation, opposite",
  ) of a simplex is obtained from the given orientation by applying an odd
  permutation.
] <def:oriented-simplex>

#definition[
  We define the $n$th *chain group*#idx("chain", "group")#idx(
    "group",
    "chain",
  ) of $Delta$,#idx("$C_n (Delta)$")
  $ C_n (Delta) = C_n (Delta; k) $
  to be the $k$-module with the oriented simplices as generators, and relators
  saying that each oriented simplex is equal to minus the same simplex with the
  opposite orientation.
] <def:chain-group>

It follows from the fact that the setwise stabiliser of a simplex stabilises it
pointwise, that $C_n (Delta)$ is a permutation module. Although the permutation
basis depends on a choice of orientations consistent over $G$-orbits, the
isomorphism type of the permutation representation is well defined, and gives us
a well defined element $c_n (Delta)$#idx("$c_n (Delta)$") of the Burnside
ring#idx("Burnside ring")#idx("ring", "Burnside") $b(G)$#idx("$b(G)$") (see
Chapter~5 of Volume~I).

#subhead[Boundary maps and homology] We define boundary maps#idx("boundary map")
$ partial_n : C_n (Delta) -> C_(n-1) (Delta) $
as follows. If $(x_0, dots, x_n)$ is an oriented simplex, we define
$
  partial(x_0, dots, x_n)
  = sum_(i=0)^n (-1)^i (x_0, dots, x_(i-1), x_(i+1), dots, x_n).
$
It is easy to check that $partial_n compose partial_(n+1) = 0$, and that the
boundary maps are $k G$-module homomorphisms, and $C_n (Delta)$ is a chain
complex of $k G$-modules. Thus the homology#idx("homology") groups
$ H_n (Delta) = H_n (Delta; k) = Ker(partial_n)\/Im(partial_(n+1)) $
are also $k G$-modules.

It is also often convenient to work with reduced homology.

#definition[
  The *augmented chain complex*#idx("augmented chain complex")#idx(
    "chain",
    "complex",
    "augmented",
  ) of $Delta$ is the chain complex with an extra copy of $k$ inserted in degree
  $-1$, where the boundary homomorphism
  $ partial_0 = epsilon : C_0 (Delta; k) -> k $
  is taken to be the *augmentation map*#idx("augmentation map")#idx(
    "map",
    "augmentation",
  ) sending each zero-simplex to the identity element of $k$.

  #source(229)The *reduced homology groups*#idx("homology", "reduced")#idx(
    "reduced",
    "homology",
  ) $tilde(H)_n (Delta; k)$ are defined to be the homology groups of the
  augmented chain complex, namely
  $
    tilde(H)_n (Delta; k) = cases(
      H_n (Delta; k) & quad n != 0,
      Ker(H_0 (Delta; k) -> k) & quad n = 0
    )
  $
] <def:augmented-chain-complex>
