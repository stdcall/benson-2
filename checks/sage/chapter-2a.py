"""Exact checks of Chapter 2 "Cohomology of groups", Sections 2.1-2.10 (Sage).

Run: sage -python checks/sage/chapter-2a.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-2a: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), printed pp. 29-73.
Pages are the printed pages; labels are those of content/02-00-*.typ ...
content/02-10-*.typ.  Sections 2.11-2.15 are checked in chapter-2b.py.

Everything is exact: integers, finite fields, number fields, GAP through
libgap (groups, character tables, tables of marks, Schur multipliers),
Sage's simplicial complexes and simplicial sets.  Group cohomology
H^k(G, F_l) is computed from a free resolution of F_l over F_l G built from
kernels (the dimensions do not depend on the random choice of generators);
group homology from the normalised chains of the nerve NG.  Printed readings
that are wrong are kept as refuted checks (`refuted`) beside the corrected
ones.

What is checked, by section:

2.2, 2.4 (pp. 31-44), section_2_2_and_2_4
  * p. 32: RP^infinity = K(Z/2, 1): H_k(RP^n) = H_k(Z/2, Z) for k < n,
    n <= 4 (periodic resolution, Volume I, Section 3.5).
  * Exercises 1, 2 of Section 2.4 (p. 41): the join of r copies of Z/2 is
    S^(r-1) and its quotient by the antipodal map has the homology of
    RP^(r-1) (r <= 6); the join of r circles has the homology of S^(2r-1)
    (r <= 3).
  * Theorems 2.2.3 and 2.4.8 (iii): H_k(NG; F_p) (nerve) has the dimension
    of Ext^k_(F_p G)(F_p, F_p) (free resolution) for C2, C3, C4, V4, S3
    (p = 2, 3), D8, Q8 (k <= 3 to 5); H_k(NG; Z) = H_k(Z/m, Z) for
    m = 2, 3, 4, also against Sage's ClassifyingSpace.
  * Exercise 3 of Section 2.4 (pp. 43-44): N C(G)/G = NG (faces, free
    action, |G|^n orbits) and N C(G) has the homology of a point in low
    degrees (S3, C4).
2.5 (pp. 44-48), section_2_5
  * The tables of p. 47 from the loop spaces of p. 46: KO~(S^n) =
    pi_0(Omega^n(BO x Z)) = Z, Z/2, Z/2, 0, Z, 0, 0, 0 and K~(S^n) = Z, 0
    (n < 16), with pi_0 of BO x Z, O, O/U, U/Sp, BSp x Z, Sp, Sp/U, U/O; the
    printed unreduced headings K(S^n), KO(S^n) refuted (K(B) = K~(B) + Z,
    p. 45).  Omega O ~ O/U: pi_0(Omega O) = pi_1(O) = KO~(S^2) has order 2;
    the printed "O/U x Z/2" (4 components) refuted.  U(n) lies in SO(2n):
    det [[A, -B], [B, A]] = det(A + iB) det(A - iB) symbolically (n <= 3), so
    O(2n)/U(n) has two components.
2.6 (pp. 48-51), section_2_6
  * pp. 49-50: Z[x_1..x_n]^(Sigma_n) = Z[sigma_1..sigma_n] degree by degree
    (unimodular transition to the orbit sums, n <= 4, degree <= 8; hence
    also over Z/2); the Whitney sum formula for the sigma_k (Proposition
    2.6.1 (ii)).
  * Chern classes of the regular representation of Z/m: c = prod_a (1 + a x)
    in (Z/m)[x], = 1 - x^(p-1) for m = p prime (m <= 13), the regular
    character being the sum of the m linear characters (GAP).
  * p. 50: H^k((Z/2)^n; F_2) = binom(k + n - 1, n - 1) (n <= 3, resolution);
    Stiefel-Whitney classes (Proposition 2.6.2 (ii), (iii), naturality):
    w(regular representation of (Z/2)^n) = 1 + sum of the Dickson
    invariants, GL_n(F_2)-invariant (n <= 4, invariance for n <= 3); w of
    the natural representation of S_4 on the normal V_4 and on
    <(1,2), (3,4)>; w_1 = class of det = sign.
2.8 (pp. 56-60), section_2_8
  * Tables of marks of eight groups (C2, C4, V4, S3, D8, Q8, A4, S4): GAP
    against fixed point counts; products in b(G) have non-negative integral
    coordinates; rank I_G = #classes - 1; b(C_p): x^2 = -p x for
    x = [C_p/1] - p (p <= 7), so I^n = p^(n-1) I.
  * p. 59: the G-free transitive G' x G-sets are the cosets of the
    Delta_(H', phi) (counts of classes of subgroups L of G' x G with
    L n (1 x G) = 1, for G', G in {C2, C3, S3}).
  * The boxed formula of p. 59 for zeta_(H', phi) o zeta_(H'', phi') against
    the composition of bisets G'' x_(H'') G' x_(H') G, for all 27 triples of
    groups in {C2, C3, S3} and all pairs of basis elements (453
    compositions; with c_x in place of c_(x^-1) the comparison fails);
    b(G, G) is associative with identity zeta_(G, id) (G = C2, C3, S3).
2.9, 2.10 (pp. 60-73), section_2_9_2_10
  * pp. 64, 71: pi_(2j-1)(F psi^q) = Z/(q^j - 1), pi_(2j) = 0 from the exact
    sequence (q <= 64, j <= 8), no p-torsion; the printed Z/(q^(2j) - 1)
    refuted; K_1(F_q) = GL_n(F_q)/E_n(F_q) cyclic of order q - 1 (n <= 3,
    q <= 9, elementary matrices in GAP); E_n = [GL_n, GL_n], perfect; the
    three block identities of p. 70 (generic 2 x 2 blocks); H_2(SL_n(F_q))
    = 0 in four cases of the stable range.
  * p. 64: (q^k - 1) c_k = 0 in F_l exactly for r | k.
  * Lemma 2.9.2: |GL_n(F_q) : Sigma_m wr GL_r(F_q)| prime to odd l (q <= 27,
    n <= 12, l <= 13); for l = 2 the subgroup Sigma_[n/2] wr GL_2(F_q) x
    (F_q^x)^(n - 2[n/2]) has odd index; Sigma_n wr GL_1(F_q) has even index
    for q = 3 mod 4 but odd index for q = 1 mod 4 (the printed "is not odd"
    of p. 66 refuted: GL_2(F_5), index 15).
  * Theorem 2.9.3 and Lemma 2.9.2: from one free resolution per case,
    dim H^k(GL_n(F_q), F_l) and the kernel of the restriction to C^m (the
    diagonal torus for r = 1, a cyclic subgroup of order q^r - 1 for n = r;
    restriction to a subgroup computed on the same resolution) for GL_1(F_3)
    (l = 2), GL_1(F_7) (3), GL_2(F_2) (3), GL_2(F_3) (2), GL_2(F_5) (2, 3),
    GL_2(F_7) (2), GL_2(F_4) (3, 5), GL_3(F_2) (3, 7): the restriction is
    injective in every computed degree; the dimensions are the Poincare
    series of F_l[c_jr] (x) Lambda(e_jr), j <= m; they equal those of the
    invariants of Sigma_m wr Z/r on H^*(C^m) for l odd (and m = 1), so the
    second map is an isomorphism there, and are strictly smaller for l = 2,
    m = 2 (GL_2(F_3), GL_2(F_5), GL_2(F_7): the printed isomorphism refuted
    for l = 2; corrected to "injective, and an isomorphism if l is odd").
    GL_3(F_3), l = 2: GL_2(F_3) x GL_1(F_3) has odd index 117 and its
    cohomology injects into that of the diagonal (Z/2)^3 (k <= 4).
    GL_2(F_5), l = 2: the images c_j -> sigma_j(y), e_j -> sum_i x_i
    sigma_(j-1)(y_k, k != i) in H^*((Z/4)^2, F_2) generate a subring with the
    dimensions of H^*(GL_2(F_5), F_2).
  * The exceptional relation (p. 67, Theorem 2.9.3): GL_1(F_3) = Z/2,
    e_1 = x, c_1 = x^2: the printed sum_(a=0)^(jr) gives e_1^2 = 0
    (refuted), the corrected sum_(a=0)^(jr-1) gives e_1^2 = c_1; for
    GL_n(F_q), q = 3 mod 4 (n <= 3, q = 3, 7, 11), e_1 spans H^1 and
    e_1^2 != 0 (no homomorphism to Z/4 lifts e_1), for q = 1 mod 4
    e_1^2 = 0; on (Z/2)^n with c_j -> sigma_j(x_1^2, ...), e_j -> sum_i x_i
    sigma_(j-1)(x_k^2, k != i) the corrected relation holds for all
    j <= n <= 6 and the printed one fails; the subring of F_2[x_1, x_2]
    generated by these images has the dimensions of H^*(GL_2(F_3), F_2).
  * p. 67, "the mod p cohomology of BGL_n(F_q) vanishes in positive degrees
    at most d(p - 1)": refuted by H^1(GL_2(F_2), F_2) != 0 (d(p-1) = 1) and
    H^2(GL_2(F_4), F_2) != 0 (d(p-1) = 2; Schur multiplier of GL_2(F_4) =
    Z/3 x A_5).  The corrected range 0 < i < d(p - 1): H^i(GL_2(F_q), F_p) =
    0 through the Borel subgroup (index q + 1 prime to p) for q = 4, 8, 9,
    and H^1(GL_n(F_q), F_p) = 0 for GL_3(F_4), GL_3(F_3), GL_4(F_2),
    GL_2(F_9).

What is NOT established.  No general theorem is proved: every check
concerns the listed groups, primes, degrees and ranges.  The topological
statements (Bott periodicity, the Atiyah completion theorem, the Segal
conjecture, Quillen's theorems) are not checked as such: the pi_0 of the
eight spaces of p. 46 are taken from the standard facts quoted in
section_2_5 (O(n) has two components, U(n), Sp(n) are connected); only
the realification identity is computed.  The restriction of e_j to
(Z/2)^n is the one forced by the primitivity of e_j for the H-space
structure of F psi^q (following Quillen); it is not derived here.  The
injectivity of Lemma 2.9.2 is checked only in the listed cases and
degrees; the vanishing of H^*(GL(F_q), F_p) in all positive degrees is not
checked (it follows from Quillen's theorem BGL(F_q)^+ ~ F psi^q).  Nothing here compares our text with the
printed book.
"""


import itertools

import numpy as np
from sage.all import (
    GF, QQ, ZZ, ChainComplex, Partitions, PolynomialRing, QuadraticField,
    SimplicialComplex, Zmod, binomial, factorial, gcd, groups, libgap, matrix,
    prod, set_random_seed, simplicial_complexes, simplicial_sets, valuation,
    vector,
)

SCOPE = 'chapter-2a'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


# ---------------------------------------------------------------------------
# Groups as multiplication tables (elements 0..N-1, sorted as in GAP)
# ---------------------------------------------------------------------------

class TGroup:
    """A finite group given by GAP, with its multiplication table."""

    def __init__(self, G, name):
        self.G = G
        self.name = name
        self.elts = G.AsSSortedList()
        tab = gap('function(e) return List(e, g -> List(e, h -> '
                  'PositionSorted(e, g*h))); end')(self.elts)
        self.mul = np.array([[int(x) - 1 for x in row] for row in tab],
                            dtype=np.int64)
        self.N = len(self.mul)
        self.one = int(self.elts.Position(G.Identity())) - 1
        self.inv = [int(np.where(self.mul[g] == self.one)[0][0])
                    for g in range(self.N)]

    def index(self, x):
        return int(self.elts.Position(x)) - 1

    def m(self, a, b):
        return int(self.mul[a][b])

    def conj_classes(self):
        seen, classes = set(), []
        for g in range(self.N):
            if g in seen:
                continue
            cl = {self.m(self.m(h, g), self.inv[h]) for h in range(self.N)}
            seen |= cl
            classes.append(sorted(cl))
        return classes

    def centraliser(self, g):
        return [h for h in range(self.N) if self.m(h, g) == self.m(g, h)]

    def subgroup(self, gens):
        S = {self.one}
        frontier = [self.one]
        while frontier:
            x = frontier.pop()
            for s in gens:
                y = self.m(x, s)
                if y not in S:
                    S.add(y)
                    frontier.append(y)
        return sorted(S)


def free_resolution(T, ell, top):
    """A free resolution of F_ell over F_ell G up to P_(top+1): returns
    (A, gens, sizes): A[n] is the coboundary Hom(P_n, F) -> Hom(P_(n+1), F)
    (s_(n+1) x s_n, acting on columns), gens[n] the images in P_n of the free
    generators of P_(n+1) (as integer vectors), sizes[n] = s_n."""
    F = GF(ell)
    N = T.shape[0]
    gi = np.arange(N)[:, None]

    def orbit(v, s):
        v = v.reshape(s, N)
        W = np.zeros((N, s, N), dtype=np.int64)
        for i in range(s):
            Wi = np.zeros((N, N), dtype=np.int64)
            Wi[gi, T] = v[i][None, :]
            W[:, i, :] = Wi
        return W.reshape(N, s * N)

    s_prev = 1
    D = matrix(F, np.ones((N, 1), dtype=np.int64))
    A, sizes, allgens = [], [1], []
    for n in range(top + 1):
        K = D.left_kernel()
        kdim = K.dimension()
        Kb = K.basis_matrix()
        M, rank, gens = None, 0, []
        while rank < kdim:
            c = matrix(F, 1, kdim, [F.random_element() for _ in range(kdim)])
            v = np.array([int(x) for x in (c * Kb).list()], dtype=np.int64)
            W = matrix(F, orbit(v, s_prev))
            M2 = (W if M is None else M.stack(W)).echelon_form()
            r = M2.rank()
            if r > rank:
                gens.append(v)
                M, rank = M2.matrix_from_rows(range(r)), r
        D = matrix(F, np.vstack([orbit(w, s_prev) for w in gens]))
        A.append(matrix(F, [[int(w[j * N:(j + 1) * N].sum())
                             for j in range(s_prev)] for w in gens]))
        allgens.append(gens)
        sizes.append(len(gens))
        s_prev = len(gens)
    return A, allgens, sizes


def free_resolution_cohomology(T, ell, top):
    """dim H^k(G, F_ell), 0 <= k <= top (the dimensions do not depend on the
    random choice of generators)."""
    A, gens, sizes = free_resolution(T, ell, top)
    return [sizes[n] - (A[n - 1].rank() if n else 0) - A[n].rank()
            for n in range(top + 1)]


def restriction_data(T, inv, ell, top, H):
    """For a subgroup H (element indices) of G: dim H^k(G), dim H^k(H) and
    dim of the kernel of res^G_H in degree k <= top, all from one free
    F_ell G-resolution P_* (free over F_ell H): Hom_H(P_n, F) is the space of
    functions on (generators) x (right cosets Hx)."""
    F = GF(ell)
    N = T.shape[0]
    A, gens, sizes = free_resolution(T, ell, top)
    cos_of = [-1] * N
    reps = []
    for x in range(N):
        if cos_of[x] < 0:
            c = len(reps)
            reps.append(x)
            for h in H:
                cos_of[int(T[h][x])] = c
    nc = len(reps)
    Mcos = np.zeros((N, nc), dtype=np.int64)
    for x in range(N):
        Mcos[x, cos_of[x]] = 1
    AH, E = [], []
    for n in range(top + 1):
        s, s1 = sizes[n], sizes[n + 1]
        rows = []
        for w in gens[n]:
            w = w.reshape(s, N)
            for g in reps:
                perm = T[inv[g]]            # x -> g^-1 x
                rows.append((w[:, perm] @ Mcos).reshape(-1))
        AH.append(matrix(F, np.array(rows, dtype=np.int64)))
    for n in range(top + 2):
        s = sizes[n]
        Em = np.zeros((s * nc, s), dtype=np.int64)
        for j in range(s):
            Em[j * nc:(j + 1) * nc, j] = 1
        E.append(matrix(F, Em))
    for n in range(top + 1):
        assert AH[n] * E[n] == E[n + 1] * A[n]
    out = []
    for k in range(top + 1):
        hG = sizes[k] - (A[k - 1].rank() if k else 0) - A[k].rank()
        hH = sizes[k] * nc - (AH[k - 1].rank() if k else 0) - AH[k].rank()
        Z = A[k].right_kernel().basis_matrix().transpose()   # columns
        U = E[k] * Z
        if k:
            V = AH[k - 1]
            dU, dV = U.rank(), V.rank()
            dsum = U.augment(V).rank()
            inter = dU + dV - dsum
            ker = inter - A[k - 1].rank()
        else:
            ker = 0
        out.append((hG, hH, ker))
    return out


def nerve_homology(TG, ring, top):
    """Homology of the nerve NG (normalised chains: n-simplices
    (g_1, ..., g_n) with all g_i != 1), degrees 0..top."""
    N, one = TG.N, TG.one
    nonid = [g for g in range(N) if g != one]
    simp = {0: [()]}
    for n in range(1, top + 2):
        simp[n] = list(itertools.product(nonid, repeat=n))
    pos = {n: {s: i for i, s in enumerate(simp[n])} for n in simp}
    diffs = {}
    for n in range(1, top + 2):
        D = {}
        for j, s in enumerate(simp[n]):
            faces = [(0, s[1:])]
            for i in range(1, n):
                faces.append((i, s[:i - 1] + (TG.m(s[i - 1], s[i]),) +
                              s[i + 1:]))
            faces.append((n, s[:-1]))
            for i, f in faces:
                if one in f:
                    continue
                k = (pos[n - 1][f], j)
                D[k] = D.get(k, 0) + (-1) ** i
        diffs[n] = matrix(ring, len(simp[n - 1]), len(simp[n]), D, sparse=True)
    C = ChainComplex(diffs, degree=-1)
    return [C.homology(k) for k in range(top + 1)]


def section_2_2_and_2_4():
    """Sections 2.2 and 2.4: Eilenberg-Mac Lane spaces, joins, nerves."""
    # Integral homology of Z/m from the periodic resolution (Volume I, 3.5)
    def cyclic_homology(m, top):
        diffs = {k: matrix(ZZ, 1, 1, [0 if k % 2 else m])
                 for k in range(1, top + 2)}
        C = ChainComplex(diffs, degree=-1)
        return [tuple(C.homology(k).invariants()) for k in range(top + 1)]

    # p. 44: RP^infinity is a K(Z/2, 1): H_k(RP^n) = H_k(Z/2, Z) for k < n
    hz2 = cyclic_homology(2, 5)
    for n in (2, 3, 4):
        H = simplicial_complexes.RealProjectiveSpace(n).homology()
        for k in range(1, n):
            check(tuple(H[k].invariants()) == hz2[k],
                  'p. 32: H_%d(RP^%d) = H_%d(Z/2, Z)' % (k, n, k))
    # Exercise 1 of Section 2.4 (p. 59): the join of r copies of Z/2 is the
    # sphere S^(r-1) (boundary of the cross-polytope), the antipodal action is
    # free and the quotient has the homology of RP^(r-1).
    for r in range(2, 7):
        facets = [[(i, s[i]) for i in range(r)]
                  for s in itertools.product((1, -1), repeat=r)]
        X = SimplicialComplex(facets)
        H = X.homology()
        check(all(H[k].invariants() == () for k in range(r - 1)) and
              tuple(H[r - 1].invariants()) == (0,),
              'p. 41, Exercise 1: (Z/2)^{*%d} has the homology of S^%d'
              % (r, r - 1))
        # orbit complex: faces (I, signs) with first sign +1
        cells = {k: [] for k in range(r)}
        for k in range(r):
            for I in itertools.combinations(range(r), k + 1):
                for s in itertools.product((1, -1), repeat=k):
                    cells[k].append((I, (1,) + s))
        posc = {k: {c: i for i, c in enumerate(cells[k])} for k in cells}

        def norm(I, s):
            return (I, s) if s[0] == 1 else (I, tuple(-x for x in s))
        diffs = {}
        for k in range(1, r):
            D = {}
            for j, (I, s) in enumerate(cells[k]):
                for t in range(k + 1):
                    f = norm(I[:t] + I[t + 1:], s[:t] + s[t + 1:])
                    key = (posc[k - 1][f], j)
                    D[key] = D.get(key, 0) + (-1) ** t
            diffs[k] = matrix(ZZ, len(cells[k - 1]), len(cells[k]), D)
        Q = ChainComplex(diffs, degree=-1)
        got = [tuple(Q.homology(k).invariants()) for k in range(r)]
        want = [(0,)] + [((2,) if k % 2 else ()) for k in range(1, r - 1)]
        want.append((0,) if (r - 1) % 2 else ())
        check(got == want, 'p. 41, Exercise 1: (Z/2)^{*%d}/(Z/2) has the '
              'homology of RP^%d: %s' % (r, r - 1, got))
    # Exercise 2: the join of r circles has the homology of S^(2r-1)
    S1 = simplicial_complexes.Sphere(1)
    J = S1
    for r in (2, 3):
        J = J.join(S1, rename_vertices=True)
        H = J.homology()
        check(all(H[k].invariants() == () for k in range(2 * r - 1)) and
              tuple(H[2 * r - 1].invariants()) == (0,),
              'p. 41, Exercise 2: (S^1)^{*%d} has the homology of S^%d'
              % (r, 2 * r - 1))
    # Theorems 2.2.3 and 2.4.8 (iii): homology of the nerve NG (= BG, the
    # exercise on p. 61) against the algebraic Tor / Ext over F_p G and over
    # Z (periodic resolution).
    set_random_seed(0)
    cases = [('C2', 'CyclicGroup(IsPermGroup, 2)', 2, 5),
             ('C3', 'CyclicGroup(IsPermGroup, 3)', 3, 5),
             ('C4', 'CyclicGroup(IsPermGroup, 4)', 2, 4),
             ('V4', 'Group((1,2),(3,4))', 2, 4),
             ('S3', 'SymmetricGroup(3)', 2, 4),
             ('S3', 'SymmetricGroup(3)', 3, 4),
             ('D8', 'DihedralGroup(IsPermGroup, 8)', 2, 3),
             ('Q8', 'QuaternionGroup(IsPermGroup, 8)', 2, 3)]
    for name, src, p, top in cases:
        TG = TGroup(gap(src), name)
        hn = [H.dimension() for H in nerve_homology(TG, GF(p), top)]
        ext = free_resolution_cohomology(TG.mul, p, top)
        check(hn == ext, 'Theorems 2.2.3, 2.4.8 (iii): H_k(NG; F_%d) = '
              'Ext^k_{F_%d G}(F_%d, F_%d) in dual dimension for G = %s, '
              'k <= %d: %s' % (p, p, p, p, name, top, hn))
    for m in (2, 3, 4):
        TG = TGroup(gap('CyclicGroup(IsPermGroup, %d)' % m), 'C%d' % m)
        hn = [tuple(H.invariants()) for H in nerve_homology(TG, ZZ, 4)]
        check(hn == cyclic_homology(m, 4), 'Theorem 2.2.3: H_k(NG; Z) = '
              'H_k(Z/%d, Z) (periodic resolution), k <= 4' % m)
        B = simplicial_sets.ClassifyingSpace(
            groups.misc.MultiplicativeAbelian([m])).n_skeleton(5)
        Hs = B.homology(range(1, 5))
        check([tuple(Hs[k].invariants()) for k in range(1, 5)] == hn[1:],
              "Sage's ClassifyingSpace(C%d) agrees with our nerve" % m)
    # Exercise 3 of Section 2.4 (pp. 61-62): N C(G) / G = N G and N C(G)
    # is contractible (here: its normalised chains are acyclic in low
    # degrees), G = S3, C4.
    for src in ('SymmetricGroup(3)', 'CyclicGroup(IsPermGroup, 4)'):
        TG = TGroup(gap(src), src)
        N, inv, m = TG.N, TG.inv, TG.m

        def phi(x):  # arrows x_(i-1) -> x_i are left mult. by x_i x_(i-1)^-1
            return tuple(m(x[i], inv[x[i - 1]]) for i in range(1, len(x)))
        ok = True
        for n in range(1, 4):
            images = {}
            for x in itertools.product(range(N), repeat=n + 1):
                a = phi(x)
                for g in range(N):  # right action of G
                    ok &= phi(tuple(m(y, g) for y in x)) == a
                images[a] = images.get(a, 0) + 1
                for i in range(n + 1):
                    fx = phi(x[:i] + x[i + 1:])
                    if i == 0:
                        fa = a[1:]
                    elif i == n:
                        fa = a[:-1]
                    else:
                        fa = a[:i - 1] + (m(a[i], a[i - 1]),) + a[i + 1:]
                    ok &= fx == fa
            ok &= len(images) == N ** n and set(images.values()) == {N}
        check(ok, 'p. 43, Exercise 3: N C(G) / G = N G (faces, free right '
              'action, |G|^n orbits), %s, n <= 3' % src)
        # normalised chains of N C(G): consecutive entries distinct
        simp = {k: [x for x in itertools.product(range(N), repeat=k + 1)
                    if all(x[i] != x[i + 1] for i in range(k))]
                for k in range(0, 4)}
        pos = {k: {s: i for i, s in enumerate(simp[k])} for k in simp}
        diffs = {}
        for k in range(1, 4):
            D = {}
            for j, s in enumerate(simp[k]):
                for i in range(k + 1):
                    f = s[:i] + s[i + 1:]
                    if any(f[t] == f[t + 1] for t in range(len(f) - 1)):
                        continue
                    key = (pos[k - 1][f], j)
                    D[key] = D.get(key, 0) + (-1) ** i
            diffs[k] = matrix(ZZ, len(simp[k - 1]), len(simp[k]), D,
                              sparse=True)
        C = ChainComplex(diffs, degree=-1)
        H = [tuple(C.homology(k).invariants()) for k in range(3)]
        check(H == [(0,), (), ()], 'Lemma 2.4.7: N C(G) (Milnor E G) has '
              'H_0 = Z, H_1 = H_2 = 0 for %s' % src)


def section_2_5():
    """Section 2.5: the tables of p. 47 from the homotopy equivalences of p. 46."""
    Z, Z2, O = 'Z', 'Z/2', '0'
    # The chain of loop spaces of p. 46, beginning with BO x Z: each entry is
    # Omega of the previous one.  pi_0 of each space: BO x Z, BSp x Z: Z;
    # O: Z/2 (det); O/U = colim O(2n)/U(n): Z/2, since U(n) is connected and
    # lies in SO(2n) (realification has determinant |det|^2, checked below);
    # U/Sp, Sp, Sp/U, U/O: connected (U(2n), Sp(n), U(n) connected).
    real = [('BO x Z', Z), ('O', Z2), ('O/U', Z2), ('U/Sp', O),
            ('BSp x Z', Z), ('Sp', O), ('Sp/U', O), ('U/O', O)]
    complex_ = [('BU x Z', Z), ('U', O)]
    printed_ko = [Z, Z2, Z2, O, Z, O, O, O]   # p. 47, n = 0..7
    printed_k = [Z, O]                        # p. 47, n mod 2
    # KO~(S^n) = [S^n; BO x Z]_* = pi_0(Omega^n (BO x Z))
    for n in range(16):
        check(real[n % 8][1] == printed_ko[n % 8],
              'p. 47: KO~(S^%d) = pi_0(Omega^%d(BO x Z)) = %s'
              % (n, n, printed_ko[n % 8]))
        check(complex_[n % 2][1] == printed_k[n % 2],
              'p. 47: K~(S^%d) = %s' % (n, printed_k[n % 2]))
    # The printed heading K^(-n)(point) = K(S^n): the unreduced group is
    # K~(S^n) + Z (p. 45), so Z + Z for n even and Z for n odd.
    def plus_z(a):
        return {Z: 'Z+Z', Z2: 'Z/2+Z', O: Z}[a]
    for n in range(8):
        refuted(plus_z(printed_ko[n]) == printed_ko[n],
                'p. 47 printed: KO^(-%d)(point) = KO(S^%d) (unreduced)'
                % (n, n))
    for n in range(2):
        refuted(plus_z(printed_k[n]) == printed_k[n],
                'p. 47 printed: K^(-%d)(point) = K(S^%d) (unreduced)'
                % (n, n))
    # Omega O: pi_0(Omega O) = pi_1(O) = pi_2(BO x Z) = KO~(S^2) = Z/2 by the
    # table; the printed Omega O ~ O/U x Z/2 has 2 * 2 = 4 components.
    order = {Z2: 2, O: 1}
    check(order[real[2][1]] == order[printed_ko[2]],
          'p. 46: Omega O ~ O/U, pi_0 of order 2 = |KO~(S^2)|')
    refuted(order[real[2][1]] * 2 == order[printed_ko[2]],
            'p. 46 printed: Omega O ~ O/U x Z/2 (4 components, against '
            '|KO~(S^2)| = 2)')
    # the reading with the identity component SO/U (connected) would fit
    check(1 * 2 == order[printed_ko[2]],
          'p. 46: (SO/U) x Z/2 would have 2 components')
    # periodicity: the chains close after 8 and 2 steps (Omega^8 BO ~ BO x Z,
    # Omega^2 BU ~ BU x Z; Theorem 2.5.3)
    check(real[8 % 8][0] == 'BO x Z' and complex_[2 % 2][0] == 'BU x Z',
          'Theorem 2.5.3: Omega^8 BO ~ BO x Z and Omega^2 BU ~ BU x Z close '
          'the chains of p. 46')
    # U(n) in SO(2n): det [[A, -B], [B, A]] = det(A + iB) det(A - iB)
    K = QuadraticField(-1, 'i')
    i = K.gen()
    for n in (1, 2, 3):
        R = PolynomialRing(K, ['a%d%d' % (r, c) for r in range(n)
                               for c in range(n)] +
                           ['b%d%d' % (r, c) for r in range(n)
                            for c in range(n)])
        g = R.gens()
        A = matrix(R, n, n, g[:n * n])
        B = matrix(R, n, n, g[n * n:])
        Rl = matrix(R, 2 * n, 2 * n)
        Rl.set_block(0, 0, A)
        Rl.set_block(0, n, -B)
        Rl.set_block(n, 0, B)
        Rl.set_block(n, n, A)
        check(Rl.det() == (A + i * B).det() * (A - i * B).det(),
              'p. 46: realification of U(%d) has det |det|^2 >= 0, so '
              'U(%d) lies in SO(%d) and O(%d)/U(%d) has two components'
              % (n, n, 2 * n, 2 * n, n))


def section_2_6():
    """Section 2.6: invariants, Whitney sum, classes of small representations."""
    # p. 61: Z[x_1..x_n]^(Sigma_n) = Z[sigma_1..sigma_n]: in each degree d
    # the sigma-monomials and the orbit sums of monomials are related by a
    # unimodular matrix (so also over Z/2, p. 62).
    for n in range(1, 5):
        R = PolynomialRing(ZZ, 'x', n)
        x = R.gens()
        sig = [R(1)] + [sum(prod(c) for c in itertools.combinations(x, k))
                        for k in range(1, n + 1)]
        for d in range(1, 9):
            lams = [list(l) for l in Partitions(d, max_length=n)]
            mus = [list(l) for l in Partitions(d, max_part=n)]
            check(len(lams) == len(mus), 'p. 49: dimensions agree (n = %d, '
                  'd = %d)' % (n, d))
            rows = []
            for mu in mus:
                f = prod(sig[k] for k in mu)
                rows.append([f.monomial_coefficient(
                    prod(x[t] ** l[t] for t in range(len(l)))) for l in lams])
            Mt = matrix(ZZ, rows)
            check(abs(Mt.det()) == 1,
                  'p. 49: Z[x_1..x_%d]^Sigma = Z[sigma] in degree %d '
                  '(unimodular transition)' % (n, d))
    # Proposition 2.6.1 (ii): image of c in H*((CP^oo)^n) is prod (1 + x_i),
    # multiplicative under the Whitney sum BU(n) x BU(m) -> BU(n + m)
    for n in range(1, 4):
        for m_ in range(1, 4):
            R = PolynomialRing(ZZ, 'x', n + m_)
            x = R.gens()

            def sigma(k, xs):
                return sum(prod(c) for c in itertools.combinations(xs, k)) \
                    if k else R(1)
            ok = all(sigma(k, x) == sum(sigma(a, x[:n]) * sigma(k - a, x[n:])
                                        for a in range(k + 1))
                     for k in range(n + m_ + 1))
            check(ok, 'Proposition 2.6.1 (ii): Whitney sum formula for the '
                  'sigma_k, n = %d, m = %d' % (n, m_))
    # Chern classes of the regular representation of Z/m: H^*(Z/m, Z) is
    # Z[x]/(m x) with x in degree 2 (periodic resolution, Volume I 3.5), the
    # regular character is the sum of the m characters chi^a (GAP), and by
    # (ii), (iii) and naturality c(chi^a) = 1 + a x; so
    # c(regular) = prod_a (1 + a x) in (Z/m)[x] in positive degrees.
    for m_ in range(2, 14):
        G = gap('CyclicGroup(IsPermGroup, %d)' % m_)
        mults = gap('function(G) local t; t := CharacterTable(G); return '
                    'List(Irr(t), c -> ScalarProduct(t, c, '
                    'PermutationCharacter(G, TrivialSubgroup(G)))); end')(G)
        check(all(int(a) == 1 for a in mults) and len(mults) == m_,
              'Z/%d: the regular character is the sum of the %d linear '
              'characters' % (m_, m_))
        Rm = PolynomialRing(Zmod(m_), 'x')
        X = Rm.gen()
        c = prod(1 + a * X for a in range(m_))
        if ZZ(m_).is_prime():
            check(c == 1 - X ** (m_ - 1), 'c(regular rep of Z/%d) = '
                  '1 - x^%d' % (m_, m_ - 1))
        else:
            check(c[1] == ZZ(m_ * (m_ - 1) // 2) % m_,
                  'c_1(regular rep of Z/%d) = m(m-1)/2 . x' % m_)
    # H^*((Z/2)^n; F_2) = F_2[x_1..x_n] (Kuenneth, p. 62): dimensions from a
    # free resolution
    set_random_seed(0)
    for n, src in ((1, 'Group((1,2))'), (2, 'Group((1,2),(3,4))'),
                   (3, 'Group((1,2),(3,4),(5,6))')):
        T = TGroup(gap(src), src).mul
        top = 5 if n < 3 else 4
        dims = free_resolution_cohomology(T, 2, top)
        check(dims == [binomial(k + n - 1, n - 1) for k in range(top + 1)],
              'p. 50: H^k((Z/2)^%d; F_2) has dimension binom(k + %d, %d), '
              'k <= %d' % (n, n - 1, n - 1, top))
    # Stiefel-Whitney classes of real representations of E = (Z/2)^n: a real
    # representation is a sum of characters E -> {+-1}, i.e. of linear forms
    # l in H^1(E; F_2) = Hom(E, F_2), and w(L_l) = 1 + l (Proposition 2.6.2
    # (ii), (iii) and naturality).
    for n in (1, 2, 3, 4):
        R = PolynomialRing(GF(2), ['x%d' % i for i in range(n)] + ['X'])
        x, X = R.gens()[:n], R.gens()[n]
        forms = [sum(c * xi for c, xi in zip(v, x))
                 for v in itertools.product((0, 1), repeat=n)]
        P = prod(X + l for l in forms)
        dick = {e: P.coefficient({X: e}) for e in range(2 ** n + 1)}
        check(all(dick[e] == 0 for e in dick
                  if e not in [2 ** i for i in range(n + 1)]),
              'Dickson: prod_l (X + l) has only the powers X^(2^i), n = %d' % n)
        w = prod(1 + l for l in forms)
        dicksum = 1 + sum(dick[2 ** i] for i in range(n))
        check(w == dicksum, 'w(regular representation of (Z/2)^%d) = '
              '1 + sum of the Dickson invariants' % n)
        # invariance under GL_n(F_2)
        if n <= 3:
            ok = True
            for Mv in itertools.product((0, 1), repeat=n * n):
                Mm = matrix(GF(2), n, n, Mv)
                if Mm.det() == 0:
                    continue
                sub = {x[i]: sum(Mm[i, j] * x[j] for j in range(n))
                       for i in range(n)}
                ok &= w.subs(sub) == w
            check(ok, 'w(regular rep of (Z/2)^%d) is GL_%d(F_2)-invariant'
                  % (n, n))
        if n == 2:
            a, b = x
            check(w == 1 + (a ** 2 + a * b + b ** 2) + (a ** 2 * b + a * b ** 2),
                  'w(regular rep of V_4) = 1 + (x^2 + xy + y^2) + '
                  '(x^2 y + x y^2), w_1 = 0')
    # The permutation representation of S_4 restricted to elementary abelian
    # subgroups: decomposition into characters by GAP, w as product, w_1 =
    # class of det = sign.
    S4 = gap('SymmetricGroup(4)')
    for gens in ('[(1,2)(3,4), (1,3)(2,4)]', '[(1,2), (3,4)]'):
        E = gap('Group(%s)' % gens)
        egens = list(E.GeneratorsOfGroup())
        n = len(egens)
        R = PolynomialRing(GF(2), 'x', n)
        x = R.gens()
        # character of the permutation action on {1..4}
        elts = list(E.AsSSortedList())
        w = R(1)
        w1 = R(0)
        for v in itertools.product((0, 1), repeat=n):
            # character chi_v(g) = (-1)^{v . coords(g)}; multiplicity in the
            # permutation module = <chi_v, perm>
            tot = 0
            for g in elts:
                coords = None
                for c in itertools.product((0, 1), repeat=n):
                    h = prod([egens[t] ** c[t] for t in range(n)],
                             E.Identity())
                    if h == g:
                        coords = c
                        break
                sign = (-1) ** sum(a * b for a, b in zip(v, coords))
                fixed = sum(1 for p in range(1, 5) if
                            libgap.OnPoints(p, g) == p)
                tot += sign * fixed
            mult = tot // len(elts)
            l = sum(a * xi for a, xi in zip(v, x))
            w *= (1 + l) ** mult
            w1 += mult * l
        sgn = sum(xi for xi, g in zip(x, egens) if g.SignPerm() == -1)
        check(w1 == sgn, 'w_1 of the permutation representation of S_4 on '
              '%s is the class of the sign (det)' % gens)
        if gens.startswith('[(1,2)(3,4)'):
            a, b = x
            check(w == 1 + (a ** 2 + a * b + b ** 2) + (a ** 2 * b + a * b ** 2),
                  'the natural representation of S_4 restricted to the '
                  'normal V_4 is regular: same w')
        else:
            check(w == (1 + x[0]) * (1 + x[1]), 'the natural representation '
                  'of S_4 restricted to <(1,2),(3,4)>: w = (1 + x)(1 + y)')


def subgroups_of(TG):
    subs = gap('function(G, e) return List(AllSubgroups(G), H -> '
               'List(AsSSortedList(H), h -> PositionSorted(e, h))); end')(
        TG.G, TG.elts)
    return [tuple(sorted(int(i) - 1 for i in H)) for H in subs]


def homs(TH, H, TG):
    """All homomorphisms from the subgroup H (element indices of TH) to TG,
    as dicts."""
    Hg = gap('function(G, e, l) return Subgroup(G, List(l, i -> e[i])); end')(
        TH.G, TH.elts, [i + 1 for i in H])
    res = gap('function(H, G, e, f) return List(AllHomomorphisms(H, G), '
              'phi -> List(e, h -> PositionSorted(f, Image(phi, h)))); end')(
        Hg, TG.G, [TH.elts[i] for i in H], TG.elts)
    return [{h: int(v) - 1 for h, v in zip(H, img)} for img in res]


class DoubleBurnside:
    """Basis zeta_(H', phi) of b(G', G): pairs up to G' x G conjugacy."""

    def __init__(self, TGp, TG):
        self.Gp, self.G = TGp, TG
        self.pairs = []
        seen = set()
        for H in subgroups_of(TGp):
            for phi in homs(TGp, H, TG):
                key = self.key(H, phi)
                if key not in seen:
                    seen.add(key)
                    self.pairs.append((H, phi))
        self.keys = [self.key(H, phi) for H, phi in self.pairs]

    def key(self, H, phi):
        Gp, G = self.Gp, self.G
        best = None
        for a in range(Gp.N):
            for b in range(G.N):
                D = tuple(sorted((Gp.m(Gp.m(a, h), Gp.inv[a]),
                                  G.m(G.m(b, phi[h]), G.inv[b])) for h in H))
                if best is None or D < best:
                    best = D
        return best


def compose_formula(Bpp, Bp, X, Y):
    """The boxed formula p. 71: zeta_(H', phi) o zeta_(H'', phi') as a dict
    {key: multiplicity} in b(G'', G).  X = (H', phi) in b(G', G),
    Y = (H'', phi') in b(G'', G')."""
    (Hp, phi), (Hpp, phip) = X, Y
    Gp = Bp.Gp  # G'
    Kp = sorted({phip[h] for h in Hpp})
    Hpset = set(Hp)
    # double cosets K' x H'
    seen, reps = set(), []
    for x in range(Gp.N):
        if x in seen:
            continue
        reps.append(x)
        seen |= {Gp.m(Gp.m(k, x), h) for k in Kp for h in Hp}
    out = {}
    for x in reps:
        xinv = Gp.inv[x]
        conjH = {Gp.m(Gp.m(x, h), xinv) for h in Hp}   # ^x H'
        L = [h for h in Hpp if phip[h] in conjH]       # phi'^-1(K' n ^xH')
        psi = {h: phi[Gp.m(Gp.m(xinv, phip[h]), x)] for h in L}
        assert all(Gp.m(Gp.m(xinv, phip[h]), x) in Hpset for h in L)
        k = Bpp.key(L, psi)
        out[k] = out.get(k, 0) + 1
    return out


def compose_bisets(Bpp, X, Y, TGpp, TGp, TG):
    """Y x_(G') X for Y = G'' x_(H'') G', X = G' x_(H') G, decomposed into
    transitive G'' x G-sets; returns {key: multiplicity} and whether every
    stabiliser meets 1 x G trivially."""
    (Hp, phi), (Hpp, phip) = X, Y
    A, B, C = TGpp.N, TGp.N, TG.N
    idx = lambda a, b, c: (a * B + b) * C + c
    parent = list(range(A * B * C))

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u, v = find(u), find(v)
        if u != v:
            parent[u] = v
    for a in range(A):
        for b in range(B):
            for c in range(C):
                for h in Hpp:   # (a h, b, c) ~ (a, phi'(h) b, c)
                    union(idx(TGpp.m(a, h), b, c), idx(a, TGp.m(phip[h], b), c))
                for h in Hp:    # (a, b h, c) ~ (a, b, phi(h) c)
                    union(idx(a, TGp.m(b, h), c), idx(a, b, TG.m(phi[h], c)))
    cls = {}
    for u in range(A * B * C):
        cls.setdefault(find(u), []).append(u)
    points = list(cls)
    rep_of = {u: find(u) for u in range(A * B * C)}

    def act(g, k, p):  # (g, k) . [a, b, c] = [g a, b, c k^-1]
        u = p
        a, rest = divmod(u, B * C)
        b, c = divmod(rest, C)
        return rep_of[idx(TGpp.m(g, a), b, TG.m(c, TG.inv[k]))]
    out, free = {}, True
    remaining = set(points)
    while remaining:
        p = remaining.pop()
        orbit = {act(g, k, p) for g in range(A) for k in range(C)}
        remaining -= orbit
        stab = [(g, k) for g in range(A) for k in range(C) if act(g, k, p) == p]
        if any(g == TGpp.one and k != TG.one for g, k in stab):
            free = False
        L = sorted({g for g, k in stab})
        psi = {g: k for g, k in stab}
        key = Bpp.key(L, psi)
        out[key] = out.get(key, 0) + 1
    return out, free, len(points)


def section_2_8():
    """Section 2.8: Burnside rings, tables of marks, double Burnside rings."""
    # Tables of marks (Section 5.4 of Volume I): GAP against direct counts
    for src in ('CyclicGroup(IsPermGroup, 2)', 'CyclicGroup(IsPermGroup, 4)',
                'Group((1,2),(3,4))', 'SymmetricGroup(3)',
                'DihedralGroup(IsPermGroup, 8)',
                'QuaternionGroup(IsPermGroup, 8)', 'AlternatingGroup(4)',
                'SymmetricGroup(4)'):
        G = gap(src)
        tom = G.TableOfMarks()
        M = [[int(a) for a in row] for row in tom.MatTom()]
        reps = [tom.RepresentativeTom(i + 1) for i in range(len(M))]
        ok = True
        for i, H in enumerate(reps):
            T = G.RightTransversal(H)
            for j, K in enumerate(reps):
                gens = K.GeneratorsOfGroup()
                fixed = sum(1 for t in T
                            if all(t * k * t ** -1 in H for k in gens))
                ok &= fixed == M[i][j]
        check(ok, 'table of marks of %s: GAP = fixed points of H_j on G/H_i'
              % src)
        # b(G): products of transitive G-sets have non-negative integral
        # coordinates; the augmentation ideal has rank #classes - 1
        Mm = matrix(QQ, M)
        okp = True
        for i in range(len(M)):
            for j in range(len(M)):
                prodmarks = vector(QQ, [M[i][k] * M[j][k]
                                        for k in range(len(M))])
                coords = Mm.solve_left(prodmarks)
                okp &= all(c in ZZ and c >= 0 for c in coords)
        check(okp, 'b(%s): [G/H_i][G/H_j] is a sum of transitive G-sets'
              % src)
        aug = vector(ZZ, [M[i][0] for i in range(len(M))])
        I = matrix(ZZ, [aug]).right_kernel()
        check(I.rank() == len(M) - 1, 'b(%s): I_G has rank %d' %
              (src, len(M) - 1))
    # b(C_p): I = Z x with x = [C_p/1] - p, x^2 = -p x, so I^n = p^(n-1) I
    # and b(C_p)^ = Z + Z_p (the completion in the Segal conjecture)
    for p in (2, 3, 5, 7):
        R = PolynomialRing(ZZ, 'u')
        u = R.gen()       # u = [C_p/1], u^2 = p u
        x = u - p
        x2 = (x * x).quo_rem(u ** 2 - p * u)[1]
        check(x2 == -p * x, 'b(C_%d): x^2 = -%d x for x = [C_p/1] - p'
              % (p, p))
    # Double Burnside rings: the boxed formula of p. 71 against the
    # composition of bisets G'' x_(H'') G' x_(H') G, and the description of
    # p. 71 (G-free G' x G-sets <-> pairs (H', phi))
    names = {'C2': 'CyclicGroup(IsPermGroup, 2)',
             'C3': 'CyclicGroup(IsPermGroup, 3)',
             'S3': 'SymmetricGroup(3)'}
    TGs = {k: TGroup(gap(v), k) for k, v in names.items()}
    Bs = {}
    for a in TGs:
        for b in TGs:
            Bs[a, b] = DoubleBurnside(TGs[a], TGs[b])
    for a in TGs:
        for b in TGs:
            # number of classes of subgroups L of G' x G with L n (1 x G) = 1
            n_free = gap('function(A, B) local D, e; D := DirectProduct(A, '
                         'B); e := Embedding(D, 2); return Number('
                         'ConjugacyClassesSubgroups(D), c -> Size(Intersection('
                         'Representative(c), Image(e))) = 1); end')(
                TGs[a].G, TGs[b].G)
            check(int(n_free) == len(Bs[a, b].pairs),
                  'p. 59: G-free transitive %s x %s-sets <-> classes of '
                  'pairs (H\', phi): %d' % (a, b, len(Bs[a, b].pairs)))
    total = 0
    for gpp in TGs:
        for gp in TGs:
            for g in TGs:
                Bpp, Bp_, Bx = Bs[gpp, g], Bs[gpp, gp], Bs[gp, g]
                ok, okfree = True, True
                for X in Bx.pairs:
                    for Y in Bp_.pairs:
                        f = compose_formula(Bpp, Bx, X, Y)
                        bis, free, npts = compose_bisets(
                            Bpp, X, Y, TGs[gpp], TGs[gp], TGs[g])
                        ok &= f == bis
                        okfree &= free
                        total += 1
                check(ok and okfree, 'p. 59 boxed formula = composition of '
                      'bisets, G\'\' = %s, G\' = %s, G = %s (%d x %d pairs)'
                      % (gpp, gp, g, len(Bp_.pairs), len(Bx.pairs)))
    # b(G, G) is a ring: associativity and the identity zeta_(G, id)
    for gname in TGs:
        B = Bs[gname, gname]
        TG = TGs[gname]
        full = tuple(range(TG.N))
        ident = B.key(full, {h: h for h in full})
        bypos = {k: i for i, k in enumerate(B.keys)}

        def mult(u, v):   # u in b(G, G) as {key: n}; returns u o v
            out = {}
            for ku, nu in u.items():
                for kv, nv in v.items():
                    X = B.pairs[bypos[ku]]
                    Y = B.pairs[bypos[kv]]
                    for k, n in compose_formula(B, B, X, Y).items():
                        out[k] = out.get(k, 0) + nu * nv * n
            return out
        ok = True
        for k in B.keys:
            ok &= mult({k: 1}, {ident: 1}) == {k: 1} == mult({ident: 1},
                                                              {k: 1})
        for k1 in B.keys:
            for k2 in B.keys:
                for k3 in B.keys:
                    ok &= mult(mult({k1: 1}, {k2: 1}), {k3: 1}) == \
                        mult({k1: 1}, mult({k2: 1}, {k3: 1}))
        check(ok, 'p. 59: b(%s, %s) (rank %d) is associative with identity '
              'zeta_(G, id)' % (gname, gname, len(B.keys)))
    return total


def prime_powers(bound):
    return [q for q in range(2, bound + 1) if ZZ(q).is_prime_power()]


def series(num_den, top):
    """Coefficients up to t^top of a product of (1 + t^a)/(1 - t^b)."""
    R = PolynomialRing(ZZ, 't')
    t = R.gen()
    f = R(1)
    for a, b in num_den:
        f = (f * (1 + t ** a)).truncate(top + 1)
        inv = sum(t ** (b * k) for k in range(top // b + 1))
        f = (f * inv).truncate(top + 1)
    return [f[k] for k in range(top + 1)]


def invariant_series(degrees, m, signs, top):
    """dim of the Sigma_m-invariants of W^(x m), W with a homogeneous basis of
    the given degrees, Sigma_m permuting tensor factors (with the Koszul sign
    if signs, i.e. l odd; without if l = 2): coefficient of u^m in
    prod_even 1/(1 - u t^d) prod_odd (1 + u t^d) (signs) or prod 1/(1 - u t^d)."""
    R = PolynomialRing(ZZ, ['u', 't'])
    u, t = R.gens()

    def trunc(f):
        return sum(c * mon for c, mon in zip(f.coefficients(), f.monomials())
                   if mon.degree(u) <= m and mon.degree(t) <= top)
    f = R(1)
    for d in degrees:
        if d > top:
            continue
        if signs and d % 2:
            f = trunc(f * (1 + u * t ** d))
        else:
            f = trunc(f * sum((u * t ** d) ** k for k in range(m + 1)))
    return [f.coefficient({u: m, t: k}) for k in range(top + 1)]


def section_2_9_2_10():
    """Sections 2.9, 2.10: F psi^q, Quillen's theorem, K-groups of F_q."""
    # pp. 64, 71: pi_(2j-1)(F psi^q) = coker(1 - q^j on Z) = Z/(q^j - 1),
    # pi_(2j)(F psi^q) = ker = 0 (pi_odd(BU) = 0); K_(2j-1)(F_q) the same.
    ok, okp, ref = True, True, True
    for q in prime_powers(64):
        p = ZZ(q).prime_factors()[0]
        for j in range(1, 9):
            mult = 1 - q ** j      # 1 - psi^q on pi_(2j)(BU) = Z
            ok &= abs(mult) == q ** j - 1 and mult != 0
            okp &= gcd(q ** j - 1, p) == 1
            ref &= q ** (2 * j) - 1 != q ** j - 1
    check(ok, 'p. 64: pi_(2j-1)(F psi^q) = Z/(q^j - 1), pi_(2j) = 0, q <= 64 '
          'prime powers, j <= 8')
    check(okp, 'p. 64: no p-torsion in pi_*(F psi^q)')
    refuted(not ref, 'pp. 64, 71 printed: Z/(q^(2j) - 1) (differs from the '
            'cokernel of 1 - q^j for every q, j)')
    # j = 1: K_1(F_q) = GL(F_q)/E(F_q) = F_q^x of order q - 1 (Proposition
    # 2.10.4 (i)); E_n(F_q) = SL_n(F_q) = [GL_n, GL_n] (n >= 3, or n = 2 and
    # q >= 3), perfect for n >= 3
    for n, q in ((2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (2, 7), (2, 8),
                 (2, 9), (3, 4)):
        G = libgap.GL(n, q)
        F = libgap.GF(q)
        one = F.One()
        elem = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    for a in F.AsList():
                        if a != F.Zero():
                            M = libgap.IdentityMat(n, F)
                            M = [list(r) for r in M]
                            M[i][j] = a
                            elem.append(libgap(M))
        E = libgap.Group(elem)
        check(int(E.Size()) == int(libgap.SL(n, q).Size()) and
              int(G.Size()) // int(E.Size()) == q - 1,
              'Prop 2.10.4 (i): GL_%d(F_%d)/E_%d(F_%d) has order q - 1 = %d '
              '(not q^2 - 1)' % (n, q, n, q, q - 1))
        check(E == G.DerivedSubgroup() or (n == 2 and q == 2),
              'p. 70: E_%d(F_%d) is the commutator subgroup' % (n, q))
        if n >= 3 or q >= 4:
            check(E.IsPerfectGroup(), 'p. 70: E_%d(F_%d) is perfect' % (n, q))
        check(G.FactorGroup(E).IsCyclic(),
              'K_1: GL_%d(F_%d)/E is cyclic (= F_q^x via det)' % (n, q))
    # The three identities of p. 72 for 2 x 2 blocks: symbolically over the
    # fraction field, and for all A, B in GL_2(F_3)
    R = PolynomialRing(QQ, ['a%d' % k for k in range(4)] +
                       ['b%d' % k for k in range(4)]).fraction_field()
    g = R.gens()
    for blocks in (2,):
        A = matrix(R, 2, 2, g[:4])
        B = matrix(R, 2, 2, g[4:])
        I2, Z2 = matrix.identity(R, 2), matrix(R, 2, 2)

        def blk(a, b, c, d):
            return matrix.block([[a, b], [c, d]])
        lhs1 = blk(A * B * A.inverse() * B.inverse(), Z2, Z2, I2)
        rhs1 = blk(A, Z2, Z2, A.inverse()) * blk(B, Z2, Z2, B.inverse()) * \
            blk((B * A).inverse(), Z2, Z2, B * A)
        check(lhs1 == rhs1, 'p. 70: first identity (commutator), generic')
        lhs2 = blk(A, Z2, Z2, A.inverse())
        rhs2 = blk(I2, A, Z2, I2) * blk(I2, Z2, -A.inverse(), I2) * \
            blk(I2, A, Z2, I2) * blk(Z2, -I2, I2, Z2)
        check(lhs2 == rhs2, 'p. 70: second identity, generic')
        lhs3 = blk(Z2, -I2, I2, Z2)
        rhs3 = blk(I2, Z2, I2, I2) * blk(I2, -I2, Z2, I2) * blk(I2, Z2, I2, I2)
        check(lhs3 == rhs3, 'p. 70: third identity')
    # H_2(E(F_q), Z) = K_2(F_q) = 0 (Theorem 2.10.3, Proposition 2.10.4
    # (ii)): Schur multipliers of SL_n(F_q) in small cases inside the stable
    # range (SL_3(F_2) and SL_2(F_4) are the known unstable exceptions)
    for n, q in ((3, 3), (2, 5), (2, 7), (2, 8)):
        check(list(libgap.AbelianInvariantsMultiplier(libgap.SL(n, q))) == [],
              'H_2(SL_%d(F_%d), Z) = 0' % (n, q))

    # H^*(F psi^q; F_l): F_l[c_1, c_2, ...]/((q^k - 1) c_k) = F_l[c_r, c_2r,..]
    ok = True
    for q in prime_powers(32):
        for l in (2, 3, 5, 7, 11, 13):
            if q % l == 0:
                continue
            r = Zmod(l)(q).multiplicative_order()
            ok &= all(((q ** k - 1) % l == 0) == (k % r == 0)
                      for k in range(1, 40))
    check(ok, 'p. 64: (q^k - 1) c_k = 0 in F_l exactly for r | k')

    # Lemma 2.9.2: index of Sigma_m wr GL_r(F_q) in GL_n(F_q) prime to l
    # (l odd); for l = 2 the index of Sigma_[n/2] wr GL_2(F_q) x
    # (F_q^x)^(n - 2[n/2]) is odd and that of Sigma_n wr GL_1 is even.
    def gl_order(n, q):
        return prod(q ** n - q ** i for i in range(n))
    ok_odd, ok2, ok2wr = True, True, True
    odd_typical = []
    for q in prime_powers(27):
        for l in (3, 5, 7, 11, 13):
            if q % l == 0:
                continue
            r = Zmod(l)(q).multiplicative_order()
            for n in range(1, 13):
                m_, e = divmod(n, r)
                sub = factorial(m_) * gl_order(r, q) ** m_
                ok_odd &= valuation(gl_order(n, q), l) == valuation(sub, l)
        if q % 2:
            for n in range(1, 13):
                h = n // 2
                sub = factorial(h) * gl_order(2, q) ** h * \
                    (q - 1) ** (n - 2 * h)
                ok2 &= (gl_order(n, q) // sub) % 2 == 1
                if n >= 2:
                    idx = gl_order(n, q) // (factorial(n) * (q - 1) ** n)
                    if q % 4 == 3:
                        ok2wr &= idx % 2 == 0
                    else:
                        odd_typical.append((n, q, idx % 2 == 1))
    check(ok_odd, 'Lemma 2.9.2: |GL_n(F_q) : Sigma_m wr GL_r(F_q)| prime to '
          'odd l (q <= 27, n <= 12, l <= 13)')
    check(ok2, 'Lemma 2.9.2, l = 2: Sigma_[n/2] wr GL_2(F_q) x '
          '(F_q^x)^(n-2[n/2]) has odd index (q odd <= 27, n <= 12)')
    check(ok2wr, 'Lemma 2.9.2, l = 2, q = 3 mod 4: Sigma_n wr GL_1(F_q) has '
          'even index (n >= 2)')
    check(all(o for _, _, o in odd_typical), 'Lemma 2.9.2, l = 2, q = 1 mod 4: '
          'Sigma_n wr GL_1(F_q) has odd index (n <= 12, q <= 27)')
    refuted(not any(o for _, _, o in odd_typical), 'p. 66 printed: "If l = 2 '
            '... the index of this wreath product is not odd" (GL_2(F_5): '
            'index 480/32 = 15)')

    # Theorem 2.9.3 and Lemma 2.9.2: from one free F_l GL_n(F_q)-resolution,
    # dim H^k(GL_n(F_q), F_l) and the kernel of the restriction to C^m (C
    # cyclic of order q^r - 1: the diagonal torus if r = 1, a cyclic subgroup
    # of order q^r - 1 if n = r).  Against (a) the Poincare series of
    # F_l[c_jr] (x) Lambda(e_jr), j <= m (additively the same for either form
    # of the exceptional relation), and (b) the series of
    # (( (x)^m H^*(C, F_l)^(Z/r) ))^(Sigma_m): the restriction is injective
    # in every case; it is onto the invariants for l odd (and m = 1), not for
    # l = 2, m >= 2 (corrected Theorem 2.9.3: injective, an isomorphism if l
    # is odd).
    set_random_seed(0)
    cases = [(1, 3, 2, 6), (1, 7, 3, 6), (2, 2, 3, 8), (2, 3, 2, 8),
             (2, 5, 2, 4), (2, 7, 2, 2), (2, 5, 3, 5), (2, 4, 3, 5),
             (2, 4, 5, 5), (3, 2, 3, 6), (3, 2, 7, 7)]
    for n, q, l, top in cases:
        r = Zmod(l)(q).multiplicative_order()
        m_, e = divmod(n, r)
        TGl = TGroup(libgap.GL(n, q), 'GL')
        if r == 1:
            C = [i for i, g in enumerate(TGl.elts) if g.IsDiagonalMat()]
        else:
            assert n == r and e == 0 or (n, q, l) == (3, 2, 3)
            o = q ** r - 1
            g0 = [i for i, g in enumerate(TGl.elts) if int(g.Order()) == o][0]
            C = TGl.subgroup([g0])
        data = restriction_data(TGl.mul, TGl.inv, l, top, C)
        dims = [hG for hG, hC, ker in data]
        check(all(ker == 0 for hG, hC, ker in data),
              'Lemma 2.9.2: H^k(GL_%d(F_%d), F_%d) -> H^k(C^%d) is injective, '
              'k <= %d (|C^m| = %d)' % (n, q, l, m_, top, len(C)))
        quillen = series([(2 * j * r - 1, 2 * j * r)
                          for j in range(1, m_ + 1)], top)
        check(dims == quillen, 'Theorem 2.9.3: dim H^k(GL_%d(F_%d), F_%d) = '
              'Poincare series of F[c_jr] (x) Lambda(e_jr), k <= %d: %s'
              % (n, q, l, top, dims))
        Csize = q ** r - 1
        if l == 2 and Csize % 4 == 2:     # H^*(C) = F_2[x], exceptional
            basis = list(range(0, top + 1))
        else:                             # Lambda(x) (x) F_l[y], Z/r-fixed
            basis = [2 * k for k in range(top + 1) if k % r == 0] + \
                    [2 * k + 1 for k in range(top + 1) if (k + 1) % r == 0]
        inv = invariant_series(basis, m_, l != 2, top)
        if l != 2 or m_ <= 1:
            check(inv == dims, 'Theorem 2.9.3 (corrected): H^*(GL_%d(F_%d), '
                  'F_%d) -> invariants of Sigma_%d wr Z/%d on H^*(C^%d) is an '
                  'isomorphism, k <= %d' % (n, q, l, m_, r, m_, top))
        else:
            refuted(inv == dims, 'Theorem 2.9.3 printed for l = 2: '
                    'H^*(GL_%d(F_%d), F_2) = (H^*(C)^(x %d))^Sigma_%d '
                    '(invariants %s, cohomology %s)'
                    % (n, q, m_, m_, inv, dims))
    # GL_3(F_3): the block subgroup GL_2(F_3) x GL_1(F_3) has odd index 117,
    # so H^*(GL_3(F_3), F_2) injects into its cohomology (Volume I,
    # Corollary 3.6.18), which injects into that of the diagonal (Z/2)^3
    H0 = gap('function() local F, gens; F := GF(3); gens := List('
             'GeneratorsOfGroup(GL(2, 3)), g -> [[g[1][1], g[1][2], 0], '
             '[g[2][1], g[2][2], 0], [0, 0, 1]] * One(F)); Add(gens, [[1, 0, 0], '
             '[0, 1, 0], [0, 0, -1]] * One(F)); return Group(gens); end')()
    TH = TGroup(H0, 'GL2xGL1')
    check(int(libgap.GL(3, 3).Size()) // TH.N == 117,
          'GL_2(F_3) x GL_1(F_3) has index 117 in GL_3(F_3)')
    D = [i for i, g in enumerate(TH.elts) if g.IsDiagonalMat()]
    data = restriction_data(TH.mul, TH.inv, 2, 4, D)
    check(all(ker == 0 for _, _, ker in data), 'Lemma 2.9.2 for GL_3(F_3), '
          'l = 2: H^*(GL_2(F_3) x GL_1(F_3), F_2) -> H^*((Z/2)^3) injective, '
          'k <= 4')
    # GL_2(F_5), l = 2 (typical): H^*(C^2) = Lambda(x_1, x_2) (x) F_2[y_1, y_2]
    # with c_j -> sigma_j(y), e_j -> sum_i x_i sigma_(j-1)(y_k, k != i); the
    # subring they generate has the dimensions 1, 1, 1, 2, 3 of
    # H^*(GL_2(F_5), F_2): the image of the restriction is this subring,
    # not the invariants
    R = PolynomialRing(GF(2), ['x1', 'x2', 'y1', 'y2'])
    x1, x2, y1, y2 = R.gens()
    Iq = R.ideal([x1 ** 2, x2 ** 2])
    wdeg = {x1: 1, x2: 1, y1: 2, y2: 2}

    def deg(mon):
        return sum(wdeg[v] * mon.degree(v) for v in (x1, x2, y1, y2))
    gensr = [(x1 + x2, 1), (y1 + y2, 2), (x1 * y2 + x2 * y1, 3), (y1 * y2, 4)]
    span = {0: [R(1)]}
    for dd in range(1, 5):
        polys = [Iq.reduce(gp * f) for gp, gd in gensr if gd <= dd
                 for f in span[dd - gd]]
        polys = [f for f in polys if f != 0]
        mons = sorted({mm for f in polys for mm in f.monomials()})
        if polys:
            Mx = matrix(GF(2), [[f.monomial_coefficient(mm) for mm in mons]
                                for f in polys])
            span[dd] = [sum(v[i] * mons[i] for i in range(len(mons)))
                        for v in Mx.row_space().basis()]
        else:
            span[dd] = []
    check([len(span[dd]) for dd in range(5)] == [1, 1, 1, 2, 3],
          'GL_2(F_5), l = 2: the c_j, e_j generate a subring of H^*((Z/4)^2, '
          'F_2) with the dimensions of H^*(GL_2(F_5), F_2), k <= 4')

    # The exceptional relation (p. 67, Theorem 2.9.3).  GL_1(F_3) = Z/2,
    # H^*(Z/2, F_2) = F_2[x]; the theorem makes e_1 (degree 1) and c_1
    # (degree 2) generators, so e_1 = x, c_1 = x^2 (c_1 != 0, p. 66).
    Rx = PolynomialRing(GF(2), 'x')
    x = Rx.gen()
    c = {0: Rx(1), 1: x ** 2}
    e1 = x
    printed = sum(c.get(a, 0) * c.get(2 * 1 - 1 - a, 0) for a in range(0, 2))
    corrected = sum(c.get(a, 0) * c.get(2 * 1 - 1 - a, 0) for a in range(0, 1))
    refuted(e1 ** 2 == printed, 'p. 67, Theorem 2.9.3 printed: e_1^2 = '
            'sum_(a=0)^1 c_a c_(1-a) = 2 c_1 = 0 in H^*(GL_1(F_3), F_2)')
    check(e1 ** 2 == corrected, 'corrected: e_1^2 = c_0 c_1 = c_1 = x^2')
    # For every n and q = 3 mod 4: H^1(GL_n(F_q), F_2) = Hom(GL_n, Z/2) is
    # spanned by e_1 (the only generator of degree 1) and e_1^2 = Bockstein
    # of e_1 is non-zero, since no homomorphism GL_n(F_q) -> Z/4 reduces to
    # e_1 (the abelianisation is F_q^x, of order 2 mod 4); the printed
    # relation gives e_1^2 = 0.  For q = 1 mod 4, e_1 lifts and e_1^2 = 0.
    for n, q in ((1, 3), (2, 3), (3, 3), (1, 7), (2, 7), (1, 11), (2, 11),
                 (1, 5), (2, 5), (3, 5), (1, 9), (2, 9), (1, 13)):
        ab = [int(a) for a in libgap.GL(n, q).AbelianInvariants()]
        two = [a for a in ab if a % 2 == 0]
        h1 = len(two)                                 # dim Hom(G, Z/2)
        lift = sum(1 for a in two if a % 4 == 0)      # classes lifting to Z/4
        if q % 4 == 3:
            check(h1 == 1 and lift == 0, 'GL_%d(F_%d): H^1 = <e_1> and '
                  'e_1^2 != 0 (exceptional case), against the printed '
                  'relation' % (n, q))
        else:
            check(h1 == 1 and lift == 1, 'GL_%d(F_%d): e_1^2 = 0 (typical '
                  'case)' % (n, q))
    # Restriction to C^n = (Z/2)^n in the exceptional case, with the
    # restrictions c_j -> sigma_j(x_1^2, ..., x_n^2) (Whitney sum, c_1 of a
    # line = x^2) and e_j -> sum_i x_i sigma_(j-1)(x_k^2, k != i) (e_j
    # primitive for the H-space structure of F psi^q, following Quillen;
    # e_1 -> sum x_i is the class of det): the corrected relation
    # e_j^2 = sum_(a=0)^(j-1) c_a c_(2j-1-a) holds for all j <= n <= 6, the
    # printed one fails for every j.
    for n in range(1, 7):
        R = PolynomialRing(GF(2), 'x', n)
        xs = R.gens()

        def sig(k, vs):
            if k < 0 or k > len(vs):
                return R(0)
            return sum(prod(cc) for cc in itertools.combinations(vs, k)) \
                if k else R(1)
        ys = [v ** 2 for v in xs]
        cc = [sig(a, ys) for a in range(2 * n + 1)]
        okc, okp = True, True
        for j in range(1, n + 1):
            ej = sum(xs[i] * sig(j - 1, ys[:i] + ys[i + 1:]) for i in range(n))
            corr = sum(cc[a] * cc[2 * j - 1 - a] for a in range(j))
            prt = sum(cc[a] * cc[2 * j - 1 - a] for a in range(j + 1))
            okc &= ej ** 2 == corr
            okp &= ej ** 2 != prt
        check(okc, 'exceptional case, n = %d: e_j^2 = sum_(a=0)^(j-1) '
              'c_a c_(2j-1-a) on C^n, all j <= n' % n)
        refuted(not okp, 'printed sum_(a=0)^(jr): fails for some j, n = %d'
                % n)
    # For GL_2(F_3): the subring of F_2[x_1, x_2] generated by c_1, c_2, e_1,
    # e_2 has the dimensions of H^*(GL_2(F_3), F_2) computed above, smaller
    # than those of the Sigma_2-invariants.
    R = PolynomialRing(GF(2), 'x', 2)
    a, b = R.gens()
    gens = [(a + b, 1), (a ** 2 + b ** 2, 2), (a * b ** 2 + a ** 2 * b, 3),
            (a ** 2 * b ** 2, 4)]
    top = 8
    span = {0: [R(1)]}
    for d in range(1, top + 1):
        polys = []
        for gpol, gd in gens:
            if gd <= d:
                polys += [gpol * f for f in span[d - gd]]
        mons = sorted({mm for f in polys for mm in f.monomials()})
        if polys:
            Mx = matrix(GF(2), [[f.monomial_coefficient(mm) for mm in mons]
                                for f in polys])
            basis = Mx.row_space().basis()
            span[d] = [sum(v[i] * mons[i] for i in range(len(mons)))
                       for v in basis]
        else:
            span[d] = []
    sub = [len(span[d]) for d in range(top + 1)]
    check(sub == series([(1, 2), (3, 4)], top),
          'GL_2(F_3): the image of the c_j, e_j in H^*((Z/2)^2) has the '
          'dimensions of H^*(GL_2(F_3), F_2): %s' % sub)

    # p. 67: "the mod p cohomology of BGL_n(F_q) vanishes in positive degrees
    # at most d(p - 1)": H^1(GL_2(F_2), F_2) != 0 (d(p-1) = 1) and
    # H^2(GL_2(F_4), F_2) != 0 (d(p-1) = 2: GL_2(F_4) = Z/3 x A_5, Schur
    # multiplier Z/2); the strict range 0 < i < d(p - 1) holds there.
    def h_dims_12(G, p):
        ab = [int(t) for t in G.AbelianInvariants()]
        mu = [int(t) for t in libgap.AbelianInvariantsMultiplier(G)]
        h1 = sum(1 for t in ab if t % p == 0)
        h2 = sum(1 for t in mu if t % p == 0) + h1
        return h1, h2
    h1, h2 = h_dims_12(libgap.GL(2, 2), 2)
    refuted(h1 == 0, 'p. 67 printed (degrees at most d(p-1) = 1): '
            'H^1(GL_2(F_2), F_2) = 0')
    h1, h2 = h_dims_12(libgap.GL(2, 4), 2)
    refuted(h2 == 0, 'p. 67 printed (degrees at most d(p-1) = 2): '
            'H^2(GL_2(F_4), F_2) = 0')
    check(h1 == 0, 'H^1(GL_2(F_4), F_2) = 0 (0 < i < d(p-1) = 2)')
    # The corrected range 0 < i < d(p - 1): the Borel subgroup B_2(F_q) has
    # index q + 1, prime to p, so H^i(GL_2(F_q), F_p) injects into
    # H^i(B_2(F_q), F_p) (Volume I, Corollary 3.6.18); q = 4, 8, 9
    for q, p, dd in ((4, 2, 2), (8, 2, 3), (9, 3, 2)):
        B = gap('function(q) local F, z; F := GF(q); z := PrimitiveRoot(F); '
                'return Group([[z, 0], [0, 1]] * One(F), [[1, 0], [0, z]] * '
                'One(F), [[1, 1], [0, 1]] * One(F)); end')(q)
        TB = TGroup(B, 'B')
        top = dd * (p - 1) - 1
        hb = free_resolution_cohomology(TB.mul, p, top)
        check(TB.N == (q - 1) ** 2 * q and all(h == 0 for h in hb[1:]),
              'p. 67 (corrected): H^i(GL_2(F_%d), F_%d) = 0 for 0 < i < '
              'd(p - 1) = %d (via B_2(F_%d))' % (q, p, dd * (p - 1), q))
    # H^1(GL_n(F_q), F_p) = Hom(F_q^x, F_p) = 0 for n >= 3 or q >= 3
    for n, q in ((3, 4), (3, 3), (4, 2), (2, 9)):
        ab = [int(a) for a in libgap.GL(n, q).AbelianInvariants()]
        p = ZZ(q).prime_factors()[0]
        check(all(a % p for a in ab), 'H^1(GL_%d(F_%d), F_%d) = 0' % (n, q, p))


def main():
    section_2_2_and_2_4()
    section_2_5()
    section_2_6()
    section_2_8()
    section_2_9_2_10()
    print('ok chapter-2a: %d checks' % COUNT[0])


if __name__ == '__main__':
    main()
