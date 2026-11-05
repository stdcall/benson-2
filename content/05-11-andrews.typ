#import "main-defs.typ": *
#import "statements.typ": *

== Andrews' theorem <sec:andrews>

#idx("Andrews' theorem", target: [@sec:andrews])#idx(
  "theorem",
  "Andrews'",
  target: [@sec:andrews],
)In the last section, we described a method for obtaining upper bounds on the
period of a periodic $k G$-module. In general, it is much harder to get lower
bounds. However, a method of Andrews [@bib:Andrews1989], which we now describe,
enables us to determine the exact period of a periodic inflated module, in
#source(205)terms of its variety as a module for the quotient. We begin with a
technical lemma.

#lemma[
  Suppose $N$ is a normal $p$-subgroup of $G$, and $M$ is a $k G$-module. Denote
  by $tilde(N)$ the sum $sum_(g in N) g$ of the elements of $N$, as an element
  of the group algebra $k N subset.eq k G$. Then $M$ has a non-zero projective
  summand as a $k G$-module if and only if $tilde(N) M$ has a non-zero
  projective summand as a $k(G slash N)$-module.
] <lem:norm-projective-summand>

#proof[
  If $M$ has a non-zero projective summand $P$ as a $k G$-module then
  $tilde(N) P$ is a non-zero projective summand of $tilde(N) M$ as a
  $k(G slash N)$-module. Conversely, suppose that $tilde(N) M$ has a non-zero
  projective summand $Q$ as a $k(G slash N)$-module. Denote by $pi$ the
  projection of $tilde(N) M$ onto $Q$, and write $pi$ as a transfer
  $pi = Tr_(1, G slash N) (alpha) = Tr_(N, G) (alpha)$,
  $alpha in End_k (tilde(N) M)$. Since $N$ is normal in $G$, the transfer map
  $Tr_(1, N)$ maps elements of $End_k (M)$ to elements preserving the submodule
  $tilde(N) M$, and gives a surjective map from $End_k (M)$ onto
  $End_k (tilde(N) M)$. So there is an element $beta in End_k (M)$ with the
  property that $Tr_(1, N) (beta)$ acts as $alpha$ on $tilde(N) M$. Thus
  $Tr_(1, G) (beta)$ acts as $pi$ on $tilde(N) M$, and so $Tr_(1, G) (beta)$ is
  a non-nilpotent $k G$-module endomorphism of $M$. So we may choose
  $phi.alt in End_(k G) (M)$ in such a way that
  $phi.alt compose Tr_(1, G) (beta)$ is a projection onto a $k G$-module summand
  of $M$. Since
  $phi.alt compose Tr_(1, G) (beta) = Tr_(1, G) (phi.alt compose beta)$, this
  summand is projective.
]

Now suppose we have a group extension
$ 1 -> N -> G -> macron(G) -> 1 $
with $N$ cyclic of order $p$. Let $epsilon = 1$ if $p = 2$ and $epsilon = 2$ if
$p$ is odd. If $M$ is a $k macron(G)$-module, regarded as a $k G$-module by
inflation, then $M down_N$ is a module with trivial action, and so $M down_N$ is
periodic with period $epsilon$. So if $M$ is periodic as a $k G$-module, then
its period is certainly divisible by $epsilon$.

Let $tilde(N)$ denote the sum $sum_(g in N) g$ of the elements of $N$, as an
element of the group algebra $k N$. Then for any $r > 0$,
$tilde(N) Omega^(epsilon r)_G (k)$ is a $k G$-module with $N$ acting trivially,
so we may regard it as a $k macron(G)$-module. We set
$
  V_r = V_(macron(G)) (tilde(N) Omega^(epsilon r)_G (k)) subset.eq
  V_(macron(G)).
$

#theorem(title: [Andrews])[
  If $M$ is a $k macron(G)$-module regarded as a $k G$-module by inflation, then
  the following are equivalent:
  + $dim_k Omega^(epsilon r)_G (M) = dim_k M$
  + $tilde(N) Omega^(epsilon r)_G (M) = 0$
  + $tilde(N) Omega^(epsilon r)_G (k) times.o M$ is a projective
    $k macron(G)$-module
  + $Omega^(epsilon r)_G (M) tilde.equiv M$
  + $V_(macron(G)) (tilde(N) Omega^(epsilon r)_G (k) times.o M) = {0}$
  + $V_r inter V_(macron(G)) (M) = {0}$.
] <th:andrews>

#proof[
  By Schanuel's lemma we have
  $
    Omega^(epsilon r)_G (M) down_N tilde.equiv
    Omega^(epsilon r)_N (M down_N) plus.o Q tilde.equiv M down_N plus.o Q
  $
  #source(206)where $Q$ is a projective $k N$-module with
  $tilde(N) Omega^(epsilon r)_G (M) = tilde(N) Q = Q^N$. Since $N$ is a
  $p$-group, $Q = 0$ if and only if $Q^N = 0$, and so (i) is equivalent to (ii).

  Since $Omega^(epsilon r)_G (M)$ has no projective summands as a $k G$-module,
  the lemma implies that $tilde(N) Omega^(epsilon r)_G (M)$ has no projective
  summands as a $k macron(G)$-module. Applying $tilde(N)$ to the isomorphism
  $
    Omega^(epsilon r)_G (k) times.o M tilde.equiv Omega^(epsilon r)_G (M)
    plus.o ("projective "k G"-module")
  $
  we obtain
  $
    tilde(N) Omega^(epsilon r)_G (k) times.o M tilde.equiv
    tilde(N) Omega^(epsilon r)_G (M) plus.o
    ("projective "k macron(G)"-module")
  $
  and so (ii) is equivalent to (iii).

  Tensoring the short exact sequence
  $
    0 -> tilde(N) Omega^(epsilon r)_G (k) -> Omega^(epsilon r)_G (k)^N -> k
    -> 0
  $
  with $M$, we see that if (iii) holds then
  $
    Omega^(epsilon r)_G (k)^N times.o M tilde.equiv M plus.o
    ("projective "k macron(G)"-module").
  $
  Since (iii) also implies that $Q = 0$ so that $N$ acts trivially on
  $Omega^(epsilon r)_G (M)$, we have
  $
    Omega^(epsilon r)_G (k)^N times.o M
    tilde.equiv (Omega^(epsilon r)_G (k) times.o M)^N
    tilde.equiv Omega^(epsilon r)_G (M) plus.o
    ("projective "k macron(G)"-module")
  $
  and hence (iii) implies (iv). It is easy to see that (iv) implies (i).

  The equivalence of (iii) and (v) and the equivalence of (v) and (vi) are given
  by Proposition~@prop:variety-dimension-complexity and
  Theorem~@th:variety-tensor-product respectively.
]

The varieties $V_r$ are completely determined in [@bib:Benson1992c].
