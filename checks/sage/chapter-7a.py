"""Exact checks of Chapter 7, Sections 7.1-7.3 (Sage, GAP through libgap).

Run: sage -python checks/sage/chapter-7a.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-7a: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 7 "Local
coefficients on subgroup complexes", Sections 7.1-7.3, printed pp. 237-243.
Our files: content/07-01-local-coefficients-def.typ,
content/07-02-coefficient-constructions.typ,
content/07-03-coefficient-homology.typ (Sections 7.4-7.5: chapter-7b.py).
Pages are printed pages; labels are those of content/07-*.typ.  Expected
values are the book's statements read off the printed pages and the
author's corrections ("Author's comments and corrections", 8 September
2010) as applied in our text; where the printed text was corrected, the
printed reading is kept as a refuted check (`refuted`) beside the corrected
one.

Conventions.  A coefficient system F on a finite poset X (Definition 7.1.1)
is stored by its dimensions and the matrices res_(y, x) : F(y) -> F(x) for
x < y (column vectors), so restriction maps go DOWN, as in the book.  GAP
matrix groups act on row vectors from the right; a G-module M is used with
column vectors and the transposed matrices, the subgroups are acted on by
P -> P^g = g^-1 P g, and m in M^P gives m g in M^(P^g) (the right-action
form of the author's correction on p. 238).  For G-equivariant systems the
G-action is given for the generators of G (permutation of X and the maps
g_* : F(x) -> F(gx)); morphisms commuting with the generators commute with
G.  colim (= H_0, Definition 7.2.1) is the quotient of the sum of the F(x)
by the relations u - res_(x', x)(u), lim (= H^0) the compatible families,
both over all pairs x < x' of the index set.  Homology (Section 7.3) is
computed on the order complex, the chain x_0 < ... < x_n carrying
F(x_n), with delta(u) = sum (-1)^i res(u) (Definition 7.3.1 and the
"usual process" of p. 238); for a building the simplices are the flags.
All linear algebra is exact over GF(2), GF(3), GF(4), GF(5) (sparse
matrices in odd characteristic) and Q.

The corrected Definition 7.2.2 used here (f : X -> Y a map of posets,
f/y = {x : f(x) <= y}, y\\f = {x : f(x) >= y}, Definition 6.5.1):
    f_* F(y) = lim over x in f/y,   f_! F(y) = colim over x in y\\f;
the printed one has y\\f for f_* and f/y for f_!.

What is checked, by section:

section_7_1 (pp. 237-239), G = GL_3(F_2), p = 2, and Sp_4(F_2):
  * the author's correction on p. 238 ("B_p(G) is the barycentric
    subdivision of the building of G"): B_2(G) (radical 2-subgroups,
    computed in GAP) is isomorphic as a G-poset to the poset of simplices
    (flags of proper non-zero subspaces, resp. totally isotropic subspaces)
    of the building by sigma -> O_2(Stab(sigma)) (35 and 75 elements); the
    printed reading ("B_p(G) is the building of G") is refuted: the building
    has 14 (resp. 30) vertices, |B_2(G)| has 35 (resp. 75); and (p. 244,
    "the smallest subspace in the corresponding flag ... is the fixed space
    of the O_p of the corresponding parabolic subgroup") the fixed space of
    O_2(Stab(sigma)) on the natural module is the smallest subspace of
    sigma, for every flag sigma;
  * the author's correction on p. 238 (m in M^P => g m in M^(g P g^-1)):
    for all 77 non-trivial 2-subgroups P and all 168 elements g, for the
    natural module, its dual and the permutation module on the 7 points;
    the fixed point systems are non-degenerate (Definition 7.1.4);
  * Examples (ii), p. 239: the permutation module on the 7 points of the
    projective plane is k + X with X indecomposable of dimension 6, a
    non-split extension of the two 3-dimensional simple modules (with the
    points the 1-spaces of the natural module V its submodule is V* and its
    quotient V; on the 7 lines it is 0 -> V -> X' -> V* -> 0 as printed: the
    two readings differ by the inverse-transpose automorphism); for every
    non-trivial 2-subgroup P the sequence of fixed points is short exact,
    and for the representatives of the 5 classes it is split as a sequence
    of N_G(P)-modules (X^P = A^P + C^P, MeatAxe); the sequence of fixed point
    coefficient systems is not split, on B_2(G) and on S_2(G), even without
    asking the splitting to commute with G;
  * "taking fixed points is left exact but not right exact" (p. 239):
    0 -> k -> F_2[Z/2] -> k -> 0.

section_7_2 (pp. 239-241):
  * Definition 7.2.1 and the Examples on p. 240: the colimit over
    {a > b, a > c} is the pushout and the limit over {w < u, w < v} the
    pullback (random systems over GF(2), GF(3));
  * the Exercise on p. 240 (left exactness of H^0, right exactness of H_0)
    on random short exact sequences of systems, with examples where H^0 is
    not right exact and H_0 not left exact;
  * Definition 7.2.2 and Lemma 7.2.3 (open question of the readers): with
    the corrected index sets, f_* F and f_! F are coefficient systems
    (transitivity checked) and the maps psi -> psi_f(x) o eta_x and
    psi -> eps_x o psi_f(x) are bijections Hom_Y(f_! F, G) ->
    Hom_X(F, f^-1 G) and Hom_Y(G, f_* F) -> Hom_X(f^-1 G, F), for 300
    random triples (X, Y, f) with random F, G over GF(2) and GF(3); the
    printed index sets are refuted: for f = id on X = {a, b < c} with F(c) =
    0, F(a) = F(b) = k, Lemma 7.2.3 (i) forces f_! F = F, but the printed
    colimit over f/c = X has dimension 2; with the printed sets the
    restriction maps of f_! F, f_* F would go up (y <= y' gives f/y in f/y'
    and y'\\f in y\\f);
  * the note in the proof of Lemma 7.2.3 ("if y = f(x_0) then the colimit
    is F(x_0)"): true for inclusions of subposets (random cases; x_0 is the
    least element of y\\f), false for f : {a, b} -> (pt), a, b
    incomparable, F = k (colimit k^2);
  * the Example "Frobenius reciprocity" and Proposition 7.2.4 for X a point
    map: dim Hom_X(F, kappa_M) = dim H_0(F) dim M and dim Hom_X(kappa_M, F)
    = dim M dim H^0(F) (random), and G-equivariantly for the fixed point
    systems F_M on B_2(GL_3(F_2)) and S_2(GL_3(F_2)): dim Hom_(X,G)(F_M,
    kappa_N) = dim Hom_kG(H_0(F_M), N), dim Hom_(X,G)(kappa_N, F_M) = dim
    Hom_kG(N, H^0(F_M)) for M in {V, V*, St}, N in {k, V, V*, St};
  * Proposition 7.2.6 (i) <=> (ii) for random inclusions and systems (both
    outcomes occur), the counit i_! i^-1 G -> G being the map induced by
    the res_(x, y), x >= y in X.

section_7_3 (pp. 242-243):
  * delta o delta = 0 and the Exercise on p. 242 (H_0(Delta; F) = colim F)
    for random systems and for the fixed point systems above;
  * the homology of a building with the tautological system (value the
    smallest subspace of a flag) equals that of its barycentric subdivision
    (SL_3(F_2), Sp_4(F_2)), and the fixed point system F_M of the natural
    module on |B_2(SL_3(F_2))| has the same dimensions as the tautological
    system (p. 244 statement used in Section 7.4);
  * Examples (i) (Solomon, Tits): H_i(kappa_M) = M (i = 0), M (x) St (i =
    r - 1), 0 otherwise, with r the SEMISIMPLE rank, r >= 2 (for r = 1 both
    cases would be i = 0; not computed); GL_3(F_2), GL_3(F_3), GL_4(F_2),
    Sp_4(F_2), Sp_4(F_3): H~_(r-1) has dimension q^N (N the number of
    positive roots) and the other reduced homology vanishes, over GF(p) and
    Q; for M the natural module of GL_3(F_2) the dimensions are 3, 24.  The
    reading "rank(G) = Lie rank" is refuted by GL_3(F_q) (Lie rank 3): its
    building is a graph, H_2 = 0, H_1 = St;
  * Examples (ii) (Lusztig): for SL_n(F_q) and the natural module M,
    H_0(F_M) = M via the natural map for n >= 3 (n = 3, q = 2, 3, 4, 5;
    n = 4, q = 2, 3; n = 5, q = 2), H_i(F_M) = 0 for 0 < i < n - 2, and
    H_(n-2)(F_M) has dimension (q - 1)(q^2 - 1)...(q^(n-1) - 1) != 0; for
    n = 2, H_0(F_M) has dimension q + 1.  The printed reading
    "H_i(F_M) = 0 for i != 0" is refuted (for n = 3, q = 2 already by the
    Euler characteristic 21 - 21 = 0 != 3).
  * the Example on p. 243: the natural map H_0(F_M) -> M is onto iff
    H_0(kappa_M / F_M) = 0 (both computed independently) for the simple
    modules k, V, V*, St of GL_3(F_2) (generated by fixed points, as the
    Example says), the permutation modules on the points and on G/B
    (generated) and the projective module F_2[G/C_7] (not generated: its
    fixed points lie in the augmentation kernel).

Not established here: anything about all posets, maps or groups beyond the
listed cases; the theorems of Solomon-Tits and Lusztig in general.
Nothing here compares our text with the printed book.
"""
import itertools
import random
import sys
import time

from sage.all import (GF, QQ, VectorSpace, identity_matrix, libgap, matrix,
                      prod, vector)

SCOPE = 'chapter-7a'
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
# Buildings of SL_n, Sp_2n as posets of subspaces
# ===========================================================================


def subspace_poset(K, n, maxdim, form=None):
    V = VectorSpace(K, n)
    spaces = []
    for k in range(1, maxdim + 1):
        for W in V.subspaces(k):
            if form is not None:
                B = W.basis_matrix()
                if not (B * form * B.transpose()).is_zero():
                    continue
            spaces.append(W)
    vecs = [frozenset(tuple(v) for v in W) for W in spaces]
    dims = [W.dimension() for W in spaces]
    N = len(spaces)
    up = [[j for j in range(N) if dims[j] > dims[i] and vecs[i] <= vecs[j]] for i in range(N)]
    return spaces, Poset(N, up)


def taut_on_flags(K, n, spaces, P):
    """The tautological system on the building realised as the order complex
    of the subspace poset ordered by REVERSE inclusion (value at the top of a
    chain = the smallest subspace of the flag)."""
    rev = Poset(P.n, [P.down[i] for i in range(P.n)])
    W = [stack_cols(K, n, [vector(K, b) for b in spaces[i].basis()]) for i in range(P.n)]
    return cs_subquotient(rev, K, n, W)


def face_poset_system(K, n, spaces, P):
    """The same system on the barycentric subdivision: the poset of flags
    (simplices of the building) ordered by inclusion, F(flag) = smallest
    subspace."""
    flags = []
    for k, cs in P.chains().items():
        flags.extend(cs)
    idx = {fl: i for i, fl in enumerate(flags)}
    fs = [frozenset(fl) for fl in flags]
    up = [[j for j in range(len(flags)) if len(fs[j]) > len(fs[i]) and fs[i] <= fs[j]]
          for i in range(len(flags))]
    FP = Poset(len(flags), up)
    W = [stack_cols(K, n, [vector(K, b) for b in spaces[fl[0]].basis()]) for fl in flags]
    return cs_subquotient(FP, K, n, W), flags, idx


# ===========================================================================
# Section 7.1
# ===========================================================================


def section_7_1():
    K = GF(2)
    gd = GroupData(libgap.eval('GL(3,2)'), 2, K)
    L, B, permsB = gd.posets['B']
    LS, S, permsS = gd.posets['S']
    check(B.n == 35 and S.n == 77, 'GL_3(F_2): |B_2(G)| = 35, |S_2(G)| = 77')

    # the poset of simplices of the building (flags of proper subspaces)
    for name, gap_group, n, form in [
            ('GL_3(F_2)', 'GL(3,2)', 3, None),
            ('Sp_4(F_2)', 'Sp(4,2)', 4, 'Sp')]:
        g2 = gd if name == 'GL_3(F_2)' else GroupData(libgap.eval(gap_group), 2, K)
        LB, PB, _ = g2.posets['B']
        J = None
        if form == 'Sp':
            J = sage_mat(K, libgap.InvariantBilinearForm(libgap.eval(gap_group))['matrix'])
        spaces, Psub = subspace_poset(K, n, n - 1 if J is None else n // 2, J)
        flags = []
        for k, cs in Psub.chains().items():
            flags.extend(cs)
        # O_2 of the stabiliser of each flag (row vectors, right action)
        iso = g2.rec['iso']
        GG = libgap.eval(gap_group)
        stab_core = []
        for fl in flags:
            H = GG
            for i in fl:
                Wg = libgap([list(b) for b in spaces[i].basis()])
                H = libgap.Stabilizer(H, libgap.Immutable(libgap.SemiEchelonMat(Wg)['vectors']),
                                      libgap.eval('OnSubspacesByCanonicalBasis'))
            U = libgap.PCore(libgap.Image(iso, H), 2)
            stab_core.append(U)
        pos = [int(libgap.Position(LB, U)) - 1 for U in stab_core]
        check(sorted(pos) == list(range(PB.n)),
              'p. 238 (author): sigma -> O_2(Stab(sigma)) is a bijection from the simplices '
              'of the building of %s onto B_2(G) (%d elements)' % (name, PB.n))
        fs = [frozenset(fl) for fl in flags]
        ok = all((fs[a] < fs[b]) == (pos[b] in PB.up[pos[a]])
                 for a in range(len(flags)) for b in range(len(flags)))
        check(ok, 'p. 238 (author): the bijection is an isomorphism of posets (faces <-> '
              'subgroups), so |B_2(%s)| is the barycentric subdivision of the building' % name)
        # p. 244: the fixed space of O_p of the stabiliser of a flag is its smallest subspace
        hom_nat = HOM(g2.Gp, g2.gens, [libgap(m) for m in g2.mats])
        ok = True
        for fl, U in zip(flags, stab_core):
            Wfix = rows_to_cols(K, n, FIX(hom_nat, U))
            if Wfix.transpose().row_space() != spaces[fl[0]]:
                ok = False
        check(ok, 'p. 244: the fixed space of O_2(Stab(sigma)) on the natural module is the smallest '
              'subspace of the flag sigma, for all %d flags of %s' % (len(flags), name))
        nverts = len(spaces)
        refuted(nverts == PB.n,
                'p. 238 printed: "B_p(G) is the building of G" (%s: %d vertices of the building, '
                '%d elements of B_2(G))' % (name, nverts, PB.n))

    # modules: natural V, dual, permutation module on the 7 points
    V = gd.mats
    Vd = [g.inverse().transpose() for g in V]
    pts = [vector(K, v) for v in VectorSpace(K, 3) if v != 0]
    pkey = {tuple(v): i for i, v in enumerate(pts)}
    perm7 = []
    for g in V:
        A = mat(K, 7, 7)
        for i, v in enumerate(pts):
            A[i, pkey[tuple(v * g)]] = 1
        perm7.append(A)
    # all elements of G (as matrices, rows) to test the author's correction
    elts = [sage_mat(K, libgap.PreImagesRepresentative(gd.rec['iso'], x))
            for x in libgap.AsList(gd.Gp)]
    check(len(elts) == 168, '|GL_3(F_2)| = 168')
    conj = libgap.eval('function(L, x) return List(L, P -> Position(L, P^x)); end')
    elist = list(libgap.AsList(gd.Gp))
    for mname, rho in [('V', V), ('V*', Vd), ('F_2[points]', perm7)]:
        FM, W = gd.fixed_system('S', rho)
        check(all(d > 0 for d in FM.d),
              'Definition 7.1.4: F_M is non-degenerate on S_2(G) (M = %s)' % mname)
        hom = HOM(gd.Gp, gd.gens, [libgap(m) for m in rho])
        ok = True
        for x in elist:
            g = sage_mat(K, libgap.Image(hom, x))
            pi = [int(i) - 1 for i in conj(LS, x)]
            for i in range(S.n):
                img = (W[i].transpose() * g)          # rows m g, m in M^P
                Wt = W[pi[i]].transpose()
                if img.nrows() and not (Wt.row_space() == img.row_space()):
                    ok = False
        check(ok, 'p. 238 (author): m in M^P => m g in M^(P^g), with equality of the spaces, '
              'for all 77 P and 168 g (M = %s)' % mname)

    # Examples (ii), p. 239
    ones = vector(K, [1] * 7)
    Xb = [vector(K, [1 if j == i else (1 if j == 6 else 0) for j in range(7)]) for i in range(6)]
    T = matrix(K, Xb + [ones])
    check(T.rank() == 7, 'p. 239: F_2[points] = k (all-ones) + X (augmentation kernel)')
    Xm = []
    inv_ok = True
    for A in perm7:
        C = T * A * T.inverse()
        inv_ok = inv_ok and C.matrix_from_rows_and_columns([6], range(6)).is_zero() \
            and C.matrix_from_rows_and_columns(range(6), [6]).is_zero()
        Xm.append(C.matrix_from_rows_and_columns(range(6), range(6)))
    check(inv_ok, 'p. 239: the decomposition k + X is G-invariant')
    gX = libgap.GModuleByMats([libgap(m) for m in Xm], libgap.GF(2))
    gV = libgap.GModuleByMats([libgap(m) for m in V], libgap.GF(2))
    gVd = libgap.GModuleByMats([libgap(m) for m in Vd], libgap.GF(2))
    check(MTX('IsIndecomposable')(gX), 'p. 239: X is indecomposable of dimension 6')
    soc = MTX('BasesMinimalSubmodules')(gX)
    check(len(soc) == 1 and len(soc[0]) == 3, 'p. 239: X has a unique minimal submodule, of dim 3')
    sub = MTX('InducedActionSubmodule')(gX, soc[0])
    quo = MTX('InducedActionFactorModule')(gX, soc[0])
    sub_is_Vd = MTX('IsomorphismModules')(sub, gVd) != libgap.eval('fail')
    quo_is_V = MTX('IsomorphismModules')(quo, gV) != libgap.eval('fail')
    check(sub_is_Vd and quo_is_V,
          'p. 239: on the points of P(V) (V natural, row vectors): 0 -> V* -> X -> V -> 0, '
          'non-split (X indecomposable)')
    check(MTX('IsomorphismModules')(gV, gVd) == libgap.eval('fail'), 'p. 239: V, V* not isomorphic')
    # on the lines (the points of the dual plane) the sequence is as printed
    perm7l = [g.inverse().transpose() for g in V]
    lpts = [vector(K, v) for v in VectorSpace(K, 3) if v != 0]
    lperm = []
    for g in perm7l:
        A = mat(K, 7, 7)
        for i, v in enumerate(lpts):
            A[i, pkey[tuple(v * g)]] = 1
        lperm.append(A)
    Xl = []
    for A in lperm:
        C = T * A * T.inverse()
        Xl.append(C.matrix_from_rows_and_columns(range(6), range(6)))
    gXl = libgap.GModuleByMats([libgap(m) for m in Xl], libgap.GF(2))
    socl = MTX('BasesMinimalSubmodules')(gXl)
    subl = MTX('InducedActionSubmodule')(gXl, socl[0])
    check(len(socl) == 1 and MTX('IsomorphismModules')(subl, gV) != libgap.eval('fail'),
          'p. 239: on the 7 lines (points of the dual plane) 0 -> V -> X\' -> V* -> 0, as printed')

    # sub A and quotient C of X in Sage coordinates
    Asub = matrix(K, [[K(x) for x in r] for r in soc[0].sage()])     # 3 x 6 rows
    comp = [vector(K, e) for e in identity_matrix(K, 6).rows()]
    Cb = []
    cur = Asub.row_space()
    for e in comp:
        if e not in cur:
            Cb.append(e)
            cur = cur + VectorSpace(K, 6).subspace([e])
    Tx = matrix(K, list(Asub.rows()) + Cb)
    Cm = [(Tx * g * Tx.inverse()).matrix_from_rows_and_columns(range(3, 6), range(3, 6)) for g in Xm]
    proj = Tx.inverse().matrix_from_columns(range(3, 6))            # rows: v -> v Tx^-1, last 3
    split_ok = True
    exact_ok = True
    for kind in ('B', 'S'):
        Lk, Pk, permk = gd.posets[kind]
        FX, WX = gd.fixed_system(kind, Xm)
        FC, WC = gd.fixed_system(kind, Cm)
        FA, WA = gd.fixed_system(kind, [(Tx * g * Tx.inverse()).matrix_from_rows_and_columns(
            range(3), range(3)) for g in Xm])
        for i in range(Pk.n):
            if FX.d[i] != FA.d[i] + FC.d[i]:
                exact_ok = False
            img = WX[i].transpose() * proj
            if img.row_space() != WC[i].transpose().row_space():
                exact_ok = False
        check(exact_ok, 'p. 239: for every P in %s_2(G), 0 -> A^P -> X^P -> C^P -> 0 is exact' % kind)
        # sections s : F_C -> F_X with pi o s = id
        for equiv in (True, False):
            E, off, tot = hom_system(FC, FX, equivariant=equiv)
            rows, rhs = [], []
            for x in range(Pk.n):
                # pi_x : X^P -> C^P in coordinates
                Pi = WC[x].solve_right(proj.transpose() * WX[x])
                for i in range(FC.d[x]):
                    for j in range(FC.d[x]):
                        r = {}
                        for k in range(FX.d[x]):
                            if Pi[i, k] != 0:
                                r[off[x] + k * FC.d[x] + j] = Pi[i, k]
                        rows.append(r)
                        rhs.append(K(1) if i == j else K(0))
            Eaff = mat(K, len(rows), tot, {(i, j): v for i, r in enumerate(rows) for j, v in r.items()})
            full = E.stack(Eaff)
            b = vector(K, [K(0)] * E.nrows() + rhs)
            aug = full.augment(mat(K, len(b), 1, [[v] for v in b]))
            check(aug.rank() > full.rank(),
                  'p. 239: the sequence of fixed point coefficient systems on %s_2(G) is not '
                  'split (no %s section F_C -> F_X)' % (kind, 'G-equivariant' if equiv else
                                                       'section, even non-equivariant,'))
    # split as N_G(P)-modules
    splitfun = libgap.eval(r'''
function(Gp, gens, mX, mA, mC, P)
  local N, hX, hA, hC, fx, a, c, sm;
  N := Normalizer(Gp, P);
  hX := GroupHomomorphismByImagesNC(Gp, Group(mX), gens, mX);
  hA := GroupHomomorphismByImagesNC(Gp, Group(mA), gens, mA);
  hC := GroupHomomorphismByImagesNC(Gp, Group(mC), gens, mC);
  fx := function(h)
    local xs, d, W;
    xs := List(GeneratorsOfGroup(P), x -> Image(h, x) - Image(h, x)^0);
    d := Length(xs[1]);
    W := NullspaceMat(List([1..d], i -> Concatenation(List(xs, m -> m[i]))));
    return List(GeneratorsOfGroup(N), n -> List(W * Image(h, n), r -> SolutionMat(W, r)));
  end;
  a := fx(hA);
  c := fx(hC);
  sm := List([1..Length(a)], i -> DirectSumMat(a[i], c[i]));
  return MTX.IsomorphismModules(GModuleByMats(fx(hX), GF(2)),
                                GModuleByMats(sm, GF(2))) <> fail;
end''')
    mA = [(Tx * g * Tx.inverse()).matrix_from_rows_and_columns(range(3), range(3)) for g in Xm]
    reps = libgap.eval('function(Gp) return Filtered(List(ConjugacyClassesSubgroups(Gp), '
                       'Representative), P -> Size(P) > 1 and IsPGroup(P) and PrimePGroup(P) = 2); end')(gd.Gp)
    allsplit = all(bool(splitfun(gd.Gp, gd.gens, [libgap(m) for m in Xm], [libgap(m) for m in mA],
                                 [libgap(m) for m in Cm], P)) for P in reps)
    check(len(reps) == 5 and allsplit,
          'p. 239: for each of the 5 classes of non-trivial 2-subgroups P, X^P = A^P + C^P '
          'as N_G(P)-modules (split; Krull-Schmidt)')

    # fixed points: left exact, not right exact
    Kz = GF(2)
    g = mat(Kz, 2, 2, [[0, 1], [1, 0]])
    fix = (g - ident(Kz, 2)).left_kernel()
    check(fix.dimension() == 1 and fix.basis()[0] == vector(Kz, [1, 1]),
          'p. 239: F_2[Z/2]^(Z/2) = <(1, 1)> = k, the image of k -> F_2[Z/2]')
    check(vector(Kz, [1, 1]) * vector(Kz, [1, 1]) == 0,
          'p. 239: the augmentation F_2[Z/2] -> k kills the fixed points, so fixed points '
          'are not right exact')


# ===========================================================================
# Section 7.2
# ===========================================================================


def random_system(P, K, m=3):
    """A random subquotient system W/U on P (W_y <= W_x for x <= y)."""
    V = VectorSpace(K, m)
    order = sorted(range(P.n), key=lambda i: -len(P.down[i]))
    W, U = [None] * P.n, [None] * P.n
    for x in order:
        base = [b for y in P.up[x] for b in W[y].basis()]
        extra = [V.random_element() for _ in range(random.randint(0, 2))]
        W[x] = V.subspace(base + extra)
    for x in order:
        base = [b for y in P.up[x] for b in U[y].basis()]
        extra = [W[x].random_element() for _ in range(random.choice([0, 0, 1]))]
        U[x] = V.subspace(base + extra)
    Wc = [stack_cols(K, m, list(Wx.basis())) for Wx in W]
    Uc = [stack_cols(K, m, list(Ux.basis())) for Ux in U]
    return cs_subquotient(P, K, m, Wc, Uc)


def monotone_maps(X, Y, limit=4000):
    out = []
    for f in itertools.product(range(Y.n), repeat=X.n):
        if all(Y.le(f[x], f[y]) for (x, y) in X.pairs):
            out.append(list(f))
            if len(out) >= limit:
                break
    return out


def section_7_2():
    random.seed(7202)
    # pushout and pullback (p. 240)
    for K in (GF(2), GF(3)):
        Xpo = Poset(3, [set(), set(), {0, 1}][::-1] if False else [{2}, {2}, set()])  # b, c < a
        Xpb = Poset(3, [{1, 2}, set(), set()])                                     # w < u, v
        for _ in range(15):
            F = random_system(Xpo, K)
            a, b, c = 2, 0, 1
            stackm = F.r(a, b).stack(F.r(a, c))
            po = F.d[b] + F.d[c] - stackm.rank()
            check(colim_dim(F) == po, 'p. 240: colim over {a > b, a > c} is the pushout (%s)' % K)
            G = random_system(Xpb, K)
            w, u, v = 0, 1, 2
            pb = G.d[u] + G.d[v] - G.r(u, w).augment(-G.r(v, w)).rank()
            check(lim_dim(G) == pb, 'p. 240: lim over {w < u, w < v} is the pullback (%s)' % K)

    # Exercise p. 240: exactness
    seen = {'H0 not left': 0, 'H^0 not right': 0}
    for trial in range(60):
        K = random.choice([GF(2), GF(3)])
        P = random_poset(random.randint(3, 5))
        m = 3
        V = VectorSpace(K, m)
        # G a subspace system, F a sub-system, G/F the quotient
        order = sorted(range(P.n), key=lambda i: -len(P.down[i]))
        Wsub = [None] * P.n
        Wbig = [None] * P.n
        for x in order:
            base = [b for y in P.up[x] for b in Wbig[y].basis()]
            Wbig[x] = V.subspace(base + [V.random_element() for _ in range(random.randint(0, 2))])
        for x in order:
            base = [b for y in P.up[x] for b in Wsub[y].basis()]
            Wsub[x] = V.subspace(base + [Wbig[x].random_element() for _ in range(random.randint(0, 1))])
        Wb = [stack_cols(K, m, list(W.basis())) for W in Wbig]
        Ws = [stack_cols(K, m, list(W.basis())) for W in Wsub]
        Fs = cs_subquotient(P, K, m, Ws)
        Gs = cs_subquotient(P, K, m, Wb)
        Qs = cs_subquotient(P, K, m, Wb, Ws)
        # H^0: compatible families are families of vectors; maps induced by inclusion/quotient
        allS = list(range(P.n))
        offF, totF, KF = lim_data(Fs, allS)
        offG, totG, KG = lim_data(Gs, allS)
        offQ, totQ, KQ = lim_data(Qs, allS)

        def amb(Fx, off, Kb):   # families -> vectors in sum of ambient copies
            cols = []
            for j in range(Kb.ncols()):
                v = []
                for x in allS:
                    blk = Kb.matrix_from_rows(range(off[x], off[x] + Fx.d[x])).column(j)
                    v.extend(list(stack_cols(K, m, Fx.comp[x]) * blk) if Fx.d[x] else [K(0)] * m)
                cols.append(vector(K, v))
            return cols
        fF, fG = amb(Fs, offF, KF), amb(Gs, offG, KG)
        dimF, dimG, dimQ = KF.ncols(), KG.ncols(), KQ.ncols()
        # image of H^0 F in H^0 G is injective (families of vectors)
        Vbig = VectorSpace(K, m * P.n)
        imF = Vbig.subspace(fF)
        check(imF.dimension() == dimF, 'Exercise p. 240 (i): H^0 F -> H^0 G injective')
        # kernel of H^0 G -> H^0(G/F): families of G lying in F at every x
        kerdim = 0
        if dimG:
            rows = []
            for j in range(dimG):
                v = []
                for x in allS:
                    blk = KG.matrix_from_rows(range(offG[x], offG[x] + Gs.d[x])).column(j)
                    vec_amb = stack_cols(K, m, Gs.comp[x]) * blk if Gs.d[x] else vector(K, [0] * m)
                    # coordinates in W/U
                    if Qs.d[x]:
                        full = stack_cols(K, m, Qs.comp[x] + [vector(K, c) for c in Ws[x].columns()])
                        co = full.solve_right(vec_amb)
                        v.extend(list(co)[:Qs.d[x]])
                rows.append(v)
            Mq = matrix(K, rows) if rows and rows[0] else matrix(K, dimG, 0)
            kerdim = dimG - Mq.rank()
            imQdim = Mq.rank()
        else:
            imQdim = 0
        check(kerdim == dimF, 'Exercise p. 240 (i): exact at H^0 G')
        if imQdim < dimQ:
            seen['H^0 not right'] += 1
        # H_0: right exactness: H_0 F -> H_0 G -> H_0(G/F) -> 0
        h0F, h0G, h0Q = colim_dim(Fs), colim_dim(Gs), colim_dim(Qs)
        # image of H_0 F in H_0 G: rank of the induced map
        offF0, totF0, QF0 = colim_data(Fs, allS)
        offG0, totG0, QG0 = colim_data(Gs, allS)
        inc = mat(K, totG0, totF0)
        for x in allS:
            if Fs.d[x]:
                cx = Gs.comp[x]
                Bg = stack_cols(K, m, cx)
                co = Bg.solve_right(stack_cols(K, m, Fs.comp[x]))
                for i in range(co.nrows()):
                    for j in range(co.ncols()):
                        inc[offG0[x] + i, offF0[x] + j] = co[i, j]
        sec = QF0.solve_right(ident(K, QF0.nrows())) if QF0.nrows() else mat(K, totF0, 0)
        rk = (QG0 * inc * sec).rank() if QF0.nrows() else 0
        check(h0G - rk == h0Q, 'Exercise p. 240 (ii): H_0 G / im H_0 F = H_0(G/F) (right exact)')
        if rk < h0F:
            seen['H0 not left'] += 1
    check(seen['H^0 not right'] > 0,
          'Exercise p. 240: H^0 is not right exact in general (%d of 60 random cases)'
          % seen['H^0 not right'])
    # H_0 not left exact: three incomparable points, three lines F(x) in kappa = k^2
    K = GF(3)
    three = Poset(3, [set(), set(), set()])
    lines = [mat(K, 2, 1, [[1], [0]]), mat(K, 2, 1, [[0], [1]]), mat(K, 2, 1, [[1], [1]])]
    Fl = cs_subquotient(three, K, 2, lines)
    check(colim_dim(Fl) == 3 and colim_dim(cs_constant(three, K, 2)) == 6,
          'Exercise p. 240: on three points, H_0 of three lines in k^2 is k^3')
    Pt3 = Poset(4, [{3}, {3}, {3}, set()])     # the three lines below a point carrying k^2
    Fl3 = cs_subquotient(Pt3, K, 2, lines + [mat(K, 2, 0)])
    kap3 = cs_constant(Pt3, K, 2)
    check(colim_dim(Fl3) == 3 and colim_dim(kap3) == 2,
          'Exercise p. 240: H_0 is not left exact: F -> kappa injective, H_0 F = k^3 -> '
          'H_0 kappa = k^2')

    # Lemma 7.2.3 with the corrected Definition 7.2.2
    n_adj = n_nontriv = 0
    for trial in range(300):
        K = GF(2) if trial % 3 else GF(3)
        X = random_poset(random.randint(2, 5))
        Y = random_poset(random.randint(1, 4))
        maps = monotone_maps(X, Y)
        f = random.choice(maps)
        F = random_system(X, K, 3)
        G = random_system(Y, K, 3)
        fG = cs_pullback(f, X, G)
        sh, eta = cs_shriek(f, X, Y, F)
        st, eps = cs_star(f, X, Y, F)
        check(sh.is_functor() and st.is_functor(),
              'Definition 7.2.2 (corrected): f_! F, f_* F are coefficient systems')
        # (i)
        Bi = hom_basis(sh, G)
        dimL = hom_dim(F, fG)
        images = []
        for psi in Bi:
            phi = {x: psi[f[x]] * eta[x] for x in range(X.n)}
            E, v = flatten(F, fG, phi)
            check((E * v).is_zero(), 'Lemma 7.2.3 (i): psi_f(x) o eta_x is a morphism F -> f^-1 G')
            images.append(v)
        rk = matrix(K, images).rank() if images else 0
        check(rk == len(Bi) == dimL,
              'Lemma 7.2.3 (i): Hom_Y(f_! F, G) -> Hom_X(F, f^-1 G) bijective (dim %d)' % dimL)
        # (ii)
        Bii = hom_basis(G, st)
        dimR = hom_dim(fG, F)
        images = []
        for psi in Bii:
            phi = {x: eps[x] * psi[f[x]] for x in range(X.n)}
            E, v = flatten(fG, F, phi)
            check((E * v).is_zero(), 'Lemma 7.2.3 (ii): eps_x o psi_f(x) is a morphism f^-1 G -> F')
            images.append(v)
        rk = matrix(K, images).rank() if images else 0
        check(rk == len(Bii) == dimR,
              'Lemma 7.2.3 (ii): Hom_Y(G, f_* F) -> Hom_X(f^-1 G, F) bijective (dim %d)' % dimR)
        n_adj += 1
        if dimL > 0 and dimR > 0 and len(set(f)) < X.n:
            n_nontriv += 1
    check(n_adj == 300 and n_nontriv >= 50,
          'Lemma 7.2.3: 300 random triples, %d with f not injective and both Hom spaces non-zero'
          % n_nontriv)

    # the printed index sets
    K = GF(2)
    Vp = Poset(3, [{2}, {2}, set()])            # a, b < c
    W = [mat(K, 2, 1, [[1], [0]]), mat(K, 2, 1, [[0], [1]]), mat(K, 2, 0)]
    F = cs_subquotient(Vp, K, 2, W)
    ident_map = [0, 1, 2]
    sh, eta = cs_shriek(ident_map, Vp, Vp, F)
    check(sh.d == F.d, 'Lemma 7.2.3 (i), f = id: the corrected f_! F = F (dims %s)' % F.d)
    pr = cs_shriek(ident_map, Vp, Vp, F, printed=True)
    refuted(pr == F.d, 'Definition 7.2.2 (iii) printed (colim over f/y): for f = id on '
            '{a, b < c}, F(c) = 0, f_! F(c) has dim %d != 0 = dim F(c), against Lemma 7.2.3 (i)'
            % pr[2])
    Wc = [mat(K, 2, 2, [[1, 0], [0, 1]]), mat(K, 2, 2, [[1, 0], [0, 1]]), mat(K, 2, 1, [[1], [0]])]
    Vq = Poset(3, [set(), set(), {0, 1}])       # c < a, b
    Fq = cs_subquotient(Vq, K, 2, [mat(K, 2, 1, [[1], [0]]), mat(K, 2, 1, [[0], [1]]),
                                   mat(K, 2, 2, [[1, 0], [0, 1]])])
    st, eps = cs_star([0, 1, 2], Vq, Vq, Fq)
    check(st.d == Fq.d, 'Lemma 7.2.3 (ii), f = id: the corrected f_* F = F')
    prs = cs_star([0, 1, 2], Vq, Vq, Fq, printed=True)
    refuted(prs == Fq.d, 'Definition 7.2.2 (ii) printed (lim over y\\f): for f = id on '
            '{c < a, b}, F(c) = k^2, F(a), F(b) lines, the printed f_* F(c) has dim %d != 2'
            % prs[2])
    # with the printed sets the restriction maps go up
    Xc = Poset(2, [{1}, set()])
    fset = [0, 1]
    fy = {y: set(x for x in range(2) if Xc.le(fset[x], y)) for y in range(2)}
    yf = {y: set(x for x in range(2) if Xc.le(y, fset[x])) for y in range(2)}
    check(fy[0] < fy[1] and yf[1] < yf[0],
          'Definition 7.2.2: for y < y\', f/y is in f/y\' and y\'\\f in y\\f: a colimit over y\\f '
          'and a limit over f/y give maps F(y\') -> F(y) (restriction maps go down)')

    # the note in the proof: inclusions vs general maps
    for trial in range(60):
        K = GF(2) if trial % 2 else GF(3)
        Y = random_poset(random.randint(3, 6))
        Xs = sorted(random.sample(range(Y.n), random.randint(1, Y.n)))
        X = Poset(len(Xs), [set(Xs.index(j) for j in Y.up[i] if j in Xs) for i in Xs])
        F = random_system(X, K)
        sh, eta = cs_shriek(Xs, X, Y, F)
        for x0 in range(X.n):
            check(eta[x0].nrows() == eta[x0].ncols() == F.d[x0] and
                  (F.d[x0] == 0 or eta[x0].rank() == F.d[x0]),
                  'proof of Lemma 7.2.3: for an inclusion and y = f(x_0), colim over y\\f = F(x_0)')
    two = Poset(2, [set(), set()])
    pt = Poset(1, [set()])
    F2 = cs_subquotient(two, GF(2), 1, [ident(GF(2), 1), ident(GF(2), 1)])
    sh, eta = cs_shriek([0, 0], two, pt, F2)
    refuted(sh.d[0] == F2.d[0], 'proof of Lemma 7.2.3, "if y = f(x_0) then colim = F(x_0)" for a '
            'general map: f : {a, b} -> (pt), F = k: colim = k^%d' % sh.d[0])

    # Frobenius reciprocity (Proposition 7.2.4), trivial group
    for trial in range(40):
        K = GF(2) if trial % 2 else GF(3)
        X = random_poset(random.randint(2, 5))
        F = random_system(X, K)
        for mdim in (1, 2):
            kap = cs_constant(X, K, mdim)
            check(hom_dim(F, kap) == colim_dim(F) * mdim,
                  'Proposition 7.2.4 (i), trivial G: Hom_X(F, kappa_M) = Hom(H_0 F, M)')
            check(hom_dim(kap, F) == lim_dim(F) * mdim,
                  'Proposition 7.2.4 (ii), trivial G: Hom_X(kappa_M, F) = Hom(M, H^0 F)')

    # Proposition 7.2.6
    outcomes = set()
    for trial in range(80):
        K = GF(2) if trial % 2 else GF(3)
        Y = random_poset(random.randint(3, 6))
        Xs = sorted(random.sample(range(Y.n), random.randint(1, Y.n - 1)))
        X = Poset(len(Xs), [set(Xs.index(j) for j in Y.up[i] if j in Xs) for i in Xs])
        G = random_system(Y, K)
        iG = cs_pullback(Xs, X, G)
        sh, eta = cs_shriek(Xs, X, Y, iG)
        # counit at y: colim over {x in X : x >= y} of G(x) -> G(y), induced by res_(x, y)
        surj = True
        for y in range(Y.n):
            S = [i for i in range(X.n) if Y.le(y, Xs[i])]
            off, tot, Q = colim_data(iG, S)
            Mp = mat(K, G.d[y], tot)
            for i in S:
                Rm = G.r(Xs[i], y)
                for a in range(G.d[y]):
                    for b in range(G.d[Xs[i]]):
                        Mp[a, off[i] + b] = Rm[a, b]
            # Mp kills the relations, so it factors through Q
            sec = Q.solve_right(ident(K, Q.nrows())) if Q.nrows() else mat(K, tot, 0)
            check(Mp == Mp * sec * Q if Q.nrows() else Mp.is_zero(),
                  'Proposition 7.2.6: the counit is well defined on the colimit')
            if Mp.rank() < G.d[y]:
                surj = False
        cond = True
        for y in range(Y.n):
            if y in Xs:
                continue
            gens = [G.r(x, y) for x in Xs if Y.le(y, x)]
            span = mat(K, G.d[y], 0)
            for gm in gens:
                span = span.augment(gm)
            if span.rank() < G.d[y]:
                cond = False
        check(surj == cond, 'Proposition 7.2.6: (i) <=> (ii)')
        outcomes.add(cond)
    check(outcomes == {True, False}, 'Proposition 7.2.6: both outcomes occur among the random cases')

    # Proposition 7.2.4 G-equivariantly: GL_3(F_2) on B_2 and S_2
    K = GF(2)
    gd = GroupData(libgap.eval('GL(3,2)'), 2, K)
    V = gd.mats
    mods = {'k': [ident(K, 1) for _ in V], 'V': V, 'V*': [g.inverse().transpose() for g in V]}
    tens = [g.tensor_product(h) for g, h in zip(V, mods['V*'])]
    gT = libgap.GModuleByMats([libgap(m) for m in tens], libgap.GF(2))
    cf = [c for c in MTX('CompositionFactors')(gT) if int(MTX('Dimension')(c)) == 8]
    mods['St'] = [sage_mat(K, m) for m in MTX('Generators')(cf[0])]
    for kind in ('B', 'S'):
        Lk, Pk, permk = gd.posets[kind]
        for mname in ('V', 'V*', 'St'):
            FM, W = gd.fixed_system(kind, mods[mname])
            Q, off, tot, acts = colim_module(FM)
            Kb, lacts = lim_module(FM)
            for nname in ('k', 'V', 'V*', 'St'):
                rho = [g.transpose() for g in mods[nname]]
                kap = cs_constant(Pk, K, rho[0].nrows(), rho, permk)
                lhs = hom_dim(FM, kap, equivariant=True)
                rhs = homkg_dim(K, acts, rho)
                check(lhs == rhs, 'Proposition 7.2.4 (i), GL_3(F_2) on %s_2: Hom_(X,G)(F_%s, '
                      'kappa_%s) = Hom_kG(H_0(F_%s), %s) (dim %d)' % (kind, mname, nname, mname, nname, lhs))
                lhs2 = hom_dim(kap, FM, equivariant=True)
                rhs2 = homkg_dim(K, rho, lacts) if Kb.ncols() else 0
                check(lhs2 == rhs2, 'Proposition 7.2.4 (ii), GL_3(F_2) on %s_2: Hom_(X,G)(kappa_%s, '
                      'F_%s) = Hom_kG(%s, H^0(F_%s)) (dim %d)' % (kind, nname, mname, nname, mname, lhs2))
    return gd, mods


# ===========================================================================
# Section 7.3
# ===========================================================================


def section_7_3(gd, mods):
    random.seed(7303)
    for trial in range(40):
        K = GF(2) if trial % 2 else GF(3)
        P = random_poset(random.randint(2, 6))
        F = random_system(P, K)
        dims, H, D = chain_homology(F)
        for k in D:
            if k + 1 in D:
                check((D[k] * D[k + 1]).is_zero(), 'Section 7.3: delta_n o delta_(n+1) = 0')
        check(H[0] == colim_dim(F), 'Exercise p. 242: H_0(Delta; F) = colim F (random)')
    K = GF(2)
    for kind in ('B', 'S'):
        for mname in ('V', 'St'):
            FM, W = gd.fixed_system(kind, mods[mname])
            dims, H, D = chain_homology(FM)
            check(H[0] == colim_dim(FM), 'Exercise p. 242: H_0(Delta; F_%s) = colim F_%s on %s_2(GL_3(F_2))'
                  % (mname, mname, kind))

    # building vs barycentric subdivision; F_M on B_2 = tautological system
    for name, K, n, form in [('SL_3(F_2)', GF(2), 3, None), ('Sp_4(F_2)', GF(2), 4, 'Sp')]:
        J = None
        if form:
            J = sage_mat(K, libgap.InvariantBilinearForm(libgap.eval('Sp(4,2)'))['matrix'])
        spaces, Psub = subspace_poset(K, n, n - 1 if J is None else n // 2, J)
        T1 = taut_on_flags(K, n, spaces, Psub)
        d1, H1, _ = chain_homology(T1)
        T2, flags, idx = face_poset_system(K, n, spaces, Psub)
        d2, H2, _ = chain_homology(T2)
        check({k: v for k, v in H1.items() if v} == {k: v for k, v in H2.items() if v},
              'Section 7.3: the tautological system on the building of %s and on its barycentric '
              'subdivision have the same homology %s' % (name, H1))
    FV, W = gd.fixed_system('B', mods['V'])
    spaces, Psub = subspace_poset(GF(2), 3, 2)
    T2, flags, idx = face_poset_system(GF(2), 3, spaces, Psub)
    check(sorted(FV.d) == sorted(T2.d) and chain_homology(FV)[1] == chain_homology(T2)[1],
          'p. 244: F_V on B_2(SL_3(F_2)) is the tautological system (dims and homology agree)')

    # Examples (i): Solomon-Tits with the semisimple rank
    cases = [('GL_3(F_2)', GF(2), 3, None, 2, 3, 3), ('GL_3(F_3)', GF(3), 3, None, 2, 3, 3),
             ('GL_4(F_2)', GF(2), 4, None, 3, 6, 4), ('Sp_4(F_2)', GF(2), 4, 'Sp', 2, 4, 2),
             ('Sp_4(F_3)', GF(3), 4, 'Sp', 2, 4, 2)]
    for name, K, n, form, r, N, lie in cases:
        J = None
        if form:
            J = sage_mat(K, libgap.InvariantBilinearForm(libgap.eval('Sp(%d,%d)' % (n, K.order())))['matrix'])
        spaces, Psub = subspace_poset(K, n, n - 1 if J is None else n // 2, J)
        q = K.order()
        for KK in (K, QQ):
            kap = cs_constant(Psub, KK, 1)
            dims, H, D = chain_homology(kap)
            red = dict(H)
            red[0] -= 1
            nz = {k: v for k, v in red.items() if v}
            check(nz == {r - 1: q ** N},
                  'Examples (i), p. 242: %s (semisimple rank %d): reduced homology of |B_p(G)| over %s '
                  'is St = %d-dim in degree r - 1 = %d' % (name, r, KK, q ** N, r - 1))
            if lie != r:
                refuted(H.get(lie - 1, 0) == q ** N,
                        'Examples (i), p. 242, with rank(G) the Lie rank %d of %s: H_%d(kappa_k) = St'
                        % (lie, name, lie - 1))
        if name == 'GL_3(F_2)':
            kapM = cs_constant(Psub, GF(2), 3)
            dims, H, D = chain_homology(kapM)
            check(H == {0: 3, 1: 24}, 'Examples (i), p. 242: H_*(kappa_M), M natural of GL_3(F_2): '
                  'M in degree 0, M (x) St (dim 24) in degree 1')

    # Examples (ii): Lusztig
    for n, q in [(2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (3, 4), (3, 5), (4, 2), (4, 3), (5, 2)]:
        K = GF(q, 'a') if q == 4 else GF(q)
        spaces, Psub = subspace_poset(K, n, n - 1)
        T = taut_on_flags(K, n, spaces, Psub)
        dims, H, D = chain_homology(T)
        top = prod(q ** i - 1 for i in range(1, n))
        if n == 2:
            check(H == {0: q + 1}, 'Examples (ii), p. 242: SL_2(F_%d): H_0(F_M) has dim q + 1 = %d'
                  % (q, q + 1))
            continue
        # natural map H_0 -> M: sum of the inclusions, onto
        off, tot, Q = colim_data(T, list(range(T.P.n)))
        incl = mat(K, n, tot)
        for x in range(T.P.n):
            Bx = stack_cols(K, n, T.comp[x])
            for i in range(n):
                for j in range(T.d[x]):
                    incl[i, off[x] + j] = Bx[i, j]
        check(Q.nrows() == n and incl.rank() == n,
              'Examples (ii) (Lusztig), corrected: H_0(F_M) = M for SL_%d(F_%d) (natural map onto, '
              'dim %d)' % (n, q, n))
        mid = all(H[i] == 0 for i in range(1, n - 2))
        check(mid, 'Examples (ii), corrected: H_i(F_M) = 0 for 0 < i < n - 2 (SL_%d(F_%d))' % (n, q))
        check(H[n - 2] == top, 'Lusztig: H_(n-2)(F_M) has dim (q-1)...(q^(n-1)-1) = %d (SL_%d(F_%d))'
              % (top, n, q))
        refuted(all(H[i] == 0 for i in H if i != 0),
                'Examples (ii), p. 242, printed: H_i(F_M) = 0 for all i != 0 (SL_%d(F_%d): '
                'H_%d = %d)' % (n, q, n - 2, H[n - 2]))
    T = taut_on_flags(GF(2), 3, *subspace_poset(GF(2), 3, 2))
    dims, H, D = chain_homology(T)
    check(dims == {0: 21, 1: 21}, 'Examples (ii): for SL_3(F_2) the chain groups have dims 21, 21, '
          'so the Euler characteristic is 0 != dim M')

    # Example p. 243: generated by fixed points
    K = GF(2)
    Lk, Pk, permk = gd.posets['B']
    Vm = gd.mats
    perm_pts = []
    pts = [vector(K, v) for v in VectorSpace(K, 3) if v != 0]
    pkey = {tuple(v): i for i, v in enumerate(pts)}
    for g in Vm:
        A = mat(K, 7, 7)
        for i, v in enumerate(pts):
            A[i, pkey[tuple(v * g)]] = 1
        perm_pts.append(A)
    cosets = libgap.eval('function(Gp, gens, p) local H; H := SylowSubgroup(Gp, p); '
                         'return List(gens, g -> PermutationMat(Permutation(g, RightCosets(Gp, H), '
                         'OnRight), Index(Gp, H), GF(2))); end')
    tests = dict(mods)
    tests['F_2[points]'] = perm_pts
    tests['F_2[G/B]'] = [sage_mat(K, m) for m in cosets(gd.Gp, gd.gens, 2)]
    # projective, with a trivial quotient on which every N_P = sum of P acts as 0
    tests['F_2[G/C_7]'] = [sage_mat(K, m) for m in cosets(gd.Gp, gd.gens, 7)]
    outcome = {}
    for mname, rho_rows in tests.items():
        FM, W = gd.fixed_system('B', rho_rows)
        m = rho_rows[0].nrows()
        kap = cs_constant(Pk, K, m)
        Wc = [ident(K, m)] * Pk.n
        quo = cs_subquotient(Pk, K, m, Wc, W)
        off, tot, Q = colim_data(FM, list(range(Pk.n)))
        incl = mat(K, m, tot)
        for x in range(Pk.n):
            Bx = stack_cols(K, m, FM.comp[x])
            for i in range(m):
                for j in range(FM.d[x]):
                    incl[i, off[x] + j] = Bx[i, j]
        onto = incl.rank() == m
        h0q = colim_dim(quo)
        check(onto == (h0q == 0), 'Example p. 243: H_0(F_M) -> M onto iff H_0(kappa_M / F_M) = 0 '
              '(M = %s)' % mname)
        outcome[mname] = onto
        if mname in ('k', 'V', 'V*', 'St'):
            check(onto, 'Example p. 243: the simple module %s is generated by fixed points' % mname)
    check(outcome['F_2[G/B]'] and not outcome['F_2[G/C_7]'],
          'Example p. 243: F_2[G/B] is generated by fixed points, the projective module '
          'F_2[G/C_7] is not (its fixed points lie in the augmentation kernel)')


def main():
    sections = ['section_7_1', 'section_7_2', 'section_7_3']
    only = sys.argv[1:]
    gd = mods = None
    if not only or 'section_7_1' in only:
        section_7_1()
    if not only or 'section_7_2' in only or 'section_7_3' in only:
        gd, mods = section_7_2()
    if not only or 'section_7_3' in only:
        section_7_3(gd, mods)
    print('ok %s: %d checks (%.0f s)' % (SCOPE, COUNT[0], time.time() - T0))


if __name__ == '__main__':
    main()
