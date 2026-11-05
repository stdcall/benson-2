#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-07-module-varieties.typ": strata-restriction

== Varieties for modules <sec:module-varieties>

#source(188)If $M$ is a $k G$-module, we associate to $M$ a subvariety $V_G (M)$
of $V_G$ as follows. There is a natural map
$
  Phi_M : H^dot (G, k) = Ext^dot_(k G) (k, k) limits(arrow.r.long)^(times.o M)
  Ext^*_(k G) (M, M)
$
#idx("$Phi_M$")whose image is central, by Corollary~3.2.2 of Volume~I. We denote
the kernel of this map by $I_G (M)$. This is a homogeneous ideal in
$H^dot (G, k)$, and therefore determines a closed homogeneous subvariety
$V_G (M) = max H^dot (G, k) slash I_G (M)$ of $V_G$. The corresponding
projective variety is denoted by $macron(V)_G (M) subset.eq macron(V)_G$.

If $M'$ is another $k G$-module, we write $I_G (M', M)$ for the annihilator in
the ring $Ext^dot_(k G) (k, k)$ of the module $Ext^*_(k G) (M', M)$, with the
cup product action. We write $V_G (M', M)$ for the closed homogeneous subvariety
of $V_G$ defined by this ideal, so that in particular $V_G (M) = V_G (M, M)$.
Since this cup product action factors as $Phi_M$ followed by Yoneda composition,
or as $Phi_(M')$ followed by Yoneda composition (Proposition~3.2.1 of Volume~I),
we have
$
  I_G (M', M) & supset.eq I_G (M') + I_G (M) \
  V_G (M', M) & subset.eq V_G (M') inter V_G (M).
$

If $0 -> M' -> M'' -> M''' -> 0$ is a short exact sequence of $k G$-modules,
then the long exact Ext sequence (Section~2.5 of Volume~I) shows that
$
  I_G (M'', M) & supset.eq I_G (M', M) . I_G (M''', M) \
  V_G (M'', M) & subset.eq V_G (M', M) union V_G (M''', M).
$

Combining these statements, we obtain the following:

#proposition[
  If $M$ is a finitely generated $k G$-module then
  $ V_G (M) = union.big_S V_G (S, M), $
  where $S$ runs over the simple $k G$-modules, or over the composition factors
  of $M$. In particular, if $G$ is a $p$-group then $V_G (M) = V_G (k, M)$, the
  subvariety of $V_G$ defined by the annihilator of $H^* (G, M)$.
] <prop:variety-simple-modules>

#proof[
  The containment of the right-hand side in the left-hand side follows from the
  first of the above inequalities, while the reverse containment follows from
  the second.
]

#remark[
  If $M$ is a finitely generated $k G$-module, then by
  Corollary~@cor:ext-noetherian, the ring $Ext^*_(k G) (M, M)$ is finitely
  generated as a module over the image of $Phi_M$. Thus if we set
  $ tilde(V)_G (M) = max Z Ext^*_(k G) (M, M), $
  the maximal ideal spectrum of the centre of $Ext^*_(k G) (M, M)$, then by
  Theorem~@th:lying-over the map
  $ Phi_M^* : tilde(V)_G (M) -> V_G (M) $
  is a finite surjective map.

  #source(189)In some sense, we should not have to stop at the centre. Since the
  ring $Ext^*_(k G) (M, M)$ is finitely generated as a module over its centre,
  it is an affine polynomial identity (P.I.) algebra#idx(
    "affine",
    "polynomial identity algebra",
  ), see McConnell and Robson [@bib:McConnell1988], Chapter~13, Corollary~1.13.
  There is a well developed theory of maximal ideal spectra for such rings, see
  for example Procesi's book [@bib:Procesi1973].
]

We begin with some properties of the varieties $V_G (M)$ which are easy
consequences of our previous discussions.

#proposition[
  If $M$ is a finitely generated $k G$-module then the dimension of $V_G (M)$ is
  equal to the complexity $c_G (M)$. In particular $V_G (M) = {0}$ if and only
  if $M$ is projective.
] <prop:variety-dimension-complexity>

#proof[
  Since $Ext^*_(k G) (M, M)$ is finitely generated as a module over the ring
  $H^dot (G, k)$ (Corollary~@cor:ext-noetherian), we have by
  Proposition~@prop:complexity-ext and Theorem~@th:krull-dimension
  $
    c_G (M) = gamma(Ext^*_(k G) (M, M)) = gamma(H^dot (G, k) slash I_G (M))
    = dim V_G (M).
  $
]

#proposition[
  We have
  $ V_G (M) = V_G (M^*) = V_G (Omega(M)) = V_G (Omega^(-1)(M)). $
] <prop:variety-dual-omega>

#proof[
  This follows from the isomorphisms
  $
    Ext^*_(k G) (M, M) & tilde.equiv Ext^*_(k G) (M^*, M^*)
                         tilde.equiv Ext^*_(k G) (Omega(M), Omega(M)) \
                       & tilde.equiv Ext^*_(k G) (Omega^(-1)(M), Omega^(-1)(M))
  $
  as modules for $Ext^dot_(k G) (k, k)$.
]

#proposition[
  We have
  $ V_G (M) = union.big_(E <= G \ "elemab") res^*_(G, E) V_E (M). $
] <prop:module-variety-union>

#proof[
  According to Theorem~@th:nilpotent-restriction, an element of
  $Ext^*_(k G) (M, M)$ is nilpotent if and only if it is nilpotent on
  restriction to every elementary abelian#idx(
    "elementary",
    "abelian group",
  )#idx("group", "elementary abelian") subgroup $E <= G$. Applying this to
  elements in the image of $Phi_M$, we have
  $
    sqrt(I_G (M)) = inter.big_(E <= G \ "elemab") res_(G, E)^(-1) sqrt(I_E (M)).
  $
  The subvariety of $V_G$ determined by $res_(G, E)^(-1) sqrt(I_E (M))$ is the
  same as the subvariety defined by $res_(G, E)^(-1) I_E (M)$, namely
  $res^*_(G, E) V_E (M)$.
]

#proposition[
  We have
  $ V_G (M_1 plus.o M_2) = V_G (M_1) union V_G (M_2). $
] <prop:variety-direct-sum>

#proof[
  #source(190)Tensoring with $M_1 plus.o M_2$ factors as follows:
  $
    Ext^dot_(k G) (k, k) limits(arrow.r.long)^((times.o M_1, times.o M_2))
    Ext^*_(k G) (M_1, M_1) plus.o Ext^*_(k G) (M_2, M_2) \
    arrow.r.hook Ext^*_(k G) (M_1 plus.o M_2, M_1 plus.o M_2)
  $
  and so
  $
    I_G (M_1 plus.o M_2) & = I_G (M_1) inter I_G (M_2) \
    V_G (M_1 plus.o M_2) & = V_G (M_1) union V_G (M_2).
  $
]

Next, we develop a version of the Quillen stratification theorem for the
varieties $V_G (M)$, due to Avrunin and Scott [@bib:Avrunin1982]. We begin with
a technical lemma.

#lemma[
  Suppose $H$ is a normal subgroup of index $p$ in $G$, and $x$ is the inflation
  to $G$ of a non-zero element $macron(x) in H^1 (G slash H, FF_p)$. If
  $zeta in H^* (G, k)$ with $res_(G, H) (zeta) in I_H (M)$, then some power of
  $zeta$ lies in the ideal generated by $I_G (M)$ and the Bockstein $beta(x)$.
] <lem:power-in-bockstein-ideal>

#proof[
  If $res_(G, H) (zeta) in I_H (M)$ then $res_(G, H) (zeta_M) = 0$, and so by
  Theorem~@th:quillen-venkov, $zeta_M^2 = beta(x) . xi$ for some
  $xi in Ext^*_(k G) (M, M)$. Now by Corollary~@cor:ext-noetherian
  $Ext^*_(k G) (M, M)$ is finitely generated as a module over
  $Ext^dot_(k G) (k, k)$, and so $xi$ satisfies some monic polynomial of the
  form
  $ xi^n + (a_(n-1))_M xi^(n-1) + dots.c + (a_0)_M = 0 $
  with the $a_i in Ext^dot_(k G) (k, k)$. Multiplying this equation by
  $beta(x)^n$, we obtain
  $
    zeta_M^(2n) + (a_(n-1))_M beta(x) zeta_M^(2n-2) + dots.c
    + (a_0)_M beta(x)^n = 0.
  $
  Thus the element
  $ zeta^(2n) + a_(n-1) beta(x) zeta^(2n-2) + dots.c + a_0 beta(x)^n $
  is in $I_G (M)$.
]

#proposition[
  If $E' <= E$ are elementary abelian $p$-groups and $M$ is a $k E$-module, then
  regarding $V_(E')$ as embedded in $V_E$ via $res^*_(E, E')$, we have
  $ V_(E') (M) = V_(E') inter V_E (M). $
] <prop:variety-subgroup-intersection>

#proof[
  Arguing by induction, we may suppose that $|E : E'| = p$. If
  $zeta in H^dot (E, k)$ lies in $I_E (M)$ then $res_(E, E') (zeta)$ lies in
  $I_(E') (M)$. Conversely, if $res_(E, E') (zeta)$ lies in $I_(E') (M)$ then by
  the lemma, some power of $zeta$ lies in the ideal generated by $beta(x)$ and
  $I_E (M)$, where $x$ is the inflation to $E$ of a non-zero element of
  $H^1 (E slash E', k)$. So we have
  $
    sqrt(res_(E, E')^(-1) I_(E') (M))
    = sqrt(chevron.l Ker(res_(E, E'))\, I_E (M) chevron.r).
  $
  Taking varieties, we obtain the required equality.
]

#source(191)We now define#idx("$V_E^+ (M)$, $V_(G, E) (M)$, $V_(G, E)^+ (M)$")
$
  V_E^+ (M) = V_E^+ inter V_E (M) \
  V_(G, E) (M) = res^*_(G, E) V_E (M) subset.eq V_G (M) \
  V_(G, E)^+ (M) = res^*_(G, E) V_E^+ (M).
$

#theorem(title: [Avrunin and Scott [@bib:Avrunin1982]])[
  Suppose $M$ is a finitely generated $k G$-module. Then the variety $V_G (M)$
  is the disjoint union of locally closed subvarieties $V_(G, E)^+ (M)$, one for
  each conjugacy class of elementary abelian subgroups $E <= G$. The group
  $W_G (E)$ acts on $V_E (M)$ and $V_E^+ (M)$, and $res^*_(G, E)$ induces an
  inseparable isogeny
  $ V_E^+ (M) slash W_G (E) -> V_(G, E)^+ (M). $
] <th:module-stratification>
#idx("Avrunin", "–Scott theorem", target: [@th:module-stratification])#idx(
  "theorem",
  "Avrunin–Scott",
  target: [@th:module-stratification],
)#idx(
  "stratification, Quillen",
  "for modules",
  target: [@th:module-stratification],
)#idx(
  "theorem",
  "Quillen",
  "stratification for modules",
  target: [@th:module-stratification],
)

#proof[
  It follows from the above proposition that
  $ V_E^+ (M) = V_E (M) without union.big_(E' < E) res^*_(E, E') V_(E') (M) $
  so that $V_E (M)$ is the disjoint union over $E' <= E$ of locally closed
  subvarieties $V_(E')^+ (M)$. It now follows from
  Proposition~@prop:module-variety-union that
  $ V_G (M) = union.big_(E <= G \ "elemab") res^*_(G, E) V_E^+ (M). $
  It follows from Theorem~@th:quillen-stratification that the subvarieties
  $V_(G, E)^+ (M) = res^*_(G, E) V_E^+ (M)$ are disjoint and that $res^*_(G, E)$
  induces an inseparable isogeny
  $ V_E^+ (M) slash W_G (E) -> V_(G, E)^+ (M). $
]

#corollary[
  If $H$ is a subgroup of $G$ and $M$ is a $k G$-module then
  $ V_H (M) = (res^*_(G, H))^(-1) V_G (M). $
] <cor:variety-restriction>

#proof[
  Clearly $res^*_(G, H) V_H (M) subset.eq V_G (M)$. Conversely, by the theorem,
  the diagram
  $ #strata-restriction $
  shows that $V_(H, E)^+ (M) = (res^*_(G, H))^(-1) V_(G, E)^+ (M)$.
]

#proposition[
  There is a natural isomorphism
  $V_(G_1 times G_2) tilde.equiv V_(G_1) times V_(G_2)$. If $M_1$ is a
  $k G_1$-module and $M_2$ is a $k G_2$-module then the image of
  $V_(G_1 times G_2) (M_1 times.o M_2)$ under this isomorphism is
  $V_(G_1) (M_1) times V_(G_2) (M_2)$.
] <prop:variety-direct-product>

#proof[
  This follows directly from the Künneth Theorem (3.5.6 of Volume~I; the Tor
  term there is zero, as we are working over a field).
]

#theorem[
  #source(192)If $M_1$ and $M_2$ are $k G$-modules then
  $ V_G (M_1 times.o M_2) = V_G (M_1) inter V_G (M_2). $
] <th:variety-tensor-product>

#proof[
  The interior tensor product $M_1 times.o M_2$ as a $k G$-module is the
  restriction from $G times G$ to the diagonal $G = Delta(G)$ of the exterior
  product $M_1 times.o M_2$ as a $k(G times G)$-module. So by
  Proposition~@prop:variety-direct-product and
  Corollary~@cor:variety-restriction we have
  $
    V_G (M_1 times.o M_2) & = (res^*_(G times G, Delta(G)))^(-1)
                            V_(G times G) (M_1 times.o M_2) \
                          & = (res^*_(G times G, Delta(G)))^(-1)
                            V_G (M_1) times V_G (M_2)
                            = V_G (M_1) inter V_G (M_2)
  $
  (Note that in general if $X$ and $Y$ are two subsets of a set $Z$ then the
  inverse image of $X times Y$ under the diagonal map
  $Z = Delta(Z) -> Z times Z$ is equal to $X inter Y$).
]

#corollary[
  If $V_G (M_1) inter V_G (M_2) = {0}$ then $Ext^n_(k G) (M_1, M_2) = 0$ for all
  $n > 0$.
] <cor:ext-vanishing>

#proof[
  By Proposition~@prop:variety-dual-omega and Theorem~@th:variety-tensor-product
  we have $V_G (M_1^* times.o M_2) = {0}$, and hence by
  Proposition~@prop:variety-dimension-complexity $M_1^* times.o M_2$ is
  projective. Hence
  $
    Ext^n_(k G) (M_1, M_2) tilde.equiv Ext^n_(k G) (k, M_1^* times.o M_2) = 0.
  $
]
