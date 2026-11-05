#import "main-defs.typ": *
#import "statements.typ": *

== The Atiyah spectral sequence <sec:atiyah-sequence>
#idx("Atiyah", "spectral sequence", target: [@sec:atiyah-sequence])#idx(
  "spectral sequence",
  "Atiyah",
  target: [@sec:atiyah-sequence],
)

The Atiyah spectral sequence [@bib:Atiyah1961] is a spectral sequence going from
the cohomology of a finite group to its representation theory. It was obtained
as a particular example of the Atiyah–Hirzebruch spectral sequence, by using the
Bott Periodicity Theorem~@th:bott-periodicity and the Atiyah Completion
Theorem~@th:atiyah-completion.

The Atiyah–Hirzebruch spectral sequence#idx(
  "Atiyah",
  "–Hirzebruch spectral sequence",
)#idx("spectral sequence", "Atiyah–Hirzebruch") is a method of computing the
value of an (unreduced) generalised cohomology theory $h^*$ on a space, starting
with the ordinary cohomology of the space and the values of $h^*$ on a point.
More generally, given any Serre fibration $p : E -> B$ with $B$ a CW-complex,
and fibre $F = p^(-1) (b_0)$, we have an Atiyah–Hirzebruch spectral sequence
$ H^p (B; h^q (F)) => h^(p+q) (E). $
The special case $E = B$ gives us
$ H^p (B; h^q ("point")) => h^(p+q) (B). $

Just as in the spectral sequence of a fibration
(Section~@sec:fibration-sequence), we should either stipulate that $pi_1 (B)$
acts trivially on $h^* (F)$, which certainly happens in case $F$ is a point, or
regard $h^* (F)$ as a local system of coefficients on $B$.

The derivation of the Atiyah–Hirzebruch spectral sequence is identical to the
derivation of the spectral sequence of a fibration. Thus for example
$E_1^(p q) = C^p (B; h^q (F))$, and $d_1$ is described in exactly the same way
as before.

The Atiyah spectral sequence is the particular case of the Atiyah–Hirzebruch
spectral sequence in which $B = E = B G$ and $h^*$ is K-theory. By
Theorem~@th:atiyah-completion, $K^n (B G) = a(CC G)^and$ for $n$ even and zero
for $n$ odd. The Bott Periodicity Theorem~@th:bott-periodicity shows that
$K^n ("point") = ZZ$ for $n$ even and zero for $n$ odd. So the spectral sequence
$ H^* (B G; K^* ("point")) => K^* (B G) $
is a first and fourth quadrant spectral sequence with periodicity two in the
vertical direction, and with alternate rows $H^* (G, ZZ)$ and zero. Since every
other row is zero, the even differentials $d_(2n)$ are also zero. It is
customary to get rid of the vertical repetition, and to consider the spectral
sequence to sit along a single line
$ H^* (G, ZZ) => a(CC G)^and $
with differentials $d_3$, $d_5$, etc. increasing cohomological degree by 3, 5,
etc.

#exercise[
  Investigate the Atiyah spectral sequence for some small finite groups; for
  example, cyclic groups, the symmetric group of degree three, the dihedral and
  quaternion groups of order eight.
]
