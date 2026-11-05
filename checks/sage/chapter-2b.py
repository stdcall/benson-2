"""Exact checks of Chapter 2 "Cohomology of groups", Sections 2.11-2.15 (Sage).

Run: sage -python checks/sage/chapter-2b.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-2b: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), printed pp. 73-92.
Pages are the printed pages; labels are those of content/02-11-*.typ ...
content/02-15-*.typ.  Sections 2.1-2.10 are checked in chapter-2a.py.

Algebras are given by integral structure constants on a basis e_0 = 1,
e_1, ...: the ground ring k, the dual numbers k[x]/(x^2), the upper
triangular matrices T_2(k), M_2(k) and the group algebra kC_3; elements of
Lambda^(x n) are integer vectors in the basis of tensors of basis elements,
and every operator of the chapter (b, b', s, t, N, eps, B, the double
complexes CC_* and B_*, the Morita maps alpha, beta, h) is an integer
matrix, so identities are checked exactly and homology is computed by ranks
over Q and finite fields.  Group algebras kG are treated through the cyclic
set SG/G (normalised chains).  Printed readings that are wrong are kept as
refuted checks beside the corrected ones.

What is checked, by section:

2.11 (pp. 73-77), section_2_11 and section_2_11_groups
  * b' b' = 0, b b = 0; p. 73: b'_(n+1) s_(n+1) - s_n b'_n = (-1)^(n+1) id
    on S_n(Lambda), n <= 3, five algebras (the printed "= id" refuted for
    n = 0, 2), and (-1)^n s_n is a chain contraction.
  * Theorem 2.11.1: HH_n(M_2(k)) = HH_n(k), k = Q, F_2, F_3, n <= 3;
    HH_*(T_2(Q)) = Q^2 in degree 0.
  * p. 74: the coboundary b^n with coefficients Lambda and Lambda^* (with
    the corrected first term) squares to zero, and p. 85: S^n(Lambda,
    Lambda^*) = (Lambda^(x (n+1)))^* with b^n the transpose of b.
    p. 75: H^*(T_2, T_2) = Q (the centre) while H^*(T_2, T_2^*) = HH_*(T_2)^*
    = Q^2: only HH^0 = H^0(Lambda, Lambda^*) agrees with HC^0 = HH^0 from the
    Connes sequence of p. 85 (the printed H^n(Lambda, Lambda) refuted);
    both readings agree for kC_3.  HH_n(Z) = 0 for n > 0 (p. 77).
  * Theorem 2.11.2 (i) and Proposition 2.12.2: dim HH_n(F_p G) = sum over
    classes of dim H_n(C_G(g), F_p) (nerves) for C2, C3, C4, V4, S3 (p = 2,
    3, 5), n <= 3 to 5.
2.12 (pp. 77-80), section_2_12
  * p. 79: the faces and degeneracies of SG/G are induced from SG with its
    G-action; simplicial identities and, with t_n of Example 1 of Section
    2.14, the cyclic relations (S_3, n <= 3).
  * Delta[1] x Delta[n] has exactly the n + 1 non-degenerate
    (n+1)-simplices (s-bar_i sigma, s_i tau), s-bar_i sigma =
    (s_0)^i (s_1)^(n-i) sigma (the printed exponent n - i - 1 refuted), and
    d_i(s-bar_i sigma, s_i tau) = d_i(s-bar_(i-1) sigma, s_(i-1) tau),
    n <= 6.
  * Proposition 2.12.3: the vertex maps of the simplex displayed on p. 80
    give a bijection of SG onto the n-simplices of X compatible with the
    faces d_0..d_n and the G-action, the arrow labels as printed,
    d_(n+1) f(s-bar_n sigma, s_n tau) = g_0 ... g_(n+1) d_0 f(s-bar_0 sigma,
    s_0 tau), and alpha_(n+1) = g_(n+1)^-1 (the printed "g_(n+1) =
    alpha_(n+1)" refuted), S_3, n <= 2.
2.13 (pp. 80-85), section_2_13 and morita_maps
  * p. 81: N eps = eps N = 0, b eps = eps b', b' N = N b; B^2 = 0,
    bB + Bb = 0, B well defined on the reduced complex (p. 85).
  * HC_n(Lambda) over Q (n <= 3, five algebras) from the double complex
    CC_* (d^2 = 0), from B_*, from the reduced B-bar and from the Connes
    complex Lambda^(x (n+1))/Im(eps) with the corrected degrees (the printed
    shift refuted for Lambda = Q); HC_*(Q) = Q in even degrees, also over
    F_2 from CC_*; the first two columns compute HH_* (p. 82).
  * p. 84: x -> x + (-1)^n s_n N x with the second term in place
    (2i - 1, j - i + 1) is an injective chain map B_* -> CC_*, n = j - i
    (five algebras, total degree <= 4).
  * Theorem 2.13.2: HC_n(M_2(Q)) = HC_n(Q), n <= 3; for Lambda = M_2(Z),
    Gamma = Z, P = Z^2 (columns), Q = Z^2 (rows), s = t = 2: beta_n alpha_n
    is the displayed formula, alpha commutes with b and t_n, and with the
    inner sums of h_n over (i_0..i_m), (j_0..j_m),
    1 - beta_n alpha_n = b h_n + h_(n-1) b (n <= 3); the printed inner sums
    over (i_0..i_n), (j_0..j_n) (either sign) and the printed sign
    beta_n alpha_n - 1 refuted.
2.14 (pp. 85-90), section_2_14
  * The relations of p. 86 in a model of Connes' category (degree-one
    periodic maps Z -> Z modulo translation by n + 1), n <= 7; n arrows from
    a cyclically ordered set of size n to one of size one (n <= 8).
  * Examples 4 (p. 87): the face and degeneracy formulas of S[1] |x| X as
    identities in the model (n <= 7), with exponent j + 1 for i < j (the
    printed j - 1 refuted); S[1] |x| Delta[2] is a cyclic set (n <= 4), and
    not with the printed degeneracies.
  * Warning (p. 88): for X = S[1] (not a Kan complex) Hom(S[1], S[1]) has
    two vertices while Map(S^1, S^1) has a component for each degree (the
    printed "any simplicial set" refuted); for the Kan complex NG the
    components of Hom(S[1], NG) = SG/G are the conjugacy classes (S_3).
  * Proof of Proposition 2.14.1 (p. 90): on the reduced chains of SG/G
    (G = C_3, S_3, n <= 3) the printed sum_i (-1)^(in) t^i(s_i x) is not
    +-B(x) (refuted); the corrected sum_i (-1)^(in) t_(n+1)^(n+1-i)(s_i x)
    is (-1)^n B(x), B = (-1)^n eps s_n N as defined on p. 89.
  * H_*(CP^2): HC_*(k) = H_*(BS^1) in degrees <= 4.
2.15 (pp. 90-92), section_2_15
  * Corollary 2.15.3 (i): dim HC_n(kG) = sum over classes of dim
    H_n(B C-hat_G(g); k), with C-hat_G(1) = S^1 x G and C-hat_G(g) =
    R/mZ = S^1 when C_G(g) = <g> has order m, for C2 (F_2, Q), C3 (F_3, Q),
    C5 (F_5), S3 (F_2, F_3, F_5), n <= 3 to 5; HC_n(F_7 S_3) = F_7^3 in
    even degrees.

What is NOT established.  No general theorem is proved: every check
concerns the listed algebras, groups, fields and degrees.  The topological
statements (Lemma 2.12.1, Theorem 2.15.2, the realisation of cyclic sets,
the Eilenberg-Zilber map) are not checked; H_*(B C-hat_G(g)) is computed
from the stated structure of C-hat_G(g) and the Kuenneth formula, not from
a model of the space.  The model of Connes' category is not shown to be
faithful.  Nothing here compares our text with the printed book.
"""


import itertools

import numpy as np
from sage.all import GF, QQ, ZZ, ChainComplex, libgap, matrix, simplicial_complexes

SCOPE = 'chapter-2b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


# ---------------------------------------------------------------------------
# Algebras with an integral basis e_0 = 1, e_1, ..., e_(d-1); elements of
# Lambda^(x k) are integer numpy arrays of length d^k (row-major multi-index);
# linear maps are integer matrices acting on row vectors (x -> x @ M).
# ---------------------------------------------------------------------------

class Algebra:
    def __init__(self, name, d, mu):
        self.name, self.d = name, d
        self.mu = np.array(mu, dtype=np.int64)   # mu[u, v] = coords of e_u e_v
        assert all((self.mu[0, v] == np.eye(d, dtype=np.int64)[v]).all() and
                   (self.mu[v, 0] == np.eye(d, dtype=np.int64)[v]).all()
                   for v in range(d)), 'e_0 must be the identity'

    def tensor_dim(self, k):
        return self.d ** k

    # basic operators on Lambda^(x k), as matrices --------------------------
    def merge(self, k, i):
        """lambda_0 (x) ... (x) lambda_i lambda_(i+1) (x) ... : d^k -> d^(k-1)."""
        d = self.d
        M = np.zeros((d ** k, d ** (k - 1)), dtype=np.int64)
        for idx in itertools.product(range(d), repeat=k):
            row = np.ravel_multi_index(idx, (d,) * k) if k else 0
            prodv = self.mu[idx[i], idx[i + 1]]
            for w in np.nonzero(prodv)[0]:
                new = idx[:i] + (w,) + idx[i + 2:]
                M[row, np.ravel_multi_index(new, (d,) * (k - 1))] += prodv[w]
        return M

    def wrap(self, k):
        """lambda_(k-1) lambda_0 (x) lambda_1 (x) ... (x) lambda_(k-2)."""
        d = self.d
        M = np.zeros((d ** k, d ** (k - 1)), dtype=np.int64)
        for idx in itertools.product(range(d), repeat=k):
            row = np.ravel_multi_index(idx, (d,) * k)
            prodv = self.mu[idx[-1], idx[0]]
            for w in np.nonzero(prodv)[0]:
                new = (w,) + idx[1:-1]
                M[row, np.ravel_multi_index(new, (d,) * (k - 1))] += prodv[w]
        return M

    def bprime(self, k):
        """b' on Lambda^(x k) (degree k - 1): sum_(i=0)^(k-2) (-1)^i merge_i."""
        if k == 1:
            return np.zeros((self.d, 1), dtype=np.int64)
        return sum((-1) ** i * self.merge(k, i) for i in range(k - 1))

    def b(self, k):
        """Hochschild b on Lambda^(x k) (p. 80)."""
        if k == 1:
            return np.zeros((self.d, 1), dtype=np.int64)
        n = k - 1
        return self.bprime(k) + (-1) ** n * self.wrap(k)

    def t(self, k):
        d = self.d
        M = np.zeros((d ** k, d ** k), dtype=np.int64)
        for idx in itertools.product(range(d), repeat=k):
            row = np.ravel_multi_index(idx, (d,) * k)
            new = (idx[-1],) + idx[:-1]
            M[row, np.ravel_multi_index(new, (d,) * k)] = 1
        return M

    def s(self, k):
        """append 1: Lambda^(x k) -> Lambda^(x (k+1))."""
        d = self.d
        M = np.zeros((d ** k, d ** (k + 1)), dtype=np.int64)
        for idx in itertools.product(range(d), repeat=k):
            row = np.ravel_multi_index(idx, (d,) * k) if k else 0
            M[row, np.ravel_multi_index(idx + (0,), (d,) * (k + 1))] = 1
        return M

    def eps(self, k):
        n = k - 1
        return np.eye(self.d ** k, dtype=np.int64) - (-1) ** n * self.t(k)

    def N(self, k):
        n = k - 1
        T = (-1) ** n * self.t(k)
        P = np.eye(self.d ** k, dtype=np.int64)
        S = np.zeros_like(P)
        for _ in range(k):
            S = S + P
            P = P @ T
        return S

    def Bop(self, k):
        """B = (-1)^n eps s_n N : Lambda^(x k) -> Lambda^(x (k+1)), n = k - 1."""
        n = k - 1
        return (-1) ** n * (self.N(k) @ self.s(k) @ self.eps(k + 1))


def matrix_algebra(n):
    d = n * n
    mu = np.zeros((d, d, d), dtype=np.int64)
    # basis: e_0 = identity is not an elementary matrix; use the basis
    # 1, E_01, E_10, E_11 for n = 2 (E_00 = 1 - E_11)
    assert n == 2
    one = np.eye(2, dtype=np.int64)
    mats = [one, np.array([[0, 1], [0, 0]]), np.array([[0, 0], [1, 0]]),
            np.array([[0, 0], [0, 1]])]
    Minv = np.array([m.flatten() for m in mats]).T  # columns = basis

    def coords(A):
        sol = np.linalg.solve(Minv.astype(float), A.flatten().astype(float))
        return np.rint(sol).astype(np.int64)
    for u in range(4):
        for v in range(4):
            mu[u, v] = coords(mats[u] @ mats[v])
    return Algebra('M_2', 4, mu), mats, coords


def upper_triangular():
    # basis 1, E_01, E_11 of T_2
    mats = [np.eye(2, dtype=np.int64), np.array([[0, 1], [0, 0]]),
            np.array([[0, 0], [0, 1]])]
    Minv = np.array([m.flatten() for m in mats]).T
    mu = np.zeros((3, 3, 3), dtype=np.int64)
    for u in range(3):
        for v in range(3):
            P = (mats[u] @ mats[v]).flatten()
            sol = np.linalg.lstsq(Minv.astype(float), P.astype(float),
                                  rcond=None)[0]
            mu[u, v] = np.rint(sol).astype(np.int64)
    return Algebra('T_2', 3, mu)


def dual_numbers():
    mu = np.zeros((2, 2, 2), dtype=np.int64)
    mu[0, 0, 0] = mu[0, 1, 1] = mu[1, 0, 1] = 1
    return Algebra('k[x]/(x^2)', 2, mu)


def ground():
    return Algebra('k', 1, [[[1]]])


def cyclic_group_algebra(m):
    mu = np.zeros((m, m, m), dtype=np.int64)
    for u in range(m):
        for v in range(m):
            mu[u, v, (u + v) % m] = 1
    return Algebra('kC_%d' % m, m, mu)


def rank(M, ring):
    if M.size == 0:
        return 0
    return matrix(ring, M.tolist()).rank()


def homology_dims(diffs, dims, ring, top):
    """diffs[k]: matrix C_k -> C_(k-1) (row convention), dims[k] = dim C_k."""
    rk = {k: rank(diffs[k], ring) if k in diffs else 0
          for k in range(0, top + 2)}
    return [dims[k] - rk[k] - rk[k + 1] for k in range(top + 1)]


def Z0(*shape):
    return np.zeros(shape, dtype=np.int64)


def eye(n):
    return np.eye(n, dtype=np.int64)


ALGS = None


def algebras():
    global ALGS
    if ALGS is None:
        M2, mats, coords = matrix_algebra(2)
        ALGS = [ground(), dual_numbers(), upper_triangular(), M2,
                cyclic_group_algebra(3)]
    return ALGS


# ---------------------------------------------------------------------------
# Hochschild cochains with coefficients in Lambda or Lambda^*
# ---------------------------------------------------------------------------

def cochain_coboundary(A, n, coeff):
    """Matrix of b^n : Hom(Lambda^(x n), M) -> Hom(Lambda^(x (n+1)), M) of
    p. 74 (first term lambda_1 f(lambda_2, ..., lambda_(n+1))), M = Lambda
    (coeff 'L') or Lambda^* (coeff 'D', (l.phi.m)(x) = phi(m x l)).  A
    cochain is a vector of length d^n * d (f(basis tensor) in coordinates of
    M); row convention."""
    d = A.d
    mu = A.mu

    def left(l, v):    # l . v for v in M (coordinates)
        if coeff == 'L':
            return sum(v[w] * mu[l, w] for w in range(d))
        # (l.phi)(x) = phi(x l): (l.phi)_u = phi(e_u l) = sum_w mu[u,l,w] phi_w
        return np.array([sum(mu[u, l, w] * v[w] for w in range(d))
                         for u in range(d)])

    def right(v, l):   # v . l
        if coeff == 'L':
            return sum(v[w] * mu[w, l] for w in range(d))
        return np.array([sum(mu[l, u, w] * v[w] for w in range(d))
                         for u in range(d)])
    rows = []
    shape_in = (d,) * n
    for fi in range(d ** n * d):
        F = np.zeros(d ** n * d, dtype=np.int64)
        F[fi] = 1
        F = F.reshape(d ** n, d)

        def f(idx):
            return F[np.ravel_multi_index(idx, shape_in) if n else 0]

        def f_lin(vecs):   # f on a tensor given as list of coordinate vectors
            out = np.zeros(d, dtype=np.int64)
            for idx in itertools.product(range(d), repeat=n):
                c = 1
                for t, i in enumerate(idx):
                    c *= vecs[t][i]
                    if c == 0:
                        break
                if c:
                    out += c * f(idx)
            return out
        out = np.zeros((d ** (n + 1), d), dtype=np.int64)
        for idx in itertools.product(range(d), repeat=n + 1):
            vecs = [np.eye(d, dtype=np.int64)[i] for i in idx]
            val = left(idx[0], f_lin(vecs[1:]))
            for i in range(1, n + 1):
                merged = vecs[:i - 1] + [mu[idx[i - 1], idx[i]]] + vecs[i + 1:]
                val = val + (-1) ** i * f_lin(merged)
            val = val + (-1) ** (n + 1) * right(f_lin(vecs[:n]), idx[n])
            out[np.ravel_multi_index(idx, (d,) * (n + 1))] = val
        rows.append(out.flatten())
    return np.array(rows, dtype=np.int64)


def section_2_11():
    """Section 2.11: the acyclic Hochschild complex, Hochschild (co)homology."""
    for A in algebras():
        d = A.d
        for k in range(2, 6):
            if k >= 3:
                check(not (A.bprime(k) @ A.bprime(k - 1)).any(),
                      "p. 73: b' b' = 0 on S_%d(%s)" % (k - 2, A.name))
            check(not (A.b(k) @ A.b(k - 1)).any() if k >= 2 else True,
                  'p. 74: b b = 0 on Lambda^(x %d), %s' % (k, A.name))
        # p. 73 in the book's indexing: S_n = Lambda^(x (n+2)); s_(n+1)
        # appends 1; b'_(n+1) s_(n+1) - s_n b'_n = (-1)^(n+1) id
        for n in range(0, 4):
            k = n + 2
            lhs = A.s(k) @ A.bprime(k + 1) - A.bprime(k) @ A.s(k - 1)
            check((lhs == (-1) ** (n + 1) * eye(d ** k)).all(),
                  "p. 73: b'_(n+1) s_(n+1) - s_n b'_n = (-1)^(n+1) id on "
                  "S_%d(%s)" % (n, A.name))
            if n % 2 == 0 and A.name == 'M_2':
                refuted((lhs == eye(d ** k)).all(),
                        "p. 73 printed: b'_(n+1) s_(n+1) - s_n b'_n = id on "
                        "S_%d(M_2)" % n)
            contr = (-1) ** (n + 1) * A.s(k) @ A.bprime(k + 1) + \
                (-1) ** n * A.bprime(k) @ A.s(k - 1)
            check((contr == eye(d ** k)).all(),
                  "p. 73: (-1)^n s_n is a chain contraction on S_%d(%s)"
                  % (n, A.name))
    # Hochschild homology HH_n = H_n of (Lambda^(x (n+1)), b), n <= 3
    def hh(A, ring, top=3):
        diffs = {k: A.b(k + 1) for k in range(1, top + 2)}
        dims = {k: A.d ** (k + 1) for k in range(top + 2)}
        return homology_dims(diffs, dims, ring, top)
    k_, dual, T2, M2, C3 = algebras()
    for ring in (QQ, GF(2), GF(3)):
        check(hh(M2, ring) == hh(k_, ring) == [1, 0, 0, 0],
              'Theorem 2.11.1: HH_n(M_2(k)) = HH_n(k), n <= 3, k = %s' % ring)
    check(hh(T2, QQ) == [2, 0, 0, 0], 'HH_*(T_2(Q)) = Q^2 in degree 0')
    # Hochschild cohomology with coefficients Lambda and Lambda^* (p. 74):
    # b b = 0, and S^n(Lambda, Lambda^*) = (Lambda^(x (n+1)))^* with b^n the
    # transpose of b (p. 85)
    for A in (T2, M2, dual):
        d = A.d
        for coeff in ('L', 'D'):
            for n in range(0, 2):
                C0 = cochain_coboundary(A, n, coeff)
                C1 = cochain_coboundary(A, n + 1, coeff)
                check(not (C0 @ C1).any(), 'p. 74: b^(n+1) b^n = 0, %s, n = '
                      '%d, coefficients %s' % (A.name, n, coeff))
        for n in range(0, 3):
            Cn = cochain_coboundary(A, n, 'D')
            # F(l_0, l_1..l_n) = f(l_1..l_n)(l_0): index (l_0, l_1..l_n) of
            # (Lambda^(x (n+1)))^* <-> (l_1..l_n ; coordinate l_0)
            def to_F(vec, m):
                Fv = vec.reshape((d,) * m + (d,))
                return np.moveaxis(Fv, -1, 0).reshape(-1)
            ok = True
            for fi in range(d ** n * d):
                e = np.zeros(d ** n * d, dtype=np.int64)
                e[fi] = 1
                lhs = to_F(e @ Cn, n + 1)
                rhs = A.b(n + 2) @ to_F(e, n)
                ok &= (lhs == rhs).all()
            check(ok, 'p. 85: S^n(Lambda, Lambda^*) = (Lambda^(x (n+1)))^* '
                  'and b^n = transpose of b, %s, n = %d' % (A.name, n))

    def coh(A, coeff, ring, top=2):
        d = A.d
        dims = [d ** n * d for n in range(top + 2)]
        rk = [0] + [rank(cochain_coboundary(A, n, coeff), ring)
                    for n in range(top + 1)]
        return [dims[n] - rk[n] - rk[n + 1] for n in range(top + 1)]
    hl, hd = coh(T2, 'L', QQ), coh(T2, 'D', QQ)
    check(hl == [1, 0, 0], 'H^*(T_2, T_2) = Q in degree 0 (the centre)')
    check(hd == [2, 0, 0] and hd == hh(T2, QQ, 2),
          'H^n(T_2, T_2^*) = HH_n(T_2)^*')
    # Cyclic cohomology: HC^0 = (HC_0)^* = (Lambda/[Lambda, Lambda])^* has
    # dimension 2 for T_2, and the Connes sequence of p. 85 gives
    # HC^0 = HH^0 (HC^(-1) = HC^(-2) = 0): so HH^0 must be H^0(Lambda,
    # Lambda^*) as defined on p. 85, not the printed H^0(Lambda, Lambda) of
    # p. 75.
    hc0 = T2.d - rank(T2.b(2), QQ)
    check(hc0 == hd[0], 'p. 85: HC^0(T_2) = HH^0(T_2) = H^0(T_2, T_2^*)')
    refuted(hc0 == hl[0], 'p. 75 printed: HH^0(T_2) = H^0(T_2, T_2), '
            'incompatible with the Connes sequence of p. 85')
    # Lambda = Lambda^* for symmetric algebras: the two readings agree for
    # group algebras (Theorem 2.11.2), e.g. kC_3
    check(coh(C3, 'L', QQ) == coh(C3, 'D', QQ) == [3, 0, 0],
          'HH^*(QC_3) with Lambda or Lambda^* coefficients: Q^3 in degree 0')
    # HH_n(Z) = 0 for n > 0 (end of Section 2.11)
    diffs = {k: ground().b(k + 1) for k in range(1, 8)}
    hz = ChainComplex({k: matrix(ZZ, diffs[k].T.tolist()) for k in diffs},
                      degree=-1)
    check(all(hz.homology(k).invariants() == () for k in range(1, 7)) and
          tuple(hz.homology(0).invariants()) == (0,),
          'p. 77: HH_n(Z) = 0 for n > 0, HH_0(Z) = Z')


class TG:
    """A small group as a multiplication table (from GAP)."""

    def __init__(self, src):
        G = libgap.eval(src)
        self.name = src
        self.elts = G.AsSSortedList()
        tab = libgap.eval('function(e) return List(e, g -> List(e, h -> '
                          'PositionSorted(e, g*h))); end')(self.elts)
        self.mul = [[int(x) - 1 for x in row] for row in tab]
        self.N = len(self.mul)
        self.one = int(self.elts.Position(G.Identity())) - 1
        self.inv = [self.mul[g].index(self.one) for g in range(self.N)]

    def m(self, a, b):
        return self.mul[a][b]

    def classes(self):
        seen, out = set(), []
        for g in range(self.N):
            if g not in seen:
                cl = {self.m(self.m(h, g), self.inv[h]) for h in range(self.N)}
                seen |= cl
                out.append(g)
        return out

    def centraliser_gens(self, g):
        return [h for h in range(self.N) if self.m(h, g) == self.m(g, h)]


# --- the cyclic set SG/G (Sections 2.12, 2.14) -----------------------------

def sgg_face(G, x, i):
    n = len(x) - 1
    if i < n:
        return x[:i] + (G.m(x[i], x[i + 1]),) + x[i + 2:]
    return (G.m(x[n], x[0]),) + x[1:n]


def sgg_degen(G, x, i):
    return x[:i + 1] + (G.one,) + x[i + 1:]


def sgg_t(G, x):
    return (x[-1],) + x[:-1]


def normalised_basis(G, n):
    nonid = [g for g in range(G.N) if g != G.one]
    return [(g0,) + rest for g0 in range(G.N)
            for rest in itertools.product(nonid, repeat=n)]


def is_degenerate(G, x):
    return any(g == G.one for g in x[1:])


def lin_apply(f, vec):
    out = {}
    for x, c in vec.items():
        for y, e in f(x).items():
            out[y] = out.get(y, 0) + c * e
    return {y: c for y, c in out.items() if c}


def sgg_b(G, x):
    n = len(x) - 1
    out = {}
    for i in range(n + 1):
        y = sgg_face(G, x, i)
        out[y] = out.get(y, 0) + (-1) ** i
    return out


def sgg_bprime(G, x):
    n = len(x) - 1
    out = {}
    for i in range(n):
        y = sgg_face(G, x, i)
        out[y] = out.get(y, 0) + (-1) ** i
    return out


def sgg_N(G, x):
    n = len(x) - 1
    out, y = {}, x
    for j in range(n + 1):
        out[y] = out.get(y, 0) + (-1) ** (n * j)
        y = sgg_t(G, y)
    return out


def sgg_B(G, x):
    """B = (-1)^n eps s_n N (p. 83, p. 89), on R[SG/G]_n."""
    n = len(x) - 1
    out = {}
    for y, c in sgg_N(G, x).items():
        z = sgg_degen(G, y, n)                 # s_n
        for w, e in ((z, 1), (sgg_t(G, z), -(-1) ** (n + 1))):  # eps
            out[w] = out.get(w, 0) + (-1) ** n * c * e
    return {y: c for y, c in out.items() if c}


def normalised_matrix(G, f, n_in, n_out, ring):
    rows = normalised_basis(G, n_in)
    cols = normalised_basis(G, n_out)
    pos = {c: i for i, c in enumerate(cols)}
    D = {}
    for r, x in enumerate(rows):
        for y, c in f(G, x).items():
            if is_degenerate(G, y):
                continue
            D[(r, pos[y])] = D.get((r, pos[y]), 0) + c
    return matrix(ring, len(rows), len(cols), D, sparse=False)


def group_hh(G, ring, top):
    dims = [len(normalised_basis(G, n)) for n in range(top + 2)]
    rk = [0] + [normalised_matrix(G, sgg_b, n, n - 1, ring).rank()
                for n in range(1, top + 2)]
    return [dims[n] - rk[n] - rk[n + 1] for n in range(top + 1)]


def group_hc(G, ring, top):
    """Homology of the total complex of the reduced double complex
    B-bar(RG) (p. 84): degree k = sum over i of normalised chains of
    Hochschild degree k - 2i; differential b + B."""
    def blocks(k):
        return [k - 2 * i for i in range(k // 2 + 1)]
    bases = {k: [(n, x) for n in blocks(k) for x in normalised_basis(G, n)]
             for k in range(top + 2)}
    pos = {k: {e: i for i, e in enumerate(bases[k])} for k in bases}
    rk = [0]
    for k in range(1, top + 2):
        D = {}
        for r, (n, x) in enumerate(bases[k]):
            terms = []
            if n >= 1:
                terms += [((n - 1, y), c) for y, c in sgg_b(G, x).items()]
            terms += [((n + 1, y), c) for y, c in sgg_B(G, x).items()]
            for (m, y), c in terms:
                if is_degenerate(G, y) or (m, y) not in pos[k - 1]:
                    continue
                key = (r, pos[k - 1][(m, y)])
                D[key] = D.get(key, 0) + c
        rk.append(matrix(ring, len(bases[k]), len(bases[k - 1]), D,
                         sparse=False).rank())
    rk.append(0)
    return [len(bases[k]) - rk[k] - rk[k + 1] for k in range(top + 1)]


def nerve_dims(G, gens, ring, top):
    """dim H_k(BC; ring) for the subgroup C = gens of G (normalised nerve)."""
    C = sorted(set(gens))
    nonid = [g for g in C if g != G.one]
    simp = {0: [()]}
    for n in range(1, top + 2):
        simp[n] = list(itertools.product(nonid, repeat=n))
    pos = {n: {s: i for i, s in enumerate(simp[n])} for n in simp}
    rk = [0]
    for n in range(1, top + 2):
        D = {}
        for j, s in enumerate(simp[n]):
            faces = [(0, s[1:])]
            for i in range(1, n):
                faces.append((i, s[:i - 1] + (G.m(s[i - 1], s[i]),) +
                              s[i + 1:]))
            faces.append((n, s[:-1]))
            for i, f in faces:
                if G.one in f:
                    continue
                key = (j, pos[n - 1][f])
                D[key] = D.get(key, 0) + (-1) ** i
        rk.append(matrix(ring, len(simp[n]), len(simp[n - 1]), D,
                         sparse=False).rank())
    rk.append(0)
    return [len(simp[k]) - rk[k] - rk[k + 1] for k in range(top + 1)]


def section_2_11_groups():
    """Theorem 2.11.2 (i) and Proposition 2.12.2: HH_n(kG) is the sum over
    classes of H_n(C_G(g), k); dimensions, n <= 3 (4 for cyclic groups)."""
    cases = [('CyclicGroup(IsPermGroup, 2)', 2, 5),
             ('CyclicGroup(IsPermGroup, 3)', 3, 5),
             ('CyclicGroup(IsPermGroup, 4)', 2, 4),
             ('Group((1,2),(3,4))', 2, 3),
             ('SymmetricGroup(3)', 2, 3), ('SymmetricGroup(3)', 3, 3),
             ('SymmetricGroup(3)', 5, 3)]
    for src, p, top in cases:
        G = TG(src)
        lhs = group_hh(G, GF(p), top)
        rhs = [0] * (top + 1)
        for g in G.classes():
            h = nerve_dims(G, G.centraliser_gens(g), GF(p), top)
            rhs = [a + b for a, b in zip(rhs, h)]
        check(lhs == rhs, 'Theorem 2.11.2 (i): dim HH_n(F_%d G) = sum over '
              'classes of dim H_n(C_G(g), F_%d), G = %s, n <= %d: %s'
              % (p, p, src, top, lhs))


def section_2_12():
    """Section 2.12: the simplicial set SG/G and Proposition 2.12.3."""
    G = TG('SymmetricGroup(3)')
    m, inv, one = G.m, G.inv, G.one
    # SG: n-simplices g_0 (x) ... (x) g_(n+1); G acts by
    # g(g_0, ..., g_(n+1)) = (g g_0, g_1, ..., g_(n+1) g^-1); the orbit of
    # (g_0, ..., g_n, 1) is the simplex g_0 (x) ... (x) g_n of SG/G (p. 79).
    def sg_face(y, i):
        return y[:i] + (m(y[i], y[i + 1]),) + y[i + 2:]

    def normalise(y):           # the orbit representative with last entry 1
        g = y[-1]
        return (m(g, y[0]),) + y[1:-1] + (m(y[-1], inv[g]),)
    ok = True
    for n in range(1, 4):
        for x in itertools.product(range(G.N), repeat=n + 1):
            y = x + (one,)
            for i in range(n + 1):
                z = normalise(sg_face(y, i))
                ok &= z[-1] == one and z[:-1] == sgg_face(G, x, i)
            for i in range(n + 1):
                z = normalise(y[:i + 1] + (one,) + y[i + 1:])
                ok &= z[:-1] == sgg_degen(G, x, i)
    check(ok, 'p. 79: the faces and degeneracies of SG/G are those induced '
          'from SG (G = S_3, n <= 3)')
    # simplicial identities and the cyclic relations of p. 86 for SG/G with
    # t_n of Example 1 (p. 87)
    okS, okC = True, True
    for n in range(1, 4):
        for x in itertools.product(range(G.N), repeat=n + 1):
            d = lambda y, i: sgg_face(G, y, i)
            s = lambda y, i: sgg_degen(G, y, i)
            t = lambda y: sgg_t(G, y)
            for i in range(n + 1):
                for j in range(i + 1, n + 1):
                    if n >= 2:
                        okS &= d(d(x, j), i) == d(d(x, i), j - 1)
            for i in range(n + 2):
                for j in range(n + 1):
                    if i < j:
                        okS &= d(s(x, j), i) == s(d(x, i), j - 1)
                    elif i == j or i == j + 1:
                        okS &= d(s(x, j), i) == x
                    else:
                        okS &= d(s(x, j), i) == s(d(x, i - 1), j)
                    if i <= j:
                        okS &= s(s(x, j), i) == s(s(x, i), j + 1)
            tx = t(x)
            for i in range(1, n + 1):
                okC &= d(tx, i) == t(d(x, i - 1))
                okC &= s(tx, i) == t(s(x, i - 1))
            okC &= d(tx, 0) == d(x, n)
            okC &= s(tx, 0) == t(t(s(x, n)))
            y = x
            for _ in range(n + 1):
                y = t(y)
            okC &= y == x
    check(okS, 'SG/G satisfies the simplicial identities (S_3, n <= 3)')
    check(okC, 'p. 86-87: SG/G with t_n of Example 1 satisfies the cyclic '
          'relations (S_3, n <= 3)')
    # Delta[1] x Delta[n]: the non-degenerate (n+1)-simplices are
    # (s-bar_i sigma, s_i tau), s-bar_i sigma = (s_0)^i (s_1)^(n-i) sigma
    def degen(seq, j):
        return seq[:j + 1] + seq[j:]
    ok, okface = True, True
    for n in range(1, 7):
        nd = []
        for a in itertools.combinations_with_replacement((0, 1), n + 2):
            for b in itertools.combinations_with_replacement(range(n + 1),
                                                             n + 2):
                pts = list(zip(a, b))
                if len(set(pts)) == n + 2:
                    nd.append((a, b))
        sbar = {}
        for i in range(n + 1):
            seq = (0, 1)
            for _ in range(n - i):
                seq = degen(seq, 1)
            for _ in range(i):
                seq = degen(seq, 0)
            sbar[i] = seq
            tau = tuple(range(n + 1))
            ok &= (seq, degen(tau, i)) in nd
            ok &= seq == (0,) * (i + 1) + (1,) * (n - i + 1)
        ok &= len(nd) == n + 1
        for i in range(1, n + 1):
            tau = tuple(range(n + 1))
            f1 = tuple(zip(sbar[i], degen(tau, i)))
            f0 = tuple(zip(sbar[i - 1], degen(tau, i - 1)))
            okface &= f1[:i] + f1[i + 1:] == f0[:i] + f0[i + 1:]
        # printed exponent n - i - 1: an n-simplex, not an (n+1)-simplex
        seq = (0, 1)
        for _ in range(n - 0 - 1):
            seq = degen(seq, 1)
        refuted(len(seq) == n + 2, 'p. 79 printed: (s_0)^0 (s_1)^(n-1) sigma '
                'is an (n+1)-simplex (n = %d)' % n)
    check(ok, 'p. 79: Delta[1] x Delta[n] has exactly the n + 1 '
          'non-degenerate (n+1)-simplices (s-bar_i sigma, s_i tau), n <= 6')
    check(okface, 'p. 79: d_i(s-bar_i sigma, s_i tau) = d_i(s-bar_(i-1) '
          'sigma, s_(i-1) tau), n <= 6')
    # The simplex formula at the end of the proof (p. 80): vertices
    # v(0, b) = g_0 ... g_b, v(1, b) = alpha_(b+1) = g_(n+1)^-1 ... g_(b+1)^-1
    # in N C(G) (indiscrete category: a map from Delta[1] x Delta[n] is a
    # vertex map); f(s-bar_i sigma, s_i tau) has vertices v(0,0..i),
    # v(1, i..n).
    def word(seq):
        r = one
        for g in seq:
            r = m(r, g)
        return r
    okv, okface2, okorb, okalpha, okg = True, True, True, True, True
    for n in range(0, 3):
        images = set()
        for gs in itertools.product(range(G.N), repeat=n + 2):
            v0 = [word(gs[:b + 1]) for b in range(n + 1)]
            alpha = [word([inv[g] for g in reversed(gs[k:])])
                     for k in range(n + 2)]       # alpha[k] = alpha_k
            v1 = [alpha[b + 1] for b in range(n + 1)]
            images.add((tuple(v0), tuple(v1)))
            # f(s-bar_i sigma, s_i tau): v0[0..i], v1[i..n]
            f = {i: tuple(v0[:i + 1]) + tuple(v1[i:]) for i in range(n + 1)}
            # arrow labels (right multiplication, p. 80)
            for i in range(n + 1):
                lab = [m(inv[f[i][k]], f[i][k + 1]) for k in range(n + 1)]
                want = list(gs[1:i + 1]) + \
                    [m(inv[word(gs[:i + 1])], alpha[i + 1])] + \
                    list(gs[i + 1:n + 1])
                okv &= lab == want
            # d_(n+1) f(s-bar_n sigma, s_n tau) = g_0 ... g_(n+1) .
            # d_0 f(s-bar_0 sigma, s_0 tau)
            top_ = f[n][:n + 1]
            bot = f[0][1:]
            c = word(gs)
            okface2 &= top_ == tuple(m(c, a) for a in bot)
            # G-orbit condition and alpha_(n+1) = g_(n+1)^-1
            okalpha &= alpha[n + 1] == inv[gs[n + 1]]
            # SG faces d_i (0 <= i <= n) correspond to faces of f
            for i in range(n + 1):
                if n == 0:
                    continue
                hs = gs[:i] + (m(gs[i], gs[i + 1]),) + gs[i + 2:]
                w0 = [word(hs[:b + 1]) for b in range(n)]
                al = [word([inv[g] for g in reversed(hs[k:])])
                      for k in range(n + 1)]
                w1 = [al[b + 1] for b in range(n)]
                okg &= w0 == v0[:i] + v0[i + 1:] and w1 == v1[:i] + v1[i + 1:]
            # G-action: g(g_0, ..., g_(n+1)) = (g g_0, ..., g_(n+1) g^-1)
            for h in range(G.N):
                hs = (m(h, gs[0]),) + gs[1:-1] + (m(gs[-1], inv[h]),)
                w0 = [word(hs[:b + 1]) for b in range(n + 1)]
                okorb &= w0 == [m(h, a) for a in v0]
        # bijection onto the maps with f(1) in the G-orbit of f(0)
        target = set()
        for v0 in itertools.product(range(G.N), repeat=n + 1):
            for h in range(G.N):
                target.add((v0, tuple(m(h, a) for a in v0)))
        check(images == target and len(images) == G.N ** (n + 2),
              'Proposition 2.12.3: g_0 (x) ... (x) g_(n+1) -> f is a '
              'bijection onto the n-simplices of X (S_3, n = %d)' % n)
    check(okv, 'p. 80: the arrow labels of f(s-bar_i sigma, s_i tau)')
    check(okface2, 'p. 80: d_(n+1) f(s-bar_n sigma, s_n tau) = g_0 ... '
          'g_(n+1) d_0 f(s-bar_0 sigma, s_0 tau)')
    check(okg, 'Proposition 2.12.3: the correspondence respects the faces '
          'd_0, ..., d_n of SG')
    check(okorb, 'Proposition 2.12.3: the correspondence respects the '
          'G-action')
    check(okalpha, 'p. 80: alpha_(n+1) = g_(n+1)^-1')
    bad = [g for g in range(G.N) if inv[g] != g]
    refuted(not bad, 'p. 80 printed: "g_(n+1) = alpha_(n+1)" (alpha_(n+1) = '
            'g_(n+1)^-1 differs whenever g_(n+1)^2 != 1, e.g. a 3-cycle)')


def cc_total(A, ring, top):
    """The double complex CC_*(Lambda) of p. 81: column p, row q holds
    Lambda^(x (q+1)); vertical b (p even), -b' (p odd); horizontal eps
    (p odd -> p - 1), N (p even >= 2 -> p - 1).  Returns (diffs, dims,
    offsets) of the total complex in degrees <= top + 1."""
    d = A.d
    offs, dims = {}, {}
    for k in range(top + 2):
        o, off = 0, {}
        for p in range(k + 1):
            off[p] = o
            o += d ** (k - p + 1)
        offs[k], dims[k] = off, o
    diffs = {}
    for k in range(1, top + 2):
        D = np.zeros((dims[k], dims[k - 1]), dtype=np.int64)
        for p in range(k + 1):
            q = k - p
            r0 = offs[k][p]
            size = d ** (q + 1)
            if q >= 1:   # vertical to (p, q - 1)
                V = A.b(q + 1) if p % 2 == 0 else -A.bprime(q + 1)
                c0 = offs[k - 1][p]
                D[r0:r0 + size, c0:c0 + d ** q] += V
            if p >= 1:   # horizontal to (p - 1, q)
                H = A.eps(q + 1) if p % 2 == 1 else A.N(q + 1)
                c0 = offs[k - 1][p - 1]
                D[r0:r0 + size, c0:c0 + size] += H
        diffs[k] = D
    return diffs, dims, offs


def b_total(A, top, reduced=False):
    """The double complex B_*(Lambda) (p. 84): column i, row j holds
    Lambda^(x (j-i+1)) (Hochschild degree n = j - i), vertical b,
    horizontal B (column i -> i - 1).  With reduced=True, the quotient
    Lambda (x) Lambda-bar^(x n) of B-bar(Lambda) (basis tuples with no e_0
    after the first place)."""
    d = A.d

    def keep(k):
        if not reduced:
            return np.arange(d ** k)
        idx = [r for r, t in enumerate(itertools.product(range(d), repeat=k))
               if all(v != 0 for v in t[1:])]
        return np.array(idx, dtype=np.int64)
    offs, dims = {}, {}
    for k in range(top + 2):
        o, off = 0, {}
        for i in range(k // 2 + 1):
            n = k - 2 * i
            off[i] = (o, n)
            o += len(keep(n + 1))
        offs[k], dims[k] = off, o
    diffs = {}
    for k in range(1, top + 2):
        D = np.zeros((dims[k], dims[k - 1]), dtype=np.int64)
        for i, (r0, n) in offs[k].items():
            rows = keep(n + 1)
            if n >= 1:
                c0, n2 = offs[k - 1][i]
                assert n2 == n - 1
                Mb = A.b(n + 1)[np.ix_(rows, keep(n))]
                D[r0:r0 + len(rows), c0:c0 + len(keep(n))] += Mb
            if i >= 1:
                c0, n2 = offs[k - 1][i - 1]
                assert n2 == n + 1
                MB = A.Bop(n + 1)[np.ix_(rows, keep(n + 2))]
                D[r0:r0 + len(rows), c0:c0 + len(keep(n + 2))] += MB
        diffs[k] = D
    return diffs, dims, offs


def connes_complex_hc(A, top):
    """Over Q: HC_n = H_n of (Lambda^(x (n+1)) / Im(eps), b) (p. 81, the
    corrected degrees)."""
    def rk(M):
        return rank(M, QQ)
    dims, rkb = {}, {}
    E = {k: A.eps(k) for k in range(1, top + 3)}
    for n in range(top + 2):
        k = n + 1
        dims[n] = A.d ** k - rk(E[k])
    for n in range(1, top + 2):
        k = n + 1
        stacked = np.vstack([A.b(k), E[k - 1]])
        rkb[n] = rk(stacked) - rk(E[k - 1])
    rkb[0] = 0
    rkb[top + 2] = 0
    return [dims[n] - rkb[n] - rkb.get(n + 1, 0) for n in range(top + 1)]


def section_2_13():
    """Section 2.13: Connes' double complex, B, the Morita maps."""
    for A in algebras():
        for k in range(1, 5):
            N, E = A.N(k), A.eps(k)
            check(not (N @ E).any() and not (E @ N).any(),
                  'p. 81: N eps = eps N = 0 on Lambda^(x %d), %s' % (k, A.name))
            if k >= 2:
                # b eps = eps b' and b' N = N b (maps Lambda^(x k) ->
                # Lambda^(x (k-1)), row convention: x -> x @ M)
                check((A.eps(k) @ A.b(k) == A.bprime(k) @ A.eps(k - 1)).all(),
                      "p. 81: b eps = eps b', %s, k = %d" % (A.name, k))
                check((A.N(k) @ A.bprime(k) == A.b(k) @ A.N(k - 1)).all(),
                      "p. 81: b' N = N b, %s, k = %d" % (A.name, k))
            if k <= 3:
                B1, B2 = A.Bop(k), A.Bop(k + 1)
                check(not (B1 @ B2).any(), 'B^2 = 0, %s, k = %d' % (A.name, k))
                check(not (B1 @ A.b(k + 1) + A.b(k) @ A.Bop(k - 1)).any()
                      if k >= 2 else not (B1 @ A.b(k + 1)).any(),
                      'b B + B b = 0, %s, k = %d' % (A.name, k))
                # B maps degenerate tensors (e_0 after the first place) to
                # degenerate ones (p. 85)
                d = A.d
                deg = [r for r, t in enumerate(itertools.product(range(d),
                                                                 repeat=k))
                       if any(v == 0 for v in t[1:])]
                nondeg_out = [r for r, t in enumerate(itertools.product(
                    range(d), repeat=k + 1)) if all(v != 0 for v in t[1:])]
                check(not B1[np.ix_(deg, nondeg_out)].any(),
                      'p. 85: B is well defined on the reduced complex, %s, '
                      'k = %d' % (A.name, k))
    top = 3
    for A in algebras():
        diffs, dims, offs = cc_total(A, QQ, top)
        check(all(not (diffs[k] @ diffs[k - 1]).any()
                  for k in range(2, top + 2)),
              'p. 81: CC_*(%s) is a double complex (total d^2 = 0)' % A.name)
        hc_cc = homology_dims(diffs, dims, QQ, top)
        bd, bdims, boffs = b_total(A, top)
        hc_b = homology_dims(bd, bdims, QQ, top)
        rd, rdims, _ = b_total(A, top, reduced=True)
        hc_r = homology_dims(rd, rdims, QQ, top)
        hc_c = connes_complex_hc(A, top)
        check(hc_cc == hc_b == hc_r == hc_c,
              'HC_n(%s) (Q): CC_* = B_* = B-bar = Connes complex, n <= %d: %s'
              % (A.name, top, hc_cc))
        if A.name == 'k':
            check(hc_cc == [1, 0, 1, 0], 'HC_*(Q) = Q in even degrees')
            # the printed quotient of p. 81 is the homology in degree n - 1
            refuted(all(hc_cc[n] == hc_c[n - 1] for n in range(1, top + 1)),
                    'p. 81 printed: HC_n = H_(n-1) of the Connes complex')
        # the map B_* -> CC_* of p. 84 with the corrected place
        # (2i - 1, j - i + 1): x -> x + (-1)^n s_n N x
        F = {}
        for k in range(top + 2):
            Fm = np.zeros((bdims[k], dims[k]), dtype=np.int64)
            for i, (r0, n) in boffs[k].items():
                size = A.d ** (n + 1)
                c0 = offs[k][2 * i]
                Fm[r0:r0 + size, c0:c0 + size] = eye(size)
                if i >= 1:
                    c1 = offs[k][2 * i - 1]
                    Fm[r0:r0 + size, c1:c1 + A.d ** (n + 2)] = \
                        (-1) ** n * (A.N(n + 1) @ A.s(n + 1))
            F[k] = Fm
        ok = all((bd[k] @ F[k - 1] == F[k] @ diffs[k]).all()
                 for k in range(1, top + 2))
        check(ok, 'p. 84: x -> x + (-1)^n s_n N x, with (-1)^n s_n N x in '
              'place (2i - 1, j - i + 1), is a chain map B_* -> CC_*, %s'
              % A.name)
        check(all(rank(F[k], QQ) == bdims[k] for k in range(top + 2)),
              'p. 84: the map B_* -> CC_* is injective, %s' % A.name)
        # printed place (2i, j - i - 1): row j - i - 1 of column 2i holds
        # Lambda^(x (j - i)), but s_n N x has j - i + 2 tensor factors
        if A.name == 'M_2':
            refuted(any(n + 2 == n for n in range(top)),
                    'p. 84 printed place (2i, j - i - 1): it holds '
                    'Lambda^(x (j - i)), while s_n N x has j - i + 2 factors')
        # Connes sequence: the first two columns X_* have homology HH_*
        X = {}
        for k in range(1, top + 2):
            cols = [p for p in (0, 1) if p <= k]
            rows_k = sum(A.d ** (k - p + 1) for p in cols)
            colsk1 = [p for p in (0, 1) if p <= k - 1]
            X[k] = diffs[k][:rows_k, :sum(A.d ** (k - p) for p in colsk1)]
        xd = {k: sum(A.d ** (k - p + 1) for p in (0, 1) if p <= k)
              for k in range(top + 2)}
        hh = homology_dims({k: A.b(k + 1) for k in range(1, top + 2)},
                           {k: A.d ** (k + 1) for k in range(top + 2)},
                           QQ, top)
        check(homology_dims(X, xd, QQ, top) == hh,
              'p. 82: the first two columns of CC_*(%s) compute HH_*'
              % A.name)
    # over F_2 the rows are not exact (Z/(n+1)-homology), and HC differs from
    # the Connes complex: Lambda = F_2
    A = algebras()[0]
    diffs, dims, offs = cc_total(A, GF(2), 3)
    check(homology_dims(diffs, dims, GF(2), 3) == [1, 0, 1, 0],
          'p. 82: HC_*(F_2) from CC_*: F_2 in even degrees')
    # Theorem 2.13.2: HC_n(M_2(Q)) = HC_n(Q)
    k_, dual, T2, M2, C3 = algebras()
    h1 = homology_dims(*cc_total(M2, QQ, 3)[:2], QQ, 3)
    h0 = homology_dims(*cc_total(k_, QQ, 3)[:2], QQ, 3)
    check(h1 == h0, 'Theorem 2.13.2: HC_n(M_2(Q)) = HC_n(Q), n <= 3')
    morita_maps()


def morita_maps():
    """Proof of Theorem 2.13.2 for Lambda = M_2(Z), Gamma = Z, P = Z^2
    (columns), Q = Z^2 (rows), phi(p (x) q) = pq, psi(q (x) p) = qp; p_i the
    columns of a unimodular U, q_i the rows of U^-1 (s = 2); q'_1 = (1, 1),
    p'_1 = (2, -1)^T, q'_2 = (1, 1), p'_2 = (1, -1)^T (t = 2,
    sum q'_j p'_j = 1).  Exact integer arithmetic on Lambda^(x (n+1)),
    n <= 3."""
    M2, mats, coords = matrix_algebra(2)
    d = 4
    U = np.array([[2, 1], [1, 1]])
    Uinv = np.array([[1, -1], [-1, 2]])
    assert (U @ Uinv == np.eye(2)).all()
    p = [U[:, [i]] for i in range(2)]
    q = [Uinv[[i], :] for i in range(2)]
    qq = [np.array([[1, 1]]), np.array([[1, 1]])]
    pp = [np.array([[2], [-1]]), np.array([[1], [-1]])]
    assert sum(qq[j] @ pp[j] for j in range(2))[0, 0] == 1
    x = {(i, j): p[i] @ qq[j] for i in range(2) for j in range(2)}
    y = {(j, i): pp[j] @ q[i] for i in range(2) for j in range(2)}
    assert (sum(x[i, j] @ y[j, i] for i in range(2) for j in range(2))
            == np.eye(2)).all()

    def tensor(ms):
        v = np.array([1], dtype=np.int64)
        for M in ms:
            v = np.multiply.outer(v, coords(M)).reshape(-1)
        return v

    def basis_mats(k):
        for idx in itertools.product(range(d), repeat=k):
            yield idx, [mats[u] for u in idx]

    def op_matrix(k_in, k_out, f):
        Mx = np.zeros((d ** k_in, d ** k_out), dtype=np.int64)
        for r, (idx, ls) in enumerate(basis_mats(k_in)):
            Mx[r] = f(ls)
        return Mx

    def beta_alpha(ls):   # printed formula of p. 83
        n = len(ls) - 1
        out = np.zeros(d ** (n + 1), dtype=np.int64)
        for I in itertools.product(range(2), repeat=n + 1):
            for J in itertools.product(range(2), repeat=n + 1):
                out += tensor([y[J[k], I[k]] @ ls[k] @
                               x[I[(k + 1) % (n + 1)], J[(k + 1) % (n + 1)]]
                               for k in range(n + 1)])
        return out

    def alpha_then_beta(ls):   # beta_n(alpha_n(...)) from the definitions
        n = len(ls) - 1
        out = np.zeros(d ** (n + 1), dtype=np.int64)
        for I in itertools.product(range(2), repeat=n + 1):
            # alpha: Gamma = Z, the tensor is the product of the scalars
            a = 1
            for k in range(n + 1):
                a *= (q[I[k]] @ ls[k] @ p[I[(k + 1) % (n + 1)]])[0, 0]
            if a == 0:
                continue
            for J in itertools.product(range(2), repeat=n + 1):
                # beta(1 (x) ... (x) 1) times the scalar a
                out += a * tensor([pp[J[k]] @ qq[J[(k + 1) % (n + 1)]]
                                   for k in range(n + 1)])
        return out

    def h(ls, full):
        n = len(ls) - 1
        out = np.zeros(d ** (n + 2), dtype=np.int64)
        for mm in range(n + 1):
            r = n + 1 if full else mm + 1
            for I in itertools.product(range(2), repeat=r):
                for J in itertools.product(range(2), repeat=r):
                    ent = [ls[0] @ x[I[0], J[0]]]
                    for k in range(1, mm + 1):
                        ent.append(y[J[k - 1], I[k - 1]] @ ls[k] @ x[I[k], J[k]])
                    ent.append(y[J[mm], I[mm]])
                    ent += ls[mm + 1:]
                    out += (-1) ** mm * tensor(ent)
        return out
    ok_ba, ok_corr, ok_printed, ok_sign = True, True, True, True
    H = {}
    Hfull = {}
    for n in range(0, 4):
        BA = op_matrix(n + 1, n + 1, beta_alpha)
        ok_ba &= (BA == op_matrix(n + 1, n + 1, alpha_then_beta)).all()
        H[n] = op_matrix(n + 1, n + 2, lambda ls: h(ls, False))
        Hfull[n] = op_matrix(n + 1, n + 2, lambda ls: h(ls, True))
        bh = H[n] @ M2.b(n + 2)
        hb = M2.b(n + 1) @ H[n - 1] if n >= 1 else 0
        ok_corr &= (eye(d ** (n + 1)) - BA == bh + hb).all()
        ok_sign &= (BA - eye(d ** (n + 1)) == bh + hb).all()
        bhf = Hfull[n] @ M2.b(n + 2)
        hbf = M2.b(n + 1) @ Hfull[n - 1] if n >= 1 else 0
        ok_printed &= (BA - eye(d ** (n + 1)) == bhf + hbf).all() or \
            (eye(d ** (n + 1)) - BA == bhf + hbf).all()
    check(ok_ba, 'p. 83: beta_n alpha_n is given by the displayed formula '
          '(n <= 3)')
    check(ok_corr, 'p. 83: with the inner sum over (i_0..i_m), (j_0..j_m), '
          '1 - beta_n alpha_n = b h_n + h_(n-1) b (n <= 3)')
    refuted(ok_sign, 'p. 83 printed sign: beta_n alpha_n - 1 = b h_n + '
            'h_(n-1) b with the same h')
    refuted(ok_printed, 'p. 83 printed: inner sum over all (i_0..i_n), '
            '(j_0..j_n) (either sign)')
    # alpha, beta commute with b, b' and t (p. 83): alpha = trace of the
    # product (Gamma = Z)
    ok = True
    for n in range(1, 4):
        tr = op_matrix(n + 1, 1, lambda ls: np.array(
            [int(np.trace(np.linalg.multi_dot(ls) if len(ls) > 1
                          else ls[0]))]))
        trm = op_matrix(n, 1, lambda ls: np.array(
            [int(np.trace(np.linalg.multi_dot(ls) if len(ls) > 1
                          else ls[0]))]))
        Zb = (-1) ** 0 * sum((-1) ** i for i in range(n + 1))
        ok &= (M2.b(n + 1) @ trm == Zb * tr).all()
        ok &= (M2.t(n + 1) @ tr == tr).all()
    check(ok, 'p. 83: alpha (here the trace of the product) commutes with b '
          'and t_n (n <= 3)')


# --- Connes' category: morphisms [m] -> [n] are non-decreasing f: Z -> Z with
# f(x + m + 1) = f(x) + n + 1, up to adding a multiple of n + 1 (tau_n^(n+1)
# = 1).  A morphism is stored as (m, n, (f(0), ..., f(m))).

def ev(f, x):
    m, n, vals = f
    qd, r = divmod(x, m + 1)
    return vals[r] + qd * (n + 1)


def comp(g, f):
    """g o f for f: [m] -> [n], g: [n] -> [k]."""
    m, n, _ = f
    n2, k, _ = g
    assert n == n2
    return (m, k, tuple(ev(g, ev(f, x)) for x in range(m + 1)))


def same(f, g):
    m, n, a = f
    m2, n2, b = g
    if (m, n) != (m2, n2):
        return False
    diffs = {y - x for x, y in zip(a, b)}
    return len(diffs) == 1 and diffs.pop() % (n + 1) == 0


def delta(n, i):    # [n-1] -> [n], skips i
    return (n - 1, n, tuple(x if x < i else x + 1 for x in range(n)))


def sigma(n, i):    # [n+1] -> [n], repeats i
    return (n + 1, n, tuple(x if x <= i else x - 1 for x in range(n + 2)))


def tau(n, power=1):
    f = (n, n, tuple(range(n + 1)))
    for _ in range(power % (n + 1)):
        f = comp((n, n, tuple(x - 1 for x in range(n + 1))), f)
    return f


def section_2_14():
    """Section 2.14: cyclic objects, the free cyclic object S[1] |x| X."""
    # The relations of p. 86 hold in the model (contravariant: d_i = X(delta_i),
    # s_i = X(sigma_i), t_n = X(tau_n), so d_i t_n = t_(n-1) d_(i-1) reads
    # tau_n o delta_i = delta_(i-1) o tau_(n-1), etc.)
    ok = True
    for n in range(1, 8):
        for i in range(1, n + 1):
            ok &= same(comp(tau(n), delta(n, i)), comp(delta(n, i - 1),
                                                      tau(n - 1)))
            ok &= same(comp(tau(n), sigma(n, i)), comp(sigma(n, i - 1),
                                                      tau(n + 1)))
        ok &= same(comp(tau(n), delta(n, 0)), delta(n, n))
        ok &= same(comp(tau(n), sigma(n, 0)), comp(sigma(n, n), tau(n + 1, 2)))
        ok &= same(tau(n, n + 1), (n, n, tuple(range(n + 1))))
        ok &= not same(tau(n, 1), (n, n, tuple(range(n + 1))))
        # simplicial identities among the cofaces / codegeneracies
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if n >= 2:
                    ok &= same(comp(delta(n, j), delta(n - 1, i)),
                               comp(delta(n, i), delta(n - 1, j - 1)))
    check(ok, 'p. 86: the relations between d_i, s_i, t_n hold in the model '
          'of Connes\' category (n <= 7)')
    # "there are n arrows from a cyclically ordered set of size n to one of
    # size one" (p. 86)
    for n in range(1, 9):
        arrows = []
        for vals in itertools.product(range(-1, 3), repeat=n):
            if list(vals) != sorted(vals) or vals[-1] > vals[0] + 1:
                continue
            f = (n - 1, 0, vals)
            if not any(same(f, g) for g in arrows):
                arrows.append(f)
        check(len(arrows) == n, 'p. 86: %d arrows from a set of size %d to '
              'one of size one' % (n, n))
    # Example 4 (p. 87): d_i t_n^j = t_(n-1)^(j') d_(i'), s_i t_n^j =
    # t_(n+1)^(j') s_(i'), i.e. tau^j o delta_i = delta_(i') o tau^(j') and
    # tau^j o sigma_i = sigma_(i') o tau^(j')
    okd, oks, okp = True, True, True
    for n in range(1, 8):
        for j in range(n + 1):
            for i in range(n + 1):
                if i - j >= 0:
                    jd, idd = j, i - j
                else:
                    jd, idd = j - 1, i - j + n + 1
                okd &= same(comp(tau(n, j), delta(n, i)),
                            comp(delta(n, idd), tau(n - 1, jd)))
                if i - j >= 0:
                    js, is_ = j, i - j
                    okp &= True
                else:
                    js, is_ = j + 1, i - j + n + 1
                    okp &= same(comp(tau(n, j), sigma(n, i)),
                                comp(sigma(n, is_), tau(n + 1, j - 1)))
                oks &= same(comp(tau(n, j), sigma(n, i)),
                            comp(sigma(n, is_), tau(n + 1, js)))
        okd &= same(comp(tau(n, n), delta(n, n)), delta(n, 0))
    check(okd, 'p. 87, Example 4: the face maps of S[1] |x| X (n <= 7)')
    check(oks, 'p. 87, Example 4: s_i(t_n^j, x) = (t_(n+1)^(j+1), '
          's_(i-j+n+1) x) for i < j, and (t_(n+1)^j, s_(i-j) x) for i >= j')
    refuted(okp, 'p. 87 printed: s_i(t_n^j, x) = (t_(n+1)^(j-1), '
            's_(i-j+n+1) x) for i < j')
    # S[1] |x| Delta[2] with these formulas is a cyclic set (n <= 4); with the
    # printed degeneracies the relation s_0 t_n = t_(n+1)^2 s_n fails
    def simp(n):
        return list(itertools.combinations_with_replacement(range(3), n + 1))

    def d_(x, i):
        return x[:i] + x[i + 1:]

    def s_(x, i):
        return x[:i + 1] + x[i:]

    def D(n, jx, i):
        j, x = jx
        if j == n and i == n:
            return (0, d_(x, 0))
        if i - j >= 0:
            return (j, d_(x, i - j))
        return (j - 1, d_(x, i - j + n + 1))

    def S(n, jx, i, printed=False):
        j, x = jx
        if i - j >= 0:
            return (j, s_(x, i - j))
        return ((j - 1) if printed else (j + 1), s_(x, i - j + n + 1))

    def T(n, jx):
        j, x = jx
        return ((j + 1) % (n + 1), x)
    for printed in (False, True):
        ok = True
        for n in range(1, 5):
            for j in range(n + 1):
                for x in simp(n):
                    jx = (j, x)
                    tx = T(n, jx)
                    for i in range(1, n + 1):
                        ok &= D(n, tx, i) == T(n - 1, D(n, jx, i - 1))
                        ok &= S(n, tx, i, printed) == \
                            T(n + 1, S(n, jx, i - 1, printed))
                    ok &= D(n, tx, 0) == D(n, jx, n)
                    ok &= S(n, tx, 0, printed) == \
                        T(n + 1, T(n + 1, S(n, jx, n, printed)))
                    for i in range(n + 2):
                        for jj in range(n + 1):
                            sx = S(n, jx, jj, printed)
                            if i == jj or i == jj + 1:
                                ok &= D(n + 1, sx, i) == jx
        if printed:
            refuted(ok, 'p. 87 printed: S[1] |x| Delta[2] with t_(n+1)^(j-1) '
                    'in the degeneracies is a cyclic set')
        else:
            check(ok, 'p. 87: S[1] |x| Delta[2] is a cyclic set (cyclic '
                  'relations and d s = id, n <= 4)')
    # Proposition 2.14.1, proof (p. 90): the composite
    # sigma (x) x -> sum_i (-1)^(in) t^i (s_i x) against B on the reduced
    # complex of the cyclic set SG/G
    for src in ('CyclicGroup(IsPermGroup, 3)', 'SymmetricGroup(3)'):
        G = TG(src)
        okP, okC = True, True
        for n in range(0, 4):
            for x in normalised_basis(G, n):
                Bx = {y: c for y, c in sgg_B(G, x).items()
                      if not is_degenerate(G, y)}
                pr, co = {}, {}
                for i in range(n + 1):
                    y = sgg_degen(G, x, i)
                    yp = y
                    for _ in range(i):
                        yp = sgg_t(G, yp)
                    if not is_degenerate(G, yp):
                        pr[yp] = pr.get(yp, 0) + (-1) ** (i * n)
                    yc = y
                    for _ in range(n + 1 - i):
                        yc = sgg_t(G, yc)
                    if not is_degenerate(G, yc):
                        co[yc] = co.get(yc, 0) + (-1) ** (i * n)
                pr = {y: c for y, c in pr.items() if c}
                co = {y: (-1) ** n * c for y, c in co.items() if c}
                okP &= pr == Bx or pr == {y: -c for y, c in Bx.items()}
                okC &= co == Bx
        refuted(okP, 'p. 90 printed: sum_i (-1)^(in) t^i(s_i x) is +-B(x) on '
                'the reduced complex of SG/G, %s' % src)
        check(okC, 'p. 90: sum_i (-1)^(in) t_(n+1)^(n+1-i)(s_i x) = '
              '(-1)^n B(x) on the reduced complex of SG/G, %s, n <= 3' % src)
    # Warning on p. 88: |Hom(S[1], X)| -> Map(S^1, |X|).  For X = S[1] (not a
    # Kan complex) the vertices of Hom(S[1], S[1]) are the simplicial maps
    # S[1] -> S[1], determined by the image of sigma among the 1-simplices
    # with both faces * (s_0 * and sigma): two, so at most two components,
    # while Map(S^1, S^1) has one component for each degree.  For the Kan
    # complex X = NG (G = S_3) the components of Hom(S[1], NG) = SG/G
    # (Proposition 2.12.3) are the conjugacy classes, as for LBG.
    S1_1 = [('s0', '*'), ('sigma',)]
    faces = {('s0', '*'): ('*', '*'), ('sigma',): ('*', '*')}
    maps = [y for y in S1_1 if faces[y] == ('*', '*')]
    refuted(len(maps) > 2, 'p. 88 printed (any simplicial set X): '
            '|Hom(S[1], S[1])| ~ Map(S^1, S^1) (2 vertices against the '
            'components of all degrees)')
    G = TG('SymmetricGroup(3)')
    parent = list(range(G.N))

    def find(u):
        while parent[u] != u:
            u = parent[u]
        return u
    for g0 in range(G.N):
        for g1 in range(G.N):
            a, b = find(G.m(g0, g1)), find(G.m(g1, g0))   # d_0, d_1 of (g0, g1)
            if a != b:
                parent[a] = b
    comps = {find(u) for u in range(G.N)}
    check(len(comps) == len(G.classes()), 'p. 88 (X = NG Kan): pi_0 of '
          'Hom(S[1], NG) = SG/G is the set of conjugacy classes = pi_0(LBG), '
          'S_3')
    # H_*(E S^1 x_(S^1) point) = H_*(BS^1) = H_*(CP^oo): HC_*(k) = k in even
    # degrees (Section 2.13), and CP^2 has Z in degrees 0, 2, 4
    H = simplicial_complexes.ComplexProjectivePlane().homology()
    check([tuple(H[k].invariants()) for k in range(5)] ==
          [(), (), (0,), (), (0,)], 'H_*(CP^2): Z in degrees 2, 4 '
          '(reduced), as HC_*(k) = H_*(BS^1) in degrees <= 4')


def section_2_15():
    """Section 2.15: HC_n(kG) = sum over classes of H_n(B C-hat_G(g); k).
    For g = 1, C-hat = S^1 x G; for g != 1 with C_G(g) = <g> of order m,
    C-hat = (R x <g>)/~ = R/mZ = S^1.  Over a field
    H_n(BS^1 x BG) = sum_(i even) H_(n-i)(BG) (Kuenneth, H_*(CP^oo))."""
    cases = [('CyclicGroup(IsPermGroup, 2)', GF(2), 5),
             ('CyclicGroup(IsPermGroup, 2)', QQ, 5),
             ('CyclicGroup(IsPermGroup, 3)', GF(3), 5),
             ('CyclicGroup(IsPermGroup, 3)', QQ, 5),
             ('CyclicGroup(IsPermGroup, 5)', GF(5), 3),
             ('SymmetricGroup(3)', GF(2), 3),
             ('SymmetricGroup(3)', GF(3), 3),
             ('SymmetricGroup(3)', GF(5), 3)]
    for src, ring, top in cases:
        G = TG(src)
        lhs = group_hc(G, ring, top)
        hG = nerve_dims(G, list(range(G.N)), ring, top)
        rhs = [sum(hG[n - i] for i in range(0, n + 1, 2))
               for n in range(top + 1)]
        for g in G.classes():
            if g == G.one:
                continue
            C = G.centraliser_gens(g)
            powers, y = {G.one}, g
            while y != G.one:
                powers.add(y)
                y = G.m(y, g)
            assert set(C) == powers      # C_G(g) = <g>
            rhs = [r + (1 if n % 2 == 0 else 0) for n, r in enumerate(rhs)]
        check(lhs == rhs, 'Corollary 2.15.3 (i): dim HC_n(%s G) = sum over '
              'classes of dim H_n(B C-hat_G(g)), G = %s, n <= %d: %s'
              % (ring, src, top, lhs))
    # over Q (or F_p with p prime to |G| and p > n + 1): HC_n(kG) = k^(classes)
    # for n even, 0 for n odd (Section 2.13: QG semisimple)
    G = TG('SymmetricGroup(3)')
    check(group_hc(G, GF(7), 3) == [3, 0, 3, 0],
          'HC_n(F_7 S_3) = F_7^3 for n even, 0 for n odd (n <= 3)')


def main():
    section_2_11()
    section_2_11_groups()
    section_2_12()
    section_2_13()
    section_2_14()
    section_2_15()
    print('ok chapter-2b: %d checks' % COUNT[0])


if __name__ == '__main__':
    main()
