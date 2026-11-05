#import "main-defs.typ": *
#import "statements.typ": *

== The Lefschetz Invariant <sec:lefschetz>
#idx("invariant, Lefschetz", target: [@sec:lefschetz])#idx(
  "Lefschetz",
  "invariant",
  target: [@sec:lefschetz],
)

Suppose $Delta$ is a finite $G$-simplicial complex. We wish to associate to
$Delta$ various representation theoretic invariants, and hence get information
about representations out of information about group actions, and vice-versa.

First we investigate what happens in characteristic zero.

#proposition[
  Suppose $k$ is a field of characteristic zero. Then we have
  $ sum_i (-1)^i H_i (Delta, k) = sum_i (-1)^i C_i (Delta, k) $
  as elements of the representation ring#idx("representation ring")#idx(
    "ring",
    "representation",
  ) $a(G)$#idx("$a(G)$") (see Chapter~5 of Volume~I).
] <prop:euler-characteristic-zero>

#proof[
  #source(231)Since we are in characteristic zero, all sequences of $G$-modules
  split. The chain complex
  $
    dots -> C_(n+1) (Delta, k) limits(arrow.r.long)^(partial_(n+1))
    C_n (Delta, k) limits(arrow.r.long)^(partial_n) C_(n-1) (Delta, k)
    -> dots
  $
  gives us short exact sequences
  $
    0 -> Im(partial_(n+1)) -> Ker(partial_n) -> H_n (Delta, k) -> 0 \
    0 -> Ker(partial_n) -> C_n (Delta, k) -> Im(partial_n) -> 0.
  $
  So in $a(G)$ we have
  $
    H_n (Delta, k) = Ker(partial_n) - Im(partial_(n+1)), wide
    C_n (Delta, k) = Ker(partial_n) + Im(partial_n),
  $
  and these expressions clearly have the same alternating sum.
]

In particular the *Euler characteristic*#idx("Euler characteristic")#idx(
  "characteristic",
  "Euler",
)
$ chi(Delta) = sum_i (-1)^i dim C_i (Delta, k) $
only depends on the homology of $Delta$, and is hence a homotopy invariant. The
*reduced Euler characteristic*#idx("reduced", "Euler characteristic") is the
corresponding concept for the augmented chain complex, namely
$tilde(chi)(Delta) = chi(Delta) - 1$.#idx("$chi(Delta)$, $tilde(chi)(Delta)$")

If the characteristic of $k$ divides the order of $G$, the above proposition is
no longer true, but we can still make the following definition.

#definition[
  The *Lefschetz module*#idx("Lefschetz", "module")#idx("module", "Lefschetz")
  $L_G (Delta, k)$#idx("$L_G (Delta, k)$, $tilde(L)_G (Delta, k)$") is defined
  to be the virtual module
  $ L_G (Delta, k) = sum_i (-1)^i C_i (Delta, k) in a(G). $
  The *reduced Lefschetz module*#idx("reduced", "Lefschetz module") is
  $
    tilde(L)_G (Delta, k) = sum_i (-1)^i tilde(C)_i (Delta, k)
    = L_G (Delta, k) - 1 in a(G).
  $
] <def:lefschetz-module>

#example[
  If $char k = p$, we call $tilde(L)_G (cal(S)_p (G), k)$ the *generalised
  Steinberg module*#idx("generalised", "Steinberg module")#idx(
    "module",
    "generalised Steinberg",
  ) for $G$ at the prime $p$. We shall see later that it is a virtual projective
  module#idx("virtual projective")#idx("projective", "virtual") (i.e., it lies
  in $a(G, 1)$, the linear span of the projective modules in $a(G)$). In the
  case where $G$ is a Chevalley group in characteristic $p$, it turns out to be
  equal to plus or minus the usual Steinberg module#idx("Steinberg module")#idx(
    "module",
    "Steinberg",
  ). We shall have more to say about this later.
]

The Lefschetz module has a precursor in the Burnside ring#idx(
  "Burnside ring",
)#idx("ring", "Burnside") $b(G)$ (see Chapter~5 of Volume~I), namely the
Lefschetz invariant, defined as follows. Let $c_n (Delta)$ denote the set of
$n$-simplices in $Delta$, regarded as a permutation representation of $G$, and
hence as an element of $b(G)$.

#definition[
  The *Lefschetz invariant* of $Delta$ is defined to be#idx(
    "$Lambda_G (Delta)$, $tilde(Lambda)_G (Delta)$",
  )
  $ Lambda_G (Delta) = sum_i (-1)^i c_i (Delta) in b(G). $
  The *reduced Lefschetz invariant* of $Delta$ is
  $tilde(Lambda)_G (Delta) = Lambda_G (Delta) - 1$.
] <def:lefschetz-invariant>

#source(232)Under the natural map $b(G) -> a(k G)$ we have
$Lambda_G (Delta) |-> L_G (Delta, k)$. Recall from Section~5.4 of Volume~I that
we have a natural inclusion
$
  b(G) & arrow.r.hook plus.o.big_(H lt.eq_G G) ZZ \
     X & |-> |X^H|.
$
In particular
$
  Lambda_G (Delta) |-> sum_i (-1)^i . |(Delta_((i)))^H| = chi(Delta^H)
$
the Euler characteristic of the fixed point set $Delta^H$. So knowing
$Lambda_G (Delta)$ is equivalent to knowing $chi(Delta^H)$ for all $H <= G$.

#exercises[
  + Show that $sum_i (-1)^i H_i (Delta, k)$ and $sum_i (-1)^i C_i (Delta, k)$
    have the same Brauer character, or equivalently the same image in the
    Grothendieck ring of $k G$-modules.
  + Show that if $Delta$ and $Delta'$ are finite $G$-simplicial complexes, then
    #enum(numbering: "(i)")[
      $Lambda_G (Delta dot(union) Delta')
      = Lambda_G (Delta) + Lambda_G (Delta')$,
    ][
      $Lambda_G (Delta times Delta') = Lambda_G (Delta) . Lambda_G (Delta')$.
    ]
]
