#import "main-defs.typ": *
#import "statements.typ": *

== Cohen–Macaulay cohomology rings <sec:cohen-macaulay>
#idx("Cohen–Macaulay", "cohomology", target: [@sec:cohen-macaulay])#idx(
  "cohomology",
  "Cohen–Macaulay",
  target: [@sec:cohen-macaulay],
)

Recall from Section~@sec:commutative-algebra that a finitely generated graded
$k$-algebra is Cohen–Macaulay if there is a polynomial subring over which it is
finitely generated and free as a module.

If $E$ is an elementary abelian $p$-group then $H^* (E, k)$ is Cohen–Macaulay.
Quillen's calculations (see Section~@sec:general-linear-groups) show that the
cohomology rings of general linear groups at primes other than the natural one
are Cohen–Macaulay, and his work on extraspecial 2-groups (see
Section~@sec:extraspecial) shows that these also have Cohen–Macaulay cohomology
rings. If $G$ is a semidihedral 2-group#idx("semidihedral group")#idx(
  "group",
  "semidihedral",
) then $H^* (G, k)$ is not Cohen–Macaulay, see Evens and Priddy
[@bib:Evens1985]. Also, if $G$ is a split metacyclic $p$-group#idx(
  "metacyclic group",
)#idx("group", "metacyclic") with $p$ odd, then usually $H^* (G, k)$ is not
Cohen–Macaulay, see Diethelm [@bib:Diethelm1985]. Note that if $G$ has maximal
elementary abelian $p$-subgroups of different ranks, then by Quillen's
Stratification Theorem~@th:quillen-stratification the variety is not
equidimensional and so $H^* (G, k)$ is not Cohen–Macaulay.

In this section, we shall use the Poincaré duality of the last section to show
that the Poincaré series satisfies a certain functional equation in the
Cohen–Macaulay case.

#theorem[
  #statement-comment[[@bib:Benson1994a]] Suppose $G$ is a finite group and $k$
  is a field of characteristic $p$. If $H^* (G, k)$ is Cohen–Macaulay, then the
  Poincaré series
  $ p(t) = sum_(r >= 0) t^r dim_k H^r (G, k) $
  is a rational function of $t$ satisfying the functional equation#idx(
    "functional equation",
  )#idx("equation", "functional")#idx("equation, functional")
  $ p(1 slash t) = (-t)^(r_p (G)) p(t), $
  where $r_p (G)$ is the $p$-rank of $G$.
] <th:cohen-macaulay-functional-equation>

#proof[
  #source(224)The fact that $p(t)$ is a rational function of $t$ follows from
  Proposition~@prop:hilbert-serre.

  Let $zeta_1, dots, zeta_r$ be elements of degrees $n_1, dots, n_r$ (with each
  $n_i >= 2$) generating a polynomial subring over which $H^* (G, k)$ is a
  finitely generated free module. Thus by Theorem~@th:quillen-krull-dimension we
  have $r = r_p (G)$. Let $bold(C)$ be the complex described in
  Theorem~@th:multiple-complex-lattice (with $M = k$). According to
  Theorem~@th:tate-spectral-sequence, there is a spectral sequence whose $E_2$
  term is given by
  $
    E_2^(p q) = Hom_k (H_q (bold(C)), H^p (G, k)) =
    H^* (G, k) times.o Lambda^* (tilde(zeta)_1, dots, tilde(zeta)_r),
  $
  where $Lambda^* (tilde(zeta)_1, dots, tilde(zeta)_r)$ is an exterior algebra
  on generators $tilde(zeta)_i$ in degree $n_i - 1$, and converging to
  $H^* (Hom_(k G) (bold(C), k))$.

  Arguing as in the proof of Theorem~@th:multiple-complex-lattice, for each
  $zeta_i$ we have a homomorphism of spectral sequences
  $
    E_2^(p q) (zeta_i) = Hom_k (H_q (bold(C)_(zeta_i)), H^p (G, k)) ->
    E_2^(p q).
  $
  By Lemma~@lem:two-row-differential we have
  $d_(n_i) (alpha . tilde(zeta)_i) = alpha . zeta_i$. Since the $zeta_i$ form a
  regular sequence in $H^* (G, k)$, one can check that this determines all the
  differentials (see the remarks below), and the $E_infinity$ page is
  $H^* (G, k) slash (zeta_1, dots, zeta_r)$ concentrated along the bottom row.
  We thus have
  $
    H^* (G, k) slash (zeta_1, dots, zeta_r) tilde.equiv
    H^* (Hom_(k G) (bold(C), k)).
  $
  Thus if $f(t)$ is the Poincaré series of $H^* (Hom_(k G) (bold(C), k))$, we
  have
  $ p(t) = f(t) slash product_(i=1)^r (1 - t^(n_i)). $
  Since by Corollary~@cor:poincare-series-duality $f(t)$ satisfies
  $t^s f(1 slash t) = f(t)$, where $s = sum_(i=1)^r (n_i - 1)$, we have
  $
    p(1 slash t) = f(1 slash t) slash product_(i=1)^r (1 - t^(-n_i)) =
    t^(-s) f(t) . product_(i=1)^r t^(n_i) slash (t^(n_i) - 1) = (-t)^r p(t).
  $
]

#remark(kind: "Remarks")[
  Strictly speaking, in the above proof, we have assumed that the spectral
  sequence has a multiplicative structure, and we have not shown this to be the
  case. One can get round this by using more homomorphisms of spectral
  sequences, see Section~9 of [@bib:Benson1994a] for further details.

  Alternatively, one can try to impose a multiplicative structure. For this
  purpose, one really needs a comultiplication#idx("comultiplication") on
  $bold(C)$. In Carlson [@bib:Carlson1987d], it is shown that as long as $zeta$
  annihilates $Ext^*_(k G) (L_zeta, L_zeta)$ (cf.
  Propositions~@prop:annihilator-criterion and~@prop:zeta-squared-annihilates;
  in particular this always happens if $p$ is odd), and as long as we use the
  dual $Hom_k (bold(C)_(zeta_i), k) [n_i - 1]$ instead of $bold(C)_(zeta_i)$
  (which we may do with impunity according to the last section), there is a
  comultiplication on each $bold(C)_(zeta_i)$ with the desired properties. For
  $p = 2$ the situation is less clear.

  Even if $H^* (G, k)$ is not Cohen–Macaulay, the spectral sequence described in
  the above theorem still gives very strong restrictions on the possible shape
  of $H^* (G, k)$. In [@bib:Benson1994a], all the differentials in this spectral
  sequence are described in terms of matric Massey products#idx(
    "matric Massey products",
  )#idx("products", "matrix Massey") (see also [@bib:Benson1992a]).
]

#source(225)Many theorems in the cohomology of finite groups generalise in an
obvious way to compact Lie groups#idx("compact Lie groups")#idx(
  "group",
  "compact Lie",
)#idx("Lie", "groups, compact"). The following corollary is, of course, false in
general for compact Lie groups.

#corollary[
  Suppose $G$ is a finite group and $k$ is a field of characteristic $p$. If
  $H^* (G, k)$ is a polynomial ring, then $p = 2$, the generators are in degree
  one, and $G slash O_(2') (G)$ is an elementary abelian 2-group#idx(
    "elementary",
    "abelian group",
  )#idx("group", "elementary abelian").
] <cor:polynomial-cohomology>

#proof[
  Since a polynomial ring is Cohen–Macaulay, the functional equation of the
  theorem must be satisfied. This can only happen if the generators are in
  degree one. It follows that $p = 2$, since otherwise degree one elements
  square to zero.

  Since $H^1 (G, k) tilde.equiv Hom(G, k)$, it follows that $G$ has an
  elementary abelian quotient $G slash N$ with the property that the map
  $G -> G slash N$ induces an isomorphism $H^* (G slash N, k) -> H^* (G, k)$.
  Since this is the horizontal edge homomorphism for the Lyndon–Hochschild–Serre
  spectral sequence of the group extension, we deduce that the vertical edge
  homomorphism, namely restriction from $H^* (G, k)$ to $H^* (N, k)$ is zero in
  positive degrees. By Theorem~@th:cohomology-nonvanishing, this implies that
  $N$ has no elements of order two, so that $N = O_(2') (G)$.
]

#remark(kind: "Recent progress", punct: ":")[
  Since the first edition of this book was published, the theory of varieties
  for modules has been extended to infinitely generated modules for finite
  groups [@bib:Benson1995b, @bib:Benson1996b] using Rickard's theory of
  idempotent modules in the stable category [@bib:Rickard1997]. The main
  difference from the finitely generated case is that instead of a single
  subvariety, a module has associated to it a collection of subvarieties of
  $V_G$. This rests on a version of Dade's lemma for infinitely generated
  modules in [@bib:Benson1996b] in which one has to restrict not just to cyclic
  shifted subgroups defined over the original field, but also to "generic"
  cyclic shifted subgroups defined over the function fields of subvarieties.

  This work has had a number of applications. It was used in [@bib:Benson1997c]
  to classify the thick subcategories of the stable category of finitely
  generated modules for a $p$-group. In [@bib:Benson1995a] it was used to prove
  most of the conjectures made in [@bib:Benson1990a] on the vanishing of
  cohomology, although it has later been shown by Carlson (see section 13 of
  [@bib:Carlson1996e]) that this can be proved without appealing to infinitely
  generated modules. In [@bib:Benson1997a, @bib:Benson1997b] the theory of
  varieties of modules is extended to a large class of infinite groups. The
  point here is that even if a module starts off finitely generated, if we
  restrict to a subgroup of infinite index it need not end up that way.

  The *nucleus*#idx("nucleus") is defined to be the subvariety $Y_G$ of $V_G$
  given by the union of the images of the restriction maps
  $res^*_(G, H) : V_H -> V_G$ as $H$ runs over the subgroups of $G$ whose
  centraliser is not $p$-nilpotent. This concept was introduced in
  [@bib:Benson1990a], and its importance has become more apparent in
  [@bib:Benson1995a] where it is seen to control the modules in the principal
  block having no cohomology, and in [@bib:Benson1997c] where it plays a role in
  the classification of thick subcategories of the stable category of finitely
  generated modules.
]
