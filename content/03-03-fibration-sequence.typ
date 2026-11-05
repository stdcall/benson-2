#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-03-fibration-sequence.typ": (
  cellular-differential, simplex-lift,
)

== The spectral sequence of a fibration <sec:fibration-sequence>
#idx(
  "spectral sequence",
  "of a fibration",
  target: [@sec:fibration-sequence],
)#idx("fibration", "spectral sequence of", target: [@sec:fibration-sequence])

In this section we give a sketchy derivation of the spectral sequence of a
fibration. Again, we shall work in cohomology rather than homology, and leave
the reader to dualise.

Suppose $p : E -> B$ is a Serre fibration with $B$ a CW-complex, and fibre
$F = p^(-1) (b_0)$ where $b_0$ is the basepoint of $B$. For the purpose of
exposition, we shall assume that $pi_1 (B)$ acts trivially on $H^* (F)$ (see
Proposition~@prop:fibre-transport), and then make comments on what to do in the
general situation.

Let
$ B^0 subset.eq B^1 subset.eq dots.c subset.eq B $
be the skeletal filtration of $B$, and let $E^i = p^(-1) (B^i)$ be the
corresponding filtration of $E$. We examine the spectral sequence arising from
this filtration.

According to the definitions, we have $E_1^(p q) = H^(p+q) (E^p, E^(p-1))$. Now
for each $p$-cell $sigma_alpha^p$ of $B$, we choose a simplex $Delta_alpha$
contained in the interior of $sigma_alpha^p$, and by excision we have
$
  H^(p+q) (E^p, E^(p-1)) tilde.equiv
  plus.o.big_alpha H^(p+q) (p^(-1) (Delta_alpha), p^(-1) (dot(Delta)_alpha)).
$
We choose a path $omega : I -> B$ with $omega(0) = b_0$ and
$omega(1) in Delta_alpha$, and let $Delta_alpha or I$ be the space obtained by
identifying $1 in I$ with $omega(1) in Delta_alpha$. Then the diagram
$ #simplex-lift $
#source(117)and Proposition~@prop:fibre-transport show that we may find a map
$Delta_alpha times F -> E$ which is a homotopy equivalence on each fibre over
$Delta_alpha$, and hence
$
  H^(p+q) (p^(-1) (Delta_alpha), p^(-1) (dot(Delta)_alpha)) tilde.equiv
  H^(p+q) (Delta_alpha times F, dot(Delta)_alpha times F) tilde.equiv H^q (F)
$
(by the Künneth theorem). Under the assumption that $pi_1 (B)$ acts trivially on
$H^* (F)$, this isomorphism is independent of choice of $omega$, and so we have
a canonical isomorphism
$
  E_1^(p q) = H^(p+q) (E^p, E^(p-1)) tilde.equiv
  Hom(H_p (B^p, B^(p-1)), H^q (F)) tilde.equiv C^p (B; H^q (F))
$
where $C^p (B; A)$ denotes the cellular cochains on $B$ with coefficients in an
abelian group $A$, namely $Hom(C_p (B), A)$.

#remark[
  If $pi_1 (B)$ has non-trivial action on $H^* (F)$, then we must regard the
  cohomologies of the fibres as a "local system" $bold(cal(H))^* (F)$ of
  coefficients on $B$ (cf. the discussion of local coefficient systems
  investigated in Chapter~@ch:local-coefficients) and we obtain
  $ H^(p+q) (E^p, E^(p-1)) tilde.equiv C^p (B; bold(cal(H))^q (F)), $
  cellular cochains on $B$ with coefficients in this local system.
]

Now to compute $E_2^(p q)$ we must see what $d_1$ does. We follow it through the
above isomorphisms as in the following diagram:
$ #cellular-differential $
Thus we have
$
  boxed(E_2^(p q) tilde.equiv H^p (B; H^q (F)).)
$

#remark(kind: "Remarks")[
  + Introducing a coefficient ring $R$ does not alter the arguments at all, and
    so we have a spectral sequence
    $ H^p (B; H^q (F; R)) => H^(p+q) (E; R). $
  + All the arguments work dually in homology to give a spectral sequence
    $ H_p (B; H_q (F; R)) => H_(p+q) (E; R). $
  + If $pi_1 (B)$ acts non-trivially on $H^* (F; R)$ and $H_* (F; R)$ we have to
    write the above spectral sequences as
    $
      H^p (B; bold(cal(H))^q (F; R)) => H^(p+q) (E; R), quad
      H_p (B; bold(cal(H))_q (F; R)) => H_(p+q) (E; R).
    $
  + #source(118)We saw in Theorem~@th:classifying-fibrations that a normal
    subgroup $N$ of a group $G$ gives rise to a fibration $B G -> B(G slash N)$
    with fibre $B N$, and hence we have spectral sequences
    $
      H^p (G slash N, H^q (N, R)) => H^(p+q) (G, R), quad
      H_p (G slash N, H_q (N, R)) => H_(p+q) (G, R).
    $
    We shall develop this spectral sequence algebraically in
    Section~@sec:group-extension.
]
