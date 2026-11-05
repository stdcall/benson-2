#import "main-defs.typ": *
#import "statements.typ": *

== Isomorphisms in group cohomology <sec:cohomology-isomorphisms>

#source(220)As an application of the theorem of the last section, we present a
modified version due to Serge Bouc (private communication) of an algebraic proof
by Benson and Evens [@bib:Benson1990b] that if a homomorphism of finite groups
induces an isomorphism in integral cohomology then it is a group isomorphism.
This was first proved by Evens (unpublished, but announced in [@bib:Evens1961])
by embedding $G$ into a compact unitary group as in the remark after
Corollary~@cor:finite-complex-integral; Jackowski [@bib:Jackowski1978]
independently found a similar proof. A related but much harder theorem of Mislin
[@bib:Mislin1990] gives a group theoretic characterisation of the homomorphisms
of finite groups which induce an isomorphism in mod $p$ cohomology.

#theorem[
  Let $phi.alt : G' -> G$ be a homomorphism of finite groups. If
  $ phi.alt^* : H^* (G, ZZ) -> H^* (G', ZZ) $
  is an isomorphism, then $phi.alt$ is an isomorphism.
] <th:cohomology-isomorphism>

#proof[
  We begin by proving that if $phi.alt$ is surjective, with kernel $N$, and
  $phi.alt^*$ is an epimorphism, then $phi.alt$ is an isomorphism. In this case,
  $phi.alt^*$ is the inflation map, which is the horizontal edge homomorphism
  for the Lyndon–Hochschild–Serre spectral sequence for the extension
  $ 1 -> N -> G' -> G -> 1. $
  If this is an epimorphism, it follows that the $E_infinity$ page of this
  spectral sequence is concentrated along the horizontal axis, and so the
  vertical edge homomorphism is zero in positive degrees. Thus the restriction
  map from $H^* (G', ZZ)$ to $H^* (N, ZZ)$ is zero in positive degrees.
  Theorem~@th:cohomology-nonvanishing shows that if $g != 1$ is an element of
  $N$ then the restriction map from $H^* (G', ZZ)$ to
  $H^* (chevron.l g chevron.r, ZZ)$ is non-zero in some positive degree, so it
  follows from this that $N = 1$, and $phi.alt$ is an isomorphism.

  Since a general homomorphism can be factored as the composite of a surjective
  and an injective group homomorphism, it follows from what we have just proved,
  that $phi.alt$ is injective. So we regard $G'$ as a subgroup of $G$ via
  $phi.alt$. Consider the map $ZZ -> ZZ_(G') up^G$ given by sending $1$ to
  $sum_(g in G slash G') g times.o 1$. Write $M$ for the cokernel, so that we
  have a short exact sequence of $ZZ G$-modules
  $ 0 -> ZZ -> ZZ_(G') up^G -> M -> 0. $
  According to the exercise at the end of Section~2.8 of Volume~I, the
  corresponding map in cohomology
  $ H^* (G, ZZ) -> H^* (G, ZZ_(G') up^G) tilde.equiv H^* (G', ZZ) $
  is the restriction map. So the long exact sequence in cohomology
  (Proposition~2.5.3(ii) of Volume~I) shows that $H^n (G, M) = 0$ for all
  $n > 0$. It now follows from Theorem~@th:cohomology-gaps that
  $hat(H)^n (G, M) = 0$ for all $n in ZZ$, so that
  $hat(H)^n (G, ZZ) tilde.equiv hat(H)^n (G', ZZ)$ for all $n in ZZ$. But
  $hat(H)^0 (G, ZZ) tilde.equiv ZZ slash |G|$, so $|G| = |G'|$ and $phi.alt$ is
  an isomorphism.
]
