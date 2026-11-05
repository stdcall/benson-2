"""Exact checks of Chapter 3, Sections 3.1-3.4 (Sage).

Benson, *Representations and Cohomology II*, first paperback edition (1998),
Chapter 3 "Spectral sequences", Sections 3.1-3.4, printed pp. 93-109.  Our
files: content/03-01-spectral-sequences-intro.typ ...
content/03-04-double-complex.typ.  (Sections 3.5-3.10 are checked in
chapter-3b.py; this script does not import it.)

Everything is an exact computation over finite fields GF(p) or over ZZ,
with random complexes from fixed seeds.  Expected values are the book's
statements read off the printed pages (page and label in each message); the
chapter files are not parsed.  Where the printed text was corrected, the
printed reading is kept as a refuted check beside the corrected one.

Spectral sequences are computed independently of the book's exact couples
by the formulas E_r^(p) = Z_r^p / (Z_(r-1)^(p+1) + d Z_(r-1)^(p-r+1)), Z_r^p
= F^p cap d^(-1) F^(p+r) (homology: Z^r_p = F_p cap d^(-1) F_(p-r)), and
compared with the pieces from which the random filtered complexes are built
(cycles and pairs x -> dx of every length).

Checked here:

3.1-3.2 (pp. 96-104), seven filtered cochain complexes over GF(2), GF(3),
GF(5) (six random, first quadrant, degrees <= 5, one made to order):
  * E_r^(pq) for all r (and E_infinity); E_(r+1) = H(E_r, d_r) with d_r of
    bidegree (r, -r + 1) (p. 96: d_2 of (2, -1), d_3 of (3, -2)); E_n^(pq)
    = E_infinity^(pq) and no d_n in or out for n > max(p, q + 1) (p. 97),
    the bound attained by transgressions d_(q+1) : E^(0q) -> E^(q+1,0);
    H^n = F^0 H^n >= ... >= F^(n+1) H^n = 0 with quotients E_infinity
    (p. 97, Definition 3.2.8, Theorem 3.2.9).
  * The exact couple of p. 98 (Ker i_1 = Im k_1, Ker j_1 = Im i_1, Ker k_1
    = Im j_1; degrees (-1, 1), (0, 0), (1, 0)) and its derived couples
    (Definitions 3.2.1-3.2.3) built literally: D' = Im i, E' = H(E, d),
    i', j'(i(x)) = j(x) + Im d, k'(z + Im d) = k(z) are well defined and
    exact; deg j_n = (n - 1, -n + 1), deg d_n = (n, -n + 1) (p. 100); the
    E_n of the derived couples are the pages, d_n = j_n k_n has their
    ranks.
  * Proposition 3.2.4: the two descriptions of Z_n^(pq) (image and kernel)
    and of B_n^(pq) agree inside E_1, E_1 = Z_1 >= Z_2 >= ... >= B_2 >= B_1
    = 0, E_n ~ Z_n / B_n; Theorem 3.2.6 (with the author's corrected entry
    H^(p+q)(F^(p-n+1) X, F^(p+1) X)); Corollary 3.2.7.
  * Proposition 3.2.10 with the explicit maps (edge maps and d_2), exact.
  * Homology (p. 97, p. 104), four random filtered chain complexes: the
    pages, E^n_(pq) = H(E^(n-1)_(pq), d^(n-1)) with deg d^n = (-n, n - 1)
    (the corrected display; the printed d^n does not act on E^(n-1)), the
    filtration 0 = F_(-1) H <= ... <= F_n H_n = H_n, Proposition 3.2.11
    with explicit maps; the transgression d^2 : E^2_(20) -> E^2_(01) is
    non-zero in an example, and the printed direction E^n_(0,n-1) ->
    E^n_(n0) is refuted (bidegree (-n, n - 1) sends (0, n - 1) to (-n,
    2n - 2)).
3.3 (p. 105), cellular models of circle bundles filtered by the preimages
  of the skeleta of the base: L(m, 1) -> S^2 (m = 1, 2, 3, 4, 6; GF(2),
  GF(3), GF(5)): E_2^(pq) = H^p(S^2; H^q(S^1)), d_2 = multiplication by m,
  the abutment H^*(L(m, 1)); the Klein bottle over S^1: E_2 is H^p(S^1;
  H^q(S^1)) with local coefficients (monodromy -1), and over GF(3), GF(5)
  the E_2 for a trivial action is refuted (Remark, Remarks (iii)).
3.4 (pp. 106-109):
  * Six random first quadrant double complexes (staircases, squares and
    dots under a random change of basis; GF(2), GF(3), GF(5), GF(7)):
    Definition 3.4.1 and d o d = 0 on Tot; Theorem 3.4.2: E_1 = H(E_0,
    d_0), E_2 = H^p(H^q(E_0, d_0), d_1) computed column by column, "d_1" =
    j_1 k_1 (p. 107); non-zero higher differentials; the Remark p. 108: the
    second spectral sequence (rows) has E_2 = H^q(H^p(E_0, d_1), d_0) and
    both converge to H^*(Tot); the vertical edge homomorphism (p. 108).
    With commuting instead of anticommuting squares d o d != 0 (refuted).
  * Proposition 3.4.3 for complexes C of free and D of free (hence
    injective) modules over F[C2] (GF(2)), F[C3], F[V4], F[S3], F[C4]: the
    double complex Hom_Lambda(C_s, D_t) filtered both ways has E_2 =
    Ext^p(H_q(C), D) resp. Ext^p(C, H_(-q)(D)) (computed independently from
    the modules H_q(C), H_t(D)), both converging to Ext^n(C, D).
  * Proposition 3.4.4 (corrected: "and H_0(D) is flat"; the printed
    statement and its "in particular" are refuted): Lambda = ZZ, C = (ZZ
    --2--> ZZ), D = ZZ/2 or D = (ZZ --2--> ZZ): H_1(C (x) D) = ZZ/2 while
    H_1(C) (x) H_0(D) = 0 and C (x) D is not exact in positive degrees; 40
    random complexes over ZZ (integral homology by Smith form, H_*(C (x) A)
    by finitely generated modules): H_*(C (x) D) ~ H_*(C (x) H_0(D))
    always (what the proof gives), equal to H_*(C) (x) H_0(D) exactly when
    no Tor term appears (universal coefficients, Weibel 3.6.2, checked
    independently), always when H_0(D) is free; 20 complexes over F[C2],
    F[C4], F[V4] (GF(2)), F[C3], F[C9] (GF(3)) with D exact in positive
    degrees (also with non-projective terms): H_*(C (x) D) ~ H_*(C (x)
    H_0(D)); the printed reading fails there too, e.g. the resolution of
    F_2 over F_2[C2] with D = F_2.  The uses: over a field (Theorem 5.14.2)
    C (x) D is exact in positive degrees with H_0 = H_0(C) (x) H_0(D); over
    ZZ (Section 4.1) C (x) C is exact in positive degrees iff Tor(H_0(C),
    H_0(C)) = 0, in particular when H_0(C) is flat.

Not established: none of the general theorems is proved here.  Every check
concerns the listed complexes, rings and degrees; random complexes are
finite and from fixed seeds.  The topology of Section 3.3 (excision, the
Kunneth isomorphism for the fibre, Proposition 1.6.7) is not checked: the
models are cellular cochain complexes with the filtration of the text.  Not
checked: convergence questions for non-first-quadrant spectral sequences,
the vertical edge homomorphism in the general filtered setting beyond the
double complexes.  Nothing here compares our Typst text with the printed
book.

Run with:  sage -python checks/sage/chapter-3a.py
"""
import random

from sage.all import GF, ZZ, ChainComplex, matrix as _matrix

SCOPE = 'chapter-3a'
COUNT = [0]
RNG = random.Random(20261105)


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


# ===========================================================================
# Linear algebra over finite fields.  Dense products over GF(p), p odd, go
# through the local OpenBLAS build, which stops with SIGILL on this machine:
# matrices over odd characteristic are created sparse (exact all the same).
# ===========================================================================


def _sp(F):
    return F.characteristic() != 2


def mat(F, r, c, entries=None):
    if entries is None:
        entries = {}
    return _matrix(F, r, c, entries, sparse=_sp(F))


def ident(F, n):
    return mat(F, n, n, {(i, i): 1 for i in range(n)})


def hcat(F, n, mats):
    out = mat(F, n, 0)
    for A in mats:
        assert A.nrows() == n
        if A.ncols():
            out = out.augment(A)
    return out


def rk(A):
    return A.rank() if A.nrows() and A.ncols() else 0


def kernel_cols(A):
    """Columns: a basis of {x : A x = 0}."""
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


def random_nonzero(F):
    return F(RNG.randrange(1, F.characteristic()))


class Quot:
    """The subquotient Z/B of F^n (Z, B given by spanning columns, B <= Z):
    coordinates cls(v) of the class of v in Z, representatives rep(c)."""

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
        X = self.basis.solve_right(V)   # raises if V is not in Z
        return X.matrix_from_rows(range(self.nb, self.nb + self.dim))

    def rep(self, X=None):
        return self.C if X is None else self.C * X


# ===========================================================================
# Filtered cochain complexes with a filtration split by the basis
# ===========================================================================


class Filtered:
    """X^n has basis vectors e_(n,i) of filtration degree filt[n][i];
    F^p X^n is spanned by those with filt >= p; d[n] : X^n -> X^(n+1) has the
    images of the basis vectors as columns and must preserve the filtration.
    All degrees outside the given range are zero."""

    def __init__(self, F, filt, d):
        self.F = F
        self.filt = {n: list(f) for n, f in filt.items()}
        self.degs = sorted(self.filt)
        self.d = d
        fs = [a for f in self.filt.values() for a in f] or [0]
        self.fmin, self.fmax = min(fs), max(fs)
        self.rinf = self.fmax - self.fmin + 2
        for n in self.degs:
            A = self.dm(n)
            assert A.nrows() == self.dim(n + 1) and A.ncols() == self.dim(n)
            for (i, j), _ in A.dict().items():
                assert self.filt[n + 1][i] >= self.filt[n][j], \
                    'd does not preserve the filtration'
            assert (self.dm(n + 1) * A).is_zero(), 'd o d != 0'

    def dim(self, n):
        return len(self.filt.get(n, []))

    def dm(self, n):
        A = self.d.get(n)
        if A is None:
            return mat(self.F, self.dim(n + 1), self.dim(n))
        return A

    def idx(self, n, lo=None, hi=None):
        """Basis indices with lo <= filt < hi (None: unbounded)."""
        return [i for i, a in enumerate(self.filt.get(n, []))
                if (lo is None or a >= lo) and (hi is None or a < hi)]

    def units(self, n, idx):
        return mat(self.F, self.dim(n), len(idx),
                   {(i, k): 1 for k, i in enumerate(idx)})

    def rows(self, n, idx):
        return mat(self.F, len(idx), self.dim(n),
                   {(k, i): 1 for k, i in enumerate(idx)})

    # --- the pages, by Z_r = F^p cap d^(-1) F^(p+r) -----------------------
    def Z(self, r, p, n):
        S = self.units(n, self.idx(n, p))
        cond = self.rows(n + 1, self.idx(n + 1, None, p + r)) * self.dm(n)
        return S * kernel_cols(cond * S)

    def B(self, r, p, n):
        if r == 0:
            return self.units(n, self.idx(n, p + 1))
        Zup = self.Z(r - 1, p + 1, n)
        Zlow = self.Z(r - 1, p - r + 1, n - 1)
        return hcat(self.F, self.dim(n), [Zup, self.dm(n - 1) * Zlow])

    def E(self, r, p, n):
        """E_r^(p, n-p) = Z_r / (Z_(r-1)^(p+1) + d Z_(r-1)^(p-r+1))."""
        return Quot(self.F, self.dim(n), self.Z(r, p, n), self.B(r, p, n))

    def Edim(self, r, p, n):
        return self.E(r, p, n).dim

    def dr_rank(self, r, p, n):
        """Rank of d_r : E_r^(p, n-p) -> E_r^(p+r, n+1-p-r)."""
        Zs = self.dm(n) * self.Z(r, p, n)
        Bt = self.B(r, p + r, n + 1)
        assert in_span(self.Z(r, p + r, n + 1), Zs)
        return rk(hcat(self.F, self.dim(n + 1), [Bt, Zs])) - rk(Bt)

    # --- cohomology of quotients F^a / F^b ----------------------------------
    def rel(self, n, a=None, b=None):
        """H^n(F^a X / F^b X) as a subquotient of X^n (None: a = -inf or
        b = +inf)."""
        I = self.idx(n, a, b)
        S = self.units(n, I)
        P = self.rows(n + 1, self.idx(n + 1, a, b))
        Zs = S * kernel_cols(P * self.dm(n) * S)
        Sm = self.units(n - 1, self.idx(n - 1, a, b))
        Bs = S * self.rows(n, I) * self.dm(n - 1) * Sm
        return Quot(self.F, self.dim(n), Zs, Bs)

    def restrict(self, n, V, a=None, b=None):
        """Zero the coordinates outside a <= filt < b."""
        keep = set(self.idx(n, a, b))
        D = mat(self.F, self.dim(n), self.dim(n),
                {(i, i): 1 for i in keep})
        return D * V

    def rel_map(self, n, src, tgt):
        """H^n(F^a1/F^b1) -> H^n(F^a2/F^b2) induced by the inclusion
        (a1 >= a2, b1 >= b2)."""
        Qs, Qt = self.rel(n, *src), self.rel(n, *tgt)
        return Qt.cls(self.restrict(n, Qs.rep(), *tgt)), Qs, Qt

    def connecting(self, n, a, b, c):
        """H^n(F^a/F^b) -> H^(n+1)(F^b/F^c) of the triple F^c <= F^b <= F^a."""
        Qs, Qt = self.rel(n, a, b), self.rel(n + 1, b, c)
        V = self.restrict(n + 1, self.dm(n) * Qs.rep(), b, c)
        return Qt.cls(V), Qs, Qt

    def H(self, n):
        return self.rel(n)

    def FH_dim(self, p, n):
        """dim F^p H^n = dim Im(H^n(F^p X) -> H^n(X)) (Definition 3.2.8)."""
        A, _, _ = self.rel_map(n, (p, None), (None, None))
        return rk(A)


def random_filtered(F, top, rng, cohomological=True, first_quadrant=True,
                    npairs=10, ncycles=5, maxfilt=None, scramble=True):
    """A random finite filtered (co)chain complex: elementary pieces (a
    cycle z of degree n and filtration c; a pair x -> y = dx, x of degree n
    and filtration a, y of degree n +- 1 and filtration b, b >= a in
    cohomology, b <= a in homology), then a random change of basis
    preserving the filtration in each degree.  Returns the complex and the
    pieces (the 'barcode')."""
    if maxfilt is None:
        maxfilt = top
    cyc, pairs = [], []
    for _ in range(ncycles):
        n = rng.randrange(0, top + 1)
        c = rng.randrange(0, (min(n, maxfilt) if first_quadrant else maxfilt)
                          + 1)
        cyc.append((n, c))
    for _ in range(npairs):
        if cohomological:
            n = rng.randrange(0, top)
            hi_a = min(n, maxfilt) if first_quadrant else maxfilt
            a = rng.randrange(0, hi_a + 1)
            hi_b = min(n + 1, maxfilt) if first_quadrant else maxfilt
            b = rng.randrange(a, hi_b + 1)
            pairs.append((n, a, b))
        else:
            n = rng.randrange(1, top + 1)
            hi_a = min(n, maxfilt) if first_quadrant else maxfilt
            a = rng.randrange(0, hi_a + 1)
            hi_b = min(a, n - 1) if first_quadrant else a
            b = rng.randrange(0, hi_b + 1)
            pairs.append((n, a, b))
    filt = {n: [] for n in range(0, top + 1)}
    entries = {}
    for (n, c) in cyc:
        filt[n].append(c)
    step = 1 if cohomological else -1
    for (n, a, b) in pairs:
        filt[n].append(a)
        i = len(filt[n]) - 1
        filt[n + step].append(b)
        j = len(filt[n + step]) - 1
        entries.setdefault(n, {})[(j, i)] = random_nonzero(F)
    d = {}
    for n in filt:
        m = n + step
        if m in filt:
            d[n] = mat(F, len(filt[m]), len(filt[n]), entries.get(n, {}))
    if scramble:
        T = {}
        for n, f in filt.items():
            # unipotent with respect to the order by filtration: column j
            # supported on filtration >= filt j (cohomology) or <= (homology)
            k = len(f)
            ent = {(i, i): 1 for i in range(k)}
            for i in range(k):
                for j in range(k):
                    if i == j:
                        continue
                    ok = (f[i] > f[j] or (f[i] == f[j] and i > j)) \
                        if cohomological else \
                        (f[i] < f[j] or (f[i] == f[j] and i > j))
                    if ok and rng.random() < 0.6:
                        ent[(i, j)] = F(rng.randrange(F.characteristic()))
            T[n] = mat(F, k, k, ent)
        for n in list(d):
            d[n] = T[n + step] * d[n] * T[n].inverse()
    return filt, d, cyc, pairs


def barcode_E(cyc, pairs, r, p, n, cohomological=True):
    """dim E_r^(p, n-p) (cohomology) or E^r_(p, n-p) (homology) predicted
    from the pieces: a cycle survives to E_infinity; a pair x -> y of length
    l = |b - a| contributes to E_r at both ends for r <= l."""
    cnt = sum(1 for (m, c) in cyc if m == n and c == p)
    step = 1 if cohomological else -1
    for (m, a, b) in pairs:
        ln = abs(b - a)
        if r is not None and r > ln:
            continue
        if r is None:
            continue
        if m == n and a == p:
            cnt += 1
        if m + step == n and b == p:
            cnt += 1
    return cnt


class HFiltered:
    """A filtered chain complex: X_n with basis vectors of filtration filt;
    F_p X_n is spanned by those with filt <= p; d[n] : X_n -> X_(n-1)
    preserves the filtration.  Pages by the formulas of the homology setup
    (p. 104): Z^r_p = F_p cap d^(-1) F_(p-r), B^r_p = Z^(r-1)_(p-1) +
    d Z^(r-1)_(p+r-1), E^r_(p q) = Z^r_p / B^r_p in degree p + q."""

    def __init__(self, F, filt, d):
        self.F, self.filt, self.d = F, filt, d
        fs = [a for f in filt.values() for a in f] or [0]
        self.fmin, self.fmax = min(fs), max(fs)
        self.rinf = self.fmax - self.fmin + 2
        for n in filt:
            A = self.dm(n)
            for (i, j), _ in A.dict().items():
                assert self.filt[n - 1][i] <= self.filt[n][j]
            assert (self.dm(n - 1) * A).is_zero()

    def dim(self, n):
        return len(self.filt.get(n, []))

    def dm(self, n):
        A = self.d.get(n)
        if A is None:
            return mat(self.F, self.dim(n - 1), self.dim(n))
        return A

    def idx(self, n, lo=None, hi=None):
        return [i for i, a in enumerate(self.filt.get(n, []))
                if (lo is None or a >= lo) and (hi is None or a <= hi)]

    def units(self, n, idx):
        return mat(self.F, self.dim(n), len(idx),
                   {(i, k): 1 for k, i in enumerate(idx)})

    def rows(self, n, idx):
        return mat(self.F, len(idx), self.dim(n),
                   {(k, i): 1 for k, i in enumerate(idx)})

    def Z(self, r, p, n):
        S = self.units(n, self.idx(n, None, p))
        cond = self.rows(n - 1, self.idx(n - 1, p - r + 1)) * self.dm(n)
        return S * kernel_cols(cond * S)

    def B(self, r, p, n):
        if r == 0:
            return self.units(n, self.idx(n, None, p - 1))
        return hcat(self.F, self.dim(n),
                    [self.Z(r - 1, p - 1, n),
                     self.dm(n + 1) * self.Z(r - 1, p + r - 1, n + 1)])

    def E(self, r, p, n):
        return Quot(self.F, self.dim(n), self.Z(r, p, n), self.B(r, p, n))

    def dr_rank(self, r, p, n):
        """Rank of d^r : E^r_(p, n-p) -> E^r_(p-r, n-1-p+r)."""
        Zs = self.dm(n) * self.Z(r, p, n)
        Bt = self.B(r, p - r, n - 1)
        assert in_span(self.Z(r, p - r, n - 1), Zs)
        return rk(hcat(self.F, self.dim(n - 1), [Bt, Zs])) - rk(Bt)

    def H(self, n):
        Zs = kernel_cols(self.dm(n))
        return Quot(self.F, self.dim(n), Zs, self.dm(n + 1))

    def FH_dim(self, p, n):
        """dim F_p H_n = dim Im(H_n(F_p X) -> H_n(X))."""
        S = self.units(n, self.idx(n, None, p))
        Zp = S * kernel_cols(self.dm(n) * S)
        Bn = self.dm(n + 1)
        return rk(hcat(self.F, self.dim(n), [Bn, Zp])) - rk(Bn)


# ===========================================================================
# Exact couples (Definitions 3.2.1-3.2.3)
# ===========================================================================


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


class Couple:
    """A bigraded exact couple: spaces D[(p,q)], E[(p,q)] (dimensions), maps
    i, j, k keyed by their source bidegree, of bidegrees deg['i'], deg['j'],
    deg['k'].  Bidegrees outside `window` are unknown."""

    def __init__(self, F, D, E, i, j, k, deg, window):
        self.F, self.D, self.E = F, D, E
        self.i, self.j, self.k, self.deg, self.window = i, j, k, deg, window

    def d(self, s):
        """d = j o k on E[s] (Definition 3.2.2: d = j k)."""
        t = add(s, self.deg['k'])
        return self.j[t] * self.k[s]

    def exact_at(self, s):
        """Ker i = Im k, Ker j = Im i, Ker k = Im j at the spaces of bidegree
        s (where all the maps involved are known)."""
        ok = True
        di, dj, dk = self.deg['i'], self.deg['j'], self.deg['k']
        # at D[s]: Im(k from E[s - dk]) = Ker(i out of D[s])
        a = sub(s, dk)
        if s in self.i and a in self.k:
            ok &= (self.i[s] * self.k[a]).is_zero()
            ok &= rk(self.k[a]) == self.D[s] - rk(self.i[s])
        # at D[s]: Im(i from D[s - di]) = Ker(j out of D[s])
        b = sub(s, di)
        if s in self.j and b in self.i:
            ok &= (self.j[s] * self.i[b]).is_zero()
            ok &= rk(self.i[b]) == self.D[s] - rk(self.j[s])
        # at E[s]: Im(j from D[s - dj]) = Ker(k out of E[s])
        c = sub(s, dj)
        if s in self.k and c in self.j:
            ok &= (self.k[s] * self.j[c]).is_zero()
            ok &= rk(self.j[c]) == self.E[s] - rk(self.k[s])
        return ok

    def derived(self):
        """The derived couple of Definition 3.2.2: D' = Im i, E' = H(E, d),
        i' = i|D', j'(i(x)) = j(x) + Im d, k'(z + Im d) = k(z).  Asserts that
        the maps are well defined (the 'easy diagram chase')."""
        F = self.F
        di, dj, dk = self.deg['i'], self.deg['j'], self.deg['k']
        Bd, Q = {}, {}
        for s in self.window:
            src = sub(s, di)
            if src in self.i:
                Bd[s] = colbasis(self.i[src])
            dsrc = sub(sub(s, dk), dj)
            if s in self.k and add(s, dk) in self.j and dsrc in self.k and \
                    add(dsrc, dk) in self.j:
                dout, din = self.d(s), self.d(dsrc)
                Q[s] = Quot(F, self.E[s], kernel_cols(dout), din)
        D2 = {s: B.ncols() for s, B in Bd.items()}
        E2 = {s: q.dim for s, q in Q.items()}
        i2, j2, k2 = {}, {}, {}
        for s in Bd:
            t = add(s, di)
            if t in Bd and s in self.i:
                i2[s] = Bd[t].solve_right(self.i[s] * Bd[s])
            src = sub(s, di)                  # D'[s] = i(D[src])
            t = add(src, dj)                  # j(x) in E[t]
            if src in self.j and t in Q:
                X = self.i[src].solve_right(Bd[s])
                j2[s] = Q[t].cls(self.j[src] * X)      # j(x) is a d-cycle
                Kx = kernel_cols(self.i[src])          # j(Ker i) <= Im d
                assert Q[t].cls(self.j[src] * Kx).is_zero()
        for s in Q:
            t = add(s, dk)
            if s in self.k and t in Bd:
                k2[s] = Bd[t].solve_right(self.k[s] * Q[s].rep())
                dsrc = sub(sub(s, dk), dj)
                assert (self.k[s] * self.d(dsrc)).is_zero()   # k(Im d) = 0
        deg2 = {'i': di, 'j': sub(dj, di), 'k': dk}
        win = [s for s in self.window if s in D2 and s in E2]
        return Couple(F, D2, E2, i2, j2, k2, deg2, win)


def couple_of(X, pwin, nwin):
    """The exact couple of p. 98: D_1^(pq) = H^(p+q)(F^p X), E_1^(pq) =
    H^(p+q)(F^p X, F^(p+1) X), i_1 induced by inclusion, j_1 by projection,
    k_1 the connecting homomorphism."""
    D, E, i, j, k = {}, {}, {}, {}, {}
    for p in pwin:
        for n in nwin:
            s = (p, n - p)
            D[s] = X.rel(n, p, None).dim
            E[s] = X.rel(n, p, p + 1).dim
            if p + 1 in pwin:
                i[(p + 1, n - p - 1)] = X.rel_map(n, (p + 1, None),
                                                  (p, None))[0]
            j[s] = X.rel_map(n, (p, None), (p, p + 1))[0]
            if n + 1 in nwin and p + 1 in pwin:
                k[s] = X.connecting(n, p, p + 1, None)[0]
    window = [(p, n - p) for p in pwin for n in nwin]
    return Couple(X.F, D, E, i, j, k,
                  {'i': (-1, 1), 'j': (0, 0), 'k': (1, 0)}, window)


# ===========================================================================
# Sections 3.1 and 3.2: pages, exact couples, Z_n and B_n, convergence
# ===========================================================================


def cohomology_examples():
    """Random first quadrant filtered cochain complexes (seeded), and two
    made to order: a transgression d_(q+1) : E^(0 q) -> E^(q+1, 0) and a
    complex with differentials d_0 ... d_4."""
    out = []
    specs = [(GF(2), 4, 10, 5), (GF(2), 5, 14, 6), (GF(3), 4, 10, 4),
             (GF(3), 5, 12, 6), (GF(5), 4, 9, 5), (GF(2), 3, 8, 4)]
    for (F, top, npairs, ncyc) in specs:
        filt, d, cyc, pairs = random_filtered(F, top, RNG, npairs=npairs,
                                              ncycles=ncyc)
        out.append((F, top, Filtered(F, filt, d), cyc, pairs))
    # made to order: x (degree q, filtration 0) -> y (degree q + 1,
    # filtration q + 1), q = 1, 2, 3 (transgressions), plus d_0 and d_1.
    F = GF(3)
    cyc = [(0, 0), (2, 1), (3, 3)]
    pairs = [(1, 0, 2), (2, 0, 3), (3, 0, 4), (2, 1, 1), (1, 1, 2)]
    filt = {n: [] for n in range(0, 5)}
    ent = {}
    for (n, c) in cyc:
        filt[n].append(c)
    for (n, a, b) in pairs:
        filt[n].append(a)
        filt[n + 1].append(b)
        ent.setdefault(n, {})[(len(filt[n + 1]) - 1, len(filt[n]) - 1)] = 1
    d = {n: mat(F, len(filt[n + 1]), len(filt[n]), ent.get(n, {}))
         for n in range(0, 4)}
    out.append((F, 4, Filtered(F, filt, d), cyc, pairs))
    return out


def section_3_1_3_2():
    exs = cohomology_examples()
    for t, (F, top, X, cyc, pairs) in enumerate(exs):
        lab = 'example %d over GF(%d)' % (t, F.characteristic())
        pw = range(X.fmin - 1, X.fmax + 2)
        nw = range(0, top + 1)
        R = X.rinf
        # pages from Z_r / B_r against the pieces of the complex
        ok = all(X.Edim(r, p, n) == barcode_E(cyc, pairs, r, p, n)
                 for r in range(0, R + 1) for p in pw for n in nw)
        check(ok, 'Sections 3.1-3.2: E_r^(pq) of a filtered complex, r = '
              '0..%d (%s)' % (R, lab))
        okinf = all(X.Edim(R, p, n) == barcode_E(cyc, pairs, None, p, n)
                    for p in pw for n in nw)
        check(okinf, 'E_infinity^(pq) (%s)' % lab)
        # E_(r+1) = H(E_r, d_r), d_r of bidegree (r, -r + 1) (p. 96)
        ok = True
        for r in range(0, R):
            for p in pw:
                for n in nw:
                    out_rk = X.dr_rank(r, p, n)
                    in_rk = X.dr_rank(r, p - r, n - 1) if n >= 1 else 0
                    ok &= X.Edim(r + 1, p, n) == X.Edim(r, p, n) - out_rk \
                        - in_rk
        check(ok, 'p. 96: E_(r+1) = H(E_r, d_r) with d_r : E_r^(pq) -> '
              'E_r^(p+r, q-r+1) (%s)' % lab)
        # p. 97: E_(n+1)^(pq) = E_n^(pq) for n > max(p, q + 1)
        ok = True
        for p in range(0, X.fmax + 1):
            for n in nw:
                q = n - p
                if q < 0:
                    continue
                for r in range(max(p, q + 1) + 1, R + 1):
                    ok &= X.dr_rank(r, p, n) == 0
                    ok &= (X.dr_rank(r, p - r, n - 1) == 0) if n else True
                    ok &= X.Edim(r, p, n) == X.Edim(R, p, n)
        check(ok, 'p. 97: d_n = 0 into and out of E_n^(pq) and E_n^(pq) = '
              'E_infinity^(pq) for n > max(p, q + 1) (%s)' % lab)
        # p. 97 and Theorem 3.2.9: the filtration of H^(p+q) and its
        # quotients, F^(p+q+1) H^(p+q) = 0 (first quadrant)
        ok = True
        for n in nw:
            hn = X.H(n).dim
            ok &= X.FH_dim(0, n) == hn and X.FH_dim(n + 1, n) == 0
            for p in range(0, n + 1):
                ok &= X.FH_dim(p, n) - X.FH_dim(p + 1, n) == \
                    X.Edim(R, p, n)
        check(ok, 'p. 97, Definition 3.2.8, Theorem 3.2.9: H^n = F^0 H^n >= '
              '... >= F^(n+1) H^n = 0, F^p H^(p+q) / F^(p+1) H^(p+q) ~ '
              'E_infinity^(pq) (%s)' % lab)
        # Theorem 3.2.6 and Corollary 3.2.7
        ok = True
        for r in range(1, R + 1):
            for p in pw:
                for n in nw:
                    A = X.rel_map(n, (p, p + r), (p - r + 1, p + 1))[0]
                    ok &= rk(A) == X.Edim(r, p, n)
        check(ok, 'Theorem 3.2.6: E_n^(pq) ~ Im(H^(p+q)(F^p X, F^(p+n) X) '
              '-> H^(p+q)(F^(p-n+1) X, F^(p+1) X)) (%s)' % lab)
        ok = all(rk(X.rel_map(n, (p, None), (None, p + 1))[0])
                 == X.Edim(R, p, n) for p in pw for n in nw)
        check(ok, 'Corollary 3.2.7: E_infinity^(pq) = Im(H^(p+q)(F^p X) -> '
              'H^(p+q)(X, F^(p+1) X)) (%s)' % lab)
        # Proposition 3.2.4: Z_n and B_n inside E_1
        ok = True
        for p in pw:
            for n in nw:
                E1 = X.rel(n, p, p + 1)
                prevZ, prevB = None, None
                for r in range(1, R + 1):
                    A1 = X.rel_map(n, (p, p + r), (p, p + 1))[0]
                    Zi = colbasis(A1)
                    Cn = X.connecting(n, p, p + 1, p + r)[0]
                    Zii = kernel_cols(Cn)
                    if n >= 1:
                        Bi = colbasis(X.connecting(n - 1, p - r + 1, p,
                                                   p + 1)[0])
                    else:
                        Bi = mat(F, E1.dim, 0)
                    Bii = kernel_cols(X.rel_map(n, (p, p + 1),
                                                (p - r + 1, p + 1))[0])
                    ok &= rk(Zi) == rk(Zii) == rk(hcat(F, E1.dim, [Zi, Zii]))
                    ok &= rk(Bi) == rk(Bii) == rk(hcat(F, E1.dim, [Bi, Bii]))
                    ok &= in_span(Zi, Bi)
                    ok &= rk(Zi) - rk(Bi) == X.Edim(r, p, n)
                    if prevZ is not None:   # Z_r <= Z_(r-1), B_(r-1) <= B_r
                        ok &= in_span(prevZ, Zi) and in_span(Bi, prevB)
                    else:                   # Z_1 = E_1, B_1 = 0
                        ok &= rk(Zi) == E1.dim and rk(Bi) == 0
                    prevZ, prevB = Zi, Bi
        check(ok, 'Proposition 3.2.4 (i), (ii): the two descriptions of '
              'Z_n^(pq) and of B_n^(pq) agree, E_1 = Z_1 >= Z_2 >= ... >= '
              'B_2 >= B_1 = 0, E_n ~ Z_n / B_n (%s)' % lab)
        # Definitions 3.2.1-3.2.3: the exact couple and its derived couples
        pwin = list(range(X.fmin - R - 1, X.fmax + 2))
        nwin = list(range(0, top + 2))
        C = couple_of(X, pwin, nwin)
        inner = [s for s in C.window if pwin[0] < s[0] < pwin[-1]
                 and nwin[0] <= s[0] + s[1] < nwin[-1]]
        check(all(C.exact_at(s) for s in inner), 'p. 98: the exact couple '
              '(D_1, E_1; i_1, j_1, k_1) is exact, Ker i_1 = Im k_1, '
              'Ker j_1 = Im i_1, Ker k_1 = Im j_1 (%s)' % lab)
        check(C.deg == {'i': (-1, 1), 'j': (0, 0), 'k': (1, 0)}, 'p. 98: '
              'deg i_1 = (-1, 1), deg j_1 = (0, 0), deg k_1 = (1, 0)')
        ok_ex, ok_dim, ok_d, ok_deg = True, True, True, True
        for nn in range(1, R + 1):
            # C is the (nn - 1)st derived couple (Definition 3.2.3)
            ok_deg &= C.deg == {'i': (-1, 1), 'j': (nn - 1, -nn + 1),
                                'k': (1, 0)}
            dd = add(C.deg['j'], C.deg['k'])
            ok_deg &= dd == (nn, -nn + 1)
            for s in C.window:
                p, q = s
                if not (X.fmin - 1 <= p <= X.fmax + 1 and 0 <= p + q <= top):
                    continue
                ok_dim &= C.E[s] == X.Edim(nn, p, p + q)
                if s in C.k and add(s, C.deg['k']) in C.j:
                    ok_d &= rk(C.d(s)) == X.dr_rank(nn, p, p + q)
            inner = [s for s in C.window if X.fmin - 1 <= s[0] <= X.fmax
                     and 0 <= s[0] + s[1] < top]
            ok_ex &= all(C.exact_at(s) for s in inner)
            C = C.derived()
        check(ok_ex, 'Definition 3.2.2: each derived couple is an exact '
              'couple (maps well defined; %s)' % lab)
        check(ok_deg, 'p. 100: deg i_n = (-1, 1), deg j_n = (n - 1, -n + 1),'
              ' deg k_n = (1, 0), deg d_n = (n, -n + 1) (%s)' % lab)
        check(ok_dim and ok_d, 'Definition 3.2.3: the E_n of the derived '
              'couples are the pages E_n of the filtered complex, and d_n = '
              'j_n k_n has the ranks of d_n (%s)' % lab)
    # the bidegrees drawn on p. 96
    check(add((1, 0), (2 - 1, -2 + 1)) == (2, -1) and
          add((1, 0), (3 - 1, -3 + 1)) == (3, -2), 'p. 96: d_2 has bidegree '
          '(2, -1), d_3 has bidegree (3, -2)')
    # the made-to-order example: transgressions d_(q+1) : E^(0 q) -> E^(q+1,
    # 0) are non-zero, so the bound n > max(p, q + 1) is attained
    F, top, X, cyc, pairs = exs[-1]
    for q in (1, 2, 3):
        check(X.dr_rank(q + 1, 0, q) == 1, 'p. 97, p. 103: the '
              'transgression d_%d : E_%d^(0,%d) -> E_%d^(%d,0) is non-zero '
              'in the made-to-order complex (n = q + 1 = max(p, q + 1))'
              % (q + 1, q + 1, q, q + 1, q + 1))


def five_term_cohomology(X):
    """The maps of Proposition 3.2.10 for a first quadrant filtered cochain
    complex, as matrices in the coordinates of the subquotients."""
    E10, E01, E20 = X.E(2, 1, 1), X.E(2, 0, 1), X.E(2, 2, 2)
    H1, H2 = X.H(1), X.H(2)
    e1 = H1.cls(E10.rep())                   # E_2^(10) -> H^1
    e1p = E01.cls(H1.rep())                  # H^1 -> E_2^(01)
    d2 = E20.cls(X.dm(1) * E01.rep())        # d_2
    e2 = H2.cls(E20.rep())                   # E_2^(20) -> H^2
    return E10, H1, E01, E20, H2, e1, e1p, d2, e2


def exact_seq_ok(maps, dims):
    """0 -> V_0 -> V_1 -> ... -> V_k given by the maps f_i : V_i -> V_(i+1):
    f_0 injective and Im f_i = Ker f_(i+1)."""
    ok = rk(maps[0]) == dims[0]
    for a, b, mid in zip(maps, maps[1:], dims[1:]):
        ok &= (b * a).is_zero() and rk(a) == mid - rk(b)
    return ok


def section_3_2_five_term():
    for t, (F, top, X, cyc, pairs) in enumerate(cohomology_examples()):
        E10, H1, E01, E20, H2, e1, e1p, d2, e2 = five_term_cohomology(X)
        check(exact_seq_ok([e1, e1p, d2, e2],
                           [E10.dim, H1.dim, E01.dim, E20.dim]),
              'Proposition 3.2.10: 0 -> E_2^(10) -> H^1 -> E_2^(01) -> '
              'E_2^(20) -> H^2 exact, with the edge maps and d_2 (example '
              '%d, GF(%d))' % (t, F.characteristic()))
    # homology: random first quadrant filtered chain complexes
    specs = [(GF(2), 4, 10, 5), (GF(3), 4, 11, 5), (GF(5), 5, 12, 6),
             (GF(2), 5, 14, 4)]
    for t, (F, top, npairs, ncyc) in enumerate(specs):
        filt, d, cyc, pairs = random_filtered(F, top, RNG, cohomological=False,
                                              npairs=npairs, ncycles=ncyc)
        X = HFiltered(F, filt, d)
        R = X.rinf
        lab = 'homology example %d, GF(%d)' % (t, F.characteristic())
        pw = range(X.fmin - 1, X.fmax + 2)
        nw = range(0, top + 1)
        ok = all(X.E(r, p, n).dim == barcode_E(cyc, pairs, r, p, n, False)
                 for r in range(0, R + 1) for p in pw for n in nw)
        check(ok, 'p. 104: E^r_(pq) of a filtered chain complex (%s)' % lab)
        ok = True
        for r in range(0, R):
            for p in pw:
                for n in nw:
                    ok &= X.E(r + 1, p, n).dim == X.E(r, p, n).dim - \
                        X.dr_rank(r, p, n) - X.dr_rank(r, p + r, n + 1)
        check(ok, 'p. 97 and p. 104 (corrected): E^n_(pq) = H(E^(n-1)_(pq), '
              'd^(n-1)), d^n : E^n_(pq) -> E^n_(p-n, q+n-1), deg d^n = '
              '(-n, n - 1) (%s)' % lab)
        ok = True
        for n in nw:
            ok &= X.FH_dim(-1, n) == 0 and X.FH_dim(n, n) == X.H(n).dim
            for p in range(0, n + 1):
                ok &= X.FH_dim(p, n) - X.FH_dim(p - 1, n) == \
                    X.E(R, p, n).dim
        check(ok, 'p. 97, p. 104: 0 = F_(-1) H_n <= F_0 H_n <= ... <= F_n '
              'H_n = H_n with F_p H_(p+q) / F_(p-1) H_(p+q) ~ E^infinity_(pq) '
              '(%s)' % lab)
        # Proposition 3.2.11 with explicit maps
        E20, E01, E10 = X.E(2, 2, 2), X.E(2, 0, 1), X.E(2, 1, 1)
        H1, H2 = X.H(1), X.H(2)
        e2 = E20.cls(H2.rep())                     # H_2 -> E^2_(20)
        d2 = E01.cls(X.dm(2) * E20.rep())          # d^2
        e1p = H1.cls(E01.rep())                    # E^2_(01) -> H_1
        e1 = E10.cls(H1.rep())                     # H_1 -> E^2_(10)
        ok = (d2 * e2).is_zero() and rk(e2) == E20.dim - rk(d2)
        ok &= (e1p * d2).is_zero() and rk(d2) == E01.dim - rk(e1p)
        ok &= (e1 * e1p).is_zero() and rk(e1p) == H1.dim - rk(e1)
        ok &= rk(e1) == E10.dim
        check(ok, 'Proposition 3.2.11: H_2 -> E^2_(20) -> E^2_(01) -> H_1 -> '
              'E^2_(10) -> 0 exact (%s)' % lab)
    # p. 104: the transgression in homology runs E^n_(n0) -> E^n_(0,n-1)
    F = GF(3)
    # x (degree 2, filtration 2) -> y (degree 1, filtration 0); the other
    # basis vectors are cycles
    X = HFiltered(F, {0: [0], 1: [0, 1], 2: [2, 1], 3: [3]},
                  {1: mat(F, 1, 2), 2: mat(F, 2, 2, {(0, 0): 1}),
                   3: mat(F, 2, 1)})
    check(X.dr_rank(2, 2, 2) == 1, 'p. 104 (corrected): the transgression '
          'd^2 : E^2_(20) -> E^2_(01) is non-zero in an example')
    refuted(add((0, 1), (-2, 1)) == (2, 0), 'p. 104 as printed: d^n maps '
            'E^n_(0,n-1) to E^n_(n0) (n = 2); bidegree (-n, n - 1) sends '
            '(0, n - 1) to (-n, 2n - 2)')


# ===========================================================================
# Section 3.3: cellular models of two circle bundles
# ===========================================================================


def local_system_circle(F, t):
    """H^0, H^1 of the circle (one 0-cell, one 1-cell) with coefficients in
    the rank one local system with monodromy t: the cochain complex
    F --(t - 1)--> F."""
    A = mat(F, 1, 1, {(0, 0): F(t) - 1})
    return 1 - rk(A), 1 - rk(A)


def section_3_3():
    # Lens space L(m, 1) -> S^2 with fibre S^1: cells e0, e1 over the 0-cell
    # of S^2 (filtration 0), e2, e3 over the 2-cell (filtration 2); cellular
    # boundary d e2 = m e1, so the coboundary sends e1* to m e2*.
    for m in (1, 2, 3, 4, 6):
        for F in (GF(2), GF(3), GF(5)):
            filt = {0: [0], 1: [0], 2: [2], 3: [2]}
            d = {0: mat(F, 1, 1), 1: mat(F, 1, 1, {(0, 0): m}),
                 2: mat(F, 1, 1)}
            X = Filtered(F, filt, d)
            E2 = {(p, q): X.Edim(2, p, p + q) for p in range(0, 3)
                  for q in range(0, 2)}
            pred = {(p, q): (1 if p in (0, 2) else 0) for (p, q) in E2}
            check(E2 == pred, 'Section 3.3 (p. 105): E_2^(pq) = H^p(S^2; '
                  'H^q(S^1)) for the circle bundle L(%d,1) -> S^2 over GF(%d)'
                  % (m, F.characteristic()))
            dv = 1 if F(m) != 0 else 0
            check(X.dr_rank(2, 0, 1) == dv and
                  [X.H(n).dim for n in range(4)] ==
                  [1, 1 - dv, 1 - dv, 1], 'Section 3.3: d_2 : E_2^(01) -> '
                  'E_2^(20) is multiplication by %d and H^*(L(%d,1); GF(%d)) '
                  'is the abutment' % (m, m, F.characteristic()))
    # Klein bottle -> S^1 with fibre S^1 (cells v, a, b, e; d e = 2b, b the
    # fibre): pi_1 of the base acts on H^1 of the fibre by -1.
    for F in (GF(2), GF(3), GF(5)):
        filt = {0: [0], 1: [0, 1], 2: [1]}      # v; b, a; e
        d = {0: mat(F, 2, 1), 1: mat(F, 1, 2, {(0, 0): 2})}
        X = Filtered(F, filt, d)
        E2 = {(p, q): X.Edim(2, p, p + q) for p in (0, 1) for q in (0, 1)}
        h0t, h1t = local_system_circle(F, -1)
        h0, h1 = local_system_circle(F, 1)
        twisted = {(0, 0): h0, (1, 0): h1, (0, 1): h0t, (1, 1): h1t}
        trivial = {(0, 0): h0, (1, 0): h1, (0, 1): h0, (1, 1): h1}
        check(E2 == twisted, 'Section 3.3, Remark (p. 105) and Remarks (iii):'
              ' for the Klein bottle over S^1, E_2^(pq) = H^p(S^1; '
              'H^q(S^1)) with local coefficients (monodromy -1) over GF(%d)'
              % F.characteristic())
        if F.characteristic() != 2:
            refuted(E2 == trivial, 'the E_2 term with pi_1(B) acting '
                    'trivially on H^*(F) (Klein bottle, GF(%d))'
                    % F.characteristic())
            # two columns: E_2 = E_infinity; the abutment
            check([X.H(n).dim for n in range(3)] == [1, 1, 0] and
                  sum(twisted.values()) == 2, 'Klein bottle: H^*(K; '
                  'GF(%d)) = 1, 1, 0 = the totals of E_2' % F.characteristic())


# ===========================================================================
# Section 3.4: double complexes
# ===========================================================================


def random_double(F, rng, size=4, nz=5, nsq=3, ndot=4, anti=True):
    """A random first quadrant double complex (p, q < size): staircases
    (zigzags) s_1 -> t_1 <- s_2 -> t_2 <- ..., squares (anticommuting, or
    commuting if anti is False) and dots, then a random change of basis at
    every (p, q).  d0 : E^(pq) -> E^(p,q+1), d1 : E^(pq) -> E^(p+1,q)."""
    basis = {}

    def new(pq):
        basis.setdefault(pq, 0)
        basis[pq] += 1
        return (pq, basis[pq] - 1)

    e0, e1 = [], []
    for _ in range(ndot):
        new((rng.randrange(size), rng.randrange(size)))
    for _ in range(nsq):
        p, q = rng.randrange(size - 1), rng.randrange(size - 1)
        x, y, z, u = new((p, q)), new((p + 1, q)), new((p, q + 1)), \
            new((p + 1, q + 1))
        e1.append((x, y, 1))
        e0.append((x, z, 1))
        e0.append((y, u, 1))
        e1.append((z, u, -1 if anti else 1))
    for z in range(nz):
        ln = rng.randrange(1, size)
        q0 = rng.randrange(ln - 1, size) if ln > 1 else rng.randrange(size)
        p0 = rng.randrange(0, max(1, size - ln))
        start_target = rng.random() < 0.3
        end_source = rng.random() < 0.3
        if z == 0:      # one staircase giving a d_(size-1)
            ln, q0, p0 = size - 1, size - 2, 0
            start_target = end_source = False
        prev = None
        p, q = p0, q0
        # vertices: s_1 (p, q), t_1 (p+1, q), s_2 (p+1, q-1), t_2 (p+2, q-1)
        if start_target:
            # t_0 at (p, q + 1) receiving d0 from s_1
            t0 = new((p, q + 1)) if q + 1 < size + 1 else None
        else:
            t0 = None
        for kk in range(ln):
            s = new((p + kk, q - kk))
            if kk == 0 and t0 is not None:
                e0.append((s, t0, random_nonzero(F)))
            if prev is not None:
                e0.append((s, prev, random_nonzero(F)))
            if kk == ln - 1 and end_source:
                break
            t = new((p + kk + 1, q - kk))
            e1.append((s, t, random_nonzero(F)))
            prev = t
    dims = dict(basis)
    D0, D1 = {}, {}
    for (a, b, c) in e0:
        D0.setdefault(a[0], {})[(b[1], a[1])] = F(c)
    for (a, b, c) in e1:
        D1.setdefault(a[0], {})[(b[1], a[1])] = F(c)
    d0 = {pq: mat(F, dims.get((pq[0], pq[1] + 1), 0), n, D0.get(pq, {}))
          for pq, n in dims.items()}
    d1 = {pq: mat(F, dims.get((pq[0] + 1, pq[1]), 0), n, D1.get(pq, {}))
          for pq, n in dims.items()}
    T = {}
    for pq, n in dims.items():
        while True:
            A = mat(F, n, n, {(i, j): F(rng.randrange(F.characteristic()))
                              for i in range(n) for j in range(n)})
            if rk(A) == n:
                break
        T[pq] = A
    for pq in dims:
        up, right = (pq[0], pq[1] + 1), (pq[0] + 1, pq[1])
        Ti = T[pq].inverse()
        if up in dims:
            d0[pq] = T[up] * d0[pq] * Ti
        if right in dims:
            d1[pq] = T[right] * d1[pq] * Ti
    return dims, d0, d1


def total_complex(F, dims, d0, d1, by='p'):
    """Tot with d = d0 + d1 (Definition 3.4.1), filtered by columns (by =
    'p': F^p = sum_(i >= p) E^(ij)) or by rows (by = 'q')."""
    keys = {}
    filt = {}
    for (p, q), n in sorted(dims.items()):
        tot = p + q
        keys.setdefault(tot, [])
        for i in range(n):
            keys[tot].append(((p, q), i))
            filt.setdefault(tot, []).append(p if by == 'p' else q)
    pos = {tot: {k: a for a, k in enumerate(v)} for tot, v in keys.items()}
    d = {}
    for tot in keys:
        if tot + 1 not in keys:
            continue
        ent = {}
        for (pq, i) in keys[tot]:
            col = pos[tot][(pq, i)]
            for tgt, A in (((pq[0], pq[1] + 1), d0.get(pq)),
                           ((pq[0] + 1, pq[1]), d1.get(pq))):
                if A is None or tgt not in dims:
                    continue
                for r in range(A.nrows()):
                    c = A[r, i]
                    if c:
                        key = (pos[tot + 1][(tgt, r)], col)
                        ent[key] = ent.get(key, F(0)) + c
        d[tot] = mat(F, len(keys[tot + 1]), len(keys[tot]), ent)
    for tot in keys:
        filt.setdefault(tot, [])
    return filt, d, keys, pos


def E2_double_direct(F, dims, d0, d1, size):
    """E_1 = H(E_0, d_0) and E_2 = H^p(H^q(E_0, d_0), d_1) computed column by
    column (independently of the filtered complex)."""
    Hq = {}
    for (p, q) in dims:
        n = dims[(p, q)]
        down = d0.get((p, q - 1)) if (p, q - 1) in dims else None
        Zs = kernel_cols(d0[(p, q)]) if d0[(p, q)].nrows() else \
            ident(F, n)
        Bs = down if down is not None else mat(F, n, 0)
        Hq[(p, q)] = Quot(F, n, Zs, Bs)
    E1 = {pq: Q.dim for pq, Q in Hq.items()}
    ind = {}
    for (p, q), Q in Hq.items():
        if (p + 1, q) in Hq:
            ind[(p, q)] = Hq[(p + 1, q)].cls(d1[(p, q)] * Q.rep())
    E2 = {}
    for (p, q), Q in Hq.items():
        out = rk(ind[(p, q)]) if (p, q) in ind else 0
        inn = rk(ind[(p - 1, q)]) if (p - 1, q) in ind else 0
        E2[(p, q)] = Q.dim - out - inn
    return E1, E2, Hq, ind


def section_3_4_double():
    for t, F in enumerate([GF(2), GF(3), GF(5), GF(3), GF(2), GF(7)]):
        size = 4 + (t % 2)
        nzig = 6
        dims, d0, d1 = random_double(F, RNG, size=size, nz=nzig, nsq=3,
                                     ndot=3)
        lab = 'random double complex %d over GF(%d)' % (t,
                                                        F.characteristic())
        ok = True
        for pq in dims:
            up, right = (pq[0], pq[1] + 1), (pq[0] + 1, pq[1])
            diag = (pq[0] + 1, pq[1] + 1)
            if up in dims and (up[0], up[1] + 1) in dims:
                ok &= (d0[up] * d0[pq]).is_zero()
            if right in dims and (right[0] + 1, right[1]) in dims:
                ok &= (d1[right] * d1[pq]).is_zero()
            if diag in dims:
                a = d0[right] * d1[pq] if right in dims else 0
                b = d1[up] * d0[pq] if up in dims else 0
                ok &= (a + b) == 0
        check(ok, 'Definition 3.4.1 (i)-(iii) (%s)' % lab)
        filt, d, _, pos = total_complex(F, dims, d0, d1, 'p')
        X = Filtered(F, filt, d)          # asserts d o d = 0 on Tot
        COUNT[0] += 1                     # Definition 3.4.1: d o d = 0
        E1, E2, Hq, ind = E2_double_direct(F, dims, d0, d1, size)
        allpq = [(p, q) for p in range(size + 1) for q in range(size + 1)]
        ok1 = all(X.Edim(1, p, p + q) == E1.get((p, q), 0) for (p, q) in
                  allpq)
        ok2 = all(X.Edim(2, p, p + q) == E2.get((p, q), 0) for (p, q) in
                  allpq)
        check(ok1, 'Section 3.4 and Theorem 3.4.2: E_1^(pq) = H(E_0^(pq), '
              'd_0) and D_0^(pq) = F^p Tot (%s)' % lab)
        check(ok2, 'Theorem 3.4.2: E_2^(pq) = H^p(H^q(E_0, d_0), d_1) (%s)'
              % lab)
        # the d_1 of the double complex is j_1 k_1 (p. 107): ranks agree
        ok = all(X.dr_rank(1, p, p + q) == (rk(ind[(p, q)]) if (p, q) in ind
                                           else 0) for (p, q) in dims)
        check(ok, 'p. 107: "d_1" = j_1 k_1 is the map induced by the d_1 of '
              'the double complex (%s)' % lab)
        R = X.rinf
        higher = sum(X.dr_rank(r, p, p + q) for r in range(2, R)
                     for (p, q) in allpq)
        check(higher > 0 or nzig == 0, 'the random double complex %d has '
              'a non-zero d_r, r >= 2' % t)
        # Remark: the second spectral sequence (rows) converges to the
        # same H^*(Tot); its E_2 is H^q(H^p(E_0, d_1), d_0)
        filt2, d2, _, _ = total_complex(F, dims, d0, d1, 'q')
        Y = Filtered(F, filt2, d2)
        tdims = {(q, p): n for (p, q), n in dims.items()}
        td0 = {(q, p): A for (p, q), A in d1.items()}
        td1 = {(q, p): A for (p, q), A in d0.items()}
        _, E2b, _, _ = E2_double_direct(F, tdims, td0, td1, size)
        ok = all(Y.Edim(2, q, p + q) == E2b.get((q, p), 0)
                 for (p, q) in allpq)
        check(ok, 'Remark p. 108: the second spectral sequence, E_2 = '
              'H^q(H^p(E_0, d_1), d_0) (%s)' % lab)
        ok = True
        for n in range(0, 2 * size + 1):
            a = sum(X.Edim(R, p, n) for p in range(0, n + 1))
            b = sum(Y.Edim(Y.rinf, q, n) for q in range(0, n + 1))
            ok &= a == b == X.H(n).dim
        check(ok, 'Remark p. 108: both spectral sequences converge to '
              'H^*(Tot(E_0)) (%s)' % lab)
        # p. 108: the vertical edge homomorphism H^q(Tot) -> E_2^(0q) is the
        # restriction to the column p = 0, image in Ker(d_1)
        ok = True
        for q in range(0, size + 1):
            if (0, q) not in dims:
                ok &= X.Edim(R, 0, q) == 0
                continue
            Hn = X.H(q)
            cols = [pos[q][((0, q), i)] for i in range(dims[(0, q)])]
            proj = mat(F, len(cols), X.dim(q),
                       {(k, c): 1 for k, c in enumerate(cols)})
            img = Hq[(0, q)].cls(proj * Hn.rep())
            if (0, q) in ind:
                ok &= (ind[(0, q)] * img).is_zero()
            ok &= rk(img) == X.Edim(R, 0, q)
        check(ok, 'p. 108: the vertical edge homomorphism H^q(Tot) -> '
              'E_2^(0q) is the restriction to H^q(E_0^(0*), d_0), with image '
              'in Ker d_1 and rank dim E_infinity^(0q) (%s)' % lab)
    # signs: commuting squares do not give a differential on Tot (p. 106)
    F = GF(3)
    dims, d0, d1 = random_double(F, RNG, size=3, nz=0, nsq=2, ndot=0,
                                 anti=False)
    filt, d, _, _ = total_complex(F, dims, d0, d1, 'p')
    refuted(all((d.get(n + 1, mat(F, 0, 0)) * d[n]).is_zero()
                if n + 1 in d else True for n in d),
            'Definition 3.4.1 with d_0 d_1 = d_1 d_0 instead of (iii): d o d '
            '= 0 on Tot (GF(3))')


# ===========================================================================
# Modules over group algebras F[G] (left modules; matrices act on columns)
# ===========================================================================


class Grp:
    def __init__(self, G, name):
        self.name = name
        self.els = list(G)
        self.n = len(self.els)
        self.ix = {g: i for i, g in enumerate(self.els)}
        self.gens = [self.ix[g] for g in G.gens()]
        self.e = self.ix[G.identity()]
        self.mul = [[self.ix[a * b] for b in self.els] for a in self.els]


def kron(F, A, B):
    """Kronecker product A (x) B (sparse-safe)."""
    ent = {}
    br, bc = B.nrows(), B.ncols()
    Bd = B.dict()
    for (i, j), a in A.dict().items():
        for (k, l), b in Bd.items():
            ent[(i * br + k, j * bc + l)] = a * b
    return mat(F, A.nrows() * br, A.ncols() * bc, ent)


class Mod:
    """A left F[G]-module: act[g] for every group element g (index)."""

    def __init__(self, F, G, dim, act):
        self.F, self.G, self.dim, self.act = F, G, dim, act

    @classmethod
    def from_gens(cls, F, G, dim, genact):
        act = {G.e: ident(F, dim)}
        act.update(genact)
        frontier = list(genact)
        while frontier:
            new = []
            for a in frontier:
                for g in G.gens:
                    b = G.mul[g][a]
                    if b not in act:
                        act[b] = act[g] * act[a]
                        new.append(b)
            frontier = new
        assert len(act) == G.n
        return cls(F, G, dim, act)

    def lam(self, v):
        """The action of the group algebra element v (a vector indexed by
        the group elements)."""
        out = mat(self.F, self.dim, self.dim)
        for g, c in enumerate(v):
            if c:
                out += c * self.act[g]
        return out


def free_module(F, G, a):
    """Lambda^a with basis e_(j,h) = h e_j at index j*|G| + h."""
    n = G.n
    act = {}
    for g in range(n):
        act[g] = mat(F, a * n, a * n, {(j * n + G.mul[g][h], j * n + h): 1
                                       for j in range(a) for h in range(n)})
    return Mod(F, G, a * n, act)


def free_map(F, G, src_rank, tgt, images):
    """The Lambda-map Lambda^src_rank -> tgt sending e_j to images[j] (column
    vectors in tgt)."""
    cols = []
    for j in range(src_rank):
        v = images[j]
        for h in range(G.n):
            cols.append(tgt.act[h] * v)
    return hcat(F, tgt.dim, cols)


def submodule(M, cols):
    """The submodule spanned (over F) by cols, assumed G-stable: basis and
    action."""
    B = colbasis(cols)
    act = {g: B.solve_right(M.act[g] * B) for g in range(M.G.n)}
    return Mod(M.F, M.G, B.ncols(), act), B


def quotient_module(M, Zs, Bs):
    Q = Quot(M.F, M.dim, Zs, Bs)
    act = {g: Q.cls(M.act[g] * Q.rep()) for g in range(M.G.n)}
    return Mod(M.F, M.G, Q.dim, act), Q


def hom_basis(M, N):
    """Basis of Hom_Lambda(M, N) as a list of matrices (dim N x dim M)."""
    F = M.F
    eqs = []
    for g in M.G.gens:
        # vec(X) column-major: N.act X - X M.act
        eqs.append(kron(F, ident(F, M.dim), N.act[g]) -
                   kron(F, M.act[g].transpose(), ident(F, N.dim)))
    A = eqs[0]
    for E in eqs[1:]:
        A = A.stack(E)
    K = kernel_cols(A)
    out = []
    for c in range(K.ncols()):
        v = K.column(c)
        out.append(mat(F, N.dim, M.dim, {(i % N.dim, i // N.dim): v[i]
                                         for i in range(len(v)) if v[i]}))
    return out


def vec(X):
    F = X.base_ring()
    ent = {}
    for (i, j), c in X.dict().items():
        ent[(j * X.nrows() + i, 0)] = c
    return mat(F, X.nrows() * X.ncols(), 1, ent)


def hom_coords(basis, X):
    """Coordinates of X in a basis of matrices."""
    F = X.base_ring()
    if not basis:
        assert X.is_zero()
        return mat(F, 0, 1)
    B = hcat(F, X.nrows() * X.ncols(), [vec(Y) for Y in basis])
    return B.solve_right(vec(X))


def random_free_complex(F, G, ranks, rng):
    """A complex of free modules Lambda^ranks[0] <- Lambda^ranks[1] <- ...
    (degrees 0, 1, ...) with random maps, each into the kernel of the
    previous one."""
    mods = [free_module(F, G, a) for a in ranks]
    dmaps = {}
    for s in range(1, len(ranks)):
        tgt = mods[s - 1]
        if s == 1:
            K = ident(F, tgt.dim)
        else:
            K = kernel_cols(dmaps[s - 1])
        imgs = []
        for _ in range(ranks[s]):
            if K.ncols() == 0:
                imgs.append(mat(F, tgt.dim, 1))
                continue
            coef = mat(F, K.ncols(), 1, {(i, 0): F(rng.randrange(
                F.characteristic())) for i in range(K.ncols())})
            imgs.append(K * coef)
        dmaps[s] = free_map(F, G, ranks[s], tgt, imgs)
    return mods, dmaps


def chain_homology_module(mods, dmaps, s):
    F = mods[0].F
    M = mods[s]
    Zs = kernel_cols(dmaps[s]) if s in dmaps else ident(F, M.dim)
    Bs = dmaps[s + 1] if s + 1 in dmaps else mat(F, M.dim, 0)
    return quotient_module(M, Zs, Bs)


# ===========================================================================
# Proposition 3.4.3 (hypercohomology), Lambda = F[G] self-injective
# ===========================================================================


def section_3_4_hyper():
    from sage.all import (CyclicPermutationGroup, KleinFourGroup,
                          SymmetricGroup)
    cases = [(GF(2), Grp(CyclicPermutationGroup(2), 'C2'), [2, 2, 1], [1, 2]),
             (GF(3), Grp(CyclicPermutationGroup(3), 'C3'), [1, 2, 1], [2, 1]),
             (GF(2), Grp(KleinFourGroup(), 'V4'), [1, 1, 1], [1, 1]),
             (GF(3), Grp(SymmetricGroup(3), 'S3'), [1, 1, 1], [1, 1]),
             (GF(2), Grp(CyclicPermutationGroup(4), 'C4'), [1, 2, 1],
              [1, 1, 1])]
    for (F, G, cr, dr) in cases:
        lab = '%s over GF(%d)' % (G.name, F.characteristic())
        Cm, Cd = random_free_complex(F, G, cr, RNG)
        Dm0, Dd0 = random_free_complex(F, G, dr, RNG)
        # D in degrees t0 .. t0 + len - 1 (shifted down by one)
        t0 = -1
        Dm = {t0 + i: Dm0[i] for i in range(len(dr))}
        Dd = {t0 + i: Dd0[i] for i in Dd0}
        Cmods = {s: Cm[s] for s in range(len(cr))}
        Cdm = {s: Cd[s] for s in Cd}
        # the double complex Hom_Lambda(C_s, D_t), total degree n = s - t
        HB = {(s, t): hom_basis(Cmods[s], Dm[t]) for s in Cmods for t in Dm}
        # components of the differential delta f = dD f - (-1)^n f dC
        comp = {}
        for (s, t), basis in HB.items():
            n = s - t
            if (s, t - 1) in HB and t in Dd:
                comp[((s, t), (s, t - 1))] = hcat(F, len(HB[(s, t - 1)]),
                    [hom_coords(HB[(s, t - 1)], Dd[t] * f) for f in basis])
            if (s + 1, t) in HB and s + 1 in Cdm:
                sign = -1 if n % 2 == 0 else 1
                comp[((s, t), (s + 1, t))] = hcat(F, len(HB[(s + 1, t)]),
                    [hom_coords(HB[(s + 1, t)], sign * f * Cdm[s + 1])
                     for f in basis])

        def tot(filt_of):
            keys, filt = {}, {}
            for (s, t), basis in sorted(HB.items()):
                n = s - t
                for i in range(len(basis)):
                    keys.setdefault(n, []).append(((s, t), i))
                    filt.setdefault(n, []).append(filt_of(s, t))
            pos = {n: {k: a for a, k in enumerate(v)} for n, v in
                   keys.items()}
            d = {}
            for n in keys:
                if n + 1 not in keys:
                    continue
                ent = {}
                for ((a, b), A) in comp.items():
                    if a[0] - a[1] != n:
                        continue
                    for (r, c), x in A.dict().items():
                        key = (pos[n + 1][(b, r)], pos[n][(a, c)])
                        ent[key] = ent.get(key, F(0)) + x
                d[n] = mat(F, len(keys[n + 1]), len(keys[n]), ent)
            return Filtered(F, filt, d)

        XI = tot(lambda s, t: -t)       # spectral sequence I: p = -t, q = s
        XII = tot(lambda s, t: s)       # spectral sequence II: p = s, q = -t
        COUNT[0] += 1                   # delta o delta = 0 (asserted)
        # E_2 of I: Ext^p(H_q(C), D) = H^p(Hom_Lambda(H_q(C), D_(-p)))
        E2I = {}
        for q in Cmods:
            Hq, _ = chain_homology_module(Cm, Cd, q)
            hb = {t: hom_basis(Hq, Dm[t]) for t in Dm}
            dm = {t: hcat(F, len(hb[t - 1]), [hom_coords(hb[t - 1],
                  Dd[t] * f) for f in hb[t]]) for t in Dm if t - 1 in Dm}
            for t in Dm:
                out = rk(dm[t]) if t in dm else 0
                inn = rk(dm[t + 1]) if t + 1 in dm else 0
                E2I[(-t, q)] = len(hb[t]) - out - inn
        # E_2 of II: Ext^p(C, H_(-q)(D)) = H^p(Hom_Lambda(C_p, H_(-q)(D)))
        E2II = {}
        for t in Dm:
            Ht, _ = chain_homology_module([Dm[k] for k in sorted(Dm)],
                                          {k - t0: Dd[k] for k in Dd},
                                          t - t0)
            hb = {s: hom_basis(Cmods[s], Ht) for s in Cmods}
            dm = {s: hcat(F, len(hb[s + 1]), [hom_coords(hb[s + 1],
                  f * Cdm[s + 1]) for f in hb[s]]) for s in Cmods
                  if s + 1 in Cmods}
            for s in Cmods:
                out = rk(dm[s]) if s in dm else 0
                inn = rk(dm[s - 1]) if s - 1 in dm else 0
                E2II[(s, -t)] = len(hb[s]) - out - inn
        okI = all(XI.Edim(2, p, p + q) == E2I[(p, q)] for (p, q) in E2I)
        okII = all(XII.Edim(2, p, p + q) == E2II[(p, q)] for (p, q) in E2II)
        check(okI, 'Proposition 3.4.3 and its proof: the double complex '
              'Hom(C, I) (I = D, injective) has E_2^(pq) = Ext^p(H_q(C), D) '
              '(%s)' % lab)
        check(okII, 'Proposition 3.4.3: the double complex Hom(P, D) (P = C, '
              'projective) has E_2^(pq) = Ext^p(C, H_(-q)(D)) (%s)' % lab)
        ok = True
        ns = range(min(XI.degs), max(XI.degs) + 1)
        for n in ns:
            ext = XI.H(n).dim
            a = sum(XI.Edim(XI.rinf, p, n) for p in range(XI.fmin, XI.fmax
                                                          + 1))
            b = sum(XII.Edim(XII.rinf, p, n) for p in range(XII.fmin,
                                                            XII.fmax + 1))
            ok &= a == b == ext
        check(ok, 'Proposition 3.4.3: both spectral sequences converge to '
              'Ext^(p+q)(C, D) = H^(p+q)(Hom(C, D)) (%s)' % lab)


# ===========================================================================
# Proposition 3.4.4
# ===========================================================================


def tensor_complex(F, G, Cm, Cd, Dmods, Ddm):
    """C (x)_Lambda D for C a complex of free modules over a commutative
    Lambda = F[G] (Cm[s] = Lambda^a_s, Cd[s] the F-matrix of d_s, a
    Lambda-map), D a complex of modules (Dmods[t], Ddm[t] : D_t -> D_(t-1)).
    C_s (x) D_t = D_t^(a_s); d = dC (x) 1 + (-1)^s 1 (x) dD."""
    n = G.n
    # the Lambda-matrix of dC: entry (i, j) = coordinates of d(e_j) in the
    # summand i
    lmat = {}
    for s, A in Cd.items():
        a_src, a_tgt = Cm[s].dim // n, Cm[s - 1].dim // n
        L = {}
        for j in range(a_src):
            col = A.column(j * n + G.e)
            for i in range(a_tgt):
                L[(i, j)] = [col[i * n + h] for h in range(n)]
        lmat[s] = (a_tgt, a_src, L)
    keys = {}
    for s in Cm:
        for t in Dmods:
            keys.setdefault(s + t, []).append((s, t))
    blocks = {}
    for s in Cm:
        for t in Dmods:
            a = Cm[s].dim // n
            N = Dmods[t]
            if s in lmat:
                a_tgt, a_src, L = lmat[s]
                ent = mat(F, a_tgt * N.dim, a_src * N.dim)
                for (i, j), v in L.items():
                    B = N.lam(v)
                    for (r, c), x in B.dict().items():
                        ent[i * N.dim + r, j * N.dim + c] += x
                blocks[((s, t), (s - 1, t))] = ent
            if t in Ddm:
                sign = 1 if s % 2 == 0 else -1
                blocks[((s, t), (s, t - 1))] = sign * kron(F, ident(F, a),
                                                           Ddm[t])
    dimof = {(s, t): (Cm[s].dim // n) * Dmods[t].dim for s in Cm
             for t in Dmods}
    off = {}
    for m, ks in keys.items():
        o = 0
        for k in ks:
            off[k] = o
            o += dimof[k]
    tot_dim = {m: sum(dimof[k] for k in ks) for m, ks in keys.items()}
    d = {}
    for m in keys:
        if m - 1 not in keys:
            continue
        A = mat(F, tot_dim[m - 1], tot_dim[m])
        for (src, tgt), B in blocks.items():
            if src[0] + src[1] != m:
                continue
            for (r, c), x in B.dict().items():
                A[off[tgt] + r, off[src] + c] += x
        d[m] = A
    return tot_dim, d


def chain_hdims(F, tot_dim, d):
    out = {}
    for m, n in tot_dim.items():
        z = n - (rk(d[m]) if m in d else 0)
        b = rk(d[m + 1]) if m + 1 in d else 0
        out[m] = z - b
    return out


def tensor_dim(F, G, M, N):
    """dim_F (M (x)_Lambda N) for Lambda = F[G] commutative."""
    rels = [kron(F, M.act[g], ident(F, N.dim)) - kron(F, ident(F, M.dim),
                                                       N.act[g])
            for g in G.gens]
    return M.dim * N.dim - rk(hcat(F, M.dim * N.dim, rels))


def canon(invs):
    """A finitely generated abelian group from its invariants (0 = ZZ): the
    rank and the sorted list of prime power orders of cyclic summands."""
    rank, tors = 0, []
    for a in invs:
        a = int(a)
        if a == 0:
            rank += 1
        elif a > 1:
            for p, e in ZZ(a).factor():
                tors.append(int(p) ** e)
    return rank, sorted(tors)


def ab_tensor(A, B):
    (r, s), (r2, s2) = A, B
    tors = s * r2 + s2 * r
    for x in s:
        for y in s2:
            px, py = ZZ(x).prime_divisors()[0], ZZ(y).prime_divisors()[0]
            if px == py:
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


def random_Z_complex(rng, top, pieces, exact_positive=False):
    """A complex of free abelian groups in degrees 0..top: pieces ZZ --m--> ZZ
    from degree s to s - 1 and single ZZ's, scrambled by unimodular changes
    of basis.  With exact_positive, only the pieces m = +-1 in positive
    degrees, ZZ --m--> ZZ from degree 1 to 0 and ZZ in degree 0."""
    basis = {s: 0 for s in range(top + 1)}
    edges = []
    for _ in range(pieces):
        if exact_positive:
            kind = rng.random()
            if kind < 0.4:
                s = rng.randrange(2, top + 1) if top >= 2 else 1
                m = 1
            elif kind < 0.8:
                s, m = 1, rng.choice([2, 3, 4, 6, 0])
                if m == 0:
                    basis[0] += 1
                    continue
            else:
                basis[0] += 1
                continue
            if s > top:
                continue
        else:
            s = rng.randrange(0, top + 1)
            if s == 0 or rng.random() < 0.25:
                basis[s] += 1
                continue
            m = rng.choice([1, 2, 3, 4, 6, 9])
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
    """H_n of a complex of free abelian groups, canonical form."""
    top = max(basis)
    out = {}
    for n in range(0, top + 1):
        rows = basis[n - 1] if n >= 1 else 0
        A = d[n] if n in d else _matrix(ZZ, rows, basis[n], 0)
        B = d[n + 1] if n + 1 in d else _matrix(ZZ, basis[n], 0, 0)
        C = ChainComplex({n: A.change_ring(ZZ), n + 1: B.change_ring(ZZ)},
                         degree=-1, base_ring=ZZ)
        out[n] = canon(C.homology(n).invariants())
    return out


def Z_tensor(bC, dC, bD, dD):
    """C (x)_ZZ D for complexes of free abelian groups."""
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


def Z_homology_with_coefficients(bC, dC, rel):
    """H_n(C (x)_ZZ A) for A = ZZ^c / (column span of rel), computed as
    {x : (d (x) 1) x in L_(n-1)} / (Im + L_n) with L the relation lattices
    (finitely generated modules over ZZ, Sage FGP modules)."""
    c = rel.nrows()
    rel = rel.change_ring(ZZ)
    dC = {s: A.change_ring(ZZ) for s, A in dC.items()}
    out = {}
    for n in bC:
        N = bC[n] * c
        V = ZZ ** N
        Ln = (_matrix.identity(ZZ, bC[n]).tensor_product(rel)).columns()
        if n in dC and n - 1 in bC:
            Dn = dC[n].tensor_product(_matrix.identity(ZZ, c))
            Lm = _matrix.identity(ZZ, bC[n - 1]).tensor_product(rel)
            big = Dn.augment(-Lm)
            K = big.right_kernel_matrix()
            Kx = [v[:N] for v in K.rows()]
        else:
            Kx = V.basis()
        if n + 1 in dC:
            Dp = dC[n + 1].tensor_product(_matrix.identity(ZZ, c))
            Im = Dp.columns()
        else:
            Im = []
        Kmod = V.span(list(Kx) + list(Ln))
        Wmod = V.span(list(Im) + list(Ln))
        out[n] = canon((Kmod / Wmod).invariants())
    return out


def section_3_4_tensor_homology():
    # --- the counterexample over ZZ --------------------------------------
    bC, dC = {0: 1, 1: 1}, {1: _matrix(ZZ, [[2]])}            # ZZ --2--> ZZ
    rel = _matrix(ZZ, [[2]])                                   # A = ZZ/2
    HC = Z_homology(bC, dC)
    HCA = Z_homology_with_coefficients(bC, dC, rel)            # C (x) ZZ/2
    A = canon([2])
    check(HC[1] == (0, []) and HC[0] == (0, [2]), 'counterexample: C = (ZZ '
          '--2--> ZZ) is projective, exact in positive degrees, H_0(C) = '
          'ZZ/2')
    check(HCA[1] == (0, [2]), 'Proposition 3.4.4, counterexample: '
          'H_1(C (x) ZZ/2) = ZZ/2 (D = ZZ/2 in degree 0)')
    refuted(HCA[1] == ab_tensor(HC[1], A), 'Proposition 3.4.4 as printed: '
            'H_1(C (x) D) ~ H_1(C) (x) H_0(D) = 0 for C = (ZZ --2--> ZZ), '
            'D = ZZ/2')
    refuted(HCA[1] == (0, []), 'Proposition 3.4.4 as printed, "in '
            'particular": C (x) D exact in positive degrees (C = (ZZ --2--> '
            'ZZ), D = ZZ/2)')
    # the same with D = (ZZ --2--> ZZ), a projective D exact in positive
    # degrees, by the integral homology of C (x) D
    bT, dT = Z_tensor(bC, dC, bC, dC)
    HT = Z_homology(bT, dT)
    check(HT[1] == (0, [2]) and HT[2] == (0, []) and HT[0] == (0, [2]),
          'Proposition 3.4.4, counterexample with D = (ZZ --2--> ZZ): '
          'H_*(C (x) D) = ZZ/2, ZZ/2, 0 = H_*(C (x) H_0(D)) = Tor_*(ZZ/2, '
          'ZZ/2)')
    refuted(HT[1] == ab_tensor(HC[1], A), 'Proposition 3.4.4 as printed '
            'with D = (ZZ --2--> ZZ)')
    # --- random complexes over ZZ ----------------------------------------
    n_fail, n_tor = 0, 0
    for trial in range(40):
        top = RNG.choice([2, 3])
        bC, dC = random_Z_complex(RNG, top, RNG.randrange(3, 7))
        bD, dD = random_Z_complex(RNG, 2, RNG.randrange(2, 5),
                                  exact_positive=True)
        HD = Z_homology(bD, dD)
        assert all(HD[t] == (0, []) for t in HD if t > 0)
        rel = dD[1] if 1 in dD else _matrix(ZZ, bD[0], 0, 0)
        if rel.ncols() == 0:
            rel = _matrix(ZZ, bD[0], 1, 0)
        A0 = canon(list((ZZ ** bD[0] / (ZZ ** bD[0]).span(rel.columns()))
                        .invariants()))
        check(A0 == HD[0], 'test D: H_0(D) computed two ways')
        bT, dT = Z_tensor(bC, dC, bD, dD)
        HT = Z_homology(bT, dT)
        HCA = Z_homology_with_coefficients(bC, dC, rel)
        HC = Z_homology(bC, dC)
        ok = all(HT[n] == HCA[n] for n in range(0, top + 1))
        check(ok, 'Proposition 3.4.4 (corrected): H_*(C (x) D) ~ H_*(C (x) '
              'H_0(D)) over ZZ (trial %d)' % trial)
        # universal coefficients (Weibel, Theorem 3.6.2) as an independent
        # value of H_n(C (x) A)
        ok = all(HCA[n] == ab_sum(ab_tensor(HC[n], A0),
                                  ab_tor(HC[n - 1], A0) if n else (0, []))
                 for n in range(0, top + 1))
        check(ok, 'universal coefficient theorem H_n(C (x) A) ~ H_n(C) (x) A '
              '+ Tor(H_(n-1)(C), A) (trial %d)' % trial)
        printed = all(HT[n] == ab_tensor(HC[n], A0)
                      for n in range(0, top + 1))
        tor = any(ab_tor(HC[n], A0)[1] for n in range(0, top))
        n_tor += tor
        n_fail += not printed
        check(printed == (not tor), 'the printed H_*(C) (x) H_0(D) is right '
              'exactly when Tor(H_*(C), H_0(D)) = 0 (trial %d)' % trial)
        if A0[1] == []:
            check(printed, 'Proposition 3.4.4 with H_0(D) flat (free): '
                  'H_*(C (x) D) ~ H_*(C) (x) H_0(D) (trial %d)' % trial)
    check(n_fail == n_tor and n_fail > 5, 'the printed statement fails in %d '
          'of 40 random cases over ZZ, all with a Tor term' % n_fail)
    # --- group algebras ------------------------------------------------------
    from sage.all import CyclicPermutationGroup, KleinFourGroup
    cases = [(GF(2), Grp(CyclicPermutationGroup(2), 'C2')),
             (GF(2), Grp(CyclicPermutationGroup(4), 'C4')),
             (GF(2), Grp(KleinFourGroup(), 'V4')),
             (GF(3), Grp(CyclicPermutationGroup(3), 'C3')),
             (GF(3), Grp(CyclicPermutationGroup(9), 'C9'))]
    nprinted_fail = 0
    for (F, G) in cases:
        for trial in range(4):
            lab = '%s over GF(%d), trial %d' % (G.name, F.characteristic(),
                                               trial)
            ranks = [RNG.randrange(1, 3) for _ in range(RNG.choice([2, 3,
                                                                     4]))]
            Cm0, Cd0 = random_free_complex(F, G, ranks, RNG)
            Cm = {s: Cm0[s] for s in range(len(ranks))}
            # D: exact in positive degrees, D = (K -> Lambda^b1 -> Lambda^b0)
            # with K = Ker or a longer one, or a module in degree 0
            kind = trial % 3
            b = [RNG.randrange(1, 3), RNG.randrange(1, 3)]
            Dm0, Dd0 = random_free_complex(F, G, b, RNG)
            Dm = {0: Dm0[0], 1: Dm0[1]}
            Ddm = {1: Dd0[1]}
            if kind == 0:
                K, inc = submodule(Dm0[1], kernel_cols(Dd0[1]))
                Dm[2], Ddm[2] = K, inc
            elif kind == 1:
                K, inc = submodule(Dm0[1], kernel_cols(Dd0[1]))
                Dm = {0: quotient_module(Dm0[0], ident(F, Dm0[0].dim),
                                         Dd0[1])[0]}
                Ddm = {}
            else:
                # free D_2 onto the kernel, then the kernel of that
                K, inc = submodule(Dm0[1], kernel_cols(Dd0[1]))
                gens = []
                S = mat(F, Dm0[1].dim, 0)
                for c in range(inc.ncols()):
                    v = inc.matrix_from_columns([c])
                    if not in_span(S, v):
                        gens.append(v)
                        S = hcat(F, Dm0[1].dim, [S] + [Dm0[1].act[g] * v
                                                       for g in range(G.n)])
                D2 = free_module(F, G, len(gens))
                d2 = free_map(F, G, len(gens), Dm0[1], gens)
                K3, inc3 = submodule(D2, kernel_cols(d2))
                Dm[2], Ddm[2] = D2, d2
                Dm[3], Ddm[3] = K3, inc3
            # D is exact in positive degrees
            tdims = {t: Dm[t].dim for t in Dm}
            hD = chain_hdims(F, tdims, Ddm)
            assert all(hD[t] == 0 for t in hD if t > 0)
            H0, _ = quotient_module(Dm[0], ident(F, Dm[0].dim),
                                    Ddm[1] if 1 in Ddm else
                                    mat(F, Dm[0].dim, 0))
            tdim, td = tensor_complex(F, G, Cm, Cd0, Dm, Ddm)
            lhs = chain_hdims(F, tdim, td)
            tdim2, td2 = tensor_complex(F, G, Cm, Cd0, {0: H0}, {})
            rhs = chain_hdims(F, tdim2, td2)
            printed = {s: tensor_dim(F, G, chain_homology_module(Cm0, Cd0,
                                                                 s)[0], H0)
                       for s in Cm}
            check(all(lhs.get(s, 0) == rhs.get(s, 0) for s in Cm),
                  'Proposition 3.4.4 (corrected): H_*(C (x) D) ~ H_*(C (x) '
                  'H_0(D)) (%s)' % lab)
            if any(lhs.get(s, 0) != printed[s] for s in Cm):
                nprinted_fail += 1
    check(nprinted_fail > 0, 'Proposition 3.4.4 as printed fails for '
          'group algebras too (%d of 20 cases)' % nprinted_fail)
    # the module counterexample over F_2[C_2]: C the periodic resolution of
    # the trivial module, truncated, D = trivial module
    F, G = GF(2), Grp(CyclicPermutationGroup(2), 'C2')
    one = mat(F, G.n, 1, {(G.e, 0): 1, (G.gens[0], 0): 1})
    Cm0 = [free_module(F, G, 1) for _ in range(4)]
    Cd0 = {s: free_map(F, G, 1, Cm0[s - 1], [one]) for s in (1, 2, 3)}
    Cm = {s: Cm0[s] for s in range(4)}
    triv = Mod.from_gens(F, G, 1, {G.gens[0]: ident(F, 1)})
    tdim, td = tensor_complex(F, G, Cm, Cd0, {0: triv}, {})
    lhs = chain_hdims(F, tdim, td)
    check([lhs[s] for s in range(3)] == [1, 1, 1], 'over F_2[C_2]: C = (... '
          '--(1+g)--> Lambda --(1+g)--> Lambda), D = F_2: H_s(C (x) D) = '
          'Tor_s(F_2, F_2) = F_2 for s = 0, 1, 2')
    refuted(lhs[1] == tensor_dim(F, G, chain_homology_module(Cm0, Cd0, 1)[0],
                                 triv),
            'Proposition 3.4.4 as printed over F_2[C_2] (H_1(C) = 0)')
    # --- the uses: Section 4.1 and Theorem 5.14.2 ----------------------------
    for trial in range(8):
        F = GF(RNG.choice([2, 3, 5]))
        Cv = random_field_complex(F, 3)
        Dv = random_field_complex(F, 3)
        hC, hD = chain_hdims(F, *Cv), chain_hdims(F, *Dv)
        Tv = field_tensor(F, Cv, Dv)
        hT = chain_hdims(F, *Tv)
        check(all(hT[n] == 0 for n in hT if n > 0) and hT[0] == hC[0] * hD[0],
              'Theorem 5.14.2 use (Lambda = k a field): C, D exact in '
              'positive degrees give C (x)_k D exact in positive degrees with '
              'H_0 = H_0(C) (x) H_0(D) (trial %d, GF(%d))'
              % (trial, F.characteristic()))
    for trial in range(10):
        bC, dC = random_Z_complex(RNG, 3, RNG.randrange(2, 6),
                                  exact_positive=True)
        rel = dC[1]
        A0 = canon(list((ZZ ** bC[0] / (ZZ ** bC[0]).span(rel.columns()))
                        .invariants()))
        bT, dT = Z_tensor(bC, dC, bC, dC)
        HT = Z_homology(bT, dT)
        exact = all(HT[n] == (0, []) for n in HT if 0 < n <= 3)
        check(exact == (A0[1] == []), 'Section 4.1 use: for C projective '
              'over ZZ and exact in positive degrees, C (x) C is exact in '
              'positive degrees iff Tor(H_0 C, H_0 C) = 0; with H_0(C) flat '
              'it is (trial %d)' % trial)


def random_field_complex(F, top):
    """A complex of F-vector spaces in degrees 0..top, exact in positive
    degrees: contractible pieces in positive degrees and a free part in
    degree 0, scrambled."""
    dims = {s: 0 for s in range(top + 1)}
    edges = []
    for _ in range(RNG.randrange(2, 6)):
        s = RNG.randrange(1, top + 1)
        edges.append((s, dims[s], dims[s - 1]))
        dims[s] += 1
        dims[s - 1] += 1
    dims[0] += RNG.randrange(1, 3)
    d = {}
    for s in range(1, top + 1):
        d[s] = mat(F, dims[s - 1], dims[s], {(j, i): random_nonzero(F)
                                             for (t, i, j) in edges
                                             if t == s})
    T = {}
    for s, n in dims.items():
        while True:
            A = mat(F, n, n, {(i, j): F(RNG.randrange(F.characteristic()))
                              for i in range(n) for j in range(n)})
            if rk(A) == n:
                break
        T[s] = A
    for s in d:
        d[s] = T[s - 1] * d[s] * T[s].inverse()
    return dims, d


def field_tensor(F, Cv, Dv):
    (bC, dC), (bD, dD) = Cv, Dv
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
        A = mat(F, dims[m - 1], dims[m])
        for (s, t) in keys[m]:
            blocks = []
            if s in dC:
                blocks.append(((s - 1, t), kron(F, dC[s], ident(F, bD[t]))))
            if t in dD:
                blocks.append(((s, t - 1), (1 if s % 2 == 0 else -1) *
                               kron(F, ident(F, bC[s]), dD[t])))
            for tgt, B in blocks:
                for (r, c), x in B.dict().items():
                    A[off[tgt] + r, off[(s, t)] + c] += x
        d[m] = A
    return dims, d


def main():
    section_3_1_3_2()
    section_3_2_five_term()
    section_3_3()
    section_3_4_double()
    section_3_4_hyper()
    section_3_4_tensor_homology()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
