"""Exact checks of Chapter 5, Sections 5.9-5.18 (Sage, with GAP via libgap).

Benson, *Representations and Cohomology II*, paperback edition (1998),
Chapter 5 "Varieties for modules and multiple complexes", Sections 5.9 "The
modules L_zeta" to 5.18 "Cohen-Macaulay cohomology rings", printed pp.
186-213.  Our files: content/05-09-modules-l-zeta.typ ...
content/05-18-cohen-macaulay.typ and their diagrams.  (Sections 5.1-5.8 are
checked in chapter-5a.py.)

Everything is exact linear algebra over finite fields (and Z for one
example).  Groups are GAP permutation groups turned into multiplication
tables; modules are given by the matrices of all group elements.  For a
p-group G the minimal resolution P of k is computed degree by degree (free
modules F[G]^b, generators completing the radical), Omega^n k is the image of
d_n, a class of H^n(G, k) is its vector of values on the generators of P_n,
zeta-hat : Omega^n k -> k is read off from it, and Yoneda products are
composites with lifted chain maps (hat(zeta_1 zeta_2) = hat(zeta_1) o
Omega^r(hat(zeta_2))); L_zeta is the kernel of zeta-hat (Omega^n k + Omega k
for zeta = 0).  "zeta annihilates Ext^*(M, M)" is tested as zeta . id_M = 0
in H^n(G, End_k(M)) (a coboundary test).  Isomorphism and decomposition use
the GAP MeatAxe; free summands of modules for p-groups are split off by
linear algebra (the vectors v with N v independent, N the sum of the group
elements, generate a free summand).  Rank varieties are tested on all
points of P^(r-1)(F_q) over F_4, F_16 or F_9 (u_alpha = 1 + sum alpha_i (g_i
- 1)), and restrictions to <u_alpha> are computed by chain maps from the
periodic resolution of F[u]/(u - 1)^p.  For D_4q the projective variety of a
module is computed through the elementary abelian subgroups <x, c>, <y, c>
(c = (xy)^q), i.e. through Theorems 5.7.8 (stratification) and 5.8.3 (rank
varieties) of Sections 5.7-5.8, as the set of points (res x1 : res x2 : res
z) (weights 1, 1, 2) at the alpha with M restricted to <u_alpha> not free.
For GL_3(F_2), A_6, S_3 and A_4 the minimal resolution of k is computed in
GAP with projective covers built from projective indecomposables (summands
of modules induced from p'-subgroups); the multiplicity of P_S in P_n is
dim Ext^n(k, S).  Expected values are the book's statements, read off the
printed pages (page and our label in the messages); the chapter files are
not parsed.  Where the printed text was corrected, the printed reading is
kept as a refuted check next to the corrected one.

Checked here:

5.9 (pp. 186-191)
  * p. 186: L_zeta restricted to H is L_(res zeta) + projective (res zeta
    != 0) or Omega^n k + Omega k + projective (res zeta = 0): D8, all
    non-zero classes of degrees 1, 2, H = <x, c>, <xy>, <x>.
  * Proposition 5.9.1 in the rank-variety form of the proof: V4 (degrees
    1-3, all 25 classes, 17 points over F_16) and E8 (degrees 1, 2, all 70
    classes, 21 points over F_4): res(x_i) to <u_alpha> is alpha_i, the
    monomials form a basis of H^n, res(zeta) is the value of the polynomial
    of zeta at alpha, and L_zeta is free on <u_alpha> iff it is non-zero,
    k + Omega k + free otherwise; E9 = Z/3 x Z/3 over F_9 (10 points): for
    n odd dim L_zeta = -2 mod 3, zeta^2 = 0 and L_zeta never free on
    <u_alpha>; for n even Omega^n k = k + free on <u_alpha> and L_zeta is
    free iff res(zeta) != 0, k + Omega k + free otherwise.
  * Corollary 5.9.2 (V4, F_16; E8, F_4): the variety of a tensor product of
    L_zeta_i is the common zero set; L_x1 (x) L_x2 (x) L_x3 is projective.
  * Lemma 5.9.3 and the author's corrections on p. 188 (V4, D8, E9, (r, s) in
    {1, 2}^2, random classes, including zeta_1 zeta_2 = 0 for D8): graded
    commutativity of the products; hat(zeta_1 zeta_2) = hat(zeta_1) o
    Omega^r(hat(zeta_2)); the kernel of hat(zeta_1) o (1 (x) hat(zeta_2)) on
    Omega^r k (x) Omega^s k is L_(zeta_1 zeta_2) + projective, maps onto
    L_zeta_1 with kernel Omega^r k (x) L_zeta_2 = Omega^r L_zeta_2 +
    projective; in the middle row the right-hand entry is Omega^r k (the
    printed L_zeta_1 refuted by dimensions).
  * Lemma 5.9.4: P_(n-1)/L_zeta = Omega^-1 L_zeta + projective, the
    extension by k does not split, with quotient Omega^(n-1) k (V4, D8, E9).
  * Proposition 5.9.5: both sides compared for 5 classes and 8 modules of V4
    and 5 classes and 6 modules of D8 (both outcomes occur).
  * Proposition 5.9.6 (i) for all classes of degrees 1, 2 of V4, D8, E9, Q8;
    (ii) for E9 (all 13 classes of degree 2 up to scalars, 4 of degree 4);
    the steps of the proof for E9, n = 2, 4: dim Omega^n k = 1 mod 3,
    Lambda^2(Omega^n k) projective, S^2(Omega^n k) = Omega^(2n) k + proj,
    S^2(L_zeta) = Omega^n L_zeta + proj, Lambda^2(L_zeta) = Omega L_zeta +
    proj, L_zeta (x) L_zeta = Omega L_zeta + Omega^n L_zeta + proj, and the
    complexes Lambda^2(C), S^2(C') built from C (x) C with the Koszul
    signs are exact except where the text says.
  * The Remark on p. 191: <x^2, xy> is quaternion of order 8 in the
    semidihedral group of order 16 and zeta^n != 0, but zeta^n DOES
    annihilate Ext^*(L_(zeta^n), L_(zeta^n)) for n = 2, 3, 4 (two
    independent tests: the coboundary test and the module criterion of
    Proposition 5.9.5); the printed statement is kept as a refuted check
    (see the part log; the same holds for the other two degree one
    classes and for n = 5, computed separately).  The phenomenon itself
    occurs in characteristic two: V4, zeta = x1^2 + x1 x2 + x2^2 does not
    annihilate Ext(L_zeta, L_zeta), nor does x1 + w x2 (w in F_4, not in F_2),
    while x1, x2, x1 + x2 do.
  * The Exercise (p. 191) for Z/3 x Z/3 and the four Bockstein classes up to
    scalars (inflations of the generator of H^2(Z/3)): L = Omega^2 L, L !=
    Omega L, a map L -> F_3 split on some subgroup of order 3 and none for
    Omega L, L (x) L = L (x) Omega L = Omega L (x) Omega L (so
    ([L] - [Omega L])^2 = 0 in a(G), [L] - [Omega L] != 0).

5.10 (pp. 191-193)
  * Q8: H^n dimensions 1, 2, 2, 1, ... (n <= 9), Omega^4 k = k (period 4),
    every class of degree 1, 2, 3 nilpotent and a class of degree 4 acting
    invertibly in degrees <= 8 (Proposition 5.10.2 for M = k); C3 the same
    with period 2; Corollary 5.10.6: Omega^4 M = M for five Q8-modules;
    Corollary 5.10.7: period one for the even dimensional V4-modules
    V_(n, alpha) (n <= 3, alpha in P^1(F_4)) and for k induced from a
    subgroup of order 2 of E8, period two for k induced from the subgroups
    of order 3 of E9.
  * Theorem 5.10.4 on all D8 string modules of length <= 6: dimensions of
    Omega^n M bounded iff Omega^2 M = M; for the periodic ones a degree one
    class (x1 or x2) generates the periodicity and M = Omega M.

5.11 (pp. 192-194)
  * Lemma 5.11.1 and Theorem 5.11.2 (Andrews) for Q8, D8 over V4, C4 over C2
    (epsilon = 1), C9 over C3 and the extraspecial group of order 27 and
    exponent 3 over E9 (epsilon = 2), N central of order p, r <= 4, 3, 3,
    2, 2, on 4-8 inflated modules each: (i)-(iv) agree, and (v), (vi)
    (rank varieties over F_16, F_9) when G/N is elementary abelian; both
    outcomes occur.  The corrected first display of the proof (p. 193):
    Omega_G(M) restricted to N is M restricted to N + projective.

5.12 (pp. 194-195)
  * Theorem 5.12.1: L_(x1 x2) and L_(x1 x2 (x1 + x2)) for V4 split into 2,
    3 summands with the points as varieties; over F_2 (not algebraically
    closed) L_(x1^2 + x1 x2 + x2^2) is indecomposable and splits over F_4;
    E8: L_(x1 x3) (x) L_(x2 x3) has variety point u line (disjoint in P^2)
    and each summand lies over one of them, both occurring.

5.13 (pp. 195-198)
  * q = 1: Omega^n(k), -3 <= n <= 3, indecomposable with variety V_G;
    L_(zeta^m) (m <= 4, zeta in P^1(F_4)) indecomposable, with variety the
    point V<zeta>, isomorphic to V_(m, alpha) of Volume I, Theorem 4.3.3.
  * H^*(D_4q, F_2) = k[x1, x2, z]/(x1 x2) in degrees <= 8 (q = 2), <= 6
    (q = 4), with x1, x2 the homomorphisms with kernels <xyx, y>, <x, yxy>;
    Omega^(2r) k = M(W_r) of dimension 4qr + 1, and the identification of
    p. 198 (x1^(2(r-s)) z^s <-> z_(2q(2r-s)), x2^(2(r-s)) z^s <-> z_(2qs))
    for r <= 3 (q = 2), r <= 2 (q = 4), z being defined by the case r = 1;
    the other labelling of x1, x2 refuted.
  * p. 197 in k D_4q (q = 2, 4, 8): 1 + xyx = Y + XY + YX + XYX, G~ =
    (XY)^q, H~ = ((1 + xyx)(1 + y))^(q/2) = ((Y + XY + YX + XYX) Y)^(q/2) =
    (YXY + XYXY)^(q/2) = (YX)^(q-1) Y + (XY)^q.
  * Theorem 5.13.1 (i): every string module of length <= 7 (q = 2, 4) and
    the special words for r <= 2 (q = 2), r <= 1 (q = 4): the projective
    variety (on the image points over F_16), periodicity, freeness on <x>
    and <y>; the periodic M(C) have period ONE (the printed "period two"
    refuted, corrected to "period dividing two").
  * Theorem 5.13.1 (ii), (iii): every band word of length <= 8 (q = 2) and
    of length 8 (q = 4), both orientations, phi = J_1(lambda), J_2(lambda),
    lambda in F_4^*: V = {infinity} unless C ~ a^-1 b (ab)^(q-1) or
    b^-1 a (ba)^(q-1); for C a rotation of a^-1 b (ab)^(q-1) the point is
    (lambda^-1)_a in the schema of Volume I (the printed lambda_a refuted for
    lambda not in F_2; see the part log), for its inverse lambda_a, and
    likewise for b; M((ab)^q (ba)^-q, id) = kG.  The proof: G~ acts as zero,
    M(C, phi) is projective on H = <xyx, y> iff (YX)^(q-1) Y has rank
    dim/2q iff C ~ a^-1 b (ab)^(q-1)^(+-1) iff V misses P^1_b (corrected;
    the printed "misses P^1_a" refuted by C ~ b^-1 a (ba)^(q-1)).
  * The claim of pp. 197-198 (q = 2, r <= 3; q = 4, r <= 2): zeta-hat in the
    basis z_i is as printed; L_zeta = M(a^-1 b (ab)^(q-1), J_r(lambda^-1)) +
    M(b^-1 a (ba)^(q-1), J_r(mu^-1)) in the schema of Volume I (the printed
    J_r(lambda), J_r(mu) refuted); V(L_zeta) = {lambda_a, mu_b}; the printed
    phi is the matrix of X from V_0 to V_1 and is conjugate to J_r(lambda)
    (r <= 6); the subspaces L_zeta cap <z_2qr, ..., z_4qr> and L_zeta cap
    <z_0, ..., z_2qr> are not submodules (refuted).

5.14 (pp. 199-205)
  * C_zeta has homology k in degrees 0 and n - 1 and C_zeta^(oo) is exact
    except H_0 = k (V4, D8, C3, E9; 10 complexes).
  * Theorem 5.14.2: V4 with (x1^2, x2^2), (x1^2, x2^3); D8 with ((x1 +
    x2)^2, z) and M = k, and with x2^2 and M = M(aba): the top module is
    projective iff the classes cover the variety (non-covering cases
    included), C is a finite complex of projectives with the Kunneth
    homology, and C^(oo) (x) ... (x) M is a projective resolution of M in
    degrees <= 6 (the use of Proposition 3.4.4: tensor products over k).
  * Lemma 5.14.4 in dimensions: dim Ext^j(P_(n-1)/L_zeta, k) = dim Coker(
    zeta : H^(j-1) -> H^(j+n-1)) + dim Ker(zeta : H^j -> H^(j+n)) (V4, D8,
    E9; 8 classes, j small).
  * pp. 201-202: the minimal resolution of k for GL_3(F_2) (char 2, n <=
    10) and for A_6 (char 3, over F_9, n <= 13) has in each degree the
    projective indecomposables of the total complex of the printed double
    complex (our diagrams gl3-resolution and a6-resolution; the printed
    region of the A_6 diagram determines degrees <= 13); L and M are not
    distinguished by the book and are compared as a pair.
  * Corollary 5.14.6 for C_p over Z (p = 2, 3, 5): H_0 = H_1 = Z with
    trivial action; R (x) C for R = F_p, Z/p^2, Q.
  * p. 205: for C = C_x1^2 (x) C_x2^2 (V4), H_1(C) = k^2, so the rows of the
    last spectral sequence are sums of two copies (printed "each isomorphic
    to" refuted); for M = k + k, E_2^(0*) is not a free module dual to H_*(C).

5.15-5.16 (pp. 205-208)
  * Tate cohomology from the complete resolution (degrees -4..3) for C3, V4,
    D8 and 4-5 modules each: Tate^n = H^n (n > 0), Tate^0 = M^G/Tr(M),
    Tate^-1 = Ker N / I M, Tate^(-n-1) = H_n (n > 0); the graded reading
    "Tate^* = H^*" refuted in degree 0 for M = kG.
  * Theorem 5.15.2: Tate^n(S3, sign) in characteristic 3 (n <= 12 and by
    duality n >= -12) vanishes in runs of exactly two and is not zero.
  * The bidegree (k, 1 - k) of d_k (printed (k, -k - 1) refuted) and the
    index argument of the proof for r <= 6.
  * S3 (char 2): H^n(S3, F_2) = F_2 = H^n(C2, F_2), n <= 8 (mod 2 cohomology
    does not detect the isomorphism type; Theorem 5.16.1 uses Z).

5.17-5.18 (pp. 208-213)
  * Proposition 5.17.2: lambda_n = (-1)^(n(n+1)/2) for C3, C5 (n <= 6), C7
    (n <= 5), E9 (n <= 3) and V4 (char 2): a chain map from the resolution
    to the dual sequence with transposed maps, lifting zeta-hat^*; the
    printed label (-1)^(n(n-1)/2) of the last diagram refuted for odd n.
  * Theorem 5.17.3, Corollary 5.17.4: C for V4 (x1^2, x2^3), (x1^2, x2^2),
    D8 ((x1 + x2)^2, z), Q8 (degree 4), E9 (two Bocksteins), C3 (x^2): the
    dimensions of H^i(Hom_kG(C, k)) are palindromic of length s + 1 and
    equal those of H^*(G, k)/(zeta_i) (Theorem 5.18.1); for V4 with
    (x1^2, x2^3) the numbers dim Hom_kG(C_i, k) = 4, 12, 14, 6 are not (the
    printed Corollary 5.17.4 refuted, corrected to H^i(Hom_kG(C, k))).
  * Theorem 5.18.1: the Poincare series of V4, E8, E9, C3, C9, D8, D16, Q8,
    C4 x C2 (n <= 13) and GL_3(F_2) give a palindromic f(t) and p(1/t) =
    (-t)^r p(t); for SD16 (not Cohen-Macaulay) the series is (1 + t)/((1 -
    t)(1 - t^4)) (n <= 16) and p(1/t) = t^4 p(t), not t^2 p(t).  Corollary 5.18.2: S3
    (polynomial, S3/O_2'(S3) = C2) and A4 (not), and the degree count.

Not established here: anything for general groups or modules (each check is
a finite computation on the named groups, modules, classes and degrees);
varieties over the algebraic closure (only the points over the finite field
used); the existence of the double complexes on pp. 201-202 (only the terms
of the minimal resolutions are compared); the convention for band modules
is the schema of Volume I as implemented in Volume I's checks (an inverse
first letter acts by phi^-1).
"""
import itertools
import random

from sage.all import (GF, ZZ, QQ, Zmod, matrix as _matrix, vector, libgap,
                      binomial, PolynomialRing)

SCOPE = 'chapter-5b'
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
# Linear algebra (sparse in odd characteristic: dense products over GF(p),
# p odd, stop with SIGILL in the local OpenBLAS build)
# ===========================================================================


def _sp(F):
    return F.characteristic() != 2


def mat(F, r, c, entries=None):
    return _matrix(F, r, c, entries or {}, sparse=_sp(F))


def ident(F, n):
    return mat(F, n, n, {(i, i): 1 for i in range(n)})


def conv(A, F=None):
    """A copy of A over F in the storage convention of F."""
    F = A.base_ring() if F is None else F
    B = A.change_ring(F)
    if _sp(F) and not B.is_sparse():
        B = B.sparse_matrix()
    if not _sp(F) and B.is_sparse():
        B = B.dense_matrix()
    return B


def hcat(F, n, mats):
    mats = [A for A in mats if A.ncols()]
    if not mats:
        return mat(F, n, 0)
    out = mats[0]
    for A in mats[1:]:
        out = out.augment(A)
    return out


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
    """Columns: a basis of the right kernel of A."""
    F = A.base_ring()
    if A.ncols() == 0:
        return mat(F, 0, 0)
    if A.nrows() == 0:
        return ident(F, A.ncols())
    return conv(A.right_kernel_matrix().transpose(), F)


def colbasis(A):
    """Independent columns of A spanning its column space."""
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
    """A finite group on the elements 0..n-1 (GAP's sorted list), with the
    given generators (GAP elements) in the given order."""

    def __init__(self, G, gens, name):
        els = libgap.AsSSortedList(G)
        tbl = libgap.MultiplicationTable(els).sage()
        self.n = len(tbl)
        self.mul = [[x - 1 for x in row] for row in tbl]
        self.gap, self.els, self.name = G, els, name
        self.e = self.index(libgap.One(G))
        self.gens = [self.index(g) for g in gens]
        self.inv = [0] * self.n
        for a in range(self.n):
            for b in range(self.n):
                if self.mul[a][b] == self.e:
                    self.inv[a] = b
                    break
        self.src = [[self.mul[self.inv[h]][t] for t in range(self.n)]
                    for h in range(self.n)]

    def index(self, g):
        return int(libgap.Position(self.els, g)) - 1

    def word(self, w):
        """The element of a word in the generators (list of indices into
        gens, applied left to right as a product g_w0 g_w1 ...)."""
        a = self.e
        for i in w:
            a = self.mul[a][self.gens[i]]
        return a

    def closure(self, elts):
        S = {self.e}
        frontier = [self.e]
        while frontier:
            new = []
            for a in frontier:
                for g in elts:
                    b = self.mul[a][g]
                    if b not in S:
                        S.add(b)
                        new.append(b)
            frontier = new
        return sorted(S)

    def power(self, g, k):
        a = self.e
        for _ in range(k):
            a = self.mul[a][g]
        return a


def subgroup_grp(G, elts, name):
    """The subgroup generated by elts (indices of G) as a Grp, with the
    inclusion list (sub-index -> G-index)."""
    H = libgap.Subgroup(G.gap, [G.els[g] for g in elts])
    S = Grp(H, [G.els[g] for g in elts], name)
    incl = [G.index(S.els[i]) for i in range(S.n)]
    return S, incl


# ===========================================================================
# Modules (left, on columns) over F[G]: matrices of all group elements
# ===========================================================================


class Mod:
    def __init__(self, F, G, dim, act):
        self.F, self.G, self.dim, self.act = F, G, dim, act

    @classmethod
    def from_gens(cls, F, G, genact):
        dim = genact[0].nrows()
        act = {G.e: ident(F, dim)}
        frontier = [G.e]
        while frontier:
            new = []
            for a in frontier:
                for g, A in zip(G.gens, genact):
                    b = G.mul[g][a]
                    if b not in act:
                        act[b] = A * act[a]
                        new.append(b)
            frontier = new
        assert len(act) == G.n, 'generators do not give a group action'
        M = cls(F, G, dim, [act[g] for g in range(G.n)])
        for a in range(G.n):
            for g in G.gens:
                assert M.act[G.mul[g][a]] == M.act[g] * M.act[a], \
                    'not a module'
        return M

    def X(self, g):
        return self.act[g] - ident(self.F, self.dim)

    def change_ring(self, F):
        return Mod(F, self.G, self.dim, [conv(A, F) for A in self.act])

    def elem(self, coeffs):
        """The matrix of an element sum c_g g of F[G] (dict g -> c)."""
        out = mat(self.F, self.dim, self.dim)
        for g, c in coeffs.items():
            if c:
                out += c * self.act[g]
        return out


def trivial(F, G):
    return Mod(F, G, 1, [ident(F, 1) for _ in range(G.n)])


def regular(F, G):
    return Mod(F, G, G.n, [mat(F, G.n, G.n, {(G.mul[h][t], t): 1
                                             for t in range(G.n)})
                           for h in range(G.n)])


def free(F, G, m):
    if m == 0:
        return Mod(F, G, 0, [mat(F, 0, 0) for _ in range(G.n)])
    R = regular(F, G)
    return dsum(*([R] * m))


def dual(M):
    return Mod(M.F, M.G, M.dim, [M.act[M.G.inv[g]].transpose()
                                 for g in range(M.G.n)])


def tensor(M, N):
    return Mod(M.F, M.G, M.dim * N.dim,
               [M.act[g].tensor_product(N.act[g]) for g in range(M.G.n)])


def dsum(*Ms):
    Ms = [M for M in Ms if M.dim]
    if len(Ms) == 1:
        return Ms[0]
    M0 = Ms[0]
    return Mod(M0.F, M0.G, sum(M.dim for M in Ms),
               [_bdiag(M0.F, [M.act[g] for M in Ms])
                for g in range(M0.G.n)])


def _bdiag(F, mats):
    out = mats[0]
    for A in mats[1:]:
        out = out.block_sum(A)
    return conv(out, F)


def sub(M, K):
    """The submodule with basis the columns of K (full column rank,
    invariant)."""
    piv = K.transpose().pivots() if K.ncols() else ()
    Kp = K.matrix_from_rows(piv)
    Kpi = Kp.inverse()
    act = []
    for g in range(M.G.n):
        A = M.act[g] * K
        assert in_span(K, A), 'not a submodule'
        act.append(Kpi * A.matrix_from_rows(piv))
    return Mod(M.F, M.G, K.ncols(), act)


def is_invariant(M, K):
    return all(in_span(K, M.act[g] * K) for g in M.G.gens)


def quot(M, K):
    """M / (span of the columns of K): (module, projection matrix)."""
    F, n, k = M.F, M.dim, K.ncols()
    B = colbasis(K.augment(ident(F, n)))
    Bi = B.inverse()
    act = [(Bi * M.act[g] * B).submatrix(k, k, n - k, n - k)
           for g in range(M.G.n)]
    return Mod(F, M.G, n - k, act), Bi.submatrix(k, 0, n - k, n)


def restrict(M, H, incl):
    return Mod(M.F, H, M.dim, [M.act[incl[h]] for h in range(H.n)])


def rad_cols(M):
    """J(F[G]) M = sum over generators of (g - 1) M (G a p-group)."""
    return colbasis(hcat(M.F, M.dim, [M.X(g) for g in M.G.gens]))


def top_dim(M):
    return M.dim - rk(hcat(M.F, M.dim, [M.X(g) for g in M.G.gens]))


def is_free(M):
    """M free over F[G], G a p-group."""
    return top_dim(M) * M.G.n == M.dim


def norm_rank(M):
    """Number of free summands of M (G a p-group): rank of sum_g g."""
    return rk(M.elem({g: 1 for g in range(M.G.n)}))


def fixed(M):
    return kernel_cols(vcat(M.F, M.dim, [M.X(g) for g in M.G.gens]))


# --- free modules F[G]^b: basis index j n + t <-> t e_j ----------------------


def act_free(G, b, h, X):
    """h . X for columns X of F[G]^b."""
    if h == G.e:
        return X
    n = G.n
    return X.matrix_from_rows([j * n + G.src[h][t] for j in range(b)
                               for t in range(n)])


def free_map(F, G, b_src, X):
    """F[G]^(b_src) -> F[G]^b, e_i |-> column i of X; the column i n + g of
    the result is g X_i."""
    n = G.n
    b = X.nrows() // n
    Y = hcat(F, X.nrows(), [act_free(G, b, g, X) for g in range(n)])
    return Y.matrix_from_columns([g * b_src + i for i in range(b_src)
                                  for g in range(n)])


def mod_map(M, X):
    """F[G]^b -> M, e_i |-> column i of X (column i n + g = g X_i)."""
    F, G = M.F, M.G
    b = X.ncols()
    Y = hcat(F, M.dim, [M.act[g] * X for g in range(G.n)])
    return Y.matrix_from_columns([g * b + i for i in range(b)
                                  for g in range(G.n)])




def min_gen_cols(K, JK):
    """Columns of K completing a basis of span(JK) to one of span(K)."""
    JB = colbasis(JK) if JK.ncols() else JK
    nb = JB.ncols()
    allc = JB.augment(K) if nb else K
    return [c - nb for c in allc.pivots() if c >= nb]


def proj_cover(M):
    """(b, X, pi): minimal generators X (columns) of M (G a p-group) and the
    map pi : F[G]^b -> M."""
    I = ident(M.F, M.dim)
    gens = min_gen_cols(I, hcat(M.F, M.dim, [M.X(g) for g in M.G.gens]))
    X = I.matrix_from_columns(gens)
    return len(gens), X, mod_map(M, X)


def omega(M, k=1):
    """Omega^k M (k >= 0) for a p-group, as a module."""
    for _ in range(k):
        if M.dim == 0:
            return M
        b, X, pi = proj_cover(M)
        K = kernel_cols(pi)
        Fb = free(M.F, M.G, b)
        M = sub(Fb, K) if K.ncols() else Mod(M.F, M.G, 0,
                                             [mat(M.F, 0, 0)] * M.G.n)
    return M


def omega_inv(M, k=1):
    return dual(omega(dual(M), k))


# ===========================================================================
# The minimal resolution of the trivial module and Yoneda products
# ===========================================================================


class Resolution:
    """Minimal resolution P_* -> F over F[G] (G a p-group), n <= nmax:
    b[k] generators, d[k] : P_k -> P_(k-1)."""

    def __init__(self, F, G, nmax):
        self.F, self.G, self.N = F, G, nmax
        n = G.n
        self.eps = mat(F, 1, n, {(0, t): 1 for t in range(n)})
        self.b = [1]
        self.d = {}
        prev = self.eps
        for k in range(1, nmax + 1):
            bp = self.b[k - 1]
            K = kernel_cols(prev)
            JK = hcat(F, K.nrows(), [act_free(G, bp, g, K) - K
                                     for g in G.gens])
            gens = min_gen_cols(K, JK)
            X = K.matrix_from_columns(gens)
            self.b.append(len(gens))
            self.d[k] = free_map(F, G, len(gens), X)
            assert rk(self.d[k]) == K.ncols()
            prev = self.d[k]
        self.x0 = mat(F, n, 1, {(G.e, 0): 1})
        self._om = {}

    def dim(self, k):
        return self.b[k] * self.G.n

    def gen_cols(self, k):
        n, e = self.G.n, self.G.e
        return self.d[k].matrix_from_columns([i * n + e
                                              for i in range(self.b[k])])

    def omega(self, k):
        """(Omega^k F as a module, basis B in P_(k-1)), k >= 1."""
        if k not in self._om:
            B = colbasis(self.d[k])
            Pm = free(self.F, self.G, self.b[k - 1])
            self._om[k] = (sub(Pm, B), B)
        return self._om[k]

    def collapse_row(self, k, alpha):
        """The cochain P_k -> F of alpha in F^(b_k) (values on generators)."""
        n = self.G.n
        return mat(self.F, 1, self.b[k] * n,
                   {(0, j * n + t): alpha[j] for j in range(self.b[k])
                    for t in range(n) if alpha[j]})

    def hat(self, k, alpha):
        """zeta-hat : Omega^k F -> F of the class alpha (row vector in the
        basis B of Omega^k F)."""
        Om, B = self.omega(k)
        U = self.d[k].solve_right(B)
        return self.collapse_row(k, alpha) * U

    def cocycle_of_hat(self, k, row):
        """The class (values on generators of P_k) of a map Omega^k -> F
        given as a row vector in the basis B."""
        Om, B = self.omega(k)
        C = B.solve_right(self.gen_cols(k))
        return vector(self.F, (row * C).row(0))


def collapse(F, G, X, b):
    """Block sums of the columns X of F[G]^b: values of trivial cochains."""
    n = G.n
    S = mat(F, b, b * n, {(j, j * n + t): 1 for j in range(b)
                          for t in range(n)})
    return S * X


class Cohom:
    """H^*(G, F) (G a p-group) from the minimal resolution: H^n = F^(b_n),
    Yoneda products by lifting chain maps."""

    def __init__(self, P):
        self.P, self.F, self.G = P, P.F, P.G
        self.b = P.b
        self._lifts = {}

    def lift(self, m, alpha, kmax):
        """tau_k : P_(m+k) -> P_k (generator images) lifting alpha in H^m."""
        key = (m, tuple(alpha))
        tau = self._lifts.setdefault(key, {})
        F, G, P = self.F, self.G, self.P
        for k in range(kmax + 1):
            if k in tau or m + k > P.N:
                continue
            bmk = self.b[m + k]
            if k == 0:
                tau[0] = P.x0 * mat(F, 1, bmk, {(0, i): alpha[i]
                                                for i in range(bmk)
                                                if alpha[i]})
            else:
                full = free_map(F, G, self.b[m + k - 1], tau[k - 1])
                tau[k] = P.d[k].solve_right(full * P.gen_cols(m + k))
        return tau

    def mul(self, beta, l, alpha, m):
        """The Yoneda composite beta o alpha in H^(l+m) (beta in H^l, alpha
        in H^m): beta-hat o Omega^l(alpha-hat)."""
        tau = self.lift(m, list(alpha), l)
        C = collapse(self.F, self.G, tau[l], self.b[l])
        return vector(self.F, (mat(self.F, 1, self.b[l],
                                   {(0, i): beta[i] for i in range(self.b[l])
                                    if beta[i]}) * C).row(0))

    def power(self, alpha, m, e):
        out, deg = vector(self.F, alpha), m
        for _ in range(e - 1):
            out = self.mul(out, deg, alpha, m)
            deg += m
        return out

    def mult_matrix(self, alpha, m, k):
        """beta |-> beta o alpha : H^k -> H^(k+m) as a matrix."""
        F = self.F
        cols = []
        for i in range(self.b[k]):
            e = vector(F, [1 if j == i else 0 for j in range(self.b[k])])
            cols.append(self.mul(e, k, alpha, m))
        if not cols:
            return mat(F, self.b[k + m], 0)
        return conv(_matrix(F, cols).transpose(), F)

    def class_of_hom(self, chi):
        """The class in H^1 of a homomorphism chi : G -> F (list over the
        elements): its value on the generators of P_1."""
        P, F, G = self.P, self.F, self.G
        out = []
        for i in range(self.b[1]):
            col = P.gen_cols(1).column(i)
            out.append(sum(col[j * G.n + t] * chi[t]
                           for j in range(self.b[0]) for t in range(G.n)))
        return vector(F, out)

    def is_cocycle_hom(self, chi):
        G = self.G
        return all(chi[G.mul[a][b]] == chi[a] + chi[b]
                   for a in range(G.n) for b in range(G.n))

    def omega_map(self, m, alpha, r):
        """Omega^r(alpha-hat) : Omega^(m+r) F -> Omega^r F (r >= 1) in the
        bases of Resolution.omega, the restriction of tau_(r-1)."""
        P = self.P
        tau = self.lift(m, list(alpha), r)
        Om_src, Bs = P.omega(m + r)
        Om_tgt, Bt = P.omega(r)
        T = free_map(self.F, self.G, self.b[m + r - 1], tau[r - 1])
        return Bt.solve_right(T * Bs)


def cochain_coboundary(P, M, k):
    """delta : Hom_G(P_k, M) -> Hom_G(P_(k+1), M) in the coordinates
    (psi(e_j))_j."""
    F, G = P.F, P.G
    n, m = G.n, M.dim
    Y = P.gen_cols(k + 1)
    A = mat(F, P.b[k + 1] * m, P.b[k] * m)
    for g in range(n):
        Cg = Y.matrix_from_rows([j * n + g for j in range(P.b[k])]).transpose()
        if Cg.is_zero():
            continue
        A += conv(Cg, F).tensor_product(M.act[g])
    return A


def kills_identity(P, alpha, n, M):
    """True iff zeta (alpha in H^n) maps to zero in Ext^n(M, M), i.e. zeta
    . id_M = 0 in H^n(G, End(M)): the cochain e_j |-> alpha_j id is a
    coboundary."""
    F = P.F
    E = tensor(M, dual(M))      # End_k(M) with g f g^-1; id = vec(I)
    m = E.dim
    d = M.dim
    idv = [1 if r % (d + 1) == 0 else 0 for r in range(m)]
    u = vector(F, [alpha[j] * idv[r] for j in range(P.b[n])
                   for r in range(m)])
    B = cochain_coboundary(P, E, n - 1)
    return in_span(B, conv(_matrix(F, [u]).transpose(), F))


# ===========================================================================
# MeatAxe (GAP)
# ===========================================================================

MTX_ISO = libgap.eval('MTX.IsomorphismModules')
MTX_INDEC = libgap.eval('MTX.IsIndecomposable')
MTX_DECOMP = libgap.eval('MTX.Indecomposition')
FAIL = libgap.eval('fail')


def gap_module(M):
    """The MeatAxe module of the matrices of the generators (GAP acts on
    rows: this is the dual of M, which does not matter for isomorphism and
    decomposition questions)."""
    mats = [libgap(conv(M.act[g]).dense_matrix()) for g in M.G.gens]
    return libgap.GModuleByMats(mats, libgap(M.F))


def isomorphic(M, N):
    if M.dim != N.dim:
        return False
    if M.dim == 0:
        return True
    return MTX_ISO(gap_module(M), gap_module(N)) != FAIL


def _ffe(F, c):
    try:
        return F(c)
    except TypeError:
        return c.polynomial()(F.gen())


def to_sage(F, X):
    return conv(_matrix(F, [[_ffe(F, c) for c in row] for row in X.sage()]),
                F)


def iso_matrix(M, N):
    """An isomorphism S : M -> N (S M.act = N.act S), or None."""
    if M.dim != N.dim:
        return None
    T = MTX_ISO(gap_module(M), gap_module(N))
    if T == FAIL:
        return None
    # rows: A_i T = T B_i  =>  T^(-1) A_i = B_i T^(-1)
    S = to_sage(M.F, T).inverse()
    for g in M.G.gens:
        assert S * M.act[g] == N.act[g] * S
    return S


def decompose(M):
    """Indecomposable summands (as modules)."""
    out = []
    for x in MTX_DECOMP(gap_module(M)):
        gm = x[1]
        mats = libgap.eval('x -> x.generators')(gm)
        out.append(Mod.from_gens(M.F, M.G, [to_sage(M.F, A).transpose()
                                            for A in mats]))
    return out


def is_indecomposable(M):
    return bool(MTX_INDEC(gap_module(M)))


def core(M):
    """M with its free summands removed (G a p-group): the vectors v_i with
    the N v_i independent (N the sum of the group elements) generate a free
    submodule F, which is injective, hence a summand; M / F is the rest."""
    if M.dim == 0:
        return M
    N = M.elem({g: 1 for g in range(M.G.n)})
    piv = N.pivots()
    if not piv:
        return M
    V = ident(M.F, M.dim).matrix_from_columns(piv)
    Fb = colbasis(hcat(M.F, M.dim, [M.act[g] * V for g in range(M.G.n)]))
    assert Fb.ncols() == len(piv) * M.G.n
    if Fb.ncols() == M.dim:
        return Mod(M.F, M.G, 0, [mat(M.F, 0, 0)] * M.G.n)
    return quot(M, Fb)[0]


def iso_mod_proj(A, B):
    """A = B + (projective = free), G a p-group (both given)."""
    n = A.G.n
    diff = A.dim - B.dim
    if diff < 0 or diff % n:
        return False
    cA, cB = core(A), core(B)
    return (A.dim - cA.dim) - (B.dim - cB.dim) == diff and isomorphic(cA, cB)


def iso_full(A, B):
    """A = B (Krull-Schmidt: equal dimensions and isomorphic cores)."""
    return A.dim == B.dim and iso_mod_proj(A, B)


# ===========================================================================
# Shifted cyclic subgroups (rank varieties) and restriction to them
# ===========================================================================


def shifted_T(M, Egens, alpha):
    """u_alpha - 1 = sum alpha_i (e_i - 1) on M (M over a field containing
    the alpha_i)."""
    out = mat(M.F, M.dim, M.dim)
    for a, e in zip(alpha, Egens):
        if a:
            out += a * M.X(e)
    return out


def free_on_shifted(M, Egens, alpha):
    p = M.F.characteristic()
    T = shifted_T(M, Egens, alpha)
    return rk(T ** (p - 1)) * p == M.dim


def proj_points(F, r):
    """Representatives of the points of P^(r-1)(F)."""
    out = []
    for v in itertools.product(list(F), repeat=r):
        if all(x == 0 for x in v):
            continue
        i = next(j for j in range(r) if v[j] != 0)
        if v[i] == 1:
            out.append(tuple(v))
    return out


def res_shifted(P, Egens, alpha, n, cls):
    """res to the shifted cyclic subgroup <u_alpha> of a class cls in
    H^n(G, F) (P over F containing alpha): the value of the cochain on the
    chain map image of the generator of Q_n, Q the periodic resolution of
    F over F[u]/(u - 1)^p (d = T in odd degrees, T^(p-1) in even ones)."""
    F, G = P.F, P.G
    p = F.characteristic()
    key = (tuple(Egens), tuple(alpha))
    cache = P.__dict__.setdefault('_shift', {})
    sig = cache.setdefault(key, {0: P.x0})

    def T(k, X):
        out = mat(F, X.nrows(), X.ncols())
        for a, e in zip(alpha, Egens):
            if a:
                out += a * (act_free(G, P.b[k], e, X) - X)
        return out
    for k in range(1, n + 1):
        if k in sig:
            continue
        Y = sig[k - 1]
        for _ in range(1 if (k % 2 or p == 2) else p - 1):
            Y = T(k - 1, Y)
        sig[k] = P.d[k].solve_right(Y)
    return (P.collapse_row(n, cls) * sig[n])[0, 0]


# ===========================================================================
# Dihedral 2-groups, words, string and band modules (Volume I, Section 4.11)
# ===========================================================================


def perm(images):
    return libgap.PermList([i + 1 for i in images])


def dihedral(q):
    """D_4q = <x, y | x^2 = y^2 = 1, (xy)^q = (yx)^q> with generators x, y
    (q >= 1 a power of two)."""
    if q == 1:
        x = perm([1, 0, 3, 2])
        y = perm([2, 3, 0, 1])
    else:
        m = 2 * q
        x = perm([(-i) % m for i in range(m)])
        y = perm([(1 - i) % m for i in range(m)])
    G = libgap.Group([x, y])
    assert int(libgap.Size(G)) == 4 * q
    return Grp(G, [x, y], 'D%d' % (4 * q))


# A word is a tuple of letters (c, e), c in 'ab', e = 1 (direct) or -1
# (inverse).


def letters(s):
    out = []
    for tok in s.split():
        out.append((tok[0], -1 if tok.endswith('-') else 1))
    return tuple(out)


def winv(C):
    return tuple((c, -e) for (c, e) in reversed(C))


def wpow(C, k):
    return tuple(C) * k


def wstr(C):
    return ''.join(c + ('' if e == 1 else "'") for c, e in C)


def other(c):
    return 'b' if c == 'a' else 'a'


def string_XY(F, C):
    """M(C) (Volume I, p. 137): basis z_0..z_n, the letter l_i joins
    z_(i-1) and z_i; a direct letter maps z_i to z_(i-1), an inverse letter
    z_(i-1) to z_i; X acts via the letters a, Y via b."""
    n = len(C)
    X, Y = mat(F, n + 1, n + 1), mat(F, n + 1, n + 1)
    for i, (c, e) in enumerate(C, start=1):
        T = X if c == 'a' else Y
        if e == 1:
            T[i - 1, i] = 1
        else:
            T[i, i - 1] = 1
    return X, Y


def band_XY(F, C, phi):
    """M(C, phi) (Volume I, p. 137): V_0..V_(n-1); the letter l_i between
    V_i and V_(i-1) (indices mod n) is phi for i = 1 and the identity
    otherwise; a direct letter maps V_i to V_(i-1), an inverse letter maps
    V_(i-1) to V_i by the inverse."""
    n, m = len(C), phi.nrows()
    X, Y = mat(F, n * m, n * m), mat(F, n * m, n * m)
    I = ident(F, m)
    phinv = phi.inverse()
    for i, (c, e) in enumerate(C, start=1):
        T = X if c == 'a' else Y
        src, dst = i % n, i - 1
        if e == 1:
            T.set_block(dst * m, src * m, phi if i == 1 else I)
        else:
            T.set_block(src * m, dst * m, phinv if i == 1 else I)
    return X, Y


def xy_module(F, G, XY):
    X, Y = XY
    I = ident(F, X.nrows())
    return Mod.from_gens(F, G, [I + X, I + Y])


def string_mod(F, G, C):
    return xy_module(F, G, string_XY(F, C))


def band_mod(F, G, C, phi):
    return xy_module(F, G, band_XY(F, C, phi))


def jordan(F, lam, r):
    return mat(F, r, r, dict([((i, i), lam) for i in range(r)] +
                             [((i, i + 1), 1) for i in range(r - 1)]))


def contains(C, sub):
    n, m = len(C), len(sub)
    return any(C[i:i + m] == sub for i in range(n - m + 1))


def is_word(C):
    return all(C[i][0] != C[i + 1][0] for i in range(len(C) - 1))


def all_words(n):
    out = []
    for first in [('a', 1), ('a', -1), ('b', 1), ('b', -1)]:
        cur = [(first,)]
        for _ in range(n - 1):
            cur = [w + ((other(w[-1][0]), e),) for w in cur for e in (1, -1)]
        out += cur
    return out


def forbidden(q):
    A = wpow(letters('a b'), q)
    B = wpow(letters('b a'), q)
    return [A, B, winv(A), winv(B)]


def string_ok(C, q):
    return not any(contains(C, f) for f in forbidden(q))


def rot(C, i):
    return C[i:] + C[:i]


def is_primitive(C):
    n = len(C)
    return all(C != rot(C, d) for d in range(1, n) if n % d == 0)


def band_ok(C, q):
    """C of even length, alternating cyclically, no power containing
    (ab)^q, (ba)^q or inverses, not a proper power."""
    n = len(C)
    if n % 2 or not is_word(C) or C[0][0] == C[-1][0]:
        return False
    big = C * (2 * q + 2)
    return is_primitive(C) and string_ok(big, q)


def string_rep(C):
    return min(C, winv(C))


def band_rep(C):
    return min([rot(C, i) for i in range(len(C))] +
               [rot(winv(C), i) for i in range(len(C))])


# ===========================================================================
# Minimal resolutions with projective indecomposables (GAP, any finite group)
# ===========================================================================

MINRES = libgap.eval(r"""function(G, F, nmax)
  local gens, simples, findim, pims, H, subs, cand, todo, m, x, s, t, i, j,
        M, mult, res, n, a, homs, f, parts, P, Pmods, rk, ker, tries, dims,
        topmult, out, S, k, mats, triv, tens;
  gens := GeneratorsOfGroup(G);
  simples := List(IrreducibleModules(G, F, 0)[2], x -> x);
  simples := Filtered(simples, x -> MTX.IsAbsolutelyIrreducible(x));
  topmult := function(M, S)
    return Length(MTX.BasisModuleHomomorphisms(M, S));
  end;
  # projective indecomposables: summands of modules induced from p'-subgroups
  # and of their tensor products with simple modules
  pims := List(simples, x -> fail);
  subs := Filtered(List(ConjugacyClassesSubgroups(G), Representative),
                   H -> Size(H) > 1 and Gcd(Size(H), Characteristic(F)) = 1);
  subs := Reversed(subs);
  cand := [];
  for H in subs{[1 .. Minimum(3, Length(subs))]} do
    Add(cand, InducedGModule(G, H, TrivialGModule(H, F)));
  od;
  if Length(cand) = 0 then
    Add(cand, RegularModule(G, F)[2]);
  fi;
  todo := ShallowCopy(cand);
  tries := 0;
  while ForAny(pims, x -> x = fail) and tries < 40 do
    tries := tries + 1;
    if Length(todo) = 0 then
      for i in [1 .. Length(pims)] do
        if pims[i] <> fail then
          for S in simples do
            Add(todo, TensorProductGModule(pims[i], S));
          od;
        fi;
      od;
    fi;
    m := Remove(todo, 1);
    for x in MTX.Indecomposition(m) do
      t := x[2];
      dims := List(simples, S -> topmult(t, S));
      if Sum(dims) = 1 then
        i := Position(dims, 1);
        if pims[i] = fail then
          # projective cover of simples[i]: its socle is simple too
          pims[i] := t;
        fi;
      fi;
    od;
  od;
  if ForAny(pims, x -> x = fail) then
    return fail;
  fi;
  triv := TrivialGModule(G, F);
  M := triv;
  res := [];
  for n in [0 .. nmax] do
    mult := List(simples, S -> topmult(M, S));
    Add(res, mult);
    if n = nmax then
      break;
    fi;
    # cover: sum of mult[i] copies of pims[i], random homomorphisms
    while true do
      parts := [];
      Pmods := [];
      for i in [1 .. Length(simples)] do
        homs := MTX.BasisModuleHomomorphisms(pims[i], M);
        for j in [1 .. mult[i]] do
          Add(parts, Sum(homs, h -> Random(F) * h));
          Add(Pmods, pims[i]);
        od;
      od;
      f := Concatenation(parts);
      if RankMat(f) = MTX.Dimension(M) then
        break;
      fi;
    od;
    mats := List([1 .. Length(gens)], g -> DirectSumMat(List(Pmods,
                  p -> MTX.Generators(p)[g])));
    P := GModuleByMats(mats, F);
    ker := TriangulizedMat(NullspaceMat(f));
    M := MTX.InducedActionSubmodule(P, ker);
  od;
  return [List(simples, MTX.Dimension), List(pims, MTX.Dimension), res,
          simples, pims];
end
""")



# ===========================================================================
# Further helpers: groups, restriction, Jordan types, squares
# ===========================================================================




def cyc(*cycles_lists):
    """A permutation from cycles on 1..m (1-based), as GAP element."""
    p = libgap.eval('()')
    for c in cycles_lists:
        p = p * libgap.CycleFromList(list(c))
    return p


def grp_from(gens, name):
    return Grp(libgap.Group(gens), gens, name)


def elementary(p, r):
    gens = [cyc(range(p * i + 1, p * i + p + 1)) for i in range(r)]
    return grp_from(gens, 'E%d^%d' % (p, r))


def cyclic(m):
    return grp_from([cyc(range(1, m + 1))], 'C%d' % m)


def small_group_perm(order, number, pick, name):
    """SmallGroup(order, number) as a permutation group; pick(G) returns the
    generators to use (GAP elements of the permutation group)."""
    S = libgap.SmallGroup(order, number)
    iso = libgap.IsomorphismPermGroup(S)
    G = libgap.Image(iso)
    return grp_from(pick(G), name)


def find_pair(G, test):
    els = list(libgap.AsSSortedList(G))
    for a in els:
        for b in els:
            if test(a, b) and int(libgap.Size(libgap.Group([a, b]))) == \
                    int(libgap.Size(G)):
                return [a, b]
    raise ValueError


def hom_class(C, G, kernel):
    """The class in H^1(G, F_p) of the homomorphism G -> F_p with the given
    kernel (index p): chi(g) = i where g lies in the coset t^i K."""
    F = C.F
    p = F.characteristic()
    K = set(kernel)
    t = next(g for g in range(G.n) if g not in K)
    chi = [None] * G.n
    a = G.e
    for i in range(p):
        for k in K:
            chi[G.mul[a][k]] = i
        a = G.mul[a][t]
    assert C.is_cocycle_hom([F(c) for c in chi])
    return C.class_of_hom([F(c) for c in chi])


def coords_elementary(G, gens, p):
    """For an elementary abelian G with basis gens: the coordinate vector
    of every element."""
    co = {}
    for v in itertools.product(range(p), repeat=len(gens)):
        a = G.e
        for gi, k in zip(gens, v):
            for _ in range(k):
                a = G.mul[a][gi]
        co[a] = v
    assert len(co) == G.n
    return co


def dual_basis_classes(C, G, gens):
    F = C.F
    p = F.characteristic()
    co = coords_elementary(G, gens, p)
    return [C.class_of_hom([F(co[g][i]) for g in range(G.n)])
            for i in range(len(gens))]


def restriction_matrix(PG, PH, incl, n):
    """res_(G,H) : H^n(G) -> H^n(H) as a matrix (b^H_n x b^G_n), through a
    chain map from the minimal resolution of H to that of G restricted."""
    F, G, H = PG.F, PG.G, PH.G
    sig = {0: hcat(F, PG.dim(0), [PG.x0] * PH.b[0])}
    for k in range(1, n + 1):
        parts = []
        for h in range(H.n):
            parts.append(act_free(G, PG.b[k - 1], incl[h], sig[k - 1]))
        full = hcat(F, PG.dim(k - 1), parts).matrix_from_columns(
            [h * PH.b[k - 1] + i for i in range(PH.b[k - 1])
             for h in range(H.n)])
        sig[k] = PG.d[k].solve_right(full * PH.gen_cols(k))
    C = collapse(F, G, sig[n], PG.b[n])        # b^G_n x b^H_n
    return C.transpose()


def L_zeta(P, n, alpha):
    """L_zeta for zeta = alpha in H^n (Section 5.9): the kernel of
    zeta-hat, or Omega^n k + Omega k if zeta = 0."""
    if all(a == 0 for a in alpha):
        return dsum(P.omega(n)[0], P.omega(1)[0])
    Om, B = P.omega(n)
    return sub(Om, kernel_cols(P.hat(n, alpha)))


def jordan_type(T, p, d):
    """Block sizes of the nilpotent T (T^p = 0) on a space of dimension d."""
    r = [d] + [rk(T ** i) for i in range(1, p + 1)]
    out = {}
    for s in range(1, p + 1):
        # number of blocks of size >= s is r[s-1] - r[s]
        out[s] = (r[s - 1] - r[s]) - (r[s] - r[s + 1] if s < p else 0)
    return out


def swap_matrix(F, d):
    return mat(F, d * d, d * d, {(j * d + i, i * d + j): 1
                                 for i in range(d) for j in range(d)})


def eigen_sub(M, sign):
    """The +1 (sign = 1) or -1 (sign = -1) eigenspace of the swap on
    M (x) M (p odd), as a submodule of M (x) M, with its basis."""
    T = tensor(M, M)
    S = swap_matrix(M.F, M.dim)
    K = kernel_cols(S - sign * ident(M.F, T.dim))
    return sub(T, K), K, T


def sym2(M):
    return eigen_sub(M, 1)[0]


def ext2(M):
    return eigen_sub(M, -1)[0]


def all_classes(F, b, projective=True):
    """Non-zero vectors of F^b (up to scalars if projective)."""
    out = []
    for v in itertools.product(list(F), repeat=b):
        if all(x == 0 for x in v):
            continue
        if projective:
            i = next(j for j in range(b) if v[j] != 0)
            if v[i] != 1:
                continue
        out.append(vector(F, v))
    return out


def prod_(xs):
    out = 1
    for x in xs:
        out = out * x
    return out


def quaternion8():
    S = libgap.SmallGroup(8, 4)
    G = libgap.Image(libgap.IsomorphismPermGroup(S))
    pair = find_pair(G, lambda a, b: int(libgap.Order(a)) == 4 and
                     int(libgap.Order(b)) == 4)
    return grp_from(pair, 'Q8')


def monomial(C, xs, exps):
    """The Yoneda product of the classes xs[i]^exps[i] (degree one xs)."""
    out, deg = None, 0
    for x, e in zip(xs, exps):
        for _ in range(e):
            if out is None:
                out, deg = vector(C.F, x), 1
            else:
                out = C.mul(out, deg, x, 1)
                deg += 1
    return out



def inflation_matrix(PE, PQ, proj, n):
    """inf : H^n(Q) -> H^n(E) for a quotient map proj : E -> Q (lists of
    indices), through a chain map from the minimal resolution of E to that
    of Q regarded as E-modules."""
    F, E, Q = PE.F, PE.G, PQ.G
    tau = {0: hcat(F, PQ.dim(0), [PQ.x0] * PE.b[0])}
    for k in range(1, n + 1):
        parts = [act_free(Q, PQ.b[k - 1], proj[g], tau[k - 1])
                 for g in range(E.n)]
        full = hcat(F, PQ.dim(k - 1), parts).matrix_from_columns(
            [g * PE.b[k - 1] + i for i in range(PE.b[k - 1])
             for g in range(E.n)])
        tau[k] = PQ.d[k].solve_right(full * PE.gen_cols(k))
    return collapse(F, Q, tau[n], PQ.b[n]).transpose()   # b^E_n x b^Q_n


def section_5_9():
    F2, F3 = GF(2), GF(3)
    F4, F16, F9 = GF(4, 'w'), GF(16, 'v'), GF(9, 'u')
    # ------------------------------------------------------------------
    # p. 186: L_zeta restricted to a subgroup H is L_(res zeta) + proj, or
    # Omega^n k + Omega k + proj if res zeta = 0.  D8, all non-zero classes
    # of degrees 1 and 2, H = <x, c> (Klein four), <xy> (cyclic of order
    # four), <x> (order two).
    G = dihedral(2)
    x, y = G.gens
    P = Resolution(F2, G, 3)
    c = G.power(G.mul[x][y], 2)
    seen = set()
    for nm, els in (('<x,c>', [x, c]), ('<xy>', [G.mul[x][y]]),
                    ('<x>', [x])):
        H, incl = subgroup_grp(G, els, nm)
        PH = Resolution(F2, H, 3)
        for n in (1, 2):
            R = restriction_matrix(P, PH, incl, n)
            for alpha in all_classes(F2, P.b[n]):
                LH = restrict(L_zeta(P, n, alpha), H, incl)
                beta = R * alpha
                if beta != 0:
                    target = L_zeta(PH, n, beta)
                else:
                    target = dsum(PH.omega(n)[0], PH.omega(1)[0])
                seen.add(beta == 0)
                check(iso_mod_proj(LH, target),
                      'p. 186: L_zeta restricted to %s (D8, n = %d)'
                      % (nm, n))
    check(seen == {True, False}, 'p. 186: both cases of res occur')
    # ------------------------------------------------------------------
    # Proposition 5.9.1 in the rank variety form of its proof (p. 187):
    # L_zeta restricted to <u_alpha> is projective iff res(zeta) != 0;
    # if res(zeta) = 0 it is k + Omega k + free.  V4 and E8 (p = 2), with
    # H^*(E) = k[x_1, ..., x_r] and res(x_i) = alpha_i (so res(zeta) is
    # the value of the polynomial of zeta at alpha); E9 = C3 x C3 (p = 3).
    for (G, F, nmax) in ((dihedral(1), F16, 3), (elementary(2, 3), F4, 2)):
        r = len(G.gens)
        P = Resolution(F, G, nmax)
        C = Cohom(P)
        xs = dual_basis_classes(C, G, G.gens)
        pts = proj_points(F, r)
        for al in pts:
            for i in range(r):
                check(res_shifted(P, G.gens, al, 1, xs[i]) == al[i],
                      'res of x_i to <u_alpha> is alpha_i (%s)' % G.name)
        for n in range(1, nmax + 1):
            exps = [e for e in itertools.product(range(n + 1), repeat=r)
                    if sum(e) == n]
            mons = [monomial(C, xs, e) for e in exps]
            check(rk(conv(_matrix(F, mons), F)) == len(mons) == P.b[n],
                  'H^%d(%s) has the monomial basis' % (n, G.name))
            for co in itertools.product([0, 1], repeat=len(mons)):
                if not any(co):
                    continue
                alpha = sum((F(a) * m for a, m in zip(co, mons)),
                            vector(F, [0] * P.b[n]))
                L = L_zeta(P, n, alpha)
                check(L.dim == P.omega(n)[0].dim - 1, 'dim L_zeta')
                for al in pts:
                    fval = sum(F(a) * prod_(al[i] ** e[i] for i in range(r))
                               for a, e in zip(co, exps))
                    check(res_shifted(P, G.gens, al, n, alpha) == fval,
                          'res to <u_alpha> evaluates the polynomial')
                    fr = free_on_shifted(L, G.gens, al)
                    check(fr == (fval != 0),
                          'Proposition 5.9.1 (%s, n = %d)' % (G.name, n))
                    if not fr:
                        T = shifted_T(L, G.gens, al)
                        jt = jordan_type(T, 2, L.dim)
                        check(jt[1] == 2, 'L_zeta = k + Omega k + free on '
                              '<u_alpha> when res(zeta) = 0')
    # p odd: E9 over GF(9)
    G = elementary(3, 2)
    F = F9
    P = Resolution(F, G, 6)
    C = Cohom(P)
    pts = proj_points(F, 2)
    for n in (1, 2, 3):
        Om = P.omega(n)[0]
        classes = all_classes(F3, P.b[n])
        if n == 3:
            classes = classes[::7]
        for a3 in classes:
            alpha = vector(F, list(a3))
            L = L_zeta(P, n, alpha)
            if n % 2:
                check(L.dim % 3 == 1, 'p. 187: dim L_zeta = -2 mod p, n odd')
                check(C.mul(alpha, n, alpha, n) == 0,
                      'p. 187: zeta^2 = 0 for p odd, n odd')
                for al in pts:
                    check(not free_on_shifted(L, G.gens, al),
                          'p. 187: L_zeta never projective on <x>, n odd')
                continue
            for al in pts:
                T = shifted_T(Om, G.gens, al)
                jt = jordan_type(T, 3, Om.dim)
                check(jt[1] == 1 and jt[2] == 0,
                      'p. 187: Omega^n k = k + free on <x>, n even')
                rs = res_shifted(P, G.gens, al, n, alpha)
                fr = free_on_shifted(L, G.gens, al)
                check(fr == (rs != 0), 'Proposition 5.9.1 (E9, n = %d)' % n)
                if not fr:
                    jt = jordan_type(shifted_T(L, G.gens, al), 3, L.dim)
                    check(jt[1] == 1 and jt[2] == 1,
                          'p. 187: L_zeta = k + Omega k + free on <x>')
    # ------------------------------------------------------------------
    # Corollary 5.9.2: V_G(L_zeta_1 (x) ... (x) L_zeta_s) is the common
    # zero set (rank varieties, all points over the field used).
    G = dihedral(1)
    F = F16
    P = Resolution(F, G, 2)
    C = Cohom(P)
    xs = dual_basis_classes(C, G, G.gens)
    pts = proj_points(F, 2)
    x1, x2 = xs
    cls = {'x1': (1, x1), 'x2': (1, x2), 'x1+x2': (1, x1 + x2),
           'x1x2': (2, C.mul(x1, 1, x2, 1)),
           'x1(x1+x2)': (2, C.mul(x1, 1, x1 + x2, 1)),
           'x1^2+x1x2+x2^2': (2, C.mul(x1, 1, x1, 1) + C.mul(x1, 1, x2, 1) +
                              C.mul(x2, 1, x2, 1))}
    Ls = {k: L_zeta(P, n, a) for k, (n, a) in cls.items()}
    for k1, k2 in (('x1x2', 'x1(x1+x2)'), ('x1', 'x2'), ('x1x2', 'x1+x2'),
                   ('x1^2+x1x2+x2^2', 'x1x2')):
        n1, a1 = cls[k1]
        n2, a2 = cls[k2]
        M = tensor(Ls[k1], Ls[k2])
        for al in pts:
            zero = (res_shifted(P, G.gens, al, n1, a1) == 0 and
                    res_shifted(P, G.gens, al, n2, a2) == 0)
            check(free_on_shifted(M, G.gens, al) == (not zero),
                  'Corollary 5.9.2: V(L_%s (x) L_%s)' % (k1, k2))
    G = elementary(2, 3)
    F = F4
    P = Resolution(F, G, 1)
    C = Cohom(P)
    xs = dual_basis_classes(C, G, G.gens)
    L1, L2, L3 = [L_zeta(P, 1, a) for a in xs]
    M = tensor(L1, L2)
    var = [al for al in proj_points(F, 3)
           if not free_on_shifted(M, G.gens, al)]
    check(var == [(0, 0, 1)], 'Corollary 5.9.2: V(L_x1 (x) L_x2) is the '
          'point x1 = x2 = 0 of P^2 (E8)')
    check(is_free(tensor(M, L3)), 'V(L_x1 (x) L_x2 (x) L_x3) = {0}: '
          'projective (E8)')
    # ------------------------------------------------------------------
    # Lemma 5.9.3 and the author's corrections on p. 188.
    for (G, F, cases) in (
            (dihedral(1), F2, None), (dihedral(2), F2, None),
            (elementary(3, 2), F3, None)):
        P = Resolution(F, G, 4)
        C = Cohom(P)
        sample = []
        for (r, s) in ((1, 1), (1, 2), (2, 1), (2, 2)):
            A = all_classes(F, P.b[r])
            B = all_classes(F, P.b[s])
            pairs = [(a, b) for a in A for b in B]
            RNG.shuffle(pairs)
            sample += [(r, s, a, b) for a, b in pairs[:4]]
        zero_seen = False
        for (r, s, z1, z2) in sample:
            prod = C.mul(z1, r, z2, s)
            # graded commutativity of the Yoneda products
            check(prod == (-1) ** (r * s) * C.mul(z2, s, z1, r),
                  'zeta_1 zeta_2 = (-1)^(rs) zeta_2 zeta_1 (%s)' % G.name)
            # p. 188, l. 1 (author's correction): hat(zeta_1 zeta_2) =
            # hat(zeta_1) o Omega^r(hat(zeta_2))
            Om_r, _ = P.omega(r)
            h1 = P.hat(r, z1)
            h2 = P.hat(s, z2)
            om = C.omega_map(s, z2, r)
            check(h1 * om == P.hat(r + s, prod),
                  'p. 188, l. 1: hat(zeta1 zeta2) = hat(zeta1) o '
                  'Omega^r(hat(zeta2)) (%s)' % G.name)
            # the middle row: Omega^r k tensored with 0 -> L -> Omega^s k
            Om_s, _ = P.omega(s)
            T = tensor(Om_r, Om_s)
            one_h2 = conv(ident(F, Om_r.dim).tensor_product(h2), F)
            K = kernel_cols(h1 * one_h2)
            Kmod = sub(T, K)
            Lp = L_zeta(P, r + s, prod)
            zero_seen |= (prod == 0)
            check(iso_mod_proj(Kmod, Lp),
                  'Lemma 5.9.3: Ker(hat(zeta1) o Omega^r(hat(zeta2))) = '
                  'L_(zeta1 zeta2) + proj (%s)' % G.name)
            L1 = L_zeta(P, r, z1)
            L2 = L_zeta(P, s, z2)
            # Kmod -> L_zeta1 onto, with kernel Omega^r k (x) L_zeta2
            img = one_h2 * K
            check(rk(img) == L1.dim and (h1 * img).is_zero(),
                  'Lemma 5.9.3: onto L_zeta1')
            check(K.ncols() - rk(img) == Om_r.dim * L2.dim,
                  'Lemma 5.9.3: kernel Omega^r k (x) L_zeta2')
            check(iso_mod_proj(tensor(Om_r, L2), omega(L2, r)),
                  'Omega^r k (x) L_zeta2 = Omega^r L_zeta2 + proj')
            # p. 188 (author's correction): the right-hand entry of the
            # middle row is Omega^r k, mapping onto k with kernel L_zeta1
            check(Om_r.dim - L1.dim == 1, 'p. 188: Omega^r k -> k, kernel '
                  'L_zeta1')
            refuted(L1.dim - L1.dim == 1, 'p. 188 as printed: L_zeta1 in '
                    'the middle row over L_zeta1 -> k')
        if G.name == 'D8':
            check(zero_seen, 'Lemma 5.9.3 with zeta1 zeta2 = 0 (L_0)')
    # ------------------------------------------------------------------
    # Lemma 5.9.4: P_(n-1)/L_zeta = Omega^-1 L_zeta + proj, and the
    # sequence 0 -> k -> P_(n-1)/L_zeta -> Omega^(n-1) k -> 0 does not
    # split for zeta != 0.
    for (G, F, nmax) in ((dihedral(1), F2, 3), (dihedral(2), F2, 2),
                         (elementary(3, 2), F3, 2)):
        P = Resolution(F, G, nmax)
        for n in range(1, nmax + 1):
            Om, B = P.omega(n)
            Pm = free(F, G, P.b[n - 1])
            for alpha in all_classes(F, P.b[n])[:6]:
                K = kernel_cols(P.hat(n, alpha))
                L = sub(Om, K)
                Q, pr = quot(Pm, B * K)
                check(iso_mod_proj(Q, omega_inv(L)),
                      'Lemma 5.9.4: P_(n-1)/L_zeta = Omega^-1 L_zeta + proj')
                w = B.column(next(i for i in range(Om.dim)
                                  if P.hat(n, alpha)[0, i] != 0))
                wq = pr * conv(_matrix(F, [w]).transpose(), F)
                check(in_span(rad_cols(Q), wq), 'Lemma 5.9.4: the extension '
                      'by k does not split')
                if n >= 2:
                    Qk, _ = quot(Q, wq)
                    check(isomorphic(Qk, P.omega(n - 1)[0]),
                          'Lemma 5.9.4: quotient Omega^(n-1) k')
    # ------------------------------------------------------------------
    # Proposition 5.9.5: zeta annihilates Ext(M, M) iff
    # Omega^-1 L_zeta (x) M = M + Omega^(n-1) M + proj.
    both = set()
    G = dihedral(1)
    P = Resolution(F2, G, 4)
    C = Cohom(P)
    x1, x2 = dual_basis_classes(C, G, G.gens)
    zs = [(1, x1), (1, x1 + x2), (2, C.mul(x1, 1, x1, 1)),
          (2, C.mul(x1, 1, x2, 1)),
          (2, C.mul(x1, 1, x1, 1) + C.mul(x1, 1, x2, 1) + C.mul(x2, 1, x2, 1))]
    k = trivial(F2, G)
    Ms = [k, P.omega(1)[0], omega_inv(k), P.omega(2)[0], L_zeta(P, 1, x1),
          L_zeta(P, 1, x2), dsum(L_zeta(P, 1, x1), L_zeta(P, 1, x2)),
          L_zeta(P, 2, C.mul(x1, 1, x1, 1))]
    for n, z in zs:
        Linv = omega_inv(L_zeta(P, n, z))
        for M in Ms:
            ann = kills_identity(P, z, n, M)
            iso = iso_mod_proj(tensor(Linv, M), dsum(M, omega(M, n - 1)))
            both.add(ann)
            check(ann == iso, 'Proposition 5.9.5 (V4)')
    G = dihedral(2)
    P = Resolution(F2, G, 3)
    C = Cohom(P)
    xx, yy = G.gens
    H1 = G.closure([G.mul[G.mul[xx][yy]][xx], yy])
    H2 = G.closure([xx, G.mul[G.mul[yy][xx]][yy]])
    x1 = hom_class(C, G, H1)
    x2 = hom_class(C, G, H2)
    zs = [(1, x1), (1, x2), (1, x1 + x2), (2, C.mul(x1, 1, x1, 1)),
          (2, C.mul(x1, 1, x1, 1) + C.mul(x2, 1, x2, 1))]
    Ms = [trivial(F2, G)] + [string_mod(F2, G, letters(w)) for w in
                             ('a b a', 'b a b', 'a b', 'a', 'a b- a')]
    for n, z in zs:
        Linv = omega_inv(L_zeta(P, n, z))
        for M in Ms:
            ann = kills_identity(P, z, n, M)
            iso = iso_mod_proj(tensor(Linv, M), dsum(M, omega(M, n - 1)))
            both.add(ann)
            check(ann == iso, 'Proposition 5.9.5 (D8)')
    check(both == {True, False}, 'Proposition 5.9.5: both cases occur')
    # ------------------------------------------------------------------
    # Proposition 5.9.6 (i): zeta^2 annihilates Ext(L_zeta, L_zeta).
    for (G, F, nmax) in ((dihedral(1), F2, 2), (dihedral(2), F2, 2),
                         (elementary(3, 2), F3, 2),
                         (quaternion8(), F2, 2)):
        P = Resolution(F, G, 2 * nmax)
        C = Cohom(P)
        for n in range(1, nmax + 1):
            for alpha in all_classes(F, P.b[n]):
                L = L_zeta(P, n, alpha)
                sq = C.mul(alpha, n, alpha, n)
                check(kills_identity(P, sq, 2 * n, L),
                      'Proposition 5.9.6 (i) (%s, n = %d)' % (G.name, n))
    # (ii): p odd, n even: zeta annihilates Ext(L_zeta, L_zeta); and the
    # steps of the proof (E9, n = 2, and n = 4 for a few classes).
    G = elementary(3, 2)
    F = F3
    P = Resolution(F, G, 8)
    C = Cohom(P)
    for n, classes in ((2, all_classes(F, P.b[2])),
                       (4, all_classes(F, P.b[4])[::40])):
        Om = P.omega(n)[0]
        d = Om.dim
        check(d % 3 == 1, 'p. 190: dim Omega^n k = 1 mod p, n even')
        E2, KE, T = eigen_sub(Om, -1)
        S2, KS, _ = eigen_sub(Om, 1)
        check(E2.dim == d * (d - 1) // 2 and E2.dim % 3 == 0 and
              S2.dim % 3 == 1, 'p. 190: dimensions of the squares')
        check(is_free(E2), 'p. 190: Lambda^2(Omega^n k) is projective')
        check(iso_mod_proj(S2, P.omega(2 * n)[0]),
              'p. 190: S^2(Omega^n k) = Omega^(2n) k + proj')
        for alpha in classes:
            L = L_zeta(P, n, alpha)
            check(kills_identity(P, alpha, n, L),
                  'Proposition 5.9.6 (ii) (E9, n = %d)' % n)
            if n != 2:
                continue
            check(iso_mod_proj(sym2(L), omega(L, n)),
                  'p. 190: S^2(L_zeta) = Omega^n(L_zeta) + proj')
            check(iso_mod_proj(ext2(L), omega(L, 1)),
                  'p. 190: Lambda^2(L_zeta) = Omega(L_zeta) + proj')
            check(iso_mod_proj(tensor(L, L), dsum(omega(L, 1), omega(L, n))),
                  'p. 191: L (x) L = Omega L + Omega^n L + proj')
            # the complexes Lambda^2(C) and S^2(C') of the proof are exact
            # except where the text says
            hat = P.hat(n, alpha)
            Kz = kernel_cols(hat)              # L in Omega
            ok = exterior_complex_exact(F, Om, Kz) and \
                symmetric_complex(F, Om, hat, Kz)
            check(ok, 'p. 190: Lambda^2(C) exact, S^2(C\') has homology '
                  'Lambda^2(L_zeta) in degree two')
    # Remark (p. 191): the semidihedral group of order 16
    SD = semidihedral16()
    x, y = SD.gens
    Qel = SD.closure([SD.mul[x][x], SD.mul[x][y]])
    Qg = libgap.Subgroup(SD.gap, [SD.els[g] for g in Qel])
    check(str(libgap.StructureDescription(Qg)) == 'Q8' and len(Qel) == 8,
          'p. 191: <x^2, xy> is quaternion of order 8')
    P = Resolution(F2, SD, 8)
    C = Cohom(P)
    zeta = hom_class(C, SD, Qel)
    for n in (2, 3, 4):
        zn = C.power(zeta, 1, n)
        check(zn != 0, 'p. 191: zeta^%d != 0 (SD16)' % n)
        L = L_zeta(P, n, zn)
        ann = kills_identity(P, zn, n, L)
        # the same answer from the criterion of Proposition 5.9.5
        check(ann == iso_mod_proj(tensor(omega_inv(L), L),
                                  dsum(L, omega(L, n - 1))),
              'Proposition 5.9.5 for L_(zeta^%d) (SD16)' % n)
        refuted(not ann, 'Remark p. 191 as printed: zeta^%d does not '
                'annihilate Ext(L_(zeta^n), L_(zeta^n)) (SD16)' % n)
        if 2 * n <= 8:
            check(kills_identity(P, C.mul(zn, n, zn, n), 2 * n, L),
                  'Proposition 5.9.6 (i) for zeta^%d (SD16)' % n)
    # the phenomenon behind the remark does occur in characteristic two:
    # V4, zeta = x1^2 + x1 x2 + x2^2 (n = 2) does not annihilate
    # Ext(L_zeta, L_zeta), and neither does x1 + w x2 over F_4 (n = 1)
    G = dihedral(1)
    P = Resolution(F4, G, 4)
    C = Cohom(P)
    x1, x2 = dual_basis_classes(C, G, G.gens)
    z = C.mul(x1, 1, x1, 1) + C.mul(x1, 1, x2, 1) + C.mul(x2, 1, x2, 1)
    check(not kills_identity(P, z, 2, L_zeta(P, 2, z)),
          'p = 2, n = 2: zeta need not annihilate Ext(L_zeta, L_zeta)')
    w = F4.gen()
    for c, ann in ((F4(0), True), (F4(1), True), (w, False), (w + 1, False)):
        z1 = x1 + c * x2
        check(kills_identity(P, z1, 1, L_zeta(P, 1, z1)) == ann,
              'p = 2, n = 1: x1 + c x2 annihilates Ext(L, L) iff c in F_2')
    # Exercise (p. 191): G = Z/3 x Z/3, zeta in the image of the Bockstein
    G = elementary(3, 2)
    F = F3
    P = Resolution(F, G, 3)
    C = Cohom(P)
    Q3 = cyclic(3)
    PQ = Resolution(F, Q3, 2)
    co = coords_elementary(G, G.gens, 3)
    t = Q3.gens[0]
    subgroups = []
    for (a, b) in ((1, 0), (0, 1), (1, 1), (1, 2)):
        # the homomorphism (i, j) -> a i + b j and its kernel
        proj = [Q3.power(t, (a * co[g][0] + b * co[g][1]) % 3)
                for g in range(G.n)]
        Inf = inflation_matrix(P, PQ, proj, 2)
        zeta = Inf * vector(F, [1])
        check(zeta != 0, 'Exercise: the Bockstein class is non-zero')
        L = L_zeta(P, 2, zeta)
        OL = omega(L)
        check(isomorphic(L, omega(L, 2)), 'Exercise: L_zeta = Omega^2 L')
        check(not isomorphic(L, OL), 'Exercise: L_zeta != Omega L_zeta')
        splits = []
        for H in [[G.e, h, G.mul[h][h]] for h in
                  (G.gens[0], G.gens[1], G.mul[G.gens[0]][G.gens[1]],
                   G.mul[G.gens[0]][G.mul[G.gens[1]][G.gens[1]]])]:
            def fix(M):
                return kernel_cols(M.X(H[1]))
            splits.append((not in_span(rad_cols(L), fix(L)),
                           not in_span(rad_cols(OL), fix(OL))))
        check(any(s[0] for s in splits), 'Exercise: a map L_zeta -> F_p '
              'splitting on some H = Z/p')
        check(not any(s[1] for s in splits), 'Exercise: no such map '
              'Omega(L_zeta) -> F_p')
        LL, LOL, OLOL = tensor(L, L), tensor(L, OL), tensor(OL, OL)
        check(iso_full(LL, LOL), 'Exercise: L (x) L = L (x) Omega L')
        check(iso_full(OLOL, LOL), 'Exercise: Omega L (x) Omega L = '
              'L (x) Omega L, so ([L] - [Omega L])^2 = 0 in a(G)')



def semidihedral16():
    """SD16 = <x, y | x^8 = y^2 = 1, y x y = x^3> (Remark after 5.9.6)."""
    S = libgap.SmallGroup(16, 8)
    G = libgap.Image(libgap.IsomorphismPermGroup(S))
    pair = find_pair(G, lambda a, b: int(libgap.Order(a)) == 8 and
                     int(libgap.Order(b)) == 2 and b * a * b == a ** 3)
    return grp_from(pair, 'SD16')


def exterior_complex_exact(F, Om, Kz):
    """Lambda^2 of C : 0 -> L -> Omega -> 0 (L in degree one): the -1
    eigenspaces of sigma(x (x) y) = (-1)^(|x||y|) y (x) x on C (x) C give
    0 -> S^2(L) -> L (x) Omega -> Lambda^2(Omega) -> 0, exact."""
    d, l = Om.dim, Kz.ncols()
    I_d = ident(F, d)
    inc = Kz                                   # L -> Omega
    # degree 2: L (x) L; sigma = -swap; -1 eigenspace = symmetric tensors
    Sw_l = swap_matrix(F, l)
    D2 = kernel_cols(Sw_l - ident(F, l * l))  # in L (x) L
    # degree 1: (L (x) Omega) + (Omega (x) L) with sigma (u, v) ->
    # (swap v, swap u); degree 0: Omega (x) Omega, sigma = swap
    # d(x (x) y) = dx (x) y + (-1)^|x| x (x) dy
    dA = inc.tensor_product(ident(F, l))       # L(x)L -> Omega (x) L
    dB = -ident(F, l).tensor_product(inc)      # L(x)L -> L (x) Omega
    d2 = dB.stack(dA)                          # into (L(x)Om) + (Om(x)L)
    d1 = inc.tensor_product(I_d).augment(I_d.tensor_product(inc))
    # -1 eigenspace in degree 1: sigma(u, v) = (P v, P' u) with P the swap
    # Omega (x) L -> L (x) Omega
    Psw = mat(F, l * d, d * l, {(j * d + i, i * l + j): 1
                                for i in range(d) for j in range(l)})
    Pinv = Psw.transpose()
    sig1 = mat(F, l * d + d * l, l * d + d * l)
    sig1.set_block(0, l * d, Psw)
    sig1.set_block(l * d, 0, Pinv)
    D1 = kernel_cols(sig1 + ident(F, 2 * l * d))
    D0 = kernel_cols(swap_matrix(F, d) + ident(F, d * d))
    ok = (d1 * d2).is_zero()
    ok &= in_span(D1, d2 * D2) and in_span(D0, d1 * D1)
    r2 = rk(d2 * D2)
    r1 = rk(d1 * D1)
    ok &= (r2 == D2.ncols())                   # injective
    ok &= (r1 == D0.ncols())                   # onto
    ok &= (r2 + r1 == D1.ncols())              # exact in the middle
    ok &= D2.ncols() == l * (l + 1) // 2 and D1.ncols() == l * d
    return ok


def symmetric_complex(F, Om, hat, Kz):
    """S^2 of C' : 0 -> Omega -> k -> 0 (Omega in degree one): the +1
    eigenspaces give 0 -> Lambda^2(Omega) -> Omega -> k -> 0 with homology
    Lambda^2(L_zeta) in degree two (and zero elsewhere)."""
    d, l = Om.dim, Kz.ncols()
    Sw = swap_matrix(F, d)
    D2 = kernel_cols(Sw + ident(F, d * d))     # antisymmetric tensors
    # degree 1: (Omega (x) k) + (k (x) Omega) = Omega + Omega, sigma swaps
    d2 = conv(hat.tensor_product(ident(F, d)), F).stack(
        -conv(ident(F, d).tensor_product(hat), F))
    D1 = kernel_cols(mat(F, 2 * d, 2 * d, {**{(i, d + i): 1
                                              for i in range(d)},
                                           **{(d + i, i): 1
                                              for i in range(d)}})
                     - ident(F, 2 * d))
    d1 = hat.augment(hat)
    ok = in_span(D1, d2 * D2) and (d1 * d2).is_zero()
    r2 = rk(d2 * D2)
    r1 = rk(d1 * D1)
    ok &= (r1 == 1) and (r2 + r1 == D1.ncols())
    ker2 = D2.ncols() - r2
    ok &= ker2 == l * (l - 1) // 2
    # the kernel in degree two is Lambda^2(L_zeta) inside Lambda^2(Omega)
    LL = Kz.tensor_product(Kz)
    E = kernel_cols(swap_matrix(F, l) + ident(F, l * l))
    ok &= ((d2 * (LL * E)).is_zero())
    return ok



def quotient_grp(G, Nel, name):
    """G/N for a normal subgroup N (list of indices): (Grp, proj list); the
    generators of G/N are the images of those of G."""
    hom = libgap.NaturalHomomorphismByNormalSubgroup(
        G.gap, libgap.Subgroup(G.gap, [G.els[g] for g in Nel]))
    Q = libgap.Image(hom)
    QP = libgap.Image(libgap.IsomorphismPermGroup(Q))
    iso = libgap.IsomorphismPermGroup(Q)
    imgs = [libgap.Image(iso, libgap.Image(hom, G.els[g])) for g in G.gens]
    gens = [x for x in imgs if x != libgap.One(QP)]
    Qg = Grp(libgap.Group(gens) if gens else QP, gens, name)
    proj = [Qg.index(libgap.Image(iso, libgap.Image(hom, G.els[g])))
            for g in range(G.n)]
    return Qg, proj


def inflate(M, G, proj):
    return Mod(M.F, G, M.dim, [M.act[proj[g]] for g in range(G.n)])


def deflate(M, Q, proj):
    """A G-module on which N acts trivially, as a Q-module."""
    act = [None] * Q.n
    for g in range(M.G.n):
        if act[proj[g]] is None:
            act[proj[g]] = M.act[g]
        else:
            assert act[proj[g]] == M.act[g], 'N does not act trivially'
    return Mod(M.F, Q, M.dim, act)


def norm_sub(M, Nel):
    """N~ M as a submodule (N~ the sum of the elements of N)."""
    Nt = M.elem({g: 1 for g in Nel})
    B = colbasis(Nt)
    return sub(M, B) if B.ncols() else Mod(M.F, M.G, 0, [mat(M.F, 0, 0)] *
                                          M.G.n)


def rank_points(M, Egens, pts):
    return set(al for al in pts if not free_on_shifted(M, Egens, al))


def section_5_10():
    F2, F3, F4 = GF(2), GF(3), GF(4, 'w')
    # Q8: k is periodic of period 4; H^*(Q8, F_2) has dimensions
    # 1, 2, 2, 1 repeated, elements of degrees 1-3 are nilpotent and a
    # class of degree 4 acts invertibly (Proposition 5.10.2 for M = k).
    Q = quaternion8()
    P = Resolution(F2, Q, 9)
    C = Cohom(P)
    k = trivial(F2, Q)
    check(P.b == [1, 2, 2, 1, 1, 2, 2, 1, 1, 2], 'H^n(Q8) dimensions')
    check(isomorphic(P.omega(4)[0], k) and
          all(P.omega(j)[0].dim != 1 for j in (1, 2, 3)),
          'Q8: k has period 4')
    for d in (1, 2, 3):
        for a in all_classes(F2, P.b[d]):
            e = 3 if d == 1 else 2
            check(C.power(a, d, e) == 0, 'Proposition 5.10.2: degree %d '
                  'elements of Ext(k, k) are nilpotent (Q8)' % d)
    x4 = all_classes(F2, P.b[4])[0]
    for i in range(0, 5):
        A = C.mult_matrix(x4, 4, i)
        check(rk(A) == P.b[i] == P.b[i + 4], 'Proposition 5.10.2: the '
              'degree 4 class acts invertibly (Q8, degree %d)' % i)
    # C3: H^*(C3, F_3) = Lambda(y) (x) k[x]; k has period 2
    G = cyclic(3)
    P = Resolution(F3, G, 6)
    C = Cohom(P)
    y = vector(F3, [1])
    check(C.mul(y, 1, y, 1) == 0, 'y^2 = 0 in H^*(C3, F_3)')
    x = vector(F3, [1])
    for i in range(4):
        check(rk(C.mult_matrix(x, 2, i)) == 1, 'x of degree 2 acts '
              'invertibly (C3)')
    check(isomorphic(P.omega(2)[0], trivial(F3, G)) and
          not isomorphic(P.omega(1)[0], trivial(F3, G)), 'C3: period 2')
    # Corollary 5.10.6: periods divide the degrees of a system of
    # parameters: Q8 (degree 4), E9 (degree 2), D8 (degrees 1, 2)
    Mods = [k, omega(k), omega_inv(k)]
    for h in Q.gens:
        H, incl = subgroup_grp(Q, [h], 'C4')
        Mods.append(induced_trivial(F2, Q, incl))
    for M in Mods:
        check(iso_full(omega(M, 4), M), 'Corollary 5.10.6: Omega^4 M = M '
              '(Q8)')
    # Corollary 5.10.7: elementary abelian groups; period 1 in
    # characteristic two (V4: the even dimensional indecomposables
    # V_(n, alpha) of Volume I, Theorem 4.3.3 (ii), (iii)), period one or
    # two for p odd (E9: k induced from a subgroup of order 3: period 2)
    V4 = dihedral(1)
    for m in (1, 2, 3):
        for al in list(F4) + [None]:
            M = klein_four_V(F4, V4, m, al)
            check(is_indecomposable(M) and isomorphic(omega(M), M),
                  'Corollary 5.10.7: period one (V4, dimension %d)' % (2 * m))
    E = elementary(3, 2)
    for h in E.gens + [E.mul[E.gens[0]][E.gens[1]]]:
        H, incl = subgroup_grp(E, [h], 'C3')
        M = induced_trivial(F3, E, incl)
        check(not isomorphic(omega(M), M) and isomorphic(omega(M, 2), M),
              'Corollary 5.10.7: period two (E9)')
    E8 = elementary(2, 3)
    H, incl = subgroup_grp(E8, [E8.gens[0]], 'C2')
    M = induced_trivial(F2, E8, incl)
    check(isomorphic(omega(M), M), 'Corollary 5.10.7: period one (E8)')
    # Theorem 5.10.4 (Eisenbud) on D8 string modules: complexity one
    # (dimensions of Omega^n M bounded) iff periodic; for the periodic
    # ones the generator x2 (or x1) of the proof: L_x (x) M projective and
    # M = Omega M (+ proj)
    G = dihedral(2)
    P = Resolution(F2, G, 2)
    C = Cohom(P)
    xx, yy = G.gens
    x1 = hom_class(C, G, G.closure([G.mul[G.mul[xx][yy]][xx], yy]))
    x2 = hom_class(C, G, G.closure([xx, G.mul[G.mul[yy][xx]][yy]]))
    Lx1, Lx2 = L_zeta(P, 1, x1), L_zeta(P, 1, x2)
    nper = 0
    for n in range(1, 7):
        for Cw in sorted(set(string_rep(w) for w in all_words(n)
                             if string_ok(w, 2))):
            M = string_mod(F2, G, Cw)
            dims = [M.dim]
            Mi = M
            for _ in range(6):
                Mi = omega(Mi)
                dims.append(Mi.dim)
            per = isomorphic(omega(M, 2), M)
            bounded = dims[2] == dims[4] == dims[6]
            check(per == bounded, 'Theorem 5.10.4 (D8, M(%s))' % wstr(Cw))
            if per:
                nper += 1
                gen = [L for L in (Lx1, Lx2) if is_free(tensor(L, M))]
                check(len(gen) == 1 and iso_mod_proj(omega(M), M) and
                      isomorphic(omega(M), M),
                      'proof of 5.10.4: a degree one class generates the '
                      'periodicity, so M = Omega M (D8, M(%s))' % wstr(Cw))
    check(nper >= 2, 'periodic strings found')


def induced_trivial(F, G, incl):
    """k induced from the subgroup with element list incl (permutation
    module on the left cosets)."""
    Hs = set(incl)
    cos, where = [], {}
    for g in range(G.n):
        if g in where:
            continue
        c = sorted(G.mul[g][h] for h in Hs)
        for x in c:
            where[x] = len(cos)
        cos.append(c)
    m = len(cos)
    return Mod(F, G, m, [mat(F, m, m, {(where[G.mul[g][c[0]]], i): 1
                                       for i, c in enumerate(cos)})
                         for g in range(G.n)])


def klein_four_V(F, G, n, alpha):
    """V_(n, alpha) of Volume I, Theorem 4.3.3 (ii) (alpha in F) and (iii)
    (alpha = None for infinity): x -> [[I, I], [0, I]], y -> [[I, J], [0, I]]
    with J the Jordan block of eigenvalue alpha; (iii): x -> [[I, J_0], [0,
    I]], y -> [[I, I], [0, I]]."""
    I = ident(F, n)
    J = jordan(F, alpha if alpha is not None else F(0), n)
    def blk(B):
        out = ident(F, 2 * n)
        out.set_block(0, n, B)
        return out
    if alpha is None:
        return Mod.from_gens(F, G, [blk(J), blk(I)])
    return Mod.from_gens(F, G, [blk(I), blk(J)])


def section_5_11():
    F2, F3, F16, F9 = GF(2), GF(3), GF(16, 'v'), GF(9, 'u')
    # Lemma 5.11.1 and Theorem 5.11.2 (Andrews) for central subgroups N of
    # order p: Q8 and D8 over V4, C4 over C2 (epsilon = 1); C9 over C3 and
    # the extraspecial group 3^(1+2) of exponent 3 over E9 (epsilon = 2).
    cases = [(quaternion8(), F2, F16, 4), (dihedral(2), F2, F16, 3),
             (cyclic(4), F2, F16, 3), (cyclic(9), F3, F9, 2),
             (small_group_perm(27, 3, lambda S: list(
                 libgap.MinimalGeneratingSet(S)), 'H27'), F3, F9, 2)]
    allv = set()
    for (G, F, Fbig, rmax) in cases:
        p = F.characteristic()
        eps = 1 if p == 2 else 2
        Z = [g for g in range(G.n)
             if all(G.mul[g][h] == G.mul[h][g] for h in range(G.n))]
        Nel = sorted(G.closure([next(g for g in Z if g != G.e and
                                     G.power(g, p) == G.e)]))
        assert len(Nel) == p
        Q, proj = quotient_grp(G, Nel, G.name + '/N')
        Ng, inclN = subgroup_grp(G, [next(g for g in Nel if g != G.e)], 'N')
        PQ = Resolution(F, Q, 3)
        kQ = trivial(F, Q)
        bar = [kQ, PQ.omega(1)[0], omega_inv(kQ), PQ.omega(2)[0]]
        if Q.n == 4:
            V4 = dihedral(1)
            # Q is a Klein four group: the modules V_(1, alpha), V_(2, 0)
            for (n, al) in ((1, F(0)), (1, F(1)), (1, None), (2, F(0))):
                Mv = klein_four_V(F, V4, n, al)
                bar.append(Mod.from_gens(F, Q, [Mv.act[V4.gens[0]],
                                                Mv.act[V4.gens[1]]]))
        if Q.n == 9:
            for h in Q.gens:
                H, incl = subgroup_grp(Q, [h], 'C3')
                bar.append(induced_trivial(F, Q, incl))
        if Q.n == 3:
            bar = [kQ, PQ.omega(1)[0]]
        kG = trivial(F, G)
        elem = (Q.n in (4, 9))
        if elem:
            pts = proj_points(Fbig, 2)
        # Lemma 5.11.1 on inflated and other modules
        tests = [kG, omega(kG), omega(kG, 2), dsum(omega(kG), regular(F, G)),
                 tensor(omega(kG), omega(kG))] + [inflate(M, G, proj)
                                                 for M in bar]
        for M in tests:
            NM = deflate(norm_sub(M, Nel), Q, proj)
            check((norm_rank(M) > 0) == (NM.dim > 0 and norm_rank(NM) > 0),
                  'Lemma 5.11.1 (%s)' % G.name)
        for r in range(1, rmax + 1):
            Ok = omega(kG, eps * r)
            NOk = deflate(norm_sub(Ok, Nel), Q, proj)
            if elem:
                Vr = rank_points(NOk.change_ring(Fbig), Q.gens, pts)
            for Mb in bar:
                M = inflate(Mb, G, proj)
                OM = omega(M, eps * r)
                check(iso_mod_proj(restrict(OM, Ng, inclN),
                                   restrict(M, Ng, inclN)),
                      'p. 193 (corrected): Omega_G(M) restricted to N = '
                      'Omega_N(M restricted to N) + Q = M restricted + Q')
                Nt = OM.elem({g: 1 for g in Nel})
                c1 = OM.dim == M.dim
                c2 = Nt.is_zero()
                T = tensor(NOk, Mb) if NOk.dim else NOk
                c3 = T.dim == 0 or is_free(T)
                c4 = isomorphic(OM, M)
                vals = [c1, c2, c3, c4]
                if elem:
                    c5 = T.dim == 0 or not rank_points(T.change_ring(Fbig),
                                                       Q.gens, pts)
                    c6 = not (Vr & rank_points(Mb.change_ring(Fbig), Q.gens,
                                               pts))
                    vals += [c5, c6]
                allv.add(c1)
                check(len(set(vals)) == 1, 'Theorem 5.11.2 (%s, r = %d): '
                      '%s' % (G.name, r, vals))
        # if M is periodic as a kG-module, its period is divisible by eps
        if p == 3:
            check(not isomorphic(omega(kG), kG), 'period divisible by '
                  'epsilon = 2 (%s)' % G.name)
    check(allv == {True, False}, 'Theorem 5.11.2: both outcomes occur')


def section_5_12():
    F2, F4, F16 = GF(2), GF(4, 'w'), GF(16, 'v')
    # Theorem 5.12.1: V_G(M) = V_1 u V_2 with V_1 n V_2 = {0} forces a
    # decomposition M = M_1 + M_2 with V(M_i) = V_i: V4, L_zeta for
    # zeta = x1 x2 and x1 x2 (x1 + x2) (two and three points of P^1).
    G = dihedral(1)
    P = Resolution(F2, G, 3)
    C = Cohom(P)
    x1, x2 = dual_basis_classes(C, G, G.gens)
    pts = proj_points(F16, 2)
    for zeta, n, comps in ((C.mul(x1, 1, x2, 1), 2, [(F16(0), F16(1)),
                                                     (F16(1), F16(0))]),
                           (C.mul(C.mul(x1, 1, x2, 1), 2, x1 + x2, 1), 3,
                            [(F16(0), F16(1)), (F16(1), F16(0)),
                             (F16(1), F16(1))])):
        L = L_zeta(P, n, zeta)
        summ = decompose(L)
        check(len(summ) == len(comps), 'Theorem 5.12.1: number of summands')
        vs = sorted([sorted(rank_points(S.change_ring(F16), G.gens, pts))
                     for S in summ])
        check(vs == sorted([[c] for c in comps]), 'Theorem 5.12.1: the '
              'summands have the components as varieties')
    # over k = F_2 (not algebraically closed) the hypothesis matters:
    # zeta = x1^2 + x1 x2 + x2^2 vanishes at two conjugate points of
    # P^1(F_4); L_zeta is indecomposable over F_2 and splits over F_4.
    z = C.mul(x1, 1, x1, 1) + C.mul(x1, 1, x2, 1) + C.mul(x2, 1, x2, 1)
    L = L_zeta(P, 2, z)
    check(is_indecomposable(L) and len(decompose(L.change_ring(F4))) == 2,
          'Theorem 5.12.1 needs k algebraically closed (F_2 vs F_4)')
    # E8: M = L_(x1 x3) (x) L_(x2 x3): V(M) = {x1 = x2 = 0} u {x3 = 0}, a
    # point and a line of P^2 meeting only in 0 (Corollary 5.9.2); M splits
    # accordingly.
    G = elementary(2, 3)
    P = Resolution(F2, G, 2)
    C = Cohom(P)
    y1, y2, y3 = dual_basis_classes(C, G, G.gens)
    M = tensor(L_zeta(P, 2, C.mul(y1, 1, y3, 1)),
               L_zeta(P, 2, C.mul(y2, 1, y3, 1)))
    Mc = core(M)
    pts3 = proj_points(F4, 3)
    allpts = rank_points(Mc.change_ring(F4), G.gens, pts3)
    check(allpts == set(p for p in pts3 if (p[0] == 0 and p[1] == 0) or
                        p[2] == 0), 'V(L_x1x3 (x) L_x2x3) = point u line')
    summ = decompose(Mc)
    kinds = set()
    for S in summ:
        v = rank_points(S.change_ring(F4), G.gens, pts3)
        point = v <= {(F4(0), F4(0), F4(1))}
        line = all(p[2] == 0 for p in v)
        check(point or line, 'Theorem 5.12.1: each summand lies over one '
              'component (E8)')
        kinds.add('point' if point else 'line')
    check(kinds == {'point', 'line'}, 'Theorem 5.12.1: both components '
          'occur (E8)')



class Dihedral:
    """D_4q with H^*(G, k) = k[x1, x2, z]/(x1 x2) (Section 5.13): x1, x2 the
    homomorphisms with kernels <xyx, y> and <x, yxy>, z the class sent to
    z_2q* by the identification of Omega^2 k with the string module of p.
    198; the projective variety through the elementary abelian subgroups
    E1 = <x, c>, E2 = <y, c> (c = (xy)^q) and shifted cyclic subgroups."""

    def __init__(self, q, F, nmax):
        self.q, self.F = q, F
        G = self.G = dihedral(q)
        x, y = G.gens
        P = self.P = Resolution(F, G, nmax)
        C = self.C = Cohom(P)
        self.H1 = G.closure([G.mul[G.mul[x][y]][x], y])
        self.H2 = G.closure([x, G.mul[G.mul[y][x]][y]])
        self.x1 = hom_class(C, G, self.H1)
        self.x2 = hom_class(C, G, self.H2)
        self.U = letters('b- a') + wpow(letters('b a'), q - 1)
        self.V = letters('a- b') + wpow(letters('a b'), q - 1)
        S = iso_matrix(string_mod(F, G, self.Wr(1)), P.omega(2)[0])
        self.z = P.cocycle_of_hat(2, mat(F, 1, 4 * q + 1, {(0, 2 * q): 1}) *
                                  S.inverse())
        c = G.power(G.mul[x][y], q)
        self.E = [(x, c), (y, c)]
        self._pts = None

    def Wr(self, r):
        return wpow(winv(self.U), r) + wpow(self.V, r)

    def points(self, Fbig):
        if self._pts is None:
            P = Resolution(Fbig, self.G, 2)
            x1 = vector(Fbig, list(self.x1))
            x2 = vector(Fbig, list(self.x2))
            z = vector(Fbig, list(self.z))
            pts = {}
            for E in self.E:
                for al in proj_points(Fbig, 2):
                    t = (res_shifted(P, E, al, 1, x1),
                         res_shifted(P, E, al, 1, x2),
                         res_shifted(P, E, al, 2, z))
                    pts[(E, al)] = wnorm(Fbig, t)
            self._pts = pts
            self.Fbig = Fbig
        return self._pts

    def variety(self, M):
        pts = self._pts
        MF = M.change_ring(self.Fbig) if M.F != self.Fbig else M
        return set(pt for (E, al), pt in pts.items()
                   if not free_on_shifted(MF, E, al))


def wnorm(F, t):
    """A point of weighted projective space (weights 1, 1, 2)."""
    c1, c2, c3 = t
    if c1 != 0:
        return (F(1), c2 / c1, c3 / c1 ** 2)
    if c2 != 0:
        return (F(0), F(1), c3 / c2 ** 2)
    assert c3 != 0
    return (F(0), F(0), F(1))


def special_strings(q, rmax):
    A = wpow(letters('a b'), q - 1) + letters('a')
    B = wpow(letters('b a'), q - 1) + letters('b')
    out = {}
    for r in range(rmax + 1):
        Ca = A + wpow(letters('b-') + A, r)
        Cb = B + wpow(letters('a-') + B, r)
        out[string_rep(Ca)] = 'a'
        out[string_rep(Cb)] = 'b'
    return out


def rotations(C):
    return [rot(C, i) for i in range(len(C))]


def section_5_13():
    F2, F4, F16 = GF(2), GF(4, 'w'), GF(16, 'v')
    w = F16.gen() ** 5                       # a primitive cube root of 1
    units = [F16(1), w, w ** 2]
    # ------------------------------------------------------------------
    # q = 1 (p. 195): V4, H^* = k[x1, x2]; Omega^n(k) and L_(zeta^m)
    G = dihedral(1)
    P = Resolution(F16, G, 4)
    C = Cohom(P)
    x1, x2 = dual_basis_classes(C, G, G.gens)
    pts = proj_points(F16, 2)
    k = trivial(F16, G)
    for n in range(-3, 4):
        M = omega(k, n) if n >= 0 else omega_inv(k, -n)
        check(is_indecomposable(M) and
              rank_points(M, G.gens, pts) == set(pts),
              'p. 195: Omega^%d(k) indecomposable with V_G(Omega^n k) = V_G'
              % n)
    sub4 = [F16(0), F16(1), w, w ** 2]
    for (c1, c2) in [p for p in pts if p[0] in sub4 and p[1] in sub4]:
        zeta = c1 * x1 + c2 * x2
        for m in range(1, 5):
            L = L_zeta(P, m, C.power(zeta, 1, m))
            v = rank_points(L, G.gens, pts)
            check(is_indecomposable(L) and v == {wnorm1(F16, (c2, c1))},
                  'p. 195: L_(zeta^m) indecomposable, V = V<zeta>')
            al = None if c1 == 0 else c2 / c1
            check(isomorphic(L, klein_four_V(F16, G, m, al)),
                  'p. 195: L_(zeta^m) = V_(m, alpha), the point of V<zeta>')
    # ------------------------------------------------------------------
    # q = 2, 4: the cohomology ring and the identification on p. 198
    for (q, N, rmax) in ((2, 8, 3), (4, 6, 2)):
        D = Dihedral(q, F2, max(N, 2 * rmax))
        P, C = D.P, D.C
        x1, x2, z = D.x1, D.x2, D.z
        check(C.mul(x1, 1, x2, 1) == 0 and C.mul(x2, 1, x1, 1) == 0,
              'x1 x2 = 0 (D%d)' % (4 * q))
        for n in range(N + 1):
            mons = []
            for b in range(n // 2 + 1):
                a = n - 2 * b
                for (xv, amin) in ((x1, 0), (x2, 1)):
                    if a < amin or (xv is x2 and a == 0):
                        continue
                    mons.append(ring_mono(C, xv, a, z, b))
            check(P.b[n] == n + 1 and len(mons) == n + 1 and
                  rk(conv(_matrix(F2, mons), F2)) == n + 1,
                  'H^%d(D%d) = k[x1, x2, z]/(x1 x2) in degree %d'
                  % (n, 4 * q, n))
        for r in range(1, rmax + 1):
            MW = string_mod(F2, D.G, D.Wr(r))
            S = iso_matrix(MW, P.omega(2 * r)[0])
            check(S is not None and MW.dim == 4 * q * r + 1,
                  'p. 198: Omega^2r(k) = M(W_r), dimension 4qr + 1')
            Si = S.inverse()

            def cls(i):
                row = mat(F2, 1, MW.dim, {(0, i): 1}) * Si
                return P.cocycle_of_hat(2 * r, row)
            for s in range(r + 1):
                check(ring_mono(C, x1, 2 * (r - s), z, s) ==
                      cls(2 * q * (2 * r - s)), 'p. 198: x1^(2(r-s)) z^s')
                check(ring_mono(C, x2, 2 * (r - s), z, s) == cls(2 * q * s),
                      'p. 198: x2^(2(r-s)) z^s')
            if r == 1:
                refuted(C.mul(x2, 1, x2, 1) == cls(4 * q),
                        'the other labelling of x1, x2 (p. 196)')
    # ------------------------------------------------------------------
    # p. 197: identities in the group algebra (q = 2, 4, 8)
    for q in (2, 4, 8):
        G = dihedral(q)
        R = regular(F2, G)
        x, y = G.gens
        I = ident(F2, G.n)
        X, Y = R.X(x), R.X(y)
        xyx = G.mul[G.mul[x][y]][x]
        check((X * X).is_zero() and (Y * Y).is_zero(), 'X^2 = Y^2 = 0')
        check(I + R.act[xyx] == Y + X * Y + Y * X + X * Y * X,
              'p. 197: 1 + xyx = Y + XY + YX + XYX')
        Gt = R.elem({g: 1 for g in range(G.n)})
        check(Gt == (X * Y) ** q == (Y * X) ** q, 'p. 197: G~ = (XY)^q')
        H = G.closure([xyx, y])
        check(len(H) == 2 * q, '|<xyx, y>| = 2q')
        Ht = R.elem({h: 1 for h in H})
        check(Ht == ((I + R.act[xyx]) * (I + R.act[y])) ** (q // 2) ==
              ((Y + X * Y + Y * X + X * Y * X) * Y) ** (q // 2) ==
              (Y * X * Y + X * Y * X * Y) ** (q // 2) ==
              (Y * X) ** (q - 1) * Y + (X * Y) ** q,
              'p. 197: H~ = ((1 + xyx)(1 + y))^(q/2) = (YX)^(q-1) Y + (XY)^q')
    # ------------------------------------------------------------------
    # Theorem 5.13.1 (i): string modules (q = 2, 4)
    for (q, nmax, rspec) in ((2, 7, 2), (4, 7, 1)):
        D = Dihedral(q, F2, 2)
        pts = D.points(F16)
        IMG = set(pts.values())
        check((F16(0), F16(1), F16(0)) in IMG and
              (F16(1), F16(0), F16(0)) in IMG,
              'z restricts to zero on <x> and <y> (the points 0_a, 0_b)')
        G = D.G
        x, y = G.gens
        spec = special_strings(q, rspec)
        words = set(string_rep(C) for n in range(1, nmax + 1)
                    for C in all_words(n) if string_ok(C, q))
        words |= set(spec)
        Pa = set(p for p in IMG if p[1] == 0)
        Pb = set(p for p in IMG if p[0] == 0)
        seen = set()
        for Cw in sorted(words, key=lambda c: (len(c), c)):
            M = string_mod(F2, G, Cw)
            f, l = Cw[0][0], Cw[-1][0]
            V = D.variety(M)
            per = isomorphic(omega(M, 2), M)
            if f != l:
                pred, kind = IMG, 'a..b'
                check(not per, 'Theorem 5.13.1 (i): M(%s) not periodic'
                      % wstr(Cw))
            elif Cw in spec:
                pred = {(F16(0), F16(1), F16(0))} if f == 'a' else \
                    {(F16(1), F16(0), F16(0))}
                kind = 'special'
                check(per, 'Theorem 5.13.1 (i): M(%s) periodic' % wstr(Cw))
                check(isomorphic(omega(M), M), 'proof of 5.13.1 (i): '
                      'M(%s) has period one' % wstr(Cw))
                refuted(not isomorphic(omega(M), M), 'p. 196-197 as '
                        'printed: M(%s) has period two' % wstr(Cw))
            else:
                pred = Pb if f == 'a' else Pa
                kind = 'line'
                check(not per, 'Theorem 5.13.1 (i): M(%s) not periodic'
                      % wstr(Cw))
            if f == l:
                h_free, h_not = (x, y) if f == 'a' else (y, x)
                Hf, inf_ = subgroup_grp(G, [h_free], 'C2')
                Hn, inn = subgroup_grp(G, [h_not], 'C2')
                check(is_free(restrict(M, Hf, inf_)) and
                      not is_free(restrict(M, Hn, inn)),
                      'proof of 5.13.1 (i): free on <x>, not on <y>')
            seen.add(kind)
            check(V == pred, 'Theorem 5.13.1 (i): V(M(%s)) (D%d)'
                  % (wstr(Cw), 4 * q))
        check(seen == {'a..b', 'special', 'line'}, 'all cases of (i)')
    # ------------------------------------------------------------------
    # Theorem 5.13.1 (ii), (iii): band modules (q = 2: words of length
    # <= 8, q = 4: length 8), phi = J_1(lambda), J_2(lambda), lambda in
    # F_4^*; H = <xyx, y>
    for (q, lens) in ((2, (2, 4, 6, 8)), (4, (8,))):
        D = Dihedral(q, F2, 2)
        D.points(F16)
        G = D.G
        x, y = G.gens
        xyx = G.mul[G.mul[x][y]][x]
        H, inclH = subgroup_grp(G, [xyx, y], 'H')
        Vw, Uw = D.V, D.U
        Pw = wpow(letters('a b'), q) + winv(wpow(letters('b a'), q))
        words = set()
        for n in lens:
            for Cw in all_words(n):
                if band_ok(Cw, q) or Cw in rotations(Pw) or \
                        winv(Cw) in rotations(Pw):
                    words.add(band_rep(Cw))
        R = regular(F16, G)
        XYq = (R.X(x) * R.X(y)) ** q
        found = set()
        for Cw in sorted(set(words) | set(winv(c) for c in words)):
            for lam in units:
                for r in (1, 2):
                    if r == 2 and len(Cw) > 4 and lam != units[1]:
                        continue
                    phi = jordan(F16, lam, r)
                    proj_word = Cw in rotations(Pw) or \
                        winv(Cw) in rotations(Pw)
                    if proj_word:
                        if lam == 1 and r == 1:
                            M = band_mod(F16, G, Cw, phi)
                            check(is_free(M) and isomorphic(M, regular(
                                F16, G)) and not D.variety(M),
                                  'Theorem 5.13.1 (iii): M((ab)^q (ba)^-q, '
                                  'id) = kG, variety empty')
                        continue
                    M = band_mod(F16, G, Cw, phi)
                    V = D.variety(M)
                    if Cw in rotations(Vw):
                        pred, kind = {(F16(1), F16(0), lam ** -1)}, 'V'
                    elif winv(Cw) in rotations(Vw):
                        pred, kind = {(F16(1), F16(0), lam)}, 'V-'
                    elif Cw in rotations(Uw):
                        pred, kind = {(F16(0), F16(1), lam ** -1)}, 'U'
                    elif winv(Cw) in rotations(Uw):
                        pred, kind = {(F16(0), F16(1), lam)}, 'U-'
                    else:
                        pred, kind = {(F16(0), F16(0), F16(1))}, 'inf'
                    found.add(kind)
                    check(V == pred, 'Theorem 5.13.1 (ii): V(M(%s, J_%d(%s)))'
                          ' (D%d)' % (wstr(Cw), r, lam, 4 * q))
                    if kind == 'V' and lam != 1:
                        refuted(V == {(F16(1), F16(0), lam)},
                                'Theorem 5.13.1 (ii) as printed: {lambda_a} '
                                'for M(a^-1 b (ab)^(q-1), J(lambda))')
                    # the restriction to H = <xyx, y> and the rank of H~
                    MH = restrict(M, H, inclH)
                    hfree = is_free(MH)
                    MX, MY = M.X(x), M.X(y)
                    rkH = rk((MY * MX) ** (q - 1) * MY)
                    check(hfree == (kind in ('V', 'V-')) ==
                          (rkH * 2 * q == M.dim),
                          'proof of 5.13.1 (ii): M(C, phi) projective on '
                          '<xyx, y> iff C ~ a^-1 b (ab)^(q-1)')
                    check(((M.X(x) * M.X(y)) ** q).is_zero(),
                          'proof of 5.13.1 (ii): G~ = (XY)^q acts as zero')
                    misses_a = all(p[1] != 0 for p in V)
                    misses_b = all(p[0] != 0 for p in V)
                    check(hfree == misses_b, 'proof of 5.13.1 (ii), '
                          'corrected: V cap P^1_b empty iff projective on H')
                    if kind in ('U', 'U-'):
                        refuted(misses_a <= hfree, 'p. 197 as printed: V cap '
                                'P^1_a empty implies projective on <xyx, y>')
        check({'V', 'V-', 'U', 'U-', 'inf'} <= found,
              'all cases of (ii) (D%d)' % (4 * q))
    # ------------------------------------------------------------------
    # The claim in the proof of (ii) (pp. 197-198): zeta = (lambda x1^2 +
    # mu x2^2 + z)^r
    for (q, rmax) in ((2, 3), (4, 2)):
        D = Dihedral(q, F16, 2 * rmax)
        P, C, G = D.P, D.C, D.G
        x, y = G.gens
        X1sq, X2sq = C.mul(D.x1, 1, D.x1, 1), C.mul(D.x2, 1, D.x2, 1)
        D.points(F16)
        for r in range(1, rmax + 1):
            MW = string_mod(F16, G, D.Wr(r))
            S = iso_matrix(MW, P.omega(2 * r)[0])
            pairs = [(a, b) for a in units for b in units]
            if q == 4 or r == 3:
                pairs = [(units[1], units[2]), (units[0], units[1])]
            for lam, mu in pairs:
                zeta = C.power(lam * X1sq + mu * X2sq + D.z, 2, r)
                hatW = P.hat(2 * r, zeta) * S
                book = mat(F16, 1, MW.dim)
                for i in range(r + 1):
                    book[0, 2 * q * (r + i)] += binomial(r, i) * lam ** i
                for j in range(1, r + 1):
                    book[0, 2 * q * (r - j)] += binomial(r, j) * mu ** j
                check(hatW == book, 'p. 198: zeta-hat in the basis z_i')
                K = kernel_cols(hatW)
                L = sub(MW, K)
                ok = isomorphic(L, dsum(
                    band_mod(F16, G, D.V, jordan(F16, lam ** -1, r)),
                    band_mod(F16, G, D.U, jordan(F16, mu ** -1, r))))
                check(ok, 'claim of p. 197: L_zeta = M(a^-1 b (ab)^(q-1), '
                      'J(lambda^-1)) + M(b^-1 a (ba)^(q-1), J(mu^-1)) in '
                      'the schema of Volume I')
                if lam != 1 or mu != 1:
                    refuted(isomorphic(L, dsum(
                        band_mod(F16, G, D.V, jordan(F16, lam, r)),
                        band_mod(F16, G, D.U, jordan(F16, mu, r)))),
                            'p. 197 as printed, with J(lambda), J(mu)')
                check(D.variety(L) == {(F16(1), F16(0), lam),
                                       (F16(0), F16(1), mu)},
                      'V(L_zeta) = {lambda_a, mu_b} (Proposition 5.9.1)')
                # the subspaces of p. 198 are not submodules
                for rng in (range(2 * q * r, 4 * q * r + 1),
                            range(0, 2 * q * r + 1)):
                    Sp = ident(F16, MW.dim).matrix_from_columns(rng)
                    A = Sp * kernel_cols(hatW * Sp)
                    refuted(is_invariant(MW, A), 'p. 198: L_zeta cap '
                            '<z_i, ...> is a submodule')
                # the printed phi is the matrix of X : V_0 -> V_1
                v = [mat(F16, MW.dim, 1, {(2 * q * (r + j), 0): 1,
                                          (2 * q * r, 0): binomial(r, j) *
                                          lam ** j}) for j in range(1, r + 1)]
                Wb = ident(F16, MW.dim).matrix_from_columns(
                    [2 * q * (r + i) + 1 for i in range(r)])
                Xm = MW.X(x)
                Phi = Wb.solve_right(hcat(F16, MW.dim, [Xm * u for u in v]))
                check(Phi == printed_phi(F16, lam, r), 'p. 198: the printed '
                      'phi is the matrix of X from V_0 to V_1')
    # p. 198: the printed phi is conjugate to J_r(lambda) (characteristic
    # two), and its inverse to J_r(lambda^-1)
    for lam in units:
        for r in range(1, 7):
            Ph = printed_phi(F16, lam, r)
            I = ident(F16, r)
            check(((Ph - lam * I) ** r).is_zero() and
                  rk(Ph - lam * I) == r - 1,
                  'p. 198: phi conjugate to the Jordan block J_r(lambda)')
            Pi = Ph.inverse()
            check(((Pi - lam ** -1 * I) ** r).is_zero() and
                  rk(Pi - lam ** -1 * I) == r - 1,
                  'phi^-1 conjugate to J_r(lambda^-1)')


def printed_phi(F, lam, r):
    """The matrix phi of p. 198: first row binom(r, i) lambda^i, ones below
    the diagonal."""
    out = mat(F, r, r)
    for i in range(1, r + 1):
        out[0, i - 1] = binomial(r, i) * lam ** i
    for i in range(1, r):
        out[i, i - 1] = 1
    return out


def ring_mono(C, xv, a, z, b):
    """xv^a z^b (Yoneda products; xv of degree one, z of degree two)."""
    out, deg = None, 0
    if a:
        out, deg = C.power(xv, 1, a), a
    if b:
        zb = C.power(z, 2, b)
        out = zb if out is None else C.mul(out, deg, zb, 2 * b)
        deg += 2 * b
    if out is None:
        return vector(C.F, [1])
    return out


def wnorm1(F, ab):
    """The point (a : b) of P^1 normalised as in proj_points."""
    a, b = ab
    if a != 0:
        return (F(1), F(b / a))
    return (F(0), F(1))



# ===========================================================================
# Complexes of modules (lists of modules, d[i] : C_i -> C_(i-1))
# ===========================================================================


class Cx:
    def __init__(self, mods, d):
        self.mods, self.d = mods, d          # d[0] is None

    def __len__(self):
        return len(self.mods)

    def dims(self):
        return [M.dim for M in self.mods]


def quot_section(M, K):
    """M / span(K) with the projection and a section (columns)."""
    F, n, k = M.F, M.dim, K.ncols()
    B = colbasis(K.augment(ident(F, n)))
    Q, pr = quot(M, K)
    return Q, pr, B.matrix_from_columns(range(k, n))


def C_zeta(P, n, alpha, M=None):
    """The complex C_zeta (Section 5.14): P_(n-1)/L_zeta -> P_(n-2) -> ...
    -> P_0 (n >= 2), with the data for splicing: (complex, the map P_0 ->
    P_(n-1)/L_zeta of C_zeta^(oo))."""
    F, G = P.F, P.G
    mods = [free(F, G, P.b[i]) for i in range(n - 1)]
    d = [None] + [P.d[i] for i in range(1, n - 1)]
    Om, B = P.omega(n)
    hat = P.hat(n, alpha)
    K = kernel_cols(hat)                      # L_zeta in Omega
    Pn1 = free(F, G, P.b[n - 1])
    Q, pr, s = quot_section(Pn1, B * K)
    mods.append(Q)
    d.append(P.d[n - 1] * s)
    # splice: P_0 -> Q, x |-> eps(x) . pr(w), hat(w) = 1
    i = next(j for j in range(Om.dim) if hat[0, j] != 0)
    wv = B.column(i) / hat[0, i]
    splice = (pr * conv(_matrix(F, [wv]).transpose(), F)) * P.eps
    return Cx(mods, d), splice


def C_infinity(P, n, alpha, top):
    """C_zeta^(oo) in degrees 0..top."""
    Cz, splice = C_zeta(P, n, alpha)
    mods, d = [], [None]
    for deg in range(top + 1):
        i = deg % n
        mods.append(Cz.mods[i])
        if deg == 0:
            continue
        d.append(splice if i == 0 else Cz.d[i])
    return Cx(mods, d)


def tensor_cx(A, B, top=None):
    """Total complex of A (x) B (diagonal action), Koszul signs."""
    F = A.mods[0].F
    n = len(A) + len(B) - 1 if top is None else top + 1
    mods, blocks, d = [], [], [None]
    for m in range(n):
        parts = [(i, m - i) for i in range(len(A)) if 0 <= m - i < len(B)]
        blocks.append(parts)
        mods.append(dsum(*[tensor(A.mods[i], B.mods[j]) for i, j in parts]))
    for m in range(1, n):
        rows = blocks[m - 1]
        cols = blocks[m]
        roff, off = {}, 0
        for (i, j) in rows:
            roff[(i, j)] = off
            off += A.mods[i].dim * B.mods[j].dim
        D = mat(F, mods[m - 1].dim, mods[m].dim)
        coff = 0
        for (i, j) in cols:
            w = A.mods[i].dim * B.mods[j].dim
            if i >= 1 and (i - 1, j) in roff:
                blk = conv(A.d[i].tensor_product(ident(F, B.mods[j].dim)), F)
                D.set_block(roff[(i - 1, j)], coff, blk)
            if j >= 1 and (i, j - 1) in roff:
                blk = conv(ident(F, A.mods[i].dim).tensor_product(B.d[j]), F)
                D.set_block(roff[(i, j - 1)], coff, (-1) ** i * blk)
            coff += w
        d.append(D)
    return Cx(mods, d)


def module_cx(M):
    return Cx([M], [None])


def homology_dims(Cc, upto=None):
    n = len(Cc) if upto is None else upto
    out = []
    for i in range(n):
        dim = Cc.mods[i].dim
        r_out = rk(Cc.d[i]) if i >= 1 else 0
        r_in = rk(Cc.d[i + 1]) if i + 1 < len(Cc) else 0
        out.append(dim - r_out - r_in)
    return out


def is_complex(Cc):
    return all((Cc.d[i - 1] * Cc.d[i]).is_zero() for i in range(2, len(Cc)))


def coinvariant_cohomology(Cc):
    """dims of H^i(Hom_kG(C, k)): homology of the coinvariants C_G = C / I C
    (their duals)."""
    qs = []
    for M in Cc.mods:
        R = rad_cols(M) if M.dim else mat(M.F, 0, 0)
        Q, pr = quot(M, R) if R.ncols() else (M, ident(M.F, M.dim))
        qs.append((Q, pr, R))
    dims = [Q.dim for Q, _, _ in qs]
    ind = [None]
    for i in range(1, len(Cc)):
        Qs, prs, Rs = qs[i]
        Qt, prt, Rt = qs[i - 1]
        # a section of prs: columns of M mapping onto the basis of Q
        sec = prs.solve_right(ident(Cc.mods[i].F, Qs.dim)) if Qs.dim else \
            mat(Cc.mods[i].F, Cc.mods[i].dim, 0)
        ind.append(prt * Cc.d[i] * sec)
    out = []
    for i in range(len(Cc)):
        r_out = rk(ind[i]) if i >= 1 and ind[i].nrows() and ind[i].ncols() \
            else 0
        r_in = rk(ind[i + 1]) if i + 1 < len(Cc) else 0
        out.append(dims[i] - r_out - r_in)
    return out, dims


def section_5_14():
    F2, F3, F4 = GF(2), GF(3), GF(4, 'w')
    # ------------------------------------------------------------------
    # C_zeta and C_zeta^(oo): homology k in degrees 0 and n - 1, exact
    # except in degree 0 (V4, D8, C3, E9)
    V4 = dihedral(1)
    P4 = Resolution(F2, V4, 9)
    C4 = Cohom(P4)
    x1, x2 = dual_basis_classes(C4, V4, V4.gens)
    sq = lambda a: C4.mul(a, 1, a, 1)
    cub = lambda a: C4.mul(sq(a), 2, a, 1)
    D8 = Dihedral(2, F2, 9)
    E9 = elementary(3, 2)
    P9 = Resolution(F3, E9, 7)
    C3g = cyclic(3)
    P3 = Resolution(F3, C3g, 9)
    cases = [(P4, 2, sq(x1)), (P4, 2, C4.mul(x1, 1, x2, 1)),
             (P4, 3, cub(x2)), (P4, 2, sq(x1) + sq(x2)),
             (D8.P, 2, D8.z), (D8.P, 2, D8.C.mul(D8.x1, 1, D8.x1, 1)),
             (P3, 2, vector(F3, [1])), (P3, 4, vector(F3, [1])),
             (P9, 2, vector(F3, [1, 0, 0])), (P9, 2, vector(F3, [0, 1, 1]))]
    for (P, n, a) in cases:
        Cz, _ = C_zeta(P, n, a)
        check(is_complex(Cz), 'C_zeta is a complex')
        h = homology_dims(Cz)
        check(h == [1] + [0] * (n - 2) + [1] if n >= 2 else False,
              'p. 199: H_i(C_zeta) = k for i = 0, n - 1 (%s)' % P.G.name)
        Ci = C_infinity(P, n, a, 3 * n)
        check(is_complex(Ci) and homology_dims(Ci, 3 * n) ==
              [1] + [0] * (3 * n - 1),
              'p. 200: C_zeta^(oo) exact except H_0 = k (%s)' % P.G.name)
    # ------------------------------------------------------------------
    # Theorem 5.14.2: zeta_1, ..., zeta_c covering the variety of M
    def thm_5_14_2(P, data, M, cover, tag, top=6):
        F, G = P.F, P.G
        tops = []
        for (n, a) in data:
            Cz, _ = C_zeta(P, n, a)
            tops.append(Cz.mods[-1])
        T = M
        for X in tops:
            T = tensor(T, X)
        check(is_free(T) == cover, 'Theorem 5.14.2: P_(n_1-1)/L (x) ... '
              '(x) M projective iff covering (%s)' % tag)
        if not cover:
            return
        Cc = module_cx(M)
        for (n, a) in data:
            Cz, _ = C_zeta(P, n, a)
            Cc = tensor_cx(Cc, Cz)
        check(all(is_free(X) for X in Cc.mods), 'Theorem 5.14.2: a finite '
              'complex of projectives (%s)' % tag)
        Ci = module_cx(M)
        for (n, a) in data:
            Ci = tensor_cx(Ci, C_infinity(P, n, a, top), top)
        h = homology_dims(Ci, top)
        check(is_complex(Ci) and h == [M.dim] + [0] * (top - 1) and
              all(is_free(X) for X in Ci.mods[1:top]) and
              iso_full(module_quotient_H0(Ci), M),
              'Theorem 5.14.2: a projective resolution of M (%s)' % tag)
        if M.dim == 1 and len(data) == 2:
            hd = homology_dims(Cc)
            n1, n2 = data[0][0], data[1][0]
            exp = [0] * (n1 + n2 - 1)
            for i in (0, n1 - 1, n2 - 1, n1 + n2 - 2):
                exp[i] += 1
            check(hd == exp, 'Kunneth: H_*(C_zeta1 (x) C_zeta2) (%s)' % tag)
    k4 = trivial(F2, V4)
    thm_5_14_2(P4, [(2, sq(x1)), (2, sq(x2))], k4, True, 'V4, x1^2, x2^2')
    thm_5_14_2(P4, [(2, sq(x1)), (3, cub(x2))], k4, True, 'V4, x1^2, x2^3')
    thm_5_14_2(P4, [(2, sq(x1)), (2, sq(x1))], k4, False, 'V4, x1^2, x1^2')
    G8 = D8.G
    k8 = trivial(F2, G8)
    s12 = D8.C.mul(D8.x1 + D8.x2, 1, D8.x1 + D8.x2, 1)
    thm_5_14_2(D8.P, [(2, s12), (2, D8.z)], k8, True, 'D8, (x1+x2)^2, z')
    Maba = string_mod(F2, G8, letters('a b a'))
    thm_5_14_2(D8.P, [(2, D8.C.mul(D8.x2, 1, D8.x2, 1))], Maba, True,
               'D8, M(aba), x2^2')
    thm_5_14_2(D8.P, [(2, D8.C.mul(D8.x1, 1, D8.x1, 1))], Maba, False,
               'D8, M(aba), x1^2')
    # ------------------------------------------------------------------
    # Lemma 5.14.4: the long exact sequence of the two row spectral
    # sequence with d_n = multiplication by zeta, in dimensions:
    # dim Ext^j(P_(n-1)/L_zeta, k) = dim Coker(zeta : H^(j-1) -> H^(j+n-1))
    #   + dim Ker(zeta : H^j -> H^(j+n))
    for (P, n, a, C) in [(P4, 2, sq(x1), C4), (P4, 2, C4.mul(x1, 1, x2, 1),
                                               C4),
                         (P4, 2, sq(x1) + C4.mul(x1, 1, x2, 1) + sq(x2), C4),
                         (P4, 3, cub(x2), C4),
                         (D8.P, 2, D8.z, D8.C),
                         (D8.P, 2, D8.C.mul(D8.x1, 1, D8.x1, 1), D8.C),
                         (P9, 2, vector(F3, [1, 0, 0]), Cohom(P9)),
                         (P9, 2, vector(F3, [1, 1, 1]), Cohom(P9))]:
        Cz, _ = C_zeta(P, n, a)
        X = Cz.mods[-1]
        Xj = X
        for j in range(0, 9 - 2 * n + 1):
            ext = top_dim(Xj)
            mj = C.mult_matrix(a, n, j)
            coker = P.b[j + n - 1] - (rk(C.mult_matrix(a, n, j - 1))
                                      if j >= 1 else 0)
            ker = P.b[j] - rk(mj)
            check(ext == coker + ker, 'Lemma 5.14.4 (%s, n = %d, j = %d)'
                  % (P.G.name, n, j))
            Xj = omega(Xj)
    # ------------------------------------------------------------------
    # Examples (pp. 201-202): minimal resolutions of k for GL_3(F_2)
    # (char 2) and A_6 (char 3) against the total complexes of the printed
    # double complexes
    out = MINRES(libgap.eval('GL(3, 2)'), libgap.GF(2), 10)
    sd = [int(x) for x in out[0]]
    check(sorted(sd) == [1, 3, 3, 8], 'GL3(2): simple modules 1, 3, 3, 8')
    iM, iN = [i for i, x in enumerate(sd) if x == 3]
    ik, iS = sd.index(1), sd.index(8)
    pattern = ['k', 'N', 'M']
    for n, mult in enumerate(out[2]):
        mult = [int(x) for x in mult]
        cnt = {'k': 0, 'M': 0, 'N': 0}
        for i in range(n + 1):
            cnt[pattern[(i - (n - i)) % 3]] += 1
        check(mult[ik] == cnt['k'] and sorted([mult[iM], mult[iN]]) ==
              sorted([cnt['M'], cnt['N']]) and mult[iS] == 0,
              'p. 201: GL3(2), P_%d is the total complex in degree %d'
              % (n, n))
    out = MINRES(libgap.eval('AlternatingGroup(6)'), libgap.GF(9), 13)
    sd = [int(x) for x in out[0]]
    check(sorted(sd) == [1, 3, 3, 4, 9], 'A6 (char 3): simple modules')
    ik, iN = sd.index(1), sd.index(4)
    iL, iM = [i for i, x in enumerate(sd) if x == 3]
    i9 = sd.index(9)
    grid = a6_grid()
    for n, mult in enumerate(out[2]):
        mult = [int(x) for x in mult]
        cnt = {'k': 0, 'L': 0, 'M': 0, 'N': 0}
        for (i, j), e in grid.items():
            if i + j == n:
                cnt[e] += 1
        check(mult[ik] == cnt['k'] and mult[iN] == cnt['N'] and
              sorted([mult[iL], mult[iM]]) == sorted([cnt['L'], cnt['M']])
              and mult[i9] == 0,
              'p. 202: A6, P_%d is the total complex in degree %d' % (n, n))
    # ------------------------------------------------------------------
    # Corollary 5.14.6 over Z for C_p: C = (Z G -> Z G, g - 1) has
    # H_0 = H_1 = Z with trivial action; R (x) C for R = F_p, Z/p^2, Q
    for p in (2, 3, 5):
        G = cyclic(p)
        g = G.gens[0]
        A = matrix_ZZ_perm(G, g) - identity_matrix_ZZ(p)
        sm = A.smith_form()[0].diagonal()
        check(sorted(x for x in sm if x != 0) == [1] * (p - 1) and
              sm.count(0) == 1, 'Corollary 5.14.6: H_0(C) = Z, H_1(C) = Z '
              '(C_%d)' % p)
        ker = A.right_kernel_matrix()
        check(ker.nrows() == 1 and (matrix_ZZ_perm(G, g) * ker.row(0) ==
                                    ker.row(0)),
              'Corollary 5.14.6: G acts trivially on H_1(C)')
        for R in (GF(p), Zmod(p * p), QQ):
            AR = A.change_ring(R)
            if R is QQ or R.is_field():
                h1 = p - AR.rank()
            else:
                h1 = len([x for x in A.smith_form()[0].diagonal()
                          if R(x) == 0])
            check(h1 == 1, 'R (x) C has H_1 = R (C_%d, %s)' % (p, R))
    # ------------------------------------------------------------------
    # Proof of Theorem 5.14.5, p. 205: E_2 = E_2^(*0) (x) Hom(H_*(C), R);
    # the rows of the last spectral sequence are sums of copies (V4,
    # C = C_x1^2 (x) C_x2^2: H_1(C) = k^2)
    Cc = tensor_cx(C_zeta(P4, 2, sq(x1))[0], C_zeta(P4, 2, sq(x2))[0])
    hd = homology_dims(Cc)
    check(hd == [1, 2, 1], 'H_*(C_x1^2 (x) C_x2^2) = k, k^2, k')
    ext, _ = coinvariant_cohomology(Cc)
    check(sum(ext) > 0 and 2 * sum(ext) != sum(ext), 'p. 205: the row '
          'q = 1 is Ext^*(C, k)^2, not Ext^*(C, k)')
    refuted(hd[1] == 1, 'p. 205 as printed: every row isomorphic to '
            'Ext^*(C (x) M, M) (needs rank H_q(C) = 1)')
    # E_2^(0q) = Hom_kG(H_q(C), End_k(M)) has dimension rank H_q(C) . dim
    # End_kG(M): for M = k + k it is not the dual of H_q(C)
    M = dsum(k4, k4)
    endM = len(end_space(M))
    check(endM == 4 and hd[1] * endM != hd[1], 'p. 205: E_2^(0*) is not a '
          'free R-module dual to H_*(C) for M = k + k')


def module_quotient_H0(Cc):
    """H_0 of a complex as a module: C_0 / Im(d_1)."""
    M0 = Cc.mods[0]
    Im = colbasis(Cc.d[1]) if len(Cc) > 1 else mat(M0.F, M0.dim, 0)
    return quot(M0, Im)[0] if Im.ncols() else M0


def end_space(M):
    """A basis of End_kG(M)."""
    F, d = M.F, M.dim
    I = ident(F, d)
    A = vcat(F, d * d, [conv(I.tensor_product(M.act[h]) -
                             M.act[h].transpose().tensor_product(I), F)
                        for h in M.G.gens])
    return kernel_cols(A).columns()


def matrix_ZZ_perm(G, g):
    """The regular representation of g on Z G (columns)."""
    n = G.n
    return _matrix(ZZ, n, n, {(G.mul[g][t], t): 1 for t in range(n)})


def identity_matrix_ZZ(n):
    return _matrix(ZZ, n, n, {(i, i): 1 for i in range(n)})


def a6_grid():
    """The double complex printed on p. 202 (our diagram a6-resolution):
    rows from the bottom (j = 0), first column and entries."""
    rows = [(0, 'kNL'), (0, 'NkkNL'), (0, 'MkkNNkkNL'), (1, 'NNkkNNkkNL'),
            (1, 'MNkkNNkkNN'), (2, 'kNNkkNNkk'), (2, 'kNNkkNNkk'),
            (2, 'NkkNNkk'), (2, 'MkkNNkk'), (3, 'NNkk'), (3, 'MNkk')]
    grid = {}
    for j, (first, ents) in enumerate(rows):
        for i, e in enumerate(ents):
            grid[(first + i, j)] = e
    return grid



def hom_G_basis(A, M):
    """Hom_kG(A, M) as a matrix whose columns are the row-major flattenings
    of a basis."""
    F, a, m = A.F, A.dim, M.dim
    Ia, Im = ident(F, a), ident(F, m)
    eqs = vcat(F, a * m, [conv(M.act[g].tensor_product(Ia) -
                               Im.tensor_product(A.act[g].transpose()), F)
                          for g in A.G.gens])
    return kernel_cols(eqs)


def tate_dims(P, M, lo, hi):
    """dim of the cohomology of Hom_kG(P_+-, M) in degrees lo..hi, P_+- the
    complete resolution (p. 206): P_i for i >= 0, P_(-i-1) = P_i^*,
    P_0 -> P_(-1) the composite P_0 -> k -> P_0^*."""
    F, G = P.F, P.G
    n = G.n
    need = max(hi + 1, -lo)
    mods, dmap = {}, {}
    for i in range(lo - 1, hi + 2):
        if i >= 0:
            mods[i] = free(F, G, P.b[i])
        else:
            mods[i] = dual(free(F, G, P.b[-i - 1]))
    for i in range(lo, hi + 2):
        if i >= 1:
            dmap[i] = P.d[i]
        elif i == 0:
            ones = mat(F, n, 1, {(t, 0): 1 for t in range(n)})
            dmap[0] = ones * P.eps          # P_0 -> P_(-1) = P_0^*
        else:
            dmap[i] = P.d[-i].transpose()   # P_i^dual -> P_(i-1)^dual
    for i in range(lo + 1, hi + 2):
        assert (dmap[i - 1] * dmap[i]).is_zero()
    out = {}
    for i in range(lo, hi + 1):
        HB = hom_G_basis(mods[i], M)
        m, a = M.dim, mods[i].dim
        Ia1 = mods[i + 1].dim
        # delta : X -> X o d_(i+1), row-major: (I_m (x) d^T)
        dl = conv(ident(F, m).tensor_product(dmap[i + 1].transpose()), F)
        Z = rk(dl * HB) if HB.ncols() else 0
        zdim = HB.ncols() - Z
        HBp = hom_G_basis(mods[i - 1], M)
        dp = conv(ident(F, m).tensor_product(dmap[i].transpose()), F)
        bdim = rk(dp * HBp) if HBp.ncols() else 0
        out[i] = zdim - bdim
    return out


def cohom_dims(P, M, nmax):
    """dim H^n(G, M) for 0 <= n <= nmax (cochains Hom_kG(P_n, M))."""
    out = []
    for n in range(nmax + 1):
        dn = cochain_coboundary(P, M, n)
        z = P.b[n] * M.dim - rk(dn)
        b = rk(cochain_coboundary(P, M, n - 1)) if n >= 1 else 0
        out.append(z - b)
    return out


def section_5_15():
    F2, F3 = GF(2), GF(3)
    # Tate cohomology from the complete resolution (p. 206): degrees -3..3
    for (G, F, mods) in ((cyclic(3), F3, None), (dihedral(1), F2, None),
                         (dihedral(2), F2, None)):
        P = Resolution(F, G, 5)
        k = trivial(F, G)
        Ms = [k, regular(F, G), omega(k), dsum(k, omega_inv(k))]
        if G.n == 8:
            Ms.append(string_mod(F, G, letters('a b a')))
        for im, M in enumerate(Ms):
            T = tate_dims(P, M, -4, 3)
            H = cohom_dims(P, M, 4)
            Hd = cohom_dims(P, dual(M), 4)
            Nm = M.elem({g: 1 for g in range(G.n)})
            fix = fixed(M).ncols()
            check(all(T[n] == H[n] for n in (1, 2, 3)),
                  'p. 206: Tate^n = H^n for n > 0 (%s)' % G.name)
            check(T[0] == fix - rk(Nm), 'p. 206: Tate^0 = M^G / Tr(M)')
            IM = rk(hcat(F, M.dim, [M.X(g) for g in G.gens]))
            check(T[-1] == (M.dim - rk(Nm)) - IM, 'p. 206: Tate^-1 = '
                  'Ker(N) / I M')
            check(all(T[-n - 1] == Hd[n] for n in (1, 2, 3)),
                  'p. 206: Tate^(-n-1) = H_n(G, M) = H^n(G, M^*)^*, n > 0')
            if im == 1:
                # the graded reading H^* = Tate^* fails in degree 0
                refuted(T[0] == H[0], 'p. 206 as printed: Tate^*(G, M) = '
                        'H^*(G, M) (degree 0, M = kG)')
    # Theorem 5.15.2: a gap of length 2 for S3 in characteristic 3
    # (M = sign), no longer gaps
    out = MINRES(libgap.eval('SymmetricGroup(3)'), libgap.GF(3), 12)
    mult = [[int(x) for x in row] for row in out[2]]
    isgn = 1
    ext = [mult[n][isgn] for n in range(13)]   # Ext^n(k, sgn), n >= 0
    tate = {}
    for n in range(1, 13):
        tate[n] = ext[n]
    tate[0] = 0
    tate[-1] = 0
    for n in range(2, 13):
        tate[-n] = tate[n - 1]                 # Tate duality, sgn* = sgn
    seq = [tate[n] for n in range(-12, 13)]
    runs, cur = [], 0
    for v in seq:
        if v == 0:
            cur += 1
        else:
            if cur:
                runs.append(cur)
            cur = 0
    check(any(seq) and max(runs) == 2 and ext[1:9] == [1, 1, 0, 0, 1, 1, 0,
                                                       0],
          'Theorem 5.15.2: Tate^n(S3, sign) (char 3) has gaps of length '
          'exactly two and does not vanish')
    # Proof of Theorem 5.15.2: d_k has bidegree (k, 1 - k) in the
    # spectral sequence of the double complex Hom(P_+- (x) C, M)
    for k in range(2, 10):
        check(k + (1 - k) == 1, 'p. 207: d_k raises the total degree by one')
        refuted(k + (-k - 1) == 1, 'p. 207 as printed: bidegree (k, -k-1)')
    for r in range(1, 7):
        nz = [k for k in range(2, r + 5) for q in range(r + 1)
              if 0 <= q - k + 1 <= r]
        check(max(nz) == r + 1, 'd_k = 0 for k > r + 1 (rows 0..r)')
        nzp = [k for k in range(2, r + 5) for q in range(r + 1)
               if 0 <= q - k - 1 <= r]
        refuted(nzp and max(nzp) == r + 1, 'printed bidegree: the bound '
                'k > r + 1 of the same sentence')
        for m in range(-4, 5):
            for k in range(2, r + 2):
                check(m <= m - 1 + k <= m + r and
                      m <= m + r + 1 - k <= m + r,
                      'p. 207: d_k from E^(m-1, r) and into E^(m+r+1, 0) '
                      'meet only the zero columns m..m+r')


def section_5_16():
    # Theorem 5.16.1 needs integral coefficients: C2 -> S3 induces an
    # isomorphism in mod 2 cohomology (both have H^n = F_2), but Tate^0
    # with Z coefficients is Z/|G| (Z/2 against Z/6).
    out = MINRES(libgap.eval('SymmetricGroup(3)'), libgap.GF(2), 8)
    sd = [int(x) for x in out[0]]
    ik = sd.index(1)
    mult = [[int(x) for x in row] for row in out[2]]
    check(all(row[ik] == 1 for row in mult), 'H^n(S3, F_2) = F_2 = '
          'H^n(C2, F_2) for n <= 8')
    check(len(sd) == 2 and sorted(sd) == [1, 2],
          'S3 in characteristic 2: simple modules k and the projective one')


def lambda_n(P, n, alpha):
    """The constant lambda_n of Proposition 5.17.2: lift zeta-hat^* : k ->
    Omega^-n k = (Omega^n k)^* to a chain map from the resolution
    P_(n-1) -> ... -> P_0 -> k to the dual sequence k -> P_0^* -> ... ->
    P_(n-1)^* -> (Omega^n k)^* (transposed maps); the induced map
    Omega^n k -> k is lambda_n zeta-hat."""
    F, G = P.F, P.G
    Om, B = P.omega(n)
    hat = P.hat(n, alpha)
    duals = {m: dual(free(F, G, P.b[m])) for m in range(n)}
    f = {}
    # f_0 : P_0 -> P_(n-1)^*, iota^* f_0 = zeta-hat^* eps
    y = B.transpose().solve_right(hat.transpose())
    f[0] = dual_free_map(duals[n - 1], P.b[0], y)
    for i in range(1, n):
        tgt = f[i - 1] * P.gen_cols(i)
        dT = P.d[n - i].transpose()             # P_(n-1-i)^* -> P_(n-i)^*
        y = dT.solve_right(tgt)
        f[i] = dual_free_map(duals[n - 1 - i], P.b[i], y)
        assert dT * f[i] == f[i - 1] * P.d[i]
    lam_map = f[n - 1] * B                      # Omega^n k -> P_0^*
    ones = mat(F, G.n, 1, {(t, 0): 1 for t in range(G.n)})
    coeff = ones.solve_right(lam_map)           # 1 x dim Omega
    i = next(j for j in range(Om.dim) if hat[0, j] != 0)
    lam = coeff[0, i] / hat[0, i]
    assert coeff == lam * hat
    return lam


def dual_free_map(Dm, b_src, Y):
    """The kG-map F[G]^(b_src) -> Dm with e_i |-> column i of Y."""
    G = Dm.G
    n = G.n
    cols = hcat(Dm.F, Dm.dim, [Dm.act[g] * Y for g in range(n)])
    return cols.matrix_from_columns([g * b_src + i for i in range(b_src)
                                     for g in range(n)])


def section_5_17():
    F2, F3, F5, F7 = GF(2), GF(3), GF(5), GF(7)
    # Proposition 5.17.2: Omega^n(zeta-hat^*) = (-1)^(n(n+1)/2) zeta-hat;
    # the left-hand map of the last diagram of the proof is this constant
    for (G, F, nmax) in ((cyclic(3), F3, 6), (cyclic(5), F5, 6),
                         (cyclic(7), F7, 5), (elementary(3, 2), F3, 3),
                         (dihedral(1), F2, 3)):
        P = Resolution(F, G, nmax)
        for n in range(1, nmax + 1):
            for alpha in all_classes(F, P.b[n])[:3]:
                lam = lambda_n(P, n, alpha)
                check(lam == F((-1) ** (n * (n + 1) // 2)),
                      'Proposition 5.17.2: lambda_%d (%s)' % (n, G.name))
                if F.characteristic() != 2 and n % 2:
                    refuted(lam == F((-1) ** (n * (n - 1) // 2)),
                            'p. 210 as printed: label (-1)^(n(n-1)/2)')
    # Theorem 5.17.3 and Corollary 5.17.4: the complex C, its minimal part
    # C' and the Poincare series of H^*(Hom_kG(C, k))
    V4 = dihedral(1)
    P4 = Resolution(F2, V4, 8)
    C4 = Cohom(P4)
    x1, x2 = dual_basis_classes(C4, V4, V4.gens)
    sq = lambda C, a: C.mul(a, 1, a, 1)
    D8 = Dihedral(2, F2, 8)
    Q8 = quaternion8()
    PQ = Resolution(F2, Q8, 8)
    E9 = elementary(3, 2)
    P9 = Resolution(F3, E9, 6)
    C9 = Cohom(P9)
    Q3 = cyclic(3)
    PQ3 = Resolution(F3, Q3, 2)
    co = coords_elementary(E9, E9.gens, 3)
    t = Q3.gens[0]
    bock = []
    for (a, b) in ((1, 0), (0, 1)):
        proj = [Q3.power(t, (a * co[g][0] + b * co[g][1]) % 3)
                for g in range(E9.n)]
        bock.append(inflation_matrix(P9, PQ3, proj, 2) * vector(F3, [1]))
    C3g = cyclic(3)
    P3 = Resolution(F3, C3g, 6)
    s12 = D8.C.mul(D8.x1 + D8.x2, 1, D8.x1 + D8.x2, 1)
    cases = [('V4, x1^2, x2^3', P4, C4, [(2, sq(C4, x1)),
                                         (3, C4.mul(sq(C4, x2), 2, x2, 1))]),
             ('V4, x1^2, x2^2', P4, C4, [(2, sq(C4, x1)), (2, sq(C4, x2))]),
             ('D8, (x1+x2)^2, z', D8.P, D8.C, [(2, s12), (2, D8.z)]),
             ('Q8, e', PQ, Cohom(PQ), [(4, vector(F2, [1]))]),
             ('E9, Bocksteins', P9, C9, [(2, bock[0]), (2, bock[1])]),
             ('C3, x^2', P3, Cohom(P3), [(4, vector(F3, [1]))])]
    printed_fails = False
    for (tag, P, C, data) in cases:
        Cc = None
        for (n, a) in data:
            Cz, _ = C_zeta(P, n, a)
            Cc = Cz if Cc is None else tensor_cx(Cc, Cz)
        s = sum(n - 1 for n, _ in data)
        check(len(Cc) == s + 1 and all(is_free(X) for X in Cc.mods),
              'Theorem 5.17.3: C is a complex of projectives of length s '
              '(%s)' % tag)
        ranks = [top_dim(X) for X in Cc.mods]
        hdims, _ = coinvariant_cohomology(Cc)
        check(hdims == hdims[::-1] and hdims[0] == 1,
              'Corollary 5.17.4 (corrected): f(t) = sum t^i dim H^i(Hom(C, '
              'k)) satisfies t^s f(1/t) = f(t) (%s)' % tag)
        if ranks != ranks[::-1]:
            printed_fails = True
            refuted(ranks == ranks[::-1], 'Corollary 5.17.4 as printed: '
                    'f(t) = sum t^i dim Hom(C_i, k) = %s (%s)' % (ranks, tag))
        # Theorem 5.18.1 (Cohen-Macaulay case): H^*(Hom(C, k)) is
        # H^*(G, k)/(zeta_1, ..., zeta_r)
        quo = []
        for d in range(s + 1):
            imgs = []
            for (n, a) in data:
                if d - n >= 0:
                    A = C.mult_matrix(a, n, d - n)
                    imgs.append(A)
            I = hcat(P.F, P.b[d], imgs) if imgs else mat(P.F, P.b[d], 0)
            quo.append(P.b[d] - rk(I))
        check(quo == hdims, 'proof of 5.18.1: H^*(Hom(C, k)) = H^*(G, k) / '
              '(zeta_i) (%s)' % tag)
    check(printed_fails, 'Corollary 5.17.4 as printed fails for some C')



def fe_numerator(dims, degs):
    """f = (sum dims[n] t^n) prod (1 - t^d) mod t^(len(dims)): coefficients."""
    N = len(dims)
    f = list(dims)
    for d in degs:
        g = [f[i] - (f[i - d] if i >= d else 0) for i in range(N)]
        f = g
    return f


def section_5_18():
    F2, F3 = GF(2), GF(3)
    R = PolynomialRing(QQ, 't')
    t = R.gen()
    # Theorem 5.18.1: for Cohen-Macaulay H^*(G, k), free of rank f(1) over
    # a polynomial ring on classes of degrees n_i, f(t) = p(t) prod (1 -
    # t^(n_i)) is a palindromic polynomial of degree s = sum (n_i - 1), so
    # p(1/t) = (-t)^r p(t) (the computation of p. 212, formalised in
    # checks/lean/BensonCohomology/PoincareFunctionalEquation.lean)
    N = 13
    groups = [('V4', dihedral(1), F2, (2, 2)),
              ('E8', elementary(2, 3), F2, (2, 2, 2)),
              ('E9', elementary(3, 2), F3, (2, 2)),
              ('C3', cyclic(3), F3, (2,)), ('C9', cyclic(9), F3, (2,)),
              ('D8', dihedral(2), F2, (2, 2)),
              ('D16', dihedral(4), F2, (2, 2)),
              ('Q8', quaternion8(), F2, (4,)),
              ('C4xC2', grp_from([cyc(range(1, 5)), cyc([5, 6])], 'C4xC2'),
               F2, (2, 2))]
    for (nm, G, F, degs) in groups:
        P = Resolution(F, G, N if G.n <= 16 else 9)
        dims = P.b
        f = fe_numerator(dims, degs)
        s = sum(d - 1 for d in degs)
        fpoly = f[:s + 1]
        check(all(c == 0 for c in f[s + 1:]) and fpoly == fpoly[::-1] and
              fpoly[0] == 1, 'Theorem 5.18.1: f(t) palindromic of degree s '
              '(%s, degrees %s, f = %s)' % (nm, degs, fpoly))
        p = sum(c * t ** i for i, c in enumerate(fpoly)) / \
            prod_([1 - t ** d for d in degs])
        r = len(degs)
        check(p(1 / t) == (-t) ** r * p, 'p(1/t) = (-t)^r p(t) (%s)' % nm)
    # GL_3(F_2) at p = 2: dimensions from the minimal resolution
    out = MINRES(libgap.eval('GL(3, 2)'), libgap.GF(2), 13)
    sd = [int(x) for x in out[0]]
    ik = sd.index(1)
    dims = [int(row[ik]) for row in out[2]]
    f = fe_numerator(dims, (2, 3))
    check(f[:4] == [1, 0, 0, 1] and all(c == 0 for c in f[4:]),
          'GL3(2): p(t) = (1 + t^3)/((1 - t^2)(1 - t^3)), f palindromic')
    # The semidihedral group of order 16 (not Cohen-Macaulay, Evens and
    # Priddy): its Poincare series fails the functional equation.
    SD = semidihedral16()
    P = Resolution(F2, SD, 16)
    dims = P.b
    found = None
    for degs in ((1, 4), (1, 1), (2, 4), (1, 3), (1, 2)):
        f = fe_numerator(dims, degs)
        if all(c == 0 for c in f[8:]):
            found = (degs, f[:8])
            break
    check(found is not None, 'SD16: a rational form of the Poincare series')
    degs, fpoly = found
    p = sum(c * t ** i for i, c in enumerate(fpoly)) / \
        prod_([1 - t ** d for d in degs])
    check(p(1 / t) != t ** 2 * p, 'SD16: p(1/t) != (-t)^2 p(t), consistent '
          'with H^*(SD16, k) not Cohen-Macaulay')
    # Corollary 5.18.2: a polynomial cohomology ring has its generators in
    # degree one, p = 2 and G/O_2'(G) elementary abelian: S3 (p = 2):
    # dims 1, O_2'(S3) = C3, S3/C3 = C2; A4 (p = 2): H^1 = 0, so not
    # polynomial, and A4/O_2'(A4) = A4 is not elementary abelian.
    for (expr, q, polyn) in (('SymmetricGroup(3)', 2, True),
                             ('AlternatingGroup(4)', 4, False)):
        G = libgap.eval(expr)
        out = MINRES(G, libgap.GF(q), 8)
        sd = [int(x) for x in out[0]]
        ik = sd.index(1)
        dims = [int(row[ik]) for row in out[2]]
        O = libgap.PCore(G, 3)
        Q = libgap.FactorGroup(G, O)
        el = bool(libgap.IsElementaryAbelian(Q)) and \
            int(libgap.Size(Q)) % 2 == 0
        check((dims == [1] * 9) == polyn == el, 'Corollary 5.18.2 (%s)'
              % expr)
    # the degree count: for k[x_1..x_r] with degrees d_i the functional
    # equation holds iff all d_i = 1
    for degs in ((1,), (1, 1), (2,), (1, 2), (3, 1, 1), (1, 1, 1)):
        p = 1 / prod_([1 - t ** d for d in degs])
        check((p(1 / t) == (-t) ** len(degs) * p) == all(d == 1
                                                         for d in degs),
              'Corollary 5.18.2: degrees %s' % (degs,))


def main():
    for sec in (section_5_9, section_5_10, section_5_11, section_5_12,
                section_5_13, section_5_14, section_5_15, section_5_16,
                section_5_17, section_5_18):
        sec()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
