#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-14-cyclic-sets.typ": (
  cyclic-set-b-bicomplex, cyclic-set-bicomplex,
)

== Cyclic sets <sec:cyclic-sets>

In order to calculate the cyclic homology of a group ring, we need to introduce
Connes' notion of a cyclic object in a category. This is a variant of the
concept of a simplicial object (Section~@sec:simplicial-sets), and cyclic sets
bear the same relation to topological spaces with an action of the circle group
$S^1$ that simplicial sets do to topological spaces (Dwyer, Hopkins and Kan
[@bib:Dwyer1985]).

We shall show that the cyclic homology of a group ring $R G$ is the same as the
ordinary homology of $E S^1 times_(S^1) L B G$, where $S^1$ acts on the free
loop space $L B G$ by rotating the loops. Just as in the case of Hochschild
homology, this admits a decomposition as a sum over conjugacy classes of
elements, which we investigate in the next section. Instead of the classifying
space of the centraliser of the corresponding element, one uses a sort of
extended centraliser obtained by gluing in a copy of the circle or the real
line, depending on whether the element has finite or infinite order. Our
approach is close to that of Burghelea and Fiedorowicz [@bib:Burghelea1986b] and
Burghelea [@bib:Burghelea1985], but see also Goodwillie [@bib:Goodwillie1985]
and Jones [@bib:Jones1987].

Let $and.big$#idx("$and.big$") be the category whose objects are the finite
cyclically ordered sets#idx("cyclically ordered sets"), and whose arrows are the
functions preserving the cyclic ordering. More #source(98)precisely (Connes
[@bib:Connes1983]), an object in $and.big$ consists of a finite set together
with an injection into $S^1$, and an arrow in $and.big$ from one such object to
another consists of a homotopy class of monotonic (but not necessarily strictly
monotonic) continuous maps $S^1 -> S^1$ of degree one such that the image of the
first finite set is contained in the second. In particular, there are $n$ arrows
from a cyclically ordered set of size $n$ to one of size one. A *cyclic
object*#idx("cyclic", "object")#idx("object", "cyclic") $X$ in a category
$cal(C)$ is a contravariant functor $and.big -> cal(C)$. A *cyclic set*#idx(
  "cyclic",
  "set",
)#idx("set", "cyclic") is a cyclic object in the category of sets. If $X$ is a
cyclic object, we write $X_n$ for the image of the cyclically ordered set
${0, dots, n}$ (with the cyclic ordering $0 < 1 < dots.c < n < 0$) in $cal(C)$.
The face maps $d_i : X_n -> X_(n-1)$ ($0 <= i <= n$) and degeneracy maps
$s_i : X_n -> X_(n+1)$ ($0 <= i <= n$) are defined in exactly the same way as
for a simplicial object, but we also have a new map $t_n : X_n -> X_n$ which is
the image of the map
$
  {0, dots, n} & -> {0, dots, n} \
             j & |-> j - 1 quad (mod n + 1).
$
These maps satisfy the relations given in Section~@sec:simplicial-sets for the
$s_j$ and $d_j$, together with the following relations between these and the
$t_n$:
$
  d_i t_n & = t_(n-1) d_(i-1) & wide s_i t_n & = t_(n+1) s_(i-1)
  & quad & 1 <= i <= n \
  d_0 t_n & = d_n & wide s_0 t_n & = t_(n+1)^2 s_n \
  (t_n)^(n+1) & = 1
$
All maps and relations coming from $and.big$ follow from these. So giving a
cyclic object $X$ in $cal(C)$ is the same as giving objects $X_n$ in $cal(C)$,
$0 <= n < infinity$, and maps $d_i : X_n -> X_(n-1)$, $s_i : X_n -> X_(n+1)$ and
$t_n : X_n -> X_n$ satisfying these relations.

A *cyclic map*#idx("cyclic", "map")#idx("map", "cyclic") $f : X -> Y$ between
cyclic objects is a natural transformation of functors; this amounts to giving
maps $f_n : X_n -> Y_n$ satisfying $f_(n-1) d_i = d_i f_n$,
$f_(n+1) s_i = s_i f_n$ and $f_n t_n = t_n f_n$ for all $0 <= i <= n$. Thus
cyclic objects in a category $cal(C)$ form a category $bold("Cycl") cal(C)$#idx(
  "$bold(\"Cycl\") cal(C)$",
).

There is an obvious functor $triangle.stroked.t -> and.big$ taking a totally
ordered finite set to the corresponding cyclically ordered set, and regarding a
monotonic function as a function preserving the cyclic ordering. By composing
with this functor, a cyclic object gives rise to a simplicial object, and so we
have an obvious forgetful functor $bold("Cycl") cal(C) -> bold("Simp") cal(C)$.

#example(kind: "Examples")[
  #enum(numbering: "1.")[
    The simplicial set $S G slash G$ corresponding to the Hochschild complex
    (see Section~@sec:free-loops) has the structure of a cyclic set with
    $
      t_n (g_0 times.o g_1 times.o dots.c times.o g_n)
      = g_n times.o g_0 times.o dots.c times.o g_(n-1).
    $
    More generally, the Hochschild complex of a ring $Lambda$ (see
    Section~@sec:hochschild) is a cyclic $R$-module with
    $
      t_n (lambda_0 times.o lambda_1 times.o dots.c times.o lambda_n)
      = lambda_n times.o lambda_0 times.o dots.c times.o lambda_(n-1).
    $
  ][
    Let $S[1]$ be the simplicial circle; namely the simplicial set with one
    non-degenerate zero-simplex $*$, one non-degenerate 1-simplex $sigma$, and
    no other #source(99)non-degenerate simplices. If $X$ is a simplicial set,
    then the simplicial set $Hom(S[1], X)$ is a cyclic set as follows. Writing
    $(macron(s)_i sigma, s_i tau)$, $0 <= i <= n$, for the $n + 1$
    non-degenerate $(n + 1)$-simplices in $S[1] times Delta[n]$ as in the proof
    of Proposition~@prop:free-loops-simplicial, we let $t_n$ act via
    $
      t_n f(macron(s)_i sigma, s_i tau)
      = f(macron(s)_(i+1) sigma, s_(i+1) tau),
    $
    where the subscript $i + 1$ is to be read modulo $n + 1$. With these
    structures of cyclic sets, it is straightforward (but tedious!) to check
    that the isomorphism given in Proposition~@prop:free-loops-simplicial is an
    isomorphism of cyclic sets.
  ][
    If $Y$ is a topological space with a continuous action of the circle group
    $S^1 = {e^(2 pi i theta), 0 <= theta <= 1}$, we give the singular simplicial
    set on $Y$ the structure of a cyclic set as follows. If $f : Delta^n -> Y$
    is a singular $n$-simplex, then we set
    $ t_n f(x_0, dots, x_n) = e^(2 pi i x_0) f(x_n, x_0, dots, x_(n-1)). $
    It is easy to check that this definition satisfies the appropriate
    relations. Thus $Sing(-)$#idx("$\"Sing\"(Y)$") is a functor from spaces with
    $S^1$-action to cyclic sets.
  ][
    The forgetful functor $bold("Cycl") cal(C) -> bold("Simp") cal(C)$ described
    above has a left adjoint, which assigns to each simplicial object $X$ the
    free cyclic object#idx("free", "cyclic object") $S[1] bowtie X$#idx(
      "$S[1] bowtie X$",
    )#idx("$bowtie$") whose $n$-simplices are pairs $(t_n^j, x)$, $0 <= j <= n$,
    $x in X_n$ with cyclic structure given by
    $
        d_i (t_n^j, x) & = (t_(n-1)^j, d_(i-j) x)         & wide & i - j >= 0 \
        d_i (t_n^j, x) & = (t_(n-1)^(j-1), d_(i-j+n+1) x) &      & i - j < 0 \
        d_n (t_n^n, x) & = (t_(n-1)^0, d_0 x) \
        s_i (t_n^j, x) & = (t_(n+1)^j, s_(i-j) x)         &      & i - j >= 0 \
        s_i (t_n^j, x) & = (t_(n+1)^(j+1), s_(i-j+n+1) x) &      & i - j < 0 \
      t_n^i (t_n^j, x) & = (t_n^(i+j), x)                 &      & i + j <= n \
      t_n^i (t_n^j, x) & = (t_n^(i+j-n-1), x)             &      & i + j > n.
    $
    In particular, $S[1] = S[1] bowtie *$ is a cyclic set.

    The underlying simplicial set of $S[1] bowtie X$ is not in general
    isomorphic to $S[1] times X$, but their topological realisations are
    homeomorphic via the map
    $
      #aligned-rows(
        ($|S[1] bowtie X|$, $-> |S[1] times X|$),
        ($((t_n^0, x), (x_0, dots, x_n))$, $|-> ((*, x), (x_0, dots, x_n))$),
        (
          $((t_n^j, x), (x_0, dots, x_n))$,
          $|-> ((macron(s)_(j-1) sigma, x),
            (x_(n-j+1), dots, x_n, x_0, dots, x_(n-j)))$,
        ),
        ($$, $quad quad 1 <= j <= n.$),
      )
    $

    Thus for example $|S[1] bowtie S[1]|$ is the triangulation in which the
    torus is cut into two triangles using the trailing diagonal instead of the
    leading diagonal in $|S[1] times S[1]|$.
  ]
]

#source(100)If $X$ is a cyclic set, then there is an evaluation map
$
  S[1] bowtie X & -> X \
     (t_n^j, x) & |-> t_n^j x
$
which gives rise to a map of topological realisations $S^1 times |X| -> |X|$. In
case $X = S[1]$, this map $S^1 times S^1 -> S^1$ is the multiplication map which
makes $S^1$ a group. Note that with the normal triangulation of $S^1 times S^1$
coming from the simplicial product, multiplication does not correspond to a
simplicial map.

Now there is an obvious identification between $(S[1] bowtie S[1]) bowtie X$ and
$S[1] bowtie (S[1] bowtie X)$ whose topological realisation shows that the above
map $S^1 times |X| -> |X|$ gives an action of the group $S^1$ on $|X|$. It
follows that topological realisation is a functor from cyclic sets to spaces
with $S^1$-action.

It is not hard to check that the functors we have just described are adjoint
functors between topological spaces with $S^1$-action and cyclic sets
$
  Map_(S^1) (|X|, Y) limits(tilde.equiv)^"nat"
  Hom_(bold("CyclSet")) (X, Sing(Y)).
$

#remark(kind: "Warning")[
  Let $X$ be a Kan complex. While the map
  $ abs(Hom(S[1], X)) -> Map(S^1, X) = L X $
  is a homotopy equivalence and commutes with the $S^1$-action, it does not
  necessarily have a homotopy inverse as a map of spaces with $S^1$-action. For
  a discussion related to this point, see Section~@sec:equivariant-homotopy.
]

We now define the cyclic homology $H C_* (X; R)$ of a cyclic set $X$. We write
down the following double complex:
$ #cyclic-set-bicomplex $
Here, $R X_n$ denotes the free $R$-module on $X_n$, with
$
  epsilon = 1 - (-1)^n t_n, quad N = sum_(j=0)^n ((-1)^n t_n)^j, quad
  b = sum_(i=0)^n (-1)^i d_i, quad b' = sum_(i=0)^(n-1) (-1)^i d_i.
$
Just as in Section~@sec:cyclic-homology, we have $b epsilon = epsilon b'$ and
$b' N = N b$, so that this is a double complex. We write $C C_* (X; R)$ for the
total complex of the above double complex, and $H C_* (X; R)$ for its homology.
Since $H_* (X; R)$ is the homology of the first column, and the second column is
contractible with contracting #source(101)homotopy $(-1)^n s_n$, we obtain by
the same argument as in Section~@sec:cyclic-homology a long exact sequence
$
  dots.c -> H_n (X; R) limits(->)^I H C_n (X; R) limits(->)^S
  H C_(n-2) (X; R) limits(->)^B H_(n-1) (X; R) limits(->)^I dots.c
$

Again we set
$ B = (-1)^n epsilon s_n N : R X_n -> R X_(n+1) $
and we write $B_* (X; R)$ for the total complex of the following double complex
$ #cyclic-set-b-bicomplex $
so that we have a homology equivalence $B_* (X; R) -> C C_* (X; R)$. Again, we
can replace $B_* (X; R)$ by the reduced version $macron(B) (X; R)$ if we wish.

Similarly, starting with the dual complex
$ C C^* (X; R) = Hom_R (C C_* (X; R), R) $
we obtain the cyclic cohomology $H C^* (X; R)$.

#proposition[
  If $X$ is a cyclic set, then there are natural isomorphisms
  + $H C_* (X; R) tilde.equiv Tor_*^(R[B]) (R, C_* (X; R))
    tilde.equiv H_* (E S^1 times_(S^1) |X|; R)$.
  + $H C^* (X; R) tilde.equiv Ext_(R[B])^* (R, C^* (X; R))
    tilde.equiv H^* (E S^1 times_(S^1) |X|; R)$.
] <prop:cyclic-set-homology>

#proof[
  We only prove (i), since (ii) is dual. The first isomorphism follows just as
  in Section~@sec:cyclic-homology from the fact that the double complex defining
  $macron(B)_* (X; R)$ can be thought of as the tensor product over $R[B]$ of
  the complex
  $ dots.c -> R[B] limits(->)^B R[B] limits(->)^B R[B] $
  and the reduced Hochschild complex $C_* (X; R)$.

  For the second isomorphism, we argue as follows (cf.
  Section~@sec:equivariant-cohomology). Given any topological group $G$ whose
  underlying topological space is a CW-complex, $E G$ is also a CW-complex. If
  $G$ acts on a CW-complex $Y$ in such a way that $G times Y -> Y$ is a cellular
  map, then $C_* (Y; R)$ is a module over the algebra $C_* (G; R)$ and
  $C_* (E G times Y; R)$ is a free resolution of $C_* (Y; R)$. We have
  $ C_* (E G times_G Y; R) = R times.o_(C_* (G; R)) C_* (E G times Y; R) $
  and so
  $ H_* (E G times_G Y; R) tilde.equiv Tor_*^(C_* (G; R)) (R, C_* (Y; R)). $
  #source(102)We use this in case $G = S^1$ to deduce that
  $
    H_* (E S^1 times_(S^1) |X|; R)
    tilde.equiv Tor_*^(C_* (S[1]; R)) (R, C_* (X; R)).
  $
  So it remains to identify the action of $C_* (S[1]; R)$ on $C_* (X; R)$ with
  the action of $R[B]$. Namely, using the Eilenberg–Zilber map (see
  Section~@sec:simplicial-sets) we have
  $
    C_* (S[1]; R) times.o C_* (X; R) & limits(->)^tilde.eq
    C_* (S[1] times X; R) && -> C_* (X; R) \
    sigma times.o x & |-> sum_(i=0)^n (-1)^(i n) (macron(s)_i sigma, s_i x)
    && |-> sum_(i=0)^n (-1)^(i n) t_(n+1)^(n+1-i) (s_i x)
  $
  Since we are using the reduced Hochschild complex, it is easy to check that
  the latter is the formula for $(-1)^n B(x)$ in $C_* (X; R)$.
]

#corollary[
  + $H C_* (R G) tilde.equiv H_* (E S^1 times_(S^1) L B G; R)$.
  + $H C^* (R G) tilde.equiv H^* (E S^1 times_(S^1) L B G; R)$.
] <cor:cyclic-group-ring>

#proof[
  Again we only prove (i), since (ii) is dual. We remarked in the discussion of
  Example~2 above that the isomorphism $Hom(S[1], N G) = S G slash G$ of
  Proposition~@prop:free-loops-simplicial is an isomorphism of cyclic sets. Thus
  the cyclic homology of $R G$, which is the cyclic homology of the cyclic set
  $S G slash G$, is equal to the cyclic homology of $Hom(S[1], N G)$. By the
  above proposition, this is equal to
  $
    H_* (E S^1 times_(S^1) abs(Hom(S[1], N G)); R)
    = H_* (E S^1 times_(S^1) L B G).
  $
]
