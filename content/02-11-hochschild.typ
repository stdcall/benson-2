#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-11-hochschild.typ": matrix-trace

== Hochschild homology <sec:hochschild>

Algebraic K-theory of even quite well understood rings is extraordinarily
difficult to calculate. For example, one only knows the first few algebraic
K-groups of $ZZ$. It is therefore useful to have maps to theories which are
easier to calculate. In this section, we introduce Hochschild homology of a
ring, and define the Dennis trace map from algebraic K-theory to Hochschild
homology. In a later section, we introduce a variant of this theory, called
cyclic homology, which admits a natural map to Hochschild homology. We shall see
that there is a map called the Chern map from algebraic K-theory to cyclic
homology, whose composite with the map to Hochschild homology is the Dennis
trace map.

Throughout this section, $R$ is a commutative ring of coefficients and $Lambda$
is an $R$-algebra which is projective as an $R$-module. We first introduce the
acyclic Hochschild complex#idx("acyclic Hochschild complex"), which is a
resolution for the regular representation of $Lambda$ as a $Lambda$-bimodule
(i.e., as a $Lambda times.o_R Lambda^op$-module), and then use it to calculate
Tor and Ext of $Lambda$ with a $Lambda$-bimodule $A$. The case $A = Lambda$
gives the Hochschild homology#idx("Hochschild", "homology")#idx(
  "homology",
  "Hochschild",
) and cohomology#idx("Hochschild", "cohomology")#idx(
  "cohomology",
  "Hochschild",
) of the ring $Lambda$.

The acyclic Hochschild complex is defined as follows. We write
$S_n (Lambda)$#idx("$S_n (Lambda)$") for the left
$Lambda times.o_R Lambda^op$-module
$
  underbrace(Lambda times.o_R dots.c times.o_R Lambda, n+2 "copies") wide
  (n >= -1)
$
where $Lambda times.o Lambda^op$ acts via
$
  (mu times.o gamma^*)(lambda_0 times.o dots.c times.o lambda_(n+1))
  = (mu lambda_0) times.o lambda_1 times.o dots.c times.o lambda_n times.o
  (lambda_(n+1) gamma).
$
The differential $b'_n : S_n (Lambda) -> S_(n-1) (Lambda)$#idx("$b'_n$") is
defined via
$
  b'_n (lambda_0 times.o dots.c times.o lambda_(n+1))
  = sum_(i=0)^n (-1)^i lambda_0 times.o dots.c times.o lambda_i lambda_(i+1)
  times.o dots.c times.o lambda_(n+1).
$
It is easy to check that $b'_(n-1) compose b'_n = 0$, so that $S_* (Lambda)$ is
a chain complex. The map $s_n : S_(n-1) (Lambda) -> S_n (Lambda)$ given by
$
  s_n (lambda_0 times.o dots.c times.o lambda_n)
  = lambda_0 times.o dots.c times.o lambda_n times.o 1
$
satisfies $b'_(n+1) compose s_(n+1) - s_n compose b'_n = (-1)^(n+1) id$ so that
$(-1)^n s_n$ is a chain contraction of $S_* (Lambda)$ (see Section~2.3 of
Volume~I). It follows that $S_* (Lambda)$ is exact.

Writing $tilde(S)_n (Lambda)$#idx("$tilde(S)_n (Lambda)$") for
$
  underbrace(Lambda times.o_R dots.c times.o_R Lambda, n "copies") wide
  (n >= 0)
$
#source(86)we have an isomorphism
$
  S_n (Lambda) tilde.equiv (Lambda times.o Lambda^op) times.o
  tilde(S)_n (Lambda) \
  lambda_0 times.o dots.c times.o lambda_(n+1) <-->
  (lambda_0 times.o lambda_(n+1)^*) times.o
  (lambda_1 times.o dots.c times.o lambda_n)
$
as $Lambda times.o Lambda^op$-modules, so that since $tilde(S)_n (Lambda)$ is
$R$-projective, $S_n (Lambda)$ is a projective
$Lambda times.o Lambda^op$-module. It follows that $S_* (Lambda)$ is a
projective resolution of $Lambda$ as a $Lambda times.o Lambda^op$-module. It is
called the *acyclic Hochschild complex*#idx("acyclic Hochschild complex")#idx(
  "complex",
  "acyclic Hochschild",
)#idx("Hochschild", "complex", "acyclic").

If $A$ is a $Lambda$-bimodule, we regard it as a right
$Lambda times.o Lambda^op$-module via $a(mu times.o gamma^*) = gamma a mu$. We
then define the *Hochschild homology* $H_n (Lambda, A)$ to be the homology of
the *Hochschild complex*#idx("Hochschild", "complex")#idx(
  "complex",
  "Hochschild",
)#idx("$b_n$")
$
  (S_n (Lambda, A), b_n)
  = (A times.o_(Lambda times.o Lambda^op) S_n (Lambda), 1 times.o b'_n).
$

We have
$
  S_n (Lambda, A) = A times.o_(Lambda times.o Lambda^op) S_n (Lambda)
  & tilde.equiv A times.o_(Lambda times.o Lambda^op)
  (Lambda times.o Lambda^op) times.o_R tilde(S)_n (Lambda) \
  & tilde.equiv A times.o_R tilde(S)_n (Lambda)
$
and it is easy to check that the boundary map is given in terms of this by
$
  & b_n (a times.o lambda_1 times.o dots.c times.o lambda_n)
    = a lambda_1 times.o dots.c times.o lambda_n + \
  & sum_(i=1)^(n-1) (-1)^i a times.o lambda_1 times.o dots.c times.o
    lambda_i lambda_(i+1) times.o dots.c times.o lambda_n
    + (-1)^n lambda_n a times.o lambda_1 times.o dots.c times.o lambda_(n-1).
$

Since $S_* (Lambda)$ is a projective resolution of $Lambda$ as a
$Lambda times.o Lambda^op$-module, it follows from Section~1.13 of Volume~I that
$ H_n (Lambda, A) tilde.equiv Tor_n^(Lambda times.o Lambda^op) (A, Lambda). $

Similarly we define the *Hochschild cohomology* $H^n (Lambda, A)$ to be the
cohomology of the cochain complex
$
  S^n (Lambda, A) & = Hom_(Lambda times.o Lambda^op) (S_n (Lambda), A) \
                  & tilde.equiv Hom_(Lambda times.o Lambda^op)
                    (Lambda times.o Lambda^op times.o tilde(S)_n (Lambda), A)
                    tilde.equiv Hom_R (tilde(S)_n (Lambda), A)
$
with coboundary
$
  & (b^n f)(lambda_1, dots, lambda_(n+1))
    = lambda_1 f(lambda_2, dots, lambda_(n+1)) + \
  & quad sum_(i=1)^n (-1)^i f(lambda_1, dots, lambda_i lambda_(i+1), dots,
      lambda_(n+1)) + (-1)^(n+1) f(lambda_1, dots, lambda_n) lambda_(n+1).
$

Again using the fact that $S_n (Lambda)$ is a projective resolution of $Lambda$
as a $Lambda times.o Lambda^op$-module, we deduce that
$ H^n (Lambda, A) tilde.equiv Ext_(Lambda times.o Lambda^op)^n (Lambda, A). $

We may compare this with our previous definitions of homology and cohomology as
follows. If $Lambda$ is an augmented algebra over $R$, and $M$ is a right
$Lambda$-module, then we may regard $M$ as a $Lambda$-bimodule by making
$Lambda$ act trivially on the left via the augmentation. In this case, since
$(Lambda times.o Lambda^op) times.o tilde(S)_n (Lambda)$ #source(87)is a
projective resolution of $Lambda$ as a left $(Lambda times.o Lambda^op)$-module,
it follows that $Lambda times.o_R tilde(S)_n (Lambda)$ is a projective
resolution of $R$ as a left $Lambda$-module. So
$
  H_n (Lambda, M) tilde.equiv Tor_n^(Lambda times.o Lambda^op) (M, Lambda)
  tilde.equiv Tor_n^Lambda (M, R)
$
agrees with our previous algebraic definition of $H_n (Lambda, M)$
(Section~@sec:cohomology-overview, and Section~1.13 of Volume~I).

Similarly if $M$ is a left $Lambda$-module regarded as a $Lambda$-bimodule with
trivial right action then
$
  Hom_(Lambda times.o Lambda^op) (S_n (Lambda), M)
  tilde.equiv Hom_Lambda (Lambda times.o tilde(S)_n (Lambda), M)
$
and so
$
  H^n (Lambda, M) tilde.equiv Ext_(Lambda times.o Lambda^op)^n (Lambda, M)
  tilde.equiv Ext_Lambda^n (R, M)
$
agrees with our previous definition of $H^n (Lambda, M)$.

The advantage of the Hochschild approach is that it provides homology and
cohomology groups for an algebra without augmentation. For example, we could use
this definition for a block of a group algebra. The "natural coefficients" to
use for the Hochschild homology of a (not necessarily augmented) algebra
$Lambda$ are the $Lambda$-bimodule $Lambda$ itself, giving homology groups
$H H_n (Lambda) = H_n (Lambda, Lambda)$#idx(
  "$H H_n (Lambda)$, $H H^n (Lambda)$",
). For Hochschild cohomology, we use the $Lambda$-bimodule
$Lambda^* = Hom_R (Lambda, R)$ to obtain cohomology groups
$H H^n (Lambda) = H^n (Lambda, Lambda^*)$. It is not hard to see that the
Hochschild (co)homology of a direct sum of algebras, with these natural
coefficients, is the direct sum of the Hochschild (co)homology of the summands.

#theorem[
  Suppose that $lmodule(Lambda, P)_Gamma$ and $lmodule(Gamma, Q)_Lambda$ are
  bimodules inducing a Morita equivalence between $Lambda$ and $Gamma$ (see
  Section~2.2 of Volume~I). Then for any $Lambda$-bimodule $M$ we have
  $
    H_n (Lambda, M) tilde.equiv
    H_n (Gamma, Q times.o_Lambda M times.o_Lambda P), wide
    H^n (Lambda, M) tilde.equiv
    H^n (Gamma, Q times.o_Lambda M times.o_Lambda P).
  $
  In particular, $H H_n (Lambda) tilde.equiv H H_n (Gamma)$ and
  $H H^n (Lambda) tilde.equiv H H^n (Gamma)$.
] <th:hochschild-morita>

#proof[
  We have adjunctions
  $
    Hom_Lambda (P times.o_Gamma -, -)
    & tilde.equiv Hom_Gamma (-, Q times.o_Lambda -), \
    Hom_Lambda (-, P times.o_Gamma -)
    & tilde.equiv Hom_Gamma (Q times.o_Lambda -, -)
  $
  and hence by dimension shifting we have
  $
    Ext_Lambda^n (P times.o_Gamma -, -)
    & tilde.equiv Ext_Gamma^n (-, Q times.o_Lambda -), \
    Ext_Lambda^n (-, P times.o_Gamma -)
    & tilde.equiv Ext_Gamma^n (Q times.o_Lambda -, -).
  $
  Hence we have
  $
    #aligned-rows(
      (
        $H^n (Lambda, M)$,
        $tilde.equiv Ext_(Lambda times.o Lambda^op)^n (Lambda, M)
        = Ext_(Lambda times.o Lambda^op)^n (P times.o_Gamma Q, M)$,
      ),
      (
        $$,
        $tilde.equiv Ext_(Gamma times.o Lambda^op)^n (Q, Q times.o_Lambda M)
        tilde.equiv Ext_(Gamma times.o Gamma^op)^n
        (Gamma, Q times.o_Lambda M times.o_Lambda P)$,
      ),
      ($$, $tilde.equiv H^n (Gamma, Q times.o_Lambda M times.o_Lambda P).$),
    )
  $
  The dual proof works in homology.
]

#theorem[
  #source(88)The additive structures of the Hochschild homology and cohomology
  of a group algebra $R G$ are given by
  + $display(
      H H_n (R G) tilde.equiv plus.o.big_(g in_G G) H_n (C_G (g), R)
    )$#idx("centraliser")
  + $display(H H^n (R G) tilde.equiv product_(g in_G G) H^n (C_G (g), R).)$
] <th:hochschild-group-algebra>

#proof[
  We shall prove (ii); the argument for (i) is dual. We have
  $ H H^n (R G) tilde.equiv Ext_(R G times.o R G^op)^n (R G, R G^*). $
  Now $R G^op tilde.equiv R G$ (via $g |-> g^(-1)$, Section~3.1 of Volume~I) and
  $R G times.o R G tilde.equiv R(G times G)$. The $R(G times G)$-module
  structure on $R G$ is given by the two-sided action
  $ (g_1, g_2) : g |-> g_1 g g_2^(-1), $
  and so it is just the permutation module $R_(Delta(G)) up^(G times G)$ on the
  cosets of the diagonal
  $ Delta(G) = {(g, g) | g in G} subset.eq G times G. $
  Similarly, $R G^*$ is the coinduced module $R_(Delta(G)) Up^(G times G)$ (cf.
  Section~2.8 of Volume~I). So by the Eckmann–Shapiro Lemma (see Corollary~2.8.4
  of Volume~I) we have
  $
    H H^n (R G) & tilde.equiv Ext_(R(G times G))^n
                  (R_(Delta(G)) up^(G times G), R_(Delta(G)) Up^(G times G)) \
                & tilde.equiv Ext_(R Delta(G))^n
                  (R_(Delta(G)), R_(Delta(G)) Up^(G times G) down_(Delta(G))).
  $
  By the Mackey Decomposition Theorem (3.3.4 of Volume~I, or rather the
  appropriate analogue for not necessarily finite groups),
  $
    R_(Delta(G)) Up^(G times G) down_(Delta(G))
    tilde.equiv product_(g in_G G) R_(Delta(C_G (g))) Up^(Delta(G))
  $
  and so by another application of the Eckmann–Shapiro Lemma we obtain
  $
    H H^n (R G) & tilde.equiv product_(g in_G G)
                  Ext_(R G)^n (R, R_(C_G (g)) Up^G) \
                & tilde.equiv product_(g in_G G) Ext_(R C_G (g))^n (R, R)
                  tilde.equiv product_(g in_G G) H^n (C_G (g), R).
  $
]

The multiplicative structure of $H H^n (R G)$ given by Yoneda composition is
described in terms of the above additive decomposition in Section~2.2 of
Volume~I.

We now describe the Dennis trace map#idx("Dennis trace map")#idx(
  "map",
  "Dennis trace",
)#idx("trace map, Dennis") from algebraic K-theory to Hochschild homology. It is
the composite of the following maps. The Hurewicz map goes from
$K_n (Lambda) = pi_n (B GL(Lambda)^+)$ to
$ H_n (B GL(Lambda)^+) = H_n (B GL(Lambda)) = H_n (GL(Lambda), ZZ). $
#source(89)By Theorem~@th:hochschild-group-algebra, $H_n (GL(Lambda), ZZ)$ sits
as a summand of $H H_n (ZZ GL(Lambda))$, corresponding to the centraliser of the
identity element. The Dennis trace map is the composite#idx(
  "Hurewicz",
  "map",
)#idx("map", "Hurewicz")
$
  K_n (Lambda) limits(arrow.r.long)^"Hurewicz" H_n (GL(Lambda), ZZ)
  -> H H_n (ZZ GL(Lambda)) -> H H_n (Lambda).
$
The map
$
  H H_n (ZZ GL(Lambda)) = dirlim_r H H_n (ZZ GL_r (Lambda))
  -> H H_n (Lambda)
$
is defined as follows. The obvious maps $ZZ GL_r (Lambda) -> Mat_r (Lambda)$
induce a diagram
$ #matrix-trace $
and then we pass to the limit. The isomorphism
$H H_n (Mat_r (Lambda)) tilde.equiv H H_n (Lambda)$ comes from
Theorem~@th:hochschild-morita, since $Mat_r (Lambda)$ is Morita equivalent to
$Lambda$ via the matrix trace (cf. Section~2.2 of Volume~I).

The inclusion of $GL_r (Lambda)$ into $GL_(r+1) (Lambda)$ is defined by
$ A |-> mat(A, 0; 0, 1) $
while the inclusion of $Mat_r (Lambda)$ into $Mat_(r+1) (Lambda)$ is defined by
$ A |-> mat(A, 0; 0, 0). $
It follows that the above diagram commutes modulo the image of
$H H_n (ZZ) -> H H_n (Lambda)$, which is zero for $n > 0$.
