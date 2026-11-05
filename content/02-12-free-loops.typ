#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-12-free-loops.typ": free-loop-square

== Free loops on $B G$ <sec:free-loops>

In the last section we saw that the Hochschild (co)homology of a group algebra
is the direct sum over conjugacy classes of ordinary (co)homology of the
centralisers of elements of $G$. In this section, we interpret this in terms of
the free loop space $L B G$#idx("$L B G$").

For any space $X$, we define the free loop space#idx("free", "loop space")#idx(
  "loop",
  "free",
) $L X$ to be the space of all (unbased) maps $S^1 -> X$, with the usual
(compact-open) topology.

#lemma[
  Let the group $G$ act on the set $G$ by conjugation, and on $E G$ in the usual
  way. Denote by $E G times_G G$ the quotient space $(E G times G) slash G$.
  Then there is a natural map
  $ rho : L B G -> E G times_G G $
  which is a homotopy equivalence.
] <lem:free-loops-borel>

#proof[
  #source(90)Let $Y$ denote the space consisting of maps from the unit interval
  $I$ to $E G$ with the property that the images of the two endpoints 0 and 1
  are in the same $G$-orbit. Thus $G$ acts freely on $Y$, and the quotient is
  $Y slash G = L B G$.

  We have a map $tilde(rho) : Y -> E G times G$ given by taking a map
  $f : I -> E G$ to $(f(0), g)$, where $g$ is the unique element of $G$ with
  $f(0) g = f(1)$. This map $tilde(rho)$ is a fibration, and since $E G$ is
  contractible, it is easy to see that the fibres of $tilde(rho)$ are
  contractible. Moreover, $tilde(rho)$ commutes with the $G$-action, and so
  passes to a map
  $ rho : Y slash G = L B G -> E G times_G G. $
  Since $tilde(rho)$ induces a bijection on $G$-orbits of connected components,
  $rho$ induces a bijection on connected components. Examining the square
  $ #free-loop-square $
  on each $G$-orbit of connected components of $Y$, $tilde(rho)$ and the
  vertical maps induce isomorphisms on homotopy groups, and hence so does $rho$.
  So $rho$ is a homotopy equivalence by Whitehead's Theorem~@th:whitehead-cw.
]

#proposition[
  Hochschild (co)homology of $R G$ is the same as ordinary (co)homology of
  $L B G$ with coefficients in $R$.
] <prop:hochschild-free-loops>

#proof[
  It follows from the above lemma that
  $
    H_* (L B G; R) & tilde.equiv H_* (E G times_G G; R) \
                   & = H_* (limits(dot(union.big))_(g in_G G) B C_G (g); R)
                     = plus.o.big_(g in_G G) H_* (C_G (g), R)
  $
  so that by Theorem~@th:hochschild-group-algebra, this is the same as
  Hochschild homology of $R G$. The same argument holds in cohomology.
]

There is another approach, using simplicial sets, which does not go via the
decomposition as a sum over centralisers, and which we now describe.

We regard the acyclic Hochschild complex $S_* (R G)$ of $R G$ as the chain
complex of the simplicial $R$-module associated (in the manner described at the
end of Section~@sec:simplicial-sets) to the simplicial set $S G$#idx("$S G$")
whose $n$-simplices are symbols $g_0 times.o dots.c times.o g_(n+1)$ and with
faces and degeneracies
$
  d_i (g_0 times.o dots.c times.o g_(n+1))
  & = g_0 times.o dots.c times.o g_i g_(i+1) times.o dots.c times.o g_(n+1) \
  s_i (g_0 times.o dots.c times.o g_(n+1))
  & = g_0 times.o dots.c times.o g_i times.o 1 times.o g_(i+1) times.o dots.c
  times.o g_(n+1).
$
We let $G$ act by conjugation on $S G$
$
  g(g_0 times.o g_1 times.o dots.c times.o g_(n+1))
  = g g_0 times.o g_1 times.o dots.c times.o g_(n+1) g^(-1)
$
and $S G slash G$ is a simplicial set whose corresponding chain complex of
$R$-modules is the Hochschild complex for $R G$ with coefficients in $R G$. We
#source(91)write $g_0 times.o dots.c times.o g_n$ for the $n$-simplex in
$S G slash G$ corresponding to the $G$-orbit of
$g_0 times.o dots.c times.o g_n times.o 1$ in $S G$. Thus the face and
degeneracy maps for $S G slash G$ are given by
$
  d_i (g_0 times.o dots.c times.o g_n)
  & = g_0 times.o dots.c times.o g_i g_(i+1) times.o dots.c times.o g_n
  && quad 0 <= i <= n - 1 \
  d_n (g_0 times.o dots.c times.o g_n)
  & = g_n g_0 times.o dots.c times.o g_(n-1) \
  s_i (g_0 times.o dots.c times.o g_n)
  & = g_0 times.o dots.c times.o g_i times.o 1 times.o g_(i+1) times.o dots.c
  times.o g_n
  && quad 0 <= i <= n.
$

#proposition[
  As simplicial sets, we have
  $ Hom(S[1], N G) = S G slash G $
  where $N G$ is the nerve of $G$ regarded as a category with one object (so
  that $|N G| = B G$), and $S[1]$ is the simplicial circle.
] <prop:free-loops-simplicial>

#proof[
  Denote by $X$ the simplicial set of maps $f : Delta[1] -> N cal(C)(G)$, the
  nerve of the Cayley category#idx("Cayley category") of $G$ (see Exercise~3 in
  Section~@sec:classifying-spaces) with the property that $f(0)$ and $f(1)$ are
  in the same $G$-orbit. Thus an $n$-simplex in $X$ is a simplicial map
  $Delta[1] times Delta[n] -> N cal(C)(G)$ with endpoint conditions which we
  discuss below, and $X slash G$ is the simplicial set $Hom(S[1], N G)$. We
  shall show that $X$ is isomorphic to $S G$ as a simplicial set with
  $G$-action.

  Denote by $sigma$ and $tau$ the unique non-degenerate simplices of dimensions
  1 and $n$ in $Delta[1]$ and $Delta[n]$, and denote by $macron(s)_i sigma$ the
  simplex $(s_0)^i (s_1)^(n-i) sigma$ of $Delta[1]$, which is only
  non-degenerate in the $i$th direction. Then $Delta[1] times Delta[n]$ has
  exactly $n + 1$ non-degenerate $(n + 1)$-simplices
  $(macron(s)_i sigma, s_i tau)$, $0 <= i <= n$, and a simplicial map
  $f : Delta[1] times Delta[n] -> N cal(C)(G)$ is determined by its value on
  these simplices. Since
  $d_i (macron(s)_i sigma, s_i tau) = d_i (macron(s)_(i-1) sigma, s_(i-1) tau)$,
  the images of these simplices are related by
  $
    d_i f(macron(s)_i sigma, s_i tau)
    = d_i f(macron(s)_(i-1) sigma, s_(i-1) tau).
  $
  Moreover, the condition that $f(0)$ and $f(1)$ are in the same $G$-orbit
  reduces to the simplicial condition that $d_0 f(macron(s)_0 sigma, s_0 tau)$
  and $d_(n+1) f(macron(s)_n sigma, s_n tau)$ are in the same $G$-orbit.

  We choose the notation so that $d_(n+1) f(macron(s)_n sigma, s_n tau)$ is the
  $n$-simplex
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_n) g_0 dots g_n
  $
  in $N cal(C)(G)$ (in bar notation, Section~3.3 of Volume~I, this is
  $g_0 [g_1 | dots.c | g_n]$). Thus $f(macron(s)_n sigma, s_n tau)$ is some
  $(n + 1)$-simplex of the form
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_n) g_0 dots g_n -> alpha_(n+1)
  $
  for some value of $alpha_(n+1)$ in $G$. Since
  $d_n f(macron(s)_n sigma, s_n tau)
  = d_n f(macron(s)_(n-1) sigma, s_(n-1) tau)$, we see that
  $f(macron(s)_(n-1) sigma, s_(n-1) tau)$ is some simplex of the form
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_(n-1)) g_0 dots g_(n-1) -> alpha_n -> alpha_(n+1)
  $
  for some value of $alpha_n$. Continuing this way, we see that for suitable
  values of $alpha_i$, $1 <= i <= n + 1$, $f(macron(s)_i sigma, s_i tau)$ is a
  simplex of the form
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_i) g_0 dots g_i -> alpha_(i+1) -> dots.c
    -> alpha_(n+1).
  $
  #source(92)In particular, $d_0 f(macron(s)_0 sigma, s_0 tau)$ is of the form
  $ alpha_1 -> dots.c -> alpha_(n+1) $
  and is in the $G$-orbit of
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_n) g_0 dots g_n.
  $
  For the sake of symmetry, we choose the notation so that
  $g_(n+1)^(-1) = alpha_(n+1)$ and hence
  $alpha_i = g_(n+1)^(-1) g_n^(-1) dots g_i^(-1)$. Thus
  $d_(n+1) f(macron(s)_n sigma, s_n tau)
  = g_0 dots g_(n+1) d_0 f(macron(s)_0 sigma, s_0 tau)$.

  We have thus shown that every $n$-simplex in $X$ is a simplicial map
  $f : Delta[1] times Delta[n] -> N cal(C)(G)$ where
  $f(macron(s)_i sigma, s_i tau)$ is the $(n + 1)$-simplex
  $
    g_0 limits(arrow.r.long)^(g_1) g_0 g_1 limits(arrow.r.long)^(g_2) dots.c
    limits(arrow.r.long)^(g_i) g_0 dots g_i
    limits(arrow.r.long)^(g_i^(-1) dots g_0^(-1) g_(n+1)^(-1) dots g_(i+1)^(-1))
    g_(n+1)^(-1) dots g_(i+1)^(-1) limits(arrow.r.long)^(g_(i+1)) dots.c
    limits(arrow.r.long)^(g_n) g_(n+1)^(-1),
  $
  and it is easy to check that a map of this form does indeed define an
  $n$-simplex in $X$. The correspondence which associates the $n$-simplex
  $g_0 times.o dots.c times.o g_(n+1)$ in $S G$ to the above $n$-simplex is
  easily seen to respect the face and degeneracy maps and the $G$-action, and
  hence gives an isomorphism of simplicial sets between $Hom(S[1], N G)$ and
  $S G slash G$.
]
