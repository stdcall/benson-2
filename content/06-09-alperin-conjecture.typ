#import "main-defs.typ": *
#import "statements.typ": *

== Steinberg module inversion and Alperin's conjecture <sec:alperin-conjecture>
#idx("Alperin", "'s conjecture", target: [@sec:alperin-conjecture])#idx(
  "conjecture",
  "Alperin's",
  target: [@sec:alperin-conjecture],
)#idx("Steinberg module", "inversion", target: [@sec:alperin-conjecture])

We defined the generalised Steinberg module in terms of an alternating sum of
permutation modules. In this section, we develop an inversion formula by the
means of which we can invert this relationship and express the trivial module as
a sum of modules induced from generalised Steinberg modules.

#proposition(title: [Bouc, Thévenaz])[
  If $X$ is a finite $G$-poset, then
  $
    Lambda_G (X) = - sum_(x in X slash G) ind_(Stab_G (x), G)
    tilde(Lambda)_(Stab_G (x)) ((x, -)_X)
  $
] <prop:lefschetz-invariant-inversion>

#proof[
  We sort the simplices $x_0 < dots.c < x_n$ of $|X|$ into clumps according to
  the $G$-orbit of $x_0$. The contribution to $Lambda_G (X)$ from such a clump
  will be given as follows. Choose an element $x$ in the orbit. Then we get the
  contribution from those simplices $x_0 < dots.c < x_n$ with $x_0 = x$,
  regarded as an element of the Burnside ring $b(Stab_G (x))$, and then induced
  up to $G$. It is easy to see that this part of the chain complex of $X$ is
  isomorphic to the chain complex of $(x, -)$ but with the dimension increased
  by one. The shift of dimension accounts for the sign change.
]

We now wish to apply this to the complex $cal(S)_p (G) union {1}$ of _all_
$p$-subgroups of $G$. If $P$ is a $p$-subgroup of $G$, then
$Stab_G (P) = N_G (P)$, and the complex $(P, -)$ is identified by the following
proposition.

#proposition(title: [Quillen, Webb])[
  If $P$ is a $p$-subgroup of $G$, then there is a $N_G (P)$-homotopy
  equivalence
  $ (P, -) tilde.eq_(N_G (P)) cal(S)_p (N_G (P) slash P) $
  where the right-hand side is regarded as a $N_G (P)$-poset via the quotient
  map $N_G (P) -> N_G (P) slash P$.

  #source(246)In particular,
  $
    tilde(Lambda)_(N_G (P)) ((P, -)) & = tilde(Lambda)_(N_G (P)) (
                                         cal(S)_p (N_G (P) slash P)
                                       ) \
         tilde(L)_(N_G (P)) ((P, -)) & = inf_(N_G (P) slash P, N_G (P)) (
                                         St_p (N_G (P) slash P)
                                       )
  $
  in $b(N_G (P))$ and $a(k N_G (P))$ respectively.
] <prop:upper-interval-equivalence>

#proof[
  By Theorem~@th:g-homotopy-equivalence, we only need show that
  $ (P, -)^H tilde.eq cal(S)_p (N_G (P) slash P)^H $
  for all $H <= N_G (P)$. Let
  $ i : cal(S)_p (N_G (P) slash P)^H arrow.r.hook (P, -)^H $
  denote the inclusion and
  $
    r : (P, -)^H & -> cal(S)_p (N_G (P) slash P)^H \
               Q & |-> N_Q (P) slash P.
  $
  Then it is easy to check that $r compose i = id$ while $i compose r(Q) <= Q$,
  so that $i$ and $r$ are homotopy inverses.
]

#remark(kind: "Comment")[
  The homotopy equivalence is due to Quillen, and the fact that the homotopy
  equivalence is equivariant is due to Webb.
]

Putting these together, we obtain the following theorem.

#theorem(closed: true)[
  In the Burnside ring $b(G)$, we have the identity
  $
    1 = - sum_("ccls of" \ p"-subgroups" \ 1 <= P <= G) ind_(N_G (P), G)
    tilde(Lambda)_(N_G (P)) (cal(S)_p (N_G (P) slash P)).
  $
  and in the representation ring $a(k G)$, the corresponding identity is the
  *Steinberg module inversion formula*
  $
    1 = - sum_("ccls of" \ p"-subgroups" \ 1 <= P <= G) ind_(N_G (P), G)
    inf_(N_G (P) slash P, N_G (P)) St_p (N_G (P) slash P)
  $
] <th:steinberg-inversion>

#remark(kind: "Remarks")[
  + If $P != O_p N_G (P)$ then $cal(S)_p (N_G (P) slash P)$ is contractible, and
    so we have $St_p (N_G (P) slash P) = 0$. Thus the Steinberg module inversion
    formula only has contributions from subgroups $P = O_p N_G (P)$.
  + We used Conlon's induction theorem#idx("Conlon's induction theorem")#idx(
      "induction theorem, Conlon's",
    )#idx("theorem", "Conlon's induction") to show that $St_p (G)$ is a virtual
    projective. Conversely the above formula shows that these statements are
    equivalent, since in $A(G)$, any virtual projective can be expressed as a
    $CC$-linear combination of modules induced from cyclic $p'$-subgroups.
]

#subhead[Length functions] For the rest of this section, we assume $k$ is
algebraically closed.

#definition[
  A *length function*#idx("length function")#idx("function", "length") on finite
  groups is an integer valued function on isomorphism classes of finite groups.
] <def:length-function>

#source(247)The following are the length functions we shall be interested in:
$
     l(G) & = "number of isomorphism classes of irreducible" k G"-modules" \
          & = "number of conjugacy classes of" p'"-elements" \
  f_0 (G) & = "number of isomorphism classes of projective irreducibles" \
          & quad "(“blocks of defect zero”)."
$
If $alpha$ is a length function, then $alpha$ gives rise to a linear map, also
denoted by $alpha$, defined as follows.
$
  alpha : b(G) & -> ZZ \
   (G slash H) & |-> alpha(H).
$

#proposition[
  Suppose that $alpha$ and $beta$ are length functions, and that $alpha$
  satisfies $alpha(G) = alpha(G slash O_p (G))$. Then the following are
  equivalent:
  #part-lines[
    + $alpha(G) = display(sum_("ccls of" \ p"-subgroups" \ 1 <= P <= G))
      beta(N_G (P) slash P)$
    + $beta(G) = -alpha(tilde(Lambda)(cal(S)_p (G)))$.
  ]
] <prop:length-function-equivalence>

#proof[
  Apply $alpha$ to the Steinberg module inversion formula to obtain
  $
    alpha(G) = - sum_("ccls of" \ p"-subgroups" \ 1 <= P <= G) alpha(
      tilde(Lambda)_(N_G (P)) (cal(S)_p (N_G (P) slash P))
    ).
  $
  Substituting (ii) in this yields (i), while substituting (i), and (ii) for all
  strictly smaller groups (by induction) yields (ii).
]

#subhead[Alperin's conjecture] Alperin has conjectured that for all finite
groups $G$,
$
  l(G) = sum_("ccls of" \ p"-subgroups" \ 1 <= P <= G) f_0 (N_G (P) slash P)
$
where $l(G)$ and $f_0 (G)$ are as above. If you know about Green correspondence,
the mnemonic for this statement is "the number of simple modules is equal to the
number of simple Green correspondents". Geoff Robinson's reformulation of this
conjecture (in the blockwise form in which it appeared in print, due to Knörr
and Robinson [@bib:Knorr1988]) is obtained by applying the above proposition.
This reformulation states that
$ f_0 (G) = -l(tilde(Lambda)_G (cal(S)_p (G))). $
The treatment of this reformulation using length functions is due to Webb.

#remark(kind: "Recent progress", punct: ":")[
  Since the first edition of this book was published, Peter Symonds
  [@bib:Symonds1996] had proved the conjecture of Webb appearing in
  Section~@sec:quillen-lemma. A lot of work has been done on Alperin's
  conjecture, but it still appears to be elusive.
]
