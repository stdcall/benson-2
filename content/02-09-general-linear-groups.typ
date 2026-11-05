#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-09-general-linear-groups.typ": (
  brauer-pullback, fixed-points, homotopy-fibre, homotopy-fixed-points,
  homotopy-lifting, path-addition, reduced-k-theory,
)

== Cohomology of general linear groups <sec:general-linear-groups>

In this section we describe Quillen's calculation [@bib:Quillen1972a] of the
cohomology of general linear groups over a finite field#idx(
  "cohomology",
  "of $GL_n (FF_q)$",
), and in the next section we describe how this led to Quillen's definition of
the algebraic K-groups of a ring (this particular case calculates the algebraic
K-groups of a finite field). In fact, it is possible to calculate the cohomology
of these general linear groups entirely algebraically (Kroll [@bib:Kroll1988]),
but this hides the most striking features of Quillen's calculation.

The idea of Quillen's calculation is to think of the Adams operation $psi^q$,
where $q$ is a power of a prime $p$, as a map from $B U$ to itself, take its
"homotopy fixed points" $F psi^q$#idx("$F psi^q$"), and to show that there is a
map $B GL_n (FF_q) -> F psi^q$#idx("general linear group", "$GL_n (FF_q)$")#idx(
  "$GL_n (FF_q)$",
)#idx("group", "general linear", "$GL_n (FF_q)$") giving interesting cohomology
classes by pulling back, and in the limit inducing a cohomology equivalence
$B GL(FF_q) -> F psi^q$, where $GL(FF_q)$ is the union of the $GL_n (FF_q)$
embedded in each other using the top left hand corner. The details are as
follows.

The first problem is to represent $psi^q$ as a map from $B U$ to itself.
According to Section~@sec:k-theory, for $B$ compact, $psi^q$ is a natural
transformation on $tilde(K)(B)$. We would like to apply Yoneda's lemma (2.1.4 of
Volume~I), and say that #source(73)because $tilde(K)(B)$ is representable as
$[B; B U]$, the natural transformation $psi^q$ is representable by a map
$B U -> B U$. The problem is that $B U$ is not compact. However, it has a CW
decomposition $B U = union.big X^m$ with only cells in even dimension (this
follows from the row echelon form for matrices—see Milnor and Stasheff
[@bib:Milnor1974], Section~6). One can show inductively (using the Bott
periodicity theorem) that on a finite CW-complex which only has cells in even
dimension, the functor $K^(-1)$ vanishes, and so the Milnor exact sequence (see
Theorem~@th:milnor-exact-sequence)
$
  0 -> attach(invlim, tr: 1) K^(-1) (X^m) -> K(B U) -> invlim K(X^m) -> 0
$
reduces to $K(B U) = invlim K(X^m)$. Thus the operations $psi^q$ are defined on
$K(B U)$ and are hence represented by maps $psi^q : B U -> B U$.

We now describe the process of taking homotopy fixed points. This is similar to
the process of taking the homotopy fibre of a map, as described in
Section~@sec:fibrations. If $phi.alt : X -> X$ is a self-map of a space, then
the fixed points $X^phi.alt$ of $phi.alt$ are obtained by taking the pullback
$ #fixed-points $
where $Delta$ is the diagonal map. The *homotopy fixed points*#idx(
  "homotopy",
  "fixed points",
)#idx("fixed point", "homotopy") $X^(h phi.alt)$ are obtained by replacing
$Delta$ by a fibration. Namely, if we denote by
$tilde(Delta) : X^I -> X times X$ the map taking a path to its endpoints, then
$tilde(Delta)$ is a fibration and it is homotopy equivalent to $Delta$ (in other
words, the inclusion of $X$ into $X^I$ as the constant maps is a homotopy
equivalence which when composed with $tilde(Delta)$ gives $Delta$). So we define
the homotopy fixed points of $phi.alt$ to be the pullback
$ #homotopy-fixed-points $
The vertical maps in this diagram are fibrations with fibre $Omega X$. Note that
there is an obvious map $X^phi.alt -> X^(h phi.alt)$.

Now suppose that $X$ has a basepoint $x_0$ and comes with an additive structure;
namely an addition map $X times X -> X$ which is associative and commutative up
to homotopy, and a map $X -> X$ which acts as an additive inverse up to
homotopy. $B U$ is an example of such a space, in which the addition is given by
the limit of the Whitney sum maps
$G^n (CC^infinity) times G^m (CC^infinity) -> G^(n+m) (CC^infinity)$ and
negation is given by the obvious maps $G^n (CC^m) -> G^(m-n) (CC^m)$ (see the
remarks in the second paragraph of Section~@sec:k-theory). Putting these
addition and inverse maps together, we get a subtraction map
$d : X times X -> X$.

#source(74)Denoting by $P X$ the (contractible) path space
$Map_* ((I, 0), (X, x_0))$, we can extend the above pullback diagram to a
diagram
$ #homotopy-fibre $
Here, the map $X^I -> P X$ sends a path $t |-> omega(t)$ to the path
$t |-> d(omega(t), omega(0))$ obtained by shifting the starting point to the
origin. The map $P X -> X$ is the map sending a path $omega$ to its endpoint
$omega(1)$. It follows that $X^(h phi.alt)$ is exactly the homotopy fibre of the
map $1 - phi.alt = d compose (1, phi.alt)$.

We give $X^(h phi.alt)$ an additive structure as follows. Denoting by
$P_(1 - phi.alt)$ the space of ordered pairs $(x, omega)$ consisting of a point
$x$ in $X$ and an unbased map $omega : I -> X$ with
$omega(1) = d(x, phi.alt(x))$ as in Section~@sec:fibrations, we know that
$P_(1 - phi.alt)$ is homotopy equivalent to $X$, and $X^(h phi.alt)$ is the
fibre of the map $P_(1 - phi.alt) -> X$ taking $(x, omega)$ to $omega(0)$. The
addition map on $X$ gives us maps
$ #path-addition $
and hence a map $X^(h phi.alt) times X^(h phi.alt) -> X^(h phi.alt)$. Similarly
the inverse map $X -> X$ gives us an inverse map
$X^(h phi.alt) -> X^(h phi.alt)$. It is easy to check that these maps give an
additive structure on $X^(h phi.alt)$ in the sense described above.

#lemma[
  If $X$ has an additive structure in the sense described above, and $Y$ is a
  space with the property that every map $Y -> Omega X$ is homotopic to the
  constant map, then $[Y; X^(h phi.alt)] = [Y; X]^phi.alt$, where the latter
  denotes the fixed points of composition with $phi.alt$ on $[Y; X]$.
] <lem:homotopy-fixed-points>

#proof[
  A map from $Y$ to $X^(h phi.alt)$ can be thought of as a map $f : Y -> X$ and
  a homotopy from $f$ to $phi.alt compose f$. So composition with
  $X^(h phi.alt) -> X$ gives a surjective map
  $[Y; X^(h phi.alt)] -> [Y; X]^phi.alt$. Both $X$ and $X^(h phi.alt)$ have an
  additive structure, which induce abelian group structures on these sets of
  homotopy classes. It is easy to check that the above map is a homomorphism of
  abelian groups. If $f : Y -> X^(h phi.alt)$ is in the kernel of this
  homomorphism, then by the homotopy lifting property for the fibration
  $X^(h phi.alt) -> X$, $f$ is homotopic to a map whose image lies in the fibre
  $Omega X$ of this fibration.
  $ #homotopy-lifting $
  Since every map $Y -> Omega X$ is homotopic to the constant map by hypothesis,
  the lemma is proved.
]

#source(75)We wish to apply the above lemma in the situation where $X$ is $B U$
and $phi.alt$ is $psi^q$. Following Quillen, we write $F psi^q$ for the homotopy
fixed point set in this case, namely the homotopy fibre of
$1 - psi^q : B U -> B U$.

By Theorem~@th:loop-space-classifying, $Omega B U$ is homotopy equivalent to the
infinite unitary group $U$, namely the union of the finite unitary groups
embedded in each other using the top left hand corner.

If $G$ is a finite group, then we saw in Section~@sec:k-theory that there is a
natural map from the representation ring to K-theory given by using a
representation to form a vector bundle. We compose this with the projection down
to reduced K-theory:
$ #reduced-k-theory $
This map clearly commutes with the operations $psi^q$, which are defined on both
sides, see Section~@sec:k-theory, and Section~5.9 of Volume~I, so that we have a
well defined map $cal(R)(CC G)^(psi^q) -> [B G; B U]^(psi^q)$. The Atiyah
Completion Theorem~@th:atiyah-completion says that the above map induces an
isomorphism $cal(R)(CC G)^and tilde.equiv K^0 (B G)$, where $cal(R)(CC G)^and$
is the completion of $cal(R)(CC G)$ at the augmentation ideal $I_G$. So we also
have an isomorphism $I_G^and tilde.equiv tilde(K)^0 (B G)$. Moreover, this
theorem also states that $[B G; Omega B U] = [B G; U] = K^1 (B G) = 0$. So we
are able to apply the above lemma to see that
$
  [B G; F psi^q] = [B G; B U^(h psi^q)] tilde.equiv [B G; B U]^(psi^q).
$
It follows that there is a well defined map
$ cal(R)(CC G)^(psi^q) -> [B G; F psi^q]. $

Now recall from Section~5.9 of Volume~I that the Brauer lift gives an
isomorphism
$ cal(R)(CC G)^(psi^q) tilde.equiv cal(R)(FF_q G) $
so that we have a well defined map
$ cal(R)(FF_q G) -> [B G; F psi^q]. $
So given any finitely generated $FF_q G$-module, we obtain a map, well defined
up to homotopy, from $B G$ to $F psi^q$. Pulling back elements of cohomology of
$F psi^q$ through this map, we obtain elements of the cohomology of $G$, which
can be thought of as *characteristic classes*#idx(
  "characteristic",
  "classes",
  "for modular representations",
)#idx("modular representations", "characteristic classes for") for modular
representations.

We now calculate the homotopy and cohomology of $F psi^q$. The homotopy is easy,
so we begin with that. Regarding $F psi^q$ as the homotopy fibre of #source(
  76,
)$1 - psi^q : B U -> B U$, we obtain a long exact sequence of homotopy groups
$
  dots.c -> pi_j (B U) limits(arrow.r.long)^(1 - psi^q) pi_j (B U)
  -> pi_(j-1) (F psi^q) \
  -> pi_(j-1) (B U) limits(arrow.r.long)^(1 - psi^q) pi_(j-1) (B U)
  -> dots.c
$
Now for $j > 0$ we saw in Section~@sec:k-theory that
$pi_j (B U) = [S^j; B U] = tilde(K)(S^j)$ is isomorphic to $ZZ$ if $j$ is even
and is zero if $j$ is odd. An explicit calculation on $S^2$ shows that $psi^q$
acts as multiplication by $q$ on $tilde(K)(S^2) tilde.equiv ZZ$ and hence as
multiplication by $q^j$ on $tilde(K)(S^(2j))$ by Bott periodicity. Thus we have
$
  pi_(2j-1) (F psi^q) = ZZ slash (q^j - 1), wide pi_(2j) (F psi^q) = 0.
$
It follows that there is no $p$-torsion in $pi_* (F psi^q)$, and so by the
$p$-local version of the Hurewicz Theorem~@th:local-hurewicz,
$H_i (F psi^q; FF_p) = 0$ for $i > 0$. Similarly, applying this theorem in
characteristic zero, we see that $H_i (F psi^q; QQ) = 0$ for $i > 0$. Note also
that if we examine the above sequence as a long exact sequence of modules for
$pi_1 (F psi^q)$, and we use the fact that $pi_1 (B U) = 0$, we see that
$pi_1 (F psi^q)$ acts trivially on $pi_n (F psi^q)$ for all $n$, so that
$F psi^q$ is a simple space.

We now describe the calculation of the cohomology of $F psi^q$ with coefficients
in $FF_l$, where $l$ is any prime other than $p$. One applies the
Eilenberg–Moore spectral sequence#idx(
  "Eilenberg",
  "–Moore spectral sequence",
)#idx(
  "spectral sequence",
  "Eilenberg–Moore",
) to the pullback square
$ #brauer-pullback $
obtained by regarding $F psi^q$ as a homotopy fixed point set. Look at
Section~@sec:eilenberg-moore for a brief discussion of the Eilenberg–Moore
spectral sequence. In this case, the $E_2$ term is
$
  E_2^(**) = Tor_(H^* (B U times B U))^(**) (H^* (B U), H^* (B U^I))
$
and the spectral sequence converges to $H^* (F psi^q)$ (all cohomology with
$FF_l$ coefficients). As a module over
$
  H^* (B U times B U) = FF_l [c'_1, c'_2, dots, c''_1, c''_2, dots]
$
via the above maps, we have
$
  H^* (B U^I) & = H^* (B U times B U) slash (c'_1 - c''_1, c'_2 - c''_2, dots) \
    H^* (B U) & = H^* (B U times B U) slash
                (q c'_1 - c''_1, q^2 c'_2 - c''_2, dots)
$
Hence
$
  H^* (B U) times.o_(H^* (B U times B U)) H^* (B U^I)
  & = FF_l [c_1, c_2, dots] slash ((q - 1) c_1, (q^2 - 1) c_2, dots) \
  & = FF_l [c_r, c_(2r), dots]
$
where $r$ is the multiplicative order of $q$ modulo $l$, and $c_(j r)$ has
degree $2 j r$.

#source(77)The standard techniques for calculating Tor over a polynomial ring
show that the $E_2$ page is a tensor product of a polynomial and an exterior
algebra
$
  E_2^(**) = FF_l [c_r, c_(2r), dots] times.o Lambda(e_r, e_(2r), dots)
$
where the $c_(j r) in E_2^(0, 2j r)$ and $e_(j r) in E_2^(-1, 2j r)$. Since this
is a second quadrant spectral sequence and the differentials take these
generators into the first quadrant, we have $E_2 = E_infinity$. It follows that
the additive structure of $H^* (F psi^q; FF_l)$#idx(
  "cohomology",
  "of $F psi^q$",
) is the same as $E_2^(**)$, and the multiplicative structure is the same with
the exception that instead of $e_(j r)^2 = 0$ we only know that $e_(j r)^2$ is
in the subring generated by $c_r, c_(2r), dots$.

#remark(kind: "Warning")[
  You may be inclined to guess from the above calculation that
  $
    H^* (F psi^q; ZZ)
    = ZZ[c_1, c_2, dots] slash ((q - 1) c_1, (q^2 - 1) c_2, dots).
  $
  This is easily seen to be false, by noticing that if this were the case, then
  $H^* (F psi^q; ZZ)$ would be concentrated in even degrees, so that the long
  exact sequence
  $
    dots.c -> H^(i-1) (F psi^q; FF_l) -> H^i (F psi^q; ZZ)
    limits(arrow.r.long)^(times l) H^i (F psi^q; ZZ) -> H^i (F psi^q; FF_l)
    -> dots.c
  $
  coming from the short exact sequence of coefficients
  $ 0 -> ZZ -> ZZ -> FF_l -> 0 $
  would reduce to
  $
    0 -> H^(2i-1) (F psi^q; FF_l) -> H^(2i) (F psi^q; ZZ)
    limits(arrow.r.long)^(times l) H^(2i) (F psi^q; ZZ)
    -> H^(2i) (F psi^q; FF_l) -> 0.
  $
  However, we have seen that $H^(2*) (F psi^q; FF_l)$ contains even products of
  the $e_(j r)$'s, which are not in the image of reduction modulo $l$. For
  further information on the integral cohomology of $F psi^q$, see Huebschmann
  [@bib:Huebschmann1987] and Jeandupeux [@bib:Jeandupeux1989].
]

We now complete the determination of the multiplicative structure of the ring
$H^* (F psi^q; FF_l)$ at the same time as calculating $H^* (GL_n (FF_q), FF_l)$,
as follows. The canonical modular representation of dimension $n$ of
$GL_n (FF_q)$ over $FF_q$ gives, via the Brauer lift as above, a map
$ B GL_n (FF_q) -> F psi^q $
#idx("$B GL_n (FF_q)$")well defined up to homotopy. We shall see that the
characteristic classes $c_(j r)$, $e_(j r)$ defined by this map generate
$H^* (GL_n (FF_q), FF_l)$. We do this by restricting to a suitable abelian
subgroup.

Let $C$ denote a cyclic group of order $q^r - 1$, so that $C$ has an irreducible
representation of dimension $r$ over $FF_q$ (via the isomorphism
$C tilde.equiv FF_(q^r)^times$). Thus the direct product $C^m$ of $m$ copies of
$C$ has a faithful representation of dimension $m r$ over $FF_q$, and hence we
have an embedding $C^m arrow.r.hook GL_n (FF_q)$.

#lemma[
  The restriction map
  $ H^* (GL_n (FF_q), FF_l) -> H^* (C^m, FF_l) $
  is injective.
] <lem:restriction-injective>

#proof[
  #source(78)We first treat the case where $l$ is odd. In this case, we
  factorise the embedding of $C^m$ in $GL_n (FF_q)$ as
  $
    C^m arrow.r.hook Sigma_m wreath GL_r (FF_q) arrow.r.hook GL_n (FF_q).
  $
  Using the fact that $l$ is odd, one finds that the index in $GL_n (FF_q)$ of
  this intermediate group is coprime to $l$, so that by Corollary~3.6.18 of
  Volume~I, the restriction map in mod $l$ cohomology is injective. Now a
  theorem of Nakaoka [@bib:Nakaoka1961] (see also the exercise at the end of
  Section~@sec:evens-norm) says that the cohomology of a wreath product
  $Sigma_m wreath A$ is detected on $A^m$ and $Sigma_m times A$. Since the Sylow
  $l$-subgroups of $Sigma_m$ are iterated wreath products of cyclic groups of
  order $l$, it follows that the cohomology of $GL_n (FF_q)$ is detected on
  $l$-subgroups of exponent dividing $q^r - 1$. These are all conjugate to
  subgroups of $C^m$, and so we are done.

  If $l = 2$ (so that $r = 1$ and $m = n$), the index of this wreath product
  need not be odd, so one uses the subgroup
  $Sigma_([n slash 2]) wreath GL_2 (FF_q) times (FF_q^times)^(n - 2[n slash 2])$
  of odd index. A separate calculation is needed to check that the mod 2
  cohomology of $GL_2 (FF_q)$ is detected on abelian 2-subgroups of exponent
  dividing $q - 1$.
]

The calculation is now completed as follows. We have maps
$ B(C^m) -> B GL_n (FF_q) -> F psi^q $
giving rise to maps in cohomology
$
  H^* (F psi^q; FF_l) -> H^* (GL_n (FF_q), FF_l) -> H^* (C^m, FF_l).
$
Now the normaliser of $C$ in $GL_r (FF_q)$ contains a cyclic group of order $r$
acting on $C$ by sending an element to its $q$th power. Thus the image of the
restriction in cohomology from $GL_n (FF_q)$ to $C^m$ lies in the invariants of
$Sigma_m wreath ZZ slash r$, and so we have
$
  H^* (F psi^q; FF_l) -> H^* (GL_n (FF_q), FF_l)
  -> (scripts(times.o.big)^m H^* (C, FF_l)^(ZZ slash r))^(Sigma_m).
$
We have seen in Lemma~@lem:restriction-injective that the second of these maps
is injective. So if we can prove that the composite is surjective, it will
follow that the second map is an isomorphism. An explicit calculation with the
cohomology of $C$ (cf. Section~3.5 of Volume~I) shows that the characteristic
classes $c_r$ and $e_r$ of the $r$ dimensional representation of $C$ over $FF_q$
are non-zero. One then needs formulae for the characteristic classes of a direct
sum of representations; this amounts to calculating the maps in cohomology
determined by the additive structure on $F psi^q$, which can be calculated from
the corresponding formulae for $B U$. Using these formulae it turns out that, if
$l$ is odd, the characteristic classes $c_r, c_(2r), dots, c_(m r)$ and
$e_r, e_(2r), dots, e_(m r)$ of the $n$ dimensional representation of $C^m$ over
$FF_q$ generate the invariants of $Sigma_m wreath ZZ slash r$ on the cohomology
of $C^m$, so that the composite map is surjective, and hence the second map is
an isomorphism.#ed-note[The book states here and in
  Theorem~@th:quillen-cohomology-gl that the second map is an isomorphism for
  every $l$. For $l = 2$ it is not onto: $H^2 (GL_2 (FF_3), FF_2)$ and
  $H^2 (GL_2 (FF_5), FF_2)$ are one-dimensional, spanned by $c_1$, while the
  $Sigma_2$-invariants in $H^2 (C times C, FF_2)$ also contain $x_1 x_2$, where
  $x_1$, $x_2$ are the generators in degree one.] It also follows that we may
evaluate the squares of the $e_(j r)$ with $j lt.eq m$ by restricting to $C^m$.

Now if $l$ is odd then $H^* (C, FF_l)$ has a polynomial generator in degree two
and a generator in degree one squaring to zero (see Section~3.5 of Volume~I). If
$l = 2$ then $r = 1$ and $m = n$, so that $C$ has order $q - 1$. In this case,
if #source(79)$q equiv 1 mod 4$ then $C$ has order divisible by 4, and
$H^* (C, FF_l)$ has the same structure as above. If $q equiv 3 mod 4$ then $C$
is a direct product of a cyclic group of order two and a cyclic group of odd
order, and so $H^* (C, FF_l)$ is a polynomial ring on a single generator in
degree one. Quillen calls the case $l$ odd or $l = 2$ and $q equiv 1 mod 4$ the
_typical case_#idx("typical case"), and the case $l = 2$ and $q equiv 3 mod 4$
the _exceptional case_#idx("exceptional", "case").

Restriction to $C^m$ shows that the classes $e_(j r)$ square to zero in the
typical case, while in the exceptional case we have
$e_(j r)^2 = sum_(a=0)^(j r - 1) c_a c_(2j r - 1 - a)$.

We summarise all this as follows.

#theorem(title: [Quillen [@bib:Quillen1972a]], closed: true)[
  Let $q$ be a prime power, and suppose $l$ is a prime not dividing $q$. Let $r$
  be the multiplicative order of $q$ modulo $l$. Then $H^* (F psi^q; FF_l)$ is
  generated by classes $c_(j r)$ and $e_(j r)$, $j = 1, 2, dots$, with
  $deg(c_(j r)) = 2 j r$ and $deg(e_(j r)) = 2 j r - 1$, subject to relations
  $
    e_(j r)^2 = cases(
      0 & "(typical case)",
      display(sum_(a=0)^(j r - 1) c_a c_(2j r - 1 - a)) & "(exceptional case)",
    )
  $
  where the typical case is $l$ odd or $l = 2$, $q equiv 1 mod 4$, and the
  exceptional case is $l = 2$, $q equiv 3 mod 4$.

  Let $n = m r + e$ with $0 lt.eq e < r$. Let $C$ be a cyclic group of order
  $q^r - 1$. Then we have restriction maps
  $
    H^* (F psi^q; FF_l) -> H^* (GL_n (FF_q), FF_l)
    -> (scripts(times.o.big)^m H^* (C, FF_l)^(ZZ slash r))^(Sigma_m).
  $
  The first of these maps is surjective and the second is injective, and an
  isomorphism if $l$ is odd. The ring $H^* (GL_n (FF_q), FF_l)$ is generated by
  the classes $c_(j r)$ and $e_(j r)$, $1 lt.eq j lt.eq m$ subject to the same
  relations as above.
] <th:quillen-cohomology-gl>

Now embed $GL_n (FF_q)$ in $GL_(n+1) (FF_q)$ as the matrices which agree with
the identity on the last row and column. Then the natural $(n + 1)$ dimensional
module for $GL_(n+1) (FF_q)$ restricts to the direct sum of the natural $n$
dimensional module for $GL_n (FF_q)$ and a one dimensional trivial module. So if
we compose the Brauer lift map $B GL_(n+1) (FF_q) -> F psi^q$ with
$B GL_n (FF_q) -> B GL_(n+1) (FF_q)$, we obtain the Brauer lift map
$B GL_n (FF_q) -> F psi^q$. So letting $GL(FF_q)$ be the union of the
$GL_n (FF_q)$ with these inclusions, there is a map $B GL(FF_q) -> F psi^q$ well
defined up to homotopy. The above theorem implies that this map is a mod $l$
cohomology isomorphism for all primes $l$ not equal to $p$. Moreover, Quillen
shows in [@bib:Quillen1972a] Section~11 that the mod $p$ cohomology of
$B GL_n (FF_q)$ vanishes in positive degrees less than $d(p - 1)$, where $d$ is
defined by $q = p^d$, and that the mod $p$ cohomology of $B GL(FF_q)$ vanishes
in all positive degrees. We also saw that
$H^i (F psi^q; FF_p) = 0 = H^i (F psi^q; QQ)$ for $i > 0$, so the map is a
cohomology equivalence at all primes. Since the cohomology groups are finitely
generated abelian groups, it is easy to see that this implies that
$H^* (F psi^q; ZZ) -> H^* (B GL(FF_q); ZZ)$ is an isomorphism, and hence also
$H_* (B GL(FF_q)) -> H_* (F psi^q)$ is an isomorphism. However,
$B GL(FF_q) -> F psi^q$ is not a homotopy equivalence, since the spaces have
very different fundamental groups. In the next section, we shall describe the
Quillen "plus" construction, #source(80)which changes the fundamental group of a
space without changing its homology, and we shall see that the above map induces
a homotopy equivalence $B GL(FF_q)^+ -> F psi^q$.

#remark[
  Similar computations may be performed with the other groups of Lie type. For
  details see Fiedorowicz and Priddy [@bib:Fiedorowicz1978] and Kleinerman
  [@bib:Kleinerman1982].
]
