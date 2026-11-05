#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/03-02-filtered-complex.typ": (
  boundaries-diagram, cycles-diagram, exact-couple, image-lemma,
  interlocking-sequences, limit-image, page-image,
)

== The spectral sequence of a filtered chain complex <sec:filtered-complex>

#source(110)#idx(
  "spectral sequence",
  "of a filtered complex",
  target: [@sec:filtered-complex],
)We shall work in this section with the cohomology spectral sequence, and then
indicate what changes are necessary to obtain the homology spectral sequence.
The ideas are the same in both cases, but the indexing is different. In some
sense, homology is indexed as though it were negative degree cohomology.

Suppose
$
  bold(X) = F^0 bold(X) supset.eq F^1 bold(X) supset.eq dots.c supset.eq
  inter.big F^i bold(X) = {0}
$
is a filtration#idx("filtered complex")#idx("$F^p bold(X)$") of a cochain
complex (i.e., a decreasing sequence of subcomplexes). Then the long exact
sequences
$
  dots.c -> H^n (F^(p+1) bold(X)) -> H^n (F^p bold(X))
  -> H^n (F^p bold(X), F^(p+1) bold(X)) \
  -> H^(n+1) (F^(p+1) bold(X)) -> dots.c
$
can be fitted together as in the following diagram, where the sequences go
alternately down one and to the right two places.
$ #interlocking-sequences $ <fig:interlocking-sequences>
To keep control of all the data here, we set
$
  E_1^(p q) = H^(p+q) (F^p bold(X), F^(p+1) bold(X)), quad
  D_1^(p q) = H^(p+q) (F^p bold(X))
$
as doubly indexed sets of abelian groups (or $R$-modules, if $bold(X)$ is a
cochain complex of $R$-modules). The exact sequences become
$ #exact-couple($D_1^(**)$, $E_1^(**)$, $i_1$, $j_1$, $k_1$) $
where
$
  deg(i_1) & = (-1, 1) & wide Ker(i_1) & = Im(k_1) \
  deg(j_1) & = (0, 0)  &      Ker(j_1) & = Im(i_1) \
  deg(k_1) & = (1, 0)  &      Ker(k_1) & = Im(j_1).
$

#definition(title: [Massey])[
  #source(111)An *exact couple*#idx("exact", "couple")#idx("couple", "exact") is
  an exact triangle of the form
  $
    #exact-couple($D$, $E$, $i$, $j$, $k$) wide
    mat(
      delim: #none,
      align: #left,
      Ker(i) = Im(k);
      Ker(j) = Im(i);
      Ker(k) = Im(j).
    )
  $
] <def:exact-couple>

Every time we have an exact couple as above, we obtain a _spectral sequence_ as
follows. Since $k compose j = 0$, we have $(j compose k)^2 = 0$. Thus setting
$d = j compose k$, we may take homology of $E$ with respect to $d$,
$ H(E, d) = Ker(d) slash Im(d). $
This gives rise to the notion of a derived couple.

#definition[
  If
  $ #exact-couple($D$, $E$, $i$, $j$, $k$) $
  is an exact couple, then the *derived couple*#idx("derived couple")#idx(
    "couple",
    "derived",
  )
  $ #exact-couple($D'$, $E'$, $i'$, $j'$, $k'$) $
  is given by setting
  $
               D' & = Im(i) subset.eq D \
               E' & = H(E, d) italic("as a subquotient of") E \
               i' & = i|_(D') \
         j'(i(x)) & = j(x) + Im(d) in Ker(d) slash Im(d) \
    k'(z + Im(d)) & = k(z)
  $
] <def:derived-couple>

It is an easy diagram chase to check that the above maps are well defined, and
that the derived couple of an exact couple is again an exact couple.

#definition[
  We define the exact couple
  $ #exact-couple($D_n$, $E_n$, $i_n$, $j_n$, $k_n$) $
  to be the $(n - 1)$st derived couple of the exact couple
  $ #exact-couple($D_1$, $E_1$, $i_1$, $j_1$, $k_1$) . $
  The sequence $(E_1, d_1)$, $(E_2, d_2)$, $dots$ is called the *spectral
  sequence*#idx("spectral sequence")#idx("sequence", "spectral") of the original
  exact couple.
] <def:spectral-sequence>

#source(112)We now keep track of the double grading. We have
$
  deg(i_n) & = deg(i_(n-1)) \
  deg(j_n) & = deg(j_(n-1)) - deg(i_(n-1)) \
  deg(k_n) & = deg(k_(n-1)) \
  deg(d_n) & = deg(j_n) + deg(k_n)
$
and hence
$
  deg(i_n) & = (-1, 1) \
  deg(j_n) & = (n - 1, -n + 1) \
  deg(k_n) & = (1, 0) \
  deg(d_n) & = (n, -n + 1).
$
Thus for example $(E_2, d_2)$ and $(E_3, d_3)$ appear as in the pictures on
page~@fig:second-page[page].

For most of the filtered complexes we are interested in, it will turn out that
$E_2^(p q) = 0$ for $q < 0$ (and also of course for $p < 0$) so that we shall
proceed for the rest of this section under this assumption. This will enable us
to avoid a detailed discussion of convergence problems.

Each $D_n^(p q)$ is contained inside $D_1^(p q)$, and we write
$D_infinity^(p q)$ for $inter.big_n D_n^(p q)$. Since each $E_n^(p q)$ is a
subquotient of $E_(n-1)^(p q)$, we may find subgroups $Z_2^(p q) = Ker(d_1)$ and
$B_2^(p q) = Im(d_1)$ of $E_1^(p q)$ such that
$E_2^(p q) = Z_2^(p q) slash B_2^(p q)$. We then have subgroups $Z_3^(p q)$ and
$B_3^(p q)$ of $E_1^(p q)$ with $Z_3^(p q) slash B_2^(p q) = Ker(d_2)$,
$B_3^(p q) slash B_2^(p q) = Im(d_2)$ and
$E_3^(p q) = (Z_3^(p q) slash B_2^(p q)) slash (B_3^(p q) slash B_2^(p q))
tilde.equiv Z_3^(p q) slash B_3^(p q)$. Continuing this way and setting
$Z_1^(p q) = E_1^(p q)$ and $B_1^(p q) = 0$, we have subgroups
$
  E_1^(p q) = Z_1^(p q) supset.eq Z_2^(p q) supset.eq Z_3^(p q) supset.eq
  dots.c supset.eq B_3^(p q) supset.eq B_2^(p q) supset.eq B_1^(p q) = 0
$
such that $E_n^(p q) tilde.equiv Z_n^(p q) slash B_n^(p q)$. We now set
$
  Z_infinity^(p q) = inter.big_n Z_n^(p q), quad
  B_infinity^(p q) = union.big_n B_n^(p q), quad
  E_infinity^(p q) = Z_infinity^(p q) slash B_infinity^(p q).
$

Now we have a canonical filtration of the cohomology of $bold(X)$:
$
  F^p H^(p+q) (bold(X)) = Im(H^(p+q) (F^p bold(X)) -> H^(p+q) (bold(X))).
$
Our next goal is to prove that
$
  F^p H^(p+q) (bold(X)) slash F^(p+1) H^(p+q) (bold(X)) tilde.equiv
  E_infinity^(p q).
$

#proposition[
  #part-lines[
    + $Z_n^(p q) = Im(
        H^(p+q) (F^p bold(X), F^(p+n) bold(X))
        -> H^(p+q) (F^p bold(X), F^(p+1) bold(X))
      )
      = Ker(
        H^(p+q) (F^p bold(X), F^(p+1) bold(X))
        limits(arrow.r.long)^(partial_*)
        H^(p+q+1) (F^(p+1) bold(X), F^(p+n) bold(X))
      )$
    + $B_n^(p q) = Im(
        H^(p+q-1) (F^(p-n+1) bold(X), F^p bold(X))
        limits(arrow.r.long)^(partial_*)
        H^(p+q) (F^p bold(X), F^(p+1) bold(X))
      )
      = Ker(
        H^(p+q) (F^p bold(X), F^(p+1) bold(X))
        -> H^(p+q) (F^(p-n+1) bold(X), F^(p+1) bold(X))
      )$
  ]
] <prop:cycles-boundaries>

#proof[
  + #source(113)The following diagram represents a part of the diagram on
    page~@fig:interlocking-sequences[page].
    $ #cycles-diagram $
    Referring to this diagram, we have $x in Z_n^(p q)$ if and only if
    $d_1 (x) = 0$, $d_2 (x) = 0, dots, d_(n-1) (x) = 0$. This happens if and
    only if $k_1 (x) in Im((i_1)^(n-1))$, namely if and only if
    $
      k_1 (x) in
      Ker(
        H^(p+q+1) (F^(p+1) bold(X))
        -> H^(p+q+1) (F^(p+1) bold(X), F^(p+n) bold(X))
      )
    $
    This in turn is true if and only if
    $
      x & in Ker(
            H^(p+q) (F^p bold(X), F^(p+1) bold(X))
            -> H^(p+q+1) (F^(p+1) bold(X), F^(p+n) bold(X))
          ) \
        & = Im(
            H^(p+q) (F^p bold(X), F^(p+n) bold(X))
            -> H^(p+q) (F^p bold(X), F^(p+1) bold(X))
          ).
    $
  + Referring to the following diagram
    $ #boundaries-diagram $
    #source(114)we have $x in B_n^(p q)$ if and only if $x = j_1 (y)$ with
    $(i_1)^(n-2) (y) in Im(k_1)$, i.e., with $(i_1)^(n-1) (y) = 0$, or
    equivalently with
    $
      y in Im(
        H^(p+q-1) (F^(p-n+1) bold(X), F^p bold(X))
        -> H^(p+q) (F^p bold(X))
      ).
    $
    This happens if and only if $x in Im(partial_*)$.
]

#lemma[
  If we have a commutative diagram of abelian groups
  $ #image-lemma $
  with the bottom row exact, then $g$ induces an isomorphism
  $ g : Im(h) slash Im(f) limits(arrow.r)^tilde.equiv Im(k). $
] <lem:image-quotient>

#proof[
  By the first isomorphism theorem
  $
    frac(Im(h), Im(f)) = frac(Im(h), Ker(g)) limits(tilde.equiv)^g Im(g h)
    = Im(k)
  $
]

#theorem[
  $E_n^(p q)$ is isomorphic to the image of
  $
    H^(p+q) (F^p bold(X), F^(p+n) bold(X))
    -> H^(p+q) (F^(p-n+1) bold(X), F^(p+1) bold(X)).
  $
] <th:page-as-image>

#proof[
  We apply Lemma~@lem:image-quotient to the diagram
  $ #page-image $
]

#corollary(closed: true)[
  $E_infinity^(p q) = Im(
    H^(p+q) (F^p bold(X))
    -> H^(p+q) (bold(X), F^(p+1) bold(X))
  )$.
] <cor:infinity-page>

#definition[
  We set
  $F^p H^(p+q) (bold(X)) = Im(H^(p+q) (F^p bold(X)) -> H^(p+q) (bold(X)))$#idx(
    "$F^p H^(p+q) (bold(X))$",
  ).
] <def:cohomology-filtration>

#theorem[
  $F^p H^(p+q) (bold(X)) slash F^(p+1) H^(p+q) (bold(X)) tilde.equiv
  E_infinity^(p q)$.
] <th:filtration-quotients>

#proof[
  We apply Lemma~@lem:image-quotient to the diagram
  $ #limit-image $
]

We may regard this theorem as saying that whenever we set up a spectral sequence
using a filtered complex, we know what it converges to; namely the cohomology of
the original complex. The problem is to understand the initial data given by the
$E_2$ term. In the next section we shall give a sketchy account of the $E_2$
term in the case of the spectral sequence of a fibration. In #source(115)the
following section, we shall see that the problem of understanding the $E_2$ term
is substantially simplified if we start off with a double complex rather than a
filtered complex.

We now discuss edge homomorphisms#idx("edge homomorphism") and transgressions.
Setting $q = 0$, we see that each $E_r^(p 0)$ is a quotient of $E_2^(p 0)$, and
$E_infinity^(p 0)$ is contained in $H^p (bold(X))$. Thus we have homomorphisms
$
  E_2^(p 0) ->> E_3^(p 0) ->> dots.c ->> E_infinity^(p 0) arrow.r.hook
  H^p (bold(X)).
$
The composite homomorphism $E_2^(p 0) limits(arrow.r)^e H^p (bold(X))$ is called
the *horizontal edge homomorphism*#idx(
  "horizontal edge homomorphism",
)#idx("homomorphism", "horizontal edge").

The *vertical edge homomorphism*#idx("vertical edge homomorphism")#idx(
  "homomorphism",
  "vertical edge",
) $H^q (bold(X)) limits(arrow.r)^(e') E_2^(0 q)$ is the composite map
$
  H^q (bold(X)) ->> E_infinity^(0 q) arrow.r.hook dots.c arrow.r.hook
  E_3^(0 q) arrow.r.hook E_2^(0 q).
$
Following through the isomorphisms used to prove
Theorem~@th:filtration-quotients, it is easy to see that this is just the
composite of the obvious maps
$
  H^q (bold(X)) -> H^q (bold(X), F^2 bold(X))
  -> Im(H^q (bold(X), F^2 bold(X)) -> H^q (bold(X), F^1 bold(X))) = E_2^(0 q).
$

The *transgression*#idx("transgression")#idx(
  "spectral sequence",
  "transgression in",
) is the differential $d_n : E_n^(0,n-1) -> E_n^(n 0)$. In case $n = 2$, this
gives rise to the *five term sequence*#idx("five term sequence")#idx(
  "sequence",
  "five term",
) involving the transgression and edge homomorphisms
$
  0 -> E_2^(10) limits(arrow.r)^e H^1 (bold(X)) limits(arrow.r)^(e')
  E_2^(01) limits(arrow.r.long)^(d_2) E_2^(20) limits(arrow.r)^e
  H^2 (bold(X)).
$

This is obtained by splicing together the sequences
$
  0 -> E_2^(10) = E_infinity^(10) -> H^1 (bold(X)) -> E_infinity^(01) -> 0 \
  0 -> E_infinity^(01) -> E_2^(01) limits(arrow.r.long)^(d_2) E_2^(20)
  -> E_infinity^(20) -> 0
$
and
$ 0 -> E_infinity^(20) -> H^2 (bold(X)). $
Thus we have the following.

#proposition(closed: true)[
  In the spectral sequence of a filtered cochain complex, there is a five term
  exact sequence
  $
    0 -> E_2^(10) limits(arrow.r)^e H^1 (bold(X)) limits(arrow.r)^(e')
    E_2^(01) limits(arrow.r.long)^(d_2) E_2^(20) limits(arrow.r)^e
    H^2 (bold(X)).
  $
] <prop:five-term-cohomology>

We now discuss the dual setup in homology. If we start off with a filtered chain
complex
$
  F_0 bold(X) subset.eq F_1 bold(X) subset.eq dots.c subset.eq bold(X) =
  union.big F_i bold(X),
$
#source(116)then we have an exact couple and spectral sequence
$
         E^1_(p q) & = H_(p+q) (F_p bold(X), F_(p-1) bold(X)) \
         D^1_(p q) & = H_(p+q) (F_p bold(X)) \
         E^n_(p q) & = H(E^(n-1)_(p q), d^(n-1)) wide deg(d^n) = (-n, n - 1) \
  E^infinity_(p q) & tilde.equiv
                     F_p H_(p+q) (bold(X)) slash F_(p-1) H_(p+q) (bold(X))
$
where
$
  F_p H_(p+q) (bold(X)) = Im(H_(p+q) (F_p bold(X)) -> H_(p+q) (bold(X))).
$

The edge homomorphisms are $H_p (bold(X)) limits(arrow.r)^e E^2_(p 0)$ and
$E^2_(0 q) limits(arrow.r)^(e') H_q (bold(X))$, the transgression is
$d^n : E^n_(n 0) -> E^n_(0,n-1)$. The five term sequence is as follows.

#proposition(closed: true)[
  In the spectral sequence of a filtered chain complex, there is a five term
  exact sequence
  $
    H_2 (bold(X)) limits(arrow.r)^e E^2_(20) limits(arrow.r.long)^(d^2)
    E^2_(01) limits(arrow.r)^(e') H_1 (bold(X)) limits(arrow.r)^e E^2_(10)
    -> 0.
  $
] <prop:five-term-homology>
