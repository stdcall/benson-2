#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-03-bockstein.typ": bockstein-couple, connecting-chase

== The Bockstein homomorphism <sec:bockstein>

#definition[
  The *Bockstein homomorphism*#idx("Bockstein", "homomorphism")#idx(
    "homomorphism",
    "Bockstein",
  )
  $ beta : H^r (G, FF_p) -> H^(r+1) (G, FF_p) $
  #idx("$beta$, $hat(beta)$")is the connecting homomorphism in the long exact
  sequence associated to the short exact sequence
  $ 0 -> FF_p -> ZZ slash p^2 -> FF_p -> 0 $
  of coefficients.

  Similarly,
  $ hat(beta) : H^r (G, FF_p) -> H^(r+1) (G, ZZ) $
  is the connecting homomorphism associated to the short exact sequence
  $ 0 -> ZZ limits(->)^p ZZ limits(->)^pi FF_p -> 0 $
  of coefficients.
] <def:bockstein>

#lemma[
  $beta^2 = 0 : H^r (G, FF_p) -> H^(r+2) (G, FF_p)$.
] <lem:bockstein-squared-zero>

#proof[
  We have $beta = pi_* compose hat(beta)$, and $hat(beta) compose pi_* = 0$
  since these are two adjacent maps in the long exact sequence.
]

#example[
  Let $G = ZZ slash p$, the cyclic group of order $p$. Then $H^r (G, ZZ)$ is
  isomorphic to $ZZ slash p$ for $r$ even and zero for $r$ odd (Section~3.5 of
  Volume~I). Thus by the long exact sequence,
  $ hat(beta) : H^r (G, FF_p) -> H^(r+1) (G, ZZ) $
  is an isomorphism for $r$ odd and zero for $r$ even, and hence also
  $ beta : H^r (G, FF_p) -> H^(r+1) (G, FF_p) $
  is an isomorphism for $r$ odd and zero for $r$ even.
]

It is worthwhile making explicit what the Bockstein of a degree one element of
cohomology looks like, since we shall be dealing with these a lot in the next
chapter. Since $H^1 (G, FF_p) tilde.equiv Hom(G, FF_p^+)$, an element $x$ in
degree one cohomology is always the inflation of an element
$macron(x) in H^1 (G slash H, FF_p)$, where $H$ #source(145)is the kernel of the
corresponding homomorphism $phi.alt : G -> FF_p^+$. We thus have an isomorphism
$macron(phi.alt) : G slash H -> FF_p^+$ corresponding to $macron(x)$. Now
$G slash H$ is cyclic of order $p$, and so
$beta(macron(x)) in H^2 (G slash H, FF_p) tilde.equiv
Ext^2_(FF_p (G slash H)) (FF_p, FF_p)$ is represented by the exact sequence
$ 0 -> FF_p -> FF_p (G slash H) -> FF_p (G slash H) -> FF_p -> 0 $
(cf. Corollary~3.5.4 of Volume~I). In this sequence, the first map is given by
taking $1 in FF_p$ to the sum of the group elements in $G slash H$. The second
map takes $1 in FF_p (G slash H)$ to
$1 - macron(phi.alt)^(-1) (1) in FF_p (G slash H)$, and the third map takes
$1 in FF_p (G slash H)$ to $1 in FF_p$. Inflating to $G$, we see that $beta(x)$
is represented by the sequence #symbol-display(
  "∗",
  parens: true,
  $ 0 -> FF_p -> (FF_p)_H up^G -> (FF_p)_H up^G -> FF_p -> 0. $,
) <eq:bockstein-sequence>

If $k$ is a field of characteristic $p$, then
$ H^* (G, k) tilde.equiv k times.o_(FF_p) H^* (G, FF_p) $
and we regard $H^* (G, FF_p)$ as embedded in $H^* (G, k)$ via this isomorphism.
If $M$ is a $k G$-module, then we have a natural map
$ H^* (G, k) tilde.equiv Ext^*_(k G) (k, k) -> Ext^*_(k G) (M, M) $
given by tensoring exact sequences with $M$. If $zeta in H^* (G, k)$, we write
$zeta_M$ for the image of $zeta$ under this map. Tensoring the above sequence
@eq:bockstein-sequence with $M$, we obtain a sequence
$
  beta(x)_M : quad 0 -> M limits(arrow.r.long)^eta M down_H up^G
  -> M down_H up^G limits(arrow.r.long)^(eta') M -> 0.
$

Finally, we remark that the above situation is symmetric. Namely, letting $M'$
be the cokernel of $eta$, or equivalently the kernel of $eta'$ (namely
$Omega_(G slash H) (k) times.o M = Omega_(G slash H)^(-1) (k) times.o M$), we
have an exact sequence
$ 0 -> M' -> M down_H up^G -> M down_H up^G -> M' -> 0. $
Since this sequence is obtained by tensoring $M$ with the sequence
$
  0 -> Omega_(G slash H) (k) -> k(G slash H) -> k(G slash H)
  -> Omega_(G slash H) (k) -> 0,
$
which represents $beta(x)_(Omega_(G slash H) (k))$, it is easy to see that the
above sequence represents the element
$ beta(x)_(M') in Ext^2_(k G) (M', M'). $

Over a field $k$ containing $FF_p$, we could extend the Bockstein map to a
linear map $beta : H^n (G, k) -> H^(n+1) (G, k)$, but this turns out not to be a
good thing to do. Instead, we extend semilinearly via the Frobenius map. Namely,
any element of $H^n (G, k)$ can be written as $sum_i lambda_i x_i$ with
$lambda_i in k$ and $x_i in H^n (G, FF_p)$. We then set
$ beta(sum_i lambda_i x_i) = sum_i lambda_i^p beta(x_i). $
We shall only use this for degree one elements, where it may be justified by
viewing the Bockstein $beta(x)$ as a $p$-fold Massey product
$chevron.l x, x, dots, x chevron.r$ (or just #source(146)as the cup square for
$p = 2$). In Section~@sec:rank-varieties we shall see another related
justification: this version of the Bockstein map commutes with restriction to
shifted subgroups of an elementary abelian $p$-group.#footnote[It is very easy
  to make mistakes in the discussion of the Bockstein map over fields larger
  than $FF_p$. In the first edition of this book, the Frobenius twist was
  omitted, resulting in problems for Section~@sec:rank-varieties.]

#subhead[The Bockstein spectral sequence] The Bockstein spectral sequence#idx(
  "Bockstein",
  "spectral sequence",
)#idx(
  "spectral sequence",
  "Bockstein",
) is the spectral sequence associated to the exact couple
$ #bockstein-couple $
The differential $d_1 = pi_* compose hat(beta) = beta$ is the Bockstein
homomorphism. The higher differentials in this spectral sequence are the "higher
Bocksteins"#idx("higher Bocksteins")#idx("Bockstein", "higher") $d_n = beta_n$.
The map $beta_n$ is defined on the image of
$H^r (G, ZZ slash p^n) -> H^r (G, ZZ slash p)$, and is given as follows. For
such an element, the image of the connecting map
$ hat(beta)_n : H^r (G, FF_p) -> H^(r+1) (G, ZZ slash p^n) $
associated to the short exact sequence of coefficients
$ 0 -> ZZ slash p^n -> ZZ slash p^(n+1) -> FF_p -> 0 $
lies in the image of the map
$ H^(r+1) (G, FF_p) -> H^(r+1) (G, ZZ slash p^n) $
given by the inclusion of $FF_p$ as the elements of additive order $p$ in
$ZZ slash p^n$, and so we pull back to an element of $H^(r+1) (G, FF_p)$. It is
only well defined modulo the image of $beta_(n-1)$. Thus the stage at which an
element vanishes in this spectral sequence tells us the order of the $p$-torsion
associated to this element. In particular the spectral sequence converges to
$ [H^* (G, ZZ) slash (p"-torsion")] times.o_ZZ FF_p. $
Of course, for a finite group this is zero except in degree zero.

The Bockstein spectral sequence should therefore be regarded as a tool for
comparing integral and mod $p$ cohomology.

#subhead[Multiplicative properties]

#lemma[
  The Bockstein of a cup product is given by
  $ beta(x y) = beta(x) y + (-1)^(deg(x)) x beta(y). $
] <lem:bockstein-product>

#proof[
  Let $bold(P)$ be a projective resolution of $ZZ$ as a $ZZ G$-module, and let
  $Delta : bold(P) -> bold(P) times.o bold(P)$ be a diagonal approximation (see
  Section~3.2 of Volume~I). Suppose $x$, $y in H^* (G, FF_p)$ are represented by
  cocycles $hat(x)$, $hat(y) : bold(P) -> FF_p$. Choose cochains $hat(xi)$,
  $hat(eta) : bold(P) -> ZZ slash p^2$ whose reductions modulo $p$ are $hat(x)$,
  $hat(y)$, so that #source(147)$delta hat(xi) = p . hat(beta(x))$ and
  $delta hat(eta) = p . hat(beta(y))$. We chase
  $hat(x y) = (hat(x) times.o hat(y)) compose Delta$ explicitly through the
  connecting homomorphism
  $ #connecting-chase $
  We have
  $
    delta(hat(xi eta)) & = delta(hat(xi) times.o hat(eta)) compose Delta
    = (delta hat(xi) times.o hat(eta)
      + (-1)^(deg(x)) hat(xi) times.o delta hat(eta))
    compose Delta \
    & = (p hat(beta(x)) times.o hat(eta)
      + (-1)^(deg(x)) hat(xi) times.o p hat(beta(y))) compose Delta \
    & = (hat(beta(x)) times.o p hat(eta)
      + (-1)^(deg(x)) p hat(xi) times.o hat(beta(y))) compose Delta \
    & = p((hat(beta(x) y)) + (-1)^(deg(x)) (hat(x beta(y))))
  $
  and hence
  $ beta(x y) = beta(x) y + (-1)^(deg(x)) x beta(y). $
]

What we would like to say next is that the Bockstein of a norm is a transfer.
However, there is a slight technical difficulty here for elements in odd degree.
Namely, the norm map goes from $H^r (H, FF_p)$ to $H^(n r) (G, FF_p^((r)))$,
where $FF_p^((r))$ is $FF_p$ for $r$ even and the sign representation for the
action of $G$ on the cosets of $H$ for $r$ odd. So what we really need to
consider is the _twisted Bockstein homomorphism_#idx("twisted Bockstein")#idx(
  "Bockstein",
  "twisted",
)
$ tilde(beta) : H^q (G, FF_p^((r))) -> H^(q+1) (G, FF_p^((r))) $
#idx("$tilde(beta)$")associated to the exact sequence of coefficients
$ 0 -> FF_p^((r)) -> (ZZ slash p^2)^((r)) -> FF_p^((r)) -> 0. $
Note that in case $p = 2$ this is a map on cohomology with trivial coefficients,
which does not necessarily agree with the usual Bockstein.

#lemma[
  Suppose $x in H^r (H, FF_p)$. Then the twisted Bockstein
  $ tilde(beta)(1 wreath x) in H^(n r+1) (Sigma_n wreath H, FF_p^((r))) $
  is given by the formula
  $
    tilde(beta)(1 wreath x)
    = Tr_(H times (Sigma_(n-1) wreath H), Sigma_n wreath H)
    (beta(x) times.o (1 wreath x)).
  $
] <lem:twisted-bockstein-norm>

#proof[
  Let $bold(P)$ be a projective resolution of $ZZ$ as a $ZZ H$-module. Then $x$
  is represented by a cocycle $hat(x) : P_r -> FF_p$. Choose a cochain
  $hat(xi) : P_r -> ZZ slash p^2$ whose reduction modulo $p$ is $hat(x)$. Then
  $1 wreath x$ is represented by the cocycle
  $
    1 wreath hat(x) : (bold(P)^(times.o n))_(n r) -> (P_r)^(times.o n)
    -> FF_p
  $
  which lifts to
  $ 1 wreath hat(xi) : (bold(P)^(times.o n))_(n r) -> ZZ slash p^2. $
  #source(148)We have
  $
    #aligned-rows(
      (
        $delta(1 wreath hat(xi))$,
        $= sum_(j=0)^(n-1) (-1)^(j r) hat(xi)^(times.o j) times.o delta hat(xi)
        times.o hat(xi)^(times.o (n-j-1))$,
      ),
      (
        $$,
        $= p . sum_(j=0)^(n-1) (-1)^(j r) hat(xi)^(times.o j) times.o
        hat(beta(x)) times.o hat(xi)^(times.o (n-j-1)).$,
      ),
    )
  $
  This expression differs from
  $
    p . Tr_(H times Sigma_(n-1) wreath H, Sigma_n wreath H)
    (hat(beta(x)) times.o hat(xi)^(times.o (n-1)))
  $
  by a coboundary. This completes the proof of the formula.
]

#proposition[
  If $|G : H| = n$ and $x in H^r (H, FF_p)$ then
  $
    tilde(beta) norm_(H, G) (x) in H^(n r+1) (G, FF_p^((r)))
  $
  is a transfer from $H$.
] <prop:bockstein-norm-transfer>

#proof[
  This follows from the lemma, since by the Mackey formula, the restriction to
  $G$ of a transfer from $H times Sigma_(n-1) wreath H$ to $Sigma_n wreath H$ is
  a transfer from $G inter (H times Sigma_(n-1) wreath H) = H$ to $G$.
]
