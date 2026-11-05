#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-13-cyclic-homology.typ": (
  cohomology-bicomplex, connes-bicomplex, connes-ladder, lambda-b-bicomplex,
  reduced-b-bicomplex,
)

== Cyclic homology <sec:cyclic-homology>

Cyclic homology was first introduced by Connes [@bib:Connes1985], and
independently by Tsygan [@bib:Tsygan1983] who called it "additive
K-theory."#idx("additive K-theory")#idx("K-theory", "additive") These authors
worked with algebras in characteristic zero, and used the quotient of the
Hochschild complex by the actions of cyclic groups. Loday and Quillen
[@bib:Loday1984] noticed that Tsygan's proof of the long exact sequence
connecting cyclic homology and Hochschild homology could be expressed in terms
of a certain double complex, which provides the appropriate definition of cyclic
homology over an arbitrary commutative ring of coefficients. We advise the
reader not already familiar with double complexes to read
Section~@sec:double-complex on the spectral sequence of a double complex before
continuing with this section.

Recall from Section~@sec:hochschild that in the Hochschild complex for computing
the Hochschild homology groups $H H_* (Lambda) = H_* (Lambda, Lambda)$, the
elements of degree $n$ are
$Lambda times.o_R tilde(S)_n (Lambda) = Lambda^(times.o (n+1))$, with
differential
$
  b(lambda_0 times.o dots.c times.o lambda_n)
  = & sum_(i=0)^(n-1) (-1)^i lambda_0 times.o dots.c times.o
      lambda_i lambda_(i+1) times.o dots.c times.o lambda_n \
    & quad + (-1)^n lambda_n lambda_0 times.o dots.c times.o lambda_(n-1).
$
We also reindex the acyclic Hochschild complex so that
$S_(n-1) (Lambda) = Lambda^(times.o (n+1))$ sits in degree $n$ (rather than
$n - 1$), with differential
$
  b'(lambda_0 times.o dots.c times.o lambda_n)
  = sum_(i=0)^(n-1) (-1)^i lambda_0 times.o dots.c times.o
  lambda_i lambda_(i+1) times.o dots.c times.o lambda_n.
$
We have an action of
$chevron.l t_n | (t_n)^(n+1) = 1 chevron.r tilde.equiv ZZ slash (n + 1)$ on
$Lambda^(times.o (n+1))$ given by
$
  t_n (lambda_0 times.o dots.c times.o lambda_n)
  = lambda_n times.o lambda_0 times.o dots.c times.o lambda_(n-1).
$
#source(93)Let $N$ be the sum of the distinct powers of $(-1)^n t_n$,
$ N = sum_(j=0)^n ((-1)^n t_n)^j, $
and let $epsilon = 1 - (-1)^n t_n$. One can easily check that
$N epsilon = epsilon N = 0$, and $N$ and $epsilon$ are related to the
differentials $b$ and $b'$ via the formulae
$ b epsilon = epsilon b', wide b' N = N b. $

From the first of these formulae, one sees that $b$ takes elements in the image
of $epsilon$ to elements in the image of $epsilon$, so that $b$ passes down to a
differential on the quotient by the action of $(-1)^n t_n$
$ b : Lambda_epsilon^(times.o (n+1)) -> Lambda_epsilon^(times.o (n)), $
where $Lambda_epsilon^(times.o (n+1))$ is defined to be
$Lambda^(times.o (n+1)) slash Im(epsilon)$. If the coefficient ring $R$ is a
field of characteristic zero, we define the cyclic homology#idx(
  "cyclic",
  "homology",
)#idx("homology", "cyclic") of $Lambda$ to be the homology of this chain
complex#idx("$H C_* (Lambda)$")
$
  H C_n (Lambda) = frac(
    Ker(b : Lambda_epsilon^(times.o (n+1)) -> Lambda_epsilon^(times.o (n))),
    Im(b : Lambda_epsilon^(times.o (n+2)) -> Lambda_epsilon^(times.o (n+1))),
  ).
$

#proposition[
  There is a long exact sequence (the *Connes sequence*#idx(
    "Connes sequence",
  )#idx(
    "exact",
    "sequence",
    "Connes",
  )#idx("sequence", "Connes"))
  $
    dots.c -> H H_n (Lambda) limits(->)^I H C_n (Lambda) limits(->)^S
    H C_(n-2) (Lambda) limits(->)^B H H_(n-1) (Lambda) limits(->)^I
    H C_(n-1) (Lambda) -> dots.c
  $
] <prop:connes-sequence>

#proof[
  We write down the following double complex.
  $ #connes-bicomplex $
  The columns are alternate copies of the Hochschild complex and the acyclic
  Hochschild complex. The signs on the acyclic Hochschild complex have been
  negated so that the squares anticommute (by the above formulae relating
  $epsilon$, $N$, $b$ and $b'$), in accordance with the definition of a double
  complex (Section~@sec:double-complex).

  The $n$th row of the above double complex is the complex described in
  Section~3.5 of Volume~I for calculating
  $H_* (ZZ slash (n + 1), Lambda^(times.o (n+1)))$. Since $Lambda$ is an algebra
  over a field of characteristic zero, this vanishes in degrees greater than
  zero, and in degree zero it just gives $Lambda_epsilon^(times.o (n+1))$. So if
  we look at the spectral sequence obtained by doing the horizontal differential
  first in the #source(94)above double complex (i.e., the spectral sequence of
  the transpose of this double complex; see Section~@sec:double-complex), we see
  that the $E^1$ term
  $ E_(p q)^1 = H_q (ZZ slash (p + 1), Lambda^(times.o (p+1))) $
  vanishes for $q > 0$ and is the complex for calculating $H C_* (Lambda)$ for
  $q = 0$. So this spectral sequence shows that $H C_* (Lambda)$ is isomorphic
  to the homology of the total complex $C C_* (Lambda)$#idx("$C C_*(Lambda)$")
  of the above double complex.

  Now the total complex $X_*$ of the first two columns of the above double
  complex has the Hochschild complex as a subcomplex, and the acyclic Hochschild
  complex as the quotient. The long exact sequence of homology for this short
  exact sequence of complexes shows that the homology of $X_*$ is just
  $H H_* (Lambda)$.

  The complex $X_*$ is a subcomplex of $C C_* (Lambda)$, and the quotient is
  just the same complex with a shift, $C C_* (Lambda)[-2]$, so we have a short
  exact sequence of complexes
  $ 0 -> X_* -> C C_* (Lambda) -> C C_* (Lambda)[-2] -> 0. $
  Taking homology, we obtain the required long exact sequence.
]

If $Lambda$ is defined over a more general coefficient ring $R$, then the
homology of the cyclic groups fails to vanish in the above proof. So we _define_
the *cyclic chains*#idx("cyclic", "chains")#idx("chain", "cyclic") $C C_*$ to be
the total complex of the double complex appearing in the above proof, and the
*cyclic homology* $H C_* (Lambda)$ to be the homology of this chain complex.
With this new definition, the rest of the above proof works, and shows that for
a general $Lambda$ we still have the long exact sequence of the above
proposition.

#theorem[
  A Morita equivalence between $R$-algebras $Lambda$ and $Gamma$ gives rise to
  an isomorphism $H C_n (Lambda) tilde.equiv H C_n (Gamma)$ for all $n >= 0$.
] <th:cyclic-morita>

#proof[
  (McCarthy [@bib:McCarthy1988]; see also Kassel [@bib:Kassel1988]) The idea
  here is to show that the isomorphism in Hochschild homology described in
  Theorem~@th:hochschild-morita comes from a chain equivalence of Hochschild
  complexes which commutes with the operations $t_n$ and $b'$, so that the
  result follows from the long exact Connes sequence by induction on $n$. The
  details are as follows.

  Suppose that $lmodule(Lambda, P)_Gamma$ and $lmodule(Gamma, Q)_Lambda$ are
  bimodules and $phi.alt : P times.o_Gamma Q -> Lambda$ and
  $psi : Q times.o_Lambda P -> Gamma$ are surjective bimodule homomorphisms as
  in Definition~2.2.2 of Volume~I, satisfying the identities
  $x psi(y times.o z) = phi.alt(x times.o y) z$ and
  $y phi.alt(z times.o w) = psi(y times.o z) w$ for $x$ and $z$ in $P$ and $y$
  and $w$ in $Q$. Choose elements $p_i$ and $q_i$, $1 <= i <= s$, with
  $phi.alt(sum_(i=1)^s p_i times.o q_i) = 1 in Lambda$, and elements $p'_j$ and
  $q'_j$, $1 <= j <= t$ with $psi(sum_(j=1)^t q'_j times.o p'_j) = 1 in Gamma$.
  We define chain maps on the Hochschild complex
  $
    & alpha_n : Lambda^(times.o (n+1)) -> Gamma^(times.o (n+1)) \
    & (lambda_0, dots, lambda_n) |-> sum_((i_0, dots, i_n))
      (psi(q_(i_0) times.o lambda_0 p_(i_1)), psi(
          q_(i_1) times.o lambda_1
          p_(i_2)
        ), dots, psi(q_(i_n) times.o lambda_n p_(i_0)))
  $
  #source(95)where the sum is over all sequences $(i_0, dots, i_n)$ of integers
  between 1 and $s$ inclusive, and
  $
    & beta_n : Gamma^(times.o (n+1)) -> Lambda^(times.o (n+1)) \
    & (gamma_0, dots, gamma_n) |-> sum_((j_0, dots, j_n))
      (phi.alt(p'_(j_0) times.o gamma_0 q'_(j_1)), phi.alt(
          p'_(j_1) times.o
          gamma_1 q'_(j_2)
        ), dots, phi.alt(p'_(j_n) times.o gamma_n q'_(j_0)))
  $
  where the sum is over all sequences $(j_0, dots, j_n)$ of integers between 1
  and $t$ inclusive.

  Using the identities satisfied by $phi.alt$ and $psi$, we see that
  $
    & beta_n compose alpha_n : (lambda_0, dots, lambda_n) |-> \
    & quad sum_((i_0, dots, i_n) \ (j_0, dots, j_n))
      (phi.alt(p'_(j_0) times.o q_(i_0)) lambda_0 phi.alt(
          p_(i_1) times.o
          q'_(j_1)
        ), dots, phi.alt(p'_(j_n) times.o q_(i_n)) lambda_n
        phi.alt(p_(i_0) times.o q'_(j_0))).
  $
  We define $h_n : Lambda^(times.o (n+1)) -> Lambda^(times.o (n+2))$ via
  $
    h_n (lambda_0, dots, lambda_n) = & sum_(m=0)^n (-1)^m
    sum_((i_0, dots, i_m) \ (j_0, dots, j_m))
    (lambda_0 phi.alt(p_(i_0) times.o q'_(j_0)), phi.alt(
        p'_(j_0) times.o
        q_(i_0)
      ) lambda_1 phi.alt(p_(i_1) times.o q'_(j_1)), \
      & dots, phi.alt(p'_(j_(m-1)) times.o q_(i_(m-1))) lambda_m
      phi.alt(p_(i_m) times.o q'_(j_m)), phi.alt(p'_(j_m) times.o q_(i_m)),
      lambda_(m+1), dots, lambda_n).
  $
  Since $sum_(i_r=1)^s sum_(j_r=1)^t phi.alt(p_(i_r) times.o q'_(j_r))
  phi.alt(p'_(j_r) times.o q_(i_r)) = 1$, it is easy to verify that
  $ 1 - beta_n compose alpha_n = b compose h_n + h_(n-1) compose b $
  so that $h$ is a chain homotopy from $beta compose alpha$ to the identity.
  Reversing the rôles of $Lambda$ and $Gamma$, we see that $alpha compose beta$
  is also homotopic to the identity.

  Since $alpha$ and $beta$ commute with the Hochschild boundary $b$, they induce
  an isomorphism on Hochschild homology by Proposition~2.3.5 of Volume~I.
  Moreover, $alpha$ and $beta$ commute with the operations $t_n$ and $b'$, and
  hence give rise to maps between $C C_* (Lambda)$ and $C C_* (Gamma)$. So we
  have a map of long exact Connes sequences
  $ #connes-ladder $
  Now arguing by induction on $n$, we see that
  $alpha_* : H C_n (Lambda) -> H C_n (Gamma)$ is an isomorphism for all
  $n >= 0$.
]

Since every other column of the double complex defining $C C_* (Lambda)$ is
contractible, with contracting homotopy $(-1)^n s_n$, we can simplify this
complex as follows. We set
$ B = (-1)^n epsilon s_n N : Lambda^(times.o (n+1)) -> Lambda^(times.o (n+2)) $
#source(96)\(which can be seen to correspond to the map $B$ in
Proposition~@prop:connes-sequence), and we write $B_* (Lambda)$#idx(
  "$B_*(Lambda)$",
) for the total complex of the following double complex.
$ #lambda-b-bicomplex $
There is an injective map of complexes $B_* (Lambda) -> C C_* (Lambda)$ given by
sending an element $x$ in degree $(i, j)$ to the sum of $x$ in degree
$(2 i, j - i)$ and $(-1)^n s_n N x$ in degree $(2 i - 1, j - i + 1)$. The
quotient complex has a filtration in which the filtered quotients are copies of
the acyclic Hochschild complex, and is hence acyclic. So the long exact sequence
in homology shows that $B_* (Lambda) -> C C_* (Lambda)$ is a homology
equivalence, and hence the cyclic homology of $Lambda$ is equal to the homology
of $B_* (Lambda)$.

Denote by $R[B]$ the algebra over the coefficient ring $R$ with one generator
$B$ satisfying $B^2 = 0$. Then the complex
$ dots.c -> R[B] limits(->)^B R[B] limits(->)^B R[B] $
is a resolution of $R$ over $R[B]$, and the above double complex can be thought
of as the tensor product over $R[B]$ of this complex and the Hochschild complex
$S_* (Lambda, Lambda)$. We thus have the following.

#proposition(closed: true)[
  $H C_* (Lambda) tilde.equiv Tor_*^(R[B]) (R, S_* (Lambda, Lambda))$.
] <prop:cyclic-tor>

Finally, we may simplify the complex $B_* (Lambda)$ further by replacing the
Hochschild complex by its normalisation. Namely, we quotient by the subcomplex
of degenerate elements (which is contractible) so that we replace
$Lambda^(times.o (n+1))$ by $macron(Lambda)^(times.o n) times.o Lambda$, where
$macron(Lambda)$ is the quotient $Lambda slash R$ of $Lambda$ by the multiples
of the identity element. Thus $B_* (Lambda)$ is chain homotopy equivalent to the
total complex $macron(B) (Lambda)$ of the following double complex.
$ #reduced-b-bicomplex $
#source(97)One has to check that the operator $B$ is well defined on the reduced
complex; this is routine.

Cyclic cohomology $H C^* (Lambda)$ is defined dually. Namely, the Hochschild
complex for computing $H H^* (Lambda) = H^* (Lambda, Lambda^*)$ is given by
$
  S^n (Lambda, Lambda^*) = Hom_R (tilde(S)_n (Lambda), Lambda^*)
  tilde.equiv Hom_R (Lambda^(times.o (n+1)), R)
  = (Lambda^(times.o (n+1)))^*.
$
Thus $t_n$ acts on $S^n (Lambda, Lambda^*)$, and we can form a double complex
$ #cohomology-bicomplex $
whose total complex is $C C^* (Lambda) = Hom_R (C C_* (Lambda), R)$. We define
the *cyclic cohomology*#idx("cohomology", "cyclic")#idx("cyclic", "cohomology")
$H C^* (Lambda)$#idx("$H C^* (Lambda)$") to be the cohomology of this complex.
Just as with cyclic homology, there is a long exact Connes sequence
$
  dots.c -> H C^(n-1) (Lambda) limits(->)^I H H^(n-1) (Lambda) limits(->)^B
  H C^(n-2) (Lambda) limits(->)^S H C^n (Lambda) limits(->)^I H H^n (Lambda)
  -> dots.c
$
and an isomorphism
$ H C^* (Lambda) tilde.equiv Ext_(R[B])^* (R, S^* (Lambda, Lambda^*)). $
