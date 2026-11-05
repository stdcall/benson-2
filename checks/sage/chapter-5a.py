"""Exact checks of Chapter 5, Sections 5.1-5.8 (Sage, with GAP through
libgap and Singular).

Benson, *Representations and Cohomology II*, first paperback edition (1998),
Chapter 5 "Varieties for modules and multiple complexes", from the chapter
heading through Section 5.8, printed pp. 153-186.  Our files:
content/05-00-varieties.typ ... content/05-08-rank-varieties.typ.
(Sections 5.9-5.18 are checked in a separate script; this one imports
nothing from it.)

Group cohomology H^*(G, F_p) of p-groups (GAP's SmallGroups as
multiplication tables) is computed from minimal resolutions over F_p[G]
built here by linear algebra, with Yoneda products by lifted chain maps,
restriction (chain maps from resolutions of subgroups, from the tensor
product of periodic resolutions of an elementary abelian subgroup, from the
periodic resolution of a cyclic shifted subgroup), inflation, cochains with
coefficients in modules and the coefficient map F -> End(M), i.e. Phi_M.
For E elementary abelian, H^*(E, M) is the homology of M (x) F[x_1, ...,
x_r] with the differential sum (g_i - 1) x_i (p = 2), resp. of the tensor
product of periodic resolutions as a module over F[beta x_1, ...,
beta x_r] (p odd); annihilators, radicals, minors, eliminations, Krull
dimensions and Hilbert series are computed by Singular.  Varieties over
the algebraic closure are compared through radicals of ideals defined over
the finite field.  Expected values are the book's statements read off the
printed pages (page and number in each message); the chapter files are not
parsed.  Where the printed text was corrected, the printed reading is kept
as a refuted check beside the corrected one.

Checked here:

5.1 (pp. 153-154): x y = (-1)^(deg x deg y) y x, and x^2 = 0 for x of odd
  degree (p odd), in H^*(G, F_p) through degree 5 or 6 for C3, C9, C3 x C3,
  3^(1+2)_+-, C4, C4 x C2, D8, Q8, SmallGroup(16, 3), (16, 6), Q8 x C2;
  complexity zero: F[G] has the resolution 0 -> F[G], while the minimal
  resolution of F never stops (D8, Q8, C3 x C3); complexity one: F over C4,
  Q8, C9, C3 has bounded ranks and Omega^n F = F for the period n = 2, 4,
  2, 2 (MeatAxe), F over D8, V4, C3 x C3 unbounded ranks.
5.2 (pp. 155-157): Theorem 5.2.1 (Quillen-Venkov) for M = F, as the proof
  gives it: for every subgroup H of index p of 25 groups (C4, V4, C8,
  C4 x C2, D8, Q8, (Z/2)^3, the 13 groups of order 16 other than C16 and
  (Z/2)^4, C9, C3 x C3, 3^(1+2)_+-, C9 x C3; degrees <= 6 to 8) the products
  of elements of positive degree in Ker(res_(G,H)) lie in beta(x) H^*(G)
  (beta(x) = x^2 for p = 2, the inflation of the generator of H^2(G/H) for
  p odd); Serre's theorem (Theorem 4.7.3) as used in Theorem 5.2.2: a
  product of Bocksteins of non-zero degree one classes vanishes for each
  group that is not elementary abelian, none for V4, (Z/2)^3, C3 x C3 (in
  range); Theorem 5.2.2 for M = F: the kernel of restriction to the maximal
  elementary abelian subgroups consists of nilpotent elements (C4, C8, Q8,
  D8, C4 x C2, (16, 4), Q8 x C2, C9, 3^(1+2)_-; degrees <= N/4 resp. N/2);
  Lemma 5.2.3 and Theorem 5.2.4 (Chouinard) on modules (permutation modules
  on all subgroups, Omega^(+-1) F, Omega^2 F, F + F[G], a tensor product,
  random quotients of F[G]^2) for D8, Q8, C4 x C2, C4, Q8 x C2.
5.3 (pp. 157-161): p(k[x_1, ..., x_n], t) = 1 / (1 - t)^n (n <= 5); the
  Exercise p. 161 (ranks r^n over k E / J^2, so 1 / (1 - r t); r <= 3,
  p = 2, 3, 5); Proposition 5.3.1 and its proof (the polynomial g(t) has
  degree < k_s, here g = 0), Proposition 5.3.2 (reduction to k_j = 1, the
  binomial formula, a polynomial of degree exactly gamma - 1, growth through
  n = 400), additivity of gamma, Theorem 5.4.6 (ii) and Lemma 5.3.6
  (nilpotency index <= sum n_i, gamma(A/J) = gamma(A)) on seven graded rings
  (H^*(D8), H^*(Q8), F2[x,y]/(x^2, xy), F2[x,y]/(x^2 y), a ring over F3 with
  generators of degrees 2, 3, 4, the ring of 2^(1+4)_-, the Dickson
  algebra); p. 159: b_r(M) = dim Ext^r(M, F) = dim H^r(G, M^*) (computed from
  the resolution of F) and dim Ext^r(M, N) <= dim P_r . dim N for modules
  over D8, Q8, C4 x C2, C3 x C3; Theorem 5.3.8 (Quillen) for 19 groups of
  order <= 16: H^*(G, F_2) presented by generators of degree <= 5 and
  relations of degree <= 10, with Hilbert series equal to the ranks of the
  minimal resolution through degree 10, has Krull dimension r_2(G); the
  Poincare series 1 / (1 - t)^n of (Z/p)^n (p = 2, n <= 4; p = 3, n <= 3;
  p = 5, n = 2) and H^*(Z/9, F_3).
5.4 (pp. 161-169): residue fields of maximal ideals over non-closed fields
  (proof of Lemma 5.4.1); Theorem 5.4.2 with the corrected hypothesis (v in
  V(I)) and its proof on 15 pairs (I, f) over GF(2), GF(3), QQ:
  f_1, ..., f_s, 1 - f t generate the unit ideal iff f is in sqrt(I), and
  t = 1/f gives f^r = sum f_i h_i; V(I_1 I_2), V(I_1 + I_2) and minimal
  primes (16 random pairs); dilations (Exercise p. 164) and the line through
  a point; the localisation p. 165: the printed S (non-zero-divisors modulo
  I) is refuted for A = k[x], I = (x) over GF(2), GF(3), GF(5) and for
  k[x, y], (x, y); the corrected S = {f^n} confirmed; homogeneous Noether
  normalisation (Lemma 5.4.5) for the graded rings above, chains of primes
  and transcendence degree (Theorem 5.4.6); p. 167: the dominant map (x, y)
  |-> (x, x y) over GF(2), GF(3), GF(4), GF(5), GF(7) and QQ has image
  {u != 0} u {(0, 0)}: the printed "image is open" is refuted, "contains a
  dense open subset" confirmed; a dominant, non-finite, non-surjective map
  and a finite surjective one (Theorem 5.4.7); the inseparable isogenies
  max k[x, y] -> max k[x^2, x y, y^2] (GF(2^m), m <= 4) and max k[x] ->
  max k[x^3, x^4] (GF(3^m), m <= 3); Proposition 5.4.8 for GL_2(F_2) on
  F_2[x, y] (the Dickson invariants through degree 12, fibres = orbits on
  GF(4)^2, GF(16)^2); Definition 5.4.9, Theorem 5.4.10 (H^*(D8), H^*(Q8)
  free over four resp. three systems of parameters, F2[x,y]/(x^2, xy) of
  depth 0 free over none); Theorem 5.4.11 (Macaulay) for 75 random
  homogeneous sequences, and a non-homogeneous sequence showing that the
  homogeneity of Definition 5.4.9 is needed.
5.5 (pp. 169-172): Lemma 5.5.1, Proposition 5.5.2 and the last sentence of
  Theorem 5.5.3 for all quadratic forms on F_2^n, n <= 3 (74 forms), 40 of
  the 1024 forms on F_2^4 and 10 on F_2^5: the maximal isotropic subspaces
  have codimension h; q(v), b(v, F v), ..., b(v, F^(h-1) v) is a regular
  sequence (colon ideals, Hilbert series); its variety is the union of the
  k (x) E', E' maximal isotropic; V(J_r) decreases strictly up to r = h and
  V(J_h) = V(J_(h+1)); b(v, F^r v) lies in J_h for h <= r <= h + 2;
  Sq^(2^(r-1)) ... Sq^1 q(v) = b(v, F^r v) (r <= 3, Cartan formula).  The
  display p. 170 with all sums from i = 0 (identity in k[V][lambda], all
  forms, n = 2, 3, r <= 3); with the printed lower limits 1 the expansion
  vanishes identically at v = (1, w) for the form of Q8 though b(v, F v) =
  1: refuted as a description of V(J_r).  Theorem 5.5.3 for the 14 groups
  of order <= 32 with |Phi(G)| = 2 (C4, C4 x C2, D8, Q8, four of order 16,
  six of order 32 including 2^(1+4)_+-): (x y)^2 = x^2 y^2 [x, y] and q a
  quadratic form with polar form the commutator; 2^h is the index of every
  maximal elementary abelian subgroup; the Poincare series prod (1 -
  t^(d_i)) / ((1 - t)^n (1 - t^(2^h))) through degree 6 to 10; restriction
  to N is zero in degrees 0 < j < 2^h and non-zero in degree 2^h; where
  2^h <= N, H^* = F_2[x_1, ..., x_n]/J_h (x) F_2[zeta] through degree N
  (generators and the exact relations).  Exercise 2 p. 172 for n = 2, 3
  (orders 16, 64): some x in H^1(G, F_2) has x^n != 0 = x^(n+1); read with
  F_p, p odd, H^1(G, F_p) = 0.
5.6 (pp. 172-175): Corollary 5.6.4 for V4, (Z/2)^3, C4, C4 x C2, D8, Q8,
  C8, D8 x C2: q_G lands in lim_E H^*(E) (all elementary abelian
  subgroups, inclusions and conjugations), its kernel is nilpotent, and the
  2^a-th power of every element of the limit is in the image (a = 0, 0, 1,
  1, 0, 2, 2, 0; for a = 0 an isomorphism in the computed degrees); Lemma
  5.6.2 (i) and (ii) for D8, Q8, C4 x C2 (rho_E and y'); the Exercise p. 175
  (the 1-eigenspace of 1 != w in GL_r(F_p) is a proper rational subspace;
  (p, r) = (2, 2), (2, 3), (3, 2)).
5.7 (pp. 176-180), for E = (Z/2)^2 over GF(2), GF(4) and (Z/2)^3 over
  GF(2), on F, F[E], Omega^(+-1) F, Omega^2 F, V_(1, alpha) (alpha in {0,
  1, infinity} and GF(4)), V_(2, w), V_(2, 1), Carlson's M_(a,b,c) for all
  (a, b, c) in F_2^3, the period-one module, permutation modules and random
  quotients: Proposition 5.7.1 (V_E(M) = V_E(k, M)), 5.7.2 (b_n(M) = dim
  H^n(E, M^*), n <= 9, with growth n^(dim V - 1) by finite differences),
  5.7.3, 5.7.5, 5.7.7, Corollary 5.7.9, Theorem 5.7.11, Corollary 5.7.12;
  for D8 and Q8 (I_G(M) = Ker Phi_M through degree 8, H^*(G) presented,
  res^(-1) by elimination): Proposition 5.7.4, Corollary 5.7.9 and
  Proposition 5.7.2 with Theorem 5.3.7 (Alperin-Evens).
5.8 (pp. 180-186): shifted subgroups ((p, r, q) = (2, 2, 4), (2, 3, 4),
  (3, 2, 9), (5, 2, 5), four random lambda each): the 1 + v_i commute, have
  order p, generate a group of order p^r and exponent p, the inverse
  automorphism is given by (mu_ij), k E is free over k <1 + v_1, ..., 1 +
  v_s>; 1 + v is not group-like (not a Hopf algebra map); Lemma 5.8.2 and
  the Remark: res(x_i) = lambda_i and res(beta x_i) = lambda_i^p on every
  cyclic shifted subgroup (all lambda in GF(4)^2, GF(9)^2; 25 in GF(9)^3, 30
  in GF(25)^2), the linear identification for p odd refuted; pp. 182-183
  for (Z/3)^2, (Z/3)^3, (Z/5)^2, identically in the lambda_i: Omega^2 k is
  generated by the b_i and c_ij, v^(p-1)(sum lambda_i gamma_i) = sum
  lambda_i^p b_i modulo Rad(Omega^2 k), the expansion into two sums,
  binom(p - 1, j) = (-1)^j, the corrected bracket (in Omega^2 k; the printed
  one refuted, its image under delta is non-zero) and the cancellation; the
  rank criterion (random modules for Z/2, Z/3, Z/5); Carlson's favourite
  example symbolically in a, b, c, lambda and Theorem 5.8.3 for six random
  (a, b, c) in GF(4)^3; Carlson's example with V_(1, alpha) for all 17
  alpha in GF(16) u {infinity}; the period-one module p. 185 (Omega M = M,
  H^n(E, M) one dimensional, Hom(k, M) = <e_4>, zeta not through a
  projective, through a projective on every cyclic shifted subgroup over
  GF(q), q <= 16, V(M) a line); the proof of Theorem 5.8.3 (a shifted
  subgroup of maximal rank is not cyclic: the printed "cyclic" refuted;
  replacing E by a shifted subgroup of maximal rank changes V_E(M) by the
  linear map lambda); Corollary 5.8.4 (Dade) on random modules of dimension
  <= 9 for (Z/2)^2 (GF(2), GF(4)), (Z/2)^3, (Z/3)^2, and V_(2, w) over F_2,
  free on all F_2-rational cyclic shifted subgroups but not free; Corollary
  5.8.5 with the trace argument; Theorem 5.8.3 for (Z/3)^2 over GF(3) and
  GF(9) with the Frobenius twist (untwisted refuted over GF(9)); Theorem
  5.1.1 (vii) for random zeta of degrees 1-3 (p = 2) and 2, 4 (p = 3), and
  (viii) for L_(x_1 x_2) (two summands, the two lines) and L_zeta, zeta =
  x_1^2 + x_1 x_2 + x_2^2 (indecomposable over F_2, two summands over
  GF(4)).

Not established: none of the general theorems is proved here.  Every check
concerns the listed groups, modules, forms, fields and degrees; cohomology
rings are known only through the stated degrees (the presentations are
those of the subalgebra generated in low degrees with relations through
degree N), I_G(M) only through degree 8, growth rates only through finite
differences.  Not checked: Theorems 5.2.1 and 5.2.2 for modules M != F; the
inseparable isogeny of Theorem 5.6.3 beyond Corollary 5.6.4; the
Avrunin-Scott stratification (Theorem 5.7.8) beyond Proposition 5.7.4;
Proposition 5.7.10; the Lyndon-Hochschild-Serre pages and the norm argument
in the proof of Theorem 5.5.3; Exercise 1 p. 172 and E_3 = E_infinity in
Exercise 2; the Exercise pp. 168-169; the Remark p. 175 (Gunawardena,
Lannes and Zarati) and the Remark pp. 184-185 (Niwasaki).  Nothing here
compares our Typst text with the printed book.

Run with:  sage -python checks/sage/chapter-5a.py  (about two minutes)
"""
import itertools
import random
import sys

from sage.all import (GF, ZZ, QQ, matrix as _matrix, vector, libgap,
                      PolynomialRing, TermOrder, binomial, block_matrix,
                      factorial, PowerSeriesRing, gcd, set_random_seed)
from sage.libs.singular.function import singular_function

SCOPE = 'chapter-5a'
COUNT = [0]
RNG = random.Random(20261105)
SYZ = singular_function('syz')
QUOTIENT = singular_function('quotient')
MINOR = singular_function('minor')


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


# ===========================================================================
# Linear algebra over finite fields (sparse in odd characteristic: dense
# products over GF(p), p odd, stop with SIGILL in the local OpenBLAS build)
# ===========================================================================


def _sp(F):
    return F.characteristic() != 2


def mat(F, r, c, entries=None):
    return _matrix(F, r, c, entries or {}, sparse=_sp(F))


def mrows(F, rows, ncols=None):
    """A matrix from a list of rows (sparse in odd characteristic)."""
    if ncols is not None and not rows:
        return mat(F, 0, ncols)
    return _matrix(F, [list(r) for r in rows], sparse=_sp(F))


def kron(F, A, B):
    """The Kronecker product A (x) B (blocks a_ij B), sparse for p odd."""
    if not _sp(F):
        return A.tensor_product(B)
    ent = {}
    br, bc = B.nrows(), B.ncols()
    Bd = B.dict()
    for (i, j), a in A.dict().items():
        for (k, l), b in Bd.items():
            ent[(i * br + k, j * bc + l)] = a * b
    return mat(F, A.nrows() * br, A.ncols() * bc, ent)


def ident(F, n):
    return mat(F, n, n, {(i, i): 1 for i in range(n)})


def hcat(F, n, mats):
    mats = [A for A in mats if A.ncols()]
    if not mats:
        return mat(F, n, 0)
    if len(mats) == 1:
        return mats[0]
    if _sp(F):
        ent, off = {}, 0
        for A in mats:
            assert A.nrows() == n
            for (i, j), x in A.dict().items():
                ent[(i, j + off)] = x
            off += A.ncols()
        return mat(F, n, off, ent)
    return block_matrix(F, 1, len(mats), mats, subdivide=False)


def vcat(F, n, mats):
    mats = [A for A in mats if A.nrows()]
    if not mats:
        return mat(F, 0, n)
    out = mats[0]
    for A in mats[1:]:
        out = out.stack(A)
    return out


def rk(A):
    return A.rank() if A.nrows() and A.ncols() else 0


def kernel_cols(A):
    F = A.base_ring()
    if A.ncols() == 0:
        return mat(F, 0, 0)
    if A.nrows() == 0:
        return ident(F, A.ncols())
    K = A.right_kernel_matrix()
    if _sp(F) and not K.is_sparse():
        K = K.sparse_matrix()
    if not _sp(F) and K.is_sparse():
        K = K.dense_matrix()
    return K.transpose()


def colbasis(A):
    if A.ncols() == 0 or A.nrows() == 0:
        return mat(A.base_ring(), A.nrows(), 0)
    return A.matrix_from_columns(A.pivots())


def in_span(S, V):
    if V.ncols() == 0:
        return True
    if S.ncols() == 0:
        return V.is_zero()
    return rk(S.augment(V)) == rk(S)


# ===========================================================================
# Finite groups as multiplication tables (from GAP)
# ===========================================================================


class Grp:
    def __init__(self, n, mul, e, gens, name):
        self.n, self.mul, self.e, self.gens, self.name = n, mul, e, gens, name
        self.inv = [next(b for b in range(n) if mul[a][b] == e)
                    for a in range(n)]
        self.src = [[mul[self.inv[h]][t] for t in range(n)]
                    for h in range(n)]
        self.order = []
        for a in range(n):
            k, x = 1, a
            while x != e:
                x = mul[x][a]
                k += 1
            self.order.append(k)

    @classmethod
    def from_gap(cls, G, name):
        els = libgap.AsSSortedList(G)
        tbl = libgap.MultiplicationTable(els).sage()
        mul = [[x - 1 for x in row] for row in tbl]
        e = int(libgap.Position(els, libgap.One(G))) - 1
        gens = libgap.MinimalGeneratingSet(G) if int(G.Size()) > 1 else []
        gi = [int(libgap.Position(els, g)) - 1 for g in gens]
        out = cls(len(mul), mul, e, gi, name)
        out.gap, out.els = G, els
        return out

    def closure(self, gens):
        S = {self.e}
        frontier = [self.e]
        while frontier:
            new = []
            for a in frontier:
                for g in gens:
                    b = self.mul[a][g]
                    if b not in S:
                        S.add(b)
                        new.append(b)
            frontier = new
        return sorted(S)

    def comm(self, a, b):
        """[a, b] = a^(-1) b^(-1) a b."""
        m, iv = self.mul, self.inv
        return m[m[m[iv[a]][iv[b]]][a]][b]

    def conj(self, g, x):
        return self.mul[self.mul[g][x]][self.inv[g]]

    def center(self):
        return [z for z in range(self.n)
                if all(self.mul[z][g] == self.mul[g][z]
                       for g in range(self.n))]

    def right_cosets(self, H):
        seen, T, dec = set(), [], {}
        for x in range(self.n):
            if x in seen:
                continue
            T.append(x)
            for h in H:
                y = self.mul[h][x]
                seen.add(y)
                dec[y] = (h, x)
        return T, dec

    def quotient(self, N, name):
        """G/N (N normal) as a table group with the projection."""
        T, dec = self.right_cosets(N)
        tix = {t: i for i, t in enumerate(T)}
        proj = [tix[dec[x][1]] for x in range(self.n)]
        mul = [[proj[self.mul[a][b]] for b in T] for a in T]
        gens = sorted(set(proj[g] for g in self.gens) - {proj[self.e]})
        Q = Grp(len(T), mul, proj[self.e], gens, name)
        return Q, proj

    def subgroup(self, H, name):
        """The table group of a subgroup H (list of elements) and the
        inclusion (H-index -> G-index)."""
        H = sorted(H)
        ix = {h: i for i, h in enumerate(H)}
        mul = [[ix[self.mul[a][b]] for b in H] for a in H]
        gens, S = [], [self.e]
        for h in sorted(H, key=lambda x: -self.order[x]):
            if h not in S:
                gens.append(h)
                S = self.closure(gens)
        assert S == H
        sub = Grp(len(H), mul, ix[self.e], [ix[g] for g in gens], name)
        return sub, H

    def elementary_abelian_subgroups(self, p):
        """All elementary abelian p-subgroups (sorted element lists)."""
        invols = [a for a in range(self.n) if self.order[a] == p]
        found = {(self.e,)}
        frontier = [(self.e,)]
        while frontier:
            new = []
            for S in frontier:
                Ss = set(S)
                for a in invols:
                    if a in Ss:
                        continue
                    if all(self.mul[a][s] == self.mul[s][a] for s in S):
                        T = tuple(self.closure(list(S) + [a]))
                        if T not in found:
                            found.add(T)
                            new.append(T)
            frontier = new
        return [list(S) for S in sorted(found, key=len)]

    def conj_classes_of(self, subs):
        """Representatives of the conjugacy classes in a list of subgroups."""
        reps, seen = [], set()
        for S in subs:
            key = tuple(S)
            if key in seen:
                continue
            reps.append(S)
            for g in range(self.n):
                seen.add(tuple(sorted(self.conj(g, x) for x in S)))
        return reps


def rank_of(n, p):
    r = 0
    while p ** r < n:
        r += 1
    assert p ** r == n
    return r


# ===========================================================================
# Modules over F[G] and minimal resolutions (G a p-group)
# ===========================================================================


class Mod:
    """A left F[G]-module given by the matrices act[g] of all g."""

    def __init__(self, F, G, dim, act):
        self.F, self.G, self.dim, self.act = F, G, dim, act

    @classmethod
    def from_gens(cls, F, G, genact, gens=None):
        gens = G.gens if gens is None else gens
        dim = genact[0].nrows()
        act = {G.e: ident(F, dim)}
        frontier = [G.e]
        while frontier:
            new = []
            for a in frontier:
                for g, A in zip(gens, genact):
                    b = G.mul[g][a]
                    if b not in act:
                        act[b] = A * act[a]
                        new.append(b)
            frontier = new
        assert len(act) == G.n
        M = cls(F, G, dim, act)
        for a in range(G.n):
            for g in gens:
                assert act[G.mul[g][a]] == act[g] * act[a], 'not a module'
        return M

    def lam(self, v):
        out = mat(self.F, self.dim, self.dim)
        for g, c in v.items():
            if c:
                out += c * self.act[g]
        return out

    def X(self, g):
        return self.act[g] - ident(self.F, self.dim)


def trivial(F, G):
    return Mod(F, G, 1, {g: ident(F, 1) for g in range(G.n)})


def regular_module(F, G):
    return Mod(F, G, G.n, {h: mat(F, G.n, G.n, {(G.mul[h][t], t): 1
                                                for t in range(G.n)})
                           for h in range(G.n)})


def perm_module(F, G, H):
    """F[G/H] on the left cosets g H."""
    cos, where = [], {}
    for g in range(G.n):
        if g in where:
            continue
        c = sorted(G.mul[g][h] for h in H)
        for x in c:
            where[x] = len(cos)
        cos.append(c)
    m = len(cos)
    return Mod(F, G, m, {g: mat(F, m, m, {(where[G.mul[g][c[0]]], i): 1
                                          for i, c in enumerate(cos)})
                         for g in range(G.n)})


def dual(M):
    return Mod(M.F, M.G, M.dim, {g: M.act[M.G.inv[g]].transpose()
                                 for g in range(M.G.n)})


def tensor(M, N):
    return Mod(M.F, M.G, M.dim * N.dim,
               {g: kron(M.F, M.act[g], N.act[g]) for g in range(M.G.n)})


def direct_sum(M, N):
    return Mod(M.F, M.G, M.dim + N.dim,
               {g: block_diag(M.F, [M.act[g], N.act[g]])
                for g in range(M.G.n)})


def end_module(M):
    """End_k(M) = M (x) M^* with g . f = g f g^(-1); the identity is
    vec(I)."""
    return tensor(M, dual(M))


def sub_action(M, K):
    """The submodule with basis columns K (full column rank)."""
    F, G = M.F, M.G
    act = {}
    for g in range(G.n):
        act[g] = K.solve_right(M.act[g] * K)
    return Mod(F, G, K.ncols(), act)


def quotient_action(M, K):
    """M / (submodule with basis columns K)."""
    F, G = M.F, M.G
    n = M.dim
    B = colbasis(K.augment(ident(F, n)))
    k = K.ncols()
    # B: first k columns K, then complement C
    act = {}
    for g in range(G.n):
        A = B.solve_right(M.act[g] * B)
        act[g] = A.submatrix(k, k, n - k, n - k)
    return Mod(F, G, n - k, act)


def restrict(M, Hsub, incl):
    return Mod(M.F, Hsub, M.dim, {h: M.act[incl[h]] for h in range(Hsub.n)})


def fixed_points(M):
    F = M.F
    A = vcat(F, M.dim, [M.X(g) for g in M.G.gens])
    return kernel_cols(A)


def top_generators(M):
    """Number of generators of M (dim M / J M) for a p-group."""
    F = M.F
    JM = hcat(F, M.dim, [M.X(g) for g in M.G.gens])
    return M.dim - rk(JM)


def is_free(M):
    """M free over F[G] (G a p-group)."""
    return top_generators(M) * M.G.n == M.dim


def act_free(G, b, h, X):
    """h . X for columns X of F[G]^b (index j n + t = basis element t e_j)."""
    if h == G.e:
        return X
    n = G.n
    return X.matrix_from_rows([j * n + G.src[h][t] for j in range(b)
                               for t in range(n)])


def free_map(F, G, b_src, X):
    """The F-matrix of F[G]^(b_src) -> F[G]^b, e_i |-> column i of X;
    columns ordered i n + g (= g e_i)."""
    n = G.n
    b = X.nrows() // n
    parts = [act_free(G, b, g, X) for g in range(n)]
    Y = hcat(F, X.nrows(), parts)
    return Y.matrix_from_columns([g * b_src + i for i in range(b_src)
                                  for g in range(n)])


def mod_map(F, G, M, X):
    """F[G]^b -> M with e_i |-> column i of X."""
    b = X.ncols()
    Y = hcat(F, M.dim, [M.act[g] * X for g in range(G.n)])
    return Y.matrix_from_columns([g * b + i for i in range(b)
                                  for g in range(G.n)])


def min_generators(K, JK):
    """Columns of K completing a basis of JK to one of K."""
    JB = colbasis(JK)
    nb = JB.ncols()
    allc = JB.augment(K) if nb else K
    return [c - nb for c in allc.pivots() if c >= nb]


class Resolution:
    """The minimal resolution P_* -> M over F[G] (G a p-group) up to degree
    nmax: b[n] generators, d[n] : P_n -> P_(n-1) (F-matrices, column i n + g
    is g d(e_i)), eps : P_0 -> M."""

    def __init__(self, M, nmax):
        F, G = M.F, M.G
        self.F, self.G, self.M = F, G, M
        n = G.n
        I = ident(F, M.dim)
        gens = min_generators(I, hcat(F, M.dim, [M.X(g) for g in G.gens]))
        X = I.matrix_from_columns(gens)
        self.b = [len(gens)]
        self.eps = mod_map(F, G, M, X)
        self.d = {}
        prev = self.eps
        for k in range(1, nmax + 1):
            bp = self.b[k - 1]
            K = kernel_cols(prev)
            JK = hcat(F, K.nrows(), [act_free(G, bp, g, K) - K
                                     for g in G.gens])
            gens = min_generators(K, JK)
            X = K.matrix_from_columns(gens)
            self.b.append(len(gens))
            self.d[k] = free_map(F, G, len(gens), X) if gens else \
                mat(F, bp * n, 0)
            assert rk(self.d[k]) == K.ncols()     # exact at P_(k-1)
            prev = self.d[k]
        self.nmax = nmax

    def dim(self, k):
        return self.b[k] * self.G.n

    def gen_cols(self, k):
        n, e = self.G.n, self.G.e
        return self.d[k].matrix_from_columns([i * n + e
                                              for i in range(self.b[k])])

    def omega(self, k):
        """Omega^k(M) as a module (the image of d_k, k >= 1; Omega^0 = M is
        not returned)."""
        A = self.d[k]
        B = colbasis(A)
        b = self.b[k - 1]
        G = self.G
        act = {g: B.solve_right(act_free(G, b, g, B)) for g in range(G.n)}
        return Mod(self.F, G, B.ncols(), act)


def collapse(F, G, X, b):
    """Sums of the coefficients of columns X of F[G]^b block by block: the
    values of cochains with trivial coefficients."""
    n = G.n
    S = mat(F, b, b * n, {(j, j * n + t): 1 for j in range(b)
                          for t in range(n)})
    return S * X


def pullback_matrix(M, G, Y, b_tgt):
    """For F[G]-linear T : P_a -> P_c with generator images Y (columns in
    F[G]^(b_tgt)), the matrix of Hom_G(P_c, M) -> Hom_G(P_a, M), psi |->
    psi o T, in the coordinates (psi(e_j))_j: the sum over g of
    C_g (x) act[g] with C_g[i, j] the coefficient of g e_j in T(e_i)."""
    F = M.F
    n, m = G.n, M.dim
    A = mat(F, Y.ncols() * m, b_tgt * m)
    if Y.ncols() == 0 or b_tgt == 0:
        return A
    for g in range(n):
        Cg = Y.matrix_from_rows([j * n + g for j in range(b_tgt)]).transpose()
        if Cg.is_zero():
            continue
        A += kron(F, Cg, M.act[g])
    return A


class Cohom:
    """H^*(G, F) for a p-group from the minimal resolution P of F: H^n =
    F^(b_n) (values on the generators), Yoneda products by lifted chain
    maps; cochains with coefficients in modules."""

    def __init__(self, G, F, nmax):
        self.G, self.F, self.N = G, F, nmax
        self.P = Resolution(trivial(F, G), nmax)
        self.b = self.P.b
        self.p = F.characteristic()
        a = self.P.eps[0, G.e]
        assert a != 0
        self.x0 = mat(F, self.P.dim(0), 1, {(G.e, 0): 1 / a})
        self._lifts = {}
        self._mm = {}

    def lift(self, m, alpha, kmax):
        """tau_k : P_(m+k) -> P_k (generator images) lifting the cocycle
        alpha in degree m."""
        key = (m, tuple(alpha))
        tau = self._lifts.setdefault(key, {})
        F, G, P = self.F, self.G, self.P
        for k in range(kmax + 1):
            if k in tau or m + k > self.N:
                continue
            bmk = self.b[m + k]
            if k == 0:
                tau[0] = self.x0 * mat(F, 1, bmk, {(0, i): alpha[i]
                                                   for i in range(bmk)
                                                   if alpha[i]})
            elif bmk == 0:
                tau[k] = mat(F, P.dim(k), 0)
            else:
                full = free_map(F, G, self.b[m + k - 1], tau[k - 1])
                tau[k] = P.d[k].solve_right(full * P.gen_cols(m + k))
        return tau

    def mult_matrix(self, m, alpha, k):
        """beta |-> beta o alpha : H^k -> H^(k+m)."""
        key = (m, tuple(alpha), k)
        if key not in self._mm:
            tau = self.lift(m, alpha, k)
            C = collapse(self.F, self.G, tau[k], self.b[k])
            self._mm[key] = C.transpose()
        return self._mm[key]

    def mul(self, beta, l, alpha, m):
        """The Yoneda composite beta o alpha (beta in H^l, alpha in H^m)."""
        assert l + m <= self.N
        return self.mult_matrix(m, list(alpha), l) * vector(self.F, beta)

    def power(self, alpha, m, e):
        out, deg = vector(self.F, alpha), m
        for _ in range(e - 1):
            out = self.mul(out, deg, alpha, m)
            deg += m
        return out

    def hom_of(self, alpha):
        """The homomorphism G -> F of a class in H^1."""
        F, G, P = self.F, self.G, self.P
        out = []
        for g in range(G.n):
            tgt = act_free(G, self.b[0], g, self.x0) - self.x0
            y = P.d[1].solve_right(tgt)
            out.append((collapse(F, G, y, self.b[1]).column(0)
                        * vector(F, alpha)))
        return out

    def class_of_hom(self, chi):
        """The class in H^1 of a homomorphism chi : G -> F (list)."""
        F = self.F
        rows = [self.hom_of([1 if i == j else 0 for i in range(self.b[1])])
                for j in range(self.b[1])]
        A = mrows(F, rows).transpose()          # n x b_1
        return A.solve_right(vector(F, chi))

    # cochains with coefficients in a module ------------------------------
    def cochain_delta(self, M, n):
        """delta : Hom_G(P_n, M) -> Hom_G(P_(n+1), M)."""
        return pullback_matrix(M, self.G, self.P.gen_cols(n + 1), self.b[n])

    def coefficient_kernel(self, M, n):
        """The kernel I_G(M) in degree n of H^n(G, F) -> H^n(G, End(M))
        induced by F -> End(M), 1 |-> id (i.e. of Phi_M), as a basis
        matrix (columns)."""
        E = end_module(M)
        F = self.F
        m = E.dim
        idv = [1 if r % (M.dim + 1) == 0 else 0 for r in range(m)]
        B = self.cochain_delta(E, n - 1) if n >= 1 else mat(F, 0, 0)
        U = mat(F, self.b[n] * m, self.b[n],
                {(j * m + r, j): 1 for j in range(self.b[n])
                 for r in range(m) if idv[r]})
        # alpha in ker iff U alpha in Im B
        if B.ncols() == 0:
            return kernel_cols(U)
        Bb = colbasis(B)
        A = Bb.augment(U)
        K = kernel_cols(A)
        return K.matrix_from_rows(range(Bb.ncols(), Bb.ncols() + self.b[n]))


# ===========================================================================
# Restriction and inflation
# ===========================================================================


def restriction(C, Hsub, incl, Q, nmax):
    """res_(G,H) : H^n(G) -> H^n(H) (matrices b^Q_n x b^G_n, n <= nmax)
    through a chain map f : Q -> P from a resolution Q of F over the table
    group Hsub of H (incl: H-index -> G-index) to the minimal resolution P
    of G restricted to H; also returns the generator images f(e_i)."""
    F, G, P = C.F, C.G, C.P
    Y = {0: C.x0 * mat(F, 1, Q.b[0], {(0, 0): Q.eps[0, Hsub.e]})}
    R = {}
    for k in range(nmax + 1):
        if k > 0:
            if Q.b[k] == 0:
                Y[k] = mat(F, P.dim(k), 0)
            else:
                # f_(k-1) on Q_(k-1): column i |H| + h = incl(h) . Y[k-1]_i
                parts = [act_free(G, P.b[k - 1], incl[h], Y[k - 1])
                         for h in range(Hsub.n)]
                full = hcat(F, P.dim(k - 1), parts).matrix_from_columns(
                    [h * Q.b[k - 1] + i for i in range(Q.b[k - 1])
                     for h in range(Hsub.n)])
                Y[k] = P.d[k].solve_right(full * Q.gen_cols(k))
        R[k] = collapse(F, G, Y[k], P.b[k]).transpose()
    return R, Y


def inflation(C, Gq, proj, Cq, nmax=None):
    """inf : H^n(G/N) -> H^n(G) (matrices b^G_n x b^Q_n) through a chain
    map from P (over G) to the minimal resolution of F over G/N."""
    F, G, P, Q = C.F, C.G, C.P, Cq.P
    nmax = min(C.N, Cq.N) if nmax is None else nmax
    a = Q.eps[0, Gq.e]
    z0 = mat(F, Q.dim(0), 1, {(Gq.e, 0): 1 / a})
    Z = {0: z0 * mat(F, 1, P.b[0], {(0, i): P.eps[0, i * G.n + G.e]
                                     for i in range(P.b[0])})}
    Inf = {0: collapse(F, Gq, Z[0], Q.b[0]).transpose()}
    for k in range(1, nmax + 1):
        if P.b[k] == 0:
            Z[k] = mat(F, Q.dim(k), 0)
        else:
            parts = [act_free(Gq, Q.b[k - 1], proj[g], Z[k - 1])
                     for g in range(G.n)]
            full = hcat(F, Q.dim(k - 1), parts).matrix_from_columns(
                [g * P.b[k - 1] + i for i in range(P.b[k - 1])
                 for g in range(G.n)])
            Z[k] = Q.d[k].solve_right(full * P.gen_cols(k))
        Inf[k] = collapse(F, Gq, Z[k], Q.b[k])
    return {k: A.transpose() for k, A in Inf.items()}


class Koszul:
    """The tensor product of the periodic resolutions for an elementary
    abelian 2-subgroup E = <g_1, ..., g_r> of G (as an F[E]-resolution over
    the table group of E): basis e_a, |a| = n, d e_a = sum_i (g_i - 1)
    e_(a - eps_i).  Cochains <-> polynomials: the dual of e_a is t^a, and
    t_i is the homomorphism E -> F_2 dual to the basis g_i."""

    def __init__(self, F, Esub, basis, nmax):
        assert F.characteristic() == 2
        self.F, self.G, self.r = F, Esub, len(basis)
        self.basis = basis
        r = self.r
        self.mons = {k: [a for a in itertools.product(range(k + 1),
                                                     repeat=r)
                         if sum(a) == k] for k in range(nmax + 1)}
        self.ix = {k: {a: i for i, a in enumerate(self.mons[k])}
                   for k in self.mons}
        self.b = [len(self.mons[k]) for k in range(nmax + 1)]
        n = Esub.n
        self.eps = mat(F, 1, n, {(0, t): 1 for t in range(n)})
        self.d = {}
        for k in range(1, nmax + 1):
            ent = {}
            for c, a in enumerate(self.mons[k]):
                for i in range(r):
                    if a[i] == 0:
                        continue
                    a2 = tuple(a[j] - (1 if j == i else 0) for j in range(r))
                    j = self.ix[k - 1][a2]
                    for g in range(n):
                        # g (g_i - 1) e_a2
                        for h, s in ((Esub.mul[g][basis[i]], 1), (g, 1)):
                            key = (j * n + h, c * n + g)
                            ent[key] = ent.get(key, 0) + s
            self.d[k] = mat(F, self.b[k - 1] * n, self.b[k] * n,
                            {kk: v for kk, v in ent.items() if v % 2})
            if k >= 2:
                assert (self.d[k - 1] * self.d[k]).is_zero()

    def dim(self, k):
        return self.b[k] * self.G.n

    def gen_cols(self, k):
        n, e = self.G.n, self.G.e
        return self.d[k].matrix_from_columns([i * n + e
                                              for i in range(self.b[k])])


def restriction_poly(C, Esub, incl, basis, S, nmax):
    """res_(G,E) in polynomial coordinates: for each n a function sending a
    class of H^n(G) to a polynomial in S = F[t_1, ..., t_r] (t_i dual to the
    basis g_i of E, given as elements of the table group Esub)."""
    Q = Koszul(C.F, Esub, basis, nmax)
    R, _ = restriction(C, Esub, incl, Q, nmax)
    t = S.gens()

    def poly(n, v):
        w = R[n] * vector(C.F, v)
        return sum((w[i] * prod_(t[j] ** a[j] for j in range(len(t)))
                    for i, a in enumerate(Q.mons[n]) if w[i]), S(0))
    return poly


def prod_(xs):
    out = 1
    for x in xs:
        out = out * x
    return out


def unit(F, n, i):
    return vector(F, [1 if j == i else 0 for j in range(n)])


def span_cols(F, vecs, n):
    if not vecs:
        return mat(F, n, 0)
    return mrows(F, vecs).transpose()


# ===========================================================================
# Groups used here, cohomology rings and their presentations
# ===========================================================================

GROUP_SPECS = {
    'C2': (2, 1), 'C4': (4, 1), 'V4': (4, 2), 'C8': (8, 1), 'C4xC2': (8, 2),
    'D8': (8, 3), 'Q8': (8, 4), 'C2^3': (8, 5), 'C3': (3, 1), 'C9': (9, 1),
    'C3xC3': (9, 2), '3^(1+2)_+': (27, 3), '3^(1+2)_-': (27, 4),
    'C4xC2xC2': (16, 10), 'D8xC2': (16, 11), 'Q8xC2': (16, 12),
    'C4oD8': (16, 13), 'C2^4': (16, 14),
    '2^(1+4)_+': (32, 49), '2^(1+4)_-': (32, 50),
}
_GRP, _COH = {}, {}


def group(name):
    if name not in _GRP:
        o, i = GROUP_SPECS[name] if name in GROUP_SPECS else \
            tuple(int(x) for x in name.split('_'))
        _GRP[name] = Grp.from_gap(libgap.SmallGroup(o, i), name)
    return _GRP[name]


def cohom(name, p, N):
    key = (name, p)
    if key not in _COH or _COH[key].N < N:
        _COH[key] = Cohom(group(name), GF(p), N)
    return _COH[key]


class Presentation:
    """H^*(G, F_2) in degrees <= N as a quotient of a weighted polynomial
    ring on given generator classes: monomial images by Yoneda products,
    relations = kernels, surjectivity degree by degree."""

    def __init__(self, C, gens, names, upto=None):
        assert C.p == 2
        self.C, self.gens = C, gens
        F, N = C.F, (C.N if upto is None else upto)
        self.N = N
        self.degs = [d for d, _ in gens]
        self.R = PolynomialRing(F, names,
                                order=TermOrder('wdegrevlex', self.degs))
        self.vec = {(0,) * len(gens): vector(F, [1])}
        self.mons = {0: [(0,) * len(gens)]}
        for d in range(1, N + 1):
            self.mons[d] = []
            for a in self._exps(d):
                i = max(j for j in range(len(gens)) if a[j])
                a2 = tuple(a[j] - (1 if j == i else 0)
                           for j in range(len(gens)))
                di, v = gens[i]
                self.vec[a] = C.mul(self.vec[a2], d - di, v, di)
                self.mons[d].append(a)
        self.rels, self.surj = [], True
        for d in range(1, N + 1):
            A = self.matrix(d)
            self.surj &= rk(A) == C.b[d]
            for kv in kernel_cols(A).columns():
                self.rels.append(self.poly(d, kv))

    def _exps(self, d):
        out = []

        def rec(i, rem, cur):
            if i == len(self.degs):
                if rem == 0:
                    out.append(tuple(cur))
                return
            for e in range(rem // self.degs[i] + 1):
                rec(i + 1, rem - e * self.degs[i], cur + [e])
        rec(0, d, [])
        return out

    def matrix(self, d):
        cols = [self.vec[a] for a in self.mons[d]]
        if not cols:
            return mat(self.C.F, self.C.b[d], 0)
        return mrows(self.C.F, cols).transpose()

    def mono(self, a):
        return prod_(g ** e for g, e in zip(self.R.gens(), a))

    def poly(self, d, coeffs):
        return sum((c * self.mono(a) for c, a in zip(coeffs, self.mons[d])
                    if c), self.R(0))

    def coords(self, d, v):
        """A polynomial representing the class v of degree d."""
        A = self.matrix(d)
        return self.poly(d, A.solve_right(vector(self.C.F, v)))

    def ideal(self):
        return self.R.ideal(self.rels) if self.rels else self.R.ideal(0)

    def evaluate(self, f, d):
        """The class of a weighted-homogeneous polynomial of degree d."""
        out = vector(self.C.F, [0] * self.C.b[d])
        for c, m in zip(f.coefficients(), f.monomials()):
            out += c * self.vec[tuple(m.exponents()[0])]
        return out


MTX_ISO = libgap.eval('MTX.IsomorphismModules')
MTX_INDEC = libgap.eval('MTX.IsIndecomposable')
MTX_DECOMP = libgap.eval('MTX.Indecomposition')


def gap_module(M):
    """The module M (left, on columns) as a GAP MeatAxe module on rows."""
    mats = [M.act[g].transpose().dense_matrix() for g in M.G.gens]
    return libgap.GModuleByMats([libgap(A) for A in mats], libgap(M.F))


def isomorphic(M, N):
    if M.dim != N.dim:
        return False
    return MTX_ISO(gap_module(M), gap_module(N)) != libgap.eval('fail')


def omega_mod(M, k=1):
    """Omega^k(M) (kernel of the projective cover, iterated)."""
    P = Resolution(M, k)
    return P.omega(k) if k >= 1 else M


def omega_inv(M, k=1):
    return dual(omega_mod(dual(M), k))


def h1_class_killing(C, Hset):
    """A non-zero class of H^1(G) whose homomorphism vanishes on the
    maximal subgroup H."""
    F, b1 = C.F, C.b[1]
    rows = [C.hom_of(unit(F, b1, j)) for j in range(b1)]
    A = mrows(F, [[rows[j][h] for j in range(b1)] for h in Hset])
    K = kernel_cols(A)
    assert K.ncols() == 1
    return K.column(0)


def bockstein_of_index_p(C, Hset):
    """For a maximal subgroup H: the class x in H^1(G) with kernel H and
    (up to a non-zero scalar) beta(x): x o x for p = 2, the inflation from
    G/H = Z/p of the generator of H^2(Z/p) for p odd."""
    x = h1_class_killing(C, Hset)
    if C.p == 2:
        return x, C.mul(x, 1, x, 1)
    G = C.G
    Gq, proj = G.quotient(Hset, 'G/H')
    Cq = Cohom(Gq, C.F, 2)
    Inf = inflation(C, Gq, proj, Cq, 2)
    assert Cq.b[2] == 1
    return x, Inf[2] * vector(C.F, [1])


# ===========================================================================
# Section 5.1 (pp. 153-154)
# ===========================================================================


def section_5_1():
    """Graded commutativity, H^dot(G, k), complexity zero and one."""
    cases = [('C3', 3, 6), ('C9', 3, 6), ('C3xC3', 3, 5),
             ('3^(1+2)_+', 3, 5), ('3^(1+2)_-', 3, 5), ('C4', 2, 6),
             ('C4xC2', 2, 6), ('D8', 2, 6), ('Q8', 2, 6), ('16_3', 2, 5),
             ('16_6', 2, 5), ('Q8xC2', 2, 5)]
    for name, p, N in cases:
        C = cohom(name, p, N)
        F = C.F
        comm_ok, sq_ok = True, True
        for l in range(1, N):
            for m in range(1, N - l + 1):
                for i in range(C.b[l]):
                    for j in range(C.b[m]):
                        a, b = unit(F, C.b[l], i), unit(F, C.b[m], j)
                        ab = C.mul(a, l, b, m)
                        ba = C.mul(b, m, a, l)
                        comm_ok &= ab == (-1) ** (l * m) * ba
            if l % 2 == 1 and 2 * l <= N and p != 2:
                for i in range(C.b[l]):
                    a = unit(F, C.b[l], i)
                    sq_ok &= C.mul(a, l, a, l).is_zero()
        check(comm_ok, 'p. 153: H^*(G, F_p) is graded commutative, x y = '
              '(-1)^(deg x deg y) y x (%s, p = %d, degrees <= %d)'
              % (name, p, N))
        if p != 2:
            check(sq_ok, 'p. 153 (ii): for p odd elements of odd degree '
                  'square to zero, so H^ev is commutative (%s, degrees <= %d)'
                  % (name, N))
    # complexity zero <=> the minimal resolution stops <=> projective
    for name, p in (('D8', 2), ('Q8', 2), ('C3xC3', 3)):
        G = group(name)
        F = GF(p)
        P = Resolution(regular_module(F, G), 4)
        check(P.b == [1, 0, 0, 0, 0], 'p. 154: a projective module has '
              'complexity zero (F[%s]: b = %s)' % (name, P.b))
        Pk = Resolution(trivial(F, G), 8)
        check(all(b > 0 for b in Pk.b), 'p. 154: a non-projective module '
              'has a minimal resolution that never stops (F for %s, b = %s)'
              % (name, Pk.b))
    # complexity one: bounded dimensions and periodicity (Q8, C4, C9)
    for name, p, period in (('C4', 2, 2), ('Q8', 2, 4), ('C9', 3, 2),
                            ('C3', 3, 2)):
        G = group(name)
        F = GF(p)
        k = trivial(F, G)
        P = Resolution(k, 12)
        check(max(P.b) <= 2 and P.b[:period] == P.b[period:2 * period],
              'p. 154: complexity one: the minimal resolution of F over %s '
              'has bounded ranks %s' % (name, P.b))
        check(isomorphic(P.omega(period), k) and
              all(not isomorphic(P.omega(j), k) for j in range(1, period)),
              'p. 154: the minimal resolution of F over %s repeats with '
              'period %d (Omega^%d F = F)' % (name, period, period))
    for name, p in (('D8', 2), ('V4', 2), ('C3xC3', 3)):
        P = Resolution(trivial(GF(p), group(name)), 12)
        check(P.b[12] > P.b[6] > P.b[1], 'p. 154: F over %s has '
              'unbounded ranks %s (complexity > 1)' % (name, P.b))


# ===========================================================================
# Section 5.2 (pp. 155-157)
# ===========================================================================

QV_CASES = [('C4', 2, 8), ('V4', 2, 8), ('C8', 2, 8), ('C4xC2', 2, 8),
            ('D8', 2, 8), ('Q8', 2, 8), ('C2^3', 2, 7), ('16_1', 2, 7),
            ('16_2', 2, 7), ('16_3', 2, 7), ('16_4', 2, 7), ('16_5', 2, 7),
            ('16_6', 2, 7), ('16_7', 2, 7), ('16_8', 2, 7), ('16_9', 2, 7),
            ('C4xC2xC2', 2, 6), ('D8xC2', 2, 6), ('Q8xC2', 2, 6),
            ('C4oD8', 2, 6), ('C9', 3, 8), ('C3xC3', 3, 6),
            ('3^(1+2)_+', 3, 6), ('3^(1+2)_-', 3, 6), ('27_2', 3, 6)]


def maximal_subgroups(G, p):
    """The subgroups of index p (kernels of the homomorphisms G -> Z/p)."""
    out = set()
    for chi in homs_to_Fp(G, p):
        out.add(tuple(g for g in range(G.n) if chi[g] == 0))
    return [list(S) for S in sorted(out)]


def prod_pow(G, a, k):
    x = G.e
    for _ in range(k):
        x = G.mul[x][a]
    return x


def homs_to_Fp(G, p):
    """All homomorphisms G -> Z/p (as value lists), by the Frattini
    quotient."""
    Phi = G.closure([G.comm(a, b) for a in range(G.n) for b in range(G.n)] +
                    [prod_pow(G, a, p) for a in range(G.n)])
    Q, proj = G.quotient(Phi, 'G/Phi')
    # a basis of Q as a vector space: greedy
    basis, span = [], {Q.e}
    for a in range(Q.n):
        if a not in span:
            basis.append(a)
            span = set(Q.closure(basis))
    r = len(basis)
    coord = {}
    for v in itertools.product(range(p), repeat=r):
        x = Q.e
        for bi, c in zip(basis, v):
            x = Q.mul[x][prod_pow(Q, bi, c)]
        coord[x] = v
    out = []
    for w in itertools.product(range(p), repeat=r):
        if any(w):
            out.append([sum(a * c for a, c in zip(w, coord[proj[g]])) % p
                        for g in range(G.n)])
    return out


def section_5_2():
    """Theorem 5.2.1 (Quillen-Venkov), Serre's theorem in the form used in
    Theorem 5.2.2, Theorem 5.2.2 for M = k, Lemma 5.2.3, Theorem 5.2.4."""
    for name, p, N in QV_CASES:
        C = cohom(name, p, N)
        G, F = C.G, C.F
        Hs = maximal_subgroups(G, p)
        for Hset in Hs:
            Hsub, incl = G.subgroup(Hset, 'H')
            QH = Resolution(trivial(F, Hsub), N)
            R, _ = restriction(C, Hsub, incl, QH, N)
            x, bx = bockstein_of_index_p(C, Hset)
            ker = {n: kernel_cols(R[n]) for n in range(1, N + 1)}
            ok = True
            for l in range(1, N):
                for m in range(1, N - l + 1):
                    if not ker[l].ncols() or not ker[m].ncols():
                        continue
                    # beta(x) . H^(l+m-2)
                    d = l + m - 2
                    img = hcat(F, C.b[l + m], [
                        span_cols(F, [C.mul(unit(F, C.b[d], i), d, bx, 2)
                                      for i in range(C.b[d])], C.b[l + m])])
                    prods = [C.mul(z1, l, z2, m)
                             for z1 in ker[l].columns()
                             for z2 in ker[m].columns()]
                    ok &= in_span(img, span_cols(F, prods, C.b[l + m]))
            check(ok, 'Theorem 5.2.1 (Quillen-Venkov), as the proof gives '
                  'it: products zeta zeta\' of elements of positive degree '
                  'with res_(G,H) = 0 lie in beta(x) . H^*(G) (%s, H of index '
                  '%d, |H| = %d, beta(x) %s 0, degrees <= %d)'
                  % (name, p, len(Hset), '=' if bx.is_zero() else '!=', N))
    # Serre's theorem as used in the proof of Theorem 5.2.2
    for name, p, N in QV_CASES:
        N = 8 if name == '3^(1+2)_+' else N
        C = cohom(name, p, N)
        G, F = C.G, C.F
        elab = p ** C.b[1] == G.n
        lines = homs_lines(C)
        bocks = [bockstein_of_line(C, x) for x in lines]
        found = None
        for s in range(1, N // 2 + 1):
            for sub in itertools.combinations_with_replacement(
                    range(len(lines)), s):
                v, deg = vector(F, [1]), 0
                for i in sub:
                    v = C.mul(v, deg, bocks[i], 2)
                    deg += 2
                if v.is_zero():
                    found = sub
                    break
            if found:
                break
        if elab:
            check(found is None, 'Theorem 4.7.3 (Serre), converse: for '
                  'elementary abelian %s no product of Bocksteins of non-zero '
                  'degree one elements vanishes (degrees <= %d)' % (name, N))
        else:
            check(found is not None, 'Serre\'s theorem (used in the proof '
                  'of Theorem 5.2.2): %s is not elementary abelian, and '
                  'beta(x_1) ... beta(x_n) = 0 for %d non-zero x_i in '
                  'H^1(G, F_%d)' % (name, len(found), p))
    # Theorem 5.2.2 for M = k: the kernel of restriction to all elementary
    # abelian subgroups is nilpotent
    for name, p, N in (('C4', 2, 12), ('C8', 2, 12), ('Q8', 2, 12),
                       ('D8', 2, 12), ('C4xC2', 2, 12), ('16_4', 2, 10),
                       ('Q8xC2', 2, 10), ('C9', 3, 10),
                       ('3^(1+2)_-', 3, 8)):
        C = cohom(name, p, N)
        G, F = C.G, C.F
        subs = G.conj_classes_of(G.elementary_abelian_subgroups(p))
        maxs = [E for E in subs if not any(set(E) < set(E2) for E2 in subs)]
        Rs = []
        for Eset in maxs:
            Esub, incl = G.subgroup(Eset, 'E')
            QE = Resolution(trivial(F, Esub), N)
            Rs.append(restriction(C, Esub, incl, QE, N)[0])
        nil_ok, nontriv = True, 0
        for d in range(1, (N // 4 if p == 2 else N // 2) + 1):
            A = vcat(F, C.b[d], [R[d] for R in Rs])
            K = kernel_cols(A)
            for z in K.columns():
                nontriv += 1
                e, ok = 2, False
                while e * d <= N:
                    if C.power(z, d, e).is_zero():
                        ok = True
                        break
                    e += 1
                nil_ok &= ok
        check(nil_ok, 'Theorem 5.2.2 (M = k): the %d basis elements of '
              'degree <= %d of the kernel of the restrictions of H^*(%s, '
              'F_%d) to the %d maximal elementary abelian subgroups (up to '
              'conjugacy) are nilpotent (a power of degree <= %d vanishes)'
              % (nontriv, N // 4 if p == 2 else N // 2, name, p, len(maxs),
                 N))
    # Lemma 5.2.3 and Chouinard's theorem 5.2.4 on modules
    for name in ('D8', 'Q8', 'C4xC2', 'C4', 'Q8xC2'):
        G = group(name)
        F = GF(2)
        C = cohom(name, 2, 5)
        subs = G.conj_classes_of(G.elementary_abelian_subgroups(2))
        maxs = [E for E in subs if not any(set(E) < set(E2) for E2 in subs)]
        Esubs = [G.subgroup(E, 'E') for E in maxs]
        mods = test_modules(G, F)
        lemma_ok, chou_ok, nfree, nlem = True, True, 0, 0
        for M in mods:
            free = is_free(M)
            nfree += free
            free_res = all(is_free(restrict(M, Es, inc)) for Es, inc in
                           Esubs)
            chou_ok &= free == free_res
            if M.dim > 12:
                continue
            nlem += 1
            E = end_module(M)
            exts = []
            for n in range(1, 4):
                dl = C.cochain_delta(E, n - 1)
                dn = C.cochain_delta(E, n)
                exts.append(dn.ncols() - rk(dn) - rk(dl))
            Pm = Resolution(M, 6)
            lemma_ok &= (free == all(x == 0 for x in exts)) and \
                (free or all(b > 0 for b in Pm.b))
        check(chou_ok, 'Theorem 5.2.4 (Chouinard): M projective iff M|E '
              'projective for the maximal elementary abelian E (%d modules '
              'for %s, %d projective)' % (len(mods), name, nfree))
        check(lemma_ok, 'Lemma 5.2.3: M projective iff Ext^n(M, M) = 0 for '
              'n = 1, 2, 3; otherwise P_F occurs in every P_n, n <= 6 (%d '
              'modules of dimension <= 12 for %s)' % (nlem, name))


def homs_lines(C):
    """Representatives of the non-zero classes of H^1 up to scalars."""
    F, b1 = C.F, C.b[1]
    out = []
    for v in itertools.product(list(F), repeat=b1):
        if not any(v):
            continue
        first = next(c for c in v if c)
        if first == 1:
            out.append(vector(F, v))
    return out


def bockstein_of_line(C, x):
    """beta(x) up to a scalar."""
    G = C.G
    chi = C.hom_of(x)
    Hset = [g for g in range(G.n) if chi[g] == 0]
    x2, bx = bockstein_of_index_p(C, Hset)
    return bx


def test_modules(G, F):
    """Small F[G]-modules: permutation modules on all subgroups (up to
    conjugacy), Omega^(+-1) of F, a few sums and tensor products, the
    regular module and random quotients of F[G]^2."""
    subs = G.conj_classes_of(all_subgroups(G))
    mods = [perm_module(F, G, H) for H in subs]
    k = trivial(F, G)
    mods += [omega_mod(k, 1), omega_mod(k, 2), omega_inv(k, 1),
             direct_sum(k, regular_module(F, G))]
    small = [M for M in mods if 1 < M.dim <= 4]
    if len(small) >= 2:
        mods.append(tensor(small[0], small[-1]))
    rnd = random.Random(G.n * 7 + 1)
    reg = regular_module(F, G)
    two = direct_sum(reg, reg)
    for _ in range(6):
        vs = [vector(F, [F.random_element() if rnd.random() < 0.5 else 0
                         for _ in range(two.dim)]) for _ in range(2)]
        S = submodule_generated(two, vs)
        if 0 < S.ncols() < two.dim:
            mods.append(quotient_action(two, S))
    return mods


def submodule_generated(M, vs):
    F = M.F
    B = colbasis(span_cols(F, [M.act[g] * v for v in vs for g in
                               range(M.G.n)], M.dim))
    return B


def all_subgroups(G):
    found = set()
    for a in range(G.n):
        for b in range(a, G.n):
            found.add(tuple(G.closure([a, b])))
    # 3-generated subgroups for rank 3 groups
    for S in list(found):
        for c in range(G.n):
            found.add(tuple(G.closure(list(S) + [c])))
    return [list(S) for S in sorted(found, key=len)]


def auto_presentation(C, maxdeg):
    """Generators of H^*(G, F_2) chosen greedily in degrees <= maxdeg (a
    complement of the decomposables in each degree) and the presentation
    with relations of degree <= C.N."""
    F = C.F
    gens = []
    for d in range(1, maxdeg + 1):
        if gens:
            P = Presentation(C, gens, ['g%d' % i for i in range(len(gens))],
                             upto=d)
            A = P.matrix(d)
        else:
            A = mat(F, C.b[d], 0)
        B = colbasis(A)
        allc = B.augment(ident(F, C.b[d])) if B.ncols() else ident(F, C.b[d])
        for c in allc.pivots():
            if c >= B.ncols():
                gens.append((d, unit(F, C.b[d], c - B.ncols())))
    return Presentation(C, gens, ['g%d' % i for i in range(len(gens))])


def local_radical_square_zero_ranks(F, r, nmax):
    """Ranks of the minimal resolution of k over Lambda = k E / J^2(k E)
    (E of rank r): Lambda has basis 1, X_1, ..., X_r with X_i X_j = 0."""
    dA = r + 1
    L = [ident(F, dA)] + [mat(F, dA, dA, {(i + 1, 0): 1}) for i in range(r)]

    def act(b, a, X):         # left multiplication by basis element a
        return block_diag(F, [L[a]] * b) * X if b else X

    def free(b_src, X):
        b = X.nrows() // dA
        cols = [act(b, a, X) for a in range(dA)]
        Y = hcat(F, X.nrows(), cols)
        return Y.matrix_from_columns([a * b_src + i for i in range(b_src)
                                      for a in range(dA)])
    eps = mat(F, 1, dA, {(0, 0): 1})
    ranks, prev, b = [1], eps, 1
    for n in range(1, nmax + 1):
        K = kernel_cols(prev)
        JK = hcat(F, K.nrows(), [act(b, a, K) for a in range(1, dA)])
        gens = min_generators(K, JK)
        X = K.matrix_from_columns(gens)
        prev = free(len(gens), X)
        assert rk(prev) == K.ncols()
        b = len(gens)
        ranks.append(b)
    return ranks


def block_diag(F, mats):
    n = sum(A.nrows() for A in mats)
    m = sum(A.ncols() for A in mats)
    ent, r0, c0 = {}, 0, 0
    for A in mats:
        for (i, j), x in A.dict().items():
            ent[(r0 + i, c0 + j)] = x
        r0 += A.nrows()
        c0 += A.ncols()
    return mat(F, n, m, ent)


def series_coeffs(f, n):
    """The first n coefficients of a rational function in t."""
    R = PowerSeriesRing(QQ, 't', default_prec=n + 5)
    num, den = R(f.numerator()), R(f.denominator())
    s = num / den
    return [s[i] for i in range(n)]


def pole_order_at_1(f):
    """The order of the pole of a rational function f(t) at t = 1."""
    num, den = f.numerator(), f.denominator()
    t = num.parent().gen()
    o = 0
    while den(1) == 0:
        den = den // (t - 1) if den % (t - 1) == 0 else den
        o += 1
        if num(1) == 0:
            num = num // (t - 1)
            o -= 1
    while num(1) == 0:
        num = num // (t - 1)
        o -= 1
    return o


def graded_examples():
    """Graded rings A = S/I (weights, generators, relations) used in
    Sections 5.3 and 5.4."""
    out = []
    F2, F3 = GF(2), GF(3)
    R = PolynomialRing(F2, 'x,y,w', order=TermOrder('wdegrevlex', (1, 1, 2)))
    x, y, w = R.gens()
    out.append(('H^*(D8) = F2[x,y,w]/(xy)', R, (1, 1, 2), [x * y]))
    R = PolynomialRing(F2, 'x,y,z', order=TermOrder('wdegrevlex', (1, 1, 4)))
    x, y, z = R.gens()
    out.append(('H^*(Q8)', R, (1, 1, 4),
                [x ** 2 + x * y + y ** 2, x ** 2 * y + x * y ** 2]))
    R = PolynomialRing(F2, 'x,y', order=TermOrder('wdegrevlex', (1, 1)))
    x, y = R.gens()
    out.append(('F2[x,y]/(x^2, xy)', R, (1, 1), [x ** 2, x * y]))
    out.append(('F2[x,y]/(x^2 y)', R, (1, 1), [x ** 2 * y]))
    R = PolynomialRing(F3, 'a,b,c', order=TermOrder('wdegrevlex', (2, 3, 4)))
    a, b, c = R.gens()
    out.append(('F3[a,b,c]/(a^3 - c a, b^2 c)', R, (2, 3, 4),
                [a ** 3 - c * a, b ** 2 * c]))
    R = PolynomialRing(F2, 'x1,x2,x3,x4,z',
                       order=TermOrder('wdegrevlex', (1, 1, 1, 1, 8)))
    x1, x2, x3, x4, z = R.gens()
    q = x1 * x2 + x3 ** 2 + x3 * x4 + x4 ** 2
    b1 = x1 * x2 ** 2 + x1 ** 2 * x2 + x3 * x4 ** 2 + x3 ** 2 * x4
    b2 = x1 * x2 ** 4 + x1 ** 4 * x2 + x3 * x4 ** 4 + x3 ** 4 * x4
    out.append(('H^*(2^(1+4)_-) form', R, (1, 1, 1, 1, 8), [q, b1, b2]))
    R = PolynomialRing(F2, 'd2,d3', order=TermOrder('wdegrevlex', (2, 3)))
    out.append(('Dickson F2[d2, d3]', R, (2, 3), []))
    return out


def section_5_3():
    """Poincare series, Propositions 5.3.1, 5.3.2, growth, the formula for
    dim P_r, Proposition 5.3.5 (inequalities), Lemma 5.3.6, Theorem 5.3.8,
    the Exercise."""
    Rt = PolynomialRing(QQ, 't')
    t = Rt.gen()
    # p. 157: Poincare series of polynomial rings in degree one generators
    for n in range(1, 6):
        S = PolynomialRing(GF(2), n, 'x')
        hs = S.ideal(0).hilbert_series()
        c = series_coeffs(hs, 4)
        check(hs == 1 / (1 - hs.parent().gen()) ** n and
              c[1] == n and c[2] == n * (n + 1) // 2,
              'p. 157: p(k[x_1, ..., x_%d], t) = 1 + n t + n(n + 1) t^2 / 2 '
              '+ ... = 1 / (1 - t)^n' % n)
    # the Exercise p. 161 (and the free ring on p. 157): Ext over k E / J^2
    for p, r, nmax in ((2, 1, 6), (2, 2, 6), (2, 3, 5), (3, 2, 5),
                       (5, 2, 4)):
        ranks = local_radical_square_zero_ranks(GF(p), r, nmax)
        check(ranks == [r ** n for n in range(nmax + 1)],
              'Exercise p. 161: H^*(k E / J^2, k) = k{x_1, ..., x_r} has '
              'Poincare series 1 / (1 - r t) (r = %d, p = %d, degrees <= %d; '
              'r = 2 is the free ring of p. 157, 1 + 2t + 4t^2 + ...)'
              % (r, p, nmax))
    # Proposition 5.3.1 (Hilbert-Serre) and its proof; Proposition 5.3.2
    for lab, R, wts, rels in graded_examples():
        I = R.ideal(rels) if rels else R.ideal(0)
        hs = I.hilbert_series(grading=wts)
        T = hs.parent().gen()
        den = prod_(1 - T ** k for k in wts)
        f = hs * den
        check(f.denominator() == 1 and
              all(c in ZZ for c in f.numerator().coefficients()),
              'Proposition 5.3.1: p(A, t) = f(t) / prod (1 - t^(k_j)) with '
              'f in ZZ[t] (%s, degrees %s)' % (lab, wts))
        # the proof: K = Ker(x_s), L = Coker(x_s) on V = A
        xs, ks = R.gens()[-1], wts[-1]
        K_hs = hs - (I.quotient(R.ideal(xs)) if rels else R.ideal(0)
                     ).hilbert_series(grading=wts)
        L_hs = (I + R.ideal(xs)).hilbert_series(grading=wts)
        g = -(T ** ks * K_hs - T ** ks * hs + hs - L_hs)
        ok = g.denominator() == 1 and (g.numerator() == 0 or
                                       g.numerator().degree() < ks)
        ok &= hs == (L_hs - T ** ks * K_hs - g) / (1 - T ** ks)
        check(ok, 'proof of Proposition 5.3.1: t^k p(K) - t^k p(V) + p(V) '
              '- p(L) + g(t) = 0 with g a polynomial of degree < k = deg '
              'x_s (here g = %s; %s)' % (g, lab))
        # Proposition 5.3.2: reduce to k_j = 1, then the binomial formula
        red = hs * prod_(sum(T ** i for i in range(k)) for k in wts)
        gam = pole_order_at_1(hs)
        num = red * (1 - T) ** gam
        check(num.denominator() == 1 and num.numerator()(1) != 0 and
              pole_order_at_1(red) == gam,
              'proof of Proposition 5.3.2: p(t) (1 + t + ... + t^(k_j - 1)) '
              '= f(t) / (1 - t)^gamma with f(1) != 0, the same pole order '
              'gamma = %d (%s)' % (gam, lab))
        fpoly = num.numerator()
        alph = [fpoly[j] for j in range(fpoly.degree() + 1)]
        m = len(alph) - 1
        a_red = series_coeffs(red, m + 40)
        Pn = PolynomialRing(QQ, 'n')
        nn = Pn.gen()
        if gam >= 1:
            poly = Pn(sum(alph[j] * binomial_poly(nn + gam - j - 1, gam - 1)
                          for j in range(m + 1)))
            ok = all(a_red[n] == sum(alph[j] * (binomial(n + gam - j - 1,
                                                         gam - 1)
                                               if n - j >= 0 else 0)
                                     for j in range(m + 1))
                     for n in range(m + 40))
            ok &= all(a_red[n] == poly(n) for n in range(m, m + 40))
            ok &= poly.degree() == gam - 1 and \
                poly.leading_coefficient() == fpoly(1) / factorial(gam - 1)
            check(ok, 'proof of Proposition 5.3.2: a_n = sum_j alpha_j '
                  'binom(n + gamma - j - 1, gamma - 1), a polynomial of '
                  'degree exactly gamma - 1 = %d for n >= m (%s)'
                  % (gam - 1, lab))
        a = series_coeffs(hs, 401)
        if gam >= 1:
            ratio1 = [a[n] / n ** (gam - 1) for n in range(1, 401)]
            ok = max(ratio1) <= max(ratio1[:100]) * 2
            if gam >= 2:
                r2 = [a[n] / n ** (gam - 2) for n in (50, 400)]
                ok &= r2[1] > 4 * r2[0]
            check(ok, 'Proposition 5.3.2 (i), (ii): a_n / n^(gamma - 1) is '
                  'bounded and a_n / n^(gamma - 2) grows (n <= 400, gamma = '
                  '%d, %s)' % (gam, lab))
        # Theorem 5.4.6 (ii) on the same rings: Krull dimension = gamma
        check(I.dimension() == gam, 'Theorem 5.4.6 (ii): dim A = gamma(A) '
              '= %d (%s)' % (gam, lab))
        # growth is additive on short exact sequences 0 -> J -> A -> A/J
        J = I + R.ideal(R.gens()[0])
        pJ = pole_order_at_1(hs - J.hilbert_series(grading=wts)) \
            if hs != J.hilbert_series(grading=wts) else 0
        pq = pole_order_at_1(J.hilbert_series(grading=wts))
        check(gam == max(pJ, pq) and pJ <= gam,
              'p. 159: gamma(V\') = max(gamma(V), gamma(V\'\')) for 0 -> '
              '(x_1) -> A -> A/(x_1) -> 0, and gamma(V) <= gamma(A) (%s)'
              % lab)
        # Lemma 5.3.6: the nilradical J, J^n = 0 with n = sum n_i, and
        # gamma(A) = gamma(A / J)
        if R.ngens() > 3:
            continue
        rad = I.radical()
        gens = [f for f in rad.gens() if f not in I]
        orders = []
        for f in gens:
            e = 1
            while f ** e not in I:
                e += 1
            orders.append(e)
        nsum = sum(orders)
        index, Jp = 1, rad
        while not all(f in I for f in Jp.gens()):
            Jp = (Jp * rad) + I
            index += 1
        ok = index <= max(nsum, 1)
        ok &= pole_order_at_1(rad.hilbert_series(grading=wts)) == gam
        check(ok, 'Lemma 5.3.6: the nilpotent elements form an ideal J '
              'generated by %d elements of nilpotency orders %s, J^%d = 0 '
              '(n = sum n_i = %d), and gamma(A / J) = gamma(A) = %d (%s)'
              % (len(gens), orders, index, nsum, gam, lab))
    # the formula for dim P_r (p. 159): for p-groups dim P_r = |G| dim
    # Ext^r(M, k), Ext^r(M, k) = H^r(G, M^*) computed from the resolution of
    # k; and dim Ext^r(M, N) <= dim P_r dim N (p. 159)
    for name, p in (('D8', 2), ('Q8', 2), ('C4xC2', 2), ('C3xC3', 3)):
        G = group(name)
        F = GF(p)
        C = cohom(name, p, 7)
        mods = test_modules(G, F)[:10]
        ok_eq, ok_ineq = True, True
        for M in mods:
            if M.dim > 9:
                continue
            P = Resolution(M, 6)
            Md = dual(M)
            for r in range(0, 6):
                dl = C.cochain_delta(Md, r - 1) if r else None
                dn = C.cochain_delta(Md, r)
                h = dn.ncols() - rk(dn) - (rk(dl) if r else 0)
                ok_eq &= h == P.b[r]
            for N in mods[:4]:
                H = tensor(N, Md)              # Hom_k(M, N)
                for r in range(0, 5):
                    dl = C.cochain_delta(H, r - 1) if r else None
                    dn = C.cochain_delta(H, r)
                    h = dn.ncols() - rk(dn) - (rk(dl) if r else 0)
                    ok_ineq &= h <= P.dim(r) * N.dim
        check(ok_eq, 'p. 159: Hom_kG(P_r, k) = Ext^r(M, k) and dim P_r = '
              '|G| dim Ext^r(M, k) for the minimal resolution (modules for '
              '%s, r <= 5; Ext from the resolution of k)' % name)
        check(ok_ineq, 'p. 159: dim Ext^r(M, N) <= dim P_r . dim N '
              '(modules for %s, r <= 4)' % name)
    # Theorem 5.3.8 (Quillen): Krull dimension of H^*(G, F_2) = r_2(G)
    for name in ('C4', 'C8', 'C4xC2', 'D8', 'Q8', 'C2^3', '16_1', '16_2',
                 '16_3', '16_4', '16_5', '16_6', '16_7', '16_8', '16_9',
                 'C4xC2xC2', 'D8xC2', 'Q8xC2', 'C4oD8'):
        C = cohom(name, 2, 10)
        G = C.G
        Pres = auto_presentation(C, 5)
        I = Pres.ideal()
        hs = I.hilbert_series(grading=Pres.degs)
        coeffs = series_coeffs(hs, 11)
        r2 = max(rank_of(len(E), 2) for E in
                 G.elementary_abelian_subgroups(2))
        check(Pres.surj and coeffs == C.b[:11] and I.dimension() == r2,
              'Theorem 5.3.8 (Quillen): H^*(%s, F_2), presented by %d '
              'generators of degree <= 5 and relations of degree <= 10 '
              '(Hilbert series = dims of the minimal resolution through '
              'degree 10), has Krull dimension r_2(G) = %d'
              % (name, len(Pres.gens), r2))
    # the proof of Theorem 5.3.8: p(H^*(E, k), t) = 1 / (1 - t)^n
    for p, n, N in ((2, 1, 10), (2, 2, 10), (2, 3, 8), (2, 4, 6), (3, 1, 8),
                    (3, 2, 7), (3, 3, 4), (5, 2, 4)):
        G = Grp.from_gap(libgap.ElementaryAbelianGroup(p ** n), 'E')
        P = Resolution(trivial(GF(p), G), N)
        check(P.b == [binomial(m + n - 1, n - 1) for m in range(N + 1)],
              'proof of Theorem 5.3.8: p(H^*(E, k), t) = 1 / (1 - t)^n, so '
              'c_E(k) = n (E = (Z/%d)^%d, degrees <= %d)' % (p, n, N))
    # p odd: H^*(C9) and H^*(C3 x C3) dims bounded resp. linear
    P = Resolution(trivial(GF(3), group('C9')), 12)
    check(P.b == [1] * 13, 'Theorem 5.3.8: H^*(Z/9, F_3) has dimension one '
          'in each degree: Krull dimension 1 = r_3(Z/9)')


def hs_free_over(I, wts, params, pdegs):
    """A = S/I free over k[params] (homogeneous, params an hsop): the
    Hilbert series criterion p(A) = p(A/(params)) / prod (1 - t^(d_i)),
    with A/(params) finite dimensional."""
    R = I.ring()
    J = I + R.ideal(params)
    if J.dimension() != 0:
        return None
    hA = I.hilbert_series(grading=wts)
    hJ = J.hilbert_series(grading=wts)
    T = hA.parent().gen()
    return hA == hJ / prod_(1 - T ** d for d in pdegs)


def is_regular_sequence(I, seq):
    """zeta_1, ..., zeta_r regular on S/I: (I + (zeta_<i)) : zeta_i = I +
    (zeta_<i) for each i (Definition 5.4.9 with M = A)."""
    R = I.ring()
    cur = I
    for z in seq:
        if cur.quotient(R.ideal(z)) != cur:
            return False
        cur = cur + R.ideal(z)
    return True


def random_homogeneous(R, d, rnd, wts=None):
    wts = wts or [1] * R.ngens()
    mons = [m for m in monomials_of_degree(R, d, wts)]
    F = R.base_ring()
    if not mons:
        return None
    while True:
        f = sum(F(rnd.randrange(F.order())) * m for m in mons)
        if f != 0:
            return f


def monomials_of_degree(R, d, wts):
    out = []

    def rec(i, rem, cur):
        if i == R.ngens():
            if rem == 0:
                out.append(prod_(g ** e for g, e in zip(R.gens(), cur)))
            return
        for e in range(rem // wts[i] + 1):
            rec(i + 1, rem - e * wts[i], cur + [e])
    rec(0, d, [])
    return out


def section_5_4():
    """Section 5.4: the Nullstellensatz and its proof, the Zariski topology,
    dilations, localisation (corrected), Noether normalisation and Krull
    dimension, dominant and finite maps (corrected), inseparable isogenies,
    Hilbert-Noether, Cohen-Macaulay rings, Macaulay's theorem."""
    rnd = random.Random(54)
    # Lemma 5.4.1, the proof: for k not algebraically closed the residue
    # fields of maximal ideals are finite (algebraic) extensions
    for F, gens in ((GF(2), lambda x, y: [x ** 2 + x + 1, y + x]),
                    (GF(2), lambda x, y: [x, y ** 3 + y + 1]),
                    (GF(3), lambda x, y: [x ** 2 + 1, y ** 3 - y - 1]),
                    (GF(5), lambda x, y: [x - 2, y + 3])):
        R = PolynomialRing(F, 'x,y')
        x, y = R.gens()
        I = R.ideal(gens(x, y))
        check(I.is_prime() and I.dimension() == 0 and
              I.vector_space_dimension() < 10,
              'proof of Lemma 5.4.1: the maximal ideal %s of %s[x, y] has a '
              'residue field of finite degree %d over k (x, y algebraic)'
              % (I.gens(), F, I.vector_space_dimension()))
    # Theorem 5.4.2 and its proof (Rabinowitsch), corrected: f(v) = 0 for
    # all v in V(I)
    cases = []
    for F in (GF(2), GF(3), QQ):
        R = PolynomialRing(F, 'x,y,z')
        x, y, z = R.gens()
        cases += [(R, [x ** 2, x * y], x), (R, [y ** 2 - x ** 3, x ** 2 * y],
                                             x * y),
                  (R, [x ** 3 - y * z, y ** 2, z ** 2 - x * y], x + y + z),
                  (R, [(x + y) ** 2 * z, x ** 3 - z], y * z),
                  (R, [x * y * z, x + y + z, x * y + y * z + z * x], x)]
    for R, fs, f in cases:
        I = R.ideal(fs)
        S = PolynomialRing(R.base_ring(), list(R.variable_names()) + ['t'])
        t = S.gens()[-1]
        Js = [S(g) for g in fs] + [1 - S(f) * t]
        J = S.ideal(Js)
        inrad = f in I.radical()
        ok = (S(1) in J) == inrad
        if inrad:
            coeffs = S(1).lift(J)
            assert sum(c * g for c, g in zip(coeffs, Js)) == 1
            # substitute t = 1/f and clear denominators
            r = max(c.degree(t) for c in coeffs)
            hs = []
            for c, g in zip(coeffs[:-1], fs):
                h = sum(c.coefficient({t: j}) * S(f) ** (r - j)
                        for j in range(r + 1))
                hs.append(R(h))
            ok &= sum(h * g for h, g in zip(hs, fs)) == f ** r
            ok &= f ** r in I
        check(ok, 'Theorem 5.4.2 and its proof: f_1, ..., f_s, 1 - f t '
              'generate the unit ideal iff f vanishes on V(I); then '
              'f_1 h_1 + ... + f_s h_s = f^r after t = 1/f (I = %s, f = %s, '
              'over %s, f in sqrt(I): %s)' % (fs, f, R.base_ring(), inrad))
    # p. 163: V(I_1 I_2) = V(I_1) u V(I_2) and V(I_1 + I_2) = V(I_1) n
    # V(I_2) through radicals; closed sets are finite unions of irreducible
    # ones (minimal primes)
    for F in (GF(2), GF(3)):
        R = PolynomialRing(F, 'x,y,z')
        ok, n = True, 0
        for _ in range(8):
            I1 = R.ideal([random_homogeneous(R, rnd.randint(1, 2), rnd)
                          for _ in range(2)])
            I2 = R.ideal([random_homogeneous(R, rnd.randint(1, 2), rnd)
                          for _ in range(2)])
            r1, r2 = I1.radical(), I2.radical()
            ok &= (I1 * I2).radical() == r1.intersection(r2) == \
                I1.intersection(I2).radical()
            ok &= (I1 + I2).radical() == (r1 + r2).radical()
            mins = I1.minimal_associated_primes()
            ok &= all(P.is_prime() for P in mins)
            inter = mins[0]
            for P in mins[1:]:
                inter = inter.intersection(P)
            ok &= inter == r1
            n += 1
        check(ok, 'p. 163: sqrt(I_1 I_2) = sqrt(I_1) n sqrt(I_2) (V(I_1 I_2) '
              '= V(I_1) u V(I_2)), sqrt(I_1 + I_2) = sqrt(sqrt(I_1) + '
              'sqrt(I_2)), and sqrt(I) is the intersection of finitely many '
              'primes (%d random pairs over %s)' % (n, F))
    # Exercise p. 164 (dilations) and the line through a point
    F = GF(7)
    R = PolynomialRing(F, 'x,y')
    x, y = R.gens()

    def dil(f, lam):
        return f(lam * x, lam * y)
    Ih = R.ideal([x ** 2 + 3 * y ** 2, x * y ** 2 - y ** 3])
    In = R.ideal([x ** 2 + y])
    check(all(dil(f, l) in Ih for f in Ih.gens() for l in F if l) and
          not all(dil(f, l) in In for f in In.gens() for l in F if l),
          'Exercise p. 164: a homogeneous ideal is stable under all '
          'dilations m_lambda, the non-homogeneous (x^2 + y) is not (over '
          'GF(7))')
    ok = True
    for a, b in ((1, 0), (0, 1), (2, 5), (3, 3)):
        hom = []
        for d in range(1, 4):
            mons = monomials_of_degree(R, d, [1, 1])
            A = mrows(F, [[m(a, b) for m in mons]])
            for v in kernel_cols(A).columns():
                hom.append(sum(c * m for c, m in zip(v, mons)))
        ok &= R.ideal(hom) == R.ideal(b * x - a * y)
    check(ok, 'p. 164: the largest homogeneous ideal in the maximal ideal of '
          'a point alpha != 0 of A^2 is the ideal (b x - a y) of the line '
          'through alpha (four points over GF(7), degrees <= 3)')
    # p. 165, localisation.  Printed: S = elements that are not zero
    # divisors modulo I.  A = k[x], I = (x): S = {f : f(0) != 0}
    for F in (GF(2), GF(3), GF(5)):
        R = PolynomialRing(F, 1, 'x')
        x = R.gen()
        I = R.ideal(x)
        # f is a non-zero-divisor on A/I = k iff f(0) != 0
        polys = [c0 + c1 * x + c2 * x ** 2 for c0 in F for c1 in F
                 for c2 in F]
        ok = all((I.quotient(R.ideal(f)) == I) == (f(0) != 0)
                 for f in polys if f != 0)
        check(ok, 'p. 165: for A = %s[x], I = (x) the elements that are not '
              'zero divisors modulo I are the f with f(0) != 0 (all f of '
              'degree <= 2)' % F)
        # (x - a) survives in A[S^-1] iff it does not meet S: for a != 0
        # it contains x - a, which lies in S; (x) is disjoint from S
        survive = [a for a in F if (x - a)(0) == 0]
        printed = [a for a in F if a != 0]            # max(A) minus V(I)
        refuted(survive == printed,
                'p. 165 (printed): with S the non-zero-divisors modulo I, '
                'max(A[S^-1]) = max(A) minus V(I); for A = %s[x], I = (x) the '
                'maximal ideals (x - a), a != 0, meet S and the only one '
                'surviving is (x), which contains I' % F)
        # corrected: S = {x^n}, I = (x): A[x^-1] = k[x, y]/(x y - 1)
        Ry = PolynomialRing(F, 'x,y')
        X, Y = Ry.gens()
        loc = Ry.ideal(X * Y - 1)
        pts = [a for a in F if Ry(1) not in loc + Ry.ideal(X - a)]
        check(pts == printed and all(
            (loc + Ry.ideal(X - a, Y - 1 / a)).is_prime() for a in printed),
            'p. 165 (corrected, S = {f^n}, I = (f)): max(A[f^-1]) = max(A) '
            'minus V(f) for A = %s[x], f = x (the F-points of A[x^-1] = '
            'k[x, y]/(x y - 1) lie over x = a != 0)' % F)
    # the same failure for a non-principal I in two variables
    F = GF(3)
    R = PolynomialRing(F, 'x,y')
    x, y = R.gens()
    I = R.ideal(x, y)
    # S = non-zero-divisors modulo (x, y) = {f : f(0, 0) != 0}; the
    # maximal ideal of the origin is disjoint from S, every other point's
    # maximal ideal (x - a, y - b) contains x - a or y - b, which lie in S
    ok = all(((x - a) if a else (y - b))(0, 0) != 0 for a in F for b in F
             if (a, b) != (0, 0))
    check(ok, 'p. 165: for A = k[x, y], I = (x, y) the printed S = {f : '
          'f(0) != 0} meets every maximal ideal except (x, y) itself, so '
          'A[S^-1] is the local ring at the origin, not max(A) minus V(I)')
    # Lemma 5.4.5 and Theorem 5.4.6: homogeneous Noether normalisation
    for lab, R, wts, rels in graded_examples():
        I = R.ideal(rels) if rels else R.ideal(0)
        dim = I.dimension()
        found = None
        cands = []
        for d in sorted(set(wts)):
            cands += [g for g in R.gens() if g.degree() == d] if \
                all(w == 1 for w in wts) else \
                [g for g, w in zip(R.gens(), wts) if w == d]
        for d in range(1, 5):
            for _ in range(2):
                f = random_homogeneous(R, d, rnd, list(wts))
                if f is not None:
                    cands.append(f)
        L = 1
        for w in wts:
            L = L * w // gcd(L, w)
        cands.append(sum(g ** (L // w) for g, w in zip(R.gens(), wts)))
        for sub in itertools.combinations(cands, dim):
            if (I + R.ideal(list(sub))).dimension() == 0 if sub else \
                    I.dimension() == 0:
                found = sub
                break
        check(found is not None and len(found) == dim,
              'Lemma 5.4.5 (graded): homogeneous y_1, ..., y_n with A finite '
              'over k[y_1, ..., y_n] (A/(y) finite dimensional), n = Krull '
              'dimension %d = number of parameters (%s: %s)'
              % (dim, lab, found))
    # Theorem 5.4.6: chains of primes of length dim A
    R = PolynomialRing(GF(2), 'x,y,w')
    x, y, w = R.gens()
    I = R.ideal(x * y)
    chain = [R.ideal(x, y, w), R.ideal(x, w), R.ideal(x)]
    check(all(P.is_prime() and I <= P for P in chain) and
          chain[0] > chain[1] > chain[2] and I.dimension() == 2 and
          (R.ideal(x)).dimension() == 2,
          'Theorem 5.4.6: H^*(D8) = F2[x, y, w]/(xy) has the chain of primes '
          '(x, y, w) > (x, w) > (x) of length 2 = dim')
    R = PolynomialRing(GF(3), 'x,y,z')
    x, y, z = R.gens()
    P = R.ideal(x ** 3 - y ** 2 * z)
    check(P.is_prime() and P.dimension() == 2,
          'Theorem 5.4.6 (i): k[x, y, z]/(x^3 - y^2 z) is a domain of '
          'dimension 2 = tr.deg (x, y algebraically independent)')
    # p. 167: dominant maps.  phi : k[u, v] -> k[x, y], u -> x, v -> x y
    for F in (GF(2), GF(3), GF(4, 'a'), GF(5), GF(7)):
        S = PolynomialRing(F, 'u,v,x,y', order='lex')
        u, v, X, Y = S.gens()
        J = S.ideal(u - X, v - X * Y)
        elim = J.elimination_ideal([X, Y])
        dominant = elim == S.ideal(0)
        # fibres: over (a, b) the ideal (x - a, x y - b)
        img = [(a, b) for a in F for b in F
               if S(1) not in J + S.ideal(u - a, v - b)]
        expect = [(a, b) for a in F for b in F if a != 0 or b == 0]
        empty_line = v in J + S.ideal(u)
        check(dominant and img == expect and empty_line,
              'p. 167: (x, y) |-> (x, x y) is dominant (k[x, x y] = '
              'k[u, v]) with image {u != 0} u {(0, 0)} (fibres over %d '
              'F-points, %s; the fibre over (0, b), b != 0, is empty over '
              'every extension)' % (F.order() ** 2, F))
    # the image is not open: it meets the irreducible line u = 0 in the
    # single point (0, 0); it contains the dense open set u != 0
    S = PolynomialRing(QQ, 'u,v,x,y', order='lex')
    u, v, X, Y = S.gens()
    J = S.ideal(u - X, v - X * Y)
    on_line = (J + S.ideal(u)).elimination_ideal([X, Y])
    R2 = PolynomialRing(QQ, 'u,v')
    refuted(on_line == S.ideal(u),
            'p. 167 (printed): the image of a dominant map is open; for (x, '
            'y) |-> (x, x y) the image meets the line u = 0 only in V(u, v) '
            '= {(0, 0)} (elimination ideal %s), a non-empty closed proper '
            'subset of an irreducible curve, so the image is not open'
            % (on_line.gens(),))
    check(on_line == S.ideal(u, v) and R2.ideal(R2.gen(0)).is_prime(),
          'p. 167 (corrected): the image contains the dense open subset '
          '{u != 0} (Chevalley; Eisenbud, Corollary 14.6 and the example of '
          'Section 14.3), but meets V(u) only in (0, 0)')
    # a dominant map that is not finite need not be surjective, a finite
    # dominant map is (Theorem 5.4.7): k[u] -> k[x, y]/(x y - 1), u -> x
    R = PolynomialRing(GF(5), 'x,y')
    x, y = R.gens()
    L = R.ideal(x * y - 1)
    check(R(1) in L + R.ideal(x) and all(
        R(1) not in L + R.ideal(x - a) for a in GF(5) if a),
        'p. 167: k[u] -> k[x, y]/(xy - 1) is dominant (injective) with image '
        'A^1 minus {0}: not finite (otherwise surjective by Theorem 5.4.7)')
    F16 = GF(16, 'b')
    R = PolynomialRing(F16, 'x')
    x = R.gen()
    check(all(len((x ** 2 + x - c).roots()) >= 1
              for c in F16 if c ** 4 == c),
          'Theorem 5.4.7: the finite map k[u] -> k[x], u -> x^2 + x is '
          'surjective on points (every fibre over GF(4) meets GF(16))')
    # p. 167: inseparable isogenies; A = k[x^2, xy, y^2] between
    # B^[2] = k[x^2, y^2] and B = k[x, y]
    for m in (1, 2, 3, 4):
        F = GF(2 ** m, 'a')
        pts = [(a, b) for a in F for b in F]
        img = set((a * a, a * b, b * b) for a, b in pts)
        targ = set((u, v, w) for u in F for v in F for w in F
                   if v * v == u * w)
        check(len(img) == len(pts) and img == targ,
              'p. 167: max k[x, y] -> max k[x^2, x y, y^2] (= V(v^2 - '
              'u w)) is bijective on GF(%d)-points; composed with max A -> '
              'max B^[2] it is the Frobenius (a, b) |-> (a^2, b^2)'
              % F.order())
    for m in (1, 2, 3):
        F = GF(3 ** m, 'a')
        img = set((a ** 3, a ** 4) for a in F)
        targ = set((u, w) for u in F for w in F if w ** 3 == u ** 4)
        check(len(img) == F.order() and img == targ,
              'p. 167: B = k[x] > A = k[x^3, x^4] > B^[3] = k[x^3]: max '
              'B -> max A is bijective on GF(%d)-points (a cusp)' % F.order())
    # Proposition 5.4.8 (Hilbert-Noether): GL_2(F_2) on F_2[x, y]
    F = GF(2)
    R = PolynomialRing(F, 'x,y')
    x, y = R.gens()
    Gl = [(a, b, c, d) for a in F for b in F for c in F for d in F
          if a * d - b * c != 0]

    def act(g, f):
        a, b, c, d = g
        return f(a * x + b * y, c * x + d * y)
    d2 = x ** 2 + x * y + y ** 2
    d3 = x ** 2 * y + x * y ** 2
    ok = all(act(g, d2) == d2 and act(g, d3) == d3 for g in Gl)
    for deg in range(0, 13):
        mons = monomials_of_degree(R, deg, [1, 1])
        # invariants of degree deg: kernel of (g - 1) on the monomial basis
        A = []
        for g in Gl:
            for mo2 in mons:
                A.append([act(g, mo).monomial_coefficient(mo2) -
                          (1 if mo == mo2 else 0) for mo in mons])
        inv_dim = kernel_cols(mrows(F, A)).ncols()
        dick = len([(i, j) for i in range(deg // 2 + 1)
                    for j in range(deg // 3 + 1) if 2 * i + 3 * j == deg])
        span = [d2 ** i * d3 ** j for i in range(deg // 2 + 1)
                for j in range(deg // 3 + 1) if 2 * i + 3 * j == deg]
        Sp = mrows(F, [[f.monomial_coefficient(mo) for mo in mons]
                       for f in span], len(mons))
        ok &= inv_dim == dick == rk(Sp)
    for a0 in (x, y):
        poly = prod_(PolynomialRing(R, 'T').gen() - act(g, a0) for g in Gl)
        ok &= all(all(act(g, c) == c for g in Gl) for c in poly.list())
    check(ok, 'Proposition 5.4.8 (Hilbert-Noether): F_2[x, y]^(GL_2(F_2)) = '
          'F_2[d_2, d_3] (Dickson; degrees <= 12), x and y are roots of '
          'prod_g (T - g(a)) with invariant coefficients')
    for m in (2, 4):
        Fq = GF(2 ** m, 'a')
        orbit_of, fib = {}, {}
        for a in Fq:
            for b in Fq:
                key = (a * a + a * b + b * b, a * a * b + a * b * b)
                fib.setdefault(key, set()).add((a, b))
        ok = True
        for key, pts in fib.items():
            a, b = next(iter(pts))
            orb = set((g[0] * a + g[1] * b, g[2] * a + g[3] * b) for g in Gl)
            ok &= orb == pts
        check(ok, 'Proposition 5.4.8: the fibres of max F[x, y] -> max '
              'F[x, y]^GL_2(F_2) on GF(%d)^2 are exactly the orbits'
              % Fq.order())
    # Cohen-Macaulay rings: Definition 5.4.9, Theorem 5.4.10, regular
    # sequences
    R = PolynomialRing(GF(2), 'x,y,w', order=TermOrder('wdegrevlex',
                                                       (1, 1, 2)))
    x, y, w = R.gens()
    I = R.ideal(x * y)
    hsops = [([w, x + y], [2, 1]), ([w + x ** 2, x + y], [2, 1]),
             ([w + y ** 2, x + y], [2, 1]), ([w, x ** 2 + y ** 2], [2, 2])]
    check(all(is_regular_sequence(I, s) and hs_free_over(I, (1, 1, 2), s, d)
              for s, d in hsops),
          'Theorem 5.4.10 (ii): H^*(D8) = F2[x, y, w]/(xy) is free over '
          'k[z_1, '
          'z_2] for each of four homogeneous systems of parameters, each a '
          'regular sequence: Cohen-Macaulay of depth 2')
    R = PolynomialRing(GF(2), 'x,y')
    x, y = R.gens()
    I = R.ideal(x ** 2, x * y)
    ok = all(hs_free_over(I, (1, 1), [s], [s.degree()]) is False and
             not is_regular_sequence(I, [s])
             for s in (y, x + y, y ** 2 + x * y))
    check(ok, 'Definition 5.4.9, Theorem 5.4.10: F2[x, y]/(x^2, xy) has '
          'dimension 1 and depth 0 (every hsop is a zero divisor: x . m = '
          '0), and is free over no k[z] (not Cohen-Macaulay)')
    R = PolynomialRing(GF(2), 'x,y,z', order=TermOrder('wdegrevlex',
                                                       (1, 1, 4)))
    x, y, z = R.gens()
    I = R.ideal(x ** 2 + x * y + y ** 2, x ** 2 * y + x * y ** 2)
    check(all(hs_free_over(I, (1, 1, 4), [s], [4]) and
              is_regular_sequence(I, [s]) for s in (z, z + x ** 4,
                                                     z + x * y ** 3)),
          'Theorem 5.4.10: H^*(Q8) is free over k[zeta] for three choices '
          'of a degree 4 parameter (Cohen-Macaulay of dimension 1)')
    # Theorem 5.4.11 (Macaulay) for homogeneous sequences
    tot, agree = 0, True
    for F, nv in ((GF(2), 3), (GF(2), 4), (GF(3), 3)):
        R = PolynomialRing(F, nv, 'x')
        for _ in range(25):
            r = rnd.randint(1, nv)
            seq = [random_homogeneous(R, rnd.randint(1, 2), rnd)
                   for _ in range(r)]
            if rnd.random() < 0.3 and r >= 2:
                seq[-1] = seq[0] * random_homogeneous(R, 1, rnd)
            I = R.ideal(seq)
            agree &= is_regular_sequence(R.ideal(0), seq) == \
                (I.dimension() == nv - r)
            tot += 1
    check(agree, 'Theorem 5.4.11 (Macaulay): homogeneous zeta_1, ..., '
          'zeta_r form a regular sequence in k[x_1, ..., x_n] iff dim '
          'k[x]/(zeta) = n - r (%d random sequences, n = 3, 4, over GF(2), '
          'GF(3))' % tot)
    R = PolynomialRing(QQ, 'x,y,z')
    x, y, z = R.gens()
    seq = [y * (x - 1), z * (x - 1), x]
    refuted(is_regular_sequence(R.ideal(0), seq),
            'Theorem 5.4.11 needs the homogeneity of Definition 5.4.9: y(x - '
            '1), z(x - 1), x generate (x, y, z) of dimension 0 = 3 - 3 but '
            'z(x - 1) is a zero divisor modulo y(x - 1)')


# ===========================================================================
# Section 5.5: quadratic forms over F_2 and extraspecial 2-groups
# ===========================================================================


class QForm:
    """A quadratic form on E = F_2^n: q(e_i) = qd[i], b(e_i, e_j) = bm[i][j]
    (alternating)."""

    def __init__(self, n, qd, bm):
        self.n, self.qd, self.bm = n, qd, bm

    def __call__(self, w):
        n = self.n
        return (sum(self.qd[i] * w[i] for i in range(n)) +
                sum(self.bm[i][j] * w[i] * w[j] for i in range(n)
                    for j in range(i + 1, n))) % 2

    def poly(self, S, w=None):
        """q(v) in S = k[x_1, ..., x_n] (or at coordinates w)."""
        x = S.gens() if w is None else w
        n = self.n
        return (sum(self.qd[i] * x[i] ** 2 for i in range(n)) +
                sum(self.bm[i][j] * x[i] * x[j] for i in range(n)
                    for j in range(i + 1, n)))

    def b_frob(self, S, r):
        """b(v, F^r(v)) = sum_(i<j) b(e_i, e_j)(x_i x_j^(2^r) + x_j
        x_i^(2^r)) (p. 171)."""
        x = S.gens()
        n = self.n
        e = 2 ** r
        return sum(self.bm[i][j] * (x[i] * x[j] ** e + x[j] * x[i] ** e)
                   for i in range(n) for j in range(i + 1, n))

    def subspaces(self):
        """All subspaces of F_2^n as frozensets of vectors (tuples)."""
        n = self.n
        vecs = list(itertools.product(range(2), repeat=n))
        out = {frozenset([(0,) * n])}
        frontier = list(out)
        while frontier:
            new = []
            for W in frontier:
                for v in vecs:
                    if v in W:
                        continue
                    W2 = frozenset(list(W) + [tuple((a + b) % 2 for a, b in
                                                    zip(v, w)) for w in W])
                    if W2 not in out:
                        out.add(W2)
                        new.append(W2)
            frontier = new
        return out

    def maximal_isotropic(self):
        iso = [W for W in self.subspaces() if all(self(w) == 0 for w in W)]
        return [W for W in iso if not any(W < W2 for W2 in iso)]


def all_forms(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for qd in itertools.product(range(2), repeat=n):
        for bs in itertools.product(range(2), repeat=len(pairs)):
            bm = [[0] * n for _ in range(n)]
            for (i, j), c in zip(pairs, bs):
                bm[i][j] = bm[j][i] = c
            yield QForm(n, list(qd), bm)


def subspace_ideal(S, W):
    """The ideal of k (x) W in k[V] = k[x_1, ..., x_n]: linear forms
    vanishing on W."""
    n = S.ngens()
    F2 = GF(2)
    A = mrows(F2, [list(w) for w in W], n)
    K = kernel_cols(A)
    return S.ideal([sum(int(c) * S.gen(i) for i, c in enumerate(col))
                    for col in K.columns()] or [S(0)])


def steenrod_total(f, S):
    """The total square Sq on F_2[x_1, ..., x_n]: the ring homomorphism
    with Sq(x_i) = x_i + x_i^2 (Cartan formula)."""
    return f(*[g + g ** 2 for g in S.gens()])


def sq(k, f, S):
    """Sq^k f for homogeneous f."""
    tot = steenrod_total(f, S)
    d = f.degree() + k
    return sum((c * m for c, m in zip(tot.coefficients(), tot.monomials())
                if m.degree() == d), S(0))


def check_quadratic_form(qf, S, extra=2):
    """Lemma 5.5.1, Proposition 5.5.2 and the last sentence of Theorem 5.5.3
    for one form; returns h and a list of failed items."""
    n = qf.n
    maxi = qf.maximal_isotropic()
    dims = set(rank_of(len(W), 2) for W in maxi)
    bad = []
    if len(dims) != 1:
        bad.append('maximal isotropic subspaces of different dimensions')
    h = n - dims.pop()
    seq = [qf.poly(S)] + [qf.b_frob(S, r) for r in range(1, h)]
    seq = [f for f in seq]
    J = S.ideal(seq) if seq else S.ideal(0)
    # regular sequence (colon criterion and Hilbert series)
    if h and not is_regular_sequence(S.ideal(0), seq):
        bad.append('not a regular sequence')
    if h:
        T = J.hilbert_series().parent().gen()
        degs = [2] + [2 ** r + 1 for r in range(1, h)]
        if J.hilbert_series() != prod_(1 - T ** d for d in degs) / \
                (1 - T) ** n:
            bad.append('Hilbert series')
    # V(J_h) = union of k (x) E', E' maximal isotropic
    rad = J.radical() if h else S.ideal(0)
    inter = None
    for W in maxi:
        I = subspace_ideal(S, W)
        inter = I if inter is None else inter.intersection(I)
    if rad != inter:
        bad.append('variety')
    if J.dimension() != n - h:
        bad.append('codimension')
    # b(v, F^r v) in J_h (Theorem 5.5.3) for h <= r <= h + extra
    for r in range(max(h, 1), h + extra + 1):
        if qf.b_frob(S, r) not in J:
            bad.append('b(v, F^%d v) not in J_h' % r)
    # Lemma 5.5.1: V(J_r) strictly decreasing for r < h, constant after
    rads = []
    for r in range(0, h + 2):
        gens = ([qf.poly(S)] if r >= 1 else []) + \
            [qf.b_frob(S, s) for s in range(1, r)]
        rads.append(S.ideal(gens).radical() if gens else S.ideal(0))
    for r in range(0, h):
        if rads[r] == rads[r + 1]:
            bad.append('V(J_%d) = V(J_%d)' % (r, r + 1))
    if rads[h] != rads[h + 1]:
        bad.append('V(J_h) != V(J_(h+1))')
    # Steenrod operations: Sq^(2^(r-1)) ... Sq^1 q(v) = b(v, F^r v)
    f = qf.poly(S)
    for r in range(1, 4):
        f = sq(2 ** (r - 1), f, S)
        if f != qf.b_frob(S, r):
            bad.append('Sq formula r = %d' % r)
    return h, bad


def expansion_identity(qf, S, r, start):
    """The display of p. 170 with all sums from `start`:
    q(sum lambda_i F^i v) = sum lambda_i^2 q(v)^(2^i) + sum_(i<j)
    lambda_i lambda_j b(v, F^(j-i) v)^(2^i), as an identity in
    k[x, lambda] and the set of v where the left side vanishes
    identically in the lambda."""
    n = qf.n
    T = PolynomialRing(S, 'l', r)
    lam = T.gens()
    x = S.gens()
    w = [sum(lam[i] * x[j] ** (2 ** i) for i in range(start, r))
         for j in range(n)]
    lhs = qf.poly(T, w)
    rhs = sum(lam[i] ** 2 * qf.poly(S) ** (2 ** i) for i in range(start, r))
    rhs += sum(lam[i] * lam[j] * qf.b_frob(S, j - i) ** (2 ** i)
               for i in range(start, r) for j in range(i + 1, r))
    return lhs == rhs, lhs


def group_form(G):
    """For G with |Phi(G)| = 2 = N: the basis of E = G/N given by the
    minimal generators, q(e_i) and b(e_i, e_j) read off squares and
    commutators."""
    z = None
    gens = G.gens
    n = len(gens)
    Phi = G.closure([G.comm(a, b) for a in range(G.n) for b in range(G.n)] +
                    [G.mul[a][a] for a in range(G.n)])
    assert len(Phi) == 2
    z = [x for x in Phi if x != G.e][0]

    def val(x):
        assert x in Phi
        return 0 if x == G.e else 1
    qd = [val(G.mul[g][g]) for g in gens]
    bm = [[val(G.comm(g, h)) for h in gens] for g in gens]
    return QForm(n, qd, bm), Phi, z


def section_5_5():
    """Lemma 5.5.1, Proposition 5.5.2 (all forms on F_2^n, n <= 3, and
    samples for n = 4, 5), the display p. 170 (corrected sums from 0), the
    Steenrod formula p. 171, Theorem 5.5.3 for the groups with |Phi(G)| = 2
    of order <= 32 (including 2^(1+2)_+- = D8, Q8 and 2^(1+4)_+-), the
    Exercise 2 (Avrunin-Carlson) for n = 2, 3."""
    rnd = random.Random(55)
    for n in (1, 2, 3, 4, 5):
        S = PolynomialRing(GF(2), n, 'x')
        forms = list(all_forms(n)) if n <= 3 else None
        if forms is None:
            allf = all_forms(n) if n == 4 else None
            if n == 4:
                forms = [f for f in all_forms(4)]
                rnd.shuffle(forms)
                forms = forms[:40]
            else:
                forms = []
                for _ in range(10):
                    qd = [rnd.randrange(2) for _ in range(5)]
                    bm = [[0] * 5 for _ in range(5)]
                    for i in range(5):
                        for j in range(i + 1, 5):
                            bm[i][j] = bm[j][i] = rnd.randrange(2)
                    forms.append(QForm(5, qd, bm))
        hs, bads = [], []
        for qf in forms:
            h, bad = check_quadratic_form(qf, S, extra=2 if n <= 3 else 1)
            hs.append(h)
            bads += bad
        check(not bads, 'Lemma 5.5.1, Proposition 5.5.2, Theorem 5.5.3 '
              '(last sentence): for %d quadratic forms on F_2^%d (%s): all '
              'maximal isotropic subspaces have codimension h; q(v), '
              'b(v, F v), ..., b(v, F^(h-1) v) is a regular sequence (Hilbert '
              'series prod (1 - t^(d_i)) / (1 - t)^n); its variety is the '
              'union of the k (x) E\', E\' maximal isotropic, of codimension '
              'h; V(J_r) decreases strictly up to r = h and V(J_h) = '
              'V(J_(h+1)); b(v, F^r v) lies in J_h for r >= h; Sq^(2^(r-1)) '
              '... Sq^1 q(v) = b(v, F^r v) (r <= 3); h takes the values %s'
              % (len(forms), n, 'all' if n <= 3 else 'a sample',
                 sorted(set(hs))))
    # the display p. 170: corrected (sums from 0) and printed (from 1)
    ok = True
    for n in (2, 3):
        S = PolynomialRing(GF(2), n, 'x')
        for qf in all_forms(n):
            for r in (1, 2, 3):
                ok &= expansion_identity(qf, S, r, 0)[0]
    check(ok, 'p. 170 (corrected): q(sum_(i=0)^(r-1) lambda_i F^i(v)) = '
          'sum_(i=0)^(r-1) lambda_i^2 q(v)^(2^i) + sum_(0<=i<j<=r-1) lambda_i '
          'lambda_j b(v, F^(j-i)(v))^(2^i) in k[V][lambda] (all forms, n = '
          '2, 3, r <= 3)')
    # with the printed ranges (from 1) the left side vanishes identically
    # in lambda on V(J_(r-1)), not on V(J_r): Q8 form, r = 2, v = (1, w)
    F4 = GF(4, 'w')
    om = F4.gen()
    qQ = QForm(2, [1, 1], [[0, 1], [1, 0]])
    S = PolynomialRing(F4, 2, 'x')
    ident_ok, lhs = expansion_identity(qQ, S, 2, 1)
    v = (F4(1), om)
    lam_poly = lhs.map_coefficients(lambda c: c(*v))
    in_J2 = qQ.poly(S)(*v) == 0 and qQ.b_frob(S, 1)(*v) == 0
    refuted((lam_poly == 0) == in_J2,
            'p. 170 (printed sums from i = 1): the expansion of q(sum '
            'lambda_i F^i v) vanishes identically in lambda exactly on '
            'V(J_r); '
            'for the form of Q8 (x_1^2 + x_1 x_2 + x_2^2), r = 2 and v = (1, '
            'w), w^2 + w + 1 = 0, it vanishes identically but b(v, F v) = 1 '
            '!= 0, so v is not in V(J_2)')
    check(ident_ok and lam_poly == 0 and not in_J2,
          'p. 170: the printed ranges give a true identity, but only of q on '
          'the span of F(v), ..., F^(r-1)(v), which detects V(J_(r-1)); the '
          'conclusion needs the span of v, ..., F^(r-1)(v)')
    # Theorem 5.5.3 for groups
    cases = [('C4', 8), ('C4xC2', 10), ('D8', 10), ('Q8', 10),
             ('C4xC2xC2', 8), ('D8xC2', 8), ('Q8xC2', 8), ('C4oD8', 9),
             ('32_45', 6), ('32_46', 6), ('32_47', 6), ('32_48', 6),
             ('2^(1+4)_+', 10), ('2^(1+4)_-', 10)]
    for name, N in cases:
        C = cohom(name, 2, N)
        G, F = C.G, C.F
        qf, Phi, z = group_form(G)
        n = qf.n
        # the quadratic form of p. 171: well defined, b = commutators
        ok = True
        # coordinates of g in E: the values of the dual homomorphisms
        duals = [C.class_of_hom(dual_hom(G, qf, Phi, i)) for i in range(n)]
        coords = {g: tuple(int(c) for c in dual_coords(G, Phi, i_g=g,
                                                       gens=G.gens))
                  for g in range(G.n)}
        for a in range(G.n):
            sa = 0 if G.mul[a][a] == G.e else 1
            ok &= sa == qf(coords[a])
            for b in range(G.n):
                ab = G.mul[a][b]
                lhs = G.mul[ab][ab]
                rhs = G.mul[G.mul[G.mul[a][a]][G.mul[b][b]]][G.comm(a, b)]
                ok &= lhs == rhs
                ok &= (0 if G.comm(a, b) == G.e else 1) == \
                    sum(qf.bm[i][j] * coords[a][i] * coords[b][j]
                        for i in range(n) for j in range(n)) % 2
        check(ok, 'p. 171: (x y)^2 = x^2 y^2 [x, y] in %s; q(x) = x~^2 is a '
              'quadratic form on E = G/N with polar form b(x, y) = [x~, y~] '
              '(all pairs)' % name)
        maxi = qf.maximal_isotropic()
        h = n - rank_of(len(maxi[0]), 2)
        elabs = G.elementary_abelian_subgroups(2)
        maxe = [E for E in elabs if not any(set(E) < set(E2)
                                             for E2 in elabs)]
        check(all(len(E) * 2 ** h == G.n for E in maxe),
              'Theorem 5.5.3: 2^h = %d is the index in %s of every maximal '
              'elementary abelian subgroup (h = codimension of a maximal '
              'isotropic subspace)' % (2 ** h, name))
        T = PowerSeriesRing(QQ, 't', default_prec=N + 2).gen()
        degs = [2] + [2 ** r + 1 for r in range(1, h)]
        pred = prod_(1 - T ** d for d in degs) / ((1 - T) ** n *
                                                  (1 - T ** (2 ** h)))
        check([pred[i] for i in range(N + 1)] == C.b[:N + 1],
              'Theorem 5.5.3: the Poincare series of H^*(%s, F_2) is prod '
              '(1 - t^(d_i)) / ((1 - t)^%d (1 - t^%d)), d = %s, through '
              'degree %d (minimal resolution)' % (name, n, 2 ** h, degs, N))
        # restriction to N = Phi: zero in degrees 1 .. 2^h - 1, non-zero in
        # degree 2^h
        Nsub, incl = G.subgroup(Phi, 'N')
        QN = Resolution(trivial(F, Nsub), N)
        R, _ = restriction(C, Nsub, incl, QN, N)
        zero_below = all(R[d].is_zero() for d in range(1, min(2 ** h, N + 1)))
        if 2 ** h <= N:
            col = next(j for j in range(C.b[2 ** h])
                       if R[2 ** h][0, j] != 0)
            zeta = unit(F, C.b[2 ** h], col)
            check(zero_below and not R[2 ** h].is_zero(),
                  'proof of Theorem 5.5.3: H^j(%s) -> H^j(N) is zero for 0 < '
                  'j < 2^h = %d and some zeta of degree 2^h restricts '
                  'non-trivially (z^(2^h) is a universal cycle)'
                  % (name, 2 ** h))
            gens = [(1, d) for d in duals] + [(2 ** h, zeta)]
            names = ['x%d' % (i + 1) for i in range(n)] + ['zeta']
            P = Presentation(C, gens, names)
            Rr = P.R
            X = Rr.gens()[:n]
            Srr = PolynomialRing(GF(2), n, 'x')
            seq = [qf.poly(Srr)] + [qf.b_frob(Srr, r) for r in range(1, h)]
            Jh = Rr.ideal([f(*X) for f in seq]) if seq else Rr.ideal(0)
            check(P.surj and P.ideal() == Jh,
                  'Theorem 5.5.3: H^*(%s, F_2) = F_2[x_1, ..., x_%d] / (q(v), '
                  'b(v, F v), ..., b(v, F^(%d) v)) (x) F_2[zeta], deg zeta = '
                  '%d, through degree %d: the x_i (inflated from E) and zeta '
                  'generate, and the relations are exactly J_h'
                  % (name, n, h - 1, 2 ** h, N))
    # Exercise 2 (Avrunin and Carlson), n = 2, 3
    for n in (2, 3):
        Fr = libgap.FreeGroup(n)
        g = Fr.GeneratorsOfGroup()
        rels = [g[i] ** 4 for i in range(n)]
        rels += [libgap.Comm(g[i], g[i + 1]) * g[i + 1] ** -2
                 for i in range(n - 1)]
        rels += [libgap.Comm(g[i], g[j]) for i in range(n)
                 for j in range(i + 2, n)]
        Gf = Fr / rels
        Gp = libgap.Image(libgap.IsomorphismPcGroup(Gf))
        G = Grp.from_gap(Gp, 'AC%d' % n)
        Nn = G.closure([G.mul[a][a] for a in range(G.n)])
        C = Cohom(G, GF(2), n + 1)
        ok = G.n == 2 ** (2 * n) and len(Nn) == 2 ** n and \
            all(x in G.center() for x in Nn) and \
            int(libgap.NilpotencyClassOfGroup(Gp)) == 2 and C.b[1] == n
        found = []
        for v in itertools.product(range(2), repeat=n):
            if not any(v):
                continue
            x = vector(GF(2), v)
            if not C.power(x, 1, n).is_zero() and \
                    C.power(x, 1, n + 1).is_zero():
                found.append(v)
        check(ok and found,
              'Exercise 2 p. 172 (Avrunin-Carlson), n = %d: G has order '
              '2^(2n), class two, N = <g_i^2> central of order 2^n, and some '
              'x in H^1(G, F_2) has x^n != 0, x^(n+1) = 0 (%d such x)'
              % (n, len(found)))
        refuted(len(homs_to_Fp(G, 3)) > 0,
                'Exercise 2 p. 172 read with p odd: H^1(G, F_3) = Hom(G, F_3) '
                '= 0 for the 2-group G (n = %d), so F_p must be F_2 here' % n)


# ===========================================================================
# Section 5.6: the Quillen stratification
# ===========================================================================


class ElemData:
    """An elementary abelian 2-subgroup E of G with a basis, the polynomial
    ring H^*(E) = F_2[t_1, ..., t_r] (t_i dual to the basis) and the
    restriction from H^*(G) in these coordinates."""

    def __init__(self, C, Eset, N):
        G = C.G
        self.Eset = sorted(Eset)
        Esub, incl = G.subgroup(self.Eset, 'E')
        self.sub, self.incl = Esub, incl
        # basis: greedy in G-indices
        basis, span = [], [G.e]
        for x in self.Eset:
            if x not in span:
                basis.append(x)
                span = G.closure(basis)
        self.basis = basis
        self.r = len(basis)
        self.S = PolynomialRing(GF(2), max(self.r, 1), 't')
        ix = {g: i for i, g in enumerate(incl)}
        self.res = restriction_poly(C, Esub, incl, [ix[g] for g in basis],
                                    self.S, N) if self.r else None
        # coordinates of the elements of E in the basis
        self.coord = {}
        for v in itertools.product(range(2), repeat=self.r):
            x = G.e
            for b, c in zip(basis, v):
                if c:
                    x = G.mul[x][b]
            self.coord[x] = v

    def pull(self, other, phi):
        """The ring map H^*(other) -> H^*(self) induced by a homomorphism
        phi : self.E -> other.E (dict on G-indices)."""
        imgs = []
        for i in range(other.r):
            # t_i o phi on the basis of self
            imgs.append(sum(other.coord[phi[b]][i] * self.S.gen(j)
                            for j, b in enumerate(self.basis)))
        return lambda f: f(*imgs) if other.r else f


def sigma_E(D):
    """sigma_E = prod over non-zero zeta in H^1(E, F_2) of beta(zeta) =
    zeta^2."""
    t = D.S.gens()
    out = D.S(1)
    for v in itertools.product(range(2), repeat=D.r):
        if any(v):
            out *= sum(c * x for c, x in zip(v, t)) ** 2
    return out


def degree_part_basis(S, d):
    return monomials_of_degree(S, d, [1] * S.ngens())


def poly_vec(f, mons):
    return [f.monomial_coefficient(m) for m in mons]


def section_5_6():
    """Proposition 5.6.1, Lemma 5.6.2, Theorem 5.6.3 and Corollary 5.6.4 for
    small 2-groups; the Exercise p. 175."""
    F = GF(2)
    for name, N, a_exp in (('V4', 8, 0), ('C2^3', 6, 0), ('C4', 10, 1),
                           ('C4xC2', 10, 1), ('D8', 12, 0), ('Q8', 12, 2),
                           ('C8', 10, 2), ('D8xC2', 6, 0)):
        C = cohom(name, 2, N)
        G = C.G
        elabs = [E for E in G.elementary_abelian_subgroups(2) if len(E) > 1]
        datas = [ElemData(C, E, N) for E in elabs]
        idx = {tuple(D.Eset): D for D in datas}
        # the morphisms of C_G: inclusions composed with conjugations
        # (generated by the inclusions of index 2 and the conjugations by
        # the generators of G)
        morph = []
        for D1 in datas:
            for D2 in datas:
                if set(D1.Eset) < set(D2.Eset) and \
                        2 * len(D1.Eset) == len(D2.Eset):
                    morph.append((D1, D2, D1.pull(D2, {x: x for x in
                                                       D1.Eset})))
            for g in G.gens:
                img = tuple(sorted(G.conj(g, x) for x in D1.Eset))
                if img != tuple(D1.Eset):
                    phi = {x: G.conj(g, x) for x in D1.Eset}
                    morph.append((D1, idx[img], D1.pull(idx[img], phi)))
                else:
                    phi = {x: G.conj(g, x) for x in D1.Eset}
                    if any(phi[x] != x for x in D1.Eset):
                        morph.append((D1, D1, D1.pull(D1, phi)))
        lim_ok, img_in_lim, inj_mod_nil, powers_ok = True, True, True, True
        for d in range(1, N + 1):
            blocks = [degree_part_basis(D.S, d) for D in datas]
            offs, tot = [], 0
            for bl in blocks:
                offs.append(tot)
                tot += len(bl)
            # equations: for each morphism and each coordinate of D1:
            # f_D1[k] = sum_c f_D2[c] * pull(m_c)[k]
            eqs = []
            for D1, D2, pull in morph:
                i1, i2 = datas.index(D1), datas.index(D2)
                mat_ = [poly_vec(pull(m2), blocks[i1]) if pull(m2) != 0 else
                        [0] * len(blocks[i1]) for m2 in blocks[i2]]
                for k_ in range(len(blocks[i1])):
                    row = [0] * tot
                    row[offs[i1] + k_] += 1
                    for c in range(len(blocks[i2])):
                        row[offs[i2] + c] += mat_[c][k_]
                    eqs.append(row)
            A = mrows(F, eqs, tot)
            lim = kernel_cols(A)
            # the image of q_G in degree d
            imgs = []
            for j in range(C.b[d]):
                v = unit(F, C.b[d], j)
                row = []
                for D, bl in zip(datas, blocks):
                    row += poly_vec(D.res(d, v), bl)
                imgs.append(row)
            Img = mrows(F, imgs, tot).transpose()
            img_in_lim &= (A * Img).is_zero()
            ker = kernel_cols(Img)
            for z in ker.columns():
                e, nil = 2, False
                while e * d <= N:
                    if C.power(z, d, e).is_zero():
                        nil = True
                        break
                    e *= 2
                inj_mod_nil &= nil or 4 * d > N
            # every element of the limit has its 2^a-th power in the image
            if d * 2 ** a_exp <= N:
                D2 = d * 2 ** a_exp
                blocks2 = [degree_part_basis(D.S, D2) for D in datas]
                imgs2 = []
                for j in range(C.b[D2]):
                    v = unit(F, C.b[D2], j)
                    row = []
                    for D, bl in zip(datas, blocks2):
                        row += poly_vec(D.res(D2, v), bl)
                    imgs2.append(row)
                tot2 = sum(len(b) for b in blocks2)
                Img2 = mrows(F, imgs2, tot2).transpose() if imgs2 else \
                    mat(F, tot2, 0)
                for col in lim.columns():
                    pw = []
                    pos = 0
                    for D, bl, bl2 in zip(datas, blocks, blocks2):
                        f = sum((col[pos + k_] * m for k_, m in enumerate(bl)
                                 if col[pos + k_]), D.S(0))
                        pos += len(bl)
                        pw += poly_vec(f ** (2 ** a_exp), bl2)
                    powers_ok &= in_span(Img2, col_vec(F, pw))
            if a_exp == 0:
                lim_ok &= lim.ncols() == rk(Img)
        check(img_in_lim and inj_mod_nil and powers_ok and lim_ok,
              'Corollary 5.6.4 (Quillen): q_G : H^*(%s, F_2) -> lim_E '
              'H^*(E, F_2) (all %d non-trivial elementary abelian subgroups, '
              'inclusions and conjugations) lands in the limit, its kernel is '
              'nilpotent (degrees <= N/4) and the 2^%d-th power of every '
              'element of the limit is in the image (degrees <= %d)%s'
              % (name, len(datas), a_exp, N,
                 '; q_G is an isomorphism there' if a_exp == 0 else ''))
    # Lemma 5.6.2 for D8 and Q8: rho_E and y'
    for name, N in (('D8', 16), ('Q8', 12), ('C4xC2', 10)):
        C = cohom(name, 2, N)
        G = C.G
        elabs = [E for E in G.elementary_abelian_subgroups(2) if len(E) > 1]
        reps = G.conj_classes_of(elabs)
        datas = {tuple(E): ElemData(C, E, N) for E in elabs}
        ok_rho, ok_y, nchk = True, True, 0
        for E in reps:
            D = datas[tuple(E)]
            NG = [g for g in range(G.n)
                  if sorted(G.conj(g, x) for x in E) == sorted(E)]
            idx = len(NG) // len(E)
            pa = 1
            while idx % (2 * pa) == 0:
                pa *= 2
            sig = sigma_E(D)
            dsig = sig.degree()
            # rho_E: res_E = sigma^(p^a), res_E' = 0 unless E <= conj of E'
            deg = dsig * pa
            if deg > N:
                continue
            others = [datas[tuple(E2)] for E2 in elabs
                      if not any(set(G.conj(g, x) for x in E) <= set(E2)
                                 for g in range(G.n))]
            blocks = [degree_part_basis(D.S, deg)] + \
                [degree_part_basis(D2.S, deg) for D2 in others]
            cols = []
            for j in range(C.b[deg]):
                v = unit(F, C.b[deg], j)
                row = poly_vec(D.res(deg, v), blocks[0])
                for D2, bl in zip(others, blocks[1:]):
                    row += poly_vec(D2.res(deg, v), bl)
                cols.append(row)
            tot = sum(len(b) for b in blocks)
            A = mrows(F, cols, tot).transpose()
            target = poly_vec(sig ** pa, blocks[0]) + [0] * (tot -
                                                             len(blocks[0]))
            ok_rho &= in_span(A, col_vec(F, target))
            nchk += 1
            # part (i): invariant y of degree <= 1, (sigma y)^(p^a)
            t = D.S.gens()
            for dy in (1, 2):
                if (dsig + dy) * pa > N:
                    continue
                mons = degree_part_basis(D.S, dy)
                # invariants under N_G(E)
                eqs = []
                for g in NG:
                    phi = {x: G.conj(g, x) for x in E}
                    pull = D.pull(D, phi)
                    for k_ in range(len(mons)):
                        eqs.append([poly_vec(pull(m), mons)[k_] -
                                    (1 if i == k_ else 0)
                                    for i, m in enumerate(mons)])
                inv = kernel_cols(mrows(F, eqs, len(mons)))
                deg2 = (dsig + dy) * pa
                bl = degree_part_basis(D.S, deg2)
                A2 = mrows(F, [poly_vec(D.res(deg2, unit(F, C.b[deg2], j)),
                                        bl) for j in range(C.b[deg2])],
                           len(bl)).transpose()
                for c in inv.columns():
                    y = sum((c[i] * m for i, m in enumerate(mons) if c[i]),
                            D.S(0))
                    ok_y &= in_span(A2, col_vec(F, poly_vec((sig * y) ** pa,
                                                            bl)))
                    nchk += 1
        check(ok_rho and ok_y,
              'Lemma 5.6.2 (%s): for each class of elementary abelian E there '
              'is rho_E with res_E(rho_E) = sigma_E^(p^a), p^a the 2-part of '
              '|N_G(E) : E|, restricting to zero on every E\' containing no '
              'conjugate of E; and y\' with res_E(y\') = (sigma_E y)^(p^a) '
              'for '
              'N_G(E)-invariant y of degree 1, 2 (%d cases, degrees <= %d)'
              % (name, nchk, N))
    # Theorem 5.6.3: strata, one per conjugacy class; Exercise p. 175: W_G(E)
    # acts freely on V_E^+ (the 1-eigenspace of w != 1 is a proper rational
    # subspace)
    for p, r in ((2, 2), (2, 3), (3, 2)):
        Fp = GF(p)
        ok = True
        from sage.all import GL as _GL
        for w in _GL(r, Fp):
            W = w.matrix()
            if W == 1:
                continue
            K = (W - 1).right_kernel()
            ok &= K.dimension() < r
        check(ok, 'Exercise p. 175: every 1 != w in GL_%d(F_%d) has a proper '
              'F_p-rational 1-eigenspace, contained in some '
              'res^*_(E,E\') V_E\', '
              'so W_G(E) acts freely on V_E^+' % (r, p))


# ===========================================================================
# Sections 5.7 and 5.8: varieties of modules for elementary abelian groups
# ===========================================================================


def elem_group(p, r, F=None):
    G = Grp.from_gap(libgap.ElementaryAbelianGroup(p ** r), 'E%d^%d' % (p, r))
    return G


def theta(M, basis, S):
    """theta = sum_i X_i x_i on M (x) S, X_i = g_i - 1 (p = 2): H^*(E, M) =
    Ker theta / Im theta as an S = H^*(E, k)-module, x_i dual to g_i - 1."""
    Th = _matrix(S, M.dim, M.dim)
    for i, g in enumerate(basis):
        Th += S.gen(i) * M.X(g).change_ring(S)
    return Th


def delta_complex(M, basis, S):
    """For p odd: Hom(Q_*, M) for the tensor product Q of the periodic
    resolutions, as M (x) S (x) Lambda (S = k[y_1, ..., y_r], y_i the
    periodicity shifts, Lambda with basis eps in {0, 1}^r) with the
    S-linear differential: X_i from eps to eps + e_i (eps_i = 0), X_i^(p-1)
    y_i from eps to eps - e_i (eps_i = 1), signs (-1)^(eps_1 + ... +
    eps_(i-1))."""
    F = M.F
    p = F.characteristic()
    r, m = len(basis), M.dim
    epss = list(itertools.product(range(2), repeat=r))
    ix = {e: i for i, e in enumerate(epss)}
    D = _matrix(S, len(epss) * m, len(epss) * m)
    for e in epss:
        for i in range(r):
            sign = (-1) ** sum(e[:i])
            Xi = M.X(basis[i]).change_ring(S)
            if e[i] == 0:
                e2 = tuple(e[j] + (1 if j == i else 0) for j in range(r))
                blk = sign * Xi
            else:
                e2 = tuple(e[j] - (1 if j == i else 0) for j in range(r))
                blk = sign * Xi ** (p - 1) * S.gen(i)
            r0, c0 = ix[e2] * m, ix[e] * m
            for a in range(m):
                for b in range(m):
                    if blk[a, b]:
                        D[r0 + a, c0 + b] += blk[a, b]
    assert (D * D).is_zero()
    return D


def support_ideal(M, basis, S):
    """The annihilator in S of H^*(E, M) = Ker / Im of theta (p = 2) or of
    the complex delta (p odd)."""
    Th = theta(M, basis, S) if M.F.characteristic() == 2 else \
        delta_complex(M, basis, S)
    if Th.is_zero():
        return S.ideal(0)
    K = SYZ(Th)
    if not K:
        return S.ideal(1)
    Km = _matrix(S, [list(v) for v in K]).transpose()
    return S.ideal(list(QUOTIENT(Th, Km)))


def rank_ideal(M, basis, S, twist=False):
    """The rank variety V^#_E(M): the minors of size (p - 1) dim M / p of
    sum lambda_i X_i (lambda_i the variables of S); for p odd with twist,
    the coefficients are raised to the p-th power (the image under the
    Frobenius-semilinear identification lambda |-> lambda^p)."""
    F = M.F
    p = F.characteristic()
    if ((p - 1) * M.dim) % p:
        return S.ideal(0)
    k = (p - 1) * M.dim // p
    if k == 0:
        return S.ideal(1)
    Th = _matrix(S, M.dim, M.dim)
    for i, g in enumerate(basis):
        Th += S.gen(i) * M.X(g).change_ring(S)
    I = S.ideal(list(MINOR(Th, k)) or [S(0)])
    I = S.ideal(I.groebner_basis())
    if twist:
        I = S.ideal([f.map_coefficients(lambda c: c ** p) for f in I.gens()])
    return I


def theta_dims(M, basis, nmax):
    """dim H^n(E, M), n <= nmax, from theta degree by degree (p = 2)."""
    F = M.F
    r, m = len(basis), M.dim
    mons = {n: [a for a in itertools.product(range(n + 1), repeat=r)
                if sum(a) == n] for n in range(nmax + 2)}
    ix = {n: {a: i for i, a in enumerate(mons[n])} for n in mons}
    Xs = [M.X(g) for g in basis]
    th = {}
    for n in range(nmax + 1):
        A = mat(F, len(mons[n + 1]) * m, len(mons[n]) * m)
        for c, a in enumerate(mons[n]):
            for i in range(r):
                a2 = tuple(a[j] + (1 if j == i else 0) for j in range(r))
                rr = ix[n + 1][a2]
                for (u, w), x in Xs[i].dict().items():
                    A[rr * m + u, c * m + w] += x
        th[n] = A
    out = []
    for n in range(nmax + 1):
        out.append(th[n].ncols() - rk(th[n]) - (rk(th[n - 1]) if n else 0))
    return out


def rad_eq(I, J):
    return I.radical() == J.radical()


def v_module(F, G, n, J, inf=False):
    """V_(n, alpha) of Volume I (Theorem 4.3.3): x |-> [[I, I], [0, I]],
    y |-> [[I, J], [0, I]] (or x |-> [[I, J_0], [0, I]], y |-> [[I, I],
    [0, I]] for alpha = infinity)."""
    I = ident(F, n)
    Z = mat(F, n, n)

    def up(B):
        return block_matrix(F, [[I, B], [Z, I]], subdivide=False) if \
            not _sp(F) else up_sparse(F, I, B, n)
    if inf:
        return Mod.from_gens(F, G, [up(J), up(I)])
    return Mod.from_gens(F, G, [up(I), up(J)])


def up_sparse(F, I, B, n):
    ent = {(i, i): 1 for i in range(2 * n)}
    for (i, j), x in B.dict().items():
        ent[(i, n + j)] = x
    return mat(F, 2 * n, 2 * n, ent)


def growth_from_dims(dims):
    """The least d such that the tail of dims is a polynomial of degree
    d - 1 (d = 0 if the tail vanishes), from finite differences on the last
    six terms."""
    tail = list(dims[-7:])
    if all(x == 0 for x in tail):
        return 0
    d = 0
    seq = tail
    while len(set(seq)) > 1:
        seq = [b - a for a, b in zip(seq, seq[1:])]
        d += 1
        if len(seq) < 2:
            return None
    return d + 1


def section_5_7_5_8_E():
    """Varieties of modules for E = (Z/2)^2, (Z/2)^3 (Sections 5.7, 5.8):
    Propositions 5.7.1, 5.7.2, 5.7.3, 5.7.5, 5.7.7, Corollary 5.7.9, Theorem
    5.7.11, Corollary 5.7.12, Theorem 5.8.3."""
    F2, F4 = GF(2), GF(4, 'w')
    om = F4.gen()
    results = {}
    for F in (F2, F4):
        for r in (2, 3):
            if F is F4 and r == 3:
                continue
            G = elem_group(2, r)
            basis = G.gens
            S = PolynomialRing(F, r, 'x')
            k = trivial(F, G)
            mods = {'k': k, 'Omega k': omega_mod(k, 1),
                    'Omega^2 k': omega_mod(k, 2),
                    'Omega^-1 k': omega_inv(k, 1), 'kE': regular_module(F, G)}
            if r == 2:
                one = ident(F, 1)
                for a in ([F(0), F(1)] + ([om, om + 1] if F is F4 else [])):
                    mods['V_(1,%s)' % a] = v_module(F, G, 1, a * one)
                mods['V_(1,inf)'] = v_module(F, G, 1, mat(F, 1, 1), inf=True)
                comp = mat(F, 2, 2, {(1, 0): 1, (0, 1): 1, (1, 1): 1})
                mods['V_(2,w) over F2'] = v_module(F, G, 2, comp)
                jb = mat(F, 2, 2, {(0, 0): 1, (1, 1): 1, (0, 1): 1})
                mods['V_(2,1)'] = v_module(F, G, 2, jb)
            else:
                for a, b, c in itertools.product(range(2), repeat=3):
                    mods['M_(%d,%d,%d)' % (a, b, c)] = carlson_module(
                        F, G, a, b, c)
                mods['period one'] = period_one_module(F, G)
                for E2 in ([basis[0]], [basis[0], basis[1]]):
                    mods['k[E/%d]' % len(E2)] = perm_module(
                        F, G, G.closure(E2))
            rnd = random.Random(57 + r)
            reg = regular_module(F, G)
            for t in range(4 if r == 2 else 2):
                vs = [vector(F, [F.random_element() if rnd.random() < 0.4
                                 else 0 for _ in range(G.n)])
                      for _ in range(1 + t % 2)]
                Sb = submodule_generated(reg, vs)
                if 0 < Sb.ncols() < G.n:
                    mods['random %d' % t] = quotient_action(reg, Sb)
            ok1 = ok3 = ok4 = okr = okc = True
            n = 0
            for lab, M in mods.items():
                A = support_ideal(M, basis, S)
                B = support_ideal(end_module(M), basis, S) if M.dim <= 6 \
                    else None
                Rk = rank_ideal(M, basis, S)
                if B is not None:
                    ok1 &= rad_eq(A, B)
                okr &= rad_eq(A, Rk)
                if M.dim <= 6 and not is_free(M):
                    for M2 in (dual(M), omega_mod(M, 1), omega_inv(M, 1)):
                        ok4 &= rad_eq(support_ideal(M2, basis, S), A)
                dimV = A.dimension() if A != S.ideal(1) else 0
                P = Resolution(M, 9)
                dims = theta_dims(dual(M), basis, 9)
                okc &= list(P.b) == dims
                okc &= growth_from_dims(dims) == dimV
                results[(F, r, lab)] = (A, M)
                n += 1
            check(ok1, 'Proposition 5.7.1: V_E(M) = V_E(k, M) (radicals of '
                  'the annihilators of Ext^*(M, M) = H^*(E, End M) and of '
                  'H^*(E, M)) for the modules of dimension <= 6 among %d '
                  'modules for (Z/2)^%d over %s' % (n, r, F))
            check(okr, 'Theorem 5.8.3 (Avrunin-Scott): V_E(M) = V_E^#(M), '
                  'the rank variety (minors of size dim M / 2 of sum lambda_i '
                  '(g_i - 1)), for %d modules for (Z/2)^%d over %s'
                  % (n, r, F))
            check(ok4, 'Proposition 5.7.3: V_E(M) = V_E(M^*) = V_E(Omega M) '
                  '= V_E(Omega^-1 M) (modules of dimension <= 6 for (Z/2)^%d '
                  'over %s)' % (r, F))
            check(okc, 'Proposition 5.7.2: dim V_E(M) = c_E(M): the ranks '
                  'of the minimal resolution are dim H^n(E, M^*) (n <= 9) and '
                  'grow like n^(dim V - 1) (finite differences of the last '
                  'terms; %d modules for (Z/2)^%d over %s)' % (n, r, F))
            # sums, tensor products, Ext vanishing, restriction
            labs = [l for l in mods if mods[l].dim <= 4]
            oks = okt = oke = True
            npair = 0
            for l1, l2 in itertools.combinations(labs, 2):
                M1, M2 = mods[l1], mods[l2]
                A1, A2 = results[(F, r, l1)][0], results[(F, r, l2)][0]
                Asum = support_ideal(direct_sum(M1, M2), basis, S)
                oks &= rad_eq(Asum, A1.intersection(A2))
                At = support_ideal(tensor(M1, M2), basis, S)
                okt &= rad_eq(At, A1 + A2)
                if (A1 + A2).radical() == S.ideal(S.gens()):
                    ext = theta_dims(tensor(dual(M1), M2), basis, 4)
                    oke &= all(x == 0 for x in ext[1:])
                    npair += 1
                if npair > 6 and r == 3:
                    break
            check(oks and okt, 'Proposition 5.7.5 and Theorem 5.7.11: '
                  'V(M_1 + M_2) = V(M_1) u V(M_2), V(M_1 (x) M_2) = V(M_1) n '
                  'V(M_2) (pairs of modules of dimension <= 4 for (Z/2)^%d '
                  'over %s)' % (r, F))
            check(oke and npair > 0, 'Corollary 5.7.12: V(M_1) n V(M_2) = '
                  '{0} implies Ext^n(M_1, M_2) = 0 for 1 <= n <= 4 (%d pairs, '
                  '(Z/2)^%d over %s)' % (npair, r, F))
            # Proposition 5.7.7 and Corollary 5.7.9 for subgroups E' < E
            ok7 = True
            for sub in ([basis[0]], [basis[0], basis[1]]) if r == 3 else \
                    ([basis[0]], [basis[1]], [G.mul[basis[0]][basis[1]]]):
                Hset = G.closure(sub)
                Hsub, incl = G.subgroup(Hset, 'E\'')
                ixs = {g: i for i, g in enumerate(incl)}
                hb = [ixs[g] for g in sub]
                S2 = PolynomialRing(F, len(sub), 's')
                # res: x_i |-> sum_j x_i(h_j) s_j, h_j in sub
                coords = elem_coords(G, basis)
                imgs = [sum(coords[h][i] * S2.gen(j) for j, h in
                            enumerate(sub)) for i in range(r)]
                for lab in labs:
                    M = mods[lab]
                    A = results[(F, r, lab)][0]
                    Ares = S2.ideal([f(*imgs) for f in A.gens()])
                    Ah = support_ideal(restrict(M, Hsub, incl), hb, S2)
                    ok7 &= rad_eq(Ares, Ah)
            check(ok7, 'Proposition 5.7.7 and Corollary 5.7.9: V_E\'(M) = '
                  'V_E\' n V_E(M) = (res^*)^-1 V_E(M) for the subgroups E\' '
                  'of rank %s of (Z/2)^%d (modules of dimension <= 4 over %s)'
                  % ('1, 2' if r == 3 else '1', r, F))
            # proof of Theorem 5.8.3: replacing E by a shifted subgroup E' of
            # maximal rank (k E = k E') changes V_E(M) by the linear map
            # lambda of the shift
            if F is F4:
                okS = True
                for _ in range(3):
                    while True:
                        Lm = _matrix(F, r, r, [F.random_element()
                                               for _ in range(r * r)])
                        if Lm.det() != 0:
                            break
                    for lab in labs:
                        M = mods[lab]
                        Xs = [sum(Lm[i, j] * M.X(basis[j]) for j in range(r))
                              for i in range(r)]
                        Th2 = _matrix(S, M.dim, M.dim)
                        for i in range(r):
                            Th2 += S.gen(i) * Xs[i].change_ring(S)
                        K = SYZ(Th2)
                        if not K:
                            A2 = S.ideal(1)
                        elif Th2.is_zero():
                            A2 = S.ideal(0)
                        else:
                            Km = _matrix(S, [list(v) for v in K]).transpose()
                            A2 = S.ideal(list(QUOTIENT(Th2, Km)))
                        # a point lambda' for E' is lambda = lambda' L
                        sub_ = [sum(S.gen(i) * Lm[i, j] for i in range(r))
                                for j in range(r)]
                        A = results[(F, r, lab)][0]
                        okS &= rad_eq(S.ideal([f(*sub_) for f in A.gens()]),
                                      A2)
                check(okS, 'proof of Theorem 5.8.3: for a shifted subgroup '
                      'E\' = <1 + v_i> of maximal rank (v_i = sum lambda_ij '
                      '(g_j - 1), three random lambda over GF(4)) the variety '
                      'of M as a k E\'-module is V_E(M) in the coordinates '
                      'of E\' (modules of dimension <= 4 for (Z/2)^2)')
    return results


class TensorRes:
    """The tensor product of the periodic resolutions of F over F[Z/p] for
    E = <g_1, ..., g_r> elementary abelian (a minimal resolution): basis
    e_a, |a| = n, d e_a = sum_i (-1)^(a_1 + ... + a_(i-1)) N_i(a_i)
    e_(a - eps_i) with N_i(m) = g_i - 1 for m odd and (g_i - 1)^(p-1) = 1 +
    g_i + ... + g_i^(p-1) for m even.  The dual basis of e_a is x^eps y^b
    (a = 2b + eps) up to sign; for p = 2 it is t^a."""

    def __init__(self, F, G, basis, nmax):
        p = F.characteristic()
        self.F, self.G, self.basis, self.p = F, G, basis, p
        r = len(basis)
        self.r = r
        self.mons = {k: [a for a in itertools.product(range(k + 1),
                                                     repeat=r)
                         if sum(a) == k] for k in range(nmax + 1)}
        self.ix = {k: {a: i for i, a in enumerate(self.mons[k])}
                   for k in self.mons}
        self.b = [len(self.mons[k]) for k in range(nmax + 1)]
        n = G.n
        self.eps = mat(F, 1, n, {(0, t): 1 for t in range(n)})
        pw = {}
        for i, g in enumerate(basis):
            x, lst = G.e, []
            for _ in range(p):
                lst.append(x)
                x = G.mul[x][g]
            pw[i] = lst
        self.d = {}
        for k in range(1, nmax + 1):
            ent = {}
            for c, a in enumerate(self.mons[k]):
                for i in range(r):
                    if a[i] == 0:
                        continue
                    sign = (-1) ** sum(a[:i])
                    a2 = tuple(a[j] - (1 if j == i else 0) for j in range(r))
                    j = self.ix[k - 1][a2]
                    if a[i] % 2 == 1:
                        elt = [(basis[i], 1), (G.e, -1)]
                    else:
                        elt = [(h, 1) for h in pw[i]]
                    for g in range(n):
                        for h, s in elt:
                            key = (j * n + G.mul[g][h], c * n + g)
                            ent[key] = ent.get(key, 0) + sign * s
            self.d[k] = mat(F, self.b[k - 1] * n, self.b[k] * n,
                            {kk: F(v) for kk, v in ent.items() if F(v)})
        for k in range(2, nmax + 1):
            assert (self.d[k - 1] * self.d[k]).is_zero()
            assert rk(self.d[k]) == self.d[k - 1].ncols() - rk(self.d[k - 1])
        assert rk(self.d[1]) == n - 1

    def dim(self, k):
        return self.b[k] * self.G.n

    def gen_cols(self, k):
        n, e = self.G.n, self.G.e
        return self.d[k].matrix_from_columns([i * n + e
                                              for i in range(self.b[k])])

    def l_zeta(self, zeta, k):
        """L_zeta = Ker(Omega^k F -> F) for the cochain zeta on Q_k (values
        on the e_a): the image under d_k of the kernel of zeta."""
        F, G = self.F, self.G
        row = mat(F, 1, self.dim(k), {(0, j * G.n + t): zeta[j]
                                      for j in range(self.b[k])
                                      for t in range(G.n) if zeta[j]})
        K = kernel_cols(row)
        L = colbasis(self.d[k] * K)
        act = {g: L.solve_right(act_free(G, self.b[k - 1], g, L))
               for g in range(G.n)}
        return Mod(F, G, L.ncols(), act)

    def shifted_restriction(self, lam, kmax):
        """res to the cyclic shifted subgroup <1 + v>, v = sum lam_i (g_i -
        1): f_k(1) in Q_k with d f_k(1) = w_k f_(k-1)(1), w = v (k odd),
        v^(p-1) (k even); returns the values of the dual basis cochains."""
        F, G, p = self.F, self.G, self.p
        n = G.n

        def times_v(b, X, power):
            for _ in range(power):
                Y = mat(F, X.nrows(), X.ncols())
                for i, g in enumerate(self.basis):
                    if lam[i]:
                        Y += lam[i] * (act_free(G, b, g, X) - X)
                X = Y
            return X
        f = mat(F, n, 1, {(G.e, 0): 1})
        out = {}
        for k in range(1, kmax + 1):
            tgt = times_v(self.b[k - 1], f, 1 if k % 2 else p - 1)
            f = self.d[k].solve_right(tgt)
            out[k] = collapse(F, G, f, self.b[k]).column(0)
        return out


def section_5_8():
    """Section 5.8: shifted subgroups, Lemma 5.8.2 and the Remark (the
    Frobenius twist for p odd), the Bockstein computation pp. 182-183 with
    the corrected bracket, the rank criterion, Carlson's examples, the
    period-one module, Theorem 5.8.3 for (Z/3)^2, Dade's lemma, Corollary
    5.8.5, Theorem 5.1.1 (vii), (viii)."""
    rnd = random.Random(58)
    # shifted subgroups (pp. 180-181)
    for p, r, q in ((2, 2, 4), (2, 3, 4), (3, 2, 9), (5, 2, 5)):
        Fq = GF(q, 'a')
        Fp = GF(p)
        G = elem_group(p, r)
        basis = G.gens
        reg = regular_module(Fq, G)
        Xs = [reg.X(g) for g in basis]
        ok = True
        for _ in range(4):
            while True:
                Lm = _matrix(Fq, r, r, [Fq.random_element()
                                        for _ in range(r * r)],
                             sparse=_sp(Fq))
                if rk(Lm) == r:
                    break
            V = [sum(Lm[i, j] * Xs[j] for j in range(r)) for i in range(r)]
            U = [ident(Fq, G.n) + v for v in V]
            ok &= all(u ** p == 1 for u in U)
            ok &= all(U[i] * U[j] == U[j] * U[i] for i in range(r)
                      for j in range(r))
            # the group generated has order p^r and exponent p: not cyclic
            elts = set()
            for a in itertools.product(range(p), repeat=r):
                Mx = prod_(U[i] ** a[i] for i in range(r))
                Mx.set_immutable()
                elts.add(Mx)
            ok &= len(elts) == p ** r
            # the automorphism X_i |-> sum lambda_ij X_j and its inverse mu
            Mu = Lm.solve_right(ident(Fq, r))
            back = [sum(Mu[i, j] * V[j] for j in range(r)) for i in range(r)]
            ok &= all(back[i] == Xs[i] for i in range(r))
            # k E free over k E' for E' = <1 + v_1, ..., 1 + v_s>
            for s in range(1, r + 1):
                JE = hcat(Fq, G.n, [V[i] for i in range(s)])
                ok &= G.n - rk(JE) == p ** (r - s)
        check(ok, 'pp. 180-181: for 4 random non-singular (lambda_ij) over '
              'GF(%d) (E = (Z/%d)^%d) the 1 + v_i commute, have order p and '
              'generate a subgroup of order p^r and exponent p (a maximal '
              'shifted subgroup is not cyclic for r > 1); g_i |-> 1 + sum '
              'lambda_ij (g_j - 1) is inverted by (mu_ij) = (lambda_ij)^-1; '
              'k E is free of rank p^(r-s) over k <1 + v_1, ..., 1 + v_s>'
              % (q, p, r))
    # the inclusion k E' -> k E is not a map of Hopf algebras
    G = elem_group(2, 2)
    g1, g2 = G.gens
    v = {g1: 1, g2: 1, G.e: 0}      # v = (g1 - 1) + (g2 - 1)
    u = {g1: 1, g2: 1, G.e: 1}      # 1 + v = g1 + g2 - 1 (char 2)
    # Delta(u) = g1 (x) g1 + g2 (x) g2 + 1 (x) 1 vs u (x) u
    lhs = {(g1, g1): 1, (g2, g2): 1, (G.e, G.e): 1}
    rhs = {}
    for a, x in u.items():
        for b, y in u.items():
            if x * y % 2:
                rhs[(a, b)] = 1
    refuted(lhs == rhs, 'p. 181: Delta(1 + v) = (1 + v) (x) (1 + v) for the '
            'shifted element 1 + v = g_1 + g_2 - 1 of k V_4 (it is not '
            'group-like, so k E\' -> k E is not a Hopf algebra map)')
    # Lemma 5.8.2 and the Remark: restriction to cyclic shifted subgroups
    for p, q, r, cnt in ((2, 4, 2, None), (3, 9, 2, None), (3, 9, 3, 25),
                         (5, 25, 2, 30)):
        Fq = GF(q, 'a')
        G = elem_group(p, r)
        Q = TensorRes(Fq, G, G.gens, 2)
        lams = [l for l in itertools.product(list(Fq), repeat=r) if any(l)]
        if cnt:
            rnd.shuffle(lams)
            lams = lams[:cnt]
        ok, lin = True, True
        for lam in lams:
            res = Q.shifted_restriction(lam, 2)
            ok &= all(res[1][Q.ix[1][tuple(1 if j == i else 0
                                          for j in range(r))]] == lam[i]
                      for i in range(r))
            ok &= all(res[2][Q.ix[2][tuple(2 if j == i else 0
                                          for j in range(r))]] ==
                      lam[i] ** p for i in range(r))
            ys = [res[2][Q.ix[2][tuple(2 if j == i else 0 for j in range(r))]]
                  for i in range(r)]
            lin &= rk(mrows(Fq, [ys, list(lam)])) <= 1
        check(ok, 'Lemma 5.8.2 and the Remark, p. 181: for every cyclic '
              'shifted subgroup <1 + v>, v = sum lambda_i (g_i - 1) (%s '
              'lambda in GF(%d)^%d), res(x_i) = lambda_i and res(beta x_i) = '
              'lambda_i^p (%s)' % ('all' if not cnt else '%d random' % cnt, q,
                                    r, 'p = 2: beta x_i = x_i^2' if p == 2
                                    else 'semilinear via the Frobenius'))
        if p != 2:
            refuted(lin, 'Remark p. 181 (a linear identification for p odd): '
                    'the restriction of (beta x_1, ..., beta x_r) to <1 + v> '
                    'is proportional to lambda; fails for lambda not '
                    'proportional to an F_p-rational vector (GF(%d), r = %d)'
                    % (q, r))
    # pp. 182-183: Omega^2 k, the Bockstein formula and the bracket
    for p, r in ((3, 2), (3, 3), (5, 2)):
        Fp = GF(p)
        G = elem_group(p, r)
        Q = TensorRes(Fp, G, G.gens, 2)
        n = G.n
        basis = G.gens
        Lr = PolynomialRing(Fp, r, 'l')
        lam = Lr.gens()
        Om = colbasis(Q.d[2])                    # Omega^2 k in P_1
        JOm = colbasis(hcat(Fp, Om.nrows(), [act_free(G, r, g, Om) - Om
                                              for g in basis]))
        # generators b_i, c_ij (p. 182) and Omega^2 k = Ker delta
        def gamma(i, coeffs):
            return {(i, g): c for g, c in coeffs.items()}
        pw = {}
        for i, g in enumerate(basis):
            x, lst = G.e, []
            for _ in range(p):
                lst.append(x)
                x = G.mul[x][g]
            pw[i] = lst

        gix = {Q.ix[1][tuple(1 if j == i else 0 for j in range(r))]: i
               for i in range(r)}      # position of gamma_i in P_1

        def vec_of(el):
            """P_1 element {(i, g): c} with F_p coefficients -> column."""
            return col_vec(Fp, [el.get((gix[q], g), 0) for q in range(r)
                                for g in range(n)])
        bs = [{(i, h): 1 for h in pw[i]} for i in range(r)]
        cs = []
        for i in range(r):
            for j in range(i + 1, r):
                cs.append({(j, basis[i]): 1, (j, G.e): -1, (i, basis[j]): -1,
                           (i, G.e): 1})
        gens_cols = hcat(Fp, r * n, [vec_of(b) for b in bs] +
                         [vec_of({k: Fp(v) for k, v in c.items()})
                          for c in cs])
        sub = colbasis(hcat(Fp, r * n, [act_free(G, r, g, gens_cols)
                                         for g in range(n)]))
        ok = sub.ncols() == Om.ncols() and in_span(Om, sub)
        # delta : P_1 -> P_0, gamma_i |-> g_i - 1
        delta = Q.d[1]
        ok &= Om.ncols() == r * n - rk(delta)
        check(ok, 'p. 182: Omega^2 k = Ker(delta : P_1 -> P_0) is generated '
              'by b_i = (g_i - 1)^(p-1) gamma_i and c_ij = (g_i - 1) gamma_j '
              '- (g_j - 1) gamma_i (E = (Z/%d)^%d)' % (p, r))

        # symbolic computations in P_1 (x) F_p[lambda]
        def pmul_v(el, coeffs):
            """(sum coeffs_i (g_i - 1)) . el for el in P_1 (x) F_p[l]."""
            out = {}
            for (i, g), c in el.items():
                for k, a in enumerate(coeffs):
                    if a == 0:
                        continue
                    for h, s in ((G.mul[basis[k]][g], 1), (g, -1)):
                        out[(i, h)] = out.get((i, h), 0) + s * a * c
            return {k: v for k, v in out.items() if v != 0}

        def in_sub(el, Sub):
            """Every lambda-monomial coefficient of el lies in Sub."""
            mons = set()
            for c in el.values():
                mons |= set(Lr(c).monomials())
            for m in mons:
                vv = col_vec(Fp, [Lr(el.get((gix[q], g), 0)
                                     ).monomial_coefficient(m)
                                  for q in range(r) for g in range(n)])
                if not in_span(Sub, vv):
                    return False
            return True

        def addp(*els):
            out = {}
            for s, el in els:
                for k, v in el.items():
                    out[k] = out.get(k, 0) + s * v
            return {k: v for k, v in out.items() if v != 0}
        Gam = {(i, G.e): lam[i] for i in range(r)}
        W = Gam
        for _ in range(p - 1):
            W = pmul_v(W, lam)
        Bsum = {}
        for i in range(r):
            for h in pw[i]:
                Bsum[(i, h)] = lam[i] ** p
        diff = addp((1, W), (-1, Bsum))
        check(in_sub(W, Om) and in_sub(diff, JOm),
              'pp. 182-183: [sum lambda_i (g_i - 1)]^(p-1) [sum lambda_i '
              'gamma_i] lies in Omega^2 k and is congruent to sum lambda_i^p '
              'b_i modulo Rad(Omega^2 k), identically in lambda (E = '
              '(Z/%d)^%d)' % (p, r))
        # the induction step: A = sum_(i<r) lambda_i (g_i - 1), B =
        # lambda_r (g_r - 1), Gamma_A, Gamma_B
        cA = [lam[i] if i < r - 1 else 0 for i in range(r)]
        cB = [0] * (r - 1) + [lam[r - 1]]
        GA = {(i, G.e): lam[i] for i in range(r - 1)}
        GB = {(r - 1, G.e): lam[r - 1]}

        def AjBk(el, j, k):
            for _ in range(j):
                el = pmul_v(el, cA)
            for _ in range(k):
                el = pmul_v(el, cB)
            return el
        first = [AjBk(GA, j, p - 1 - j) for j in range(p - 1)]
        second = [AjBk(GB, j, p - 1 - j) for j in range(p)]
        total = addp(*([((-1) ** j, f) for j, f in enumerate(first)] +
                       [((-1) ** j, f) for j, f in enumerate(second)]))
        lhs = addp((1, W), (-1, AjBk(GA, p - 1, 0)))
        ok = lhs == total
        ok &= all(binomial(p - 1, j) % p == (-1) ** j % p for j in range(p))
        # the corrected bracket identity and its membership in Omega^2 k
        brk_l = addp((1, pmul_v(GA, cB)), (-1, pmul_v(GB, cA)))
        brk_r = {}
        for i in range(r - 1):
            # lambda_i lambda_r [(g_r - 1) gamma_i - (g_i - 1) gamma_r]
            e1 = pmul_v({(i, G.e): lam[i] * lam[r - 1]},
                        [0] * (r - 1) + [1])
            e2 = pmul_v({(r - 1, G.e): lam[i] * lam[r - 1]},
                        [1 if k == i else 0 for k in range(r)])
            brk_r = addp((1, brk_r), (1, e1), (-1, e2))
        ok &= brk_l == brk_r and in_sub(brk_l, Om)
        # cancellation of term j of the first sum with term j + 1 of the
        # second modulo Rad(Omega^2 k)
        for j in range(p - 1):
            ok &= in_sub(addp(((-1) ** j, first[j]),
                              ((-1) ** (j + 1), second[j + 1])), JOm)
        check(ok, 'p. 183 (corrected): the expansion into the two sums, '
              'binom(p - 1, j) = (-1)^j mod p, lambda_r (g_r - 1)(sum '
              'lambda_i gamma_i) - (sum lambda_i (g_i - 1)) lambda_r gamma_r '
              '= sum lambda_i lambda_r [(g_r - 1) gamma_i - (g_i - 1) '
              'gamma_r] '
              'in Omega^2 k, and the cancellation of the j-th and (j+1)-st '
              'terms modulo Rad(Omega^2 k) (E = (Z/%d)^%d)' % (p, r))
        # the printed bracket [(lambda_r - 1) gamma_i - (lambda_i - 1)
        # gamma_r] is not even in Ker(delta)
        i = 0
        pr = {(i, G.e): lam[r - 1] - 1, (r - 1, G.e): -(lam[i] - 1)}
        img = {}
        for (k, g), c in pr.items():
            for h, s in ((G.mul[basis[k]][g], 1), (g, -1)):
                img[h] = img.get(h, 0) + s * c
        refuted(all(v == 0 for v in img.values()),
                'p. 183 (printed): the bracket [(lambda_r - 1) gamma_i - '
                '(lambda_i - 1) gamma_r] lies in Omega^2 k; its image under '
                'delta is (lambda_r - 1)(g_i - 1) - (lambda_i - 1)(g_r - 1) '
                '!= 0 (E = (Z/%d)^%d)' % (p, r))
    # p. 183: the rank criterion by Jordan canonical form (cyclic groups)
    for p in (2, 3, 5):
        Fp = GF(p)
        ok = True
        for _ in range(12):
            sizes = [rnd.randint(1, p) for _ in range(rnd.randint(1, 4))]
            m = sum(sizes)
            J = block_diag(Fp, [jordan_nil(Fp, s) for s in sizes])
            rkv = rk(J)
            free = all(s == p for s in sizes)
            ok &= rkv * p <= (p - 1) * m and ((rkv * p == (p - 1) * m) == free)
        check(ok, 'p. 183: the rank of v on M is at most (p - 1) dim M / p, '
              'with equality iff M restricted to <1 + v> is free (12 random '
              'modules for Z/%d)' % p)


def section_5_8_examples():
    """Carlson's examples pp. 183-185, the period-one module, Dade's lemma,
    Corollary 5.8.5, Theorem 5.8.3 for (Z/3)^2 with the Frobenius twist,
    Theorem 5.1.1 (vii), (viii)."""
    rnd = random.Random(585)
    F2, F4 = GF(2), GF(4, 'w')
    om = F4.gen()
    # Carlson's favourite example, symbolically in a, b, c, lambda
    Rs = PolynomialRing(F2, 'a,b,c,l1,l2,l3')
    a, b, c, l1, l2, l3 = Rs.gens()
    g1 = _matrix(Rs, [[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1]])
    g2 = _matrix(Rs, [[1, 0, 0, 0], [0, 1, 0, 0], [a, 0, 1, 0], [0, b, 0, 1]])
    g3 = _matrix(Rs, [[1, 0, 0, 0], [0, 1, 0, 0], [0, c, 1, 0], [1, 0, 0, 1]])
    I4 = _matrix(Rs, 4, 4, 1)
    ok = all(g * g == I4 for g in (g1, g2, g3)) and \
        g1 * g2 == g2 * g1 and g1 * g3 == g3 * g1 and g2 * g3 == g3 * g2
    v = l1 * (g1 - I4) + l2 * (g2 - I4) + l3 * (g3 - I4)
    printed = _matrix(Rs, [[0, 0, 0, 0], [0, 0, 0, 0],
                           [l1 + l2 * a, l3 * c, 0, 0],
                           [l3, l1 + l2 * b, 0, 0]])
    det = v.submatrix(2, 0, 2, 2).det()
    ok &= v == printed and v.rank() <= 2
    ok &= det == (l1 + a * l2) * (l1 + b * l2) - c * l3 ** 2
    check(ok, 'Example p. 184 (Carlson): the matrices define a k E-module '
          'M_(a,b,c) for all a, b, c; v = sum lambda_i (g_i - 1) is the '
          'printed matrix; it has rank 2 iff (lambda_1 + a lambda_2)(lambda_1 '
          '+ b lambda_2) != c lambda_3^2')
    G = elem_group(2, 3)
    S = PolynomialRing(F4, 3, 'x')
    x = S.gens()
    ok = True
    for _ in range(6):
        aa, bb, cc = [F4.random_element() for _ in range(3)]
        M = carlson_module(F4, G, aa, bb, cc)
        quad = (x[0] + aa * x[1]) * (x[0] + bb * x[1]) + cc * x[2] ** 2
        ok &= rad_eq(support_ideal(M, G.gens, S), S.ideal(quad)) and \
            rad_eq(rank_ideal(M, G.gens, S), S.ideal(quad))
    check(ok, 'Example p. 184 and Theorem 5.8.3: V_E(M_(a,b,c)) = V_E^#(M_(a,'
          'b,c)) is the quadric (X_1 + a X_2)(X_1 + b X_2) = c X_3^2 (6 '
          'random '
          '(a, b, c) in GF(4)^3; all of F_2^3 in the general checks)')
    # Example p. 184 (Carlson): Klein four, M = V_(1, alpha), zeta_alpha,
    # E_alpha
    F16 = GF(16, 'b')
    V4 = elem_group(2, 2)
    X1, X2 = V4.gens
    nonzero = []
    for alpha in list(F16) + ['inf']:
        if alpha == 'inf':
            M = v_module(F16, V4, 1, mat(F16, 1, 1), inf=True)
            zeta = (F16(0), F16(1))           # vanishes on (1, 0)
            lam = (F16(1), F16(0))
        else:
            M = v_module(F16, V4, 1, alpha * ident(F16, 1))
            zeta = (F16(1), alpha)            # zeta(X) = 1, zeta(Y) = alpha
            lam = (alpha, F16(1))             # E_alpha = <1 + alpha X + Y>
        U = Mod.from_gens(F16, V4, [mat(F16, 2, 2, {(0, 0): 1, (1, 1): 1,
                                                     (0, 1): zeta[0]}),
                                    mat(F16, 2, 2, {(0, 0): 1, (1, 1): 1,
                                                     (0, 1): zeta[1]})])

        def v_on(N):
            return lam[0] * N.X(X1) + lam[1] * N.X(X2)
        assert v_on(M).is_zero()          # M restricted to E_alpha trivial
        res_zeta_zero = v_on(U).is_zero()
        UM = tensor(U, M)
        res_tensor_nonzero = not v_on(UM).is_zero()
        ok_a = res_zeta_zero
        nonzero.append((alpha, res_tensor_nonzero, ok_a))
    check(all(z for _, _, z in nonzero) and
          all(nz == (al not in (F16(0), F16(1), 'inf'))
              for al, nz, _ in nonzero),
          'Example p. 184 (Carlson): for M = V_(1, alpha) over GF(16), '
          'res_(E, E_alpha)(zeta_alpha) = 0 always, while res_(E, '
          'E_alpha)(zeta_alpha (x) Id_M) != 0 exactly for alpha not in {0, 1, '
          'infinity} (all 17 alpha)')
    # the period-one module, p. 185
    G = elem_group(2, 3)
    M = period_one_module(F2, G)
    fix = fixed_points(M)
    Nrm = prod_(M.X(g) for g in G.gens)
    e4 = col_vec(F2, [0, 0, 0, 1])
    ok = isomorphic(omega_mod(M, 1), M)
    ok &= theta_dims(M, G.gens, 8) == [1] * 9
    ok &= fix.ncols() == 1 and in_span(fix, e4)
    ok &= Nrm.is_zero()
    check(ok, 'Example p. 185: M is periodic of period one (Omega M = M), '
          'Ext^n(k, M) = H^n(E, M) is one dimensional (n <= 8), Hom(k, M) = '
          '<e_4>, and zeta : 1 |-> e_4 does not factor through a projective '
          '(the norm element of k E kills M, so e_4 is not in N . M)')
    ok = True
    for q in (2, 4, 8, 16):
        Fq = GF(q, 'a')
        Mq = period_one_module(Fq, G)
        e4q = col_vec(Fq, [0, 0, 0, 1])
        for lam in itertools.product(list(Fq), repeat=3):
            if not any(lam):
                continue
            vM = sum(l * Mq.X(g) for l, g in zip(lam, G.gens))
            ok &= in_span(vM, e4q)
    check(ok, 'Example p. 185: the restriction of zeta to every cyclic '
          'shifted subgroup <1 + v> factors through a projective (e_4 in v M; '
          'all lambda != 0 in GF(q)^3, q <= 16)')
    S2 = PolynomialRing(F2, 3, 'x')
    check(rad_eq(support_ideal(M, G.gens, S2), S2.ideal(S2.gen(0),
                                                        S2.gen(1))),
          'Example p. 185: V_E(M) = V_E^#(M) is the line lambda_1 = '
          'lambda_2 = 0 (complexity one)')
    # Dade's lemma (Corollary 5.8.4) over the algebraic closure, and why
    # F_q-rational cyclic shifted subgroups do not suffice
    for p, r, F in ((2, 2, F2), (2, 2, F4), (2, 3, F2), (3, 2, GF(3))):
        G = elem_group(p, r)
        S = PolynomialRing(F, r, 'x')
        reg = regular_module(F, G)
        tot, ok, nfree = 0, True, 0
        pool = [M for M in test_modules(G, F) if M.dim <= 9]
        for t in range(30):
            two = direct_sum(reg, reg) if t % 2 else reg
            vs = [vector(F, [F.random_element() if rnd.random() < 0.15 else 0
                             for _ in range(two.dim)])
                  for _ in range(1 + t % 3)]
            Sb = submodule_generated(two, vs)
            if 0 < Sb.ncols() < two.dim:
                pool += [sub_action(two, Sb), quotient_action(two, Sb)]
        if True:
            for M in pool:
                if M.dim > 9:
                    continue
                free = is_free(M)
                nfree += free
                Rk = rank_ideal(M, G.gens, S)
                ok &= free == (Rk.radical() == S.ideal(S.gens()))
                tot += 1
        check(ok and tot > 10, 'Corollary 5.8.4 (Dade): M is free iff its '
              'restriction to every cyclic shifted subgroup over the '
              'algebraic closure is free (V^#(M) = {0}) (%d random sub- and '
              'quotient modules of k E or k E^2, %d free; E = (Z/%d)^%d over '
              '%s)' % (tot, nfree, p, r, F))
    V4 = elem_group(2, 2)
    comp = mat(F2, 2, 2, {(1, 0): 1, (0, 1): 1, (1, 1): 1})
    M = v_module(F2, V4, 2, comp)       # V_(2, w) defined over F_2
    X1, X2 = V4.gens
    rational_free = all(rk(l1_ * M.X(X1) + l2_ * M.X(X2)) == 2
                        for l1_, l2_ in ((1, 0), (0, 1), (1, 1)))
    M4 = v_module(F4, V4, 2, mat(F4, 2, 2, {(1, 0): 1, (0, 1): 1,
                                            (1, 1): 1}))
    shifted = [rk(l1_ * M4.X(X1) + l2_ * M4.X(X2))
               for l1_, l2_ in ((om, 1), (om + 1, 1))]
    check(rational_free and not is_free(M) and min(shifted) < 2,
          'Corollary 5.8.4 needs the shifted subgroups over the algebraic '
          'closure: V_(2, w) (realised over F_2 by the companion matrix of '
          'x^2 + x + 1) is free on <g_1>, <g_2>, <g_1 g_2> and on the three '
          'F_2-rational cyclic shifted subgroups, not free, and not free on '
          '<1 + w X + Y> over GF(4)')
    # Corollary 5.8.5 and the argument by Theorem 3.1.9 of Volume I
    ok, n = True, 0
    for p, r, F in ((2, 2, F2), (2, 3, F2), (3, 2, GF(3))):
        G = elem_group(p, r)
        S = PolynomialRing(F, r, 'x')
        mods = [omega_mod(trivial(F, G), 1), omega_mod(trivial(F, G), 2),
                perm_module(F, G, G.closure([G.gens[0]]))]
        mods += [M for M in test_modules(G, F) if M.dim <= 12]
        for M in mods:
            if M.dim % p == 0:
                continue
            Iv = support_ideal(M, G.gens, S)
            ok &= Iv.radical() == S.ideal(0)
            E = end_module(M)
            idv = vector(F, [1 if j % (M.dim + 1) == 0 else 0
                             for j in range(E.dim)])
            tr = vector(F, [1 if j % (M.dim + 1) == 0 else 0
                            for j in range(E.dim)])
            ok &= all(E.act[g] * idv == idv for g in range(G.n))
            ok &= all(tr * E.act[g] == tr for g in range(G.n))
            ok &= tr * idv == M.dim % p and tr * idv != 0
            n += 1
    check(ok, 'Corollary 5.8.5: if p does not divide dim M then V_G(M) = '
          'V_G (the annihilator of H^*(E, M) is nilpotent), and k -> End(M) '
          '-> k (identity, trace) is multiplication by dim M != 0, so k is a '
          'summand of M (x) M^* (Theorem 3.1.9 of Volume I) (%d modules for '
          '(Z/2)^2, (Z/2)^3, (Z/3)^2)' % n)
    # Theorem 5.8.3 for p = 3 with the Frobenius twist (E = (Z/3)^2)
    for q in (3, 9):
        Fq = GF(q, 'a')
        G = elem_group(3, 2)
        S = PolynomialRing(Fq, 2, 'y')
        mods = {'k': trivial(Fq, G), 'Omega k': omega_mod(trivial(Fq, G), 1),
                'Omega^-1 k': omega_inv(trivial(Fq, G), 1)}
        reg = regular_module(Fq, G)
        X1, X2 = G.gens
        for alpha in (list(Fq) if q == 3 else
                      [Fq.gen(), Fq.gen() + 1, Fq.gen() ** 2 + 2]):
            vX = reg.X(X1) + alpha * reg.X(X2)
            Sb = colbasis(vX)
            mods['k E / v_%s' % alpha] = quotient_action(reg, Sb)
        mods['k[E/<g_1>]'] = perm_module(Fq, G, G.closure([X1]))
        ok_tw, ok_lin = True, True
        for lab, M in mods.items():
            A = support_ideal(M, G.gens, S)
            ok_tw &= rad_eq(A, rank_ideal(M, G.gens, S, twist=True))
            ok_lin &= rad_eq(A, rank_ideal(M, G.gens, S, twist=False))
        check(ok_tw, 'Theorem 5.8.3 with the Remark p. 181 (p = 3, E = '
              '(Z/3)^2 over GF(%d), %d modules incl. k E / (g_1 - 1 + alpha '
              '(g_2 - 1)) k E): V_E(M) (annihilator of H^*(E, M) in k[beta '
              'x_1, beta x_2]) is the image of V_E^#(M) under lambda |-> '
              'lambda^3' % (q, len(mods)))
        if q == 9:
            refuted(ok_lin, 'Theorem 5.8.3 with a linear identification for '
                    'p = 3 (no Frobenius twist): fails for k E / (g_1 - 1 + '
                    'alpha (g_2 - 1)) with alpha in GF(9) minus GF(3)')
    # Theorem 5.1.1 (vii): V_G(L_zeta) = V_G<zeta>
    for p, r, F in ((2, 2, F2), (2, 2, F4), (2, 3, F2), (3, 2, GF(3)),
                    (3, 2, GF(9, 'a'))):
        G = elem_group(p, r)
        Q = TensorRes(F, G, G.gens, 4 if p == 2 else 4)
        S = PolynomialRing(F, r, 'x' if p == 2 else 'y')
        ok, n = True, 0
        if p == 2:
            degs = (1, 2, 3) if r == 2 else (1, 2)
        else:
            degs = (2, 4)
        for d in degs:
            for _ in range(3 if r == 2 else 2):
                # a random cochain on Q_d and its polynomial
                zeta = [F.random_element() for _ in range(Q.b[d])]
                if not any(zeta):
                    continue
                if p == 2:
                    f = sum(z * prod_(S.gen(i) ** a[i] for i in range(r))
                            for z, a in zip(zeta, Q.mons[d]))
                else:
                    # only the y-monomials (a even) survive modulo
                    # nilpotents: x^eps y^b with eps = 0
                    f = sum(z * prod_(S.gen(i) ** (a[i] // 2)
                                      for i in range(r))
                            for z, a in zip(zeta, Q.mons[d])
                            if all(ai % 2 == 0 for ai in a))
                L = Q.l_zeta(zeta, d)
                Iv = support_ideal(L, G.gens, S)
                ok &= rad_eq(Iv, S.ideal(f))
                n += 1
        check(ok, 'Theorem 5.1.1 (vii): V(L_zeta) = V<zeta> for %d random '
              'zeta of degrees %s in H^*(E) (E = (Z/%d)^%d over %s; for p = '
              '3 the hypersurface of the image of zeta modulo nilpotents in '
              'k[beta x_1, beta x_2])' % (n, list(degs), p, r, F))
    # Theorem 5.1.1 (viii): V(L_(x_1 x_2)) = two lines meeting in 0 for V_4
    V4 = elem_group(2, 2)
    for F in (F2, F4):
        Q = TensorRes(F, V4, V4.gens, 2)
        S = PolynomialRing(F, 2, 'x')
        x1, x2 = S.gens()
        # x_1 x_2 = dual of e_(1,1)
        zeta = [1 if a == (1, 1) else 0 for a in Q.mons[2]]
        L = Q.l_zeta(zeta, 2)
        dec = MTX_DECOMP(gap_module(L))
        parts = [gap_to_mod(F, V4, pr[1]) for pr in dec]
        vs = sorted(str(support_ideal(Pm, V4.gens, S).radical().gens())
                    for Pm in parts)
        check(len(parts) == 2 and
              sorted(str(S.ideal(x).radical().gens()) for x in (x1, x2)) ==
              vs, 'Theorem 5.1.1 (viii): V(L_(x_1 x_2)) = {x_1 = 0} u {x_2 = '
              '0} with intersection {0}, and L_(x_1 x_2) = M_1 + M_2 with '
              'V(M_1), '
              'V(M_2) the two lines (over %s)' % F)
        zeta = [1 for a in Q.mons[2]]          # x_1^2 + x_1 x_2 + x_2^2
        L = Q.l_zeta(zeta, 2)
        dec = MTX_DECOMP(gap_module(L))
        check(len(dec) == (1 if F is F2 else 2),
              'Theorem 5.1.1 (viii) over %s: L_zeta for zeta = x_1^2 + x_1 '
              'x_2 + x_2^2 (two lines conjugate over GF(4)) has %d summand(s)'
              % (F, 1 if F is F2 else 2))


def ff_conv(F, x):
    """An element of a finite field of GAP's (Conway) form as an element
    of F (same order, Conway modulus)."""
    if x.parent().order() == F.characteristic():
        return F(x)
    return x.polynomial()(F.gen())


def section_5_7_groups():
    """Varieties of modules for D8 and Q8 through I_G(M) = Ker(Phi_M)
    (degrees <= 8) and the presentations of H^*(G): Proposition 5.7.4,
    Corollary 5.7.9, Proposition 5.7.2 with Theorem 5.3.7."""
    F = GF(2)
    for name, N, maxdeg in (('D8', 8, 2), ('Q8', 8, 4)):
        C = cohom(name, 2, N)
        G = C.G
        Pres = auto_presentation(C, maxdeg)
        R = Pres.R
        base = Pres.ideal()
        elabs = [E for E in G.elementary_abelian_subgroups(2) if len(E) > 1]
        reps = G.conj_classes_of(elabs)
        maxs = [E for E in reps if not any(set(E) < set(E2) for E2 in elabs)]
        datas = [ElemData(C, E, N) for E in maxs]
        resg = [[D.res(d, v) for d, v in Pres.gens] for D in datas]
        mods = [M for M in test_modules(G, F) if 1 < M.dim <= 8]
        ok5, ok10, ok3, okst = True, True, True, True
        for M in mods:
            polys = {}
            for n in range(1, N + 1):
                K = C.coefficient_kernel(M, n)
                polys[n] = [Pres.coords(n, v) for v in K.columns()]
            IG = base + R.ideal(sum((polys[n] for n in range(1, N + 1)),
                                    []) or [R(0)])
            IG2 = base + R.ideal(sum((polys[n] for n in range(1, N - 1)),
                                     []) or [R(0)])
            radG = IG.radical()
            okst &= radG == IG2.radical()
            inter, dims = None, []
            for D, rg in zip(datas, resg):
                ixs = {g: i for i, g in enumerate(D.incl)}
                IE = support_ideal(restrict(M, D.sub, D.incl),
                                   [ixs[g] for g in D.basis], D.S)
                radE = IE.radical()
                dims.append(IE.dimension() if IE != D.S.ideal(1) else 0)
                # res^(-1)(sqrt(I_E)) by elimination
                T = PolynomialRing(F, list(R.variable_names()) +
                                   list(D.S.variable_names()))
                gR = T.gens()[:R.ngens()]
                gS = T.gens()[R.ngens():]
                tomap = lambda f, vars_: f(*vars_)
                J = T.ideal([gR[i] - tomap(rg[i], gS) if rg[i] != 0 else
                             gR[i] for i in range(R.ngens())] +
                            [tomap(f, gS) for f in radE.gens()] +
                            [tomap(f, gR) for f in base.gens()])
                pre = J.elimination_ideal(list(gS))
                preR = R.ideal([sum((c * prod_(R.gen(i) ** e[i]
                                               for i in range(R.ngens()))
                                     for e, c in f.dict().items()), R(0))
                                for f in pre.gens()] or [R(0)])
                inter = preR if inter is None else inter.intersection(preR)
                # Corollary 5.7.9: V_E(M) = (res^*)^(-1) V_G(M)
                img = D.S.ideal([f(*rg) for f in IG.gens()])
                ok10 &= img.radical() == radE
            ok5 &= radG == inter.radical()
            dG = IG.dimension()
            ok3 &= dG == max(dims)
        check(ok5, 'Proposition 5.7.4: sqrt(I_G(M)) = intersection over the '
              'maximal elementary abelian E (up to conjugacy) of '
              'res^(-1)(sqrt(I_E(M))), i.e. V_G(M) = union res^* V_E(M) (%d '
              'modules for %s; I_G(M) = Ker Phi_M through degree %d, I_E(M) '
              'from H^*(E, M))' % (len(mods), name, N))
        check(ok10, 'Corollary 5.7.9: V_E(M) = (res^*_(G,E))^(-1) V_G(M) '
              'for the maximal elementary abelian E of %s (%d modules)'
              % (name, len(mods)))
        check(ok3, 'Proposition 5.7.2 and Theorem 5.3.7 (Alperin-Evens): dim '
              'V_G(M) = max_E dim V_E(M) = max_E c_E(M) (%d modules for %s)'
              % (len(mods), name))
        check(okst, 'the radicals of the ideals generated by I_G(M) in '
              'degrees <= %d and <= %d agree (%s): the computed V_G(M) is '
              'stable' % (N - 2, N, name))


def gap_to_mod(F, G, gm):
    mats = libgap.eval('MTX.Generators')(gm)
    genact = [mrows(F, [[ff_conv(F, x) for x in row] for row in A.sage()]
                    ).transpose() for A in mats]
    return Mod.from_gens(F, G, genact)


def jordan_nil(F, s):
    return mat(F, s, s, {(i + 1, i): 1 for i in range(s - 1)})


def elem_coords(G, basis):
    out = {}
    for v in itertools.product(range(2), repeat=len(basis)):
        x = G.e
        for b, c in zip(basis, v):
            if c:
                x = G.mul[x][b]
        out[x] = v
    return out


def carlson_module(F, G, a, b, c):
    """Carlson's favourite example M_(a,b,c) (p. 183)."""
    def m(rows):
        return mrows(F, rows)
    g1 = m([[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1]])
    g2 = m([[1, 0, 0, 0], [0, 1, 0, 0], [a, 0, 1, 0], [0, b, 0, 1]])
    g3 = m([[1, 0, 0, 0], [0, 1, 0, 0], [0, c, 1, 0], [1, 0, 0, 1]])
    return Mod.from_gens(F, G, [g1, g2, g3])


def period_one_module(F, G):
    """The four dimensional module of p. 185."""
    def m(rows):
        return mrows(F, rows)
    g1 = m([[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1]])
    g2 = m([[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1]])
    g3 = m([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]])
    return Mod.from_gens(F, G, [g1, g2, g3])


def col_vec(F, entries):
    return mat(F, len(entries), 1, {(i, 0): x for i, x in enumerate(entries)
                                    if x})


def dual_hom(G, qf, Phi, i):
    """The homomorphism G -> F_2 dual to the i-th minimal generator."""
    return [dual_coords(G, Phi, g, G.gens)[i] for g in range(G.n)]


_DC = {}


def dual_coords(G, Phi, i_g, gens):
    """Coordinates in E = G/Phi (basis: the images of gens) of g."""
    key = (id(G),)
    if key not in _DC:
        Q, proj = G.quotient(Phi, 'E')
        n = len(gens)
        table = {}
        for v in itertools.product(range(2), repeat=n):
            x = G.e
            for gg, c in zip(gens, v):
                if c:
                    x = G.mul[x][gg]
            table[proj[x]] = v
        _DC[key] = (proj, table)
    proj, table = _DC[key]
    return table[proj[i_g]]


def binomial_poly(x, k):
    """binom(x, k) as a polynomial in x."""
    return prod_([x - i for i in range(k)]) * QQ(1) / factorial(k)


def main():
    set_random_seed(20261105)
    sections = [section_5_1, section_5_2, section_5_3, section_5_4,
                section_5_5, section_5_6, section_5_7_5_8_E, section_5_8,
                section_5_8_examples, section_5_7_groups]
    only = sys.argv[1:]
    for f in sections:
        if not only or f.__name__ in only:
            f()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
