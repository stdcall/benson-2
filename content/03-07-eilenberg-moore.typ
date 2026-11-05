#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-07-eilenberg-moore.typ": cochain-square, pullback-square

== The Eilenberg–Moore spectral sequence <sec:eilenberg-moore>
#idx(
  "Eilenberg",
  "–Moore spectral sequence",
  target: [@sec:eilenberg-moore],
)#idx(
  "spectral sequence",
  "Eilenberg–Moore",
  target: [@sec:eilenberg-moore],
)

In this section, we give an extremely condensed account of the Eilenberg–Moore
spectral sequence. For more detailed accounts, see for example Smith
[@bib:Smith1967, @bib:Smith1970] or McCleary [@bib:McCleary1985]. We shall not
make much use of this spectral sequence in the rest of this book, but as we
already pointed out in the introductory section of this chapter, it can be used
as an effective computational device for computing the cohomology of central
extensions.

Suppose we are given a pullback diagram of fibrations of CW-complexes
$ #pullback-square $
and assume for simplicity that $pi_1 (B) = 0$ and that we are working over a
field of coefficients. The complex of singular cochains $Delta^* (B)$ has a
structure of a graded algebra (multiplication corresponding to cup product,
which is associative but not commutative) with a differential $d$ satisfying
$d(a b) = d(a) b + (-1)^(deg(a)) a d(b)$. Such an object is called a
*differential graded algebra*#idx("differential", "graded algebra")#idx(
  "graded",
  "algebra, differential",
) or DGA#idx("DGA"). There is also an obvious notion of differential graded
modules over a DGA, and we have a diagram of DG modules over $Delta^* (B)$ as
follows.
$ #cochain-square $
As in Definition~@def:proper-projective-resolution, DG modules admit *proper
projective resolutions*, and it turns out that if $Q^(**) -> Delta^* (B')$ is a
proper projective resolution, there is a natural map
$
  Tot (Q^(**)) times.o_(Delta^* (B)) Delta^* (E) -> Delta^* (E')
$
#source(125)inducing an isomorphism in cohomology
$
  Tot (Tor^(**)_(Delta^* (B)) (Delta^* (B'), Delta^* (E)))
  tilde.equiv H^* (E').
$
Here, $Tor^(**)$ is defined as follows. If $M^*$ and $N^*$ are right, resp. left
DG modules over a DG algebra $Gamma$, and $P^(**) -> M^*$ is a proper projective
resolution, we define
$ Tor_Gamma^(**) (M^*, N^*) = H^* (P^(**) times.o_Gamma N^*) $
with respect to the total differential
$(d_0 + d_1) times.o 1 + (-1)^m 1 times.o d_N$. The two gradings on Tor are as
follows. The first grading is the homological grading, and the second is the
internal grading coming from the grading on the modules.

Regarding $P^(**) times.o_Gamma N^*$ as a double complex
$
  (P^(**) times.o_Gamma N^*)^(p q) = plus.o.big_(s+t=q) P^(p s)
  times.o_Gamma N^t
$
we obtain a spectral sequence
$
  E_2^(**) = Tor^(**)_(H(Gamma)) (H(M^*), H(N^*))
  => Tot (Tor_Gamma^(**) (M^*, N^*)).
$
Applying this to the above isomorphism, we obtain the Eilenberg–Moore spectral
sequence
$ Tor^(**)_(H^* (B)) (H^* (B'), H^* (E)) => H^* (E'). $
As in the case of the Künneth spectral sequence for cochain complexes, this is a
second quadrant spectral sequence. In fact, L.~Smith has shown that the
Eilenberg–Moore spectral sequence can be viewed as a kind of Künneth spectral
sequence.

Given a central extension $1 -> Z -> G -> G slash Z -> 1$, the corresponding
element of $H^2 (G slash Z, Z)$ (see Section~3.7 of Volume~I) corresponds to a
map $K(G slash Z, 1) -> K(Z, 2)$ (see Section~@sec:eilenberg-mac-lane). If we
turn this into a fibration (end of Section~@sec:fibrations), then the long exact
sequence in homotopy (Theorem~@th:fibration-long-exact-sequence) shows that the
fibre is a $K(G, 1)$, so we have a fibration
$ K(G, 1) -> K(G slash Z, 1) -> K(Z, 2), $
and hence an Eilenberg–Moore spectral sequence
$
  Tor^(**)_(H^* (K(Z, 2))) (H^* ("point"), H^* (G slash Z)) => H^* (G).
$
It is most practical to compute this in case $Z = ZZ slash 2$. Now the spectral
sequence (Section~@sec:fibration-sequence) of the path fibration (end of
Section~@sec:fibrations)
$ K(Z, 1) = Omega K(Z, 2) -> P K(Z, 2) -> K(Z, 2) $
converges to zero in degrees other than zero. Following this through, we see
that
$ H^* (K(ZZ slash 2, 2); FF_2) = FF_2 [u_0, u_1, dots], $
a polynomial ring in infinitely many variables $u_i$ of degree $2^i + 1$. To
calculate Tor, one uses a Koszul complex (see for example Serre
[@bib:Serre1965b], Section~#source(126)IV~A, or Mac~Lane [@bib:MacLane1974],
Section~VII.2). See also Section~@sec:steenrod-spectral for the rôle of the
Steenrod operations, and Rusin [@bib:Rusin1989] for explicit calculations in
this situation.
