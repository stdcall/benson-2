#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-08-simplicial-sets.typ": kan-fibration

== Simplicial sets <sec:simplicial-sets>

#source(35)In this book, I have tried wherever possible to avoid the language of
simplicial sets, in order to make the discussion as accessible as possible to a
wide audience. However, at times they are indispensable; and at times
discussions are greatly clarified when described in this language. This will be
especially true when we discuss cyclic homology in Section~@sec:free-loops.

The idea of the theory of simplicial sets is that homotopy theory really should
not depend on properties of point set topology, and ought to admit an algebraic,
or at least combinatorial description. The appropriate combinatorial framework
was first formulated by Eilenberg and Zilber [@bib:Eilenberg1950] and developed
by D.~M. Kan [@bib:Kan1955, @bib:Kan1958]; other good references are Bousfield
and Kan [@bib:Bousfield1972], May [@bib:May1967], Lamotke [@bib:Lamotke1974] and
Section~VIII.5 of Mac~Lane [@bib:MacLane1974]. We shall content ourselves with a
brief summary of the salient features of the theory, and the reader is referred
to these references for further details.

Let $triangle.stroked.t$#idx("$triangle.stroked.t$") be the category whose
objects are the finite totally ordered sets, and whose arrows are the monotonic
functions. A *simplicial object*#idx("object", "simplicial")#idx(
  "simplicial",
  "object",
) $X$ in a category $cal(C)$ is a contravariant functor
$triangle.stroked.t -> cal(C)$. A *simplicial set*#idx("set", "simplicial")#idx(
  "simplicial",
  "set",
) is a simplicial object in the category of sets. If $X$ is a simplicial object,
we write $X_n$ for the image of ${0, dots, n}$ in $cal(C)$ (the "set of
$n$-simplices"), $d_i : X_n -> X_(n-1)$#idx("$d_i$") ($0 <= i <= n$) for the
image of the $i$th "face map"#idx("face map")
$
  {0, dots, n - 1} & -> {0, dots, n} \
                 j & |-> cases(j & "if" j < i, j + 1 & "if" j >= i)
$
and $s_i : X_n -> X_(n+1)$#idx("$s_i$") ($0 <= i <= n$) for the image of the
$i$th "degeneracy map"#idx("degeneracy map")
$
  {0, dots, n + 1} & -> {0, dots, n} \
                 j & |-> cases(j & "if" j <= i, j - 1 & "if" j > i)
$
These maps satisfy the relations
$
  d_i d_j & = d_(j-1) d_i & quad & i < j \
  d_i s_j & = s_(j-1) d_i & quad & i < j \
  d_i s_j & = 1           & quad & i = j "or" j + 1 \
  d_i s_j & = s_j d_(i-1) & quad & i > j + 1 \
  s_i s_j & = s_(j+1) s_i & quad & i <= j
$
and all maps and relations coming from $triangle.stroked.t$ follow from these.
So giving a simplicial object $X$ in $cal(C)$ is the same as giving objects
$X_n$ in $cal(C)$, $0 <= n < infinity$, and maps $d_i : X_n -> X_(n-1)$ and
$s_i : X_n -> X_(n+1)$ satisfying the above relations.

A *simplicial map*#idx("map", "simplicial")#idx("simplicial", "map")
$f : X -> Y$ between simplicial objects is a natural transformation of functors;
this amounts to giving maps $f_n : X_n -> Y_n$ satisfying
$f_(n-1) d_i = d_i f_n$ and $f_(n+1) s_i = s_i f_n$ for all $0 <= i <= n$. Thus
simplicial objects in a category $cal(C)$ form a category
$bold("Simp") cal(C)$#idx("$bold(\"Simp\") cal(C)$").

#source(36)If $X$ is a simplicial set, an $n$-simplex $x in X_n$ is said to be
*degenerate*#idx("degenerate simplex")#idx("simplex", "degenerate") if
$x = s_i y$ for some $y in X_(n-1)$ and some $i$. The remaining simplices are
said to be *non-degenerate*#idx("non-degenerate", "simplex")#idx(
  "simplex",
  "non-degenerate",
). Note that because of the above relations, the maps $s_i$ are injective, so
that there are in general lots of degenerate simplices.

The relationship with topological simplices is as follows. We denote by
$Delta^n$#idx("$Delta^n$") the standard $n$-simplex
$
  Delta^n = {(x_0, dots, x_n) in RR^(n+1) | sum x_i = 1 "and each" x_i >= 0}.
$
The maps $bold(d)^i : Delta^(n-1) -> Delta^n$ and
$bold(s)^i : Delta^(n+1) -> Delta^n$ are defined by
$
  #aligned-rows(
    (
      $bold(d)^i (x_0, dots, x_(n-1))$,
      $= (x_0, dots, x_(i-1), 0, x_i, dots, x_(n-1))$,
    ),
    (
      $bold(s)^i (x_0, dots, x_(n+1))$,
      $= (x_0, dots, x_i + x_(i+1), dots, x_(n+1)).$,
    ),
  )
$
These satisfy the above relations given for the $d_i$ and $s_i$, but with the
order of composition reversed. If $X$ is a simplicial set, we define its
*topological realisation*#idx("realisation", "topological")#idx(
  "topological",
  "realisation",
) $|X|$#idx("$|X|$") to be the quotient of
$ scripts(dot(union.big))_(n >= 0) X_n times Delta^n $
by the equivalence relation given by identifying $(d_i x, y)$ with
$(x, bold(d)^i y)$ and $(s_i x, y)$ with $(x, bold(s)^i y)$. This gives a
CW-complex (not in general a simplicial complex since faces of a simplex may get
identified) with one $n$-cell for each non-degenerate $n$-simplex in $X$. The
topological standard simplex itself is the topological realisation of the
simplicial set $Delta[n]$#idx("$Delta[n]$") whose $r$-simplices are the
sequences of integers $0 <= a_0 <= dots.c <= a_r <= n$ with
$
  d_i (a_0, dots, a_r) & = (a_0, dots, a_(i-1), a_(i+1), dots, a_r) \
  s_i (a_0, dots, a_r) & = (a_0, dots, a_i, a_i, dots, a_r).
$
The maps $bold(d)^i$ and $bold(s)^i$ correspond to obvious maps
$bold(d)^i : Delta[n - 1] -> Delta[n]$ and
$bold(s)^i : Delta[n + 1] -> Delta[n]$. There is also the obvious corresponding
notion of the topological realisation of a map of simplicial sets, so that
topological realisation is a functor from simplicial sets to CW-complexes.

If $Y$ is a topological space, then the *singular simplices*#idx(
  "simplex",
  "singular",
)#idx("singular", "simplices") on $Y$ form a simplicial set $Sing(Y)$#idx(
  "$\"Sing\"(Y)$",
) with $Sing(Y)_n = Map(Delta^n, Y)$ and with maps $d_i$ and $s_i$ induced by
the maps $bold(d)^i$ and $bold(s)^i$. There is an obvious adjunction between
topological realisation and singular simplices
$
  Map(|X|, Y) limits(tilde.equiv)^"nat"
  Hom_(bold("SimpSet")) (X, Sing(Y)).
$

If $X$ and $Y$ are simplicial sets then $X times Y$ is the simplicial set with
$(X times Y)_n = X_n times Y_n$ with the obvious face and degeneracy maps. This
definition takes a bit of getting used to, because a product of degenerate
simplices may be non-degenerate. This is related to the topological product by
$ |X times Y| = |X| times |Y|, $
#source(37)where the product on the right is taken in the category of compactly
generated spaces (the usual topology of the product is wrong for infinite
dimensional spaces). For example, taking $X = Y = Delta[1]$ (the "simplicial
unit interval"), $X times Y$ has four zero-simplices $(0, 0)$, $(0, 1)$,
$(1, 0)$, $(1, 1)$, five non-degenerate one-simplices $(00, 01)$, $(01, 00)$,
$(01, 01)$, $(01, 11)$ and $(11, 01)$, and two non-degenerate two-simplices
$(001, 011)$ and $(011, 001)$. Thus $|X times Y|$ is a unit square, triangulated
by cutting into two triangles using the diagonal. A proof of the fact that
products commute with topological realisation can be found in Chapter~III of May
[@bib:May1967].

The (reduced) *suspension*#idx("suspension") $S X$ of a pointed simplicial set
$(X, x_0)$ is the simplicial set with one zero-simplex $*$, and whose
$n$-simplices for $n > 0$ are the pairs $(i, x)$, $i >= 1$, $x in X_(n-i)$,
modulo the equivalence relation $(i, s_0^n x_0) tilde s_0^(n+i) *$. The face and
degeneracy maps are determined by the relations
$
      d_0 (1, x) & = s_0^(n-1) * &     quad s_0 (i, x) & = (i + 1, x) \
  d_(i+1) (1, x) & = (1, d_i x)  & quad s_(i+1) (1, x) & = (1, s_i x).
$
It is easy to check that this is related to the usual reduced suspension
(Section~@sec:homotopy-groups) by $|S X| = S|X|$.

The simplicial version of the space of maps from one space to another goes as
follows. If $X$ and $Y$ are simplicial sets, then $Hom(X, Y)$ is the simplicial
set in which an $n$-simplex is a simplicial map $f : X times Delta[n] -> Y$,
with face and degeneracy maps given by composition
$d_i (f) = f compose (id_X times bold(d)^i)$ and
$s_i (f) = f compose (id_X times bold(s)^i)$. The realisation of an $n$-simplex
$f : X times Delta[n] -> Y$ gives a map $|X| times Delta^n -> |Y|$ and hence a
map $Delta^n -> Map(|X|, |Y|)$. Putting these together gives a map
$ abs(Hom(X, Y)) -> Map(|X|, |Y|) $
which is a weak homotopy equivalence if $Y$ is a Kan complex, and a homotopy
equivalence if moreover $X$ is finite.

The notion of a fibration in $bold("SimpSet")$ is similar to that of a Serre
fibration in the topological category. Let $Delta[n, i]$ be the simplicial
subset of $Delta[n]$ generated by all except the $i$th face; in other words, if
$sigma$ is the unique non-degenerate $n$-simplex in $Delta[n]$ then
$Delta[n, i]$ is generated by $d_0 sigma, dots, d_(i-1) sigma$,
$d_(i+1) sigma, dots, d_n sigma$. Thus the topological realisation
$Delta^(n, i)$ of $Delta[n, i]$ is the subset of $Delta^n$ consisting of those
$(x_0, dots, x_n)$ such that $x_j = 0$ for some $j != i$. One can show that a
map of topological spaces is a Serre fibration if and only if it has the lifting
property with respect to the pair $(Delta^n, Delta^(n, i))$. So we define a map
$E -> B$ of simplicial sets to be a *Kan fibration*#idx(
  "fibration",
  "Kan",
)#idx("Kan", "fibration") if the diagonal arrow can always be filled in, as in
the following diagram:
$ #kan-fibration $
#source(38)A number of remarks need to be made at this point. First of all, in
contrast to the situation in topology, if we denote by $*$ the simplicial set
with one $n$-simplex for each $n$ (so that the topological realisation of $*$ is
a single point), given a simplicial set $X$, the (unique) map $X -> *$ is not
necessarily a Kan fibration. A simplicial set is called a *Kan complex*#idx(
  "complex",
  "Kan",
)#idx("Kan", "complex") if $X -> *$ is a fibration. However, if $X$ is (the
underlying simplicial set of) a simplicial group#idx("group", "simplicial")#idx(
  "simplicial",
  "group",
), then $X$ is necessarily a Kan complex (see for example May [@bib:May1967],
Theorem~17.1). If $E -> B$ is a Serre fibration of topological spaces, then
$Sing(E) -> Sing(B)$ is a Kan fibration, as can easily be seen using the
adjunction between singular simplices and topological realisation. Thus for any
topological space $Y$, $Sing(Y)$ is a Kan complex. In particular, the functor
$X |-> Sing(|X|)$ provides a canonical way of turning simplicial sets into Kan
complexes. There is also a combinatorial construction of such a functor
$X |-> Ex^infinity (X)$ constructed by Kan [@bib:Kan1957].

If $f, f' : X -> Y$ are simplicial maps from one simplicial set to another, then
a homotopy from $f$ to $f'$ is a simplicial map $F : X times Delta[1] -> Y$ with
the property that $F compose (id_X times bold(d)^0) = f$ and
$F compose (id_X times bold(d)^1) = f'$. As long as $Y$ is a Kan complex,
homotopy is an equivalence relation on maps from $X$ to $Y$. The topological
realisation of a homotopy between simplicial maps is a homotopy between maps of
CW-complexes. We write $[X; Y]$ for the homotopy classes of maps from $X$ to $Y$
when $Y$ is a Kan complex. There are also obvious notions of homotopy classes of
pointed maps $[X, x_0; Y, y_0]$, where $x_0$ and $y_0$ are zero-simplices, and
of maps between pairs $[X, A, x_0; Y, B, y_0]$.

#theorem[
  The adjunction between the singular simplices functor and the topological
  realisation functor passes down to an equivalence of categories between
  CW-complexes and homotopy classes of maps, and Kan complexes and homotopy
  classes of simplicial maps.
] <th:simplicial-equivalence>

#proof[
  See May [@bib:May1967] Chapter~III §16, or Bousfield and Kan
  [@bib:Bousfield1972] Chapter~VIII §4.
]

This theorem says that we can do homotopy theory in the category of simplicial
sets, without reference to topological spaces. For example, we give the
simplicial definition of homotopy groups.

The simplicial $n$-sphere#idx("simplicial", "$n$-sphere") $S[n]$#idx("$S[n]$")
is the unique simplicial set with one non-degenerate zero-simplex $*$, one
non-degenerate $n$-simplex, and no other non-degenerate simplices. Thus
$|S[n]| = S^n$ (the $n$-sphere is obtained from $Delta^n$ by identifying the
boundary to a point). So if $X$ is a Kan complex, we define
$pi_n (X, x_0) = [S[n], *; X, x_0]$. Now a map from $(S[n], *)$ to $(X, x_0)$
consists of an $n$-simplex in $X$ with the property that each face map gives the
fully degenerate $(n - 1)$-simplex $s_0^(n-1) (x_0)$. Therefore $pi_n (X, x_0)$
consists of equivalence classes of certain $n$-simplices in $X$ under an
equivalence relation which the reader is invited to write down explicitly in
terms of the existence of an $(n + 1)$-simplex with certain properties.

#source(39)Finally, we discuss the homology of a simplicial set with
coefficients in a commutative ring $R$. If $X$ is a simplicial set, regarded as
a contravariant functor $triangle.stroked.t -> bold("Set")$, then we may compose
with the free module functor $bold("Set") -> lmodule(R, bold("Mod"))$ to get a
simplicial $R$-module $R X$. The chain complex of a simplicial $R$-module $M$ is
the chain complex of $R$-modules with $M_n$ in degree $n$ and boundary map
$partial_n = sum_(i=0)^n (-1)^i d_i : M_n -> M_(n-1)$. Note that the subcomplex
of degenerate simplices is contractible, since the degeneracies can be
interpreted as contracting homotopies (see Mac~Lane [@bib:MacLane1974]), so one
may as well only use the non-degenerate simplices in forming this chain complex.
It is easy to see that this reduced complex is just the complex of cellular
chains on $|X|$ regarded as a CW-complex, so we use the notation $C_* (X; R)$.
The homology groups $H_n (X; R)$ are defined to be the homology groups of
$C_* (X; R)$, and the cohomology groups $H^n (X; R)$ are defined to be the
cohomology groups of $C^* (X; R) = Hom_R (C_* (X; R), R)$. If $Y$ is a
topological space, then the above construction on $Sing(Y)$ yields the usual
singular homology groups $H_n (Y; R)$.

The *Eilenberg–Zilber Theorem*#idx("Eilenberg", "–Zilber theorem")#idx(
  "theorem",
  "Eilenberg–Zilber",
) says that there is a natural chain homotopy equivalence
$ C_* (X; R) times.o C_* (Y; R) -> C_* (X times Y; R) $
given as follows. If $p + q = n$ and $x in X_p$, $y in Y_q$, then
$
  x times.o y |-> sum_((mu, nu)) (-1)^(epsilon(mu, nu))
  (s_(nu_q) dots s_(nu_1) x, s_(mu_p) dots s_(mu_1) y).
$
Here, the sum runs over the *Eilenberg–Mac~Lane* $(p, q)$-*shuffles*#idx(
  "Eilenberg",
  "–Mac Lane",
  "shuffle",
)#idx("shuffle, Eilenberg–Mac Lane") $(mu, nu)$ of $n$. Namely,
$mu = (mu_1, dots, mu_p)$ and $nu = (nu_1, dots, nu_q)$ with
$mu_1 < dots.c < mu_p$ and $nu_1 < dots.c < nu_q$, in such a way that
${mu_1, dots, mu_p, nu_1, dots, nu_q}$ is a permutation of ${0, dots, n - 1}$,
and the sign of the permutation is $epsilon(mu, nu)$. For further details, see
Mac~Lane [@bib:MacLane1974], Section~VIII.8.

#exercise[
  If $cal(C)$ is a category, the *nerve*#idx("nerve") of $cal(C)$ is the
  simplicial set $N cal(C)$#idx("$N cal(C)$") whose $n$-simplices are the chains
  of $n$ consecutive maps $bullet -> bullet -> dots.c -> bullet$ in $cal(C)$.
  Write down the face and degeneracy maps, and check that this is a simplicial
  set. The *classifying space*#idx("classifying space")#idx(
    "space",
    "classifying",
  ) $B cal(C)$#idx("$B cal(C)$") of $cal(C)$ is the topological realisation of
  the nerve $|N cal(C)|$.

  If $X$ is a CW-complex, let $cal(C)(X)$ be the category formed from the
  partially ordered set of singular simplices on $X$. Show that $B cal(C)(X)$ is
  the "barycentric subdivision"#idx("barycentric subdivision")#idx(
    "subdivision, barycentric",
  ) of $|Sing(X)|$ (cf. Section~@sec:g-simplicial-complexes), and hence using
  Theorem~@th:simplicial-equivalence that there is a homotopy equivalence
  between $X$ and $B cal(C)(X)$. Thus every CW-complex is homotopy equivalent to
  the classifying space of a category.
]
