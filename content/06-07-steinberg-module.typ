#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/06-07-steinberg-module.typ": conlon-square

== The generalised Steinberg module <sec:steinberg-module>

#definition[
  We define the *generalised Steinberg module*#idx(
    "generalised",
    "Steinberg module",
  )#idx("module", "generalised Steinberg")#idx(
    "Steinberg module",
    "generalised",
  ) for a finite group $G$ at a prime $p$ to be#idx("$St_p (G)$")
  $ St_p (G) = tilde(L)_G (|cal(S)_p (G)|) in a(G). $
] <def:generalised-steinberg-module>

#remark(kind: "Remarks")[
  #source(239)Since
  $cal(S)_p (G) tilde.eq_G cal(A)_p (G) tilde.eq_G cal(B)_p (G)$, we could have
  used any of these complexes in the above definition.

  We shall see in the next section what this has to do with the classical
  definition of Steinberg module for a Chevalley group#idx(
    "Chevalley group",
  )#idx("group", "Chevalley").
]

#theorem(title: [Quillen, Webb])[
  The generalised Steinberg module is a virtual projective module
  $ St_p (G) in a(G, 1). $
] <th:steinberg-virtual-projective>

#proof(closed: false)[
  Since $St_p (G)$ clearly lies in $a(G)$#idx("$a(G)$"), it suffices to show
  that it lies in $A(G, 1) = CC times.o_ZZ a(G, 1)$. Recall from Section~5.6 of
  Volume~I that we have a commutative diagram
  $ #conlon-square $
  with $H$ $p$-hypo-elementary#idx("hypo-elementary group")#idx(
    "group",
    "hypo-elementary",
  ) and $g$ an element of $H slash O_p (H)$. Under the top map,
  $tilde(Lambda)_G (Delta)$ goes to the element whose $H$th coordinate is
  $tilde(chi)(Delta^H)$. Under the bottom map, the ideal $A(G, 1)$ corresponds
  to those $(H, g)$ for which $O_p (H) = 1$. Thus the theorem follows from the
  following lemma.
]

#lemma[
  Suppose that $H$ is a $p$-hypo-elementary subgroup of $G$ with $O_p (H) != 1$.
  Then $cal(S)_p (G)^H$ is conically contractible, and in particular the reduced
  Euler characteristic $tilde(chi)(cal(S)_p (G)^H) = 0$.
] <lem:hypo-elementary-conically-contractible>

#proof[
  If $P in cal(S)_p (G)^H$ then $P <= P O_p (H) >= O_p (H)$.
]

#remark(kind: "Comment")[
  The fact that the character of $St_p (G)$ is the character of a virtual
  projective module is due to Quillen [@bib:Quillen1978]. The statement that
  this alternating sum is virtual projective in the representation ring $a(G)$
  is due to Webb.
]

#corollary(title: [Ken Brown's theorem])[
  The Euler characteristic
  $ chi(cal(S)_p (G)) equiv 1 (mod |G|_p) $
] <cor:ken-brown>
#idx("Brown's theorem", target: [@cor:ken-brown])#idx(
  "theorem",
  "Brown's",
  target: [@cor:ken-brown],
)

#proof[
  The dimension of any projective module is divisible by $|G|_p$ since on
  restriction to a Sylow $p$-subgroup it must be free. But the dimension of
  $St_p (G)$ is $chi(cal(S)_p (G)) - 1$.
]

#remark[
  This statement may be thought of as analogous to the statement that the number
  of Sylow $p$-subgroups is congruent to $1 mod p$. In fact, Thévenaz has proved
  a relative version of Ken Brown's theorem of which these two statements are
  the extreme examples.
]

#example[
  It is not true that all the $tilde(H)_i (cal(S)_p (G), k)$ are necessarily
  projective. The following is an unpublished example of Alperin. Let $H$ be a
  #source(240)semidirect product of $ZZ slash q$ by $ZZ slash p$, where
  $p|(q - 1)$, $p^2 divides.not (q - 1)$, and the action is non-trivial. Let $G$
  be the wreath product of $H$ with $ZZ slash p$, so that $|G| = p^(p+1) q^p$.
  Then every elementary abelian subgroup of $G$ of order bigger than $p^2$ is
  contained in the normal subgroup $H^p$. So long as $p > 2$ the $(p - 1)$st
  homology
  $
    tilde(H)_(p-1) (cal(S)_p (G), k) tilde.equiv tilde(H)_(p-1) (
      cal(A)_p (G), k
    ) tilde.equiv tilde(H)_(p-1) (cal(A)_p (H^p), k)
  $
  has dimension $(q - 1)^p$. Since the dimension of a projective module is
  divisible by the $p$-part of $p(q - 1)^p$, this module is not projective.
]

#remark[
  This example is also discussed in Segev and Webb [@bib:Segev1994].
]
