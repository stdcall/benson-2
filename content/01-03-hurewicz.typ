#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-03-hurewicz.typ": generator-choice, hurewicz-ladder

== The Hurewicz theorem <sec:hurewicz>

#source(21)#idx("Hurewicz", "theorem", target: [@sec:hurewicz])For an arbitrary
topological space, we have the *singular homology*#idx(
  "homology",
  "singular",
)#idx("singular", "homology") $H_p (X; R)$ with coefficients in a commutative
ring $R$, defined as the homology of the singular chain complex
$Delta_* (X, A; R) = Delta_* (X; R)\/Delta_* (A; R)$, where
$Delta_p (X; R) = Delta_p (X) times.o R$ is the free $R$-module on the singular
$p$-simplices. A singular $p$-simplex in $X$ is a (continuous) map
$Delta^p -> X$ where $Delta^p$ is a standard $p$-simplex
$
  Delta^p = {(x_0, dots, x_p) in RR^(p+1) | sum x_i = 1 "and each" x_i >= 0}.
$
For more details see for example Spanier [@bib:Spanier1966]. Similarly *singular
cohomology*#idx("cohomology", "singular")#idx("singular", "cohomology")
$H^p (X; R)$ is the cohomology of the cochain complex
$ Delta^p (X, A; R) = Delta^p (X; R)\/Delta^p (A; R), $
where $Delta^p (X; R) = Hom(Delta_p (X), R)$. In case $R = ZZ$, we write
$H_p (X)$ and $H^p (X)$.

Recall that if $(X, x_0)$ is a based space then $pi_n (X, x_0)$ is defined to be
the group of homotopy classes of maps from $(S^n, s_0)$ to $(X, x_0)$. If
$f : (S^n, s_0) -> (X, x_0)$ is such a map, then we have an induced map in
homology
$ f_* : H_n (S^n) -> H_n (X) $
which only depends on the homotopy class $[f] in pi_n (X, x_0)$. Since
$H_n (S^n) tilde.equiv ZZ$, we can define
$ h_n ([f]) = f_* (1) in H_n (X) $
to obtain a well defined map
$ h_n : pi_n (X, x_0) -> H_n (X) $
called the *Hurewicz map*#idx("Hurewicz", "map")#idx("map", "Hurewicz")#idx(
  "$h_n$",
).

Similarly if $[f] in pi_n (X, A, x_0)$, then $[f]$ is represented by a map
$ f : (D^n, S^(n-1), s_0) -> (X, A, x_0). $

This induces a map
$ f_* : H_n (D^n, S^(n-1)) -> H_n (X, A), $
and since $H_n (D^n, S^(n-1)) tilde.equiv ZZ$ we can define
$ h_n ([f]) = f_* (1) in H_n (X, A) $
to obtain a well defined Hurewicz map
$ h_n : pi_n (X, A, x_0) -> H_n (X, A). $

#proposition[
  If $n >= 1$ then $h_n : pi_n (X, x_0) -> H_n (X)$ is a group homomorphism. If
  $omega$ is a path in $X$ then $h_n (omega^* (f)) = h_n (f)$ (see
  Section~@sec:homotopy-groups for notation), so that we have a well defined map
  $h_n : pi'_n (X, x_0) -> H_n (X)$.

  If $n >= 2$ then $h_n : pi_n (X, A, x_0) -> H_n (X, A)$ is a group
  homomorphism. If $omega$ is a path in $A$ then $h_n (omega^* (f)) = h_n (f)$,
  so that we have an induced map $h_n : pi'_n (X, A, x_0) -> H_n (X, A)$.
] <prop:hurewicz-homomorphism>

#proof[
  #source(22)See Spanier [@bib:Spanier1966, Section~7.4].
]

If we wish to compare the maps $h_n$ for different values of $n$, we must choose
the identifications $H_n (S^n) tilde.equiv ZZ$ and
$H_n (D^n, S^(n-1)) tilde.equiv ZZ$ in a consistent way, since there are two
possible choices for each $n$. Since $(S^n, s_0) tilde.equiv (I^n, dot(I)^n)$
and $(D^n, S^(n-1), s_0) tilde.equiv (I^n, dot(I)^n, C^(n-1))$, we may do this
inductively as follows.
$ #generator-choice $
If $z_n$ is our choice of generator for $H_n (I^n, dot(I)^n)$ then we let
$z_(n+1) = partial_*^(-1) j_* (z_n)$.

With these choices of identifications, we have the following theorem:

#theorem[
  Given a based pair $(X, A, x_0)$ we have a commutative diagram
  $ #hurewicz-ladder $
] <th:hurewicz-diagram>

#proof[
  See Spanier [@bib:Spanier1966, Section~7.4].
]

#theorem(title: [Absolute Hurewicz theorem])[
  Suppose that $pi_i (X, x_0) = 0$ for $i < n$. Then $H_i (X) = 0$ for
  $0 < i < n$, and $h_n : pi'_n (X, x_0) -> H_n (X)$ is an isomorphism. Note
  that if $n > 1$, $pi'_n (X, x_0) = pi_n (X, x_0)$, while
  $pi'_1 (X, x_0) = pi_1 (X, x_0)\/[pi_1 (X, x_0), pi_1 (X, x_0)]$, the
  abelianisation of $pi_1 (X, x_0)$.
] <th:absolute-hurewicz>
#idx("absolute Hurewicz theorem", target: [@th:absolute-hurewicz])

#theorem(title: [Relative Hurewicz theorem])[
  Suppose that $n >= 2$, that $X$ and $A$ are path connected and
  $ pi_i (X, A, x_0) = 0 italic("for") i < n. $
  Then $H_i (X, A) = 0$ for $i < n$, and $h_n : pi'_n (X, A, x_0) -> H_n (X, A)$
  is an isomorphism.
] <th:relative-hurewicz>
#idx("relative", "Hurewicz theorem", target: [@th:relative-hurewicz])

#proof[
  The above two theorems are proved simultaneously by induction, together with a
  third theorem called the "homotopy addition theorem"#idx(
    "homotopy",
    "addition theorem",
  )#idx("theorem", "homotopy addition"). For the details, see Spanier
  [@bib:Spanier1966, Section~7.5].
]

Note that the converse of the Hurewicz theorem is false. It is not hard to
construct spaces $(X, x_0)$ with $pi_i (X, x_0)$ non-zero for infinitely many
different $i > 0$, but with $H_i (X) = 0$ for all $i > 0$. However, the
following theorem is easy to deduce from the absolute Hurewicz theorem.

#theorem(closed: true)[
  Suppose $X$ is simply connected and $H_i (X) = 0$ for $0 < i < n$. Then
  $pi_i (X, x_0) = 0$ for $0 < i < n$, and $h_n : pi_n (X, x_0) -> H_n (X)$ is
  an isomorphism.
] <th:hurewicz-converse>

#example[
  #source(23)Let $n >= 2$. Since $H_i (S^n) = 0$ for $0 < i < n$,
  $H_n (S^n) tilde.equiv ZZ$, and $pi_1 (S^n, s_0) = 0$, we have
  $pi_i (S^n, s_0) = 0$ for $i < n$ and $pi_n (S^n, s_0) tilde.equiv ZZ$. One of
  the hardest problems in algebraic topology, and one which has motivated many
  developments in the subject, is the problem of determining $pi_i (S^n, s_0)$
  for $i > n$. See for example Ravenel [@bib:Ravenel1986] for a detailed survey
  of this still unsolved problem.
]

There is also a "local" version of the Hurewicz theorem at a prime.

#theorem[
  Suppose that $k$ is a field (of characteristic zero or $p$), that $X$ is a
  path connected simple space with finitely generated homotopy groups, and that
  $k times.o_ZZ pi_i (X, x_0) = 0$ for $i < n$. Then $H_i (X; k) = 0$ for
  $0 < i < n$ and $h_n : k times.o_ZZ pi'_n (X, x_0) -> H_n (X; k)$ is an
  isomorphism.
] <th:local-hurewicz>

#proof[
  See Mosher and Tangora [@bib:Mosher1968] Chapter~10.#ed-note[The book states
    Theorem~@th:local-hurewicz without the hypotheses on $X$. It fails for
    $X = B A_4$, $k = FF_2$ and $n = 2$, where $H_2 (X; FF_2) tilde.equiv FF_2$,
    and for $X = K(ZZ slash p^infinity, 2)$, $k = FF_p$ and $n = 3$, where
    $H_3 (X; FF_p) tilde.equiv FF_p$. For the spaces above it follows from
    Theorem~@th:absolute-hurewicz applied to the localization of $X$ at $p$, or
    to its rationalization; see May and Ponto [@bib:May2012, Theorems 5.3.2 and
    6.1.2].]
]
