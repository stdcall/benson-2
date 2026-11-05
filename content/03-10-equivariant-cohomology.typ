#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-10-equivariant-cohomology.typ": (
  borel-square, spectral-sequence-map,
)

== Equivariant cohomology and finite generation <sec:equivariant-cohomology>

In this book, we give two different proofs of finite generation of
cohomology#idx("cohomology", "finite generation of")#idx(
  "finite",
  "generation of cohomology",
) of a finite group. The first proof, due to Venkov [@bib:Venkov1959,
@bib:Venkov1961] (see also Quillen [@bib:Quillen1971b]) is topological, and
occupies this section. The second proof, due to Evens [@bib:Evens1961], is
algebraic, and is given in Section~@sec:finite-generation. In each case, we
prove the theorem natural to the theory. In the case of Venkov's proof, the
setting is equivariant cohomology.

Given any topological group $G$ of the homotopy type of a CW complex, and a
$G$-space $X$, we may define the *equivariant cohomology*#idx(
  "cohomology",
  "equivariant",
)#idx("equivariant", "cohomology") of $G$ with coefficients in $X$ to be
$ H_G^* (X; R) = H^* (E G times_G X; R). $
If $phi.alt : G -> G'$ is a homomorphism and $f : X -> X'$ is a compatible map
(i.e., $f(g x) = phi.alt(g) f(x)$) we have a square which commutes up to
homotopy
$ #borel-square $
The fibres of the left-hand and top map are contractible by
Lemma~@lem:milnor-contractible, so by Theorem~@th:whitehead-cw they are homotopy
equivalences. This allows us to fill in the dotted arrow at the bottom uniquely
up to homotopy.

In particular, if we take $G = G'$ and $X = X'$, this shows that the dotted
arrow is a homotopy equivalence, so that $H_G^* (X; R)$ is independent of the
choice of $E G$.

#source(130)In fact this is the topological analogue of hypercohomology,
introduced in Section~2.7 of Volume~I. Namely, if $G$ is discrete, let
$Delta_* (X; R)$ be the complex of singular chains on $X$. Then
$Delta_* (E G times X; R)$ is a projective resolution of $Delta_* (X; R)$ as a
complex of $R G$-modules, and so
$
  H^* (E G times_G X; R) & = H^* (Hom_R (Delta_* (E G times_G X; R), R)) \
                         & = H^* (Hom_(R G) (Delta_* (E G times X; R), R)) \
                         & = Ext_(R G)^* (Delta_* (X; R), R).
$

Since there is a fibration $E G times_G X -> E G times_G ("point") = B G$ with
fibre $X$, we have a spectral sequence
$ H^p (B G; H^q (X)) => H_G^(p+q) (X) $
The space $E G times_G X$ is known as the *Borel construction*#idx(
  "Borel",
  "construction",
)#idx("construction", "Borel") on $X$, and so this spectral sequence is called
the spectral sequence of the Borel construction#idx(
  "spectral sequence",
  "of the Borel construction",
), or the spectral sequence of equivariant cohomology.

#theorem[
  Suppose $G$ is a finite group (or more generally a compact Lie group), $R$ is
  a commutative Noetherian ring of coefficients, and $G arrow.r.hook U(n)$ is an
  embedding of $G$ into a complex unitary group. If $X$ is a $G$-space with the
  property that $H^* (X; R)$ is a finitely generated $R$-module, then
  $H_G^* (X; R)$ is a finitely generated module over $H^* (B U; R)$.
] <th:equivariant-finite-generation>

#proof[
  It follows from the hypothesis that $H^n (X; R) = 0$ for $n$ large. We have a
  fibration $U(n) times_G X -> U(n) slash G$ with fibre $X$, which gives rise to
  a spectral sequence
  $ H^* (U(n) slash G; H^* (X; R)) => H^* (U(n) times_G X; R). $
  Now $U(n) slash G$ is a finite CW-complex, and so the $E_2$ term of the above
  spectral sequence is a finitely generated $R$-module. Since $E_infinity$ is a
  subquotient of $E_2$, this is also a finitely generated $R$-module. It follows
  that $H^* (U(n) times_G X; R)$ has a finite filtration by finitely generated
  $R$-modules, and is hence finitely generated.

  Since $E U(n) times_(U(n)) (U(n) times_G X) = E U(n) times_G X$ and $E U(n)$
  is a contractible space on which $G$ acts freely, we have
  $ H_(U(n))^* (U(n) times_G X; R) tilde.equiv H_G^* (X; R). $
  We thus have a map of spectral sequences
  $ #spectral-sequence-map $
  which makes the lower spectral sequence into a spectral sequence of modules
  over the ring $H^* (B U(n); R)$. Now we described the latter in
  Section~@sec:characteristic-classes. We have
  $ H^* (B U(n); R) = R[c_1, dots, c_n] $
  #source(131)with $deg(c_i) = 2i$. The space $B U(n)$ is simply connected, and
  so
  $
    H^* (B U(n); H^* (U(n) times_G X; R)) = H^* (U(n) times_G X; R)
    [c_1, dots, c_n]
  $
  is a finitely generated module over the Noetherian ring $H^* (B U(n); R)$ by
  the Hilbert basis theorem, and so the $E_2$ page of the lower spectral
  sequence in the above diagram is a finitely generated
  $H^* (B U(n); R)$-module. It follows that the $E_infinity$ page is also a
  finitely generated module, and hence $H_G^* (X; R)$ has a finite filtration by
  finitely generated $H^* (B U(n); R)$-modules and is hence finitely generated.
]

#corollary[
  If $G$ is finite (or compact Lie) and $R$ is Noetherian, the ring $H^* (G; R)$
  is finitely generated as a module over the subring generated by the Chern
  classes of any faithful complex representation. In particular, it is a
  finitely generated graded commutative $R$-algebra.
] <cor:cohomology-finitely-generated>

#proof[
  This is the case where $X$ is a point in the above theorem.
]
