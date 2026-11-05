"""Exact checks of Chapter 7, Sections 7.4-7.5 (Sage, GAP through libgap).

Run: sage -python checks/sage/chapter-7b.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-7b: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 7,
Sections 7.4 "Symplectic and orthogonal groups" and 7.5 "Smith's theorem
and universal coefficient systems", printed pp. 243-249, and the Examples
(iii) of p. 242-243.  Our files: content/07-04-symplectic-orthogonal.typ,
content/07-05-smith-theorem.typ (Sections 7.1-7.3: chapter-7a.py, whose
conventions and helpers are repeated here).  Pages are printed pages;
labels are those of content/07-*.typ.  Expected values are the book's
statements read off the printed pages and the author's corrections as
applied in our text; where the printed text was corrected, the printed
reading is kept as a refuted check (`refuted`) beside the corrected one.

Symplectic groups are GAP's Sp(2n, q) with GAP's invariant form; the
orthogonal spaces of odd dimension are F_q^(2n+1) with q(v) = x_1 y_1 +
... + x_n y_n + t_0^2 (non-degenerate in every characteristic), and in
characteristic two also GAP's GO(2n+1, q) with its quadratic form.
H_0 of the tautological system is computed as the sum of the isotropic
(singular) points modulo the linear relations inside the isotropic
(singular) 2-spaces, and once as the colimit over the whole poset of
isotropic subspaces.  Modules of groups are GAP MeatAxe modules, the simple
ones obtained as the composition factors of the permutation module on the
cosets of a Sylow p-subgroup (every simple module M is a quotient, since
M^S != 0).  B_p(G) of a Chevalley group is computed as the set of the
O_p(H)^g for the parabolic subgroups H containing B = N_G(S) (the
Borel-Tits theorem of Section 6.8, th:borel-tits; for GL_3(F_2),
Sp_4(F_2) this gives the 35 and 75 radical subgroups found in
chapter-7a.py).  The parabolic subgroups containing B are the
intermediate subgroups of B < G (GAP's IntermediateSubgroups); a check
confirms that there are 2^r of them, r minimal.

What is checked:

section_7_4 (pp. 243-246):
  * Theorem 7.4.1 and Examples (iii), p. 242: H_0(F_M) for Sp_2n(F_q) and
    the natural map onto M: dim 2n for (n, q) = (2, 3), (2, 5), (2, 7),
    (3, 3) and 2n + 1 for (2, 2), (2, 4), (3, 2), (4, 2); for n = 1 the
    theorem fails unless q = 2 (Sp_2(F_q) has q + 1 isotropic points and no
    isotropic 2-space, dim H_0 = q + 1: refuted for q = 3, 4, 5), so the
    section needs n >= 2;
  * p. 244: the presentation by isotropic points and 2-spaces is the
    colimit over all non-zero isotropic subspaces (Sp_6(F_2), Sp_6(F_3));
  * in characteristic two (Sp_4(F_2), Sp_4(F_4), Sp_6(F_2)): the kernel k
    of H_0(F_M) -> M is a trivial module, the extension does not split
    (Examples (iii) (b)), and H_0(F_M) carries a unique invariant quadratic
    form, non-degenerate with radical k: the natural orthogonal module
    (p. 243);
  * the proof of Theorem 7.4.1 (i): the displayed identities for every
    z = x + y with (x, y) != 0 (Sp_4(F_3), Sp_4(F_5), Sp_6(F_3)); for n = 1
    no x' != 0 exists;
  * Theorem 7.4.2 for O_5(F_q), q = 2, 3, 4, 5, and O_7(F_2), O_7(F_3);
    the printed hypothesis n >= 1 is refuted for n = 1, q = 3, 4, 5 (a
    conic with q + 1 points, H_0 of dimension q + 1); the basis x_i, y_i,
    t with q(t) = 0 of the proof; Case 2 (open question): S meets X + Y in
    a line; read with z = x + y + lambda t the sentence fails (z^perp
    contains S); read with z = t it holds: t^perp has dimension 2n, and for
    every singular x + y + lambda t, lambda != 0, some S gives t^perp meet S
    = <w>, <w, t> singular meeting X + Y in a line and S = <s, w> -- except,
    in odd characteristic, the second singular point of the plane <t,
    (X + Y)^perp>, for which every S has t^perp meet S inside X + Y; that
    point is covered through another point of a singular 2-space through it
    (a gap of the printed sketch, not of the theorem);
  * the proof of Theorem 7.4.1 (ii) and Corollary 7.4.3 for GO(3, 2),
    GO(3, 4), GO(5, 2), GO(5, 4), GO(7, 2): the radical of b is a line on
    which q is non-zero, it is invariant, V/rad is a non-degenerate
    symplectic space preserved by the image, each vector of V/rad has
    exactly one singular preimage, the singular lifts span V, and
    O_(2n+1)(F_q) -> Sp_2n(F_q) is an isomorphism (orders equal, image of
    full order).

section_7_5_smith (pp. 246-248):
  * Theorem 7.5.1 (Smith) and Corollary 7.5.2 for GL_3(F_2), Sp_4(F_2),
    GL_4(F_2), GL_2(F_3), SL_2(F_4), SL_2(F_5), SL_2(F_7), SL_3(F_3),
    GL_2(F_5), SL_2(F_8): all simple modules over F_q (as many as the
    p-regular classes, all absolutely irreducible); M^(O_p(H)) is
    absolutely irreducible for all 2^r parabolic subgroups H >= B; simple
    modules are separated by the minimal parabolics; Examples (i): B/O_p(B)
    abelian p', fixed points of S one dimensional; Examples (ii) (q = 2):
    B = S, H/O_2(H) = S_3, the 2^r assignments of 1s and 2s all occur, the
    Steinberg module has 2s everywhere; SL_2(p), p = 5, 7: p simple modules,
    the symmetric powers of the natural module;
  * the numbers of simple modules (p-regular classes): q^(n-1) for
    SL_n(F_q) and (q - 1) q^(n-1) for GL_n(F_q) in 15 cases;
    |G : G'|_p' q^r in all 17 cases; |G : G'| q^r with G' the commutator
    subgroup of the finite group fails exactly for the non-perfect
    SL_2(F_2), SL_2(F_3), Sp_4(F_2) (not corrected: with G' the group of
    rational points of the derived algebraic group, as in the author's
    correction to p. 229, the formula holds); PGL_2(F_5) has 6 < 10;
  * simple modules of GL_2(F_q), q = 3, 4, 5, with isomorphic restrictions
    to SL_2(F_q) differ by a one dimensional module;
  * the Comment on A_7: a 20-dimensional absolutely simple module in
    characteristic two, Sylow 2-subgroup of order 8, self-normalising, with
    a fixed space of dimension > 1.  (J_4 is not checked.)

section_7_5_systems (pp. 248-249):
  * Lemma 7.5.3 for all pairs of simple modules of GL_3(F_2) and Sp_4(F_2)
    (equivariant morphisms of fixed point systems on B_2(G));
  * Proposition 7.5.4 for these groups (H_0(F_M) has a unique maximal
    submodule with quotient M), Lemma 7.5.7 (F_(M-hat) = F_M + F_J
    pointwise) and the step of the algorithm (the image of H_0(F_J) is a
    non-zero submodule of J);
  * p. 248 (open question): B_p^(1)(G) consists of the simplices of
    dimension r - 1 and r - 2 (r the semisimple rank) for GL_3(F_2),
    Sp_4(F_2) (r = 2) and GL_4(F_2) (r = 3); the printed "r and r - 1" is
    refuted; for r = 2, B_p^(1)(G) = B_p(G);
  * Definition 7.5.5 and Proposition 7.5.6 for GL_4(F_2) (rank 3, all 8
    simple modules): with the printed index set of Definition 7.2.2 (iii)
    the colimit defining U_M at the 65 vertices is over the empty set, with
    the corrected one it is not; U_M is a coefficient system on B_2(G),
    H_0(U_M) is the colimit of F_M over B_2^(1)(G), and it has a unique
    maximal submodule with quotient M.

Not established here: Smith's theorem, the counting statements or the
theorems of Section 7.4 beyond the listed groups; the second half of
Proposition 7.5.6 (Weyl modules); the Comment on J_4 and the Comment of
Ronan-Smith on minimum weight modules.  Nothing here compares our text
with the printed book.
"""
import itertools
import random
import sys
import time

from sage.all import (GF, QQ, PolynomialRing, VectorSpace, identity_matrix,
                      libgap, matrix, prod, vector)

SCOPE = 'chapter-7b'
COUNT = [0]
T0 = time.time()


def check(cond, what):
    """One check of a statement of the book; fails loudly."""
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    """The printed reading, kept beside the corrected one: it must fail."""
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def mat(K, nr, nc, entries=0):
    """Matrices over K (sparse in odd characteristic: dense products over
    GF(p), p odd, stop with SIGILL in the local OpenBLAS build)."""
    return matrix(K, nr, nc, entries, sparse=(K.characteristic() not in (0, 2)))


def ident(K, n):
    return mat(K, n, n, {(i, i): 1 for i in range(n)})


def stack_cols(K, m, cols):
    if not cols:
        return mat(K, m, 0)
    return mat(K, m, len(cols), [[c[i] for c in cols] for i in range(m)])


# ===========================================================================
# Posets and coefficient systems
# ===========================================================================


class Poset:
    """Finite poset on 0..n-1; up[i] = set of elements strictly above i
    (transitively closed)."""

    def __init__(self, n, up):
        self.n = n
        self.up = [frozenset(u) for u in up]
        self.down = [set() for _ in range(n)]
        for i in range(n):
            for j in self.up[i]:
                self.down[j].add(i)
        self.pairs = [(x, y) for x in range(n) for y in self.up[x]]
        self.covers = [(x, y) for (x, y) in self.pairs
                       if not any(z in self.up[x] for z in self.down[y])]

    def le(self, a, b):
        return a == b or b in self.up[a]

    def chains(self):
        out = {}

        def ext(c):
            out.setdefault(len(c) - 1, []).append(tuple(c))
            for y in self.up[c[-1]]:
                ext(c + [y])
        for x in range(self.n):
            ext([x])
        return out


def closure(n, rel):
    up = [set(b for (a, b) in rel if a == i) for i in range(n)]
    changed = True
    while changed:
        changed = False
        for i in range(n):
            new = set(up[i])
            for j in up[i]:
                new |= up[j]
            if new != up[i]:
                up[i] = new
                changed = True
    return up


def random_poset(n, prob=0.45):
    rel = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < prob]
    perm = list(range(n))
    random.shuffle(perm)
    return Poset(n, [set(perm[j] for j in u) for u in
                     [closure(n, rel)[perm.index(i)] for i in range(n)]])


class CS:
    """A coefficient system: dims[x], R[(y, x)] : F(y) -> F(x) for x < y;
    optional G-action: list of (perm, {x: matrix F(x) -> F(perm[x])})."""

    def __init__(self, P, K, dims, R, act=None):
        self.P, self.K, self.d, self.R, self.act = P, K, list(dims), R, act

    def r(self, y, x):
        if x == y:
            return ident(self.K, self.d[x])
        return self.R[(y, x)]

    def is_functor(self):
        P = self.P
        for x in range(P.n):
            for y in P.up[x]:
                for z in P.up[y]:
                    if self.r(y, x) * self.r(z, y) != self.r(z, x):
                        return False
        return True


def cs_subquotient(P, K, m, W, U=None, rho=None, perms=None):
    """F(x) = W_x / U_x for subspaces of K^m (column bases) with W_y <= W_x,
    U_y <= U_x for x <= y; restriction induced by the inclusions; rho[t] the
    matrices of the generators on K^m, perms[t] their permutations of P."""
    V = VectorSpace(K, m)
    comp, full = [], []
    for x in range(P.n):
        Wx = V.subspace([vector(K, c) for c in W[x].columns()])
        Ux = V.subspace([vector(K, c) for c in U[x].columns()]) if U is not None else V.subspace([])
        cur, C = Ux, []
        for b in Wx.basis():
            if b not in cur:
                C.append(b)
                cur = cur + V.subspace([b])
        comp.append(C)
        full.append(stack_cols(K, m, C + list(Ux.basis())))
    dims = [len(C) for C in comp]

    def coords(x, cols):
        if not cols:
            return mat(K, dims[x], 0)
        A = full[x].solve_right(stack_cols(K, m, cols))
        return A.matrix_from_rows(range(dims[x]))
    R = {}
    for (x, y) in P.pairs:
        R[(y, x)] = coords(x, comp[y])
    act = None
    if rho is not None:
        act = []
        for g, pi in zip(rho, perms):
            act.append((pi, {x: coords(pi[x], [g * c for c in comp[x]]) for x in range(P.n)}))
    F = CS(P, K, dims, R, act)
    F.comp = comp
    F.ambient = m
    return F


def cs_constant(P, K, m, rho=None, perms=None):
    W = [ident(K, m)] * P.n
    return cs_subquotient(P, K, m, W, None, rho, perms)


# --------------------------------------------------------------------------
# limits and colimits over subsets


def offsets(F, S):
    off, o = {}, 0
    for x in S:
        off[x] = o
        o += F.d[x]
    return off, o


def colim_data(F, S):
    """Quotient map Q (rows) of the sum over S onto colim_S F."""
    K, P = F.K, F.P
    off, tot = offsets(F, S)
    Sset = set(S)
    cols = []
    for x in S:
        for y in P.up[x]:
            if y in Sset:
                Rm = F.r(y, x)
                for j in range(F.d[y]):
                    c = {off[y] + j: K(1)}
                    for i in range(F.d[x]):
                        if Rm[i, j] != 0:
                            c[off[x] + i] = c.get(off[x] + i, K(0)) - Rm[i, j]
                    cols.append(c)
    Rel = mat(K, tot, len(cols), {(i, j): v for j, c in enumerate(cols) for i, v in c.items()})
    Q = Rel.transpose().right_kernel_matrix() if cols else ident(K, tot)
    Q = mat(K, Q.nrows(), tot, Q.dict())
    return off, tot, Q


def lim_data(F, S):
    """Basis (columns) of the compatible families over S."""
    K, P = F.K, F.P
    off, tot = offsets(F, S)
    Sset = set(S)
    rows = []
    for x in S:
        for y in P.up[x]:
            if y in Sset:
                Rm = F.r(y, x)
                for i in range(F.d[x]):
                    r = {off[x] + i: K(1)}
                    for j in range(F.d[y]):
                        if Rm[i, j] != 0:
                            r[off[y] + j] = r.get(off[y] + j, K(0)) - Rm[i, j]
                    rows.append(r)
    E = mat(K, len(rows), tot, {(i, j): v for i, r in enumerate(rows) for j, v in r.items()})
    Kb = E.right_kernel_matrix() if rows else ident(K, tot)
    Kb = mat(K, Kb.nrows(), tot, Kb.dict()).transpose()
    return off, tot, Kb


def colim_dim(F, S=None):
    S = list(range(F.P.n)) if S is None else S
    return colim_data(F, S)[2].nrows()


def lim_dim(F, S=None):
    S = list(range(F.P.n)) if S is None else S
    return lim_data(F, S)[2].ncols()


def embed(K, off_small, off_big, F, S_small, tot_big, v):
    w = mat(K, tot_big, 1)
    for x in S_small:
        for i in range(F.d[x]):
            w[off_big[x] + i, 0] = v[off_small[x] + i, 0]
    return w


def cs_pullback(f, X, Gs):
    K = Gs.K
    dims = [Gs.d[f[x]] for x in range(X.n)]
    R = {(y, x): Gs.r(f[y], f[x]) for (x, y) in X.pairs}
    return CS(X, K, dims, R)


def cs_shriek(f, X, Y, F, printed=False):
    """f_! F with f_! F(y) = colim over y\\f (corrected) or over f/y
    (printed); returns the system (corrected only) and eta_x."""
    K = F.K
    S = {}
    for y in range(Y.n):
        if printed:
            S[y] = [x for x in range(X.n) if Y.le(f[x], y)]
        else:
            S[y] = [x for x in range(X.n) if Y.le(y, f[x])]
    data = {y: colim_data(F, S[y]) for y in range(Y.n)}
    dims = [data[y][2].nrows() for y in range(Y.n)]
    if printed:
        return dims
    R = {}
    for (y, y2) in Y.pairs:            # y < y2: S[y2] in S[y]
        off2, tot2, Q2 = data[y2]
        off1, tot1, Q1 = data[y]
        cols = []
        for j in range(dims[y2]):
            e = mat(K, dims[y2], 1, {(j, 0): 1})
            s = Q2.solve_right(e)
            cols.append((Q1 * embed(K, off2, off1, F, S[y2], tot1, s)).column(0))
        R[(y2, y)] = stack_cols(K, dims[y], cols)
    eta = {}
    for x in range(X.n):
        off, tot, Q = data[f[x]]
        Ex = mat(K, tot, F.d[x], {(off[x] + i, i): 1 for i in range(F.d[x])})
        eta[x] = Q * Ex
    return CS(Y, K, dims, R), eta


def cs_star(f, X, Y, F, printed=False):
    K = F.K
    S = {}
    for y in range(Y.n):
        if printed:
            S[y] = [x for x in range(X.n) if Y.le(y, f[x])]
        else:
            S[y] = [x for x in range(X.n) if Y.le(f[x], y)]
    data = {y: lim_data(F, S[y]) for y in range(Y.n)}
    dims = [data[y][2].ncols() for y in range(Y.n)]
    if printed:
        return dims
    R = {}
    for (y, y2) in Y.pairs:            # y < y2: S[y] in S[y2]
        off2, tot2, K2 = data[y2]
        off1, tot1, K1 = data[y]
        proj = mat(K, tot1, K2.ncols())
        for x in S[y]:
            for i in range(F.d[x]):
                for j in range(K2.ncols()):
                    proj[off1[x] + i, j] = K2[off2[x] + i, j]
        R[(y2, y)] = K1.solve_right(proj) if K2.ncols() else mat(K, dims[y], 0)
    eps = {}
    for x in range(X.n):
        off, tot, Kb = data[f[x]]
        eps[x] = Kb.matrix_from_rows(range(off[x], off[x] + F.d[x]))
    return CS(Y, K, dims, R), eps


# --------------------------------------------------------------------------
# morphisms


def hom_system(F, G, equivariant=False, extra=None):
    """Equations (sparse matrix) for morphisms F -> G; unknown A_x (G.d[x] x
    F.d[x]) at offset off[x], row-major."""
    K, P = F.K, F.P
    off, tot = {}, 0
    for x in range(P.n):
        off[x] = tot
        tot += G.d[x] * F.d[x]

    def var(x, i, j):
        return off[x] + i * F.d[x] + j
    rows = []
    for (x, y) in P.covers:
        RF, RG = F.r(y, x), G.r(y, x)
        for i in range(G.d[x]):
            for j in range(F.d[y]):
                r = {}
                for k in range(F.d[x]):
                    if RF[k, j] != 0:
                        r[var(x, i, k)] = r.get(var(x, i, k), K(0)) + RF[k, j]
                for k in range(G.d[y]):
                    if RG[i, k] != 0:
                        r[var(y, k, j)] = r.get(var(y, k, j), K(0)) - RG[i, k]
                rows.append(r)
    if equivariant:
        for (piF, DF), (piG, DG) in zip(F.act, G.act):
            assert piF == piG
            for x in range(P.n):
                gx = piF[x]
                for i in range(G.d[gx]):
                    for j in range(F.d[x]):
                        r = {}
                        for k in range(F.d[gx]):
                            if DF[x][k, j] != 0:
                                r[var(gx, i, k)] = r.get(var(gx, i, k), K(0)) + DF[x][k, j]
                        for k in range(G.d[x]):
                            if DG[x][i, k] != 0:
                                r[var(x, k, j)] = r.get(var(x, k, j), K(0)) - DG[x][i, k]
                        rows.append(r)
    E = mat(K, len(rows), tot, {(i, j): v for i, r in enumerate(rows) for j, v in r.items() if v != 0})
    return E, off, tot


def hom_dim(F, G, equivariant=False):
    E, off, tot = hom_system(F, G, equivariant)
    return tot - E.rank()


def hom_basis(F, G):
    E, off, tot = hom_system(F, G)
    B = E.right_kernel_matrix()
    out = []
    for row in B.rows():
        out.append({x: mat(F.K, G.d[x], F.d[x],
                           [row[off[x] + i * F.d[x] + j] for i in range(G.d[x]) for j in range(F.d[x])])
                    for x in range(F.P.n)})
    return out


def flatten(F, G, phi):
    E, off, tot = hom_system(F, G)
    v = [F.K(0)] * tot
    for x in range(F.P.n):
        for i in range(G.d[x]):
            for j in range(F.d[x]):
                v[off[x] + i * F.d[x] + j] = phi[x][i, j]
    return E, vector(F.K, v)


# --------------------------------------------------------------------------
# G-modules: H_0 with its action; Hom_kG


def colim_module(F):
    """H_0(F) = colim F with the induced action of the generators."""
    K, P = F.K, F.P
    S = list(range(P.n))
    off, tot, Q = colim_data(F, S)
    c = Q.nrows()
    sec = Q.solve_right(ident(K, c)) if c else mat(K, tot, 0)
    acts = []
    for pi, D in F.act:
        A = mat(K, tot, tot)
        for x in S:
            gx = pi[x]
            for i in range(F.d[gx]):
                for j in range(F.d[x]):
                    if D[x][i, j] != 0:
                        A[off[gx] + i, off[x] + j] = D[x][i, j]
        acts.append(Q * A * sec)
    return Q, off, tot, acts


def lim_module(F):
    K, P = F.K, F.P
    S = list(range(P.n))
    off, tot, Kb = lim_data(F, S)
    acts = []
    for pi, D in F.act:
        A = mat(K, tot, tot)
        for x in S:
            gx = pi[x]
            for i in range(F.d[gx]):
                for j in range(F.d[x]):
                    if D[x][i, j] != 0:
                        A[off[gx] + i, off[x] + j] = D[x][i, j]
        acts.append(Kb.solve_right(A * Kb) if Kb.ncols() else mat(K, 0, 0))
    return Kb, acts


def homkg_dim(K, actsA, actsB):
    """dim Hom_kG(A, B) for modules given by the generator matrices."""
    a = actsA[0].ncols()
    b = actsB[0].nrows()
    rows = []
    for gA, gB in zip(actsA, actsB):
        for i in range(b):
            for j in range(a):
                r = {}
                for k in range(a):
                    if gA[k, j] != 0:
                        r[i * a + k] = r.get(i * a + k, K(0)) + gA[k, j]
                for k in range(b):
                    if gB[i, k] != 0:
                        r[k * a + j] = r.get(k * a + j, K(0)) - gB[i, k]
                rows.append(r)
    if a * b == 0:
        return 0
    E = mat(K, len(rows), a * b, {(i, j): v for i, r in enumerate(rows) for j, v in r.items() if v != 0})
    return a * b - E.rank()


# --------------------------------------------------------------------------
# homology on the order complex


def chain_homology(F, ring_dims=False):
    """dims of H_n of the order complex of F.P with the system F (chain
    x_0 < ... < x_n carries F(x_n)); returns ({n: dim C_n}, {n: dim H_n},
    boundary matrices)."""
    K, P = F.K, F.P
    ch = P.chains()
    blocks = {}
    for k, cs in ch.items():
        off, o = {}, 0
        for c in cs:
            off[c] = o
            o += F.d[c[-1]]
        blocks[k] = (off, o)
    D = {}
    for k in range(1, max(ch) + 1):
        offk, nk = blocks[k]
        offm, nm = blocks[k - 1]
        dd = {}
        for c in ch[k]:
            top = c[-1]
            for i in range(len(c)):
                face = c[:i] + c[i + 1:]
                Rm = F.r(top, face[-1])
                sgn = K((-1) ** i)
                for a in range(F.d[face[-1]]):
                    for b in range(F.d[top]):
                        if Rm[a, b] != 0:
                            key = (offm[face] + a, offk[c] + b)
                            dd[key] = dd.get(key, K(0)) + sgn * Rm[a, b]
        D[k] = mat(K, nm, nk, {kk: v for kk, v in dd.items() if v != 0})
    top = max(ch)
    rk = {k: D[k].rank() for k in D}
    dims = {k: blocks[k][1] for k in blocks}
    H = {k: dims[k] - rk.get(k, 0) - rk.get(k + 1, 0) for k in range(top + 1)}
    return dims, H, D


# ===========================================================================
# GAP helpers
# ===========================================================================

libgap.eval(r'''
BensonCh7Setup := function(G, p)
  local iso, Gp, gens, mats, all, B;
  iso := IsomorphismPermGroup(G);
  Gp := Image(iso);
  gens := GeneratorsOfGroup(Gp);
  mats := List(gens, x -> PreImagesRepresentative(iso, x));
  all := Filtered(Flat(List(ConjugacyClassesSubgroups(Gp), AsList)),
                  P -> Size(P) > 1 and IsPGroup(P) and PrimePGroup(P) = p);
  B := Filtered(all, P -> PCore(Normalizer(Gp, P), p) = P);
  return rec(Gp := Gp, iso := iso, gens := gens, mats := mats, S := all, B := B);
end''')
libgap.eval(r'''
BensonCh7Perms := function(L, gens)
  return List(gens, g -> List(L, P -> Position(L, P^g)));
end''')
libgap.eval(r'''
BensonCh7Up := function(L)
  return List(L, P -> Filtered([1..Length(L)], j -> Size(L[j]) > Size(P)
                                   and IsSubset(L[j], P)));
end''')
libgap.eval(r'''
BensonCh7Hom := function(Gp, gens, ms)
  return GroupHomomorphismByImagesNC(Gp, Group(ms), gens, ms);
end''')
libgap.eval(r'''
BensonCh7Fix := function(hom, P)
  local xs, d;
  xs := List(GeneratorsOfGroup(P), x -> Image(hom, x));
  xs := List(xs, m -> m - m^0);
  d := Length(xs[1]);
  return NullspaceMat(List([1..d], i -> Concatenation(List(xs, m -> m[i]))));
end''')
def MTX(name):
    return libgap.eval('MTX.' + name)


FAIL = libgap.eval('fail')
SETUP = libgap.eval('BensonCh7Setup')
PERMS = libgap.eval('BensonCh7Perms')
UPS = libgap.eval('BensonCh7Up')
HOM = libgap.eval('BensonCh7Hom')
FIX = libgap.eval('BensonCh7Fix')


def sage_mat(K, g):
    return mat(K, len(g), len(g[0]), [[K(x) for x in row] for row in g.sage()])


def rows_to_cols(K, m, rows):
    rows = [[K(x) for x in r] for r in rows.sage()] if len(rows) else []
    return stack_cols(K, m, [vector(K, r) for r in rows])


class GroupData:
    """A matrix group from GAP with its 2-subgroup posets B and S."""

    def __init__(self, gap_group, p, K):
        self.K, self.p = K, p
        self.rec = SETUP(gap_group, p)
        self.Gp = self.rec['Gp']
        self.gens = self.rec['gens']
        self.mats = [sage_mat(K, m) for m in self.rec['mats']]
        self.posets = {}
        for kind in ('B', 'S'):
            L = self.rec[kind]
            up = [[int(j) - 1 for j in u] for u in UPS(L)]
            perms = [[int(i) - 1 for i in pi] for pi in PERMS(L, self.gens)]
            self.posets[kind] = (L, Poset(len(L), up), perms)

    def fixed_system(self, kind, rho_rows):
        """F_M on B_2 or S_2 for the module with generator matrices
        rho_rows (Sage, acting on rows)."""
        K = self.K
        L, P, perms = self.posets[kind]
        hom = HOM(self.Gp, self.gens, [libgap(m) for m in rho_rows])
        m = rho_rows[0].nrows()
        W = [rows_to_cols(K, m, FIX(hom, L[i])) for i in range(P.n)]
        rho_cols = [g.transpose() for g in rho_rows]
        return cs_subquotient(P, K, m, W, None, rho_cols, perms), W


# ===========================================================================
# Section 7.4: isotropic and singular points and lines
# ===========================================================================


def normalize(v):
    for a in v:
        if a != 0:
            return v / a
    return v


def points_lines(K, m, b, Q=None):
    """Isotropic (b alternating) or singular (Q) points of K^m (normalised
    vectors) and the totally isotropic / singular 2-spaces through them,
    each line given by the indices of its q + 1 points."""
    V = VectorSpace(K, m)
    pts, index = [], {}
    for v in V:
        if v == 0 or (Q is not None and Q(v) != 0):
            continue
        w = normalize(v)
        w.set_immutable()
        if w not in index:
            index[w] = len(pts)
            pts.append(w)
    lines, seen = [], set()
    for i, p in enumerate(pts):
        for j in range(i + 1, len(pts)):
            u = pts[j]
            if b(p, u) != 0:
                continue
            L = V.subspace([p, u])
            key = tuple(tuple(r) for r in L.echelonized_basis_matrix().rows())
            if key in seen:
                continue
            seen.add(key)
            idx = set()
            for v in L:
                if v != 0:
                    w = normalize(v)
                    w.set_immutable()
                    idx.add(index[w])
            lines.append(sorted(idx))
    return pts, index, lines


def h0_points_lines(K, m, pts, lines):
    """H_0 of the tautological system = sum of the points / relations of the
    lines; returns (dim, quotient map Q (rows), rank of the natural map)."""
    rows = []
    for L in lines:
        a, c = L[0], L[1]
        B = matrix(K, [pts[a], pts[c]]).transpose()
        B = mat(K, m, 2, B.list())
        for j in L[2:]:
            co = B.solve_right(mat(K, m, 1, list(pts[j])))
            rows.append({j: K(1), a: -co[0, 0], c: -co[1, 0]})
    R = mat(K, len(rows), len(pts), {(i, j): v for i, r in enumerate(rows) for j, v in r.items() if v != 0})
    Qm = R.right_kernel_matrix()
    Qm = mat(K, Qm.nrows(), len(pts), Qm.dict())
    natural = mat(K, m, len(pts), [[pts[j][i] for j in range(len(pts))] for i in range(m)])
    return Qm.nrows(), Qm, natural.rank(), natural


def point_action(K, pts, index, g):
    """The action of g (rows) on the sum of the points: v_p g = c v_p'."""
    n = len(pts)
    A = mat(K, n, n)
    for i, p in enumerate(pts):
        w = p * g
        c = None
        for a in w:
            if a != 0:
                c = a
                break
        wn = w / c
        wn.set_immutable()
        A[index[wn], i] = c
    return A


def quadratic_invariants(K, acts):
    """Quadratic forms Q(x) = sum_{i <= j} c_ij x_i x_j with Q(A x) = Q(x)
    for the matrices A (column action)."""
    d = acts[0].nrows()
    mons = [(i, j) for i in range(d) for j in range(i, d)]
    pos = {mn: t for t, mn in enumerate(mons)}
    rows = []
    for A in acts:
        T = matrix(K, len(mons), len(mons))
        for (i, j) in mons:
            col = pos[(i, j)]
            for k in range(d):
                for l in range(d):
                    c = A[i, k] * A[j, l]
                    if c != 0:
                        T[pos[(min(k, l), max(k, l))], col] += c
        rows.append(T - identity_matrix(K, len(mons)))
    E = rows[0]
    for T in rows[1:]:
        E = E.stack(T)
    out = []
    for c in E.right_kernel().basis():
        C = matrix(K, d, d)
        for (i, j), t in pos.items():
            C[i, j] = c[t]
        out.append(C)
    return out


def section_7_4():
    # ---- Theorem 7.4.1 and Examples (iii) of p. 242 --------------------
    sp_cases = [(2, 3), (2, 5), (2, 7), (3, 3), (2, 2), (2, 4), (3, 2), (4, 2), (1, 2), (1, 3), (1, 4), (1, 5)]
    for n, q in sp_cases:
        K = GF(q, 'a') if q in (4, 8, 9) else GF(q)
        J = sage_mat(K, libgap.InvariantBilinearForm(libgap.Sp(2 * n, q))['matrix'])

        def b(u, v, J=J):
            return u * J * v
        pts, index, lines = points_lines(K, 2 * n, b)
        dim, Qm, nat, natural = h0_points_lines(K, 2 * n, pts, lines)
        what = 'Sp_%d(F_%d): dim H_0(F_M) = %d' % (2 * n, q, dim)
        if n >= 2:
            check(nat == 2 * n, 'Theorem 7.4.1: the natural map H_0(F_M) -> M is onto (%s)' % what)
            if q % 2:
                check(dim == 2 * n, 'Theorem 7.4.1 (i): H_0(F_M) = M in odd characteristic (%s)' % what)
            else:
                check(dim == 2 * n + 1, 'Theorem 7.4.1 (ii): 0 -> k -> H_0(F_M) -> M -> 0 in '
                      'characteristic two (%s)' % what)
            if n == 2:
                check(dim == (4 if q % 2 else 5),
                      'Examples (iii), p. 242: Sp_4(F_%d), H_0(F_M) %s' % (q, '= M' if q % 2 else 'of dim 5'))
        else:
            ok = (dim == 2) if q % 2 else (dim == 3)
            check(dim == q + 1, 'Theorem 7.4.1 for n = 1: Sp_2(F_%d) has q + 1 = %d isotropic points '
                  'and no isotropic 2-spaces, dim H_0(F_M) = %d' % (q, q + 1, dim))
            if q == 2:
                check(ok, 'Theorem 7.4.1 (ii) holds for Sp_2(F_2) (dim 3)')
            else:
                refuted(ok, 'Theorem 7.4.1 without n >= 2: Sp_2(F_%d), dim H_0(F_M) = %d, not %d'
                        % (q, dim, 2 if q % 2 else 3))

    # the presentation by points and lines is the colimit over all isotropic subspaces
    for n, q in [(3, 2), (3, 3)]:
        K = GF(q)
        J = sage_mat(K, libgap.InvariantBilinearForm(libgap.Sp(2 * n, q))['matrix'])
        V = VectorSpace(K, 2 * n)
        spaces = []
        for k in range(1, n + 1):
            for W in V.subspaces(k):
                Bm = W.basis_matrix()
                if (Bm * J * Bm.transpose()).is_zero():
                    spaces.append(W)
        vecs = [frozenset(tuple(v) for v in W) for W in spaces]
        dims = [W.dimension() for W in spaces]
        N = len(spaces)
        # reverse inclusion: x <= y iff W_y <= W_x, so F(y) = W_y -> F(x) = W_x
        up = [[j for j in range(N) if dims[j] < dims[i] and vecs[j] <= vecs[i]] for i in range(N)]
        P = Poset(N, up)
        Wc = [stack_cols(K, 2 * n, list(W.basis())) for W in spaces]
        T = cs_subquotient(P, K, 2 * n, Wc)
        full = colim_dim(T)
        bfun = (lambda u, v, J=J: u * J * v)
        pts, index, lines = points_lines(K, 2 * n, bfun)
        dim = h0_points_lines(K, 2 * n, pts, lines)[0]
        check(full == dim == (2 * n + (1 if q == 2 else 0)),
              'p. 244: H_0(F_M) over all %d isotropic subspaces of Sp_%d(F_%d) = sum of the isotropic '
              'points / relations of the isotropic 2-spaces (dim %d)' % (N, 2 * n, q, dim))

    # G-module structure in characteristic two: k trivial, non-split, orthogonal
    for n, q in [(2, 2), (2, 4), (3, 2)]:
        K = GF(q, 'a') if q == 4 else GF(q)
        G = libgap.Sp(2 * n, q)
        J = sage_mat(K, libgap.InvariantBilinearForm(G)['matrix'])
        gens = [sage_mat(K, g) for g in libgap.GeneratorsOfGroup(G)]
        bfun = (lambda u, v, J=J: u * J * v)
        pts, index, lines = points_lines(K, 2 * n, bfun)
        dim, Qm, nat, natural = h0_points_lines(K, 2 * n, pts, lines)
        sec = Qm.solve_right(ident(K, dim))
        acts = [Qm * point_action(K, pts, index, g) * sec for g in gens]
        nat_h0 = natural * sec                      # H_0 -> M (columns)
        ker = nat_h0.right_kernel_matrix()
        check(ker.nrows() == 1, 'Theorem 7.4.1 (ii): the kernel of H_0(F_M) -> M is one dimensional '
              '(Sp_%d(F_%d))' % (2 * n, q))
        kv = ker.row(0)
        check(all(A * kv == kv for A in acts), 'Theorem 7.4.1 (ii): G acts trivially on the kernel k '
              '(Sp_%d(F_%d))' % (2 * n, q))
        triv = [ident(K, 1) for _ in acts]
        check(homkg_dim(K, acts, triv) == 0,
              'Examples (iii) (b), p. 243: the extension 0 -> k -> H_0(F_M) -> M -> 0 does not split '
              '(Hom_kG(H_0(F_M), k) = 0, M irreducible) (Sp_%d(F_%d))' % (2 * n, q))
        forms = quadratic_invariants(K, acts)
        check(len(forms) == 1, 'p. 243: H_0(F_M) carries a G-invariant quadratic form, unique up to '
              'scalars (Sp_%d(F_%d))' % (2 * n, q))
        C = forms[0]
        Bq = C + C.transpose()
        rad = Bq.right_kernel_matrix()
        Qf = (lambda x, C=C: (x * C * x))
        check(rad.nrows() == 1 and Qf(rad.row(0)) != 0 and rad.row(0) in VectorSpace(K, dim).subspace([kv]),
              'p. 243 and Corollary 7.4.3: the form is non-degenerate, its radical is the trivial '
              'submodule k: H_0(F_M) is the natural orthogonal module of Sp_%d(F_%d) = O_%d(F_%d)'
              % (2 * n, q, 2 * n + 1, q))

    # Theorem 7.4.1 (i), the proof: the identities in odd characteristic
    for n, q in [(2, 3), (2, 5), (3, 3), (1, 3), (1, 5)]:
        K = GF(q)
        m = 2 * n
        Jb = mat(K, m, m)
        for i in range(n):
            Jb[i, n + i] = 1
            Jb[n + i, i] = -1

        def b(u, v):
            return (u.row() * Jb * v.column())[0, 0]
        E = VectorSpace(K, m).basis()
        Xs = VectorSpace(K, m).subspace(E[:n])
        Ys = VectorSpace(K, m).subspace(E[n:])
        cases = 0
        impossible = 0
        for x in Xs:
            for y in Ys:
                a = b(x, y)
                if a == 0:
                    continue
                xps = [xp for xp in Xs if xp != 0 and b(xp, y) == 0]
                if not xps:
                    impossible += 1
                    continue
                xp = xps[0]
                inv2 = ~K(2)
                x0, x0p = (x + xp) * inv2, (x - xp) * inv2
                # y0 in Y with (x0, y0) = 0 and (x0', y0) = a/2
                Am = mat(K, 2, n, [[b(x0, E[n + j]) for j in range(n)], [b(x0p, E[n + j]) for j in range(n)]])
                c = Am.solve_right(mat(K, 2, 1, [[0], [a / 2]]))
                y0 = sum(c[j, 0] * E[n + j] for j in range(n))
                y0p = y - y0
                ok = (x0 + x0p == x and x0 - x0p == xp and b(x0, y0) == 0 and b(x0p, y0p) == 0
                      and b(x0 + y0, x0p + y0p) == 0 and (x0 + y0) + (x0p + y0p) == x + y
                      and b(x0, y0p) == a / 2 and b(y0, x0p) == -a / 2)
                check(ok, 'Theorem 7.4.1 (i), proof: the displayed identities (Sp_%d(F_%d))' % (m, q))
                cases += 1
        if n >= 2:
            check(cases > 0 and impossible == 0, 'Theorem 7.4.1 (i), proof: x\' != 0 exists for every '
                  'z = x + y with (x, y) != 0 (Sp_%d(F_%d), %d cases)' % (m, q, cases))
        else:
            check(cases == 0 and impossible > 0, 'Theorem 7.4.1 (i), proof, n = 1: x\' in X with '
                  '(x\', y) = 0 is 0 (Sp_2(F_%d)), and then x_0 = x\'_0 admits no y_0' % q)

    # ---- Theorem 7.4.2 -------------------------------------------------
    def orth(q, n):
        K = GF(q, 'a') if q in (4, 8, 9) else GF(q)

        def Q(v):
            return sum(v[i] * v[n + i] for i in range(n)) + v[2 * n] ** 2

        def b(u, v):
            return Q(u + v) - Q(u) - Q(v)
        return K, Q, b
    for n, q in [(2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (1, 2), (1, 3), (1, 4), (1, 5)]:
        K, Q, b = orth(q, n)
        m = 2 * n + 1
        pts, index, lines = points_lines(K, m, b, Q)
        dim, Qm, nat, natural = h0_points_lines(K, m, pts, lines)
        what = 'O_%d(F_%d): dim H_0(F_V) = %d' % (m, q, dim)
        if n >= 2:
            check(dim == m and nat == m, 'Theorem 7.4.2 (n >= 2): H_0(F_V) -> V is an isomorphism (%s)' % what)
        elif q == 2:
            check(dim == m and nat == m, 'Theorem 7.4.2 for n = 1 holds for q = 2 (%s)' % what)
        else:
            check(dim == q + 1 and not lines, 'Theorem 7.4.2, n = 1: the q + 1 singular points of the '
                  'conic and no singular 2-spaces (%s)' % what)
            refuted(dim == m, 'Theorem 7.4.2 printed with (n >= 1): %s, not %d' % (what, m))

    # the basis of the proof, Case 1 and Case 2 (z read as t, and as x + y + lambda t)
    for n, q in [(2, 2), (2, 3), (2, 5), (3, 2)]:
        K, Q, b = orth(q, n)
        m = 2 * n + 1
        V = VectorSpace(K, m)
        E = V.basis()
        t = E[2 * n] + E[0] - E[n]
        check(Q(t) == 0 and all(Q(E[i]) == 0 for i in range(2 * n)) and
              all(b(E[i], E[n + j]) == (1 if i == j else 0) for i in range(n) for j in range(n)) and
              all(b(E[i], E[j]) == 0 for i in range(n) for j in range(n)) and
              all(b(E[n + i], E[n + j]) == 0 for i in range(n) for j in range(n)),
              'Theorem 7.4.2, proof: a basis x_i, y_i, t with X, Y isotropic, (x_i, y_j) = delta_ij, '
              'q(t) = 0 (O_%d(F_%d))' % (m, q))
        XY = V.subspace(E[:2 * n])

        def perp(u):
            return V.subspace(matrix(K, [[b(e, u) for e in E]]).right_kernel().basis())
        tperp = perp(t)
        check(tperp.dimension() == 2 * n, 'Theorem 7.4.2, Case 2: t^perp has dimension 2n (O_%d(F_%d))'
              % (m, q))
        pts, index, lines = points_lines(K, m, b, Q)
        through = {}
        for L in lines:
            for i in L:
                through.setdefault(i, []).append(L)
        t0 = E[2 * n]
        plane = V.subspace([t, t0])
        good = {}
        n_pairs = 0
        for i, v in enumerate(pts):
            if v in XY or V.subspace([v]) == V.subspace([t]):
                continue
            good[i] = False
            for L in through.get(i, []):
                S = V.subspace([pts[j] for j in L])
                n_pairs += 1
                check(S.intersection(XY).dimension() == 1,
                      'Theorem 7.4.2, Case 2: S meets X + Y in a line (O_%d(F_%d))' % (m, q))
                refuted(S.intersection(perp(v)).dimension() == 1,
                        'Theorem 7.4.2, Case 2, z read as x + y + lambda t: z^perp contains S, so '
                        'z^perp meets S in dimension 2, not 1 (O_%d(F_%d))' % (m, q))
                ts = S.intersection(tperp)
                if ts.dimension() == 1 and t not in S:
                    w = ts.basis()[0]
                    s = S.intersection(XY).basis()[0]
                    WT = V.subspace([w, t])
                    if (V.subspace([w, s]) == S and Q(w) == 0 and b(w, t) == 0
                            and WT.intersection(XY).dimension() == 1):
                        good[i] = True
        bad = [i for i in good if not good[i]]
        exceptional = [i for i in bad if pts[i] in plane]
        check(bad == exceptional and len(bad) == (0 if q % 2 == 0 else 1),
              'Theorem 7.4.2, Case 2 with z = t: for every singular x + y + lambda t (lambda != 0) other '
              'than <t> some S works (t^perp meets S in a line <w>, <w, t> singular, meeting X + Y in a '
              'line, S = <s, w>), except in odd characteristic the second singular point of <t, '
              '(X + Y)^perp> (O_%d(F_%d): %d exceptions, %d pairs (v, S))' % (m, q, len(bad), n_pairs))
        for i in bad:
            # the exception is covered through a third point of a line through it
            ok = any(good.get(j, False) for L in through[i] for j in L if j != i)
            check(ok, 'Theorem 7.4.2, Case 2: the exceptional point lies on a singular 2-space with '
                  'another point outside X + Y to which the argument applies (O_%d(F_%d))' % (m, q))

    # characteristic two: radical, unique singular lifts, Corollary 7.4.3
    for d, q in [(3, 2), (3, 4), (5, 2), (5, 4), (7, 2)]:
        K = GF(q, 'a') if q == 4 else GF(q)
        G = libgap.GO(d, q)
        C = sage_mat(K, libgap.InvariantQuadraticForm(G)['matrix'])
        gens = [sage_mat(K, g) for g in libgap.GeneratorsOfGroup(G)]
        Bq = C + C.transpose()
        rad = Bq.left_kernel()
        r = rad.basis()[0]
        Qf = (lambda x, C=C: (x * C * x))
        check(rad.dimension() == 1 and Qf(r) != 0,
              'Theorem 7.4.1 (ii), proof: the radical of b is one dimensional and q is non-zero on it '
              '(O_%d(F_%d))' % (d, q))
        V = VectorSpace(K, d)
        Tb = None
        for i in range(d):
            cand = [e for j, e in enumerate(V.basis()) if j != i]
            M = matrix(K, cand + [r])
            if M.rank() == d:
                Tb = M
                break
        lifts_ok = True
        singular_lifts = []
        for coords in VectorSpace(K, d - 1):
            base = sum((coords[j] * Tb.row(j) for j in range(d - 1)), V.zero())
            sl = [base + lam * r for lam in K if Qf(base + lam * r) == 0]
            if len(sl) != 1:
                lifts_ok = False
            singular_lifts.extend(sl)
        check(lifts_ok, 'Theorem 7.4.1 (ii), proof: each vector of the symplectic quotient has exactly '
              'one singular preimage (O_%d(F_%d))' % (d, q))
        check(V.subspace(singular_lifts).dimension() == d,
              'Corollary 7.4.3, proof: the singular lifts generate the orthogonal space (O_%d(F_%d))' % (d, q))
        # action on V / rad
        Ti = Tb.inverse()
        quo = [(Tb * g * Ti).matrix_from_rows_and_columns(range(d - 1), range(d - 1)) for g in gens]
        check(all((Tb * g * Ti).matrix_from_rows_and_columns([d - 1], range(d - 1)).is_zero()
                  for g in gens), 'Theorem 7.4.1 (ii), proof: the radical is invariant under the '
              'orthogonal group (O_%d(F_%d))' % (d, q))
        Bbar = (Tb * Bq * Tb.transpose()).matrix_from_rows_and_columns(range(d - 1), range(d - 1))
        check(Bbar.rank() == d - 1 and all(x * Bbar * x.transpose() == Bbar for x in quo),
              'Theorem 7.4.1 (ii), proof: V / rad is a non-degenerate symplectic space preserved by the '
              'image (O_%d(F_%d))' % (d, q))
        img = libgap.Group([libgap(x) for x in quo])
        check(libgap.Size(img) == libgap.Size(G) == libgap.Size(libgap.Sp(d - 1, q)),
              'Corollary 7.4.3: O_%d(F_%d) -> Sp_%d(F_%d) is an isomorphism (order %s)'
              % (d, q, d - 1, q, libgap.Size(G)))


# ===========================================================================
# Section 7.5
# ===========================================================================

libgap.eval(r'''
BensonCh7Smith := function(G, p, F)
  local S, B, inter, pars, minpars, perm, mods, homs, fixmod, res;
  S := SylowSubgroup(G, p);
  B := Normalizer(G, S);
  inter := List(IntermediateSubgroups(G, B).subgroups, x -> x);
  pars := Concatenation([B], inter, [G]);
  if inter = [] then minpars := [G];
  else minpars := Filtered(inter, H -> ForAll(inter, K -> K = H or not IsSubset(H, K)));
  fi;
  perm := List(GeneratorsOfGroup(G), g -> PermutationMat(Permutation(g,
            RightCosets(G, S), OnRight), Index(G, S), F));
  mods := List(MTX.CollectedFactors(GModuleByMats(perm, F)), x -> x[1]);
  homs := List(mods, m -> GroupHomomorphismByImagesNC(G, Group(MTX.Generators(m)),
            GeneratorsOfGroup(G), MTX.Generators(m)));
  fixmod := function(h, H)
    local xs, d, W, U;
    U := PCore(H, p);
    if Size(U) = 1 then
      return GModuleByMats(List(GeneratorsOfGroup(H), x -> Image(h, x)), F);
    fi;
    xs := List(GeneratorsOfGroup(U), x -> Image(h, x) - Image(h, x)^0);
    d := Length(xs[1]);
    W := NullspaceMat(List([1..d], i -> Concatenation(List(xs, m -> m[i]))));
    return GModuleByMats(List(GeneratorsOfGroup(H), n -> List(W * Image(h, n),
             r -> SolutionMat(W, r))), F);
  end;
  res := rec();
  res.mods := mods;
  res.nmods := Length(mods);
  res.dims := List(mods, MTX.Dimension);
  res.absirr := ForAll(mods, MTX.IsAbsolutelyIrreducible);
  res.npars := Length(pars);
  res.nminpars := Length(minpars);
  res.BmodS := [IsAbelian(B/S), Gcd(Size(B)/Size(S), p) = 1, B = S];
  res.fixS := List(homs, h -> MTX.Dimension(fixmod(h, B)));
  res.irr := ForAll(homs, h -> ForAll(pars, H -> MTX.IsAbsolutelyIrreducible(fixmod(h, H))));
  res.distinct := ForAll([1..Length(mods)], i -> ForAll([i+1..Length(mods)], j ->
      ForAny(minpars, H -> MTX.IsomorphismModules(fixmod(homs[i], H), fixmod(homs[j], H)) = fail)));
  res.assign := List(homs, h -> List(minpars, H -> MTX.Dimension(fixmod(h, H))));
  res.minquot := List(minpars, H -> [Size(H/PCore(H, p)), IsAbelian(H/PCore(H, p))]);
  res.preg := Number(ConjugacyClasses(G), c -> Order(Representative(c)) mod p <> 0);
  res.index := Size(G) / Size(DerivedSubgroup(G));
  return res;
end''')
SMITH = libgap.eval('BensonCh7Smith')
PREG = libgap.eval('function(G, p) return [Number(ConjugacyClasses(G), c -> Order(Representative(c)) '
                   'mod p <> 0), Size(G) / Size(DerivedSubgroup(G))]; end')


def ppart(n, p):
    n, r = int(n), 1
    while n % p == 0:
        n //= p
        r *= p
    return r


def perm_image(gap_group):
    return libgap.Image(libgap.IsomorphismPermGroup(gap_group))


def section_7_5_smith():
    # (name, GAP group, p, q, semisimple rank r, number of positive roots N)
    groups = [('GL_3(F_2)', 'GL(3,2)', 2, 2, 2, 3), ('Sp_4(F_2)', 'Sp(4,2)', 2, 2, 2, 4),
              ('GL_4(F_2)', 'GL(4,2)', 2, 2, 3, 6), ('GL_2(F_3)', 'GL(2,3)', 3, 3, 1, 1),
              ('SL_2(F_4)', 'SL(2,4)', 2, 4, 1, 1), ('SL_2(F_5)', 'SL(2,5)', 5, 5, 1, 1),
              ('SL_2(F_7)', 'SL(2,7)', 7, 7, 1, 1), ('SL_3(F_3)', 'SL(3,3)', 3, 3, 2, 3),
              ('GL_2(F_5)', 'GL(2,5)', 5, 5, 1, 1), ('SL_2(F_8)', 'SL(2,8)', 2, 8, 1, 1)]
    for name, s, p, q, r, N in groups:
        G = perm_image(libgap.eval(s))
        res = SMITH(G, p, libgap.GF(q))
        nm = int(res['nmods'])
        check(nm == int(res['preg']) and bool(res['absirr']),
              'Section 7.5: %s has %d absolutely irreducible modules over F_%d (= number of p-regular '
              'classes), all quotients of k[G/S]' % (name, nm, q))
        bms = [bool(x) for x in res['BmodS']]
        check(bms[0] and bms[1], 'Examples (i), p. 247: B = N_G(S) and B/O_p(B) is an abelian p\'-group (%s)'
              % name)
        check(all(int(x) == 1 for x in res['fixS']),
              'Examples (i), p. 247: the fixed points of a Sylow p-subgroup on every simple module are '
              'one dimensional (%s)' % name)
        check(int(res['npars']) == 2 ** r and int(res['nminpars']) == r,
              'Section 7.5: %s has 2^r = %d parabolic subgroups containing B, r = %d minimal ones'
              % (name, 2 ** r, r))
        check(bool(res['irr']), 'Theorem 7.5.1 (Smith), Corollary 7.5.2: M^(O_p(H)) is absolutely '
              'irreducible for every parabolic H >= B and every simple M (%s)' % name)
        check(bool(res['distinct']), 'Theorem 7.5.1 (Smith): non-isomorphic simple modules differ on '
              'some minimal parabolic (%s)' % name)
        if q == 2:
            assign = sorted(tuple(int(x) for x in a) for a in res['assign'])
            check(bms[2], 'Examples (ii), p. 247: for q = 2 the Borel subgroup is a Sylow 2-subgroup (%s)' % name)
            check(all(int(a[0]) == 6 and not bool(a[1]) for a in res['minquot']),
                  'Examples (ii): H / O_2(H) = SL_2(2) = S_3 for the minimal parabolics (%s)' % name)
            check(assign == sorted(itertools.product([1, 2], repeat=r)),
                  'Examples (ii): the assignments of 1s and 2s to the r = %d vertices are all different '
                  'and all occur: 2^r = %d simple modules (%s)' % (r, 2 ** r, name))
            dims = [int(x) for x in res['dims']]
            st = [i for i, d in enumerate(dims) if d == q ** N]
            check(len(st) == 1 and all(int(x) == 2 for x in res['assign'][st[0]]),
                  'Examples (ii): the Steinberg module (dim %d) carries a 2 on each vertex (%s)'
                  % (q ** N, name))
        if s.startswith('SL(2,') and q == p:
            dims = sorted(int(x) for x in res['dims'])
            check(dims == list(range(1, p + 1)), 'p. 247: SL_2(%d) has p simple modules of dimensions '
                  '1, ..., p' % p)
            # they are the symmetric powers of the natural module
            K = GF(p)
            nat = [sage_mat(K, libgap.PreImagesRepresentative(libgap.IsomorphismPermGroup(libgap.eval(s)), g))
                   for g in libgap.GeneratorsOfGroup(G)]
            R = PolynomialRing(K, 'X,Y')
            X, Y = R.gens()
            allsym = True
            for a in range(p):
                mons = [X ** (a - i) * Y ** i for i in range(a + 1)]
                mats = []
                for g in nat:
                    # row vector (X, Y) -> (X, Y) g
                    Xg = g[0, 0] * X + g[0, 1] * Y
                    Yg = g[1, 0] * X + g[1, 1] * Y
                    rows = []
                    for mn in mons:
                        f = mn.subs({X: Xg, Y: Yg})
                        rows.append([f.monomial_coefficient(m2) for m2 in mons])
                    mats.append(matrix(K, rows))
                gm = libgap.GModuleByMats([libgap(m) for m in mats], libgap.GF(p))
                found = any(MTX('IsomorphismModules')(gm, md) != FAIL for md in res['mods'])
                allsym = allsym and found
            check(allsym, 'p. 247: the simple modules of SL_2(%d) are the symmetric powers of the natural '
                  'module' % p)

    # numbers of simple modules: |G : G'| . q^r
    count_cases = [('SL_2(F_2)', 'SL(2,2)', 2, 2, 1), ('SL_2(F_3)', 'SL(2,3)', 3, 3, 1),
                   ('SL_2(F_4)', 'SL(2,4)', 2, 4, 1), ('SL_2(F_5)', 'SL(2,5)', 5, 5, 1),
                   ('SL_2(F_7)', 'SL(2,7)', 7, 7, 1), ('SL_2(F_8)', 'SL(2,8)', 2, 8, 1),
                   ('SL_2(F_9)', 'SL(2,9)', 3, 9, 1), ('SL_3(F_2)', 'SL(3,2)', 2, 2, 2),
                   ('SL_3(F_3)', 'SL(3,3)', 3, 3, 2), ('SL_4(F_2)', 'SL(4,2)', 2, 2, 3),
                   ('GL_2(F_3)', 'GL(2,3)', 3, 3, 1), ('GL_2(F_4)', 'GL(2,4)', 2, 4, 1),
                   ('GL_2(F_5)', 'GL(2,5)', 5, 5, 1), ('GL_2(F_7)', 'GL(2,7)', 7, 7, 1),
                   ('GL_3(F_3)', 'GL(3,3)', 3, 3, 2), ('Sp_4(F_2)', 'Sp(4,2)', 2, 2, 2),
                   ('Sp_4(F_3)', 'Sp(4,3)', 3, 3, 2)]
    fails = []
    for name, s, p, q, r in count_cases:
        G = perm_image(libgap.eval(s))
        preg, idx = [int(x) for x in PREG(G, p)]
        check(preg == (idx // ppart(idx, p)) * q ** r,
              'p. 247: %s has |G : G\'|_p\' q^r = %d simple modules' % (name, preg))
        if s.startswith('SL'):
            n = r + 1
            check(preg == q ** (n - 1), 'p. 247: %s has q^(n-1) = %d simple modules' % (name, q ** (n - 1)))
        if s.startswith('GL'):
            n = r + 1
            check(preg == (q - 1) * q ** (n - 1), 'p. 247: %s has (q-1) q^(n-1) = %d simple modules'
                  % (name, (q - 1) * q ** (n - 1)))
        if preg != idx * q ** r:
            fails.append(name)
    check(fails == ['SL_2(F_2)', 'SL_2(F_3)', 'Sp_4(F_2)'],
          'p. 247: with G\' the commutator subgroup of the finite group, |G : G\'| . q^r counts the '
          'simple modules except for the non-perfect SL_2(F_2), SL_2(F_3), Sp_4(F_2), where it counts '
          'the p\'-part of |G : G\'| only (%s)' % fails)
    preg, idx = [int(x) for x in PREG(perm_image(libgap.eval('PGL(2,5)')), 5)]
    check(preg == 6 and idx * 5 == 10, 'p. 247: PGL_2(F_5) is not of universal type: 6 < |G : G\'| q = 10')

    # modules with isomorphic restrictions to SL_2 differ by a one dimensional module
    tw = libgap.eval(r'''
function(G, p, F)
  local S, perm, mods, D, res, one, i, j, hom, restr;
  S := SylowSubgroup(G, p);
  perm := List(GeneratorsOfGroup(G), g -> PermutationMat(Permutation(g,
            RightCosets(G, S), OnRight), Index(G, S), F));
  mods := List(MTX.CollectedFactors(GModuleByMats(perm, F)), x -> x[1]);
  D := DerivedSubgroup(G);
  restr := function(m)
    local h;
    h := GroupHomomorphismByImagesNC(G, Group(MTX.Generators(m)), GeneratorsOfGroup(G), MTX.Generators(m));
    return GModuleByMats(List(GeneratorsOfGroup(D), x -> Image(h, x)), F);
  end;
  one := Filtered(mods, m -> MTX.Dimension(m) = 1);
  res := [];
  for i in [1..Length(mods)] do for j in [1..Length(mods)] do
    if MTX.IsomorphismModules(restr(mods[i]), restr(mods[j])) <> fail then
      Add(res, ForAny(one, l -> MTX.IsomorphismModules(TensorProductGModule(mods[i], l), mods[j]) <> fail));
    fi;
  od; od;
  return [Length(one), res];
end''')
    for name, s, p in [('GL_2(F_3)', 'GL(2,3)', 3), ('GL_2(F_5)', 'GL(2,5)', 5), ('GL_2(F_4)', 'GL(2,4)', 2)]:
        q = int(s.split(',')[1][:-1])
        none, res = tw(perm_image(libgap.eval(s)), p, libgap.GF(q))
        check(int(none) == q - 1 and all(bool(x) for x in res),
              'p. 247: simple modules of %s with isomorphic restrictions to SL_2 differ by one of the '
              '%d one dimensional modules (%d pairs)' % (name, q - 1, len(res)))

    # Comment p. 247-248: A_7 in characteristic two
    a7 = libgap.eval(r'''
function()
  local G, S, perm, mods, m20, h, xs, d;
  G := AlternatingGroup(7);
  S := SylowSubgroup(G, 2);
  perm := List(GeneratorsOfGroup(G), g -> PermutationMat(Permutation(g,
            RightCosets(G, S), OnRight), Index(G, S), GF(2)));
  mods := List(MTX.CollectedFactors(GModuleByMats(perm, GF(2))), x -> x[1]);
  m20 := Filtered(mods, m -> MTX.Dimension(m) = 20);
  h := GroupHomomorphismByImagesNC(G, Group(MTX.Generators(m20[1])), GeneratorsOfGroup(G),
         MTX.Generators(m20[1]));
  xs := List(GeneratorsOfGroup(S), x -> Image(h, x) - Image(h, x)^0);
  d := Length(xs[1]);
  return [Length(m20), MTX.IsAbsolutelyIrreducible(m20[1]), Size(S), Size(Normalizer(G, S)),
          Length(NullspaceMat(List([1..d], i -> Concatenation(List(xs, m -> m[i])))))];
end''')()
    n20, absirr, sS, nS, fix = [a7[i] for i in range(5)]
    check(int(n20) >= 1 and bool(absirr) and int(sS) == 8 and int(nS) == 8 and int(fix) > 1,
          'Comment p. 247: A_7 has a 20-dimensional absolutely simple module in characteristic two; '
          'its Sylow 2-subgroup has order 8, is self-normalising, and has %d > 1 fixed dimensions' % int(fix))


libgap.eval(r'''
BensonCh7Bp := function(G, p, F)
  local S, B, inter, pars, subs, H, U, els, keys, perm, mods;
  S := SylowSubgroup(G, p);
  B := Normalizer(G, S);
  inter := List(IntermediateSubgroups(G, B).subgroups, x -> x);
  pars := Concatenation([B], inter);
  subs := [];
  for H in pars do
    U := PCore(H, p);
    Append(subs, List(RightTransversal(G, H), t -> U^t));
  od;
  els := AsSSortedList(G);
  keys := List(subs, U -> List(AsList(U), x -> PositionSorted(els, x)));
  perm := List(GeneratorsOfGroup(G), g -> PermutationMat(Permutation(g,
            RightCosets(G, S), OnRight), Index(G, S), F));
  mods := List(MTX.CollectedFactors(GModuleByMats(perm, F)), x -> x[1]);
  return rec(subs := subs, keys := keys,
             gperm := List(GeneratorsOfGroup(G), g -> List(els, x -> PositionSorted(els, x^g))),
             mods := mods, gens := GeneratorsOfGroup(G));
end''')
BP = libgap.eval('BensonCh7Bp')
FIXALL = libgap.eval(r'''
function(G, gens, ms, subs)
  local h;
  h := GroupHomomorphismByImagesNC(G, Group(ms), gens, ms);
  return List(subs, U -> BensonCh7Fix(h, U));
end''')


class BpData:
    """B_p(G) as the O_p of the conjugates of the parabolic subgroups
    containing B (Borel-Tits, Section 6.8), with the simple modules."""

    def __init__(self, gap_group, p, K):
        self.K = K
        self.G = perm_image(gap_group)
        self.rec = BP(self.G, p, libgap.GF(K.order()))
        keys = [frozenset(int(i) for i in k) for k in self.rec['keys']]
        self.keys = keys
        n = len(keys)
        up = [[j for j in range(n) if len(keys[j]) > len(keys[i]) and keys[i] <= keys[j]] for i in range(n)]
        self.P = Poset(n, up)
        pos = {k: i for i, k in enumerate(keys)}
        self.perms = []
        for gp in self.rec['gperm']:
            gp = [int(i) for i in gp]
            self.perms.append([pos[frozenset(gp[i - 1] for i in k)] for k in keys])
        self.sizes = [len(k) for k in keys]
        self.mods = [[sage_mat(K, m) for m in MTX('Generators')(md)] for md in self.rec['mods']]
        self.gapmods = list(self.rec['mods'])

    def fixed_system(self, rho_rows, sub=None):
        K = self.K
        idx = list(range(self.P.n)) if sub is None else sub
        fx = FIXALL(self.G, self.rec['gens'], [libgap(m) for m in rho_rows],
                    [self.rec['subs'][i] for i in idx])
        m = rho_rows[0].nrows()
        W = [rows_to_cols(K, m, fx[t]) for t in range(len(idx))]
        if sub is None:
            P, perms = self.P, self.perms
        else:
            loc = {i: t for t, i in enumerate(idx)}
            P = Poset(len(idx), [set(loc[j] for j in self.P.up[i] if j in loc) for i in idx])
            perms = [[loc[pi[i]] for i in idx] for pi in self.perms]
        rho_cols = [g.transpose() for g in rho_rows]
        return cs_subquotient(P, K, m, W, None, rho_cols, perms), W, P


def gap_module(K, acts_cols):
    return libgap.GModuleByMats([libgap(A.transpose()) for A in acts_cols], libgap.GF(K.order()))


def head_check(K, acts_cols, target):
    """Unique maximal submodule, quotient isomorphic to target."""
    md = gap_module(K, acts_cols)
    maxs = MTX('BasesMaximalSubmodules')(md)
    if len(maxs) != 1:
        return False, md, None
    quo = MTX('InducedActionFactorModule')(md, maxs[0])
    return MTX('IsomorphismModules')(quo, target) != FAIL, md, maxs[0]


def section_7_5_systems():
    for name, gg in [('GL_3(F_2)', 'GL(3,2)'), ('Sp_4(F_2)', 'Sp(4,2)')]:
        K = GF(2)
        bd = BpData(libgap.eval(gg), 2, K)
        check(bd.P.n == (35 if name == 'GL_3(F_2)' else 75),
              'Section 6.8: B_2(%s) from the parabolic subgroups has %d elements' % (name, bd.P.n))
        systems = []
        for i, rho in enumerate(bd.mods):
            FM, W, P = bd.fixed_system(rho)
            systems.append(FM)
        nm = len(bd.mods)
        for i in range(nm):
            for j in range(nm):
                lhs = hom_dim(systems[i], systems[j], equivariant=True)
                rhs = 1 if i == j else 0
                check(lhs == rhs, 'Lemma 7.5.3: Hom_(Delta,G)(F_M, F_N) = Hom_kG(M, N) for simple M, N '
                      '(%s, dims %d, %d: %d)' % (name, bd.mods[i][0].nrows(), bd.mods[j][0].nrows(), lhs))
        # p. 248: B_p^(1)(G) and the dimensions of its simplices
        r = 2
        verts = [x for x in range(bd.P.n) if not bd.P.down[x]]
        top = max(bd.sizes)
        sylow = [x for x in range(bd.P.n) if bd.sizes[x] == top]
        below = set()
        for s in sylow:
            below |= set(y for y in bd.P.down[s] if not any(z in bd.P.down[s] for z in bd.P.up[y]))
        B1 = sorted(set(sylow) | below)
        dimsimp = sorted(set(len([v for v in verts if v == x or v in bd.P.down[x]]) - 1 for x in B1))
        check(dimsimp == [r - 2, r - 1], 'p. 248: B_p^(1)(%s) consists of the simplices of dimension '
              'r - 1 and r - 2 (r = %d): %s' % (name, r, dimsimp))
        refuted(dimsimp == [r - 1, r], 'p. 248 printed: "the simplices of dimension r and r - 1" (%s)' % name)
        check(len(B1) == bd.P.n, 'p. 248: for semisimple rank 2, B_p^(1)(G) = B_p(G) (%s), so U_M = F_M' % name)
        # Proposition 7.5.4 and Lemma 7.5.7
        for i, rho in enumerate(bd.mods):
            FM = systems[i]
            Qm, off, tot, acts = colim_module(FM)
            ok, md, maxsub = head_check(K, acts, bd.gapmods[i])
            dM = rho[0].nrows()
            check(ok, 'Proposition 7.5.4: H_0(F_M) (dim %d) has a unique maximal submodule with quotient '
                  'M (%s, dim M = %d)' % (Qm.nrows(), name, dM))
            if Qm.nrows() == dM:
                continue
            # Lemma 7.5.7 with N = M-hat
            Mhat = [sage_mat(K, m) for m in MTX('Generators')(md)]
            Jm = MTX('InducedActionSubmodule')(md, maxsub)
            Jrows = [sage_mat(K, m) for m in MTX('Generators')(Jm)]
            FN, _, _ = bd.fixed_system(Mhat)
            FJ, WJ, _ = bd.fixed_system(Jrows)
            check(all(FN.d[x] == FM.d[x] + FJ.d[x] for x in range(bd.P.n)),
                  'Lemma 7.5.7: F_(M-hat) = F_M + F_(J(M-hat)) (dimensions at all %d points; %s, dim M = %d, '
                  'dim M-hat = %d)' % (bd.P.n, name, dM, Qm.nrows()))
            # the image of H_0(F_J) -> M-hat lies in J and is non-zero
            offJ, totJ, QJ = colim_data(FJ, list(range(bd.P.n)))
            incl = mat(K, Jrows[0].nrows(), totJ)
            for x in range(bd.P.n):
                Bx = stack_cols(K, Jrows[0].nrows(), FJ.comp[x])
                for a in range(Bx.nrows()):
                    for c in range(Bx.ncols()):
                        incl[a, offJ[x] + c] = Bx[a, c]
            check(incl.rank() > 0, 'p. 249: the image of H_0(F_(J(M-hat))) -> M-hat is non-zero and lies in '
                  'J(M-hat) (%s, dim M = %d)' % (name, dM))
            if incl.rank() == Jrows[0].nrows():
                check(True, 'p. 249: one step: M-hat / image = M (%s, dim M = %d)' % (name, dM))

    # GL_4(F_2): semisimple rank 3, the universal coefficient system
    K = GF(2)
    bd = BpData(libgap.eval('GL(4,2)'), 2, K)
    check(bd.P.n == 695, 'GL_4(F_2): B_2(G) has 65 + 315 + 315 = 695 elements')
    r = 3
    verts = [x for x in range(bd.P.n) if not bd.P.down[x]]
    sdim = [len([v for v in verts if v == x or v in bd.P.down[x]]) - 1 for x in range(bd.P.n)]
    top = max(bd.sizes)
    sylow = [x for x in range(bd.P.n) if bd.sizes[x] == top]
    below = set()
    for s in sylow:
        below |= set(y for y in bd.P.down[s] if not any(z in bd.P.down[s] for z in bd.P.up[y]))
    B1 = sorted(set(sylow) | below)
    check(len(sylow) == 315 and len(B1) == 630, 'p. 248: B_2^(1)(GL_4(F_2)): 315 Sylow subgroups and the '
          '315 maximal points below them')
    check(sorted(set(sdim[x] for x in B1)) == [r - 2, r - 1],
          'p. 248: B_2^(1)(GL_4(F_2)) = the simplices of dimension r - 1 = 2 and r - 2 = 1')
    refuted(sorted(set(sdim[x] for x in B1)) == [r - 1, r],
            'p. 248 printed: "the simplices of dimension r and r - 1" (GL_4(F_2): no 3-simplices)')
    B1set = set(B1)
    outside = [y for y in range(bd.P.n) if y not in B1set]
    check(all(not [x for x in B1 if x in bd.P.down[y]] for y in outside) and
          all([x for x in B1 if x in bd.P.up[y]] for y in outside),
          'Definition 7.5.5: for each of the 65 points P of B_2(G) outside B_2^(1)(G) the printed index set '
          '{x in B^(1) : x <= P} of (i_G)_! is empty, the corrected {x >= P} is not')
    # Proposition 7.5.6: H_0(U_M) = colim over B^(1) of F_M (Lemma 7.2.3), unique maximal submodule
    for i, rho in enumerate(bd.mods):
        dM = rho[0].nrows()
        F1, W1, P1 = bd.fixed_system(rho, sub=B1)
        Qm, off, tot, acts = colim_module(F1)
        ok, md, maxsub = head_check(K, acts, bd.gapmods[i])
        check(ok, 'Proposition 7.5.6: H_0(U_M) (dim %d) has a unique maximal submodule with quotient M '
              '(GL_4(F_2), dim M = %d)' % (Qm.nrows(), dM))
        if dM == 4:
            FM, W, P = bd.fixed_system(rho)
            iF = cs_pullback(B1, P1, FM)
            UM, eta = cs_shriek(B1, P1, bd.P, iF)
            check(UM.is_functor() and colim_dim(UM) == Qm.nrows(),
                  'Definition 7.5.5 (corrected): U_M = (i_G)_! i_G^-1 F_M is a coefficient system on '
                  'B_2(GL_4(F_2)) with H_0(U_M) = colim over B^(1) (dim %d)' % Qm.nrows())
            Qf, offf, totf, actsf = colim_module(FM)
            ok2, _, _ = head_check(K, actsf, bd.gapmods[i])
            check(ok2 and Qf.nrows() == 4, 'Proposition 7.5.4 and Lusztig: H_0(F_V) = V for GL_4(F_2)')


def main():
    sections = [section_7_4, section_7_5_smith, section_7_5_systems]
    only = sys.argv[1:]
    for f in sections:
        if not only or f.__name__ in only:
            f()
    print('ok %s: %d checks (%.0f s)' % (SCOPE, COUNT[0], time.time() - T0))


if __name__ == '__main__':
    main()
