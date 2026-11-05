#import "main-defs.typ": *
#import "statements.typ": *

== Equivariant homotopy <sec:equivariant-homotopy>
#idx("equivariant", "homotopy", target: [@sec:equivariant-homotopy])#idx(
  "homotopy",
  "equivariant",
  target: [@sec:equivariant-homotopy],
)

#definition[
  Suppose that $X$ and $Y$ are $G$-simplicial complexes. We say $f : X -> Y$ is
  a *$G$-map*#idx("$G$-map") if $f(g x) = g f(x)$ for all $x in X$ and $g in G$.
  If $f, f' : X -> Y$ are $G$-maps, we say $f$ and $f'$ are *$G$-homotopic*#idx(
    "$G$-homotopy",
  ) (written $f tilde.eq_G f'$#idx("$tilde.eq_G$")) if there is a $G$-map
  $F : X times I -> Y$ (where $I$ is the unit interval $[0, 1]$ with trivial
  $G$-action) such that $F(x, 0) = f(x)$ and $F(x, 1) = f'(x)$.

  We say $X$ and $Y$ are *$G$-homotopy equivalent* (written $X tilde.eq_G Y$) if
  there are $G$-maps $f : X -> Y$ and $f' : Y -> X$ such that the composites are
  $G$-homotopic to the identity maps $f compose f' tilde.eq_G id_Y$ and
  $f' compose f tilde.eq_G id_X$.
] <def:g-homotopy>

Clearly, if $X tilde.eq_G Y$ then $X^H tilde.eq Y^H$ for all subgroups $H <= G$.
It is a remarkable fact that the converse is also true when these homotopy
equivalences are the restrictions of a $G$-map.

#theorem[
  Suppose that $X$ and $Y$ are two $G$-simplicial complexes and $f : X -> Y$ is
  a $G$-map with the property that for all subgroups $H <= G$, $f$ restricts to
  an ordinary homotopy equivalence $f^H : X^H tilde.eq Y^H$. Then $f$ is a
  $G$-homotopy equivalence.
] <th:g-homotopy-equivalence>

#proof[
  In fact this statement is true for a much wider class of spaces and maps. See
  for example Tammo tom Dieck's book [@bib:TomDieck1979, Proposition~8.2.4 and
  Remark~8.2.5] and also James and Segal [@bib:James1978]. We shall prove the
  theorem in the context of $G$-CW-complexes, where $G$ is supposed to act
  cellularly and $f$ is a cellular map. The proof is modelled on the proof of
  Whitehead's Theorem~@th:whitehead-cw but with $G$-action incorporated. Let
  $M_f$ denote the mapping cylinder of $f$. For each subgroup $H$ of $G$, we
  have a long exact sequence
  $
    dots.c -> pi_(n+1) (M_f^H, X^H) -> pi_n (X^H)
    limits(arrow.r.long)^(f_*^H) pi_n (Y^H) -> pi_n (M_f^H, X^H) -> dots.c
  $
  #source(233)and so since $f_*^H$ is an isomorphism, we deduce that we have
  $pi_n (M_f^H, X^H) = 0$ for all subgroups $H$ of $G$ and all $n >= 0$.

  Now suppose $(K, L)$ is a relative $G$-CW-complex and $g : (K, L) -> (M_f, X)$
  is a cellular $G$-map. By induction on skeleta, the restriction of $g$ to the
  $n$-skeleton of $(K, L)$ is $G$-homotopic relative to $L$ to a cellular
  $G$-map sending $K^((n))$ into $X$. Namely, once the $(n - 1)$-skeleton is in,
  for each orbit of $G$ on the cells, say $G\/H times$ (cell), we choose a
  representative cell in this orbit, with stabiliser $H$. Since
  $pi_n (M_f^H, X^H) = 0$, there is no obstruction to moving it
  (non-equivariantly) into $X$, and then we use the $G$-action to see how to
  move the rest of the orbit. We may fit these $G$-homotopies together by doing
  the first skeleton in the interval $[0, 1/2]$, the second in $[1/2, 3/4]$, and
  so on, to show that $g$ is $G$-homotopic relative to $L$ to a $G$-map sending
  $K$ into $X$.

  Applying the above statement to the identity map from $(M_f, X)$ to itself, we
  see that the inclusion $X subset.eq M_f$ is a $G$-homotopy equivalence, and
  hence so is $f$.
]

#remark[
  It is _not_ true that if the restrictions of two maps $f$, $f' : X -> Y$ to
  fixed point sets of $H$ are homotopic as maps from $X^H$ to $Y^H$ for all
  subgroups $H <= G$ then $f tilde.eq_G f'$.
]

#proposition[
  Suppose that $X$ and $Y$ are two finite $G$-simplicial complexes. Then we have
  #statement-comment[(i)] $<=>$ #statement-comment[(ii)] $=>$
  #statement-comment[(iii)] $=>$ #statement-comment[(iv)] $=>$
  #statement-comment[(v)] in the following list of statements:
  + $X tilde.eq_G Y$
  + $X^H tilde.eq Y^H$ for all $H <= G$, via the restrictions $f^H$ of a $G$-map
    $f : X -> Y$
  + $chi(X^H) = chi(Y^H)$ for all $H <= G$
  + $Lambda_G (X) = Lambda_G (Y) in b(G)$
  + $L_G (X) = L_G (Y) in a(k G)$.
] <prop:g-homotopy-invariants>

#proof[
  This is clear from the definitions and the above theorem.#ed-note[The book
    states the converse without the condition that the homotopy equivalences are
    the restrictions of a $G$-map, here and in the sentence before
    Theorem~@th:g-homotopy-equivalence. It fails for $G = ZZ slash 2$ acting
    freely on a torus by a translation and by a glide reflection: the fixed
    point sets agree for every subgroup, but the orbit spaces, a torus and a
    Klein bottle, are not homotopy equivalent.]
]

We shall be applying this to several $G$-simplicial complexes arising from the
subgroup structure of $G$, and we shall mostly be interested in properties of
the corresponding Lefschetz modules.

Now recall that Conlon's Induction Theorem#idx(
  "Conlon's induction theorem",
)#idx(
  "induction theorem, Conlon's",
)#idx("theorem", "Conlon's induction") (5.6.8 of Volume~I) implies that two
elements of $b(G)$ have the same image in $a(k G)$ if their restrictions to all
$p$-hypo-elementary subgroups#idx("hypo-elementary group")#idx(
  "group",
  "hypo-elementary",
) (i.e., subgroups $H$ with $H\/O_p (H)$ cyclic) are equal. So by the same chain
of reasoning as above, we have the following.

#proposition(closed: true)[
  Suppose $k$ is a field of characteristic $p$. Suppose $X$ and $Y$ are two
  finite $G$-simplicial complexes such that for all $p$-hypo-elementary
  subgroups $H <= G$, we have $chi(X^H) = chi(Y^H)$. Then
  $L_G (X, k) = L_G (Y, k) in a(k G)$.
] <prop:hypo-elementary-lefschetz>

We now turn to the equivariant homotopy theory of $G$-posets#idx(
  "$G$-poset",
)#idx("poset"). If $X$ and $Y$ are $G$-posets then we have equivariant
homeomorphisms
$ |X^op| tilde.equiv |X|, wide |X times Y| = |X| times |Y|. $
#source(234)Here, the product on the right is taken in the category of compactly
generated spaces, as in the remark after Definition~@def:cw-complex. This
statement can be seen by going through simplicial sets, where the behaviour with
respect to products is clearer, and then using the fact that topological
realisation commutes with products for simplicial sets (see
Section~@sec:simplicial-sets).

If $f : X -> Y$ is a $G$-map of $G$-posets (i.e., order preserving $G$-map of
the underlying sets) then $f$ induces a map $|f| : |X| -> |Y|$. If two maps of
posets (resp. $G$-posets) $f$, $f' : X -> Y$ induce homotopic (resp.
$G$-homotopic) maps of simplicial complexes, then we say that $f$ and $f'$ are
*homotopic*, (resp. *$G$-homotopic*) and write $f tilde.eq f'$ (resp.
$f tilde.eq_G f'$). We say that a poset $X$ is *contractible*#idx(
  "contractible",
  "poset",
)#idx("poset", "contractible") if $|X|$ is contractible.

#lemma[
  If $f$, $f' : X -> Y$ are maps of posets such that for all $x in X$,
  $f(x) <= f'(x)$, then $f tilde.eq f'$.
] <lem:comparable-maps-homotopic>

#proof[
  Denote by $(0 < 1)$ the poset with two elements and one inequality. Then $f$
  and $f'$ define a map of posets
  $
    F : (0 < 1) times X & -> Y \
                 (0, x) & |-> f(x) \
                 (1, x) & |-> f'(x)
  $
  Since $|(0 < 1)|$ is the unit interval, $|F|$ is a homotopy from $|f|$ to
  $|f'|$.
]

#definition[
  We say a poset $X$ is *conically contractible*#idx(
    "conically contractible",
  )#idx("contractible", "conically") if there exists a map of posets
  $f : X -> X$ and an element $x_0 in X$ such that for all $x in X$,
  $x <= f(x) >= x_0$.
] <def:conically-contractible>

By the above lemma, if $X$ is conically contractible, then it is contractible.

#example[
  If a simplicial complex $Delta$ is a cone, with vertex $x_0$, then $S(Delta)$
  is conically contractible, since we may take for $f$ the map sending each
  simplex to the simplex obtained by adjoining $x_0$ if it is not already a
  vertex.
]
