#import "main-defs.typ": *
#import "statements.typ": *

== Steenrod operations <sec:steenrod-operations>

In this section we investigate the operations $Sq^i$ ($p = 2$) and $P^i$ ($p$
odd) in group cohomology#idx("Steenrod operations")#idx(
  "operations",
  "Steenrod",
)#idx("square", "Steenrod"). This is a special case of a more general
construction on cohomology of topological spaces. In a sense, the Kan–Thurston
theorem [@bib:Kan1976] says that it is no loss of generality only to consider
group cohomology, but the price we have to pay for our lack of generality is
that some of the proofs are harder, in particular the proofs that the zeroth
Steenrod operation is the identity and that the negative Steenrod operations are
zero. The standard reference for Steenrod operations in topology is Steenrod and
Epstein [@bib:Steenrod1962].

The idea of the construction is as follows. As indicated in Section~3.2 of
Volume~I, the diagonal approximation on a resolution may be chosen to be
strictly co-associative, but only cocommutative up to homotopy. This lack of
strict cocommutativity means that when we norm a restriction we do not end up
with a power of what we started with (while the transfer of a restriction _is_ a
multiple of what we started with). Thus the norm from $G$ to
$ZZ slash p times G$ should be an interesting operation, even though the
transfer is not.

Now by the Künneth Theorem (3.5.6 of Volume~I),
$
  H^r (ZZ slash p times G, FF_p) = plus.o.big_j H^j (ZZ slash p, FF_p)
  times.o H^(r-j) (G, FF_p),
$
and from Section~3.5 of Volume~I, we know that each $H^j (ZZ slash p, FF_p)$ is
one dimensional over $FF_p$. We choose a basis vector
$a_j in H^j (ZZ slash p, FF_p)$ in the following manner. The element $a_1$ is
chosen arbitrarily, we set $a_2 = -beta(a_1)$, $a_(2j) = (a_2)^j$ and
$a_(2j+1) = a_1 (a_2)^j$, so that $beta(a_(2j-1)) = -a_(2j)$ and
$beta(a_(2j)) = 0$.

#definition[
  #source(149)We define operations
  $ D_j : H^r (G, FF_p) -> H^(p r-j) (G, FF_p) $
  #idx("$D_j$")as follows. If $x in H^r (G, FF_p)$, set
  $
    norm_(G, ZZ slash p times G) (x) & = sum_j a_j times.o D_j (x) \
    & in H^(p r) (ZZ slash p times G)
    = plus.o.big_j H^j (ZZ slash p, FF_p) times.o H^(p r-j) (G, FF_p).
  $
] <def:steenrod-d>

#remark[
  Since the transfer from $G$ to $ZZ slash p times G$ is zero (every element is
  a restriction, so its transfer is given by multiplying by $p$, by
  Proposition~3.6.17 of Volume~I) it follows from
  Proposition~@prop:norm-properties[(iii)] that the norm from $G$ to
  $ZZ slash p times G$ is additive. So the $D_j$ are also additive maps.

  Note that for $r$ odd, the exact sign of $D_j (x)$ depends on the order we
  choose for the cosets of $G$ in $ZZ slash p times G$. We have a particular
  choice in mind, which we discuss at the end of Section~@sec:steenrod-proof.
]

#definition[
  If $p = 2$ and $x in H^r (G, FF_2)$, we define
  $ Sq^i (x) = D_(r-i) (x) in H^(r+i) (G, FF_2). $
  #idx("$Sq^i$")
] <def:steenrod-squares>

For $p$ odd, it turns out that most of the $D_j$ are either the zero map, or
obtainable from others by composing with the Bockstein homomorphism, as will be
seen in the next section. We therefore make the following definition:

#definition[
  If $p$ is odd and $x in H^r (G, FF_p)$, we define
  $
    P^i (x) = (-1)^(i + m r(r+1) slash 2) (m!)^(-r) D_((p-1)(r-2i)) (x)
    in H^(r+2(p-1)i) (G, FF_p)
  $
  #idx("$P^i$")where $m = (p - 1) slash 2$.
] <def:steenrod-powers>

#remark[
  The choice of the constant multiplier of
  $(-1)^(i + m r(r+1) slash 2) (m!)^(-r)$ ensures that $P^0 = 1$, as we shall
  see in the next section.

  Note that $m!$ is a fourth root of unity modulo $p$. Namely, by Wilson's
  theorem,
  $ (m!) . (-1)^m (m!) equiv (p - 1)! equiv -1 quad (mod p) $
  so that
  $
    (m!)^2 equiv (-1)^(m+1) equiv -scaled((frac(-1, p))) quad (mod p)
  $
  (the expression on the right hand side is the Legendre symbol).
]

The principal properties of the Steenrod operations are listed in the following
two theorems, whose proofs will occupy the next two sections.

#theorem(title: [$p = 2$])[
  The Steenrod operations
  $ Sq^i : H^r (G, FF_2) -> H^(r+i) (G, FF_2) $
  satisfy the following axioms:
  + #source(150)$Sq^i$ is an additive map and a natural transformation of
    functors on the category of groups.
  + $Sq^0 = 1$.
  + If $deg(x) = r$ then $Sq^r (x) = x^2$.
  + If $deg(x) < r$ then $Sq^r (x) = 0$.
  + (Cartan formula#idx("Cartan formula"))
    $ Sq^k (x y) = sum_(i+j=k) Sq^i (x) Sq^j (y). $
  + $Sq^1 = beta : H^r (G, FF_2) -> H^(r+1) (G, FF_2)$.
  + (Adem relations#idx("Adem relations")#idx("relations, Adem")) If
    $0 < a < 2b$ then
    $
      Sq^a Sq^b = sum_(j=0)^([a slash 2]) binom(b - 1 - j, a - 2j)
      Sq^(a+b-j) Sq^j.
    $
] <th:steenrod-squares>

#theorem(title: [$p$ odd])[
  The Steenrod operations
  $ P^i : H^r (G, FF_p) -> H^(r+2(p-1)i) (G, FF_p) $
  satisfy the following axioms:
  + $P^i$ is an additive map and a natural transformation of functors on the
    category of groups.
  + $P^0 = 1$.
  + If $deg(x) = 2r$ then $P^r (x) = x^p$.
  + If $deg(x) < 2r$ then $P^r (x) = 0$.
  + (Cartan formula)
    $ P^k (x y) = sum_(i+j=k) P^i (x) P^j (y). $
  + (Adem relations) If $a < p b$ then
    $
      P^a P^b = sum_(j=0)^([a slash p]) (-1)^(a+j)
      binom((p - 1)(b - j) - 1, a - p j) P^(a+b-j) P^j.
    $
    If $a lt.eq p b$ then
    $
      P^a beta P^b & = sum_(j=0)^([a slash p]) (-1)^(a+j)
                     binom((p - 1)(b - j), a - p j) beta P^(a+b-j) P^j \
                   & quad + sum_(j=0)^([(a-1) slash p]) (-1)^(a+j-1)
                     binom((p - 1)(b - j) - 1, a - p j - 1)
                     P^(a+b-j) beta P^j.
    $
] <th:steenrod-powers>
