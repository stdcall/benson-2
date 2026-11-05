#import "main-defs.typ": *
#import "statements.typ": *

== Gaps in group cohomology <sec:cohomology-gaps>
#idx("gaps in cohomology", target: [@sec:cohomology-gaps])#idx(
  "cohomology",
  "gaps in",
  target: [@sec:cohomology-gaps],
)

In this and the next section, we give some examples of theorems which may be
proved using the theory of multiple complexes developed in the last section.

#source(218)Our first theorem is best stated and proved in terms of Tate
cohomology, so we begin with a quick review of this subject.

Let $G$ be a finite group and $R$ be a commutative ring of coefficients. If
$ dots.c -> P_2 -> P_1 -> P_0 $
is a projective resolution of $R$ as an $R G$-module then
$ Hom_R (P_0, R) -> Hom_R (P_1, R) -> Hom_R (P_2, R) -> dots.c $
is an exact sequence of modules which are injective relative to the trivial
subgroup, or equivalently projective (see Proposition~3.6.4 of Volume~I).
Splicing these sequences together, we obtain a doubly infinite sequence
$
  bold(P)_plus.minus : quad
  dots.c -> P_2 -> P_1 -> P_0 -> P_(-1) -> P_(-2) -> dots.c
$
where $P_(-n-1) = Hom_R (P_n, R)$. This is called a *complete resolution*#idx(
  "complete",
  "resolution",
)#idx("resolution", "complete") of $R$. The cohomology groups of the complex
$Hom_(R G) (bold(P)_plus.minus, M)$ are the Tate cohomology#idx(
  "Tate cohomology",
)#idx("cohomology", "Tate") groups $hat(H)^* (G, M)$#idx("$hat(H)^* (G, M)$").
Thus for $n > 0$ we have $hat(H)^n (G, M) tilde.equiv H^n (G, M)$. Since
$Hom_(R G) (P_(-n-1), M) tilde.equiv P_n times.o_(R G) M$, for $n > 0$ we have
$hat(H)^(-n-1) (G, M) tilde.equiv H_n (G, M)$. The group $hat(H)^0 (G, M)$ is
the quotient of $H^0 (G, M) = M^G$ by the image of $Tr_(1, G)$. In the notation
of Definition~3.6.2 of Volume~I we have $hat(H)^0 (G, M) = M^(G, 1)$. The group
$hat(H)^(-1) (G, M)$ is the dually defined submodule of
$H_0 (G, M) = R times.o_(R G) M = M slash [G, M]$.

It is easy to see that a short exact sequence of $R G$-modules
$0 -> M_0 -> M_1 -> M_2 -> 0$ gives rise to a doubly infinite long exact
sequence in Tate cohomology extending the usual long exact sequence
(Proposition~2.5.3~(ii) of Volume~I) in ordinary cohomology.

#theorem[
  Suppose $G$ is a finite group and $R$ is a commutative ring of coefficients.
  Let $bold(C)$ be the finite complex of projective $R G$-modules described in
  Corollary~@cor:finite-complex-integral (or
  Theorem~@th:multiple-complex-lattice with $M = R$). Then there is a spectral
  sequence whose $E_2$ term is given by
  $ E_2^(p q) = Hom_R (H_q (bold(C)), hat(H)^p (G, M)), $
  and which converges to zero.

  There is also a spectral sequence whose $E_2$ term is given by
  $ E_2^(p q) = Hom_R (H_q (bold(C)), H^p (G, M)), $
  and which converges to $H^* (Hom_(R G) (bold(C), M))$.
] <th:tate-spectral-sequence>

#proof[
  Let $bold(P)_plus.minus$ be a complete resolution of $R$ as an $R G$-module,
  and let $E_0^(p q)$ be the double complex
  $Hom_(R G) (bold(P)_plus.minus times.o bold(C), M)$, with horizontal
  differential $d_1$ coming from $bold(P)_plus.minus$ and vertical differential
  $d_0$ coming from $bold(C)$. If we look at the spectral sequence in which
  $d_1$ is performed first, we see that since $C_i$ is projective, each row is a
  split exact sequence of projectives, and so $E_1$ is zero. Thus the cohomology
  of the total complex is zero, and so the spectral sequence in which $d_0$ is
  performed first also converges to zero. In the latter spectral sequence we
  have
  $
    E_1^(p q) tilde.equiv
    Hom_(R G) (bold(P)_plus.minus times.o H_q (bold(C)), M) tilde.equiv
    Hom_R (H_q (bold(C)), Hom_(R G) (bold(P)_plus.minus, M))
  $
  #source(219)since $H_q (bold(C))$ is a direct sum of copies of $R$ with
  trivial $G$-action. Now the horizontal differential is the one induced by the
  boundary map on $bold(P)_plus.minus$, and so $E_2$ is as given.

  If instead of a complete resolution $bold(P)_plus.minus$ we use a projective
  resolution $bold(P)$ of $R$ as an $R G$-module, then the spectral sequence in
  which $d_1$ is performed first has $E_1 = Hom_(R G) (bold(C), M)$ concentrated
  along the vertical axis and $E_2 = E_infinity = H^* (Hom_(R G) (bold(C), M))$.
  The spectral sequence in which $d_0$ is performed first has
  $ E_1 tilde.equiv Hom_R (H_q (bold(C)), Hom_(R G) (bold(P), M)) $
  and $E_2$ as given.
]

#theorem[
  #statement-comment[[@bib:Benson1990a]] Given a finite group $G$, there exists
  a positive integer $r$ such that for any commutative ring $R$ of coefficients
  and any $R G$-module $M$, if $hat(H)^n (G, M) = 0$ for $r + 1$ consecutive
  values of $n$, then $hat(H)^n (G, M) = 0$ for all $n$, positive and negative.
] <th:cohomology-gaps>

#proof[
  We first prove this in the case where $M$ is projective as an $R$-module. Let
  $bold(C)$ be the finite complex of projective $R G$-modules described in
  Corollary~@cor:finite-complex-integral, and let $r$ be its length, so that
  $bold(C)$ has the form
  $ 0 -> C_r -> dots.c -> C_1 -> C_0 -> 0. $
  Then $H_r (bold(C)) tilde.equiv H_0 (bold(C)) tilde.equiv R$, and so the top
  and bottom rows of the spectral sequence described in the above theorem have
  the form
  $ E_2^(n r) tilde.equiv E_2^(n 0) tilde.equiv hat(H)^n (G, M). $
  Suppose that $hat(H)^n (G, M)$ is not always zero, but is zero for $r + 1$
  consecutive values of $n$, say $m, m + 1, dots, m + r$, with either
  $hat(H)^(m-1) (G, M)$ or $hat(H)^(m+r+1) (G, M)$ non-zero. Thus either
  $E_2^(m-1, r) != 0$ or $E_2^(m+r+1, 0) != 0$. However, $E_2^(p q) = 0$ for
  $m <= p <= m + r$. The differential $d_k$ on the $E_k$ page takes $E_k^(p q)$
  to $E_k^(p+k, q-k+1)$, and $d_k = 0$ for $k > r + 1$. So whichever of
  $E_2^(m-1, r)$ or $E_2^(m+r+1, 0)$ is non-zero, this group can never be killed
  at any stage in the spectral sequence. This contradicts the fact that the
  spectral sequence converges to zero.

  We now deal with the general case where $M$ is not necessarily projective as
  an $R$-module. In this case, we first remark that since $hat(H)^n (G, M)$ does
  not change when the coefficient ring $R$ is replaced by $ZZ$ (cf. the remark
  after Definition~2.4.4 in Volume~I), we may as well assume $R$ is $ZZ$. Note
  at this stage that we have not assumed that $M$ is finitely generated. Now if
  $ 0 -> M' -> F -> M -> 0 $
  is a short exact sequence with $F$ a free $ZZ G$-module, then $M'$ is
  $ZZ$-free. Since $hat(H)^n (G, F) = 0$, we have
  $hat(H)^n (G, M) tilde.equiv hat(H)^(n+1) (G, M')$ and so the theorem for $M$
  follows from the theorem for $M'$.
]
