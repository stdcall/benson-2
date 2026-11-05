#import "main-defs.typ": *
#import "statements.typ": *

== Steenrod operations and spectral sequences <sec:steenrod-spectral>
#idx(
  "spectral sequence",
  "Steenrod operations in",
  target: [@sec:steenrod-spectral],
)#idx(
  "Steenrod operations",
  "in spectral sequences",
  target: [@sec:steenrod-spectral],
)

When calculating cohomology of groups, one often ends up applying spectral
sequence techniques, and needing methods for determining the differentials. One
such method involves the fact that the Steenrod operations commute with the
transgressions. See Section~@sec:extraspecial for an example of an application
of this.

#theorem[
  In the Lyndon–Hochschild–Serre spectral sequence
  $ H^* (G slash N, H^* (N, FF_p)) => H^* (G, FF_p), $
  suppose that $x in E_n^(0, n-1)$ with $d_n (x) = y$ in $E_n^(n, 0)$, and
  $phi.alt$ is a Steenrod operation of degree $r$. Then $phi.alt(x)$ survives to
  $E_(n+r)^(0, n+r-1)$, and $d_(n+r) (phi.alt(x)) = phi.alt(y)$ in
  $E_(n+r)^(n+r, 0)$.
] <th:steenrod-transgression>

#proof[
  This theorem is proved in the context of Steenrod operations in the cohomology
  of topological spaces in Serre [@bib:Serre1951], Section~II.9~c. Namely, if
  $F -> E -> B$ is a fibration, then in the spectral sequence
  $ H^* (B; H^* (F; FF_p)) => H^* (E; FF_p) $
  the transgression#idx("transgression") $d_n : E_n^(0, n-1) -> E_n^(n, 0)$ has
  the following description. If $x in H^(n-1) (F; FF_p)$ survives to give an
  element of $E_n^(0, n-1)$, then it is the image of an #source(163)element
  $hat(x)$ under the boundary homomorphism
  $ partial : H^n (E, F; FF_p) -> H^(n-1) (F; FF_p). $
  All such choices of $hat(x)$ have the same image $pi_* (hat(x))$ under the
  projection map
  $ pi_* : H^n (E, F; FF_p) -> H^n (B; FF_p). $
  The element $pi_* (hat(x))$ survives to $E_n^(n, 0)$, and is equal to
  $d_n (x)$. Since the Steenrod operations commute with both $partial$ and
  $pi_*$, the theorem follows.

  To prove the theorem in the cohomology of groups, one can simply notice that
  this is a special case of the spectral sequence of a fibration (Remark~(iv) at
  the end of Section~@sec:fibration-sequence). Alternatively, to provide an
  algebraic proof, one must introduce the relative version of group cohomology
  corresponding to $H^* (E, F; FF_p)$. This is not the same as the relative
  cohomology introduced in Section~3.9 of Volume~I, and has less interesting
  algebraic properties, but it is not hard to describe algebraically. One then
  introduces Steenrod operations into this relative theory in the same way as in
  Section~@sec:steenrod-operations, and the proof carries over verbatim.
]

If $p$ is odd, there is also an internal differential which may be calculated in
a similar way. Namely, if $x in E_(2n+1)^(0, 2n)$ with $d_(2n+1) (x) = y$ in
$E_(2n+1)^(2n+1, 0)$, then since $d_(2n+1)$ is a derivation we have
$d_(2n+1) (x^j) = j x^(j-1) y$. In particular,
$d_(2n+1) (x^p) = p x^(p-1) y = 0$, and the above theorem states that
$x^p = P^n (x)$ survives to $E_(2n p+1)^(0, 2n p)$ and
$d_(2n p+1) (x^p) = P^n (y)$ in $E_(2n p+1)^(2n p+1, 0)$. Kudo's transgression
theorem#idx("Kudo transgression theorem")#idx(
  "theorem",
  "Kudo transgression",
)#idx("transgression", "theorem, Kudo") [@bib:Kudo1956] states that the element
$x^(p-1) y$, which failed to get hit by $d_(2n+1)$, also survives to
$E_(2n(p-1)+1)^(2n+1, 2n(p-1))$ (draw a picture), and
$ d_(2n(p-1)+1) (x^(p-1) y) = -beta P^n (y) in E_(2n(p-1)+1)^(2n p+2, 0). $

Further information about how Steenrod operations fit into spectral sequences
can be found in Araki [@bib:Araki1957a, @bib:Araki1957b], Sawka
[@bib:Sawka1982], Singer [@bib:Singer1973a, @bib:Singer1973b], among others.

Turning now to the Eilenberg–Moore spectral sequence, we recall from
Section~@sec:eilenberg-moore that given a central extension
$1 -> Z -> G -> G slash Z -> 1$, there is a spectral sequence
$
  Tor_(H^* (K(Z, 2)))^(**) (H^* ("point"), H^* (G slash Z)) => H^* (G).
$
In case $Z = ZZ slash 2$, we have
$ H^* (K(ZZ slash 2, 2), FF_2) = FF_2 [u_0, u_1, dots], $
a polynomial ring in variables $u_i$ of degree $2^i + 1$. We have
$Sq^(2^i) u_i = u_(i+1)$, and the ring homomorphism
$ FF_2 [u_0, u_1, dots] -> H^* (G slash Z, FF_2) $
sends $u_0$ to the element $zeta$ of $H^2 (G slash Z, FF_2)$ classifying the
central extension (Section~3.7 of Volume~I) and
$ u_i |-> Sq^(2^(i-1)) Sq^(2^(i-2)) dots.c Sq^1 zeta. $
#source(164)Thus in the $E_2$ page of the Eilenberg–Moore spectral sequence, all
the differentials determined by the transgressions in the
Lyndon–Hochschild–Serre spectral sequence have already happened. So one expects
the Eilenberg–Moore spectral sequence to converge much more rapidly than the
Lyndon–Hochschild–Serre spectral sequence. For an example, see the exercise at
the end of Section~@sec:extraspecial.
