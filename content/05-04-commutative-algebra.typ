#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-04-commutative-algebra.typ": projective-quotient

== Varieties and commutative algebra <sec:commutative-algebra>

In preparation for the theory of varieties for modules, we include here a brief
summary of the commutative algebra#idx("commutative", "algebra")#idx(
  "algebra",
  "commutative",
) and algebraic geometry#idx("algebraic", "geometry")#idx(
  "geometry, algebraic",
) we shall need.

Suppose $A$ is a commutative ring, finitely generated over an algebraically
closed field $k$. Then $A$ has the form $k[x_1, dots, x_n] slash I_A$ for some
ideal $I_A$ in a polynomial ring $k[x_1, dots, x_n]$. We wish to investigate the
prime ideals of $A$. In order to do this, we should try to understand the prime
ideals in $k[x_1, dots, x_n]$, and then see which ones contain $I_A$.

We start by describing the maximal ideals#idx("ideal", "maximal"). We regard
$k[x_1, dots, x_n]$ as the polynomial functions#idx(
  "polynomial",
  "functions",
)#idx("function", "polynomial") on an $n$-dimensional space $AA^n (k)$#idx(
  "$AA^n (k)$",
). This is really an affine space#idx(
  "affine",
  "space",
)#idx("space", "affine") rather than a vector space, since if
$(lambda_1, dots, lambda_n)$ is a point in this space, we can just as well
regard $k[x_1, dots, x_n]$ as $k[x_1 - lambda_1, dots, x_n - lambda_n]$; from
this new point of view, this point becomes the origin.

Each point $(lambda_1, dots, lambda_n) in AA^n (k)$ determines a ring
homomorphism
$
  k[x_1, dots, x_n] & -> k \
                x_i & |-> lambda_i,
$
namely evaluation of the polynomial function at the point. The kernel is a
maximal ideal in $k[x_1, dots, x_n]$. Since polynomial functions separate points
in $AA^n (k)$, distinct points give rise to distinct maximal ideals.

#lemma(title: [Weak Nullstellensatz])[
  #source(174)Every maximal ideal in the polynomial ring#idx(
    "polynomial",
    "ring",
  )#idx("ring", "polynomial") $k[x_1, dots, x_n]$ is determined by a point
  $(lambda_1, dots, lambda_n)$ in $AA^n (k)$ in the above way.
] <lem:weak-nullstellensatz>
#idx("Nullstellensatz", "weak", target: [@lem:weak-nullstellensatz])#idx(
  "weak",
  "Nullstellensatz",
  target: [@lem:weak-nullstellensatz],
)

#proof[
  We shall prove by induction on $n$, that even if $k$ is not algebraically
  closed, if $cal(M)$ is a maximal ideal in $k[x_1, dots, x_n]$ then in the
  field $K = k[x_1, dots, x_n] slash cal(M)$ the $x_i$ are algebraic over $k$.
  In the algebraically closed case, this forces the $x_i$ to be in $k$, proving
  the lemma.

  Since $k[x_1]$ is not a field ($x_1$ has no inverse), the statement is clear
  for $n = 1$. If $n > 1$ and (say) $x_1$ is transcendental over $k$, then
  $k(x_1)$ is a subfield of $K$, and by induction $x_2, dots, x_n$ are algebraic
  over $k(x_1)$. So there exists a polynomial $p(x_1)$ such that
  $p(x_1)x_2, dots, p(x_1)x_n$ are integral over $k[x_1]$. So given any element
  $f(x_1, dots, x_n) in K$, for some $r > 0$ the element
  $p(x_1)^r f(x_1, dots, x_n)$ is integral over $k[x_1]$. Since $k[x_1]$ is
  integrally closed in $k(x_1)$, this means that if
  $f(x_1, dots, x_n) in k(x_1)$ then $p(x_1)^r f(x_1, dots, x_n) in k[x_1]$, so
  that $f(x_1, dots, x_n)$ has the form $q(x_1) slash p(x_1)^r$. But $p(x_1)$ is
  independent of the element of $k(x_1)$ chosen, which is absurd because there
  are infinitely many irreducible polynomials in $k[x_1]$.
]

The above lemma is a special case of the following theorem.

#theorem(title: [Hilbert's Nullstellensatz])[
  If $I$ is an ideal in the polynomial ring $k[x_1, dots, x_n]$, we set
  $ V(I) = {v in AA^n (k) | f(v) = 0 forall f in I}. $
  #idx("$V(I)$")If $f in k[x_1, dots, x_n]$ with $f(v) = 0$ for all $v in V(I)$,
  then for some $r > 0$ we have $f^r in I$.
] <th:nullstellensatz>
#idx("Hilbert's Nullstellensatz", target: [@th:nullstellensatz])#idx(
  "Nullstellensatz",
  "Hilbert's",
  target: [@th:nullstellensatz],
)

#proof[
  Suppose $I = (f_1, dots, f_s)$, and suppose $f(v) = 0$ for all $v in V(I)$.
  Let $t$ be a new indeterminate. Then the polynomials
  $f_1, dots, f_s, 1 - f . t$ have no common zero in $AA^(n+1) (k)$. So by the
  weak Nullstellensatz the ideal they generate is not contained in any maximal
  ideal, so it is the whole ring $k[x_1, dots, x_n, t]$. So there are
  polynomials $g_1, dots, g_s, g in k[x_1, dots, x_n, t]$ with
  $ f_1 . g_1 + dots.c + f_s . g_s + (1 - f . t)g = 1. $
  Substituting $t = 1 slash f$ and clearing denominators, we obtain polynomials
  $h_1, dots, h_s$ in $k[x_1, dots, x_n]$ with
  $ f_1 . h_1 + dots.c + f_s . h_s = f^r, $
  as required.
]

The effect this has is the following. If $I$ is an ideal in $k[x_1, dots, x_n]$,
we define the *radical*#idx("radical") of $I$ to be
$
  sqrt(I) = {f in k[x_1, dots, x_n] | "for some" r > 0, space f^r in I}.
$
#idx("$sqrt(I)$")A *radical ideal*#idx("radical", "ideal")#idx(
  "ideal",
  "radical",
) is one with $I = sqrt(I)$. Certainly $V(I) = V(sqrt(I))$, and Hilbert's
Nullstellensatz says that $f in sqrt(I)$ if and only if $f(v) = 0$ for all
$v in V(sqrt(I))$.

#corollary(closed: true)[
  #source(175)There is a one–one inclusion reversing correspondence between sets
  in $AA^n (k)$ of the form $V(I)$ for some $I$ (simultaneous sets of zeroes of
  some polynomials), and radical ideals $I = sqrt(I)$.
] <cor:radical-correspondence>

The sets $V(I)$ form the closed sets of a topology on $AA^n (k)$ called the
*Zariski topology*#idx("Zariski topology")#idx("topology", "Zariski"). This is
because
$
  V(I_1 . I_2) = V(I_1) union V(I_2), quad
  V(sum_alpha I_alpha) = inter.big_alpha V(I_alpha)
$
so that a finite union or arbitrary intersection of closed sets is closed#idx(
  "closed set",
). Note that this topology is very badly separated. For example, every non-empty
open set is dense, so that in particular the space is not Hausdorff.

A closed set $V$ in the Zariski topology is said to be *irreducible* if whenever
we write $V = V_1 union V_2$ as a union of two closed sets then either $V = V_1$
or $V = V_2$. This is equivalent to the corresponding ideal being _prime_#idx(
  "prime ideal",
)#idx("ideal", "prime"). Since $k[x_1, dots, x_n]$ is Noetherian, every closed
set is a finite union of irreducible closed sets#idx("irreducible closed set").

Now we go back to the situation of a general commutative ring $A$, finitely
generated over $k$. If we write $A = k[x_1, dots, x_n] slash I_A$, then the
maximal ideals in $A$ are in one–one correspondence with the maximal ideals in
$k[x_1, dots, x_n]$ containing $I_A$, and hence with the points of $V(I_A)$. We
thus write
$ max(A) = V(I_A) subset.eq AA^n (k) $
for the set of maximal ideals of $A$. It inherits the Zariski topology from
$AA^n (k)$. Namely, radical ideals in $A$ correspond to radical ideals in
$k[x_1, dots, x_n]$ containing $I_A$, and hence to closed subsets of $V(I_A)$.
We thus make the following definition.

#definition[
  Suppose that $A$ is a commutative ring, finitely generated over an
  algebraically closed field $k$. Denote by $max(A)$#idx("$max(A)$") the set of
  maximal ideals of $A$. If $I$ is an ideal in $A$, we set
  $V(I) subset.eq max(A)$ to be the set of maximal ideals containing $I$. The
  *Zariski topology* on $max(A)$ is the topology whose closed sets are of the
  form $V(I)$, for some ideal $I$. The set $max(A)$ with this topology is called
  the *maximal ideal spectrum*#idx("maximal", "ideal spectrum")#idx(
    "spectrum",
    "maximal ideal",
  ) of $A$. An object of this form is called an *affine variety*#idx(
    "affine",
    "variety",
  )#idx("variety", "affine").
] <def:maximal-ideal-spectrum>

Giving a presentation $A = k[x_1, dots, x_n] slash I_A$ corresponds to giving an
embedding of the "abstract" affine variety $max(A)$ as a closed set in
$AA^n (k)$.

We regard elements $a in A$ as "polynomial functions"#idx(
  "polynomial",
  "functions",
)#idx("function", "polynomial") on $max(A)$ as follows. If $alpha in max(A)$
corresponds to a ring homomorphism $phi.alt_alpha : A -> k$, we set
$a(alpha) = phi.alt_alpha (a)$. Hilbert's Nullstellensatz tells us that the
elements giving the zero function are precisely the nilpotent elements in $A$.

If $phi.alt : A -> B$ is a homomorphism of commutative rings (both finitely
generated over $k$), then we have a map of affine varieties
$ phi.alt^* : max(B) -> max(A) $
#source(176)given as follows. If $alpha in max(B)$ corresponds to
$phi.alt_alpha : B -> k$ then $phi.alt^* (alpha) in max(A)$ corresponds to
$phi.alt_alpha compose phi.alt : A -> k$.

#remark[
  For more general commutative rings (not necessarily finitely generated over an
  algebraically closed field), it is not true that the inverse image of a
  maximal ideal under a ring homomorphism is again a maximal ideal. However, the
  inverse image of a prime ideal is always prime, and so we define
  $spec(A)$#idx("$\"spec\"(A)$") to be the set of prime ideals of $A$. If $I$ is
  an ideal in $A$, then $V(I)$ is the set of prime ideals containing $I$. These
  form the closed sets of the Zariski topology on $spec(A)$. The set $spec(A)$
  with this topology is called the *prime ideal spectrum*#idx(
    "prime ideal",
    "spectrum",
  )#idx(
    "spectrum",
    "prime ideal",
  ) of $A$. Notice that $max(A)$ can be recovered as the set of closed points in
  $spec(A)$. The remaining points should be thought of as "generic points"#idx(
    "generic points",
  )#idx("point, generic") of irreducible subvarieties of $max(A)$.

  Since all the rings we wish to consider are finitely generated over
  algebraically closed fields, we shall always use $max(A)$ rather than
  $spec(A)$.
]

#subhead[Graded rings and projective varieties]#idx("graded", "ring")#idx(
  "ring",
  "graded",
) Now suppose $A$ is a finitely generated commutative graded ring of finite type
over an algebraically closed field $k$,
$ A = plus.o.big_(r gt.eq 0) A_r $
with each $A_r$ finite dimensional over $k$. Then $A_0$ is a finite dimensional
commutative $k$-algebra, and hence is a finite sum of local rings whose residue
field is $k$. The corresponding idempotents split $A$ as a direct sum of graded
rings, so we may as well suppose $A_0$ is a local ring. Since nilpotent elements
do not affect the maximal (or prime) ideal spectrum, we may thus assume
$A_0 = k$. Thus $A = k[x_1, dots, x_n] slash I_A$, where say
$deg(x_i) = n_i > 0$ and $I_A$ is a *homogeneous ideal*;#idx(
  "homogeneous",
  "ideal",
)#idx("ideal", "homogeneous") namely if $a = sum a_j in I_A$ with $deg(a_j) = j$
then each $a_j in I_A$. Note that $k[x_1, dots, x_n] slash I$ inherits a grading
from $k[x_1, dots, x_n]$ if and only if $I$ is homogeneous.

Thus $A$ has a distinguished maximal ideal $A^+$, consisting of the elements of
positive degree in $A$. We regard this as the origin in $max(A)$. If
$lambda in k$ is a scalar, we define "dilation#idx("dilation") by $lambda$" as
an operation on $max(A)$ as follows. We have a ring homomorphism
$m_lambda : A -> A$ which multiplies an element of degree $r$ by $lambda^r$. The
map $m_lambda^* : max(A) -> max(A)$ is dilation by $lambda$. If $alpha$ is not
the origin, then the set of dilations $lambda alpha$ of $alpha$, $lambda in k$,
forms a subvariety which should be thought of as the line through the origin,
containing $alpha$. The corresponding ideal in $A$ is the largest homogeneous
ideal contained in the maximal ideal $alpha$.

#exercise[
  Show that an ideal $I$ of $A$ is homogeneous if and only if the dilation by
  $lambda$ of an element of $I$ is in $I$ for all $lambda in k$.
]

If we regard $max(A)$ as a closed subset of $AA^n (k)$ via the presentation
$ A = k[x_1, dots, x_n] slash I_A $
#source(177)with $I_A$ homogeneous as above, then $max(A)$ is a union of lines
through the origin in $AA^n (k)$, i.e., a "homogeneous" closed set. So if $A$ is
a graded ring as above, we say $max(A)$ is a *homogeneous affine variety*#idx(
  "homogeneous",
  "affine variety",
)#idx(
  "affine",
  "variety",
  "homogeneous",
)#idx("variety", "homogeneous affine").

In this situation, it is sometimes better to think in terms of projective
varieties. The points in $proj(A)$#idx("$\"proj\"(A)$") are the lines through
the origin in $max(A)$; namely the maximal homogeneous ideals of $A$ (properly
contained in $A^+$). If $I$ is a homogeneous ideal in $A$, we write
$macron(V)(I)$#idx("$macron(V)(I)$") for the subset of $proj(A)$ consisting of
the maximal homogeneous ideals containing $I$. These form the closed sets of the
Zariski topology on $proj(A)$. A set of the form $proj(A)$ with this topology is
called a *projective variety*#idx(
  "projective",
  "variety",
)#idx("variety", "projective"). The projective variety $proj k[x_1, dots, x_n]$
is written $PP^(n-1) (k)$#idx("$PP^(n-1) (k)$") and is called
$(n - 1)$-dimensional *projective space*#idx(
  "projective",
  "space",
)#idx("space", "projective"). There are obvious maps
$max(A) without {0} ->> proj(A)$ and $AA^n (k) without {0} ->> PP^(n-1) (k)$
making the following diagram commute.
$ #projective-quotient $

The most general sort of variety we shall consider is a *quasiprojective
variety*#idx("quasiprojective variety")#idx("variety", "quasiprojective"),
namely an open subset of a projective variety, with the inherited topology. For
example, $AA^(n-1) (k)$ is the open subset of $PP^(n-1) (k)$ complementing the
closed set $x_n = 0$. Thus every affine variety is also a quasiprojective
variety, as also is every projective variety.

One can think of quasiprojective varieties, and also of open subsets in affine
varieties, in terms of localisation#idx("localisation"). If $I = (f)$ is a
principal ideal in $A$, then the set $S$ of powers of $f$ is closed under
multiplication.#ed-note[The book takes for $S$ the set of elements which are not
  zero divisors modulo an arbitrary ideal $I$. Then the maximal ideals of
  $A[S^(-1)]$ are those of $A$ consisting of zero divisors modulo $I$: for
  $A = k[x]$ and $I = (x)$ only $(x)$ remains. For a non-principal ideal the
  open set $max(A) without V(I)$ is in general not affine (the plane minus a
  point); Section~@sec:quillen-stratification needs only the principal case. See
  Eisenbud [@bib:Eisenbud1995, pp.~57–59 and Proposition 2.2].] So we can form
the localisation $A[S^(-1)]$ whose elements are formal quotients $a slash s$
($a in A$, $s in S$) with $a slash s = a' slash s'$ if and only if for some
$s'' in S$ we have $s''(s' a - s a') = 0$. The maximal ideals of $A[S^(-1)]$
correspond to the maximal ideals of $A$ not containing $I$, and so
$ max(A[S^(-1)]) = max(A) without V(I). $
Similarly if $A$ is graded and $f$ is homogeneous, then $A[S^(-1)]$ is graded
(in positive and negative degrees), and letting $proj(A[S^(-1)])$ be the
spectrum of homogeneous ideals we have
$ proj(A[S^(-1)]) = proj(A) without macron(V)(I). $
Note that $proj(A[S^(-1)])$ is a quasiprojective, not a projective variety.

#subhead[Dimension]#idx("dimension") There are many different concepts of
dimensions of rings; for an extensive discussion of this topic see McConnell and
Robson [@bib:McConnell1988], Part~II. In the case of a finitely generated
commutative ring over a field, all these definitions agree. The following lemma
is the starting point of our discussion of dimension.

#lemma(title: [Noether Normalisation Lemma])[
  #source(178)Suppose that $k$ is a field and $A$ is a finitely generated
  commutative algebra over $k$. Then there exist elements $y_1, dots, y_n in A$
  generating a polynomial subalgebra $k[y_1, dots, y_n] subset.eq A$ over which
  $A$ is finitely generated as a module.

  If $A$ is graded then $y_1, dots, y_n$ may be chosen to be homogeneous
  elements.
] <lem:noether-normalisation>
#idx("Noether normalisation lemma", target: [@lem:noether-normalisation])#idx(
  "lemma",
  "Noether normalisation",
  target: [@lem:noether-normalisation],
)

#proof[
  See Matsumura [@bib:Matsumura1969] (14G).
]

The integer $n$ in the above lemma is called the *dimension* of $A$. If $A$ is
an integral domain#idx("integral domain")#idx("domain, integral"), this is the
same as the transcendence degree#idx("transcendence degree")#idx(
  "degree, transcendence",
) of the field of fractions of $A$ as an extension of $k$.

If $A_*$ is a finitely generated graded ring of finite type over $k$ then
$y_1, dots, y_n$ may be chosen to be homogeneous of positive degree, so that the
rate of growth is
$ gamma(A_*) = gamma(k[y_1, dots, y_n]) = n. $
Thus the above definition of dimension agrees with the definition of Krull
dimension given in the last section.

The usual definition of the Krull dimension#idx("Krull dimension")#idx(
  "dimension",
  "Krull",
) of a ring is as follows. If there is a chain of prime ideals of length $n$
$
  frak(p)_0 supset frak(p)_1 supset dots.c supset frak(p)_n
$
in $A$ but none of length $n + 1$, then the Krull dimension of $A$ is $n$. If
there are arbitrarily long chains of prime ideals, $A$ has infinite Krull
dimension. In case $A$ is a finitely generated commutative ring over a field
$k$, the Krull dimension is equal to the dimension as defined above. This is
proved in Matsumura [@bib:Matsumura1969] Chapter~5 §14. In summary, we have the
following theorem:

#theorem(closed: true)[
  If $A$ is a finitely generated commutative ring over a field $k$, then the
  Krull dimension $dim(A)$ (defined in terms of chains of prime ideals) is equal
  to the integer $n$ given in the Noether normalisation lemma. We also have the
  following:
  + If $A$ is an integral domain then $dim(A)$ is equal to the transcendence
    degree of the field of fractions of $A$.
  + If $A_*$ is a finitely generated commutative graded ring of finite type over
    $k$ then $dim(A_*) = gamma(A_*)$.
] <th:krull-dimension>

#subhead[Finite maps] Suppose $phi.alt : A -> B$ is a map of finitely generated
commutative algebras over $k$. We say
$ phi.alt^* : max(B) -> max(A) $
is a *finite map*#idx("finite", "map")#idx("map", "finite") if $B$ is finitely
generated as a module over the image of $phi.alt$ (or equivalently $B$ is
integral over the image of $phi.alt$). If $phi.alt^*$ is finite, then every
point in $max(A)$ has only finitely many inverse images in $max(B)$. To see
this, let $B = k[x_1, dots, x_n] slash I_B$ so that $max(B) subset.eq AA^n (k)$.
Then each $x_j$ satisfies an equation of the form
$x_j^m + phi.alt(a_(m-1))x_j^(m-1) + dots.c + phi.alt(a_0) = 0$ with $a_i in A$.
So on the pre-image of a point in $max(A)$, the coordinate $x_j$ can take on
only finitely many values.

#source(179)We say $phi.alt^*$ is a *dominant map*#idx("dominant map")#idx(
  "map",
  "dominant",
) if the kernel of $phi.alt$ is a nilpotent ideal in $A$. In general a dominant
map of varieties is not necessarily surjective, but its image contains a dense
open subset. However, a finite dominant map is always surjective because of the
following theorem:

#theorem[
  Let $A subset B$ be commutative rings with $B$ integral over $A$, and let
  $frak(p)$ be a prime ideal of $A$. Then there exists a prime ideal $frak(p)'$
  of $B$ such that $frak(p)' inter A = frak(p)$.
] <th:lying-over>

#proof[
  See Atiyah and Macdonald [@bib:Atiyah1969] Theorem~5.10.
]

Thus, for example, we can view the Noether Normalisation Lemma as saying that
any affine variety of dimension $n$ can be expressed as a finite branched cover
of $AA^n (k)$, and any projective variety of dimension $n - 1$ can be expressed
as a finite branched cover of $PP^(n-1) (k)$.

Suppose $A subset.eq B$ are finitely generated commutative algebras over a field
$k$ of characteristic $p$, and suppose there exists some power $p^a$ of $p$ such
that the $p^a$th power of any element of $B$ lies in $A$. Writing $B^([p^a])$
for the subring consisting of $p^a$th powers of elements of $B$, the inclusions
$B^([p^a]) subset.eq A subset.eq B$ give rise to finite dominant maps
$ max(B) -> max(A) -> max(B^([p^a])). $
The composite of these surjective maps is equal to the Frobenius morphism#idx(
  "Frobenius",
  "morphism",
)#idx("morphism", "Frobenius") on $max(B)$, which at the level of the Zariski
topology is a homeomorphism. It follows that the map
$ max(B) -> max(A) $
is also a homeomorphism in the Zariski topology. Such a map is called an
*inseparable isogeny*#idx("inseparable isogeny")#idx("isogeny, inseparable") or
an *F-isomorphism*#idx("F-isomorphism").

Finally, we discuss finite group actions on varieties#idx(
  "group",
  "action on variety",
)#idx("variety", "group action on").

#proposition(title: [Hilbert–Noether])[
  Suppose a finite group $G$ acts as automorphisms on a finitely generated
  commutative $k$-algebra $A$. Then the fixed point subalgebra $A^G$ is a
  finitely generated $k$-algebra over which $A$ is integral. The variety
  $max(A^G)$ is the quotient of $max(A)$ by the action of $G$.
] <prop:hilbert-noether>

#proof[
  If $a$ is an element of $A$, then $a$ satisfies the monic equation
  $product_(g in G) (x - g(a)) = 0$ with coefficients in $A^G$. This proves that
  $A$ is integral over $A^G$. Let $B$ be the subalgebra of $A^G$ generated by
  the coefficients of the monic polynomials satisfied by a finite set of
  $k$-algebra generators of $A$. Then $B$ is a finitely generated commutative
  $k$-algebra, and hence Noetherian. So $A$ is a finitely generated $B$-module,
  and hence so is $A^G$. Thus $A^G$ is a finitely generated $k$-algebra.

  Now the map of varieties
  $ max(A) -> max(A^G) $
  is a finite dominant map, and hence surjective. If $cal(M)$ and $cal(M)'$ are
  maximal ideals in $A$ which are not $G$-conjugate, then there exists an
  element $a in A$ #source(180)with $a in cal(M)$ but $a in.not g(cal(M)')$ for
  all $g in G$. So $product_(g in G) g(a)$ is an element of $A^G$ lying in
  $cal(M)$ but not in $cal(M)'$. It follows that the preimage in $max(A^G)$ is a
  single $G$-orbit of points in $max(A)$.
]

#subhead[Cohen–Macaulay rings] We end this section with a brief review of
Cohen–Macaulay rings and modules. For further details, see Zariski and Samuel
[@bib:Zariski1975], Appendix~6, Matsumura [@bib:Matsumura1969] Chapter~6, and
Serre [@bib:Serre1965b], Chapter~4.

#definition[
  Suppose that $A = plus.o.big_(n gt.eq 0) A_n$ is a finitely generated graded
  (anti-) commutative $k$-algebra, and $M = plus.o.big_(n gt.eq 0) M_n$ is a
  finitely generated graded $A$-module. A sequence $zeta_1, dots, zeta_r$ of
  homogeneous elements of degree $n_1, dots, n_r$ in $A$ is said to be a
  *regular sequence*#idx("regular sequence")#idx("sequence", "regular") for $M$
  if for each $i = 1, dots, r$ the map
  $
    M_n slash M_n inter (zeta_1, dots, zeta_(i-1))M
    -> M_(n+n_i) slash M_(n+n_i) inter (zeta_1, dots, zeta_(i-1))M
  $
  induced by multiplication by $zeta_i$ is injective. Note that we are not
  asking that $M_n slash M_n inter (zeta_1, dots, zeta_(i-1))M$ be non-zero.

  The *depth*#idx("depth") of $M$ is the length of the longest regular sequence.
  $M$ is said to be *Cohen–Macaulay*#idx("Cohen–Macaulay", "ring")#idx(
    "ring",
    "Cohen–Macaulay",
  ) if its depth is equal to its Krull dimension. The ring $A$ is said to be
  Cohen–Macaulay if it is Cohen–Macaulay as a module over itself. This is
  equivalent to the condition that there is a polynomial subring
  $k[zeta_1, dots, zeta_r] subset.eq A$ generated by homogeneous elements
  $zeta_i$, such that $A$ is a finitely generated free module over
  $k[zeta_1, dots, zeta_r]$.
] <def:regular-sequence>

The following theorem is proved in Serre [@bib:Serre1965b], p.~IV–20, Theorem~2;
see also Stanley [@bib:Stanley1979], Proposition~3.1. Actually the proof given
in Serre [@bib:Serre1965b] is for strictly commutative rings, but the proof
carries over verbatim to the graded commutative case.

#theorem[
  Suppose that $A$ is a finitely generated graded commutative $k$-algebra. Then
  the following are equivalent.
  + There exists a polynomial subring $k[zeta_1, dots, zeta_r] subset.eq A$
    generated by homogeneous elements $zeta_i$, such that $A$ is a finitely
    generated free module over $k[zeta_1, dots, zeta_r]$.
  + For every polynomial subring $k[zeta_1, dots, zeta_r] subset.eq A$ generated
    by homogeneous elements $zeta_i$, such that $A$ is finitely generated as a
    module over $k[zeta_1, dots, zeta_r]$ (i.e., $zeta_1, dots, zeta_r$ is a
    homogeneous set of parameters for $A$), $A$ is a free module.
] <th:cohen-macaulay-free>

One can recognise regular sequences in polynomial rings using the following
theorem.

#theorem(title: [Macaulay])[
  Suppose $I = (zeta_1, dots, zeta_r)$ is an ideal in a polynomial ring
  $A = k[x_1, dots, x_n]$. Then $zeta_1, dots, zeta_r$ is a regular sequence for
  $A$ if and only if the Krull dimension of $A slash I$ is equal to $n - r$.
] <th:macaulay>
#idx("Macaulay's theorem", target: [@th:macaulay])#idx(
  "theorem",
  "Macaulay's",
  target: [@th:macaulay],
)

#proof[
  See Zariski and Samuel [@bib:Zariski1975], Appendix~6, Theorem~2.
]

#exercise[
  #source(181)Show that if $A$ and $B$ are commutative rings#idx(
    "tensor product",
    "of commutative rings",
  ), finitely generated over an algebraically closed field $k$, then
  $
    max(A times.o_k B) tilde.equiv max(A) times max(B).
  $
]
