#import "main-defs.typ": *
#import "statements.typ": *

== The Künneth spectral sequence <sec:kunneth-sequence>
#idx("Künneth spectral sequence", target: [@sec:kunneth-sequence])#idx(
  "spectral sequence",
  "Künneth",
  target: [@sec:kunneth-sequence],
)

#definition[
  A double complex $P_(p q)$ is called a *proper projective resolution*#idx(
    "proper projective resolution",
  )#idx(
    "projective",
    "resolution, proper",
  )#idx("resolution", "proper projective") of the chain complex $bold(D)$ if for
  each value of $q$ the sequences
  $
    dots.c -> P_(2,q) -> P_(1,q) -> P_(0,q) -> D_q -> 0 \
    dots.c -> Z_q (P_(2,*)) -> Z_q (P_(1,*)) -> Z_q (P_(0,*)) -> Z_q (D_*)
    -> 0 \
    dots.c -> H_q (P_(2,*)) -> H_q (P_(1,*)) -> H_q (P_(0,*)) -> H_q (D_*)
    -> 0
  $
  are projective resolutions.
] <def:proper-projective-resolution>

#lemma[
  Every chain complex has a proper projective resolution.
] <lem:proper-resolution-exists>

#proof[
  Choose projective resolutions of $B_q (D_*)$ and $H_q (D_*)$ and apply the
  horseshoe lemma to the short exact sequences
  $
    0 -> B_q (D_*) -> Z_q (D_*) -> H_q (D_*) -> 0 \
    0 -> Z_q (D_*) -> D_q -> B_(q+1) (D_*) -> 0
  $
  to obtain appropriate projective resolutions $P_(p q)$ of the $D_q$ and maps
  between them. As usual, it is necessary to negate the maps on every other
  column to make $P_(**)$ a double complex.
]

#theorem[
  Suppose $bold(C)$ and $bold(D)$ are chain complexes of right, resp. left
  $Lambda$-modules and suppose the $C_n$ are flat. Then there is a spectral
  sequence
  $
    E^2_(p q) = plus.o.big_(s+t=q) Tor_p^Lambda (H_s (bold(C)), H_t (bold(D)))
    => H_(p+q) (bold(C) times.o_Lambda bold(D)).
  $
  If $bold(C)$ and $bold(D)$ are cochain complexes then there is a spectral
  sequence with
  $
    E_2^(p q) = plus.o.big_(s+t=q) Tor_(-p)^Lambda (H^s (bold(C)),
      H^t (bold(D))).
  $
  This is a "second quadrant spectral sequence" (i.e. $p <= 0$ and $q >= 0$) so
  there are convergence problems, but when the spectral sequence does converge,
  it does so to $H^(p+q) (bold(C) times.o_Lambda bold(D))$.
] <th:kunneth-spectral-sequence>

#proof[
  Form a proper projective resolution $P_(p q)$ of $bold(D)$, and tensor with
  $bold(C)$ in the vertical direction:
  $
    (bold(C) times.o_Lambda bold(P))_(p q) = plus.o.big_(s+t=q) C_s
    times.o_Lambda P_(p t).
  $
  Examine the two spectral sequences associated to this double complex. If we do
  the vertical differential first, each column is $C_* times.o_Lambda P_(p *)$.
  Since $Z(P_(p *))$ and $H(P_(p *))$ are projective (since $P_(p q)$ is a
  proper projective resolution of $bold(D)$), Corollary~2.7.2 to the Künneth
  theorem (Volume~I) implies that
  $
    E^1_(p q) = H_q (C_* times.o P_(p *)) = plus.o.big_(s+t=q) H_s (C_*)
    times.o H_t (P_(p *)).
  $
  #source(124)Since
  $
    dots.c -> H_t (P_(2 *)) -> H_t (P_(1 *)) -> H_t (P_(0 *)) -> H_t (D_*)
    -> 0
  $
  is a projective resolution, the homology of this complex with respect to the
  horizontal differential $d^1$ is
  $ E^2_(p q) = plus.o.big_(s+t=q) Tor_p (H_s (C_*), H_t (D_*)). $

  On the other hand, if we do the horizontal differential first, we obtain a
  spectral sequence in which $E^1$ consists of just the zeroth column, since the
  $C_n$ are flat so that the rows remain exact. The zeroth column is
  $Tot (bold(C) times.o bold(D))$ and so
  $E^2 = E^infinity = H_* (Tot (bold(C) times.o bold(D)))$. Thus the first
  spectral sequence also converges to the same answer.

  The case of cochain complexes is similar, with the stated proviso.
]
