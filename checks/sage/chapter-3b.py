"""Exact checks of Chapter 3, Sections 3.5-3.10 (Sage, with GAP's group data
through Sage's permutation groups).

Benson, *Representations and Cohomology II*, first paperback edition (1998),
Chapter 3 "Spectral sequences", Sections 3.5-3.10, printed pp. 109-119.  Our
files: content/03-05-group-extension.typ ...
content/03-10-equivariant-cohomology.typ.  (Sections 3.1-3.4 are checked in
chapter-3a.py; this script does not import it.)

Group cohomology is computed from free resolutions over GF(p)[G] built here
by linear algebra (minimal ones for p-groups), with cochains Hom_G(P_n, M),
Hom_N(P_n, M) over coset representatives, the conjugation action
(g phi)(x) = g phi(g^(-1) x), chains P_n (x)_G M, chain maps lifted between
resolutions (inflation, the projection to G/N) and Yoneda products.  The
pages of spectral sequences are computed by the formulas of chapter-3a.py
(E_r = Z_r / (Z_(r-1) + d Z_(r-1))).  Expected values are the book's
statements read off the printed pages (page and label in each message); the
chapter files are not parsed.  Where the printed text was corrected, the
printed reading is kept as a refuted check beside the corrected one.

Checked here:

3.5 (pp. 109-111), the extensions C4 > C2, Q8 > Z(Q8), Q8 > C4, D8 > Z(D8),
  D8 > C4, D8 > V4 (both), V4 > C2, C4 x C2 > C2 (three), A4 > V4 over GF(2),
  S3 > A3 over GF(3) and GF(2), with trivial and non-trivial modules M
  (F2[Q8/C4], F2[D8/V4], the sign and the permutation module F3^3 of S3);
  total degrees <= 4 or 5:
  * the double complex E_0^(pq) = Hom_(R(G/N))(P_p, Hom_(RN)(Q_q, M)) with
    d_0 = (-1)^p d'_q (p. 109): N acts trivially on H^q(N, M); E_1^(pq) =
    Hom(P_p, H^q(N, M)); E_2^(pq) = H^p(G/N, H^q(N, M)) computed separately;
    the abutment H^n(G, M) (p. 110); E_2 bounds H^n with equality exactly
    without higher differentials; the unsigned d_0, d_1 commute, so the
    sign is needed in odd characteristic (refuted without it);
  * Lemma 3.5.1 as an equality of subspaces of Hom_F(P_p (x) Q_q, F) (Q8,
    D8, C4, p, q <= 2), P_p (x) Q_q free, Tot(P (x) Q) a resolution of F;
  * the Exercise p. 110: the horizontal edge homomorphism is the inflation
    (rank = dim E_infinity^(n0)), the vertical one is the restriction into
    H^n(N, M)^(G/N) (rank = dim E_infinity^(0n));
  * the inflation-restriction sequence (Proposition 3.2.10) with explicit
    inflation and restriction, and d_2 of the double complex; the homology
    five term sequence (Proposition 3.2.11) with explicit corestriction from
    the G/N-coinvariants of H_1(N, M) and the projection to G/N;
  * the Ext spectral sequence of p. 110 over a field (D8 > V4 and Q8 > Z,
    non-trivial M_1, M_2, M_3): E_2 = Ext^p_(G/N)(M_1, Ext^q_N(M_2, M_3)) and
    the abutment Ext^n_G(M_1 (x) M_2, M_3).  As printed (no condition on
    M_1, M_2 over R) it is refuted: R = ZZ, G = N = 1, M_1 = M_2 = M_3 =
    ZZ/2 gives E_2 = E_infinity with total degree 1 of order 4 and total
    degree 2 non-zero, while Ext^1_ZZ(ZZ/2, ZZ/2) = ZZ/2, Ext^2 = 0;
    corrected ("with M_1 or M_2 projective as an R-module"): M_1 = ZZ.
3.6 (pp. 111-112): over ZZ (30 random pairs of complexes of free abelian
  groups) E^2_(pq) = sum Tor_p(H_s(C), H_t(D)) lives in the columns p = 0, 1
  and gives H_n(C (x) D) (Smith forms; the sequence splits over ZZ); over
  F_2[C_2] (6 pairs) the totals of E^2 bound H_n(C (x) D).
3.7 (pp. 112-114):
  * the total differential (d_0 + d_1) (x) 1 + (-1)^m 1 (x) d_N squares to
    zero for m = p + s, the total degree of the factor in P^(ps), and not
    for m = p or m = s (4 random cases over GF(3));
  * H^*(K(Z/2, 2); F_2) = F_2[u_0, u_1, ...], deg u_i = 2^i + 1: Serre's
    admissible Sq^I of excess < 2 (Sage's Steenrod algebra, degrees <= 64)
    are Sq^(2^(k-1)) ... Sq^1; a multiplicative model of the path fibration
    spectral sequence (E_2 = F_2[u_i] (x) F_2[x], filtration by the base
    degree) converges to F_2 in degree 0 through degree 20, its non-zero
    differentials are the transgressions d_(2^i + 1);
  * the Eilenberg-Moore spectral sequence Tor_(H^*(K(Z/2,2)))(F_2, H^*(G/Z))
    of the central extensions of (Z/2)^r by Z/2 (the bilinear cocycles: all
    2 for r = 1, all 8 for r = 2 (groups (Z/2)^3, C4 x C2, D8, Q8), 4 for
    r = 3), with u_0 |-> the class, u_(i+1) = Sq^(2^i) u_i (Cartan formula),
    Tor by the Koszul complex: its totals equal dim H^n(G; F_2) for n <= 7,
    6, 4 (r = 1, 2, 3), i.e. it collapses in these cases.
3.8 (p. 114): even differentials vanish when every other row is zero; d_r
  raises p by r; for Z/n (n = 2..8) H^*(Z/n, ZZ) = ZZ, 0, ZZ/n, 0, ... and
  the I-adic quotients of R(Z/n) are ZZ/n (k = 1..4), the same orders.
3.9 (pp. 115-117): three filtered differential graded commutative algebras
  over GF(3) (with differentials d_2 and d_4): Definition 3.9.4 (Leibniz on
  all pairs of monomials), Z_n Z_n <= Z_n, Z_n B_n + B_n Z_n <= B_n, and
  d_n(xy) = d_n(x) y + (-1)^(p+q) x d_n(y) in E_n (random elements), the
  sign necessary; in the LHS spectral sequences of central extensions by
  Z/2 with elementary abelian quotient (C4 > C2, Q8 > Z, D8 > Z, V4 > C2,
  C4 x C2 > C2, two of order 16) d_2 is a derivation of E_2 = H^*(G/N)
  (x) F_2[z]: rank d_2 on E_2^(pq) = [q odd] dim H^p(G/N) when d_2 z != 0.
3.10 (pp. 117-119): H^*(BU(m)) -> H^*(BU(n)) onto (elementary symmetric
  polynomials, n <= 4) -- so "finitely generated over H^*(BU; R)" agrees with
  the proof's H^*(BU(n); R); Corollary 3.10.2: multiplication by the
  non-zero class of degree 1 (C2; its square is c_1 of the sign), 2 (C4, C3,
  C5), resp. 4 (Q8, S3), is an isomorphism H^k -> H^(k+deg) (Yoneda
  products) for C2, C4, C3, C5, Q8 (GF(2)), S3 (GF(3)), k + deg <= 9; the
  degree 4 class of Q8 restricts non-trivially to each C4 (as c_2 of the
  2-dimensional representation does) and that of S3 to C3; for (Z/2)^r (r = 2, 3) H^* = F_2[x_i] is finite
  over the subring of the mod 2 Chern classes of a sum of characters iff the
  representation is faithful (7 cases).

Not established: none of the general theorems is proved here.  Every check
concerns the listed groups, modules, complexes and degrees.  Not checked:
the topological constructions (fibrations, the Eilenberg-Moore isomorphism,
the Atiyah-Hirzebruch spectral sequence, the Borel construction) beyond the
algebraic models named above; the identification c_2(rho) = the degree 4
class (only its restrictions are compared); integral cohomology of groups
other than cyclic; the Kunneth spectral sequence over rings of higher
global dimension beyond the inequality; Lemma 3.6.2 (proper projective
resolutions).  Nothing here compares our Typst text with the printed book.

Run with:  sage -python checks/sage/chapter-3b.py
"""
import itertools
import random

from sage.all import (GF, ZZ, QQ, matrix as _matrix, CyclicPermutationGroup,
                      DihedralGroup, QuaternionGroup, SymmetricGroup,
                      AlternatingGroup, KleinFourGroup, PermutationGroup,
                      PolynomialRing, SteenrodAlgebra, binomial)

SCOPE = 'chapter-3b'
COUNT = [0]
RNG = random.Random(20261106)


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


def ident(F, n):
    return mat(F, n, n, {(i, i): 1 for i in range(n)})


def hcat(F, n, mats):
    out = mat(F, n, 0)
    for A in mats:
        assert A.nrows() == n
        if A.ncols():
            out = out.augment(A)
    return out


def vcat(F, n, mats):
    out = mat(F, 0, n)
    for A in mats:
        assert A.ncols() == n
        if A.nrows():
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
    if not K.is_sparse() and _sp(F):
        K = K.sparse_matrix()
    return K.transpose()


def colbasis(A):
    if A.ncols() == 0 or A.nrows() == 0:
        return mat(A.base_ring(), A.nrows(), 0)
    return A.matrix_from_columns(A.pivots())


def in_span(S, V):
    return rk(S.augment(V)) == rk(S) if V.ncols() else True


def kron(F, A, B):
    ent = {}
    br, bc = B.nrows(), B.ncols()
    Bd = B.dict()
    for (i, j), a in A.dict().items():
        for (k, l), b in Bd.items():
            ent[(i * br + k, j * bc + l)] = a * b
    return mat(F, A.nrows() * br, A.ncols() * bc, ent)


class Quot:
    """The subquotient Z/B of F^n (spanning columns, B <= Z)."""

    def __init__(self, F, n, Zs, Bs):
        self.F, self.n = F, n
        Bb = colbasis(Bs)
        Zall = Bb.augment(Zs) if Zs.ncols() else Bb
        assert rk(Zall) == rk(Zs), 'B is not contained in Z'
        piv = Zall.pivots() if Zall.ncols() else ()
        self.nb = Bb.ncols()
        assert tuple(piv[:self.nb]) == tuple(range(self.nb))
        self.basis = Zall.matrix_from_columns(piv) if piv else mat(F, n, 0)
        self.dim = self.basis.ncols() - self.nb
        self.C = self.basis.matrix_from_columns(range(self.nb, self.nb
                                                      + self.dim))

    def cls(self, V):
        if V.ncols() == 0:
            return mat(self.F, self.dim, 0)
        X = self.basis.solve_right(V)
        return X.matrix_from_rows(range(self.nb, self.nb + self.dim))

    def rep(self, X=None):
        return self.C if X is None else self.C * X


# ===========================================================================
# Finite groups as multiplication tables
# ===========================================================================


class Grp:
    def __init__(self, n, mul, e, gens, name):
        self.n, self.mul, self.e, self.gens, self.name = n, mul, e, gens, name
        self.inv = [next(b for b in range(n) if mul[a][b] == e)
                    for a in range(n)]
        self.order = [self._order(a) for a in range(n)]

    def _order(self, a):
        k, x = 1, a
        while x != self.e:
            x = self.mul[x][a]
            k += 1
        return k

    @classmethod
    def from_sage(cls, G, name):
        els = list(G)
        ix = {g: i for i, g in enumerate(els)}
        mul = [[ix[a * b] for b in els] for a in els]
        gens = [ix[g] for g in G.gens()]
        return cls(len(els), mul, ix[G.identity()], gens, name)

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

    def is_normal(self, N):
        Ns = set(N)
        return all(self.mul[self.mul[g][x]][self.inv[g]] in Ns
                   for g in range(self.n) for x in N)

    def center(self):
        return [z for z in range(self.n)
                if all(self.mul[z][g] == self.mul[g][z]
                       for g in range(self.n))]

    def right_cosets(self, H):
        """Representatives T with G = disjoint union of H t, and for each x
        the decomposition x = h t (h in H, t in T)."""
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
        """G/N as a table group with the projection."""
        T, dec = self.right_cosets(N)
        tix = {t: i for i, t in enumerate(T)}
        proj = [tix[dec[x][1]] for x in range(self.n)]
        mul = [[proj[self.mul[a][b]] for b in T] for a in T]
        gens = sorted(set(proj[g] for g in self.gens) - {proj[self.e]})
        if not gens:
            gens = [proj[self.e]]
        Q = Grp(len(T), mul, proj[self.e], gens, name)
        return Q, proj

# ===========================================================================
# Modules and free resolutions over F[G]
# ===========================================================================


class Mod:
    """A left F[G]-module: act[g] for every element g."""

    def __init__(self, F, G, dim, act):
        self.F, self.G, self.dim, self.act = F, G, dim, act

    @classmethod
    def from_gens(cls, F, G, dim, genact):
        act = {G.e: ident(F, dim)}
        frontier = [G.e]
        while frontier:
            new = []
            for a in frontier:
                for g in G.gens:
                    b = G.mul[g][a]
                    if b not in act:
                        act[b] = genact[g] * act[a]
                        new.append(b)
            frontier = new
        assert len(act) == G.n
        M = cls(F, G, dim, act)
        assert all(act[G.mul[a][b]] == act[a] * act[b] for a in range(G.n)
                   for b in range(G.n)), 'not a representation'
        return M

    def lam(self, v):
        out = mat(self.F, self.dim, self.dim)
        for g, c in v.items():
            if c:
                out += c * self.act[g]
        return out

def trivial(F, G):
    return Mod(F, G, 1, {g: ident(F, 1) for g in range(G.n)})


def free_act(F, G, b):
    """The action on Lambda^b, basis e_(j,h) = h e_j at index j*|G| + h."""
    n = G.n
    return {g: mat(F, b * n, b * n, {(j * n + G.mul[g][h], j * n + h): 1
                                       for j in range(b) for h in range(n)})
            for g in range(n)}


def is_p_group(G, p):
    n = G.n
    while n % p == 0:
        n //= p
    return n == 1


def module_generators(F, G, act, K):
    """Generators of the F[G]-submodule with basis columns K of an ambient
    module with action act: minimal (complement of J K) for p-groups,
    greedy otherwise."""
    p = F.characteristic()
    dim = K.nrows()
    if K.ncols() == 0:
        return []
    if is_p_group(G, p):
        JK = hcat(F, dim, [(act[g] - ident(F, dim)) * K for g in G.gens])
        JB = colbasis(JK)
        allc = JB.augment(K) if JB.ncols() else K
        piv = allc.pivots()
        nb = JB.ncols()
        return [allc.matrix_from_columns([c]) for c in piv if c >= nb]
    gens = []
    S = mat(F, dim, 0)
    for c in range(K.ncols()):
        v = K.matrix_from_columns([c])
        if not in_span(S, v):
            gens.append(v)
            S = colbasis(hcat(F, dim, [S] + [act[g] * v for g in
                                              range(G.n)]))
    return gens


def map_from_free(F, G, act_tgt, images):
    """Lambda^b -> target with e_j |-> images[j]."""
    cols = []
    for v in images:
        for h in range(G.n):
            cols.append(act_tgt[h] * v)
    dim = images[0].nrows() if images else 0
    return hcat(F, dim, cols)


class Resolution:
    """A free resolution P_* -> M of an F[G]-module (minimal when G is a
    p-group), up to degree nmax: ranks b[n], F-matrices d[n] : P_n ->
    P_(n-1), eps : P_0 -> M."""

    def __init__(self, M, nmax):
        F, G = M.F, M.G
        self.F, self.G, self.M = F, G, M
        gens = module_generators(F, G, M.act, ident(F, M.dim))
        self.b = [len(gens)]
        self.eps = map_from_free(F, G, M.act, gens)
        self.act = {0: free_act(F, G, self.b[0])}
        self.d = {}
        prev = self.eps
        for n in range(1, nmax + 1):
            K = kernel_cols(prev)
            gens = module_generators(F, G, self.act[n - 1], K)
            self.b.append(len(gens))
            self.act[n] = free_act(F, G, len(gens))
            if gens:
                self.d[n] = map_from_free(F, G, self.act[n - 1], gens)
            else:
                self.d[n] = mat(F, self.act[n - 1][G.e].nrows(), 0)
            # exactness at P_(n-1)
            assert rk(self.d[n]) == K.ncols()
            prev = self.d[n]
        self.nmax = nmax

    def dim(self, n):
        return self.b[n] * self.G.n

    def lam_entries(self, n):
        """The F[G]-matrix of d_n: L[(j, i)] = {h: coefficient} with
        d(e_i) = sum_j L[(j, i)] e_j."""
        G = self.G
        A = self.d[n]
        L = {}
        for i in range(self.b[n]):
            col = A.column(i * G.n + G.e)
            for j in range(self.b[n - 1]):
                v = {h: col[j * G.n + h] for h in range(G.n)
                     if col[j * G.n + h]}
                if v:
                    L[(j, i)] = v
        return L


def cochain_differentials(P, M, nmax):
    """Hom_G(P_n, M) = M^(b_n) via phi |-> (phi(e_j))_j, and the
    coboundaries delta^n : C^n -> C^(n+1)."""
    F = M.F
    dims = {n: P.b[n] * M.dim for n in range(nmax + 1)}
    delta = {}
    for n in range(nmax):
        L = P.lam_entries(n + 1)
        A = mat(F, dims[n + 1], dims[n])
        for (j, i), v in L.items():
            B = M.lam(v)
            for (r, c), x in B.dict().items():
                A[i * M.dim + r, j * M.dim + c] += x
        delta[n] = A
    return dims, delta


def cohomology(P, M, nmax):
    """H^n(G, M) for n <= nmax - 1 (needs P up to degree nmax) as Quot
    objects in cochain coordinates."""
    dims, delta = cochain_differentials(P, M, nmax)
    H = {}
    for n in range(nmax):
        Zs = kernel_cols(delta[n])
        Bs = delta[n - 1] if n >= 1 else mat(M.F, dims[n], 0)
        H[n] = Quot(M.F, dims[n], Zs, Bs)
    return H, dims, delta


def restricted_cochains(P, M, H, nmax):
    """Hom_H(P_n, M) for a subgroup H (a list of elements of G) with
    coordinates (psi(t e_j))_(j,t), t over right coset representatives;
    coboundaries; restriction from Hom_G(P_n, M)."""
    F, G = M.F, P.G
    T, dec = G.right_cosets(H)
    tix = {t: k for k, t in enumerate(T)}
    m = M.dim
    nt = len(T)
    dims = {n: P.b[n] * nt * m for n in range(nmax + 1)}

    def idx(j, t):
        return (j * nt + tix[t]) * m

    delta = {}
    for n in range(nmax):
        L = P.lam_entries(n + 1)
        A = mat(F, dims[n + 1], dims[n])
        for (j, i), v in L.items():
            for t1 in T:
                for h, c in v.items():
                    x = G.mul[t1][h]
                    hh, t2 = dec[x]
                    B = M.act[hh]
                    r0, c0 = idx(i, t1), idx(j, t2)
                    for (r, cc), y in B.dict().items():
                        A[r0 + r, c0 + cc] += c * y
        delta[n] = A
    res = {}
    for n in range(nmax + 1):
        A = mat(F, dims[n], P.b[n] * m)
        for j in range(P.b[n]):
            for t in T:
                B = M.act[t]
                for (r, cc), y in B.dict().items():
                    A[idx(j, t) + r, j * m + cc] += y
        res[n] = A

    def conj(g):
        """(g . psi)(t e_j) = g psi(g^(-1) t e_j), g normalising H."""
        out = {}
        for n in range(nmax + 1):
            A = mat(F, dims[n], dims[n])
            gi = G.inv[g]
            for j in range(P.b[n]):
                for t in T:
                    x = G.mul[gi][t]
                    hh, t2 = dec[x]
                    B = M.act[g] * M.act[hh]
                    for (r, cc), y in B.dict().items():
                        A[idx(j, t) + r, idx(j, t2) + cc] += y
            out[n] = A
        return out

    return dims, delta, res, conj, T, dec


# ===========================================================================
# Chain maps between resolutions; inflation; Yoneda products
# ===========================================================================


def lift_chain_map(P, Q, start, nmax, proj=None):
    """A chain map f : P -> Q over a map on the modules, given on the
    generators of P_0 by start (columns in Q_0) with eps_Q start = the
    prescribed values.  Q may be a resolution over a quotient group, P_n
    acting through proj : G -> G/N.  Returns F-matrices f[n] : P_n -> Q_n
    (G-linear)."""
    F, G = P.F, P.G
    pr = proj if proj is not None else list(range(G.n))
    f = {}
    imgs = {0: start}
    for n in range(0, nmax + 1):
        if n > 0:
            imgs[n] = []
            for i in range(P.b[n]):
                col = P.d[n].matrix_from_columns([i * G.n + G.e])
                target = f[n - 1] * col
                x = Q.d[n].solve_right(target)
                imgs[n].append(x)
        cols = []
        for x in imgs[n]:
            for h in range(G.n):
                cols.append(Q.act[n][pr[h]] * x)
        f[n] = hcat(F, Q.dim(n), cols)
        if n > 0:
            assert Q.d[n] * f[n] == f[n - 1] * P.d[n]
    return f


def inflation_maps(PG, PQ, MN, M, incl, proj, nmax):
    """inf : Hom_(G/N)(P'_n, M^N) -> Hom_G(P_n, M), via a chain map P -> P'
    over the identity of F (trivial module) and the inclusion M^N -> M
    (incl: columns of M^N in M)."""
    F = M.F
    QG = PQ.G
    # start: e_i |-> c e_(0, 1) with eps' = eps
    j0 = next(j for j in range(PQ.b[0])
              if PQ.eps[0, j * QG.n + QG.e] != 0)
    a = PQ.eps[0, j0 * QG.n + QG.e]
    start = []
    for i in range(PG.b[0]):
        val = PG.eps[0, i * PG.G.n + PG.G.e]
        start.append(mat(F, PQ.dim(0), 1, {(j0 * QG.n + QG.e, 0): val / a}))
    f = lift_chain_map(PG, PQ, start, nmax, proj)
    infl = {}
    for n in range(nmax + 1):
        A = mat(F, PG.b[n] * M.dim, PQ.b[n] * MN.dim)
        for i in range(PG.b[n]):
            col = f[n].column(i * PG.G.n + PG.G.e)
            for j in range(PQ.b[n]):
                v = {y: col[j * QG.n + y] for y in range(QG.n)
                     if col[j * QG.n + y]}
                if not v:
                    continue
                B = incl * MN.lam(v)
                for (r, c), x in B.dict().items():
                    A[i * M.dim + r, j * MN.dim + c] += x
        infl[n] = A
    return infl, f


def yoneda_lift(P, cocycle, m, kmax):
    """For a cocycle P_m -> F (trivial module; values on the generators),
    chain maps tau_k : P_(m+k) -> P_k with eps tau_0 = cocycle."""
    F, G = P.F, P.G
    j0 = next(j for j in range(P.b[0]) if P.eps[0, j * G.n + G.e] != 0)
    a = P.eps[0, j0 * G.n + G.e]
    tau = {}
    for k in range(kmax + 1):
        imgs = []
        for i in range(P.b[m + k]):
            if k == 0:
                imgs.append(mat(F, P.dim(0), 1,
                                {(j0 * G.n + G.e, 0): cocycle[i] / a}))
            else:
                col = P.d[m + k].matrix_from_columns([i * G.n + G.e])
                imgs.append(P.d[k].solve_right(tau[k - 1] * col))
        cols = []
        for x in imgs:
            for h in range(G.n):
                cols.append(P.act[k][h] * x)
        tau[k] = hcat(F, P.dim(k), cols)
        if k > 0:
            assert P.d[k] * tau[k] == tau[k - 1] * P.d[m + k]
        else:
            assert P.eps * tau[0] == mat(F, 1, P.dim(m), {
                (0, i * G.n + h): cocycle[i] for i in range(P.b[m])
                for h in range(G.n) if cocycle[i]})
    return tau


def cup_matrix(P, H, cocycle, m, k):
    """The matrix of eta |-> eta . zeta : H^k -> H^(k+m) (trivial module F,
    zeta of degree m given by a cocycle), in the Quot coordinates."""
    F, G = P.F, P.G
    tau = yoneda_lift(P, cocycle, m, k)
    # a cochain of degree k is (psi(e_j))_j; psi o tau_k on e_i
    A = mat(F, P.b[m + k], P.b[k])
    for i in range(P.b[m + k]):
        col = tau[k].column(i * G.n + G.e)
        for j in range(P.b[k]):
            A[i, j] = sum(col[j * G.n + h] for h in range(G.n))
    return H[k + m].cls(A * H[k].rep())


# ===========================================================================
# Homology over F[G]
# ===========================================================================


def chain_differentials(P, M, nmax):
    """P_n (x)_G M = M^(b_n) via e_j (x) m; h e_j (x) m = e_j (x) h^(-1) m."""
    F, G = M.F, P.G
    dims = {n: P.b[n] * M.dim for n in range(nmax + 1)}
    dd = {}
    for n in range(1, nmax + 1):
        L = P.lam_entries(n)
        A = mat(F, dims[n - 1], dims[n])
        for (j, i), v in L.items():
            B = M.lam({G.inv[h]: c for h, c in v.items()})
            for (r, c), x in B.dict().items():
                A[j * M.dim + r, i * M.dim + c] += x
        dd[n] = A
    return dims, dd


def homology(P, M, nmax):
    dims, dd = chain_differentials(P, M, nmax)
    H = {}
    for n in range(nmax):
        Zs = kernel_cols(dd[n]) if n >= 1 else ident(M.F, dims[0])
        H[n] = Quot(M.F, dims[n], Zs, dd[n + 1])
    return H, dims, dd


def restricted_chains(P, M, N, nmax):
    """P_n (x)_N M with basis (t e_j) (x) m; corestriction to P_n (x)_G M;
    the conjugation action g . (x (x) m) = g x (x) g m."""
    F, G = M.F, P.G
    T, dec = G.right_cosets(N)
    tix = {t: k for k, t in enumerate(T)}
    m = M.dim
    nt = len(T)
    dims = {n: P.b[n] * nt * m for n in range(nmax + 1)}

    def idx(j, t):
        return (j * nt + tix[t]) * m

    dd = {}
    for n in range(1, nmax + 1):
        L = P.lam_entries(n)
        A = mat(F, dims[n - 1], dims[n])
        for (j, i), v in L.items():
            for t1 in T:
                for h, c in v.items():
                    hh, t2 = dec[G.mul[t1][h]]
                    B = M.act[G.inv[hh]]
                    for (r, cc), y in B.dict().items():
                        A[idx(j, t2) + r, idx(i, t1) + cc] += c * y
        dd[n] = A
    cor = {}
    for n in range(nmax + 1):
        A = mat(F, P.b[n] * m, dims[n])
        for j in range(P.b[n]):
            for t in T:
                B = M.act[G.inv[t]]
                for (r, cc), y in B.dict().items():
                    A[j * m + r, idx(j, t) + cc] += y
        cor[n] = A

    def conj(g):
        out = {}
        for n in range(nmax + 1):
            A = mat(F, dims[n], dims[n])
            for j in range(P.b[n]):
                for t in T:
                    hh, t2 = dec[G.mul[g][t]]
                    B = M.act[G.inv[hh]] * M.act[g]
                    for (r, cc), y in B.dict().items():
                        A[idx(j, t2) + r, idx(j, t) + cc] += y
            out[n] = A
        return out

    return dims, dd, cor, conj


def coinvariant_quotient(G, Hq, conj_mats, deg):
    """dim and projection for H_(G/N) = H / span((g - 1) H)."""
    F = Hq.F
    rels = []
    for g in G.gens:
        A = Hq.cls(conj_mats[g][deg] * Hq.rep()) - ident(F, Hq.dim)
        rels.append(A)
    R = hcat(F, Hq.dim, rels)
    return Quot(F, Hq.dim, ident(F, Hq.dim), R)


# ===========================================================================
# Filtered complexes (pages by Z_r / B_r), as in chapter-3a.py
# ===========================================================================


class Filtered:
    """Finite filtered cochain complex, filtration split by the basis;
    F^p X^n spanned by basis vectors with filt >= p."""

    def __init__(self, F, filt, d):
        self.F, self.filt, self.d = F, filt, d
        fs = [a for f in filt.values() for a in f] or [0]
        self.fmin, self.fmax = min(fs), max(fs)
        self.rinf = self.fmax - self.fmin + 2
        for n in filt:
            A = self.dm(n)
            for (i, j), _ in A.dict().items():
                assert self.filt[n + 1][i] >= self.filt[n][j]
            assert (self.dm(n + 1) * A).is_zero()

    def dim(self, n):
        return len(self.filt.get(n, []))

    def dm(self, n):
        A = self.d.get(n)
        return A if A is not None else mat(self.F, self.dim(n + 1),
                                           self.dim(n))

    def idx(self, n, lo=None, hi=None):
        return [i for i, a in enumerate(self.filt.get(n, []))
                if (lo is None or a >= lo) and (hi is None or a < hi)]

    def units(self, n, idx):
        return mat(self.F, self.dim(n), len(idx),
                   {(i, k): 1 for k, i in enumerate(idx)})

    def rows(self, n, idx):
        return mat(self.F, len(idx), self.dim(n),
                   {(k, i): 1 for k, i in enumerate(idx)})

    def Z(self, r, p, n):
        S = self.units(n, self.idx(n, p))
        cond = self.rows(n + 1, self.idx(n + 1, None, p + r)) * self.dm(n)
        return S * kernel_cols(cond * S)

    def B(self, r, p, n):
        if r == 0:
            return self.units(n, self.idx(n, p + 1))
        return hcat(self.F, self.dim(n),
                    [self.Z(r - 1, p + 1, n),
                     self.dm(n - 1) * self.Z(r - 1, p - r + 1, n - 1)])

    def E(self, r, p, n):
        return Quot(self.F, self.dim(n), self.Z(r, p, n), self.B(r, p, n))

    def Edim(self, r, p, n):
        return self.E(r, p, n).dim

    def dr_rank(self, r, p, n):
        Zs = self.dm(n) * self.Z(r, p, n)
        Bt = self.B(r, p + r, n + 1)
        return rk(hcat(self.F, self.dim(n + 1), [Bt, Zs])) - rk(Bt)

# ===========================================================================
# Section 3.5: the Lyndon-Hochschild-Serre double complex
# ===========================================================================


def quotient_resolution_action(PQ, W, n):
    """Hom_Q(P'_n, W) = W^(b_n) and d_1 : Hom(P'_n, W) -> Hom(P'_(n+1), W)."""
    F = W.F
    L = PQ.lam_entries(n + 1)
    A = mat(F, PQ.b[n + 1] * W.dim, PQ.b[n] * W.dim)
    for (j, i), v in L.items():
        B = W.lam(v)
        for (r, c), x in B.dict().items():
            A[i * W.dim + r, j * W.dim + c] += x
    return A


class LHS:
    """E_0^(pq) = Hom_(G/N)(P_p, Hom_N(Q_q, M)), d_0 = (-1)^p (induced by
    d'_q), d_1 induced by d_p (p. 109), total degrees <= top + 1."""

    def __init__(self, G, N, M, top, M1=None, PQ=None, M2=None):
        F = M.F
        self.G, self.N, self.M, self.top = G, N, M, top
        Q, proj = G.quotient(N, G.name + '/N')
        self.Q, self.proj = Q, proj
        self.QG = Resolution(M2 if M2 is not None else trivial(F, G),
                             top + 2)                   # Q_* over G
        if M1 is None:
            M1 = trivial(F, Q)
        self.PQ = PQ or Resolution(M1, top + 2)             # P_* over G/N
        dims, delta, res, conj, _, _ = restricted_cochains(
            self.QG, M, N, top + 2)
        self.Wdims, self.Wdelta, self.res = dims, delta, res
        # Hom_N(Q_q, M) as a G/N-module (the action factors through G/N)
        cmaps = {g: conj(g) for g in range(G.n)}
        self.cmaps = cmaps
        W = {}
        for q in range(top + 3):
            act = {}
            for g in range(G.n):
                act.setdefault(proj[g], cmaps[g][q])
                assert act[proj[g]] == cmaps[g][q], 'N acts non-trivially'
            W[q] = Mod(F, Q, dims[q], act)
            for g in range(G.n):          # d'_q is G-equivariant
                if q + 1 <= top + 2 and q in delta:
                    assert delta[q] * cmaps[g][q] == cmaps[g][q + 1] * \
                        delta[q]
        self.W = W
        # the double complex
        PQ = self.PQ
        keys, filt = {}, {}
        for p in range(top + 2):
            for q in range(top + 2 - p):
                n = p + q
                for i in range(PQ.b[p] * W[q].dim):
                    keys.setdefault(n, []).append((p, q, i))
                    filt.setdefault(n, []).append(p)
        pos = {n: {k: a for a, k in enumerate(v)} for n, v in keys.items()}
        d = {}
        for n in keys:
            if n + 1 not in keys:
                continue
            A = mat(F, len(keys[n + 1]), len(keys[n]))
            for p in range(0, n + 1):
                q = n - p
                if PQ.b[p] * W[q].dim == 0:
                    continue
                if PQ.b[p] * W[q + 1].dim:      # d_0 = (-1)^p d'_q
                    B = (-1) ** p * kron(F, ident(F, PQ.b[p]),
                                         self.Wdelta[q])
                    for (r, c), x in B.dict().items():
                        A[pos[n + 1][(p, q + 1, r)], pos[n][(p, q, c)]] += x
                if PQ.b[p + 1] * W[q].dim:      # d_1 induced by d_(p+1)
                    B = quotient_resolution_action(PQ, W[q], p)
                    for (r, c), x in B.dict().items():
                        A[pos[n + 1][(p + 1, q, r)], pos[n][(p, q, c)]] += x
            d[n] = A
        self.X = Filtered(F, filt, d)
        self.keys, self.pos = keys, pos


# ===========================================================================
# Section 3.5 (with Propositions 3.2.10, 3.2.11 for group extensions)
# ===========================================================================


def groups():
    G = {
        'C2': Grp.from_sage(CyclicPermutationGroup(2), 'C2'),
        'C4': Grp.from_sage(CyclicPermutationGroup(4), 'C4'),
        'V4': Grp.from_sage(KleinFourGroup(), 'V4'),
        'Q8': Grp.from_sage(QuaternionGroup(), 'Q8'),
        'D8': Grp.from_sage(DihedralGroup(4), 'D8'),
        'S3': Grp.from_sage(SymmetricGroup(3), 'S3'),
        'A4': Grp.from_sage(AlternatingGroup(4), 'A4'),
        'C4xC2': Grp.from_sage(PermutationGroup([[(1, 2, 3, 4)], [(5, 6)]]),
                               'C4xC2'),
    }
    return G


def normal_subgroups_of_order(G, k):
    """All normal subgroups of order k (by closure of 1 or 2 elements)."""
    found = set()
    for a in range(G.n):
        for b in range(G.n):
            S = tuple(G.closure([a, b]))
            if len(S) == k and G.is_normal(S):
                found.add(S)
    return sorted(found)


def perm_module_on_quotient(F, G, N):
    """F[G/N] (N acts trivially) as a G-module."""
    T, dec = G.right_cosets(N)
    # left action on left cosets x N: use x |-> g x on the coset of g x;
    # for normal N left and right cosets agree
    tix = {t: k for k, t in enumerate(T)}

    def coset(x):
        return tix[dec[x][1]]
    genact = {}
    for g in G.gens:
        genact[g] = mat(F, len(T), len(T), {(coset(G.mul[g][t]), tix[t]): 1
                                            for t in T})
    return Mod.from_gens(F, G, len(T), genact)


def lhs_cases():
    Gs = groups()
    F2, F3 = GF(2), GF(3)
    cases = []
    C4 = Gs['C4']
    cases.append(('C4 > C2', C4, normal_subgroups_of_order(C4, 2)[0],
                  trivial(F2, C4), 5))
    Q8 = Gs['Q8']
    cases.append(('Q8 > Z(Q8)', Q8, Q8.center(), trivial(F2, Q8), 5))
    N4 = normal_subgroups_of_order(Q8, 4)[0]
    cases.append(('Q8 > C4', Q8, N4, trivial(F2, Q8), 5))
    cases.append(('Q8 > C4, M = F2[Q8/C4]', Q8, N4,
                  perm_module_on_quotient(F2, Q8, N4), 4))
    D8 = Gs['D8']
    cases.append(('D8 > Z(D8)', D8, D8.center(), trivial(F2, D8), 5))
    for N in normal_subgroups_of_order(D8, 4):
        kind = 'C4' if any(D8.order[x] == 4 for x in N) else 'V4'
        cases.append(('D8 > %s' % kind, D8, list(N), trivial(F2, D8), 4))
        if kind == 'V4':
            cases.append(('D8 > V4, M = F2[D8/V4]', D8, list(N),
                          perm_module_on_quotient(F2, D8, N), 4))
    V4 = Gs['V4']
    cases.append(('V4 > C2', V4, normal_subgroups_of_order(V4, 2)[0],
                  trivial(F2, V4), 5))
    S3 = Gs['S3']
    A3 = normal_subgroups_of_order(S3, 3)[0]
    cases.append(('S3 > A3 (p = 3)', S3, A3, trivial(F3, S3), 5))
    sgn = Mod.from_gens(F3, S3, 1, {g: mat(F3, 1, 1, {(0, 0): 1 if
                                                         S3.order[g] != 2
                                                         else -1})
                                    for g in S3.gens})
    cases.append(('S3 > A3, sign module (p = 3)', S3, A3, sgn, 5))
    perm3 = Mod.from_gens(F3, S3, 3, {g: perm_matrix_of(F3, S3, g)
                                      for g in S3.gens})
    cases.append(('S3 > A3, permutation module F3^3 (p = 3)', S3, A3,
                  perm3, 4))
    cases.append(('S3 > A3 (p = 2)', S3, A3, trivial(F2, S3), 4))
    A4 = Gs['A4']
    cases.append(('A4 > V4 (p = 2)', A4, normal_subgroups_of_order(A4, 4)[0],
                  trivial(F2, A4), 4))
    C42 = Gs['C4xC2']
    for N in normal_subgroups_of_order(C42, 2):
        cases.append(('C4xC2 > C2', C42, list(N), trivial(F2, C42), 4))
    return cases


SAGE_S3 = SymmetricGroup(3)


def perm_matrix_of(F, G, g):
    """The permutation matrix of the element g of S3 on {1, 2, 3} (G built
    from SymmetricGroup(3) in its element order)."""
    el = list(SAGE_S3)[g]
    return mat(F, 3, 3, {(el(i + 1) - 1, i): 1 for i in range(3)})


def module_cohomology_dims(PQ, V, top):
    H, _, _ = cohomology(PQ, V, top + 1)
    return [H[n].dim for n in range(top + 1)]


def section_3_5():
    for (lab, G, N, M, top) in lhs_cases():
        F = M.F
        L = LHS(G, N, M, top)
        X, Q, proj = L.X, L.Q, L.proj
        PG = L.QG
        HG, _, _ = cohomology(PG, M, top + 1)
        # H^q(N, M) with the action of G/N, from the cochains Hom_N(Q_q, M)
        Hq = {}
        for q in range(top + 1):
            Zs = kernel_cols(L.Wdelta[q])
            Bs = L.Wdelta[q - 1] if q else mat(F, L.Wdims[0], 0)
            Hq[q] = Quot(F, L.Wdims[q], Zs, Bs)
        # N acts trivially on H^q(N, M); G/N-modules H^q(N, M)
        ok = all(Hq[q].cls(L.cmaps[x][q] * Hq[q].rep()) ==
                 ident(F, Hq[q].dim) for q in range(top + 1) for x in N)
        check(ok, 'Section 3.5: N acts trivially on H^q(N, M) (conjugation);'
              ' %s' % lab)
        Vq = {}
        for q in range(top + 1):
            act = {proj[g]: Hq[q].cls(L.cmaps[g][q] * Hq[q].rep())
                   for g in range(G.n)}
            Vq[q] = Mod(F, Q, Hq[q].dim, act)
        PQ = L.PQ
        E2 = {}
        for q in range(top + 1):
            dims = module_cohomology_dims(PQ, Vq[q], top - q) if \
                Vq[q].dim else [0] * (top - q + 1)
            for p in range(top - q + 1):
                E2[(p, q)] = dims[p]
        okE1 = all(X.Edim(1, p, p + q) == PQ.b[p] * Hq[q].dim
                   for p in range(top + 1) for q in range(top + 1 - p))
        check(okE1, 'p. 109: E_1^(pq) = Hom_(R(G/N))(P_p, H^q(N, M)) (%s)'
              % lab)
        okE2 = all(X.Edim(2, p, p + q) == E2[(p, q)] for (p, q) in E2)
        check(okE2, 'p. 109: E_2^(pq) = H^p(G/N, H^q(N, M)) (%s)' % lab)
        R = X.rinf
        ok = all(sum(X.Edim(R, p, n) for p in range(n + 1)) == HG[n].dim
                 for n in range(top + 1))
        check(ok, 'p. 110: H^*(Tot(E_0)) ~ H^*(G, M), i.e. the spectral '
              'sequence converges to H^(p+q)(G, M) (%s)' % lab)
        # E_2 against the abutment: the totals bound H^n, and are equal
        # exactly when no differential d_r, r >= 2, is non-zero
        nd = sum(X.dr_rank(r, p, p + q) for r in range(2, R)
                 for p in range(top + 1) for q in range(top - p))
        tot2 = [sum(E2[(p, n - p)] for p in range(n + 1))
                for n in range(top + 1)]
        check(all(t >= HG[n].dim for n, t in enumerate(tot2)) and
              ((nd == 0) == all(t == HG[n].dim for n, t in enumerate(tot2)
                                if n < top)),
              'E_2 against the known cohomology: sum_(p+q=n) dim E_2^(pq) '
              '>= dim H^n(G, M), equality iff no d_r (%s; totals %s, H^n %s)'
              % (lab, tot2, [HG[n].dim for n in range(top + 1)]))
        # the exercise (p. 110): edge homomorphisms
        MN_cols = kernel_cols(vcat(F, M.dim, [M.act[x] - ident(F, M.dim)
                                               for x in N]))    # M^N
        MN = Mod(F, Q, MN_cols.ncols(), {
            proj[g]: MN_cols.solve_right(M.act[g] * MN_cols)
            for g in range(G.n)})
        infl, _ = inflation_maps(PG, PQ, MN, M, MN_cols, proj,
                                        top + 1)
        HQ, _, _ = cohomology(PQ, MN, top + 1)
        ok_inf, ok_res, ok_inv = True, True, True
        inf_mats, res_mats = {}, {}
        for n in range(top + 1):
            A = HG[n].cls(infl[n] * HQ[n].rep())
            inf_mats[n] = A
            ok_inf &= rk(A) == X.Edim(R, n, n)
            B = Hq[n].cls(L.res[n] * HG[n].rep())
            res_mats[n] = B
            ok_res &= rk(B) == X.Edim(R, 0, n)
            for g in range(G.n):
                C = Hq[n].cls(L.cmaps[g][n] * Hq[n].rep())
                ok_inv &= (C * B == B)
        check(ok_inf, 'Exercise p. 110: the horizontal edge homomorphism is '
              'the inflation H^n(G/N, M^N) -> H^n(G, M) (rank = dim '
              'E_infinity^(n0)) (%s)' % lab)
        check(ok_res and ok_inv, 'Exercise p. 110: the vertical edge '
              'homomorphism is res : H^n(G, M) -> H^n(N, M)^(G/N) (image '
              'invariant, rank = dim E_infinity^(0n)) (%s)' % lab)
        # inflation-restriction sequence (Proposition 3.2.10, p. 110)
        inv1 = kernel_cols(vcat(F, Hq[1].dim, [
            Hq[1].cls(L.cmaps[g][1] * Hq[1].rep()) - ident(F, Hq[1].dim)
            for g in G.gens]))
        dim_inv = inv1.ncols()
        check(dim_inv == E2[(0, 1)], 'E_2^(01) = H^1(N, M)^(G/N) (%s)' % lab)
        i1, r1, i2 = inf_mats[1], res_mats[1], inf_mats[2]
        ok = rk(i1) == HQ[1].dim                                   # injective
        ok &= (r1 * i1).is_zero() and rk(i1) == HG[1].dim - rk(r1)
        d2 = X.dr_rank(2, 0, 1)
        ok &= d2 == dim_inv - rk(r1)                       # Ker d_2 = Im res
        ok &= d2 == HQ[2].dim - rk(i2)                     # Im d_2 = Ker inf
        check(ok, 'p. 110, Proposition 3.2.10: 0 -> H^1(G/N, M^N) -> H^1(G, M)'
              ' -> H^1(N, M)^(G/N) -> H^2(G/N, M^N) -> H^2(G, M) is exact '
              '(inflation-restriction sequence; %s)' % lab)
        # the sign (-1)^p of d_0 (p. 109): the unsigned maps commute
        B0p = kron(F, ident(F, PQ.b[1]), L.Wdelta[0])
        B1 = quotient_resolution_action(PQ, L.W[0], 0)
        B1b = quotient_resolution_action(PQ, L.W[1], 0)
        A0 = kron(F, ident(F, PQ.b[0]), L.Wdelta[0])
        check((B0p * B1 - B1b * A0).is_zero(), 'p. 109: the differentials '
              'induced by d_p and d\'_q commute, so d_0 = (-1)^p d\'_q gives '
              'd_0 d_1 = -d_1 d_0 (%s)' % lab)
        if F.characteristic() != 2 and not (B1b * A0).is_zero():
            refuted((B0p * B1 + B1b * A0).is_zero(), 'p. 109 without the '
                    'sign (-1)^p: d_0 d_1 = -d_1 d_0 (%s)' % lab)


def section_3_5_lemma():
    """Lemma 3.5.1 as an equality of subspaces of Hom_F(P_p (x) Q_q, M), and
    Tot(P (x) Q) a free resolution (p. 110)."""
    Gs = groups()
    F = GF(2)
    for name, nsub in (('Q8', 'center'), ('D8', 4), ('C4', 2)):
        G = Gs[name]
        N = G.center() if nsub == 'center' else \
            list(normal_subgroups_of_order(G, nsub)[0])
        Q, proj = G.quotient(N, 'Q')
        PQ = Resolution(trivial(F, Q), 3)
        PG = Resolution(trivial(F, G), 3)
        for p in range(3):
            for q in range(3):
                Pact = {g: PQ.act[p][proj[g]] for g in range(G.n)}
                Qact = PG.act[q]
                dp, dq = PQ.dim(p), PG.dim(q)
                eqG, eqL = [], []
                for g in G.gens:
                    T = kron(F, Pact[g], Qact[g])
                    # X T = M X with X : dim M x (dp dq), vec row-wise
                    eqG.append(T.transpose() - ident(F, dp * dq))
                    # G/N-linearity of f: X (P(g) (x) 1) = X (1 (x) Q(g)^-1)
                    eqL.append((kron(F, Pact[g], ident(F, dq)) -
                                kron(F, ident(F, dp), Qact[G.inv[g]]))
                               .transpose())
                for x in N:
                    eqL.append((kron(F, ident(F, dp), Qact[x]) -
                                ident(F, dp * dq)).transpose())
                KG = kernel_cols(vcat(F, dp * dq, eqG))
                KL = kernel_cols(vcat(F, dp * dq, eqL))
                same = rk(KG) == rk(KL) == rk(KG.augment(KL))
                check(same, 'Lemma 3.5.1: Hom_(G/N)(P_%d, Hom_N(Q_%d, F)) = '
                      'Hom_G(P_%d (x) Q_%d, F) inside Hom_F (%s)'
                      % (p, q, p, q, name))
                # P_p (x) Q_q is free over F[G] (norm element of the
                # 2-group acts with rank dim / |G|)
                T = sum((kron(F, Pact[g], Qact[g]) for g in range(G.n)),
                        mat(F, dp * dq, dp * dq))
                check(rk(T) * G.n == dp * dq, 'p. 110: P_%d (x) Q_%d is a '
                      'free F[%s]-module' % (p, q, name))
        # Tot(P (x) Q) is exact in positive degrees, H_0 = F
        tot = {}
        for n in range(0, 4):
            tot[n] = sum(PQ.dim(p) * PG.dim(n - p) for p in range(n + 1))
        dd = {}
        for n in range(1, 4):
            A = mat(F, tot[n - 1], tot[n])
            ro = {}
            o = 0
            for p in range(n):
                ro[p] = o
                o += PQ.dim(p) * PG.dim(n - 1 - p)
            co = 0
            for p in range(n + 1):
                q = n - p
                w = PQ.dim(p) * PG.dim(q)
                if p >= 1:
                    B = kron(F, PQ.d[p], ident(F, PG.dim(q)))
                    for (r, c), x in B.dict().items():
                        A[ro[p - 1] + r, co + c] += x
                if q >= 1:
                    B = kron(F, ident(F, PQ.dim(p)), PG.d[q])
                    for (r, c), x in B.dict().items():
                        A[ro[p] + r, co + c] += x
                co += w
            dd[n] = A
        h = [tot[n] - (rk(dd[n]) if n in dd else 0) - rk(dd[n + 1])
             for n in range(0, 3)]
        check(h == [1, 0, 0], 'p. 110 (Corollary 2.7.3 of Volume I): '
              'Tot(P (x) Q) is exact in positive degrees with H_0 = F (%s)'
              % name)


def section_3_5_homology():
    """The five term sequence in homology (p. 110, Proposition 3.2.11)."""
    for (lab, G, N, M, _) in lhs_cases():
        F = M.F
        Q, proj = G.quotient(N, 'Q')
        PG = Resolution(trivial(F, G), 3)
        PQ = Resolution(trivial(F, Q), 3)
        HG, _, _ = homology(PG, M, 3)
        # M_N = M / span((x - 1) M, x in N) as a G/N-module
        rel = hcat(F, M.dim, [M.act[x] - ident(F, M.dim) for x in N])
        Qm = Quot(F, M.dim, ident(F, M.dim), rel)
        MNc = Mod(F, Q, Qm.dim, {proj[g]: Qm.cls(M.act[g] * Qm.rep())
                                 for g in range(G.n)})
        piM = Qm.cls(ident(F, M.dim))
        HQ, _, _ = homology(PQ, MNc, 3)
        # the chain map P -> P' over F (as in the inflation)
        j0 = next(j for j in range(PQ.b[0])
                  if PQ.eps[0, j * Q.n + Q.e] != 0)
        a = PQ.eps[0, j0 * Q.n + Q.e]
        start = [mat(F, PQ.dim(0), 1, {(j0 * Q.n + Q.e, 0):
                                       PG.eps[0, i * G.n + G.e] / a})
                 for i in range(PG.b[0])]
        f = lift_chain_map(PG, PQ, start, 3, proj)
        pmaps = {}
        for n in (1, 2):
            A = mat(F, PQ.b[n] * MNc.dim, PG.b[n] * M.dim)
            for i in range(PG.b[n]):
                col = f[n].column(i * G.n + G.e)
                for j in range(PQ.b[n]):
                    v = {Q.inv[y]: col[j * Q.n + y] for y in range(Q.n)
                         if col[j * Q.n + y]}
                    if not v:
                        continue
                    B = MNc.lam(v) * piM
                    for (r, c), x in B.dict().items():
                        A[j * MNc.dim + r, i * M.dim + c] += x
            pmaps[n] = HQ[n].cls(A * HG[n].rep())
        dims, dd, cor, conj = restricted_chains(PG, M, N, 3)
        HN1 = Quot(F, dims[1], kernel_cols(dd[1]), dd[2])
        cmats = {g: conj(g) for g in range(G.n)}
        coinv = coinvariant_quotient(G, HN1, cmats, 1)
        corH = HG[1].cls(cor[1] * HN1.rep())
        # cor kills (g - 1) H_1(N, M): it factors through the coinvariants
        relc = hcat(F, HN1.dim, [HN1.cls(cmats[g][1] * HN1.rep()) -
                                 ident(F, HN1.dim) for g in G.gens])
        ok = (corH * relc).is_zero()
        corC = corH * coinv.rep()          # H_1(N, M)_(G/N) -> H_1(G, M)
        p1, p2 = pmaps[1], pmaps[2]
        ok &= (p1 * corC).is_zero() and rk(corC) == HG[1].dim - rk(p1)
        ok &= rk(p1) == HQ[1].dim
        # the place of d^2: Coker(H_2(G) -> H_2(G/N)) ~ Ker(cor)
        ok &= HQ[2].dim - rk(p2) == coinv.dim - rk(corC)
        check(ok, 'p. 110, Proposition 3.2.11: H_2(G, M) -> H_2(G/N, M_N) -> '
              'H_1(N, M)_(G/N) -> H_1(G, M) -> H_1(G/N, M_N) -> 0 is exact '
              '(%s)' % lab)


def ext_Z(relA, relB):
    """Ext^0, Ext^1 over ZZ of A = coker(relA) and B = coker(relB) (finitely
    generated, relA injective), as canonical forms: the homology of
    Hom(ZZ^c, B) -> Hom(ZZ^r, B) (transpose of relA)."""
    c, r = relA.nrows(), relA.ncols()
    k = relB.nrows()
    # Hom(ZZ^c, B) = B^c = ZZ^(c k) / L
    L0 = _matrix.identity(ZZ, c).tensor_product(relB)
    L1 = _matrix.identity(ZZ, r).tensor_product(relB)
    D = relA.transpose().tensor_product(_matrix.identity(ZZ, k))
    V0, V1 = ZZ ** (c * k), ZZ ** (r * k)
    big = D.augment(-L1)
    K = big.right_kernel_matrix()
    Kx = [v[:c * k] for v in K.rows()]
    e0 = canon((V0.span(Kx + L0.columns()) / V0.span(L0.columns()))
               .invariants())
    e1 = canon((V1 / V1.span(D.columns() + L1.columns())).invariants())
    return e0, e1


def canon(invs):
    rank, tors = 0, []
    for a in invs:
        a = int(a)
        if a == 0:
            rank += 1
        elif a > 1:
            for p, e in ZZ(a).factor():
                tors.append(int(p) ** e)
    return rank, sorted(tors)


def order(A):
    assert A[0] == 0
    out = 1
    for t in A[1]:
        out *= t
    return out


def section_3_5_ext():
    """The spectral sequence Ext^p_(R(G/N))(M_1, Ext^q_(RN)(M_2, M_3)) =>
    Ext^(p+q)_(RG)(M_1 (x)_R M_2, M_3) (p. 110)."""
    # over a field: modules M_1 of G/N, M_2, M_3 of G
    Gs = groups()
    F = GF(2)
    D8 = Gs['D8']
    V = [list(N) for N in normal_subgroups_of_order(D8, 4)
         if not any(D8.order[x] == 4 for x in N)][0]
    Q, proj = D8.quotient(V, 'C2')
    perm = perm_module_on_quotient(F, D8, V)
    cases = [('D8 > V4, M1 = F, M2 = M3 = F', D8, V, trivial(F, Q),
              trivial(F, D8), trivial(F, D8)),
             ('D8 > V4, M1 = F[C2], M2 = F, M3 = F', D8, V,
              perm_module_on_quotient(F, Q, [Q.e]), trivial(F, D8),
              trivial(F, D8)),
             ('D8 > V4, M1 = F, M2 = F[D8/V4], M3 = F', D8, V, trivial(F, Q),
              perm, trivial(F, D8)),
             ('D8 > V4, M1 = F, M2 = F, M3 = F[D8/V4]', D8, V, trivial(F, Q),
              trivial(F, D8), perm)]
    Q8 = Gs['Q8']
    Z = Q8.center()
    QQ8, _ = Q8.quotient(Z, 'V4')
    x0 = [g for g in range(QQ8.n) if g != QQ8.e][0]
    sub = QQ8.closure([x0])
    cases.append(('Q8 > Z, M1 = F[V4/C2], M2 = M3 = F', Q8, Z,
                  perm_module_on_quotient(F, QQ8, sub), trivial(F, Q8),
                  trivial(F, Q8)))
    top = 3
    for (lab, G, N, M1, M2, M3) in cases:
        Qg, proj = G.quotient(N, 'Q')
        # M_1 is given over the quotient Q of G.quotient: rebuild on Qg
        M1q = Mod(F, Qg, M1.dim, M1.act) if M1.G.n == Qg.n else None
        assert M1q is not None
        L = LHS(G, N, M3, top, M1=M1q, M2=M2)
        X = L.X
        # independent E_2: Ext^q_N(M_2, M_3) with the G/N-action, then
        # Ext^p_(G/N)(M_1, -)
        E2 = {}
        for q in range(top + 1):
            Zs = kernel_cols(L.Wdelta[q])
            Bs = L.Wdelta[q - 1] if q else mat(F, L.Wdims[0], 0)
            Hq = Quot(F, L.Wdims[q], Zs, Bs)
            Vq = Mod(F, Qg, Hq.dim, {proj[g]: Hq.cls(L.cmaps[g][q] *
                                                       Hq.rep())
                                     for g in range(G.n)})
            if Vq.dim:
                Hp, _, _ = cohomology(L.PQ, Vq, top - q + 1)
                for p in range(top - q + 1):
                    E2[(p, q)] = Hp[p].dim
            else:
                for p in range(top - q + 1):
                    E2[(p, q)] = 0
        check(all(X.Edim(2, p, p + q) == E2[(p, q)] for (p, q) in E2),
              'p. 110: E_2^(pq) = Ext^p_(G/N)(M_1, Ext^q_N(M_2, M_3)) (%s)'
              % lab)
        # abutment: Ext^n_G(M_1 (x) M_2, M_3), M_1 inflated
        T = Mod(F, G, M1q.dim * M2.dim, {g: kron(F, M1q.act[proj[g]],
                                                   M2.act[g])
                                          for g in range(G.n)})
        PT = Resolution(T, top + 1)
        HT, _, _ = cohomology(PT, M3, top + 1)
        R = X.rinf
        check(all(sum(X.Edim(R, p, n) for p in range(n + 1)) == HT[n].dim
                  for n in range(top + 1)), 'p. 110: the spectral sequence '
              'converges to Ext^n_G(M_1 (x) M_2, M_3) (over a field; %s)'
              % lab)
    # over R = ZZ, G = N = 1: M_1 = M_2 = M_3 = ZZ/2
    two = _matrix(ZZ, [[2]])
    e0, e1 = ext_Z(two, two)
    check(e0 == (0, [2]) and e1 == (0, [2]), 'Ext^0_ZZ(ZZ/2, ZZ/2) = '
          'Ext^1_ZZ(ZZ/2, ZZ/2) = ZZ/2, Ext^n = 0 for n >= 2')
    # E_2^(pq) = Ext^p(ZZ/2, Ext^q(ZZ/2, ZZ/2)) = ZZ/2 for p, q in {0, 1},
    # zero elsewhere; no differential d_r (r >= 2) can be non-zero, so the
    # printed statement would give |Ext^1(ZZ/2 (x) ZZ/2, ZZ/2)| = 4 and
    # Ext^2 != 0
    E2Z = {(p, q): order(ext_Z(two, two)[p]) for p in (0, 1) for q in (0, 1)}
    tensor = two                     # ZZ/2 (x) ZZ/2 = ZZ/2
    ab = ext_Z(tensor, two)
    refuted(E2Z[(0, 1)] * E2Z[(1, 0)] == order(ab[1]) and E2Z[(1, 1)] == 1,
            'p. 110 as printed, R = ZZ, G = N = 1, M_1 = M_2 = M_3 = ZZ/2: '
            'E_2 = E_infinity has |total degree 1| = %d and total degree 2 '
            '!= 0, while Ext^1 = ZZ/2, Ext^2 = 0'
            % (E2Z[(0, 1)] * E2Z[(1, 0)]))
    # corrected: M_1 = ZZ (projective over R): E_2 = Ext^0(ZZ, Ext^q) only
    zero_rel = _matrix(ZZ, 1, 0)
    e0z, e1z = ext_Z(zero_rel, two)          # Ext(ZZ, ZZ/2)
    check(e0z == (0, [2]) and e1z == (0, []), 'p. 110 corrected (M_1 = ZZ '
          'projective over R = ZZ): E_2^(0q) = Hom(ZZ, Ext^q(ZZ/2, ZZ/2)) = '
          'Ext^q(ZZ (x) ZZ/2, ZZ/2), E_2^(1q) = 0')


# ===========================================================================
# Section 3.6: the Kunneth spectral sequence
# ===========================================================================


def ab_tensor(A, B):
    (r, s), (r2, s2) = A, B
    tors = s * r2 + s2 * r
    for x in s:
        for y in s2:
            if ZZ(x).prime_divisors()[0] == ZZ(y).prime_divisors()[0]:
                tors.append(min(x, y))
    return r * r2, sorted(tors)


def ab_tor(A, B):
    tors = []
    for x in A[1]:
        for y in B[1]:
            if ZZ(x).prime_divisors()[0] == ZZ(y).prime_divisors()[0]:
                tors.append(min(x, y))
    return 0, sorted(tors)


def ab_sum(*As):
    return sum(A[0] for A in As), sorted(sum((A[1] for A in As), []))


def random_unimodular(n, rng):
    A = _matrix(ZZ, n, n, 1)
    for _ in range(3 * n):
        i, j = rng.randrange(n), rng.randrange(n)
        if i != j:
            A.add_multiple_of_row(i, j, rng.choice([-2, -1, 1, 2]))
    return A


def random_Z_complex(rng, top, pieces):
    basis = {s: 0 for s in range(top + 1)}
    edges = []
    for _ in range(pieces):
        s = rng.randrange(0, top + 1)
        if s == 0 or rng.random() < 0.25:
            basis[s] += 1
            continue
        m = rng.choice([1, 2, 3, 4, 6, 9, 0])
        if m == 0:
            basis[s] += 1
            basis[s - 1] += 1
            continue
        edges.append((s, basis[s], basis[s - 1], m))
        basis[s] += 1
        basis[s - 1] += 1
    d = {}
    for s in range(1, top + 1):
        A = _matrix(ZZ, basis[s - 1], basis[s], 0)
        for (t, i, j, m) in edges:
            if t == s:
                A[j, i] = m
        d[s] = A
    U = {s: random_unimodular(basis[s], rng) for s in basis}
    for s in d:
        d[s] = (U[s - 1] * d[s] * U[s].inverse()).change_ring(ZZ)
    return basis, d


def Z_homology(basis, d):
    from sage.all import ChainComplex
    out = {}
    for n in sorted(basis):
        rows = basis.get(n - 1, 0)
        A = d[n] if n in d else _matrix(ZZ, rows, basis[n], 0)
        B = d[n + 1] if n + 1 in d else _matrix(ZZ, basis[n], 0, 0)
        C = ChainComplex({n: A, n + 1: B}, degree=-1, base_ring=ZZ)
        out[n] = canon(C.homology(n).invariants())
    return out


def Z_tensor(bC, dC, bD, dD):
    keys = {}
    for s in bC:
        for t in bD:
            keys.setdefault(s + t, []).append((s, t))
    dims = {m: sum(bC[s] * bD[t] for (s, t) in ks) for m, ks in keys.items()}
    off = {}
    for m, ks in keys.items():
        o = 0
        for k in ks:
            off[k] = o
            o += bC[k[0]] * bD[k[1]]
    d = {}
    for m in keys:
        if m - 1 not in keys:
            continue
        A = _matrix(ZZ, dims[m - 1], dims[m], 0)
        for (s, t) in keys[m]:
            if s in dC and s - 1 in bC:
                B = dC[s].tensor_product(_matrix.identity(ZZ, bD[t]))
                o1, o0 = off[(s, t)], off[(s - 1, t)]
                A[o0:o0 + B.nrows(), o1:o1 + B.ncols()] += B
            if t in dD and t - 1 in bD:
                B = (-1) ** s * _matrix.identity(ZZ, bC[s]).tensor_product(
                    dD[t])
                o1, o0 = off[(s, t)], off[(s, t - 1)]
                A[o0:o0 + B.nrows(), o1:o1 + B.ncols()] += B
        d[m] = A
    return dims, d


def section_3_6():
    # over ZZ: Tor_p = 0 for p >= 2, so E^2 = E^infinity has the columns
    # p = 0, 1 and H_n(C (x) D) ~ E^2_(0n) + E^2_(1,n-1) (split over ZZ)
    for trial in range(30):
        bC, dC = random_Z_complex(RNG, RNG.choice([1, 2, 3]),
                                  RNG.randrange(2, 6))
        bD, dD = random_Z_complex(RNG, RNG.choice([1, 2]),
                                  RNG.randrange(2, 5))
        HC, HD = Z_homology(bC, dC), Z_homology(bD, dD)
        bT, dT = Z_tensor(bC, dC, bD, dD)
        HT = Z_homology(bT, dT)
        ok = True
        for n in HT:
            E0 = ab_sum(*[ab_tensor(HC[s], HD[n - s]) for s in HC
                          if n - s in HD])
            E1 = ab_sum(*[ab_tor(HC[s], HD[n - 1 - s]) for s in HC
                          if n - 1 - s in HD])
            ok &= HT[n] == ab_sum(E0, E1)
        check(ok, 'Theorem 3.6.3 over ZZ: E^2_(pq) = sum_(s+t=q) Tor_p(H_s(C),'
              ' H_t(D)) (p = 0, 1) gives H_n(C (x) D) (trial %d)' % trial)
    # over F_2[C_2] = F_2[x]/(x^2): E^2 has infinitely many columns; the
    # totals of E^2 bound H_n(C (x) D) (E^infinity is a subquotient)
    F = GF(2)
    G = Grp.from_sage(CyclicPermutationGroup(2), 'C2')
    for trial in range(6):
        ranks = [RNG.randrange(1, 3) for _ in range(3)]
        C = free_complex(F, G, ranks)
        D = free_complex(F, G, [RNG.randrange(1, 3) for _ in range(2)])
        HCm = {s: chain_hom_module(C, s) for s in range(len(C[0]))}
        HDm = {t: chain_hom_module(D, t) for t in range(len(D[0]))}
        Tdims, Td = comm_tensor(F, G, C, D)
        HT = {n: Tdims[n] - (rk(Td[n]) if n in Td else 0) -
              (rk(Td[n + 1]) if n + 1 in Td else 0) for n in Tdims}
        ok = True
        for n in HT:
            tot = 0
            for p in range(0, n + 1):
                q = n - p
                for s in HCm:
                    t = q - s
                    if t in HDm:
                        tot += tor_dim(F, G, HCm[s], HDm[t], p)
            ok &= tot >= HT[n]
        check(ok, 'Theorem 3.6.3 over F_2[C_2]: sum_(p+q=n) dim E^2_(pq) >= '
              'dim H_n(C (x) D) (trial %d)' % trial)


def free_complex(F, G, ranks):
    """A complex of free F[G]-modules (G abelian) with random maps."""
    n = G.n
    acts = [free_act(F, G, a) for a in ranks]
    dmaps = {}
    for s in range(1, len(ranks)):
        tgt_dim = ranks[s - 1] * n
        K = ident(F, tgt_dim) if s == 1 else kernel_cols(dmaps[s - 1])
        imgs = []
        for _ in range(ranks[s]):
            coef = mat(F, K.ncols(), 1, {(i, 0): F(RNG.randrange(
                F.characteristic())) for i in range(K.ncols())})
            imgs.append(K * coef)
        dmaps[s] = map_from_free(F, G, acts[s - 1], imgs)
    mods = [Mod(F, G, a * n, acts[i]) for i, a in enumerate(ranks)]
    return mods, dmaps, ranks


def chain_hom_module(C, s):
    mods, dmaps, _ = C
    F = mods[0].F
    M = mods[s]
    Zs = kernel_cols(dmaps[s]) if s in dmaps else ident(F, M.dim)
    Bs = dmaps[s + 1] if s + 1 in dmaps else mat(F, M.dim, 0)
    Qt = Quot(F, M.dim, Zs, Bs)
    return Mod(F, M.G, Qt.dim, {g: Qt.cls(M.act[g] * Qt.rep())
                                for g in range(M.G.n)})


def comm_tensor(F, G, C, D):
    """C (x)_Lambda D for complexes of free modules over a commutative group
    algebra: (C (x) D)_n = sum Lambda^(a_s b_t)."""
    (_, cd, ca), (_, dd, da) = C, D
    n = G.n
    keys = {}
    for s in range(len(ca)):
        for t in range(len(da)):
            keys.setdefault(s + t, []).append((s, t))
    # Lambda^a (x)_Lambda Lambda^b = Lambda^(a b), basis (i, j, h)
    dims = {m: sum(ca[s] * da[t] * n for (s, t) in ks)
            for m, ks in keys.items()}
    off = {}
    for m, ks in keys.items():
        o = 0
        for k in ks:
            off[k] = o
            o += ca[k[0]] * da[k[1]] * n

    def lmat(A, a_src, a_tgt):
        L = {}
        for j in range(a_src):
            col = A.column(j * n + G.e)
            for i in range(a_tgt):
                v = {h: col[i * n + h] for h in range(n) if col[i * n + h]}
                if v:
                    L[(i, j)] = v
        return L

    d = {}
    for m in keys:
        if m - 1 not in keys:
            continue
        A = mat(F, dims[m - 1], dims[m])
        for (s, t) in keys[m]:
            if s in cd:
                L = lmat(cd[s], ca[s], ca[s - 1])
                for (i, j), v in L.items():
                    for k in range(da[t]):
                        # e_j (x) f_k h |-> e_i (x) f_k (v h)
                        for h in range(n):
                            for g, c in v.items():
                                r = off[(s - 1, t)] + (i * da[t] + k) * n + \
                                    G.mul[g][h]
                                cc = off[(s, t)] + (j * da[t] + k) * n + h
                                A[r, cc] += c
            if t in dd:
                L = lmat(dd[t], da[t], da[t - 1])
                sign = 1 if s % 2 == 0 else -1
                for (i, j), v in L.items():
                    for k in range(ca[s]):
                        for h in range(n):
                            for g, c in v.items():
                                r = off[(s, t - 1)] + (k * da[t - 1] + i) * \
                                    n + G.mul[g][h]
                                cc = off[(s, t)] + (k * da[t] + j) * n + h
                                A[r, cc] += sign * c
        d[m] = A
    return dims, d


def tor_dim(F, G, A, B, p):
    """dim Tor_p^Lambda(A, B) for Lambda = F[G] commutative: H_p(P (x) B), P a
    free resolution of A."""
    if A.dim == 0 or B.dim == 0:
        return 0
    P = Resolution(A, p + 1)
    dims = {k: P.b[k] * B.dim for k in range(p + 2)}

    def dmat(k):
        L = P.lam_entries(k)
        M = mat(F, dims[k - 1], dims[k])
        for (j, i), v in L.items():
            Bm = B.lam(v)
            for (r, c), x in Bm.dict().items():
                M[j * B.dim + r, i * B.dim + c] += x
        return M
    out = dims[p] - (rk(dmat(p)) if p >= 1 else 0) - rk(dmat(p + 1))
    return out


# ===========================================================================
# Section 3.7: the sign in the total differential, the Eilenberg-Moore
# spectral sequence of central extensions, H^*(K(Z/2, 2); F_2)
# ===========================================================================


def section_3_7_sign():
    """(d_0 + d_1) (x) 1 + (-1)^m 1 (x) d_N on P^(**) (x) N squares to zero
    for m the total degree p + s of the factor in P^(ps), not for m = p or
    m = s."""
    F = GF(3)
    for trial in range(4):
        # P = A (x) B with d_1 = d_A (x) 1, d_0 = (-1)^a 1 (x) d_B
        A = random_cochain(F, [2, 3, 2])
        B = random_cochain(F, [2, 2, 2])
        N = random_cochain(F, [2, 3, 1])
        res = {}
        for name in ('total', 'p', 's'):
            res[name] = sign_test(F, A, B, N, name)
        check(res['total'], 'p. 113: the total differential (d_0 + d_1) (x) 1'
              ' + (-1)^m 1 (x) d_N squares to zero with m = p + s, the total '
              'degree in P^(**) (trial %d)' % trial)
        refuted(res['p'], 'p. 113 with m = p (homological degree only)')
        refuted(res['s'], 'p. 113 with m = s (internal degree only)')


def random_cochain(F, dims):
    """A cochain complex in degrees 0..k-1 with d o d = 0 and d != 0."""
    while True:
        d = {}
        ok = True
        for i in range(len(dims) - 1):
            K = ident(F, dims[i]) if i == 0 else kernel_cols(d[i - 1])
            if K.ncols() == 0:
                ok = False
                break
            R = mat(F, dims[i + 1], K.ncols(), {
                (a, b): F(RNG.randrange(3)) for a in range(dims[i + 1])
                for b in range(K.ncols())})
            # d_i vanishes on the image of d_(i-1): d_i = R pi, pi a
            # projection killing Im d_(i-1)
            if i == 0:
                d[i] = R
            else:
                Im = d[i - 1]
                Qt = Quot(F, dims[i], ident(F, dims[i]), Im)
                C = Qt.cls(ident(F, dims[i]))
                R = mat(F, dims[i + 1], C.nrows(), {
                    (a, b): F(RNG.randrange(3)) for a in range(dims[i + 1])
                    for b in range(C.nrows())})
                d[i] = R * C
            ok &= not d[i].is_zero()
        if ok:
            return dims, d


def sign_test(F, A, B, N, which):
    (da_, dA), (db_, dB), (dn_, dN) = A, B, N
    # basis: (a, b, c) degrees; element of P^(ps) with p = a, s = b
    cells = [(a, b, c) for a in range(len(da_)) for b in range(len(db_))
             for c in range(len(dn_))]
    dim = {x: da_[x[0]] * db_[x[1]] * dn_[x[2]] for x in cells}
    off, o = {}, 0
    for x in cells:
        off[x] = o
        o += dim[x]
    tot = o
    D = mat(F, tot, tot)
    for (a, b, c) in cells:
        src = off[(a, b, c)]
        Ia, Ib, Ic = ident(F, da_[a]), ident(F, db_[b]), ident(F, dn_[c])
        parts = []
        if a in dA:
            parts.append(((a + 1, b, c), kron(F, kron(F, dA[a], Ib), Ic)))
        if b in dB:
            parts.append(((a, b + 1, c), (-1) ** a * kron(F, kron(F, Ia,
                                                                dB[b]), Ic)))
        if c in dN:
            m = {'total': a + b, 'p': a, 's': b}[which]
            parts.append(((a, b, c + 1), (-1) ** m * kron(F, kron(F, Ia, Ib),
                                                          dN[c])))
        for tgt, M in parts:
            for (r, cc), x in M.dict().items():
                D[off[tgt] + r, src + cc] += x
    return (D * D).is_zero()


def extension_group(r, B, name):
    """The central extension 1 -> Z/2 -> E -> (Z/2)^r -> 1 with the bilinear
    cocycle B (an r x r 0/1 matrix): (u, z)(v, w) = (u + v, z + w + B(u, v)).
    Its class in H^2((Z/2)^r; F_2) = F_2[x_1, ..., x_r]_2 is
    sum B_ij x_i x_j."""
    els = [(u, z) for u in itertools.product((0, 1), repeat=r)
           for z in (0, 1)]
    ix = {e: i for i, e in enumerate(els)}

    def mul(a, b):
        (u, z), (v, w) = a, b
        s = sum(B[i][j] * u[i] * v[j] for i in range(r) for j in range(r))
        return (tuple((u[i] + v[i]) % 2 for i in range(r)), (z + w + s) % 2)
    table = [[ix[mul(a, b)] for b in els] for a in els]
    e = ix[((0,) * r, 0)]
    gens = [ix[(tuple(1 if k == i else 0 for k in range(r)), 0)]
            for i in range(r)] + [ix[((0,) * r, 1)]]
    return Grp(len(els), table, e, gens, name)


def sq_hom(i, f, R):
    """Sq^i f for f homogeneous in F_2[x_1..x_r]: the part of degree
    deg f + i of Sq(f), Sq the ring map x |-> x + x^2 (Cartan formula)."""
    T = f.subs({v: v + v ** 2 for v in R.gens()})
    d = f.degree()
    out = R(0)
    for c, m in zip(T.coefficients(), T.monomials()):
        if m.degree() == d + i:
            out += c * m
    return out


def section_3_7_emss():
    """Tor_(H^*(K(Z/2,2)))(F_2, H^*(G/Z)) => H^*(G) for the central
    extensions of (Z/2)^r by Z/2 (r = 1, 2) and some of (Z/2)^3."""
    F = GF(2)
    # H^*(K(Z/2,2); F_2) = F_2[u_0, u_1, ...], u_(i+1) = Sq^(2^i) u_i
    for r, top in ((1, 7), (2, 6), (3, 4)):
        R = PolynomialRing(F, ['x%d' % i for i in range(r)])
        xs = R.gens()
        if r == 1:
            Bs = [[[0]], [[1]]]
        elif r == 2:
            Bs = []
            for b11, b12, b22 in itertools.product((0, 1), repeat=3):
                Bs.append([[b11, b12], [0, b22]])
        else:
            Bs = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                  [[1, 1, 0], [0, 1, 0], [0, 0, 0]],
                  [[0, 1, 0], [0, 0, 0], [0, 0, 1]],
                  [[1, 0, 0], [0, 0, 1], [0, 0, 0]]]
        for B in Bs:
            q = sum(B[i][j] * xs[i] * xs[j] for i in range(r)
                    for j in range(r))
            q = R(q)
            images = [q]
            while 2 ** len(images) <= top + 1:
                i = len(images) - 1
                images.append(sq_hom(2 ** i, images[-1], R) if images[-1]
                              else R(0))
            # degree bookkeeping: u_i has degree 2^i + 1
            check(all((im == 0) or im.degree() == 2 ** i + 1
                       for i, im in enumerate(images)), 'u_i in degree '
                  '2^i + 1 (images %s)' % images)
            # the Koszul complex needs homogeneous images of the right
            # degree also when zero
            tor = koszul_tor_totals_deg(R, images, top)
            G = extension_group(r, B, 'E')
            inv = sum(1 for g in range(G.n) if G.order[g] == 2)
            P = Resolution(trivial(F, G), top + 1)
            H, _, _ = cohomology(P, trivial(F, G), top + 1)
            hd = [H[n].dim for n in range(top + 1)]
            tot = [tor[n] for n in range(top + 1)]
            check(all(t >= h for t, h in zip(tot, hd)), 'Section 3.7: the '
                  'Eilenberg-Moore E_2 = Tor_(H^*(K(Z/2,2)))(F_2, '
                  'H^*((Z/2)^%d)) bounds H^*(G) (class %s, |G| = %d, %d '
                  'involutions)'
                  % (r, q, G.n, inv))
            check(tot == hd, 'Section 3.7: the Eilenberg-Moore spectral '
                  'sequence collapses for the central extension of (Z/2)^%d '
                  'by Z/2 with class %s (%d involutions): totals %s = dim '
                  'H^n(G; F_2), n <= %d' % (r, q, inv, tot, top))


def koszul_tor_totals_deg(R, images, top):
    """As koszul_tor_totals, with the generator degrees 2^i + 1 given even
    when an image is zero."""
    F = GF(2)
    m = len(images)
    tot_e = [2 ** i for i in range(m)]
    subsets = [I for s in range(m + 1) for I in itertools.combinations(
        range(m), s)]

    def basis(k):
        if k < 0:
            return []
        return list(R.monomials_of_degree(k)) if k else [R(1)]

    def chain(n):
        cells = []
        for I in subsets:
            k = n - sum(tot_e[i] for i in I)
            for mono in basis(k):
                cells.append((I, mono))
        return cells

    def dmat(n):
        src, tgt = chain(n), chain(n + 1)
        tix = {c: a for a, c in enumerate(tgt)}
        A = mat(F, len(tgt), len(src))
        for b, (I, mono) in enumerate(src):
            for i in I:
                J = tuple(x for x in I if x != i)
                f = images[i] * mono
                if f == 0:
                    continue
                for c, mm in zip(f.coefficients(), f.monomials()):
                    A[tix[(J, mm)], b] += c
        return A, len(src)
    mats = {n: dmat(n) for n in range(-1, top + 1)}
    return {n: mats[n][1] - rk(mats[n][0]) - rk(mats[n - 1][0])
            for n in range(0, top + 1)}


def section_3_7_kz2():
    """p. 113: H^*(K(Z/2, 2); F_2) = F_2[u_0, u_1, ...], deg u_i = 2^i + 1."""
    A = SteenrodAlgebra(2, basis='admissible')
    top = 64
    found = []
    for d in range(0, top + 1):
        for b in A.basis(d):
            for I in b.support():
                I = tuple(I)
                exc = (I[0] - sum(I[1:])) if I else 0
                if exc < 2:
                    found.append(I)
    expect = [tuple(2 ** j for j in range(k - 1, -1, -1)) for k in range(0, 7)]
    check(sorted(found) == sorted(expect), 'p. 113 (Serre): the admissible '
          'Sq^I with excess < 2 in degrees <= 64 are Sq^(2^(k-1)) ... Sq^2 '
          'Sq^1, so H^*(K(Z/2,2); F_2) is polynomial on u_k = Sq^(2^(k-1)) '
          '... Sq^1 u_0')
    check(all(sum(I) + 2 == 2 ** len(I) + 1 for I in found), 'p. 113: '
          'deg u_i = 2^i + 1')
    # the spectral sequence of K(Z/2,1) -> P K(Z/2,2) -> K(Z/2,2): the
    # multiplicative model with E_2 = F_2[u_0, u_1, ...] (x) F_2[x], the
    # simple system x^(2^i) transgressing to u_i, converges to F_2 in
    # degree 0 (filtration by the degree in the u's)
    F = GF(2)
    T = 20
    m = 0
    while 2 ** (m + 1) <= T + 1:
        m += 1
    m += 1                                     # u_0 .. u_(m-1), y_0 .. y_(m-1)
    ud = [2 ** i + 1 for i in range(m)]
    yd = [2 ** i for i in range(m)]
    cells = {}
    for n in range(0, T + 2):
        cells[n] = []
    # monomials u^a y^eps with total degree <= T + 1
    def rec(i, deg, p, a, eps):
        if i == m:
            if deg <= T + 1:
                cells[deg].append((tuple(a), tuple(eps), p))
            return
        for e in (0, 1):
            k = 0
            while deg + e * yd[i] + k * ud[i] <= T + 1:
                rec(i + 1, deg + e * yd[i] + k * ud[i], p + k * ud[i],
                    a + [k], eps + [e])
                k += 1
    rec(0, 0, 0, [], [])
    pos = {n: {(c[0], c[1]): j for j, c in enumerate(cells[n])}
           for n in cells}
    filt = {n: [c[2] for c in cells[n]] for n in cells}
    d = {}
    for n in range(0, T + 1):
        A = mat(F, len(cells[n + 1]), len(cells[n]))
        for j, (a, eps, p) in enumerate(cells[n]):
            for i in range(m):
                if eps[i]:
                    a2 = list(a)
                    a2[i] += 1
                    e2 = list(eps)
                    e2[i] = 0
                    A[pos[n + 1][(tuple(a2), tuple(e2))], j] += 1
        d[n] = A
    X = Filtered(F, filt, d)
    Rinf = X.rinf
    einf = [sum(X.Edim(Rinf, p, n) for p in range(n + 1))
            for n in range(0, T + 1)]
    check(einf == [1] + [0] * T, 'p. 113: the path fibration spectral '
          'sequence with E_2 = F_2[u_i] (x) F_2[x] converges to F_2 in '
          'degree 0 (model through degree %d)' % T)
    # E_2^(pq) = H^p(K(Z/2,2)) (x) H^q(K(Z/2,1)) with dim H^q(K(Z/2,1)) = 1
    Rp = PolynomialRing(QQ, 't')
    tvar = Rp.gen()
    ser = 1
    for i in range(m):
        ser *= sum(tvar ** (k * ud[i]) for k in range(T // ud[i] + 2))
    hp = [ser[k] for k in range(T + 1)]
    ok = all(X.Edim(2, p, p + q) == hp[p] for p in range(0, T + 1)
             for q in range(0, T + 1 - p))
    check(ok, 'the model has E_2^(pq) = H^p(K(Z/2,2)) (x) H^q(K(Z/2,1)), '
          'dim H^q(K(Z/2,1); F_2) = 1')
    nz = sorted(set(r for r in range(2, Rinf) for p in range(T + 1)
                    for q in range(T + 1 - p) if X.dr_rank(r, p, p + q)))
    check(nz == [2 ** i + 1 for i in range(m) if 2 ** i + 1 <= T],
          'the non-zero differentials are d_(2^i + 1), the transgressions '
          'x^(2^i) |-> u_i (%s)' % nz)


# ===========================================================================
# Section 3.8: the Atiyah spectral sequence
# ===========================================================================


def section_3_8():
    # even differentials vanish when every other row is zero (p. 114)
    ok = True
    for r in range(2, 30):
        for q in range(0, 30, 2):
            target_row = q - r + 1
            ok &= (target_row % 2 == 1) == (r % 2 == 0)
    check(ok, 'p. 114: with rows q odd zero, d_r : E_r^(pq) -> '
          'E_r^(p+r, q-r+1) lands in an odd row exactly when r is even, so '
          'd_(2n) = 0; d_3, d_5, ... raise the degree p by 3, 5, ...')
    # cyclic groups: H^*(Z/n, ZZ) = ZZ, 0, ZZ/n, 0, ZZ/n, ... (periodic
    # resolution), so the spectral sequence collapses; the I-adic quotients
    # of R(Z/n) = ZZ[t]/(t^n - 1) have the same orders
    from sage.all import ChainComplex
    for n in range(2, 9):
        top = 8
        # cochain complex Hom_G(P, ZZ) = ZZ --0--> ZZ --n--> ZZ --0--> ...
        dif = {k: _matrix(ZZ, 1, 1, [0 if k % 2 == 0 else n])
               for k in range(0, top + 1)}
        C = ChainComplex(dif, degree=1, base_ring=ZZ)
        Hs = [canon(C.homology(k).invariants()) for k in range(0, top)]
        expect = [(1, [])] + [((0, []) if k % 2 else canon([n]))
                              for k in range(1, top)]
        check(Hs == expect, 'Section 3.8, exercise: H^*(Z/%d, ZZ) = ZZ, 0, '
              'Z/%d, 0, ... (no odd cohomology: all d_r vanish)' % (n, n))
        # I^k / I^(k+1) in ZZ[t]/(t^n - 1), basis 1, t, ..., t^(n-1)
        V = ZZ ** n

        def mult_by_t_minus_1(v):
            w = [0] * n
            for i in range(n):
                w[(i + 1) % n] += v[i]
                w[i] -= v[i]
            return V(w)
        Ik = [V.basis()]
        for k in range(1, 6):
            Ik.append([mult_by_t_minus_1(v) for v in Ik[-1]])
        orders = []
        for k in range(1, 5):
            Q = V.span(Ik[k]) / V.span(Ik[k + 1])
            orders.append(canon(Q.invariants()))
        check(all(o == canon([n]) for o in orders), 'Section 3.8: I^k / '
              'I^(k+1) ~ Z/%d = H^(2k)(Z/%d, ZZ) for R(Z/%d), k = 1..4'
              % (n, n, n))


# ===========================================================================
# Section 3.9: products
# ===========================================================================


class GCA:
    """A free graded commutative algebra over F on generators of given
    degrees and filtration weights, truncated at degree top + 1, with a
    derivation d given on the generators (d(x y) = d(x) y + (-1)^|x| x d(y)).
    Monomials: exponent tuples (odd generators with exponent <= 1)."""

    def __init__(self, F, degs, wts, dgen, top):
        self.F, self.degs, self.wts, self.top = F, degs, wts, top
        self.k = len(degs)
        mons = {n: [] for n in range(top + 2)}

        def rec(i, e, deg):
            if i == self.k:
                mons[deg].append(tuple(e))
                return
            mx = 1 if degs[i] % 2 else top + 1
            for a in range(mx + 1):
                if deg + a * degs[i] > top + 1:
                    break
                rec(i + 1, e + [a], deg + a * degs[i])
        rec(0, [], 0)
        self.mons = mons
        self.pos = {n: {m: j for j, m in enumerate(ms)}
                    for n, ms in mons.items()}
        self.dgen = dgen          # generator index -> dict monomial -> coef

    def deg(self, m):
        return sum(a * d for a, d in zip(m, self.degs))

    def wt(self, m):
        return sum(a * w for a, w in zip(m, self.wts))

    def mul_mono(self, m1, m2):
        """m1 m2 = sign * monomial (or None if zero)."""
        sign = 1
        res = list(m1)
        # move each odd generator of m2 past the odd generators of m1 with
        # larger index
        for j in range(self.k):
            if m2[j] == 0:
                continue
            if self.degs[j] % 2:
                if m1[j]:
                    return 0, None
                # m2's generators before j already placed; count odd
                # generators of m1 with index > j
                c = sum(m1[i] for i in range(j + 1, self.k)
                        if self.degs[i] % 2)
                sign *= (-1) ** c
            res[j] += m2[j]
        return sign, tuple(res)

    def mul(self, x, y):
        out = {}
        for m1, c1 in x.items():
            for m2, c2 in y.items():
                s, m = self.mul_mono(m1, m2)
                if m is None or self.deg(m) > self.top + 1:
                    continue
                out[m] = out.get(m, self.F(0)) + s * c1 * c2
        return {m: c for m, c in out.items() if c}

    def d_mono(self, m):
        """d of the ordered monomial x_0^a_0 x_1^a_1 ...: the sum over i of
        (-1)^deg(prefix) prefix d(x_i^a_i) suffix, d(x^a) = a x^(a-1) d(x)
        for x even."""
        out = {}
        F, k = self.F, self.k
        for i in range(k):
            a = m[i]
            if a == 0 or i not in self.dgen:
                continue
            before = tuple(m[j] if j < i else 0 for j in range(k))
            after = tuple(m[j] if j > i else 0 for j in range(k))
            sgn = (-1) ** (self.deg(before) % 2)
            if self.degs[i] % 2 == 0:
                dp = self.mul({tuple(a - 1 if j == i else 0
                                     for j in range(k)): F(a)}, self.dgen[i])
            else:
                dp = dict(self.dgen[i])
            t = self.mul(self.mul({before: F(sgn)}, dp), {after: F(1)})
            for mm, c in t.items():
                out[mm] = out.get(mm, F(0)) + c
        return {mm: c for mm, c in out.items() if c}

    def vec(self, x, n):
        v = mat(self.F, len(self.mons[n]), 1)
        for m, c in x.items():
            v[self.pos[n][m], 0] += c
        return v

    def elem(self, v, n):
        return {self.mons[n][j]: v[j, 0] for j in range(v.nrows())
                if v[j, 0]}

    def filtered(self):
        d = {}
        for n in range(self.top + 1):
            A = mat(self.F, len(self.mons[n + 1]), len(self.mons[n]))
            for j, m in enumerate(self.mons[n]):
                for mm, c in self.d_mono(m).items():
                    if self.deg(mm) <= self.top + 1:
                        A[self.pos[n + 1][mm], j] += c
            d[n] = A
        filt = {n: [self.wt(m) for m in self.mons[n]]
                for n in range(self.top + 2)}
        return Filtered(self.F, filt, d)


def section_3_9():
    F = GF(3)
    models = [
        # a (1, wt 1), b (2, wt 2), y (1, wt 0), z (2, wt 0); d y = b
        ('d y = b (a model of Z/9 > Z/3 at p = 3)', (1, 2, 1, 2),
         (1, 2, 0, 0), {2: {(0, 1, 0, 0): F(1)}}),
        # a (1, wt 1), b (2, wt 2), w (3, wt 0); d w = b^2: a d_4
        ('d w = b^2 (a d_4)', (1, 2, 3), (1, 2, 0), {2: {(0, 2, 0): F(1)}}),
        # a (1, wt 1), c (2, wt 1), b (2, wt 2), y (1, wt 0): d y = c + b
        ('d y = c + b', (1, 2, 2, 1), (1, 1, 2, 0),
         {3: {(0, 1, 0, 0): F(1), (0, 0, 1, 0): F(1)}}),
    ]
    top = 7
    for (lab, degs, wts, dgen) in models:
        A = GCA(F, degs, wts, dgen, top)
        X = A.filtered()                      # asserts d o d = 0, filtration
        # Leibniz on the chain level (Definition 3.9.4: d(xy) = d(x) y +
        # (-1)^deg(x) x d(y)), for all pairs of monomials of total degree
        # <= top
        ok = True
        for n1 in range(top + 1):
            for n2 in range(top + 1 - n1):
                for m1 in A.mons[n1]:
                    for m2 in A.mons[n2]:
                        x, y = {m1: F(1)}, {m2: F(1)}
                        lhs = {}
                        for mm, c in A.mul(x, y).items():
                            for m3, c3 in A.d_mono(mm).items():
                                lhs[m3] = lhs.get(m3, F(0)) + c * c3
                        rhs = A.mul(A.d_mono(m1), y)
                        for mm, c in A.mul(x, A.d_mono(m2)).items():
                            rhs[mm] = rhs.get(mm, F(0)) + \
                                (-1) ** (n1 % 2) * c
                        lhs = {k: v for k, v in lhs.items() if v}
                        rhs = {k: v for k, v in rhs.items() if v}
                        ok &= lhs == rhs
        check(ok, 'Definition 3.9.4: the model is a filtered complex with '
              'pairing, d(xy) = d(x) y + (-1)^deg(x) x d(y) (%s)' % lab)
        R = X.rinf
        okZ, okB, okL, ok_sign = True, True, True, False

        def sample(M, k=3):
            """k random elements of the column span (and the columns
            themselves when few)."""
            if M.ncols() == 0:
                return []
            out = [M.matrix_from_columns([i]) for i in range(min(2,
                                                                M.ncols()))]
            for _ in range(k):
                c = mat(F, M.ncols(), 1, {(i, 0): F(RNG.randrange(3))
                                          for i in range(M.ncols())})
                out.append(M * c)
            return out
        for r in range(1, R):
            for n1 in range(0, top):
                for n2 in range(0, top - n1):
                    for p1 in range(0, n1 + 1):
                        for p2 in range(0, n2 + 1):
                            Z1, Z2 = X.Z(r, p1, n1), X.Z(r, p2, n2)
                            B1, B2 = X.B(r, p1, n1), X.B(r, p2, n2)
                            Zt = X.Z(r, p1 + p2, n1 + n2)
                            Bt = X.B(r, p1 + p2, n1 + n2)
                            Bdt = X.B(r, p1 + p2 + r, n1 + n2 + 1)
                            for u in sample(Z1):
                                x = A.elem(u, n1)
                                for w in sample(Z2):
                                    y = A.elem(w, n2)
                                    v = A.vec(A.mul(x, y), n1 + n2)
                                    okZ &= in_span(Zt, v)
                                    dx = A.elem(X.dm(n1) * u, n1 + 1)
                                    dy = A.elem(X.dm(n2) * w, n2 + 1)
                                    lhs = X.dm(n1 + n2) * v
                                    t1 = A.vec(A.mul(dx, y), n1 + n2 + 1)
                                    t2 = A.vec(A.mul(x, dy), n1 + n2 + 1)
                                    s = (-1) ** n1
                                    okL &= in_span(Bdt, lhs - t1 - s * t2)
                                    if n1 % 2 and not in_span(
                                            Bdt, lhs - t1 + s * t2):
                                        ok_sign = True
                                for w in sample(B2):
                                    y = A.elem(w, n2)
                                    okB &= in_span(Bt, A.vec(A.mul(x, y),
                                                             n1 + n2))
                            for u in sample(B1):
                                x = A.elem(u, n1)
                                for w in sample(Z2):
                                    y = A.elem(w, n2)
                                    okB &= in_span(Bt, A.vec(A.mul(x, y),
                                                             n1 + n2))
        check(okZ and okB, 'p. 116: Z_n Z\'_n <= Z\'\'_n, Z_n B\'_n and '
              'B_n Z\'_n <= B\'\'_n, so E_n has a product with [x][y] = [xy] '
              '(%s)' % lab)
        check(okL, 'Theorem 3.9.3: d_n(x y) = d_n(x) y + (-1)^(p+q) x d_n(y)'
              ' in E_n (%s)' % lab)
        if lab.startswith('d y = b'):
            check(ok_sign, 'Theorem 3.9.3: the sign (-1)^(p+q) matters (the '
                  'other sign fails for some x of odd degree; %s)' % lab)


def section_3_9_groups():
    """Theorem 3.9.3 in the LHS spectral sequence of central extensions by
    Z/2 with trivial action: E_2 = H^*(G/Z) (x) F_2[z], d_2(z) = c (the
    class), so d_2(f z^q) = q f c z^(q-1): rank of d_2 on E_2^(pq) is
    dim H^p(G/Z) for q odd (c non-zero, multiplication by c injective on a
    polynomial ring), 0 for q even."""
    Gs = groups()
    F = GF(2)
    cases = [('C4 > C2', Gs['C4'],
              normal_subgroups_of_order(Gs['C4'], 2)[0]),
             ('Q8 > Z', Gs['Q8'], Gs['Q8'].center()),
             ('D8 > Z', Gs['D8'], Gs['D8'].center()),
             ('V4 > C2', Gs['V4'], normal_subgroups_of_order(Gs['V4'], 2)[0])]
    C42 = Gs['C4xC2']
    for N in normal_subgroups_of_order(C42, 2):
        cases.append(('C4xC2 > C2', C42, N))
    for B, nm in (([[1, 0, 0], [0, 0, 1], [0, 0, 0]], 'E(x0^2 + x1 x2)'),
                  ([[1, 1, 0], [0, 1, 0], [0, 0, 0]], 'Q8 x C2')):
        Gx = extension_group(3, B, nm)
        cases.append((nm + ' > Z', Gx, [Gx.e, Gx.gens[-1]]))
    for case in cases:
        lab, G, N = case
        N = list(N)
        Q, _ = G.quotient(N, 'Q')
        if any(Q.order[x] > 2 for x in range(Q.n)):
            continue
        r = 0
        while 2 ** r < Q.n:
            r += 1
        L = LHS(G, list(N), trivial(F, G), 4)
        X = L.X
        c_nonzero = X.dr_rank(2, 0, 1) == 1
        ok = True
        for p in range(0, 4):
            for q in range(0, 4 - p):
                hp = binomial(p + r - 1, r - 1)          # dim H^p((Z/2)^r)
                pred = hp if (q % 2 == 1 and c_nonzero) else 0
                ok &= X.dr_rank(2, p, p + q) == pred
        check(ok, 'Theorem 3.9.3 (d_2 a derivation of E_2 = H^*(G/N) (x) '
              'H^*(N)): rank d_2 on E_2^(pq) = [q odd] dim H^p(G/N) when '
              'd_2(z) != 0 (%s, d_2 z %s 0)' % (lab, '!=' if c_nonzero
                                                  else '='))


# ===========================================================================
# Section 3.10: finite generation
# ===========================================================================


def section_3_10():
    # H^*(BU; R) -> H^*(BU(n); R) is onto: c_i |-> c_i (i <= n), 0 (i > n)
    for nn in range(1, 5):
        for mm in range(nn, nn + 3):
            Rm = PolynomialRing(ZZ, ['t%d' % i for i in range(mm)])
            ts = Rm.gens()
            ok = True
            for i in range(1, mm + 1):
                e = sum(prod_(c) for c in itertools.combinations(ts, i))
                e_res = e.subs({ts[j]: 0 for j in range(nn, mm)})
                if i <= nn:
                    e_n = sum(prod_(c) for c in itertools.combinations(
                        ts[:nn], i))
                    ok &= e_res == e_n
                else:
                    ok &= e_res == 0
            check(ok, 'Theorem 3.10.1 ("over H^*(BU; R)"): restriction along '
                  'BU(%d) -> BU(%d) sends c_i to c_i (i <= %d) and to 0 '
                  '(i > %d), so H^*(BU(%d)) -> H^*(BU(%d)) is onto'
                  % (nn, mm, nn, nn, mm, nn))
    # Corollary 3.10.2: periodicity classes (Yoneda products)
    Gs = groups()
    cases = [('C2', Gs['C2'], GF(2), 1), ('C4', Gs['C4'], GF(2), 2),
             ('C3', Grp.from_sage(CyclicPermutationGroup(3), 'C3'), GF(3), 2),
             ('C5', Grp.from_sage(CyclicPermutationGroup(5), 'C5'), GF(5), 2),
             ('Q8', Gs['Q8'], GF(2), 4), ('S3', Gs['S3'], GF(3), 4)]
    for (lab, G, F, deg) in cases:
        top = 9
        P = Resolution(trivial(F, G), top + 1)
        H, _, _ = cohomology(P, trivial(F, G), top + 1)
        check(H[deg].dim == 1, 'H^%d(%s; F_%d) is one dimensional'
              % (deg, lab, F.characteristic()))
        rep = H[deg].rep()
        cocycle = [rep[i, 0] for i in range(rep.nrows())]
        ok = True
        for k in range(0, top - deg + 1):
            A = cup_matrix(P, H, cocycle, deg, k)
            ok &= A.nrows() == A.ncols() == H[k].dim and rk(A) == H[k].dim
        check(ok, 'Corollary 3.10.2: multiplication by the non-zero class '
              'of degree %d (a Chern class of a faithful representation) is '
              'an isomorphism H^k(%s) -> H^(k+%d)(%s), k <= %d, so '
              'H^*(%s; F_%d) is generated over it by degrees < %d'
              % (deg, lab, deg, lab, top - deg, lab, F.characteristic(),
                 deg))
    # Q8: the class of degree 4 restricts non-trivially to each cyclic
    # subgroup of order 4 (as c_2(rho) does: c_1(chi) c_1(chi^-1) = -u^2);
    # S3 at p = 3: to the Sylow subgroup
    for (lab, G, F, subs) in (('Q8', Gs['Q8'], GF(2), 4),
                              ('S3', Gs['S3'], GF(3), 3)):
        P = Resolution(trivial(F, G), 5)
        H, _, _ = cohomology(P, trivial(F, G), 5)
        for S in [s for s in normal_or_all_subgroups(G, subs)]:
            dims, delta, res, _, _, _ = restricted_cochains(
                P, trivial(F, G), S, 5)
            Zs = kernel_cols(delta[4])
            HS = Quot(F, dims[4], Zs, delta[3])
            r4 = HS.cls(res[4] * H[4].rep())
            check(rk(r4) == 1, 'Corollary 3.10.2: the degree 4 class of %s '
                  'restricts non-trivially to a cyclic subgroup of order %d'
                  % (lab, subs))
    # elementary abelian 2-groups: H^* = F_2[x_1..x_r]; Chern classes of a
    # sum of characters chi_v (v in the dual) have mod 2 reductions the
    # elementary symmetric functions in the squares v(x)^2; the quotient by
    # them is finite iff the characters separate the group (faithful)
    for r, chars, faithful in ((2, [(1, 0), (0, 1)], True),
                               (2, [(1, 0), (1, 1)], True),
                               (2, [(1, 1), (1, 1)], False),
                               (3, [(1, 0, 0), (0, 1, 0), (0, 0, 1)], True),
                               (3, [(1, 0, 0), (0, 1, 0), (1, 1, 1)], True),
                               (3, [(1, 0, 0), (0, 1, 0), (1, 1, 0)], False),
                               (3, [(1, 1, 0), (0, 1, 1), (1, 0, 1),
                                    (1, 1, 1)], True)):
        R = PolynomialRing(GF(2), ['x%d' % i for i in range(r)])
        xs = R.gens()
        lin = [sum(a * x for a, x in zip(v, xs)) for v in chars]
        sq = [l ** 2 for l in lin]
        k = len(sq)
        chern = [sum(prod_(c) for c in itertools.combinations(sq, i))
                 for i in range(1, k + 1)]
        I = R.ideal(chern)
        fin = I.dimension() == 0
        Mx = _matrix(GF(2), chars)
        check(fin == faithful and faithful == (Mx.rank() == r),
              'Corollary 3.10.2 for (Z/2)^%d and the characters %s: '
              'H^* is finite over the Chern subring iff the representation '
              'is faithful (%s)' % (r, chars, faithful))


def prod_(xs):
    out = 1
    for x in xs:
        out = out * x
    return out


def normal_or_all_subgroups(G, k):
    found = set()
    for a in range(G.n):
        S = tuple(G.closure([a]))
        if len(S) == k:
            found.add(S)
    return [list(S) for S in sorted(found)]


def main():
    section_3_5()
    section_3_5_lemma()
    section_3_5_homology()
    section_3_5_ext()
    section_3_6()
    section_3_7_sign()
    section_3_7_emss()
    section_3_7_kz2()
    section_3_8()
    section_3_9()
    section_3_9_groups()
    section_3_10()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
