#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-10-plus-construction.typ": (
  extension-five-term, fibration-five-term, fibre-homotopy-sequence,
  plus-pushout, pullback-composition,
)

== The plus construction and algebraic K-theory <sec:plus-construction>

In the last section we saw that there is a map $B GL(FF_q) -> F psi^q$ which
induces an isomorphism in integral homology. We now introduce the Quillen "plus"
construction#idx("plus construction")#idx(
  "Quillen",
  "'s plus construction",
)#idx("construction", "Quillen's plus"), which turns homology equivalences into
homotopy equivalences, and use this to define the algebraic K-theory#idx(
  "algebraic",
  "K-theory",
)#idx("K-theory", "algebraic") of a ring. The homotopy equivalence
$B GL(FF_q)^+ -> F psi^q$ calculates the algebraic K-theory of finite fields.

#theorem(title: [Quillen])[
  Let $(X, x_0)$ be a CW-complex. Let $pi$ be a perfect normal subgroup (i.e.,
  equal to its commutator subgroup) of $pi_1 (X, x_0)$. Then there is an
  inclusion $i : X arrow.r.hook X^+$ with the following properties:
  + $(X^+, X)$ is a relative CW-complex of dimension at most 3.
  + $i_* : pi_1 (X, x_0) -> pi_1 (X^+, x_0)$ is an epimorphism with kernel $pi$.
  + Let $tilde(X)^+$ be a covering space of $X^+$, and $tilde(X)$ be the
    corresponding cover of $X$ with fundamental group
    $pi_1 (tilde(X), x_0) = i_*^(-1) pi_1 (tilde(X)^+, x_0)$, so that $i$ lifts
    to a map $tilde(i) : tilde(X) -> tilde(X)^+$. Then
    $tilde(i)_* : H_n (tilde(X)) -> H_n (tilde(X)^+)$ is an isomorphism for all
    $n gt.eq 0$.
  + If $f : (X, x_0) -> (Z, z_0)$ is a map of spaces with $pi$ in the kernel of
    $f_* : pi_1 (X, x_0) -> pi_1 (Z, z_0)$, then there is a map
    $f' : (X^+, x_0) -> (Z, z_0)$ with $f' compose i tilde.eq f$. If $f$ enjoys
    properties #statement-comment[(ii)] and #statement-comment[(iii)] above of
    the inclusion $i$ (but $f$ is not necessarily an inclusion), then $f'$ is a
    homotopy equivalence. In particular, $X^+$ is uniquely determined up to
    homotopy.
] <th:plus-construction>

#proof[
  The idea of the proof is to attach 2-cells to kill $pi$, and then attach
  3-cells to make sure the homology is unaffected, which of course by the
  Hurewicz theorem requires that $pi$ is perfect. The details are as follows.
  Choose a collection of commutators $[y_j, z_j]$ of elements of $pi$,
  generating $pi$ as a normal subgroup of $pi_1 (X, x_0)$. Choose maps
  $tilde(y)_j, tilde(z)_j : (S^1, s_0) -> (X, x_0)$, $j in J$, representing
  these generators. Set
  $lambda_j = tilde(y)_j * tilde(z)_j * tilde(y)_j^(-1) * tilde(z)_j^(-1)$, and
  let $Y$ be the space
  $ Y = X union_(lambda_j) union.big_(j in J) sigma_j^2 $
  obtained by attaching 2-cells $sigma_j^2$ to $X$ using the attaching maps
  $lambda_j$. Thus we have $pi_1 (Y, y_0) tilde.equiv pi_1 (X, x_0) slash pi$.

  Let $macron(sigma)_j^2$ denote the quotient of the cell $sigma_j^2$ obtained
  by identifying the parts of the boundary corresponding to $tilde(y)_j$ and
  $tilde(y)_j^(-1)$ in opposite directions, so that the characteristic map
  $sigma_j^2 -> Y$ factors through $macron(sigma)_j^2$, and $macron(sigma)_j^2$
  is an open #source(81)cylinder with ends corresponding to $tilde(z)_j$ and
  $tilde(z)_j^(-1)$. Since $z_j$ can be expressed as a product of the
  commutators generating $pi$, the path $tilde(z)_j$ is null homotopic in $Y$,
  and so the map $macron(sigma)_j^2 -> Y$ extends to a map from the 2-sphere (=
  closed cylinder) obtained by capping off the ends of $macron(sigma)_j^2$. This
  can then be used as the attaching map $mu_j : (S^2, s_0) -> (Y, x_0)$ for a
  3-cell $sigma_j^3$, and we set
  $ X^+ = Y union_(mu_j) union.big_(j in J) sigma_j^3. $
  Note that the attaching maps $lambda_j$ and $mu_j$ can be chosen to have their
  images lying in the 1-skeleton of $X$, resp. 2-skeleton of $Y$, so that $X^+$
  is a CW-complex.

  We now check properties (i)–(iv) above. Property (i) is clear from the
  construction. Property (ii) follows from the fact that
  $ pi_2 (X^+, Y, x_0) = pi_1 (X^+, Y, x_0) = 0 $
  so that $pi_1 (X^+, x_0) = pi_1 (Y, x_0) = pi_1 (X, x_0) slash pi$.

  To prove property (iii), suppose $tilde(X)^+$ is a cover of $X^+$
  corresponding to a subgroup $G slash pi lt.eq pi_1 (X, x_0) slash pi$, and
  $tilde(X)$ is the cover of $X$ corresponding to $G lt.eq pi_1 (X, x_0)$. Then
  we have a corresponding cover $tilde(Y)$ of $Y$ with
  $
    tilde(Y) = tilde(X) union_(phi.alt_g (lambda_j))
    union.big_(j in J \ g in pi_1 (X, x_0) slash G) sigma_(j, g)^2
  $
  where the $phi.alt_g$ are the covering translations corresponding to coset
  representatives $g$ of $G$ in $pi_1 (X, x_0)$. Similarly
  $
    tilde(X)^+ = tilde(Y) union_(phi.alt_g (mu_j))
    union.big_(j in J \ g in pi_1 (X, x_0) slash G) sigma_(j, g)^3.
  $
  Thus the complex of cellular chains $C_* (tilde(X)^+, tilde(X))$ is just
  $ dots.c -> 0 -> F limits(->)^tilde.equiv F -> 0 -> 0, $
  where $F$ is the free $ZZ$-module on the cells $sigma_(j, g)^3$, respectively
  $sigma_(j, g)^2$. The boundary map is the map taking $sigma_(j, g)^3$ to
  $sigma_(j, g)^2$, and so $H_* (tilde(X)^+, tilde(X)) = 0$, which implies
  property (iii).

  Finally, if $f : (X, x_0) -> (Z, z_0)$ is a map of spaces with the property
  that $pi$ is in the kernel of $f_* : pi_1 (X, x_0) -> pi_1 (Z, z_0)$, then we
  form the pushout $(Z^+, z_0)$ of $f$ and $i$
  $ #plus-pushout $
  This is the same as the space obtained from $(Z, z_0)$ by attaching 2-cells
  and 3-cells by the above recipe using the null homotopic paths
  $f compose tilde(y)_j, f compose tilde(z)_j :$
  #source(82)$(S^1, s_0) -> (Z, z_0)$. Thus by (ii), the inclusion $i'$ induces
  an isomorphism $pi_1 (Z, z_0) -> pi_1 (Z^+, z_0)$ and hence lifts to an
  inclusion of universal covers $tilde(i)' : tilde(Z) arrow.r.hook tilde(Z)^+$.
  By (iii), this is a homology isomorphism of spaces with trivial fundamental
  group, and hence by Whitehead's Theorem~@th:whitehead-homology, it induces an
  isomorphism on homotopy groups. So for $n > 1$,
  $
    pi_n (Z, z_0) = pi_n (tilde(Z), z_0) = pi_n (tilde(Z)^+, z_0)
    = pi_n (Z^+, z_0).
  $
  So we can now apply Whitehead's Theorem~@th:whitehead-cw to deduce that the
  inclusion $i' : (Z, z_0) arrow.r.hook (Z^+, z_0)$ is a homotopy equivalence.
  Let $alpha : (Z^+, z_0) -> (Z, z_0)$ be a homotopy inverse for $i'$. Then we
  can take for $f'$ the map $alpha compose f^+$, so that
  $
    f' compose i = alpha compose f^+ compose i
    = alpha compose i' compose f tilde.eq f.
  $

  If $f$ enjoys properties (ii) and (iii) then
  $f'_* : pi_1 (X^+, x_0) -> pi_1 (Z, z_0)$ is an isomorphism, and so $f'$ lifts
  to a map $tilde(f)' : (tilde(X)^+, x_0) -> (tilde(Z), z_0)$ of universal
  covers, which is a homology isomorphism and hence an isomorphism on homotopy
  groups by Theorem~@th:whitehead-homology. So $f'$ is also an isomorphism on
  homotopy groups, and hence a homotopy equivalence by Theorem~@th:whitehead-cw.
]

If $Lambda$ is a ring, let $GL(Lambda)$ be the union of the groups
$GL_n (Lambda)$ under the obvious inclusions
$GL_n (Lambda) arrow.r.hook GL_(n+1) (Lambda)$, and regarded as a discrete
group. Let $E(Lambda)$ denote the subgroup generated by the *elementary
matrices*#idx("elementary", "matrices")#idx("matrices, elementary"), namely the
matrices which differ from the identity matrix in a single off-diagonal entry.
The identities
$
  mat(A B A^(-1) B^(-1), 0; 0, I)
  & = mat(A, 0; 0, A^(-1)) mat(B, 0; 0, B^(-1)) mat((B A)^(-1), 0; 0, B A) \
  mat(A, 0; 0, A^(-1))
  & = mat(I, A; 0, I) mat(I, 0; -A^(-1), I) mat(I, A; 0, I) mat(0, -I; I, 0) \
  mat(0, -I; I, 0) & = mat(I, 0; I, I) mat(I, -I; 0, I) mat(I, 0; I, I)
$
show that every commutator in $GL_n (Lambda)$ is a product of elementary
matrices in $GL_(2n) (Lambda)$, so that $E(Lambda)$ is the commutator subgroup
of $GL(Lambda)$ and is perfect.

#definition[
  The (Quillen) algebraic K groups of a ring $Lambda$ are defined as
  $ K_i (Lambda) = pi_i (B GL(Lambda)^+) quad (i gt.eq 1). $
  Here, the plus construction is with respect to the commutator subgroup
  $E(Lambda)$ of the fundamental group $pi_1 (B GL(Lambda)) = GL(Lambda)$. Note
  that since $GL(Lambda)$ is a discrete group, $B GL(Lambda)$ is the same thing
  as the Eilenberg–Mac~Lane space $K(GL(Lambda), 1)$.
] <def:algebraic-k-groups>
#idx("$K_i (Lambda)$", target: [@def:algebraic-k-groups])

(The group $K_0 (Lambda)$ is defined as the Grothendieck group of finitely
generated projective $Lambda$-modules, as usual; see Section~5.1 of Volume~I).

#theorem[
  #source(83)The map $B GL(FF_q) -> F psi^q$ defined in the last section induces
  a homotopy equivalence $B GL(FF_q)^+ tilde.eq F psi^q$, where the plus
  construction is applied to the perfect normal subgroup $E(FF_q)$#idx(
    "$E(FF_q)$",
  ) of elementary matrices. We have
  $
    K_(2j-1) (FF_q) = ZZ slash (q^j - 1), wide K_(2j) (FF_q) = 0.
  $
] <th:k-theory-finite-fields>

#proof[
  We saw at the end of the last section that $B GL(FF_q) -> F psi^q$ is a
  homology isomorphism. Now $pi_1 (B GL(FF_q)) = GL(FF_q)$, and
  $pi_1 (F psi^q) = ZZ slash (q - 1)$. Since the map is a homology isomorphism,
  the kernel of the map on $pi_1$ is $E(FF_q)$, the kernel of the determinant
  map. It follows from Theorem~@th:plus-construction[(iv)] that this map extends
  to a map $B GL(FF_q)^+ -> F psi^q$ which is a homology isomorphism. Since both
  $B GL(FF_q)^+$ and $F psi^q$ are simple spaces, we may apply Whitehead's
  Theorems~@th:whitehead-homology and~@th:whitehead-cw to deduce that this map
  is a homotopy equivalence. Thus $K_i (FF_q) tilde.equiv pi_i (F psi^q)$, which
  was calculated in Section~@sec:general-linear-groups.
]

The groups $K_1 (Lambda)$ and $K_2 (Lambda)$#idx(
  "$K_1 (Lambda)$, $K_2 (Lambda)$",
) have explicit algebraic interpretations as follows.

#proposition[
  + $K_1 (Lambda) tilde.equiv GL(Lambda) slash E(Lambda)$
  + $K_2 (Lambda) tilde.equiv H_2 (E(Lambda), ZZ)$.
] <prop:k1-k2>

#proof[
  + This follows directly from the definition
    $ K_1 (Lambda) = pi_1 (B GL(Lambda)^+) $
    since the purpose of the plus construction on $B GL(Lambda)$ was to kill the
    perfect subgroup $E(Lambda)$ of $pi_1 (B GL(Lambda)) = GL(Lambda)$.
  + Let $F$ be the homotopy fibre (see the exercise at the end of
    Section~@sec:fibrations) of the map $B GL(Lambda) -> B GL(Lambda)^+$. Thus
    we have a long exact sequence of homotopy groups
    (Proposition~@prop:homotopy-long-exact-sequence)
    $ #fibre-homotopy-sequence $
    and so we have a central extension
    $ 0 -> pi_2 (B GL(Lambda)^+) -> pi_1 (F) -> E(Lambda) -> 0. $

    We have a map $F -> B pi_1 (F)$ inducing an isomorphism on $pi_1$. Turn it
    into a fibration with fibre $F'$. The five term exact sequence of this
    fibration (see Proposition~@prop:five-term-homology and
    Section~@sec:fibration-sequence) is
    $ #fibration-five-term $
    #source(84)and hence $H_2 (pi_1 (F), ZZ) = 0$. The five term exact sequence
    of the above central extension (see Section~@sec:group-extension) is
    $ #extension-five-term $
    and hence
    $K_2 (Lambda) = pi_2 (B GL(Lambda)^+) tilde.equiv H_2 (E(Lambda), ZZ)$.
]

#remark[
  In Quillen [@bib:Quillen1973a], another definition is given for
  $K_i (Lambda)$. Namely, one forms a category
  $Q(lmodule(Lambda, bold("Proj")))$ whose objects are finitely generated
  projective $Lambda$-modules, and where an arrow from $P$ to $Q$ is an
  isomorphism class of diagrams of the form
  $ P limits(<-)^j P' limits(->)^i Q $
  where $P'$ is another finitely generated projective $Lambda$-module, $j$ is an
  epimorphism and $i$ is a monomorphism. Two such diagrams are thought of as
  isomorphic if there is an isomorphism which is the identity on $P$ and $Q$.
  Arrows are composed by pulling back
  $ #pullback-composition $
  so that $P''$ is the submodule of $P' plus.o Q'$ consisting of elements
  $(x, y)$ where $x$ and $y$ have the same image in $Q$. We now form the
  classifying space $B Q(lmodule(Lambda, bold("Proj")))$ of this category (see
  the exercise in Section~@sec:simplicial-sets), and set
  $
    K_i (Lambda) = pi_(i+1) (B Q(lmodule(Lambda, bold("Proj"))), bold(0)),
    quad i gt.eq 0
  $
  where $bold(0)$ denotes the zero module in $Q(lmodule(Lambda, bold("Proj")))$,
  thought of as a basepoint for $B Q(lmodule(Lambda, bold("Proj")))$.

  In Grayson [@bib:Grayson1976], one can find Quillen's proof that there is a
  homotopy equivalence
  $
    Omega B Q(lmodule(Lambda, bold("Proj")))
    tilde.eq K_0 (Lambda) times B GL(Lambda)^+
  $
  so that
  $
    pi_(i+1) (B Q(lmodule(Lambda, bold("Proj"))))
    tilde.equiv pi_i (B GL(Lambda)^+)
  $
  for $i gt.eq 1$, and hence this definition agrees with the previous one.

  It is proved in Wagoner [@bib:Wagoner1972] that if we let $mu(Lambda)$ be the
  ring of infinite matrices $(lambda_(i j))$, $1 lt.eq i, j < infinity$ with
  only a finite number of non-zero entries in each row and column, modulo the
  ideal consisting of those matrices with at #source(85)most finitely many
  non-zero entries (this should be thought of as a sort of algebraic suspension
  of the ring $Lambda$), then
  $
    Omega(B GL(mu(Lambda))^+) tilde.eq K_0 (Lambda) times B GL(Lambda)^+.
  $
  It follows that $K_0 (Lambda) times B GL(Lambda)^+$ is an $n$-fold loop space
  in a canonical way for every value of $n gt.eq 0$.
]
