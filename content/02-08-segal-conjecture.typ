#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-08-segal-conjecture.typ": mackey-composite

== Stable cohomotopy and the Segal conjecture <sec:segal-conjecture>
#idx("Segal conjecture", target: [@sec:segal-conjecture])#idx(
  "conjecture",
  "Segal",
  target: [@sec:segal-conjecture],
)

In Theorem~@th:atiyah-completion, we described the K-theory of a classifying
space of a finite group as the completion of the representation ring with
respect to the augmentation ideal. In this section, we describe another
generalised cohomology theory, namely stable cohomotopy $pi_s^*$#idx(
  "$pi_s^*$",
)#idx("cohomotopy, stable")#idx("stable", "cohomotopy"). Graeme Segal
conjectured that this theory evaluated on $B G$ should bear exactly the same
relation to the Burnside ring as $K^* (B G)$ does to the representation ring;
namely, it should equal the completion of the Burnside ring at the augmentation
ideal. This conjecture was proved by G.~Carlsson [@bib:Carlsson1984].

To explain stable cohomotopy, we first explain the notion of stable maps. If $X$
and $Y$ are finite dimensional pointed CW-complexes, then a map from $X$ to $Y$
gives rise to a map between the suspensions $S X -> S Y$ in an obvious way. This
gives us a well defined map
$ [X; Y] -> [S X; S Y] $
and we define *stable maps*#idx("stable", "map")#idx("map", "stable") (i.e.,
stabilised with respect to suspension) from $X$ to $Y$ to be
$
  {X; Y} = dirlim_m [S^m X; S^m Y].
$
Note that if $alpha, beta : S^m X -> S^m Y$ then we can define the sum
$S(alpha) + S(beta) : S^(m+1) X -> S^(m+1) Y$ by dividing the suspension
coordinate into two halves. Thus ${X; Y}$ has the structure of an abelian group,
and ${X; X}$ has the structure of a ring, with multiplication given by
composition.

#source(69)Now recall from Section~@sec:homotopy-groups that
$ [S^m X; S^m Y] = [X; Omega^m S^m Y] $
so that
$
  {X; Y} = dirlim_m [X; Omega^m S^m Y]
  = [X; dirlim_m Omega^m S^m Y]
$
where again the maps
$Omega^m S^m Y = Map_* (S^m, S^m Y) -> Omega^(m+1) S^(m+1) Y$ are given by
suspension as above. The fact that we may pass the limit sign through the
brackets depends on the fact that $X$ is a finite dimensional complex, and for a
general CW-complex $X$ the second expression is better behaved and so we define
in general
$ {X; Y} = [X; Omega^infinity S^infinity Y] $
where $Omega^infinity S^infinity$#idx("$Omega^infinity S^infinity$") denotes
$dirlim_m
Omega^m S^m$. Composition of maps gives in an obvious way a map
$ {Y; Z} times {X; Y} -> {X; Z}. $

We can now define the *stable homotopy*#idx("stable", "homotopy")#idx(
  "homotopy",
  "stable",
) $pi_*^s$ and *stable cohomotopy* $pi_s^*$ of a space via
$
  pi_r^s (X) = {S^r; X_+}, quad pi_s^r (X) = {X_+; S^r}
  = [X_+; dirlim_m Omega^m S^(r+m)].
$
where $X_+$ denotes $X$ with a disjoint basepoint.

Stable cohomotopy is a generalised cohomology theory. Note that the exactness
axiom fails if we use ordinary cohomotopy $[X; S^r]$ instead of stabilising with
respect to suspension. Also note that the space $dirlim_m
Omega^m S^(r+m)$ makes sense for $r$ negative as well as positive. More
generally, for any space $Y$, the functors
$ h_Y^r : X |-> {X; S^r Y} $
form a generalised cohomology theory. Note that it is easy to see that
$
  Omega^infinity S^infinity (S^r Y)
  = Omega(Omega^infinity S^infinity (S^(r+1) Y)).
$

Now the transfer map (Section~@sec:transfer) gives us some elements of
$pi_s^0 (B G)$, for $G$ a finite group. Namely, if $H$ is a subgroup of $G$,
then there is a finite covering map $B H -> B G$. Regarding ${-; B H_+}$ as a
generalised cohomology theory, we have a transfer map
$ {B H_+; B H_+} -> {B G_+; B H_+}. $
The image of the identity element under this map is a stable map from $B G_+$ to
$B H_+$ (i.e., a map $Tr_(H, G) : B G_+ -> Omega^infinity S^infinity B H_+$)
which is also called the transfer#idx("transfer", "as stable map"). Composing
with the element of ${B H_+; S^0}$ given by identifying $B H$ to a point, we
obtain an element of $pi_s^0 (B G)$ corresponding to $H$. This element only
depends on the conjugacy class of $H$ as a subgroup of $G$, and #source(70)so
this way we obtain a map from the Burnside ring#idx("Burnside ring") $b(G)$#idx(
  "$b(G)$",
) (see Section~5.4 of Volume~I) to stable cohomotopy
$ b(G) -> pi_s^0 (B G). $
The Segal conjecture says that the above map induces an isomorphism between the
completion $b(G)^and$ and $pi_s^0 (B G)$. The completion is taken with respect
to the kernel $I_G$ of the augmentation map $b(G) -> ZZ$ sending a permutation
representation to the number of points being permuted,
$ b(G)^and = invlim_n b(G) slash I_G^n. $

As in the case of K-theory (Theorem~@th:atiyah-completion), the Segal conjecture
also contains information about $pi_s^n (B G)$ for $n != 0$. In case $G = 1$,
the groups $pi_s^n ("point") = pi_(-n)^s ("point")$ are the stable homotopy
groups of spheres for $n$ negative (the calculation of which is still an open
problem), and zero for $n$ positive. In general, Segal's conjecture includes the
statement that $pi_s^n (B G) = 0$ for $n$ positive. There is no trivial reason
why this should be true, as there is (Hurewicz theorem) in case $G = 1$.

#theorem(title: [Segal conjecture; Carlsson])[
  The transfer maps described above induce an isomorphism
  $ b(G)^and -> pi_s^0 (B G). $
  Furthermore, for $n > 0$, $pi_s^n (B G) = 0$.
] <th:segal-conjecture>

#proof[
  The proof depends on developing an equivariant version of stable cohomotopy
  theory, and is beyond the scope of this book. For details see Carlsson
  [@bib:Carlsson1984].
]

It has been pointed out by Adams [@bib:Adams1982] (this is developed in detail
in Lewis, May and McClure [@bib:Lewis1982]) that as a consequence of the Segal
conjecture, one knows all the stable maps between $B G'$ and $B G$ for finite
groups $G'$ and $G$. If $H'$ is a subgroup of $G'$ and $phi.alt : H' -> G$ is a
group homomorphism, then the composite of $B phi.alt in {B H'_+; B G_+}$ and
$Tr_(H', G') in {B G'_+; B H'_+}$ gives us an element of ${B G'_+; B G_+}$ which
we write as $zeta_(H', phi.alt)$#idx("$zeta_(H', phi.alt)$").

If $zeta_(H', phi.alt) in {B G'_+; B G_+}$ and
$zeta_(H'', phi.alt') in {B G''_+; B G'_+}$ are such maps, then we can calculate
the composite
$zeta_(H', phi.alt) compose zeta_(H'', phi.alt') in {B G''_+; B G_+}$ by using
the Mackey decomposition theorem as follows. Factor $phi.alt' : H'' -> G'$ as a
surjection $H'' -> K'$ followed by an inclusion $i' : K' arrow.r.hook G'$. Then
the Mackey formula enables us to express the composite of the stable maps
$ B K' limits(arrow.r.long)^(B(i')) B G' limits(arrow.r.long)^Tr B H' $
as a sum of stable maps
$
  B K' limits(arrow.r.long)^Tr B(K' inter lconj(x, H'))
  limits(arrow.r.long)^(c_(x^(-1))) B(lconj(x^(-1), K') inter H')
  limits(arrow.r.long)^(B(i')) B H'
$
#source(71)where $x$ runs over a set of double coset representatives
$K' backslash G' slash H'$ and $c_(x^(-1))$ denotes conjugation by $x^(-1)$.
Then the composite
$
  B H'' limits(arrow.r.long)^(B(phi.alt')) B K' limits(arrow.r.long)^Tr
  B(K' inter lconj(x, H'))
$
is equal to the composite
$
  B H'' limits(arrow.r.long)^Tr
  B((phi.alt')^(-1) (K' inter lconj(x, H')))
  limits(arrow.r.long)^(B(phi.alt')) B(K' inter lconj(x, H')),
$
and so we have expressed the composite as a sum of basis elements of the given
kind
$
  boxed(
    zeta_(H', phi.alt) compose zeta_(H'', phi.alt')
    = sum_(x in K' backslash G' slash H')
    zeta_((phi.alt')^(-1) (K' inter lconj(x, H')),
    phi.alt compose i' compose c_(x^(-1)) compose phi.alt').
  )
$
This formula for the composite is illustrated in the following diagram:
$ #mackey-composite $

Denote by $b(G', G)$#idx("$b(G', G)$") the free abelian group whose basis
elements are labelled $zeta_(H', phi.alt)$, one for each conjugacy class of
pairs $(H', phi.alt)$, where $H'$ is a subgroup of $G'$ and $phi.alt : H' -> G$.
Then the above formula for multiplying basis elements gives a bilinear map
$ b(G', G) times b(G'', G') -> b(G'', G). $
This makes $b(G, G)$ into a ring, which may be thought of as a non-commutative
analogue of the Burnside ring $b(G)$. This multiplication also makes $b(G', G)$
into a $b(G, G)$-$b(G', G')$-bimodule. We have a map
$ b(G', G) -> {B G'_+; B G_+} $
sending the basis element $zeta_(H', phi.alt)$ to the corresponding stable map.
We wish to state that this is an isomorphism after completing $b(G', G)$ with
respect to a suitable filtration.

Before describing this completion, we give another interpretation of $b(G', G)$
and the above map. Namely, $b(G', G)$ is the abelian group with generators the
finite $G' times G$-sets which are free on restriction to $G$ (i.e., to
$1 times G$); and relations $[X] + [Y] = [X dot(union) Y]$. The basis element
$zeta_(H', phi.alt)$ described above corresponds to the transitive permutation
representation of $G' times G$ on the cosets of
$
  Delta_(H', phi.alt) = {(h', phi.alt(h')), h' in H'} subset.eq G' times G.
$
#idx("$Delta_(H', phi.alt)$")Clearly every finite $G$-free $G' times G$-set can
be written as a disjoint union of such transitive $G' times G$-sets in an
essentially unique way.

#source(72)If $X$ is a finite $G$-free $G' times G$-set, then the corresponding
stable map from $B G'_+$ to $B G_+$ can be described as follows. The space
$E G' times_(G') X$ admits a free $G$-action, and so the covering map
$E G' times_(G') X -> E G' times_(G') X slash G$ is a principal $G$-bundle. Thus
(Theorem~@th:milnor-universal) there is a corresponding map
$E G' times_(G') X slash G -> B G$, well defined up to homotopy. The stable map
from $B G'_+$ to $B G_+$ corresponding to $X$ is the transfer for the finite
covering $E G' times_(G') X slash G -> B G'$ (and send the disjoint basepoint in
$B G'_+$ to the disjoint basepoint in $(E G' times_(G') X slash G)_+$) followed
by the above map $(E G' times_(G') X slash G)_+ -> B G_+$.

We make $b(G', G)$ into a $b(G')$-module as follows. If $X$ is a finite $G$-free
$G' times G$-set and $Y$ is a finite $G'$-set, then $Y times X$ is a
$G' times G' times G$-set, and we restrict to the diagonal copy of $G' times G$
to get a finite $G$-free $G' times G$-set. We write $b(G', G)^and$ for the
completion of $b(G', G)$ at the augmentation ideal $I_(G')$ of $b(G')$; namely
$ b(G', G)^and = invlim_n b(G', G) slash I_(G')^n.b(G', G). $

#theorem(title: [Lewis, May, McClure [@bib:Lewis1982]], closed: true)[
  The map
  $ b(G', G) -> {B G'_+; B G_+} $
  described above induces an isomorphism between $b(G', G)^and$ and
  ${B G'_+; B G_+}$.
] <th:lewis-may-mcclure>

Finally, we point out that as a consequence of this theorem, stable splittings
of $B G_+$ as a wedge sum correspond to decompositions of the identity in
$b(G, G)^and$ as a sum of primitive orthogonal idempotents. This subject is
pursued further in Martino and Priddy [@bib:Martino1992a] and Benson and
Feshbach [@bib:Benson1992d].
