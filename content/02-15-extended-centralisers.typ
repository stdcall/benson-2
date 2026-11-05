#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/02-15-extended-centralisers.typ": extended-pushout

== Extended centralisers <sec:extended-centralisers>

In the last section, we saw that
$ H C_* (R G) tilde.equiv H_* (E S^1 times_(S^1) L B G; R). $
In this section, we decompose the latter as a direct sum over conjugacy classes
of ordinary group cohomology of extended centralisers. Dually in cohomology we
obtain a direct product decomposition.

#definition[
  Suppose $g$ is an element of a (discrete) group $G$. The *extended
  centraliser*#idx("extended centraliser")#idx("centraliser", "extended")
  $hat(C)_G (g)$#idx("$hat(C)_G (g)$") is the topological group defined by the
  pushout diagram
  $ #extended-pushout $
  In other words, $hat(C)_G (g) = (RR times C_G (g)) slash tilde$ where $tilde$
  is the equivalence relation given by $(lambda, g x) tilde (lambda + 1, x)$.
] <def:extended-centraliser>

Thus $hat(C)_G (g) slash C_G (g) tilde.equiv RR slash ZZ = S^1$, and so by
Theorem~@th:classifying-fibrations[(ii)] there is a fibration
$B C_G (g) -> B hat(C)_G (g)$ with fibre $S^1$.

#theorem[
  #source(103)$display(
    E S^1 times_(S^1) L B G = union.big_(g in_G G) B hat(C)_G (g).
  )$
] <th:extended-centraliser-decomposition>

#proof[
  As in the proof of Lemma~@lem:free-loops-borel, we let $Y$ denote the space of
  maps $I -> E G$ such that the images of the two endpoints 0 and 1 are in the
  same $G$-orbit. Recall that $G$ acts freely on $Y$ with quotient
  $Y slash G = L B G$.

  We can write $Y$ as a disjoint union over elements $g in G$ of spaces $Y_g$,
  where $Y_g$ is the subspace consisting of maps $f : I -> E G$ with
  $f(0) g = f(1)$. The action of an element $h in G$ takes $Y_g$ to
  $Y_(h^(-1) g h)$, and so $L B G = Y slash G$ is a disjoint union over
  conjugacy classes of $g in G$ of the spaces $Y_g slash C_G (g)$. Each $Y_g$ is
  contractible, and $C_G (g)$ acts freely on it.

  Given a map $f : I -> E G$ in $Y_g$, we can extend to a map
  $tilde(f) : RR -> E G$ as follows. If $lambda in RR$ is equal to $n + t$ with
  $n in ZZ$ and $0 <= t <= 1$, we set $tilde(f) (lambda) = f(t) g^n$. It is
  easily seen that this definition "matches up" at the integers to give a
  continuous map.

  The action of $S^1$ on $L B G$ preserves the connected components
  $Y_g slash C_G (g)$, and lifts to an action of $RR$ on $Y_g$, given by
  $(lambda . tilde(f))(mu) = tilde(f) (lambda + mu)$ for $lambda$, $mu in RR$.
  Thus $RR times C_G (g)$ acts on $E S^1 times Y_g$, by letting $RR$ act on
  $E S^1$ via the map $RR -> RR slash ZZ = S^1$ and on $Y_g$ as above, and
  $C_G (g)$ act trivially on $E S^1$ and freely on $Y_g$ as above. Now $1 in RR$
  acts in the same way as $g in C_G (g)$, so that this passes down to an action
  of $hat(C)_G (g)$ on $E S^1 times Y_g$, which can be seen to be free. Thus we
  can use $E S^1 times Y_g$ as our model for $E hat(C)_G (g)$, so that the
  quotient is
  $
    E S^1 times_(S^1) (Y_g slash C_G (g)) = (E S^1 times Y_g) slash hat(C)_G (g)
    = B hat(C)_G (g).
  $
]

#corollary[
  + $display(H C_* (R G) = plus.o.big_(g in_G G) H_* (B hat(C)_G (g); R).)$
  + $display(H C^* (R G) = product_(g in_G G) H^* (B hat(C)_G (g); R).)$
] <cor:cyclic-extended-centralisers>

#proof[
  This follows from Corollary~@cor:cyclic-group-ring and the above theorem.
]

We can now define the *Chern map*#idx("Chern", "map in algebraic K-theory")#idx(
  "map",
  "Chern",
) $Ch_(n,r) : K_n (Lambda) -> H C_(n+2r) (Lambda)$ ($r >= 0$) of Connes and
Karoubi [@bib:Karoubi1983a, @bib:Karoubi1983b, @bib:Karoubi1983c]. Recall that
we defined the Dennis trace map#idx("Dennis trace map")#idx(
  "map",
  "Dennis trace",
)#idx("trace map, Dennis") at the end of Section~@sec:hochschild as a composite
of maps, one of which was the map
$ H_n (GL(Lambda), ZZ) -> H H_n (ZZ GL(Lambda)) $
which embeds the left hand side as the summand of the right hand side
corresponding to the identity element in the decomposition of
Theorem~@th:hochschild-group-algebra. Now according to the above discussion, the
summand of $H C_n (ZZ GL(Lambda))$ corresponding to the centraliser of the
identity element is
$
  H_n (S^1 times GL(Lambda), ZZ)
  = H_n (GL(Lambda), ZZ) plus.o H_(n-2) (GL(Lambda), ZZ) plus.o dots.c
$
#source(104)\(Recall that $H_n (S^1, ZZ) = H_n (CC P^infinity; ZZ)$ is
isomorphic to $ZZ$ for $n$ even and is zero for $n$ odd). Thus there is an
obvious map
$ H_n (GL(Lambda), ZZ) -> H C_(n+2r) (ZZ GL(Lambda)) $
for each value of $r >= 0$ (related by composition with the $S$ operator in the
long exact Connes sequence). The Chern map $Ch_(n,r)$ is defined to be the
composite
$
  K_n (Lambda) limits(arrow.r.long)^"Hurewicz" H_n (GL(Lambda), ZZ)
  -> H C_(n+2r) (ZZ GL(Lambda)) -> H C_(n+2r) (Lambda).
$
The map $H C_(n+2r) (ZZ GL(Lambda)) -> H C_(n+2r) (Lambda)$ is defined in a
manner analogous to the map in Hochschild homology described at the end of
Section~@sec:hochschild.
