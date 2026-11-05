#import "main-defs.typ": *
#import "statements.typ": *

== The Quillen stratification <sec:quillen-stratification>
#idx("Quillen", "stratification", target: [@sec:quillen-stratification])#idx(
  "stratification, Quillen",
  target: [@sec:quillen-stratification],
)

The basic object of study here is the maximal ideal spectrum
$ V_G = max H^dot (G, k). $
#idx("$V_G$")Here, $H^dot (G, k)$ denotes $H^* (G, k)$ if $char(k) = 2$, and the
subring $H^"ev" (G, k)$ of elements of even degree if $char(k) != 2$ (in this
case, elements of odd degree square to zero). Thus $H^dot (G, k)$ is a
commutative graded ring, and so $V_G$ is #source(185)a homogeneous affine
variety. We denote by $macron(V)_G$#idx("$macron(V)_G$") the projective variety
of one smaller dimension
$ macron(V)_G = proj H^dot (G, k). $

If $H$ is a subgroup of $G$ then we have a restriction map
$ res_(G, H) : H^dot (G, k) -> H^dot (H, k), $
and hence a corresponding map of varieties $res^*_(G, H) : V_H -> V_G$#idx(
  "$res^*_(G, H)$",
).

#proposition[
  We have
  $ V_G = union.big_(E <= G \ "elemab") res^*_(G, E) V_E. $
] <prop:variety-union-elementary-abelian>

#proof[
  By Theorem~@th:nilpotent-restriction, an element of
  $H^dot (G, k) = Ext^dot_(k G) (k, k)$ is nilpotent if and only if it is
  nilpotent on restriction to every elementary abelian subgroup $E <= G$. Thus
  the map
  $ plus.o.big res_(G, E) : H^dot (G, k) -> plus.o.big H^dot (E, k) $
  has nilpotent kernel. Also, by Corollary~@cor:subgroup-finitely-generated, the
  right-hand side is finitely generated as a module over the image. Thus
  $ union.big res^*_(G, E) : dot(union.big) V_E -> V_G $
  is a finite dominant map, so that by Theorem~@th:lying-over it is surjective.
]

The Quillen Stratification Theorem [@bib:Quillen1971b, @bib:Quillen1971c] is a
refinement of the above proposition, giving a decomposition of $V_G$ into
disjoint pieces corresponding to the conjugacy classes of elementary abelian
subgroups of $G$.

Recall from Section~3.5 of Volume~I that if $E$ is an elementary abelian#idx(
  "elementary",
  "abelian group",
)#idx("group", "elementary abelian") $p$-group of rank $n$, then
$ H^* (E, k) tilde.equiv k[x_1, dots, x_n] $
with $deg(x_i) = 1$ if $p = 2$, while
$ H^* (E, k) tilde.equiv Lambda(x_1, dots, x_n) times.o k[y_1, dots, y_n] $
with $deg(x_i) = 1$, $deg(y_i) = 2$ and $beta(x_i) = y_i$ if $p$ is odd. In
either case, we see that $V_E$ is a $k$-vector space of dimension equal to the
$p$-rank of $E$. We define
$ V_E^+ = V_E without union.big_(E' < E) res^*_(E, E') V_(E'). $
#idx("$V_E^+$")Thus $V_E^+$ is $V_E$ with the hyperplanes defined over $FF_p$
removed. Let
$ sigma_E = product_(0 != zeta in H^1 (E, FF_p)) beta(zeta) in H^dot (E, k). $
#idx("$sigma_E$")Then since the subvariety of $V_E$ defined by $beta(zeta)$ is
$res^*_(E, E') V_(E')$, where $E'$ is the maximal subgroup corresponding to
$zeta$, the subvariety defined by the above element $sigma_E$ is
$union.big_(E' < E) res^*_(E, E') V_(E')$. So the points of $V_E^+$ correspond
to maximal #source(186)ideals of $H^dot (E, k)$ not containing $sigma_E$, and
hence to the maximal ideals of $H^dot (E, k)[sigma_E^(-1)]$. So we have
$ V_E^+ = max H^dot (E, k)[sigma_E^(-1)]. $
We define $V_(G, E) = res^*_(G, E) V_E subset.eq V_G$, and
$V_(G, E)^+ = res^*_(G, E) V_E^+$#idx("$V_(G, E)$, $V_(G, E)^+$").

The following lemma produces enough elements of cohomology to describe the
structures of these varieties.

#lemma[
  If $E$ is an elementary abelian $p$-subgroup of $G$ with
  $|N_G (E) : E| = p^a h$ and $(p, h) = 1$ then the following hold:
  + If $y in H^dot (E, k)$ is invariant under the action of $N_G (E)$ then there
    exists an element $y' in H^dot (G, k)$ with
    $ res_(G, E) (y') = (sigma_E . y)^(p^a). $
  + There exists an element $rho_E in H^dot (G, k)$ such that
    $res_(G, E) (rho_E) = (sigma_E)^(p^a)$, and such that if $E$ is not
    contained in any conjugate of an elementary abelian $p$-subgroup $E' <= G$
    then $res_(G, E') (rho_E) = 0$.
] <lem:stratification-elements>

#proof[
  + Without loss of generality $y$ is homogeneous. Let
    $ z = norm_(E, G) (1 + sigma_E . y). $
    Then the Mackey formula~@prop:norm-properties[(v)] shows that
    $
      res_(G, E) (z) & = (1 + sigma_E . y)^(p^a h)
                       = (1 + (sigma_E . y)^(p^a))^h \
                     & = 1 + h(sigma_E . y)^(p^a) + "terms of higher degree".
    $
    So we take for $y'$ the homogeneous part of $z$ of degree
    $p^a . deg(sigma_E . y)$, divided by $h$.
  + We take $y = 1$ in part (i), and write $rho_E$ for the element $y'$ obtained
    in this case. Since $res_(E, F) (sigma_E) = 0$ for all proper subgroups $F$
    of $E$, the Mackey formula~@prop:norm-properties[(v)] shows that
    $res_(G, E') (rho_E) = 0$ unless $E$ is conjugate to a subgroup of $E'$.
]

#theorem(
  title: [Quillen Stratification [@bib:Quillen1971b, @bib:Quillen1971c]],
)[
  The variety $V_G$ is the disjoint union of locally closed subvarieties
  $V_(G, E)^+$, one for each conjugacy class of elementary abelian subgroups
  $E <= G$. Let $W_G (E) = N_G (E) slash C_G (E)$#idx("$W_G (E)$"). Then
  $W_G (E)$ acts on $V_E$ and $V_E^+$, and $res^*_(G, E)$ induces an inseparable
  isogeny#idx("inseparable isogeny")#idx("isogeny, inseparable")
  $ V_E^+ slash W_G (E) -> V_(G, E)^+ $
  (see the end of Section~@sec:commutative-algebra).
] <th:quillen-stratification>
#idx(
  "theorem",
  "Quillen",
  "stratification",
  target: [@th:quillen-stratification],
)

#proof[
  By the lemma we have
  $
    {(H^dot (E, k)[sigma_E^(-1)])^(W_G (E))}^([p^a])
    subset.eq res_(G, E) H^dot (G, k)[rho_E^(-1)]
    subset.eq (H^dot (E, k)[sigma_E^(-1)])^(W_G (E))
  $
  and so we have an inseparable isogeny
  $
    max(H^dot (E, k)[sigma_E^(-1)])^(W_G (E))
    -> max res_(G, E) H^dot (G, k)[rho_E^(-1)].
  $
  #source(187)By Proposition~@prop:hilbert-noether the left-hand side is the
  quotient of $V_E^+$ by the action of $W_G (E)$, while the right-hand side is
  $V_(G, E)^+$. Thus we have an inseparable isogeny
  $ V_E^+ slash W_G (E) -> V_(G, E)^+. $
  If $E$ is not conjugate to a subgroup of $E'$ then by part (ii) of the lemma
  we have $res_(G, E') (rho_E) = 0$, and so $rho_E$ is a function which is
  everywhere non-zero on $V_(G, E)^+$ but everywhere zero on $V_(G, E')^+$. It
  follows that the $V_(G, E)^+$ are disjoint. Since $V_G$ is the union of the
  $res^*_(G, E) V_E$ by Proposition~@prop:variety-union-elementary-abelian, it
  is the union of the $V_(G, E)^+$.
]

A more succinct way to write the Quillen stratification theorem is as follows.
We form a category $cal(C)_G$ whose objects are the elementary abelian subgroups
of $G$, and where a morphism from $E$ to $E'$ consists of an element $g in G$
such that $g E g^(-1) subset.eq E'$. Then $E |-> V_E$ is a covariant functor on
$cal(C)_G$, and so it makes sense to talk of the limit $dirlim_E V_E$. This is
the maximal ideal spectrum of $invlim_E H^dot (E, k)$.

#corollary(closed: true)[
  The natural map
  $ dirlim_E V_E -> V_G $
  is an inseparable isogeny. Equivalently, the natural map
  $ q_G : H^dot (G, k) -> invlim_E H^dot (E, k) $
  is a finite map, whose kernel is nilpotent, and with the property that there
  is some power $p^a$ of $p$ such that the $p^a$th power of any element in the
  right hand side lies in the image of $q_G$.
] <cor:variety-limit>

#remark[
  It is an interesting question to ask when the map $q_G$ is an isomorphism of
  rings. Gunawardena, Lannes and Zarati [@bib:Gunawardena1989b] have shown that
  one can tell whether $q_G$ is an isomorphism just by looking at $H^dot (G, k)$
  as a module over the Steenrod algebra. Using this, they have shown that for
  $p = 2$ and $G$ a symmetric group $cal(S)_n$#idx(
    "group",
    "symmetric",
    "$cal(S)_n$",
  )#idx("symmetric", "group", "$cal(S)_n$") the map $q_G$ is an isomorphism.
  This is false for $p$ odd, but it seems that the reason is in some sense that
  the definition of $H^dot (G, k)$ is wrong for $p$ odd. A better definition
  would be to take the subring consisting of all elements which are annihilated
  by all elements of the Steenrod algebra involving the Bockstein operation. For
  example, with this definition, we have
  $H^dot (G_1 times G_2, k) tilde.equiv H^dot (G_1, k) times.o H^dot (G_2, k)$,
  so that if $E$ is elementary abelian then $H^dot (E, k)$ is just the
  polynomial subring, and the exterior part disappears. It is still an open
  question as to whether, with this definition, the map $q_G$ is an isomorphism
  for $G = cal(S)_n$ and $p$ odd.
]

#exercise[
  Show that in Theorem~@th:quillen-stratification, the action of $W_G (E)$ on
  $V_E^+$ is free. (Hint: show that if $1 != w in W_G (E)$ then the 1-eigenspace
  of $w$ on $V_E$ is contained in $res^*_(E, E') (V_(E'))$ for some $E' < E$)
]
