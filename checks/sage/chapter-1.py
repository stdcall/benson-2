"""Exact checks of Chapter 1 "Background from algebraic topology" (Sage).

Run: sage -python checks/sage/chapter-1.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-1: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), printed pp. 1-28.
Pages are the printed pages; labels are those of content/01-*.typ.

Chapter 1 is a survey of background with references to the literature; it
prints few numbers.  Its concrete statements are checked on small exact
models: finite simplicial sets written out here (the standard simplices
Delta[n] as monotone sequences, quotients Delta[n]/K such as the simplicial
spheres S[n], horns, products, Kan's suspension, nerves of small
categories, simplicial groups), cubical cell complexes, finite simplicial
complexes of Sage (spheres, real projective spaces, torus, Klein bottle,
surfaces, CP^2, the Poincare homology sphere), Sage's simplicial sets, the
lens spaces L(m, q) as orbit complexes of a free Z/m action on S^3, and
finite groups and free groups in GAP (libgap).  Homology is computed from
the chain complexes over ZZ and over finite fields and QQ.  Printed
readings that are wrong are kept as refuted checks (`refuted`) beside the
corrected ones.

What is checked, by section:

section_1_1 (pp. 1-2): prop:exponential and prop:based-exponential on
  finite discrete spaces (all maps, |X|, |Y|, |Z| <= 3: the bijection and
  the subspace of maps sending X x y0 u x0 x Y to z0); def:wedge-smash:
  S^(n-1) ^ S^1 has the homology of S^n (n <= 5), wedges have the sum of
  the reduced homologies.
section_1_2 (pp. 2-8): eq:divide-and-stretch and the associativity
  homotopy of prop:homotopy-group-structure (pieces, ends, continuity, as
  rational functions of s1, t); the inverse; the homotopy of the step
  "j_* i_* = 0" of prop:homotopy-long-exact-sequence; the Remark after it:
  the printed "image of pi_2(X, A, x0) lies in the centre of pi_1(A, x0)"
  refuted by (C(S^1 v S^1), S^1 v S^1) (pi_1 free of rank 2, its
  generators do not commute); the change of basepoint omega^* (ends of the
  pieces); the
  relative change of basepoint: the printed construction goes from
  pi_n(X, A, x0) to pi_n(X, A, x1) (direction of the display refuted), the
  corrected one (x0, x1 exchanged, omega(1 - x0)) goes as displayed, and
  the exchange without 1 - x0 is refuted; the Notation remark: identifying
  omega^*(f) with f in pi_1 is the abelianisation (normal closure of the
  commutators = derived subgroup, not the orbit set) for 9 groups; the
  proof of prop:extension-obstruction (S^n x I modulo S^n x 0 u s0 x I is
  acyclic, and the triple has the homology of (D^(n+1), S^n, s0), n <= 3);
  the Exercise: S^n X = S^n ^ X shifts reduced homology by n.
section_1_3 (pp. 9-11): H_n(S^n) = H_n(D^n, S^(n-1)) = Z (n <= 6); the
  inductive choice of generators (cubical chains: the triple
  (I^(n+1), dot I^(n+1), C^n), C^n acyclic, partial_* and j_* are
  isomorphisms, n <= 5); th:absolute-hurewicz for n = 1: H_1 = abelianised
  pi_1 for 15 complexes and simplicial sets; th:hurewicz-converse and the
  remark before it (the punctured Poincare sphere is acyclic with pi_1 of
  order 120); th:hurewicz-converse without path connectedness refuted
  (S^n + point); th:relative-hurewicz with n = 1 refuted
  ((S^1 v S^1, point)) and without X path connected (H_0(A + point, A));
  th:local-hurewicz refuted as printed by BA_4 at p = 2 (pi'_1 (x) F_2 = 0,
  pi_2 = 0, H_2(BA_4; F_2) = F_2, from the nerve and from the Schur
  multiplier; BA_4 is not simple) and by the simply connected
  K(Z/p^inf, 2) at n = 3 (Z/p^inf (x) F_p = 0, Tor(Z/p^inf, F_p) = F_p,
  computed on the finite stages, p = 2, 3, 5); the corrected theorem
  (X simple, homotopy groups finitely generated) on BZ/3 (F_2, F_3) and on
  four lens spaces L(m, q) (simple: the deck transformations act on
  H_3(S^3) by +1) over F_2, F_3, F_5, F_7.
section_1_4 (pp. 11-12): the homotopy of lem:cylinder-equivalence; the
  proof of th:whitehead-homology as corrected: (B) <=> H_i(Y, X) = 0 for
  i <= n, for all skeleton pairs of 7 complexes and all n, over F_2, F_3,
  Q; the printed "i < n" refuted (point in S^n; the same pair refutes the
  printed reading for (A), since pi_i(S^n) = 0 for i < n and
  pi_n(S^n) = Z by the Example of p. 11, which is not computed here).
section_1_5 (pp. 12-16): cellular chains: H_q(X^(p), X^(p-1)) free on the
  p-cells in degree p only, H_q(X^(p)) = 0 for q > p, H_q(X^(p)) ->
  H_q(X) iso for q < p (7 complexes, over Z and the fields);
  th:cellular-homology: one-cell-per-simplex models of Sage against
  triangulations (RP^2, RP^3, T^2, Klein bottle, CP^2, S^n), the cellular
  boundaries 0, 2, 0, 2, ... of RP^n (n <= 7), lens spaces L(m, q) (five
  cases, Z, Z/m, 0, Z; the cover S^3 -> L(m, q) with Z/m acting regularly
  on each fibre, the regular permutation representation of
  def:covering-space).
section_1_6 (pp. 16-22): lem:product-fibration (the lift
  H = h x (pi_F f pi_X), exhaustive on finite sets); the Examples of
  covering spaces: pi_1(S^1) = Z, pi_1(RP^n) = Z/2 and the universal cover
  of RP^n is S^n with fibre of 2 points for 2 <= n <= 5, for n = 1
  refuted (pi_1(RP^1) = Z); pi_1(T^2) = Z^2; th:universal-cover for
  S^1 v S^1: connected d-fold covers (d <= 4) are 1, 3, 7, 26 up to
  isomorphism (= conjugacy classes of subgroups of index d of F_2, GAP's
  low index subgroups), based ones 1, 3, 13, 71, and the image of
  pi_1(E', e'_0) is the stabiliser of the point e'_0 of the fibre F'
  (Schreier generators, index computed by GAP).
section_1_7 (pp. 22-23): the proof of th:paracompact-countable-cover on
  finite samples with piecewise linear partitions of unity: x in
  W(S(x)), disjointness, W_j empty for j > n; the printed
  "W(S(x)) contained in U_alpha" refuted for a cover by two sets (S(x)
  the whole index set), the corrected W(S) (with f_alpha > 0) checked.
section_1_8 (pp. 23-27): the face and degeneracy maps of the category
  Delta and the five relations (n <= 7), the normal form (all maps of
  Delta, counted); the maps d^i, s^i of topological simplices: the
  corrected d^i is the affine map of the i-th face map, the printed one is
  refuted, and the relations hold with the order reversed; Delta[n]
  (counts, relations, s_i injective); Delta[1] x Delta[1] (4, 5, 2
  non-degenerate simplices as listed) and Delta[p] x Delta[q] (binomial
  (p+q, p) top simplices); Kan's suspension S X by the printed formulas
  (relations, cells, H~_(n+1)(S X) = H~_n(X)) for six X; the horns:
  Delta[n, i] generated by all faces but the i-th is acyclic and its
  realisation is {x_j = 0 for some j != i}, the printed generators
  d_1 sigma, ... refuted; Kan complexes: Delta[1] is not Kan, the nerves
  BZ/3, BS_3 and the simplicial group F_2[Delta[1]] fill all horns
  (n <= 3); the homotopy with the bold cofaces d^0, d^1 (end points; the
  relation is not symmetric for Delta[1]); Hom(X, Y): Hom(S[1], S[1]) has
  2 vertices and 2 components while [S^1; S^1] = Z, so
  |Hom(X, Y)| -> Map(|X|, |Y|) is not a homotopy equivalence without Y
  Kan; Hom(S[1], BZ/2) gives the 2 classes; S[n] and pi_1(BG) = G; the
  normalized chains (degenerate subcomplex acyclic, same homology) on 7
  simplicial sets; the Eilenberg-Zilber shuffle map: with shuffles of
  {0, ..., n-1} every term is defined and nabla is a chain map in the
  universal case Delta[p] x Delta[q], p + q <= 6 (hence natural chain map
  in total degree <= 6 by Yoneda), with shuffles of {1, ..., n} (printed)
  no term is defined, equal signs are refuted; Alexander-Whitney: chain map
  (universal case, n <= 5) and AW nabla = id on normalized chains
  (p + q <= 6); nabla induces H_2(S[1] x S[1]) = Z; the Exercise: nerves of
  small categories satisfy the relations, the nerve of [n] is Delta[n],
  B Z/3 and the Kronecker category have the expected homology, the nerve
  of the face poset is the barycentric subdivision (f-vectors and
  homology, 4 complexes).
section_1_9 (pp. 27-28): lim^1 of groups: the printed formula is a left
  action of prod G_n on prod G_n (exhaustive on the truncations
  G_2 -> G_1 -> G_0 of two non-abelian towers, S_3 = S_3 -> S_2 and
  C_3 -> S_3 -> S_2), the stabiliser of (1, 1, ...) is lim G_n; in the
  abelian case (Z/4 <-2- Z/4 <-2- Z/4) the orbits are the cosets of the
  image of partial(g)_n = g_n - alpha(g_(n+1)) (so lim^1 is the cokernel,
  as in Goerss-Jardine VI.2 and Volume I, Section 4.1);
  th:milnor-exact-sequence for X = B Z/2 with skeleta X_n and
  Y = K(Z/2, k) (k <= 3): the maps of the towers H^k(X_n; F_2) are
  eventually isomorphisms of F_2, so lim^1 = 0 and
  [X; Y] = lim [X_n; Y] = H^k(BZ/2; F_2).

What these checks do NOT establish.  Each check is an exact computation
for the listed spaces, simplicial sets, groups and parameters (exhaustive
where so stated) or an identity of rational functions in the written
variables; none proves a general theorem of Chapter 1.  The exception is
the Eilenberg-Zilber and Alexander-Whitney identities: both sides are
natural, so the universal cases Delta[p] x Delta[q] (Yoneda) prove them
for all simplicial sets in the stated degrees.  Homotopy groups other
than pi_1 are not computed; the point-set topology (exponential law, CW
topology, paracompactness, fibrations, cellular approximation,
Whitehead's theorem, th:simplicial-equivalence, the Milnor sequence in
general, non-vanishing lim^1) is not checked.  The corrected
th:local-hurewicz and the corrected statement on
|Hom(X, Y)| -> Map(|X|, |Y|) (Y a Kan complex) rest on the literature
(May-Ponto, Theorems 5.3.2 and 6.1.2; Goerss-Jardine, Proposition I.11.1,
Theorem II.1.10, Example II.3.14); here they are only checked on the
examples above.  Nothing here compares our text with the printed book.
"""
import itertools
from fractions import Fraction

from sage.all import (
    GF, QQ, ZZ, AlternatingGroup, ChainComplex, CyclicPermutationGroup,
    PolynomialRing, SimplicialComplex, SymmetricGroup, binomial, factorial,
    groups, libgap, matrix, simplicial_complexes, simplicial_sets, vector,
)

COUNT = [0]


def check(condition, label):
    """The book's statement (or our corrected reading) holds."""
    assert bool(condition), label
    COUNT[0] += 1


def refuted(condition, label):
    """The printed reading must fail: it is kept as a refuted check."""
    assert not bool(condition), 'printed reading unexpectedly holds: ' + label
    COUNT[0] += 1


def pi1_trivial(X, **kw):
    return libgap(X.fundamental_group(**kw)).Size() == 1


# ---------------------------------------------------------------------------
# Homology of Sage objects.

def invariants(X, d, **kw):
    """Invariants of H_d (0 for a copy of Z), sorted."""
    return sorted(X.homology(d, **kw).invariants())


def reduced_invariants(X, d):
    return sorted(X.homology(d, reduced=True).invariants())


# ---------------------------------------------------------------------------
# Finite simplicial sets, truncated at a dimension N.  A simplex is a pair
# (n, data); face(i, x) and degen(i, x) are the maps d_i and s_i.

class SSet:
    def __init__(self, name, simplices, face, degen):
        self.name = name
        self.S = simplices          # S[n] = list of n-simplices, n <= N
        self.N = len(simplices) - 1
        self.face = face
        self.degen = degen

    def is_degenerate(self, x):
        n = x[0]
        return any(self.degen(i, self.face(i, x)) == x for i in range(n))

    def nondegenerate(self, n):
        return [x for x in self.S[n] if not self.is_degenerate(x)]


def delta(n, N):
    """Delta[n]: r-simplices are the sequences 0 <= a_0 <= ... <= a_r <= n."""
    S = [[(r, a) for a in itertools.combinations_with_replacement(range(n + 1), r + 1)]
         for r in range(N + 1)]

    def face(i, x):
        r, a = x
        return (r - 1, a[:i] + a[i + 1:])

    def degen(i, x):
        r, a = x
        return (r + 1, a[:i + 1] + a[i:])
    return SSet('Delta[%d]' % n, S, face, degen)


def delta_quotient(n, N, collapse, name):
    """Delta[n]/K, K the subcomplex of the sequences a with collapse(set(a));
    the image of K is a single vertex * (and its degeneracies)."""
    S = []
    for r in range(N + 1):
        S.append([(r, a) for a in itertools.combinations_with_replacement(range(n + 1), r + 1)
                  if not collapse(set(a))] + [(r, '*')])

    def norm(r, a):
        return (r, '*') if collapse(set(a)) else (r, a)

    def face(i, x):
        r, a = x
        return (r - 1, '*') if a == '*' else norm(r - 1, a[:i] + a[i + 1:])

    def degen(i, x):
        r, a = x
        return (r + 1, '*') if a == '*' else (r + 1, a[:i + 1] + a[i:])
    return SSet(name, S, face, degen)


def sphere(n, N):
    """S[n] = Delta[n]/boundary: one non-degenerate 0-simplex and n-simplex."""
    return delta_quotient(n, N, lambda s: len(s) < n + 1, 'S[%d]' % n)


def product(X, Y):
    N = min(X.N, Y.N)
    S = [[(r, (x, y)) for x in X.S[r] for y in Y.S[r]] for r in range(N + 1)]

    def face(i, z):
        r, (x, y) = z
        return (r - 1, (X.face(i, x), Y.face(i, y)))

    def degen(i, z):
        r, (x, y) = z
        return (r + 1, (X.degen(i, x), Y.degen(i, y)))
    return SSet(X.name + 'x' + Y.name, S, face, degen)


def relations_hold(X):
    """The five simplicial relations of p. 23 on all simplices of X."""
    d, s = X.face, X.degen
    for n in range(X.N + 1):
        for x in X.S[n]:
            for j in range(n + 1):
                for i in range(j):
                    if n >= 2 and d(i, d(j, x)) != d(j - 1, d(i, x)):
                        return False
            if n + 1 <= X.N:
                for j in range(n + 1):
                    sj = s(j, x)
                    for i in range(n + 2):
                        if i < j and n >= 1 and d(i, sj) != s(j - 1, d(i, x)):
                            return False
                        if i in (j, j + 1) and d(i, sj) != x:
                            return False
                        if i > j + 1 and n >= 1 and d(i, sj) != s(j, d(i - 1, x)):
                            return False
            if n + 2 <= X.N:
                for j in range(n + 1):
                    for i in range(j + 1):
                        if s(i, s(j, x)) != s(j + 1, s(i, x)):
                            return False
    return True


def normalized_complex(X, sub=None, ring=ZZ):
    """Normalized chains N_*(X) (modulo the simplices of a subcomplex sub),
    degrees 0..X.N, as a Sage ChainComplex."""
    basis = []
    for n in range(X.N + 1):
        b = [x for x in X.nondegenerate(n) if sub is None or not sub(x)]
        basis.append(b)
    index = [dict((x, k) for k, x in enumerate(b)) for b in basis]
    data = {}
    for n in range(1, X.N + 1):
        M = matrix(ring, len(basis[n - 1]), len(basis[n]), sparse=True)
        for c, x in enumerate(basis[n]):
            for i in range(n + 1):
                y = X.face(i, x)
                if y in index[n - 1]:
                    M[index[n - 1][y], c] += (-1) ** i
        data[n] = M
    if X.N == 0:
        data[1] = matrix(ring, len(basis[0]), 0)
    return ChainComplex(data, degree=-1, base_ring=ring), basis


def sset_invariants(X, d, sub=None):
    C, _ = normalized_complex(X, sub)
    return sorted(C.homology(d).invariants())


def unnormalized_invariants(X, d):
    """Homology of the full chain complex with all simplices (d < X.N)."""
    index = [dict((x, k) for k, x in enumerate(X.S[n])) for n in range(X.N + 1)]
    data = {}
    for n in range(1, X.N + 1):
        M = matrix(ZZ, len(X.S[n - 1]), len(X.S[n]), sparse=True)
        for c, x in enumerate(X.S[n]):
            for i in range(n + 1):
                M[index[n - 1][X.face(i, x)], c] += (-1) ** i
        data[n] = M
    return sorted(ChainComplex(data, degree=-1).homology(d).invariants())


def degenerate_subcomplex_acyclic(X):
    """The subcomplex D_* of degenerate simplices has zero homology in
    degrees < X.N."""
    deg = [[x for x in X.S[n] if X.is_degenerate(x)] for n in range(X.N + 1)]
    index = [dict((x, k) for k, x in enumerate(b)) for b in deg]
    data = {}
    for n in range(1, X.N + 1):
        M = matrix(ZZ, len(deg[n - 1]), len(deg[n]), sparse=True)
        for c, x in enumerate(deg[n]):
            for i in range(n + 1):
                y = X.face(i, x)
                assert y in index[n - 1] or not X.is_degenerate(y)
                if y in index[n - 1]:
                    M[index[n - 1][y], c] += (-1) ** i
                else:
                    # a face of a degenerate simplex that is non-degenerate
                    # cancels in pairs: d_i s_i y = d_(i+1) s_i y = y.
                    pass
        data[n] = M
    # The boundary of a degenerate simplex lies in D only modulo the pairs
    # of equal non-degenerate faces; check that they cancel.
    for n in range(1, X.N + 1):
        for x in deg[n]:
            tally = {}
            for i in range(n + 1):
                y = X.face(i, x)
                if not X.is_degenerate(y):
                    tally[y] = tally.get(y, 0) + (-1) ** i
            if any(v != 0 for v in tally.values()):
                return False
    C = ChainComplex(data, degree=-1)
    return all(C.homology(d).order() == 1 for d in range(X.N))


def simplicial_maps(D, Y, dim):
    """All simplicial maps D -> Y, D generated by its non-degenerate
    simplices of dimension <= dim (dim <= min(D.N, Y.N)).  A map is the
    dictionary of the images of the non-degenerate simplices."""
    gens = [x for n in range(dim + 1) for x in D.nondegenerate(n)]

    def image(table, z):
        if z in table:
            return table[z]
        for i in range(z[0]):
            if D.degen(i, D.face(i, z)) == z:
                return Y.degen(i, image(table, D.face(i, z)))
        raise KeyError(z)

    result = []

    def extend(k, table):
        if k == len(gens):
            result.append(dict(table))
            return
        x = gens[k]
        n = x[0]
        targets = [image(table, D.face(i, x)) for i in range(n + 1)] if n > 0 else None
        for y in Y.S[n]:
            if n > 0 and any(Y.face(i, y) != targets[i] for i in range(n + 1)):
                continue
            table[x] = y
            extend(k + 1, table)
            del table[x]
    extend(0, {})
    return result, image


def horn_data_fill(X, n, i):
    """Every compatible family (x_0, ..., x_n without x_i) of (n-1)-simplices
    has a filler z with d_k z = x_k (k != i)."""
    ks = [k for k in range(n + 1) if k != i]
    by_faces = {}
    for z in X.S[n]:
        key = tuple(X.face(k, z) for k in ks)
        by_faces[key] = z
    for fam in itertools.product(X.S[n - 1], repeat=n):
        xs = dict(zip(ks, fam))
        ok = all(X.face(a, xs[b]) == X.face(b - 1, xs[a])
                 for a in ks for b in ks if a < b)
        if ok and tuple(fam) not in by_faces:
            return False
    return True


def nerve(objects, morphisms, src, tgt, comp, ident, N, name):
    """Nerve of a small category: an n-simplex is (c_0, f_1, ..., f_n)."""
    S = [[(0, (c,)) for c in objects]]
    for n in range(1, N + 1):
        layer = []
        for x in S[n - 1]:
            c = x[1][0] if n == 1 else tgt(x[1][-1])
            for f in morphisms:
                if src(f) == c:
                    layer.append((n, x[1] + (f,)))
        S.append(layer)

    def face(i, x):
        n, a = x
        if n == 1:
            return (0, (tgt(a[1]),)) if i == 0 else (0, (a[0],))
        if i == 0:
            return (n - 1, (tgt(a[1]),) + a[2:])
        if i == n:
            return (n - 1, a[:-1])
        return (n - 1, a[:i] + (comp(a[i + 1], a[i]),) + a[i + 2:])

    def degen(i, x):
        n, a = x
        c = a[0] if i == 0 else tgt(a[i])
        return (n + 1, a[:i + 1] + (ident(c),) + a[i + 1:])
    return SSet(name, S, face, degen)


def group_nerve(G, N, name):
    els = list(G)
    e = G.identity()
    return nerve(['*'], els, lambda f: '*', lambda f: '*',
                 lambda g, f: g * f, lambda c: e, N, name)


def restrict(X, pred, name):
    """The simplicial subset of the simplices satisfying pred."""
    return SSet(name, [[x for x in X.S[r] if pred(x)] for r in range(X.N + 1)],
                X.face, X.degen)


# ---------------------------------------------------------------------------
# Finite simplicial complexes: chains over a ring with our own orientation.

class Complex:
    """A finite simplicial complex given by its faces (frozensets), with a
    fixed order of the vertices for the orientation."""

    def __init__(self, faces):
        allf = set()
        for f in faces:
            f = tuple(f)
            for r in range(1, len(f) + 1):
                for g in itertools.combinations(f, r):
                    allf.add(frozenset(g))
        self.faces = allf
        verts = sorted(set(v for f in allf for v in f), key=repr)
        self.vidx = dict((v, k) for k, v in enumerate(verts))
        self.dim = max(len(f) for f in allf) - 1

    def n_faces(self, n):
        return sorted((tuple(sorted(f, key=self.vidx.get)) for f in self.faces
                       if len(f) == n + 1), key=lambda t: [self.vidx[v] for v in t])

    def skeleton(self, p):
        return Complex([f for f in self.faces if len(f) <= p + 1])

    def union(self, other):
        return Complex(list(self.faces) + list(other.faces))


def sage_complex(K):
    return Complex([tuple(f) for f in K.facets()])


def boundary(K, n, ring, sub=None):
    """The boundary C_n -> C_(n-1) of K relative to sub, with bases."""
    rows = [f for f in K.n_faces(n - 1) if sub is None or frozenset(f) not in sub.faces] \
        if n >= 1 else []
    cols = [f for f in K.n_faces(n) if sub is None or frozenset(f) not in sub.faces]
    ri = dict((f, k) for k, f in enumerate(rows))
    M = matrix(ring, len(rows), len(cols), sparse=True)
    for c, f in enumerate(cols):
        for i in range(len(f)):
            g = f[:i] + f[i + 1:]
            if g in ri:
                M[ri[g], c] += (-1) ** i
    return M, rows, cols


def betti(K, n, F, sub=None):
    """dim H_n(K, sub; F) over a field F."""
    Mn, _, cols = boundary(K, n, F, sub)
    Mn1, _, _ = boundary(K, n + 1, F, sub)
    return len(cols) - Mn.rank() - Mn1.rank()


def complex_invariants(K, n, sub=None):
    data = dict((m, boundary(K, m, ZZ, sub)[0]) for m in range(1, K.dim + 2))
    if K.dim == 0:
        data[1] = boundary(K, 1, ZZ, sub)[0]
    return sorted(ChainComplex(data, degree=-1).homology(n).invariants())


def induced_rank(L, K, n, F):
    """Rank of H_n(L; F) -> H_n(K; F) for a subcomplex L of K."""
    _, _, colsK = boundary(K, n, F)
    idx = dict((f, k) for k, f in enumerate(colsK))
    ML, _, colsL = boundary(L, n, F)
    Z = ML.right_kernel().basis() if colsL else []
    emb = [vector(F, [0] * len(colsK)) for _ in Z]
    for v, z in zip(emb, Z):
        for k, f in enumerate(colsL):
            v[idx[f]] = z[k]
    B = boundary(K, n + 1, F)[0]
    Bcols = B.columns()
    rB = matrix(F, Bcols).rank() if Bcols else 0
    both = Bcols + emb
    rZB = matrix(F, both).rank() if both else 0
    return rZB - rB


# ---------------------------------------------------------------------------
# Section 1.1

def section_1_1():
    # prop:exponential, prop:based-exponential on finite discrete spaces
    # (the compact-open topology is discrete): f |-> f', f'(x)(y) = f(x, y).
    for a, b, c in [(1, 1, 2), (2, 1, 2), (2, 2, 2), (1, 2, 3), (2, 2, 3), (3, 2, 2)]:
        X, Y, Z = range(a), range(b), range(c)
        maps_XY = list(itertools.product(Z, repeat=a * b))      # f(x, y) = m[x*b + y]
        maps_Y = list(itertools.product(Z, repeat=b))
        curried = set()
        for m in maps_XY:
            fp = tuple(tuple(m[x * b + y] for y in Y) for x in X)
            curried.add(fp)
        check(len(curried) == len(maps_XY) == len(maps_Y) ** a,
              'prop:exponential: Map(X x Y, Z) = Map(X, Map(Y, Z)) (%d, %d, %d)' % (a, b, c))
        # based: x0 = y0 = z0 = 0; Map_*(Y, Z) has the constant map as base.
        const = tuple(0 for _ in Y)
        good = 0
        for m in maps_XY:
            fp = tuple(tuple(m[x * b + y] for y in Y) for x in X)
            sends_wedge = all(m[x * b + 0] == 0 for x in X) and all(m[0 * b + y] == 0 for y in Y)
            based = fp[0] == const and all(fp[x][0] == 0 for x in X)
            good += sends_wedge == based
        check(good == len(maps_XY),
              'p. 2: Map_*(X, Map_*(Y, Z)) = maps sending X x y0 u x0 x Y to z0 (%d, %d, %d)'
              % (a, b, c))
        check(sum(1 for m in maps_XY if all(m[x * b] == 0 for x in X)
                  and all(m[y] == 0 for y in Y)) == c ** ((a - 1) * (b - 1)),
              'prop:based-exponential: |Map_*(X ^ Y, Z)| = |Z|^((|X|-1)(|Y|-1))')

    # def:wedge-smash: S^(n-1) ^ S^1 = S^n (homology), wedges.
    S = simplicial_sets
    for n in range(2, 6):
        Sm = S.Sphere(n - 1).smash_product(S.Sphere(1))
        check(all(reduced_invariants(Sm, d) == ([0] if d == n else []) for d in range(n + 2)),
              'p. 8: S^(n-1) ^ S^1 has the homology of S^n, n = %d' % n)
    for X, Y in [(S.Sphere(1), S.Sphere(2)), (S.RealProjectiveSpace(2), S.Torus()),
                 (S.KleinBottle(), S.Sphere(1))]:
        W = X.wedge(Y)
        check(all(reduced_invariants(W, d) == sorted(reduced_invariants(X, d) + reduced_invariants(Y, d))
                  for d in range(4)),
              'def:wedge-smash: reduced homology of a wedge is the sum')


# ---------------------------------------------------------------------------
# Section 1.2

def section_1_2():
    R = PolynomialRing(QQ, ['s', 't']).fraction_field()
    s, t = R.gens()
    # eq:divide-and-stretch: (f * g)(s) = f(2s) on [0, 1/2], g(2s - 1) on
    # [1/2, 1]; at s = 1/2 both arguments are on the boundary (f(1), g(0)).
    check((2 * s).subs(s=QQ(1) / 2) == 1 and (2 * s - 1).subs(s=QQ(1) / 2) == 0,
          'eq:divide-and-stretch: the two pieces meet on the boundary')
    # The associativity homotopy of prop:homotopy-group-structure.
    a1 = 4 * s / (1 + t)
    a2 = 4 * s - 1 - t
    a3 = (4 * s - 2 - t) / (2 - t)
    b1 = (1 + t) / 4
    b2 = (2 + t) / 4
    check(a1.subs(s=0) == 0 and a1.subs(s=b1) == 1 and a2.subs(s=b1) == 0
          and a2.subs(s=b2) == 1 and a3.subs(s=b2) == 0 and a3.subs(s=1) == 1,
          'prop:homotopy-group-structure: each piece maps its interval onto [0, 1] and '
          'consecutive pieces meet on the boundary (the basepoint)')
    check(a1.subs(t=0) == 4 * s and a2.subs(t=0) == 4 * s - 1 and a3.subs(t=0) == 2 * s - 1
          and b1.subs(t=0) == QQ(1) / 4 and b2.subs(t=0) == QQ(1) / 2,
          'prop:homotopy-group-structure: F at t = 0 is (f1 * f2) * f3')
    check(a1.subs(t=1) == 2 * s and a2.subs(t=1) == 4 * s - 2 and a3.subs(t=1) == 4 * s - 3
          and b1.subs(t=1) == QQ(1) / 2 and b2.subs(t=1) == QQ(3) / 4,
          'prop:homotopy-group-structure: F at t = 1 is f1 * (f2 * f3)')
    # inverse: (f * f')(s) uses f(2s) and f(1 - (2s - 1)): the loop retraces.
    left = 2 * s
    right = 1 - (2 * (1 - s) - 1)
    check(left == right, 'prop:homotopy-group-structure: f * f\' retraces f')
    # j_* i_* = 0: F(t_1, ..., t_n, t) = f(..., t + (1 - t) t_n).
    tn = s
    arg = t + (1 - t) * tn
    check(arg.subs(t=0) == tn and arg.subs(t=1) == 1 and arg.subs(s=1) == 1
          and all(0 <= arg.subs(s=u, t=v) <= 1 for u in (0, 1) for v in (0, 1)),
          'prop:homotopy-long-exact-sequence, j_* i_* = 0: the homotopy ends in the face '
          't_n = 1 of C^(n-1) and keeps C^(n-1) there')

    # Change of basepoint, absolute case: radius r = |u|.
    r = s
    inner = 2 * r              # |2u|
    outer = 2 - 2 * r          # argument of omega
    check(inner.subs(s=QQ(1) / 2) == 1 and outer.subs(s=QQ(1) / 2) == 1 and outer.subs(s=1) == 0,
          'p. 6: omega^*(f) is continuous (f = x1 = omega(1) at radius 1/2) and based at '
          'omega(0) = x0: omega^* : pi_n(X, x1) -> pi_n(X, x0)')

    # Change of basepoint, relative case.  The strip 0 <= x_0 <= 1 is sent
    # by omega(arg(x_0)); the collapsed face x_0 = 0 meets the half disk,
    # which is sent by f to its basepoint; (1, 0, ..., 0) is the new base.
    omega = {0: 'x0', 1: 'x1'}

    def reading(base_f, base_new, arg):
        continuous = omega[arg(0)] == base_f
        based = omega[arg(1)] == base_new
        return continuous and based, (base_f, base_new)

    ok, direction = reading('x0', 'x1', lambda u: u)
    check(ok, 'p. 7 printed construction is consistent (f at x0, omega^*(f) at x1)')
    refuted(direction == ('x1', 'x0'),
            'p. 7: the printed construction defines omega^* : pi_n(X, A, x1) -> pi_n(X, A, x0)')
    ok, direction = reading('x1', 'x0', lambda u: 1 - u)
    check(ok and direction == ('x1', 'x0'),
          'p. 7 corrected: f at x1, omega^*(f) at x0, omega(1 - x_0): the displayed direction')
    refuted(reading('x1', 'x0', lambda u: u)[0],
            'p. 7: exchanging x0, x1 without omega(1 - x_0)')

    # Remark after prop:homotopy-long-exact-sequence: the printed "image of
    # pi_2(X, A, x0) lies in the centre of pi_1(A, x0)".  For A = S^1 v S^1
    # and X = CA (acyclic, simply connected), the exact sequence gives
    # partial : pi_2(X, A) = pi_1(A), a free group of rank 2.
    S = simplicial_sets
    A = S.Sphere(1).wedge(S.Sphere(1))
    CA = A.cone()
    check(all(CA.homology(d, reduced=True).order() == 1 for d in range(3))
          and pi1_trivial(CA),
          'Remark p. 5: the cone on S^1 v S^1 is acyclic and simply connected')
    G = libgap(A.fundamental_group())
    gens = G.GeneratorsOfGroup()
    S3 = libgap.SymmetricGroup(3)
    hom = libgap.GroupHomomorphismByImages(G, S3, gens,
                                           [libgap.eval('(1,2)'), libgap.eval('(2,3)')])
    x, y = [libgap.Image(hom, g) for g in gens]
    check(len(gens) == 2 and A.fundamental_group().relations() == (),
          'Remark p. 5: pi_1(S^1 v S^1) is free of rank 2')
    refuted(x * y == y * x,
            'Remark p. 5: the image of pi_2(X, A, x0) (here all of pi_1(A, x0)) lies in the '
            'centre of pi_1(A, x0)')

    # Notation remark (p. 7): identifying omega^*(f) = omega f omega^(-1)
    # with f in pi_1 gives the abelianisation (as a group quotient).
    for name in ['SymmetricGroup(3)', 'DihedralGroup(8)', 'QuaternionGroup(8)',
                 'AlternatingGroup(4)', 'SymmetricGroup(4)', 'SL(2,3)',
                 'AlternatingGroup(5)', 'CyclicGroup(6)', 'SmallGroup(21,1)']:
        H = libgap.eval(name)
        els = H.AsList()
        comms = [libgap.Comm(f, w) for f in els for w in els]
        Nc = libgap.NormalClosure(H, libgap.Subgroup(H, comms))
        check(Nc == H.DerivedSubgroup(),
              'Notation p. 7: pi\'_1 is pi_1 modulo the identifications = abelianisation (%s)' % name)
        if not H.IsAbelian():
            check(H.NrConjugacyClasses() != H.Size() / H.DerivedSubgroup().Size(),
                  'Notation p. 7: the quotient is a group quotient, not the orbit set (%s)' % name)

    # prop:extension-obstruction, its proof: (S^n x I, S^n x 0 u S^n x 1 u
    # s0 x I, S^n x 0 u s0 x I) has the homology of (D^(n+1), S^n, s0).
    for n in range(1, 4):
        P = product(sphere(n, n + 2), delta(1, n + 2))

        def in_B0(z):
            x, y = z[1]
            return x[1] == '*' or set(y[1]) == {0}

        def in_B(z):
            x, y = z[1]
            return x[1] == '*' or len(set(y[1])) == 1
        B = restrict(P, in_B, 'B')
        check(all(sset_invariants(P, d, in_B0) == [] for d in range(n + 2)),
              'prop:extension-obstruction: S^n x I modulo S^n x 0 u s0 x I is acyclic, n = %d' % n)
        check(all(sset_invariants(P, d, in_B) == ([0] if d == n + 1 else []) for d in range(n + 2)),
              'prop:extension-obstruction: H(S^n x I, S^n x {0,1} u s0 x I) = H(D^(n+1), S^n)')
        check(all(sset_invariants(B, d, in_B0) == ([0] if d == n else []) for d in range(n + 2)),
              'prop:extension-obstruction: the boundary modulo S^n x 0 u s0 x I is S^n')

    # Exercise p. 8: S^n X = S^n ^ X shifts reduced homology by n.
    for X in [S.RealProjectiveSpace(2), S.Torus(), S.KleinBottle(),
              S.Sphere(1).wedge(S.Sphere(2))]:
        for n in (1, 2):
            Sm = S.Sphere(n).smash_product(X)
            check(all(reduced_invariants(Sm, d + n) == reduced_invariants(X, d) for d in range(4))
                  and all(reduced_invariants(Sm, d) == [] for d in range(n)),
                  'Exercise p. 8: H~_(d+n)(S^n X) = H~_d(X)')


# ---------------------------------------------------------------------------
# Cubical cell complexes: a cell of I^m is a tuple over {0, 1, 'I'}.

def cube_cells(m):
    return [c for c in itertools.product((0, 1, 'I'), repeat=m)]


def cube_boundary(c):
    out = {}
    k_I = 0
    for k, v in enumerate(c):
        if v == 'I':
            sign = (-1) ** k_I
            for end, e in ((1, 1), (0, -1)):
                f = c[:k] + (end,) + c[k + 1:]
                out[f] = out.get(f, 0) + sign * e
            k_I += 1
    return out


def cell_invariants(cells, sub, d):
    """H_d of the cell complex `cells` (closed under the boundary) modulo the
    subcomplex `sub`, over ZZ."""
    by_dim = {}
    for c in cells:
        if c not in sub:
            by_dim.setdefault(sum(1 for v in c if v == 'I'), []).append(c)
    top = max(by_dim) if by_dim else 0
    idx = dict((k, dict((c, i) for i, c in enumerate(by_dim.get(k, [])))) for k in range(top + 2))
    data = {}
    for k in range(1, top + 2):
        M = matrix(ZZ, len(idx[k - 1]), len(idx[k]), sparse=True)
        for c, j in idx[k].items():
            for f, v in cube_boundary(c).items():
                if f in idx[k - 1]:
                    M[idx[k - 1][f], j] += v
        data[k] = M
    return sorted(ChainComplex(data, degree=-1).homology(d).invariants())


def primary(invs):
    out = []
    for n in invs:
        if n == 0:
            out.append(0)
        else:
            out += [p ** e for p, e in ZZ(n).factor()]
    return sorted(out)


# ---------------------------------------------------------------------------
# Section 1.3

def section_1_3():
    # H_n(S^n) = H_n(D^n, S^(n-1)) = Z.
    for n in range(1, 7):
        Sn = simplicial_complexes.Sphere(n)
        Dn = simplicial_complexes.Simplex(n)
        check(invariants(Sn, n) == [0] and all(invariants(Sn, d) == [] for d in range(1, n)),
              'p. 9: H_n(S^n) = Z, n = %d' % n)
        check(sorted(Dn.homology(n, subcomplex=simplicial_complexes.Sphere(n - 1)).invariants()) == [0]
              and all(Dn.homology(d, subcomplex=simplicial_complexes.Sphere(n - 1)).order() == 1
                      for d in range(n)),
              'p. 9: H_n(D^n, S^(n-1)) = Z, n = %d' % n)

    # The choice of generators (p. 10), cubical chains.  I^m, its boundary,
    # C^(m-1) = boundary minus the open face (I, ..., I, 0).
    for m in range(1, 6):
        cells = cube_cells(m)
        top = tuple('I' for _ in range(m))
        bd = set(c for c in cells if c != top)
        open_face = top[:-1] + (0,)
        C = set(c for c in bd if c != open_face)
        check(cell_invariants(cells, set(), 0) == [0]
              and all(cell_invariants(cells, set(), d) == [] for d in range(1, m + 1)),
              'p. 10: I^%d is acyclic' % m)
        check(all(cell_invariants(C, set(), d) == ([0] if d == 0 else []) for d in range(m + 1)),
              'p. 10: C^(m-1) is acyclic, m = %d' % m)
        check(all(cell_invariants(cells, C, d) == [] for d in range(m + 1)),
              'p. 10: H_*(I^m, C^(m-1)) = 0 (the outer terms of the sequence), m = %d' % m)
        check(all(cell_invariants(bd, C, d) == ([0] if d == m - 1 else []) for d in range(m + 1))
              and all(cell_invariants(cells, bd, d) == ([0] if d == m else []) for d in range(m + 1)),
              'p. 10: H(dot I^m, C^(m-1)) = Z in degree m-1, H(I^m, dot I^m) = Z in degree m')
        # partial_* sends the top cell to the coefficient of the open face
        # times its class; j_* sends the top cell of I^(m-1) to the open face.
        coef = cube_boundary(top).get(open_face, 0)
        check(abs(coef) == 1, 'p. 10: partial_* and j_* are isomorphisms, so '
              'z_(n+1) = partial_*^(-1) j_*(z_n) is a generator (m = %d)' % m)

    # th:absolute-hurewicz, n = 1: H_1 is the abelianised pi_1.
    S = simplicial_sets
    spaces = [
        ('RP^2', simplicial_complexes.RealProjectivePlane()),
        ('RP^3', simplicial_complexes.RealProjectiveSpace(3)),
        ('Klein', simplicial_complexes.KleinBottle()),
        ('T^2', simplicial_complexes.Torus()),
        ('genus 2', simplicial_complexes.SurfaceOfGenus(2)),
        ('N_3', simplicial_complexes.SurfaceOfGenus(3, orientable=False)),
        ('M(Z/3,1)', simplicial_complexes.MooreSpace(3)),
        ('M(Z/4,1)', simplicial_complexes.MooreSpace(4)),
        ('dunce hat', simplicial_complexes.DunceHat()),
        ('Poincare', simplicial_complexes.PoincareHomologyThreeSphere()),
        ('CP^2', simplicial_complexes.ComplexProjectivePlane()),
        ('S^1 v S^1', S.Sphere(1).wedge(S.Sphere(1))),
        ('RP^5', S.RealProjectiveSpace(5)),
        ('presentation Q8', S.PresentationComplex(groups.presentation.Quaternion())),
        ('presentation D10', S.PresentationComplex(groups.presentation.Dihedral(5))),
    ]
    for name, X in spaces:
        G = libgap(X.fundamental_group())
        check(primary(list(G.AbelianInvariants())) == primary(invariants(X, 1)),
              'th:absolute-hurewicz (n = 1): H_1 = pi_1 abelianised (%s)' % name)

    # th:hurewicz-converse and the remark before it: the Poincare sphere has
    # pi_1 of order 120 (perfect), and minus an open 3-simplex it is acyclic.
    P = simplicial_complexes.PoincareHomologyThreeSphere()
    GP = libgap(P.fundamental_group())
    check(GP.Size() == 120 and list(GP.AbelianInvariants()) == [],
          'p. 11: pi_1 of the Poincare sphere has order 120 and H_1 = 0')
    facet = next(iter(P.facets()))
    Q = SimplicialComplex([f for f in P.facets() if f != facet])
    check(all(Q.homology(d, reduced=True).order() == 1 for d in range(4))
          and libgap(Q.fundamental_group()).Size() == 120,
          'p. 11: a space with H~_* = 0 and pi_1 non-zero (punctured Poincare sphere)')
    # th:hurewicz-converse needs X path connected: S^n + point, based at the
    # point: pi_1 = 0, H_i = 0 for 0 < i < n, H_n = Z, pi_n(point) = 0.
    for n in range(2, 5):
        X = SimplicialComplex(list(simplicial_complexes.Sphere(n).facets()) + [(n + 2,)])
        cond = (pi1_trivial(X, base_point=n + 2)
                and all(X.homology(d).order() == 1 for d in range(1, n)))
        refuted(cond and invariants(X, n) == [],
                'th:hurewicz-converse without path connectedness (S^%d + point): '
                'pi_n(X, point) = 0 but H_n(X) = Z' % n)
        check(invariants(simplicial_complexes.Sphere(n), n) == [0]
              and pi1_trivial(simplicial_complexes.Sphere(n)),
              'Example p. 11: S^%d simply connected, H_n = Z' % n)
    # th:relative-hurewicz with n = 1: (S^1 v S^1, point); pi'_1(X, A) =
    # pi_1(X) is free, h_1 is the abelianisation, not injective.
    W = S.Sphere(1).wedge(S.Sphere(1))
    G = libgap(W.fundamental_group())
    a, b = G.GeneratorsOfGroup()
    hom = libgap.GroupHomomorphismByImages(G, libgap.SymmetricGroup(3), [a, b],
                                           [libgap.eval('(1,2)'), libgap.eval('(2,3)')])
    comm = libgap.Comm(a, b)
    nontrivial = libgap.Image(hom, comm) != libgap.Image(hom, a ** 0)
    check(invariants(W, 1) == [0, 0], 'p. 10: H_1(S^1 v S^1) = Z^2, where [a, b] dies')
    refuted(not nontrivial,
            'th:relative-hurewicz for n = 1: h_1 : pi\'_1(S^1 v S^1, point) -> H_1 is '
            'injective (the commutator [a, b] is non-trivial, h_1([a, b]) = 0)')
    # ... and X must be path connected: X = A + point, H_0(X, A) = Z.
    X = SimplicialComplex(list(simplicial_complexes.Sphere(1).facets()) + [(5,)])
    refuted(X.homology(0, subcomplex=simplicial_complexes.Sphere(1)).order() == 1,
            'th:relative-hurewicz without X path connected: H_0(A + point, A) = 0')

    # th:local-hurewicz as printed: X = BA_4, k = F_2, n = 2.  pi_1 = A_4,
    # pi'_1 (x) F_2 = Z/3 (x) F_2 = 0, pi_2 = 0, but H_2(BA_4; F_2) = F_2.
    A4 = AlternatingGroup(4)
    check(list(libgap(A4).AbelianInvariants()) == [3]
          and list(libgap(A4).AbelianInvariantsMultiplier()) == [2],
          'th:local-hurewicz: A_4 has abelianisation Z/3 and Schur multiplier Z/2')
    B = group_nerve(A4, 3, 'BA4')
    check(sset_invariants(B, 1) == [3] and sset_invariants(B, 2) == [2],
          'th:local-hurewicz: H_1(BA_4) = Z/3, H_2(BA_4) = Z/2 (nerve)')
    BS = S.ClassifyingSpace(A4).n_skeleton(3)
    h2 = BS.homology(2, base_ring=GF(2)).dimension()
    h1 = BS.homology(1, base_ring=GF(2)).dimension()
    refuted(h1 == 0 and h2 == 0,
            'th:local-hurewicz as printed (BA_4, F_2, n = 2): H_2(BA_4; F_2) = '
            'F_2 (x) pi\'_2 = 0')
    check(h1 == 0 and h2 == 1, 'th:local-hurewicz: H_1(BA_4; F_2) = 0, H_2 = F_2')
    check(not libgap(A4).IsAbelian(),
          'th:local-hurewicz as corrected: BA_4 is not simple (pi_1 = A_4 is not abelian)')

    # th:local-hurewicz as printed, simply connected: X = K(Z/p^inf, 2),
    # k = F_p, n = 3.  pi_2 = H_2 = Z/p^inf (Hurewicz), pi_3 = 0; by the
    # universal coefficient theorem H_3(X; F_p) contains Tor(Z/p^inf, F_p).
    # Z/p^inf = union of the stages (1/p^k)Z/Z: it is p-divisible (each
    # element of a stage is p times an element of the next), so
    # pi_2 (x) F_p = 0, and its p-torsion has p elements at every stage
    # k >= 1, so Tor(Z/p^inf, F_p) = F_p.
    for p in (2, 3, 5):
        divisible = all(set((p * b) % p ** (k + 1) for b in range(p ** (k + 1)))
                        >= set(p * a for a in range(p ** k))
                        for k in range(1, 6))
        torsion = [sum(1 for a in range(p ** k) if (p * a) % p ** k == 0) for k in range(1, 6)]
        check(divisible and torsion == [p] * 5,
              'th:local-hurewicz: Z/%d^inf (x) F_%d = 0 and Tor(Z/%d^inf, F_%d) = F_%d'
              % (p, p, p, p, p))
        refuted(torsion[-1] == 1,
                'th:local-hurewicz as printed (K(Z/%d^inf, 2), F_%d, n = 3): '
                'H_3(X; F_%d) = F_%d (x) pi_3 = 0 (it contains Tor(H_2, F_%d) = F_%d)'
                % (p, p, p, p, p, p))

    # th:local-hurewicz as corrected (X simple, homotopy groups finitely
    # generated): BZ/3 = K(Z/3, 1) and the lens spaces L(m, q) (pi_1 = Z/m,
    # pi_2 = 0, pi_3 = Z on which Z/m acts by the degree +1 of the deck
    # transformations).
    BZ3 = group_nerve(CyclicPermutationGroup(3), 4, 'BZ/3')
    C3, _ = normalized_complex(BZ3, ring=GF(2))
    check(all(C3.homology(d).dimension() == 0 for d in (1, 2, 3)),
          'th:local-hurewicz as corrected: H_i(BZ/3; F_2) = 0 (F_2 (x) pi_i = 0 for all i)')
    C3, _ = normalized_complex(BZ3, ring=GF(3))
    check(C3.homology(1).dimension() == 1,
          'th:local-hurewicz as corrected (BZ/3, F_3, n = 1): H_1 = F_3 = F_3 (x) pi_1')
    for m, q in [(2, 1), (3, 1), (5, 2), (7, 3)]:
        C, full, regular = lens_space(m, q)
        check(lens_deck_sign(m, q) == 1,
              'L(%d, %d) is simple: Z/%d acts on H_3(S^3) = pi_3 by +1' % (m, q, m))
        for p in (2, 3, 5, 7):
            dims = [C.homology(d, base_ring=GF(p)).dimension() for d in range(1, 4)]
            if m % p:
                check(dims == [0, 0, 1],
                      'th:local-hurewicz as corrected (L(%d, %d), F_%d, n = 3): H_1 = H_2 = 0, '
                      'H_3 = F_%d (x) pi_3' % (m, q, p, p))
            else:
                check(dims[0] == 1, 'th:local-hurewicz as corrected (L(%d, %d), F_%d, n = 1): '
                      'H_1 = F_%d (x) pi_1' % (m, q, p, p))


def test_complexes():
    return [
        ('RP^2', sage_complex(simplicial_complexes.RealProjectivePlane())),
        ('RP^3', sage_complex(simplicial_complexes.RealProjectiveSpace(3))),
        ('T^2', sage_complex(simplicial_complexes.Torus())),
        ('Klein', sage_complex(simplicial_complexes.KleinBottle())),
        ('S^3', sage_complex(simplicial_complexes.Sphere(3))),
        ('CP^2', sage_complex(simplicial_complexes.ComplexProjectivePlane())),
        ('M(Z/3,1)', sage_complex(simplicial_complexes.MooreSpace(3))),
    ]


# ---------------------------------------------------------------------------
# Section 1.4

def section_1_4():
    R = PolynomialRing(QQ, ['t', 'u']).fraction_field()
    t, u = R.gens()           # u is t' of lem:cylinder-equivalence
    h = 1 - u * (1 - t)
    check(h.subs(u=0) == 1 and h.subs(u=1) == t and h.subs(t=1) == 1
          and all(0 <= h.subs(t=a, u=b) <= 1 for a in (0, 1) for b in (0, 1)),
          'lem:cylinder-equivalence: F starts at j pi ((x, 1) = f(x)), ends at the '
          'identity and is constant on the end (x, 1) ~ f(x)')

    # th:whitehead-homology, its proof: for an inclusion X <= Y (M_f ~ Y rel
    # X), (B) f_* iso for i < n, epi for i = n  <=>  H_i(Y, X) = 0, i <= n.
    printed_fails = 0
    cases = 0
    pairs = []
    for name, K in test_complexes():
        for p in range(K.dim + 1):
            pairs.append((name, K.skeleton(p), K))
    for n in range(1, 5):
        Sn = sage_complex(simplicial_complexes.Sphere(n))
        pairs.append(('point in S^%d' % n, Complex([(0,)]), Sn))
    for F in (GF(2), GF(3), QQ):
        for name, L, K in pairs:
            top = K.dim + 1
            hL = [betti(L, i, F) for i in range(top + 1)]
            hK = [betti(K, i, F) for i in range(top + 1)]
            rk = [induced_rank(L, K, i, F) for i in range(top + 1)]
            rel = [betti(K, i, F, sub=L) for i in range(top + 1)]
            for n in range(1, top):
                B = all(rk[i] == hL[i] == hK[i] for i in range(n)) and rk[n] == hK[n]
                corrected = all(rel[i] == 0 for i in range(n + 1))
                printed = all(rel[i] == 0 for i in range(n))
                cases += 1
                if B != corrected:
                    raise AssertionError('th:whitehead-homology proof: %s, n = %d' % (name, n))
                printed_fails += B != printed
    check(cases > 0, 'th:whitehead-homology, proof as corrected: (B) <=> H_i(M_f, X) = 0 for '
          'i <= n (%d cases)' % cases)
    COUNT[0] += cases - 1
    refuted(printed_fails == 0,
            'th:whitehead-homology, proof as printed: (B) <=> H_i(M_f, X) = 0 for i < n '
            '(fails in %d cases, e.g. point in S^n)' % printed_fails)


# ---------------------------------------------------------------------------
# Lens spaces L(m, q): the orbit complex of the free Z/m action on
# S^3 = C_N * C_N (join of two N-gons), a_i -> a_(i+N/m), b_j -> b_(j+qN/m).

def perm_sign(seq, key):
    seq = list(seq)
    sign = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if key(seq[i]) > key(seq[j]):
                sign = -sign
    return sign


def lens_space(m, q):
    N = 3 * m
    key = lambda v: (0 if v[0] == 'a' else 1, v[1])
    parts = [()] + [(i,) for i in range(N)] + [(i, (i + 1) % N) for i in range(N)]
    simplices = set()
    for P in parts:
        for Q in parts:
            if P or Q:
                simplices.add(tuple(sorted([('a', i) for i in P] + [('b', j) for j in Q], key=key)))

    def g(v, k):
        step = N // m
        return ('a', (v[1] + k * step) % N) if v[0] == 'a' else ('b', (v[1] + k * q * step) % N)

    rep = {}
    for s in simplices:
        orbit = []
        for k in range(m):
            img = [g(v, k) for v in s]
            orbit.append(tuple(sorted(img, key=key)))
        r = min(orbit, key=lambda t: [key(v) for v in t])
        if len(set(orbit)) != m:
            return None                       # not free
        rep[s] = r
    sign_to_rep = {}
    for s in simplices:
        r = rep[s]
        for k in range(m):
            img = [g(v, k) for v in r]
            if set(img) == set(s):
                sign_to_rep[s] = perm_sign(img, key)
    reps = sorted(set(rep.values()), key=lambda t: (len(t), [key(v) for v in t]))
    by_dim = {}
    for r in reps:
        by_dim.setdefault(len(r) - 1, []).append(r)
    idx = dict((d, dict((r, i) for i, r in enumerate(by_dim[d]))) for d in by_dim)
    data = {}
    for d in range(1, 4):
        M = matrix(ZZ, len(by_dim[d - 1]), len(by_dim[d]), sparse=True)
        for r, c in idx[d].items():
            for i in range(len(r)):
                f = r[:i] + r[i + 1:]
                M[idx[d - 1][rep[f]], c] += (-1) ** i * sign_to_rep[f]
        data[d] = M
    C = ChainComplex(data, degree=-1)
    vertex_orbits = [s for s in simplices if len(s) == 1]
    regular = all(len(set(g(s[0], k) for k in range(m))) == m for s in vertex_orbits)
    full = Complex(list(simplices))
    return C, full, regular


def lens_deck_sign(m, q):
    """The sign s with g z = s z for the generator g of Z/m and a generator
    z of H_3(S^3) = Z (S^3 = C_N * C_N, as in lens_space)."""
    _, full, _ = lens_space(m, q)
    N = 3 * m
    step = N // m

    def g(v):
        return ('a', (v[1] + step) % N) if v[0] == 'a' else ('b', (v[1] + q * step) % N)
    M3, _, cols = boundary(full, 3, ZZ)
    z = M3.right_kernel().basis()[0]
    idx = dict((f, k) for k, f in enumerate(cols))
    gz = [0] * len(cols)
    for k, f in enumerate(cols):
        img = [g(v) for v in f]
        target = tuple(sorted(img, key=full.vidx.get))
        gz[idx[target]] += perm_sign(img, full.vidx.get) * z[k]
    gz = vector(ZZ, gz)
    return 1 if gz == z else (-1 if gz == -z else 0)


# ---------------------------------------------------------------------------
# Section 1.5

def section_1_5():
    for name, K in test_complexes():
        for p in range(K.dim + 1):
            Xp = K.skeleton(p)
            Xq = K.skeleton(p - 1) if p > 0 else None
            nfaces = len(K.n_faces(p))
            check(all(complex_invariants(Xp, q, Xq) == ([0] * nfaces if q == p else [])
                      for q in range(K.dim + 1)),
                  'p. 14: H_q(X^(p), X^(p-1)) is free on the p-cells, zero for q != p (%s)' % name)
            check(all(complex_invariants(Xp, q) == [] for q in range(p + 1, K.dim + 1)),
                  'p. 14: H_q(X^(p)) = 0 for q > p (%s)' % name)
            check(all(complex_invariants(Xp, q) == complex_invariants(K, q) for q in range(p)),
                  'p. 14: H_q(X^(p)) = H_q(X) for q < p (%s, groups)' % name)
            for F in (GF(2), QQ):
                check(all(induced_rank(Xp, K, q, F) == betti(Xp, q, F) == betti(K, q, F)
                          for q in range(p)),
                      'p. 14: H_q(X^(p)) -> H_q(X) is an isomorphism for q < p (%s)' % name)
        # relative to A = the closure of one facet
        A = Complex([max(K.faces, key=lambda f: (len(f), sorted(K.vidx[v] for v in f)))])
        for p in range(K.dim + 1):
            Xp = A.union(K.skeleton(p))
            check(all(complex_invariants(Xp, q, A) == [] for q in range(p + 1, K.dim + 1))
                  and all(complex_invariants(Xp, q, A) == complex_invariants(K, q, A)
                          for q in range(p)),
                  'p. 14: H_q(X^(p), A) = 0 for q > p, = H_q(X, A) for q < p (%s)' % name)

    # th:cellular-homology: models with one cell per non-degenerate simplex
    # against triangulations.
    S = simplicial_sets
    for name, X, K, top in [
            ('RP^2', S.RealProjectiveSpace(2), simplicial_complexes.RealProjectivePlane(), 2),
            ('RP^3', S.RealProjectiveSpace(3), simplicial_complexes.RealProjectiveSpace(3), 3),
            ('T^2', S.Torus(), simplicial_complexes.Torus(), 2),
            ('Klein', S.KleinBottle(), simplicial_complexes.KleinBottle(), 2),
            ('CP^2', S.ComplexProjectiveSpace(2), simplicial_complexes.ComplexProjectivePlane(), 4),
            ('S^3', S.Sphere(3), simplicial_complexes.Sphere(3), 3)]:
        check(all(invariants(X, d) == invariants(K, d) for d in range(top + 1)),
              'th:cellular-homology: cellular and simplicial homology agree (%s)' % name)
    for n in range(1, 8):
        C = S.RealProjectiveSpace(n).chain_complex()
        check(all(abs(C.differential(k)[0, 0]) == 1 + (-1) ** k for k in range(1, n + 1)),
              'p. 13: the cellular boundaries of RP^%d are 0, 2, 0, 2, ...' % n)

    # Lens spaces.
    for m, q in [(2, 1), (3, 1), (5, 1), (5, 2), (7, 3)]:
        C, full, regular = lens_space(m, q)
        check([sorted(C.homology(d).invariants()) for d in range(4)] == [[0], [m], [], [0]],
              'cellular homology of the lens space L(%d, %d): Z, Z/%d, 0, Z' % (m, q, m))
        check([complex_invariants(full, d) for d in range(4)] == [[0], [], [], [0]] and regular,
              'S^3 -> L(%d, %d): the cover is S^3, Z/%d acts regularly on each fibre' % (m, q, m))


# ---------------------------------------------------------------------------
# Section 1.6

def covering_data(d):
    """Transitive pairs (sigma, tau) of permutations of {0, ..., d-1}."""
    perms = list(itertools.permutations(range(d)))
    out = []
    for s in perms:
        for t in perms:
            seen = {0}
            stack = [0]
            while stack:
                i = stack.pop()
                for j in (s[i], t[i]):
                    if j not in seen:
                        seen.add(j)
                        stack.append(j)
            if len(seen) == d:
                out.append((s, t))
    return perms, out


def section_1_6():
    # lem:product-fibration: H = h x (pi_F f pi_X) on finite sets
    # (X = {0, 1}, I = {0, 1, 2} with end 0, B = F = {0, 1}).
    Xs, Ts, Bs, Fs = range(2), range(3), range(2), range(2)
    count = 0
    for hv in itertools.product(Bs, repeat=6):
        h = lambda x, t: hv[3 * x + t]
        for fv in itertools.product(Fs, repeat=2):
            f = lambda x: (h(x, 0), fv[x])        # p f = h i
            H = lambda x, t: (h(x, t), f(x)[1])
            assert all(H(x, 0) == f(x) for x in Xs)
            assert all(H(x, t)[0] == h(x, t) for x in Xs for t in Ts)
            count += 1
    check(count == 256, 'lem:product-fibration: H lifts h and extends f (256 cases)')

    # Examples p. 21.
    S = simplicial_sets
    G = libgap(S.Sphere(1).fundamental_group())
    check(list(G.AbelianInvariants()) == [0] and G.GeneratorsOfGroup().Length() == 1
          and S.Sphere(1).fundamental_group().relations() == (),
          'Examples p. 21: pi_1(S^1) = Z')
    for n in range(2, 6):
        RP = S.RealProjectiveSpace(n)
        U = RP.universal_cover()
        check(libgap(RP.fundamental_group()).Size() == 2
              and all(reduced_invariants(U, d) == ([0] if d == n else []) for d in range(n + 1))
              and len(U.n_cells(0)) == 2 * len(RP.n_cells(0)),
              'Examples p. 21: pi_1(RP^%d) = Z/2, the universal cover is S^%d, fibre of 2 points'
              % (n, n))
    G1 = libgap(S.RealProjectiveSpace(1).fundamental_group())
    refuted(G1.Size() == 2,
            'Examples p. 21 for n = 1: pi_1(RP^1) = Z/2 (it is Z: RP^1 = S^1, universal cover R)')
    T = S.Torus().fundamental_group()
    TG = libgap(T)
    f0, f1 = TG.FreeGroupOfFpGroup().GeneratorsOfGroup()
    check(list(TG.AbelianInvariants()) == [0, 0]
          and list(TG.RelatorsOfFpGroup()) == [libgap.Comm(f0 ** -1, f1)],
          'Examples p. 21: pi_1(T^2) = <a, b | [a^-1, b]> = Z^2')

    # th:universal-cover for B = S^1 v S^1, pi_1 = F_2 = <a, b>.
    F = libgap.FreeGroup(2)
    a, b = F.GeneratorsOfGroup()
    based = []
    classes = []
    for d in range(1, 5):
        perms, pairs = covering_data(d)
        based.append(len(pairs) // factorial(d - 1))
        orbits = set()
        for s, t in pairs:
            conj = []
            for c in perms:
                ci = [0] * d
                for i in range(d):
                    ci[c[i]] = i
                conj.append((tuple(c[s[ci[i]]] for i in range(d)),
                             tuple(c[t[ci[i]]] for i in range(d))))
            orbits.add(min(conj))
        classes.append(len(orbits))
        low = libgap.LowIndexSubgroupsFpGroup(F, d)
        gap_classes = sum(1 for H in low if F.Index(H) == d)
        check(len(orbits) == gap_classes,
              'th:universal-cover: connected %d-fold covers of S^1 v S^1 up to isomorphism = '
              'conjugacy classes of subgroups of index %d of F_2' % (d, d))
        # the image of pi_1(E', e'_0) is the stabiliser of e'_0 in F'
        all_ok = True
        for s, t in pairs:
            tree = {0: F.One()}
            order = [0]
            for i in order:
                for g, perm in ((a, s), (b, t)):
                    j = perm[i]
                    if j not in tree:
                        tree[j] = tree[i] * g
                        order.append(j)
            gens = [tree[i] * g * tree[perm[i]] ** -1
                    for i in range(d) for g, perm in ((a, s), (b, t))]
            img = libgap.Subgroup(F, gens)
            hom = libgap.GroupHomomorphismByImages(
                F, libgap.SymmetricGroup(max(d, 2)), [a, b],
                [libgap.PermList([x + 1 for x in s]), libgap.PermList([x + 1 for x in t])])
            # the generators fix the base point 0 (= 1 in GAP) and the index
            # is d = the index of the stabiliser (orbit of length d)
            fixes = all(libgap.OnPoints(1, libgap.Image(hom, w)) == 1 for w in gens)
            all_ok = all_ok and fixes and F.Index(img) == d
        check(all_ok, 'th:universal-cover proof: H = Im(pi_1(E\', e\'_0) -> pi_1(B, b_0)) is the '
              'stabiliser of the point e\'_0 of F\' (%d transitive actions of degree %d)'
              % (len(pairs), d))
    check(based == [1, 3, 13, 71] and classes == [1, 3, 7, 26],
          'th:universal-cover: based connected covers 1, 3, 13, 71; unbased 1, 3, 7, 26')


# ---------------------------------------------------------------------------
# Section 1.7

def section_1_7():
    Fr = Fraction

    def hat(c, w):
        return lambda x: max(Fr(0), 1 - abs(x - c) / w)

    def analyse(points, fs, opens, corrected):
        idx = range(len(fs))

        def W(S):
            return set(x for x in points
                       if all(fs[a](x) > fs[b](x) for a in S for b in idx if b not in S)
                       and (not corrected or all(fs[a](x) > 0 for a in S)))
        Sx = dict((x, frozenset(a for a in idx if fs[a](x) != 0)) for x in points)
        sets = set(Sx.values())
        Ws = dict((S, W(S)) for S in sets)
        ok_member = all(x in Ws[Sx[x]] for x in points)
        ok_disjoint = all(not (Ws[S] & Ws[T]) for S in sets for T in sets
                          if not S <= T and not T <= S)
        ok_contained = all(Ws[S] <= opens[a] for S in sets for a in S)
        mult = max(sum(1 for a in idx if x in opens[a]) for x in points)
        ok_bound = all(len(S) <= mult for S in sets)
        return ok_member, ok_disjoint, ok_contained, ok_bound

    # Two sets: U_1 = [0, 2/3), U_2 = (1/3, 1], f_1 + f_2 = 1.
    points = [Fr(k, 24) for k in range(25)]
    f1 = lambda x: Fr(1) if x <= Fr(1, 3) else (max(Fr(0), (Fr(2, 3) - x) * 3))
    f2 = lambda x: 1 - f1(x)
    U = [set(x for x in points if x < Fr(2, 3)), set(x for x in points if x > Fr(1, 3))]
    check(all(f1(x) + f2(x) == 1 and (f1(x) == 0 or x in U[0]) and (f2(x) == 0 or x in U[1])
              for x in points), 'def:partition-of-unity: f_1, f_2 subordinate to U_1, U_2')
    m, dsj, cont, bound = analyse(points, [f1, f2], U, corrected=False)
    check(m and dsj and bound, 'th:paracompact-countable-cover proof: x in W(S(x)), '
          'disjointness, |S(x)| <= n (two sets)')
    refuted(cont, 'th:paracompact-countable-cover proof: W(S(x)) is contained in U_alpha for '
            'alpha in S(x) (S(x) = {1, 2} gives W(S(x)) = X)')
    check(all(analyse(points, [f1, f2], U, corrected=True)),
          'th:paracompact-countable-cover proof with f_alpha > 0 in W(S): all four properties')
    # Five hats on [0, 1] and products of hats on [0, 1]^2.
    cs = [Fr(k, 4) for k in range(5)]
    raw = [hat(c, Fr(1, 4) + Fr(1, 8)) for c in cs]
    tot = lambda x: sum(g(x) for g in raw)
    fs = [(lambda g: (lambda x: g(x) / tot(x)))(g) for g in raw]
    opens = [set(x for x in points if g(x) > 0) for g in raw]
    for corrected in (False, True):
        check(all(analyse(points, fs, opens, corrected)),
              'th:paracompact-countable-cover proof: five sets on [0, 1] (corrected = %s)'
              % corrected)
    grid = [(Fr(i, 8), Fr(j, 8)) for i in range(9) for j in range(9)]
    raw2 = [(lambda g, h: (lambda p: g(p[0]) * h(p[1])))(g, h) for g in raw[::2] for h in raw[::2]]
    tot2 = lambda p: sum(g(p) for g in raw2)
    fs2 = [(lambda g: (lambda p: g(p) / tot2(p)))(g) for g in raw2]
    opens2 = [set(p for p in grid if g(p) > 0) for g in raw2]
    check(all(tot2(p) > 0 for p in grid) and all(analyse(grid, fs2, opens2, True)),
          'th:paracompact-countable-cover proof (corrected): nine sets on [0, 1]^2')


# ---------------------------------------------------------------------------
# Section 1.8: helpers

def kan_suspension(X, x0, N, name):
    """Kan's suspension S X by the formulas of p. 25: n-simplices * and
    (i, x), i >= 1, x in X_(n-i), with (i, s_0^k x0) identified with *."""
    base_deg = [x0]
    for k in range(N):
        base_deg.append(X.degen(0, base_deg[-1]))

    def norm(n, i, x):
        return (n, ('*',)) if x == base_deg[x[0]] else (n, (i, x))
    S = []
    for n in range(N + 1):
        layer = [(n, ('*',))]
        for i in range(1, n + 1):
            layer += [(n, (i, x)) for x in X.S[n - i] if x != base_deg[n - i]]
        S.append(layer)

    def degen(j, z):
        n, a = z
        if a == ('*',):
            return (n + 1, ('*',))
        i, x = a
        if j == 0:
            return (n + 1, (i + 1, x))
        if i == 1:
            return norm(n + 1, 1, X.degen(j - 1, x))
        return degen(0, degen(j - 1, (n - 1, (i - 1, x))))

    def face(j, z):
        n, a = z
        if a == ('*',):
            return (n - 1, ('*',))
        i, x = a
        if i == 1:
            if j == 0 or x[0] == 0:
                return (n - 1, ('*',))
            return norm(n - 1, 1, X.face(j - 1, x))
        if j in (0, 1):
            return (n - 1, (i - 1, x))
        return degen(0, face(j - 1, (n - 1, (i - 1, x))))
    return SSet(name, S, face, degen)


def closure(X, gens):
    """The simplicial subset generated by gens (faces and degeneracies)."""
    out = set()
    todo = list(gens)
    while todo:
        x = todo.pop()
        if x in out:
            continue
        out.add(x)
        n = x[0]
        if n > 0:
            todo += [X.face(i, x) for i in range(n + 1)]
        if n < X.N:
            todo += [X.degen(i, x) for i in range(n + 1)]
    return out


def chain_add(c, x, v):
    c[x] = c.get(x, 0) + v
    if c[x] == 0:
        del c[x]


def apply_degens(X, x, idx):
    """s_(idx[-1]) ... s_(idx[0]) x, or None when an index is too large."""
    for j in idx:
        if j > x[0]:
            return None
        x = X.degen(j, x)
    return x


def shuffles(p, q, labels):
    out = []
    for mu in itertools.combinations(labels, p):
        nu = tuple(v for v in labels if v not in mu)
        seq = list(mu) + list(nu)
        inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
        out.append((mu, nu, (-1) ** inv))
    return out


def eilenberg_zilber(X, Y, x, y, labels_shift=0, sign_rule=None):
    """nabla(x (x) y) in the chains of X x Y; labels {0, ..., n-1} shifted."""
    p, q = x[0], y[0]
    n = p + q
    c = {}
    for mu, nu, sg in shuffles(p, q, range(labels_shift, n + labels_shift)):
        a = apply_degens(X, x, nu)
        b = apply_degens(Y, y, mu)
        if a is None or b is None:
            return None
        chain_add(c, (n, (a, b)), sg if sign_rule is None else sign_rule)
    return c


def chain_boundary(X, c):
    out = {}
    for x, v in c.items():
        for i in range(x[0] + 1):
            chain_add(out, X.face(i, x), v * (-1) ** i)
    return out


def alexander_whitney(X, Y, z):
    """AW(x, y) = sum_i (front i-face of x) (x) (back (n-i)-face of y)."""
    n, (x, y) = z
    out = {}
    for i in range(n + 1):
        a = x
        for k in range(n, i, -1):
            a = X.face(k, a)
        b = y
        for _ in range(i):
            b = Y.face(0, b)
        chain_add(out, (a, b), 1)
    return out


def tensor_boundary(X, Y, c):
    out = {}
    for (a, b), v in c.items():
        if a[0] > 0:
            for i in range(a[0] + 1):
                chain_add(out, (X.face(i, a), b), v * (-1) ** i)
        if b[0] > 0:
            for i in range(b[0] + 1):
                chain_add(out, (a, Y.face(i, b)), v * (-1) ** (a[0] + i))
    return out


def modulo_degenerate(X, c):
    return dict((x, v) for x, v in c.items() if not X.is_degenerate(x))


def free_vector_space_on(X, name):
    """The simplicial F_2-vector space F_2[X] (a simplicial group)."""
    S = []
    for n in range(X.N + 1):
        basis = X.S[n]
        S.append([(n, frozenset(b for b, e in zip(basis, bits) if e))
                  for bits in itertools.product((0, 1), repeat=len(basis))])

    def face(i, v):
        out = set()
        for b in v[1]:
            out ^= {X.face(i, b)}
        return (v[0] - 1, frozenset(out))

    def degen(i, v):
        out = set()
        for b in v[1]:
            out ^= {X.degen(i, b)}
        return (v[0] + 1, frozenset(out))
    return SSet(name, S, face, degen)


def sset_induced_rank(Xs, Xl, k, F):
    """Rank of H_k(Xs; F) -> H_k(Xl; F) for a simplicial subset Xs of Xl."""
    Cs, bs = normalized_complex(Xs, ring=F)
    Cl, bl = normalized_complex(Xl, ring=F)
    idx = dict((x, i) for i, x in enumerate(bl[k]))
    Z = Cs.differential(k).right_kernel().basis() if k > 0 else \
        [vector(F, [1 if j == i else 0 for j in range(len(bs[0]))]) for i in range(len(bs[0]))]
    emb = []
    for z in Z:
        v = vector(F, [0] * len(bl[k]))
        for i, x in enumerate(bs[k]):
            v[idx[x]] = z[i]
        emb.append(v)
    Bc = Cl.differential(k + 1).columns()
    rB = matrix(F, Bc).rank() if Bc else 0
    both = Bc + emb
    return (matrix(F, both).rank() if both else 0) - rB


# ---------------------------------------------------------------------------
# Section 1.8

def section_1_8():
    # The face and degeneracy maps of the category Delta (p. 23).
    def delta_i(i):
        return lambda j: j if j < i else j + 1

    def sigma_i(i):
        return lambda j: j if j <= i else j - 1

    def same(f, g, dom):
        return all(f(j) == g(j) for j in range(dom))
    ok = True
    for n in range(1, 8):
        # relations of d_i, s_j on X_n read in Delta (contravariance)
        for j in range(n + 1):
            for i in range(j):
                if n >= 2:
                    ok &= same(lambda k: delta_i(j)(delta_i(i)(k)),
                               lambda k: delta_i(i)(delta_i(j - 1)(k)), n - 1)
        for j in range(n + 1):
            for i in range(n + 2):
                comp = lambda k: sigma_i(j)(delta_i(i)(k))
                if i < j:
                    ok &= same(comp, lambda k: delta_i(i)(sigma_i(j - 1)(k)), n + 1)
                elif i in (j, j + 1):
                    ok &= same(comp, lambda k: k, n + 1)
                else:
                    ok &= same(comp, lambda k: delta_i(i - 1)(sigma_i(j)(k)), n + 1)
            for i in range(j + 1):
                ok &= same(lambda k: sigma_i(j)(sigma_i(i)(k)),
                           lambda k: sigma_i(i)(sigma_i(j + 1)(k)), n + 2)
    check(ok, 'p. 23: the face and degeneracy maps of Delta satisfy the five relations (n <= 7)')
    # Normal form: every monotone map [m] -> [n] is delta_(i_1)...delta_(i_s)
    # sigma_(j_1)...sigma_(j_t), i_1 > ... > i_s, j_1 < ... < j_t, uniquely.
    for m in range(0, 5):
        for n in range(0, 5):
            maps = set(f for f in itertools.combinations_with_replacement(range(n + 1), m + 1))
            words = []
            for t in range(m + 1):
                s = n - (m - t)
                if s < 0:
                    continue
                for js in itertools.combinations(range(m), t):
                    for is_ in itertools.combinations(range(n + 1), s):
                        def f(k, js=js, is_=is_):
                            for j in reversed(js):           # sigma_(j_t) first
                                k = sigma_i(j)(k)
                            for i in sorted(is_):            # delta_(i_s) first
                                k = delta_i(i)(k)
                            return k
                        words.append(tuple(f(k) for k in range(m + 1)))
            check(len(words) == len(set(words)) == len(maps) == binomial(m + n + 1, m + 1)
                  and set(words) == maps,
                  'p. 23: normal form of the maps of Delta, [%d] -> [%d]' % (m, n))

    # The topological maps d^i, s^i (p. 24).
    for n in range(1, 6):
        R = PolynomialRing(QQ, ['x%d' % k for k in range(n + 2)])
        xs = list(R.gens())

        def d_top(i, v):
            return v[:i] + [R(0)] + v[i:]

        def d_printed(i, v):
            return v[:i + 1] + [R(0)] + v[i + 1:] if i + 1 <= len(v) else None

        def s_top(i, v):
            return v[:i] + [v[i] + v[i + 1]] + v[i + 2:]
        e = lambda k, size: [R(1) if a == k else R(0) for a in range(size)]
        check(all(d_top(i, e(k, n)) == e(delta_i(i)(k), n + 1) for i in range(n + 1) for k in range(n)),
              'p. 24 corrected: d^i is the affine map of the i-th face map (n = %d)' % n)
        refuted(all(d_printed(i, e(k, n)) == e(delta_i(i)(k), n + 1)
                    for i in range(n) for k in range(n)),
                'p. 24 printed: d^i(x_0, ..., x_(n-1)) = (x_0, ..., x_i, 0, x_(i+1), ...)')
        refuted(n == 0 or d_printed(n, xs[:n]) is not None,
                'p. 24 printed: d^n needs a coordinate x_n of an (n-1)-simplex')
        check(all(s_top(i, e(k, n + 2)) == e(sigma_i(i)(k), n + 1)
                  for i in range(n + 1) for k in range(n + 2)),
              'p. 24: s^i is the affine map of the i-th degeneracy map (n = %d)' % n)
        v = xs[:n]
        rel = all(d_top(j, d_top(i, v[:n - 1])) == d_top(i, d_top(j - 1, v[:n - 1]))
                  for j in range(1, n + 1) for i in range(j)) if n >= 2 else True
        w = xs[:n + 1]
        rel &= all(s_top(j, d_top(i, w)) == (d_top(i, s_top(j - 1, w)) if i < j else
                                              (w if i in (j, j + 1) else d_top(i - 1, s_top(j, w))))
                   for j in range(n + 1) for i in range(n + 2)
                   if not (i < j and j == 0))
        u = xs[:n + 2]
        rel &= all(s_top(i, s_top(j + 1, u)) == s_top(j, s_top(i, u))
                   for j in range(n) for i in range(j + 1))
        check(rel, 'p. 24: d^i, s^i satisfy the relations with the order reversed (n = %d)' % n)

    # Delta[n] (p. 24).
    for n in range(0, 5):
        D = delta(n, 5)
        check(all(len(D.S[r]) == binomial(n + r + 1, r + 1) and
                  len(D.nondegenerate(r)) == binomial(n + 1, r + 1) for r in range(6))
              and relations_hold(D),
              'p. 24: Delta[%d]: counts of simplices and the relations' % n)
        check(all(len(set(D.degen(i, x) for x in D.S[r])) == len(D.S[r])
                  for r in range(5) for i in range(r + 1)),
              'p. 24: the s_i are injective on Delta[%d]' % n)

    # Delta[1] x Delta[1] (p. 25) and Delta[p] x Delta[q].
    P = product(delta(1, 4), delta(1, 4))
    nd = [set((x, y) for _, (x, y) in [(z[0], z[1]) for z in P.nondegenerate(r)]) for r in range(5)]
    seq = lambda s: (len(s) - 1, tuple(int(c) for c in s))
    check(len(P.S[0]) == 4 and nd[1] == set((seq(a), seq(b)) for a, b in
                                             [('00', '01'), ('01', '00'), ('01', '01'),
                                              ('01', '11'), ('11', '01')])
          and nd[2] == {(seq('001'), seq('011')), (seq('011'), seq('001'))}
          and not nd[3] and not nd[4],
          'p. 25: Delta[1] x Delta[1] has 4, 5, 2 non-degenerate simplices as listed')
    check(relations_hold(P) and sset_invariants(P, 0) == [0]
          and all(sset_invariants(P, d) == [] for d in (1, 2, 3)),
          'p. 25: |Delta[1] x Delta[1]| is a (contractible) square')
    for p in range(0, 4):
        for q in range(0, 4):
            if p + q > 5:
                continue
            Q = product(delta(p, p + q + 1), delta(q, p + q + 1))
            check(len(Q.nondegenerate(p + q)) == binomial(p + q, p)
                  and not Q.nondegenerate(p + q + 1),
                  'p. 25: Delta[%d] x Delta[%d] has binomial(p+q, p) top simplices' % (p, q))

    # Kan's suspension (p. 25).
    N = 5
    cases = [
        ('S[1]', sphere(1, N), (0, '*')),
        ('S[2]', sphere(2, N), (0, '*')),
        ('Delta[1]', delta(1, N), (0, (0,))),
        ('boundary Delta[2]', restrict(delta(2, N), lambda x: len(set(x[1])) < 3, 'bd'),
         (0, (0,))),
        ('Delta[1] x Delta[1]', product(delta(1, N), delta(1, N)), (0, ((0, (0,)), (0, (0,))))),
        ('S[1] x Delta[1]', product(sphere(1, N), delta(1, N)), (0, ((0, '*'), (0, (0,))))),
    ]
    for name, X, x0 in cases:
        SX = kan_suspension(X, x0, N, 'S' + name)
        check(relations_hold(SX), 'p. 25: Kan\'s suspension of %s is a simplicial set' % name)
        cells_ok = all(len(SX.nondegenerate(n)) ==
                       len([x for x in X.nondegenerate(n - 1) if x != x0])
                       for n in range(1, N + 1)) and len(SX.nondegenerate(0)) == 1
        check(cells_ok, 'p. 25: the cells of S X are * and the (1, x), x non-degenerate, '
              'x != x0 (%s)' % name)
        Xr = [sset_invariants(X, d) for d in range(N - 1)]
        Xr[0] = Xr[0][1:]                      # reduced H_0
        check(all(sset_invariants(SX, d + 1) == Xr[d] for d in range(N - 2))
              and sset_invariants(SX, 0) == [0],
              'p. 25: |S X| = S|X|: H~_(d+1)(S X) = H~_d(X) (%s)' % name)

    # Horns (p. 25).
    for n in range(1, 5):
        D = delta(n, n + 1)
        sigma = (n, tuple(range(n + 1)))
        for i in range(n + 1):
            horn = set(x for r in range(n + 2) for x in D.S[r]
                       if not (set(range(n + 1)) - {i}) <= set(x[1]))
            gen = closure(D, [D.face(k, sigma) for k in range(n + 1) if k != i])
            check(gen == horn, 'p. 25 corrected: Delta[%d, %d] is generated by the d_k sigma, '
                  'k != i, and its realisation is {x_j = 0 for some j != i}' % (n, i))
            if i >= 1:
                printed = closure(D, [D.face(k, sigma) for k in range(1, n + 1) if k != i])
                refuted(printed == horn, 'p. 25 printed: Delta[%d, %d] generated by '
                        'd_1 sigma, ..., d_(i-1) sigma, d_(i+1) sigma, ...' % (n, i))
            H = restrict(D, lambda x: x in horn, 'horn')
            check(sset_invariants(H, 0) == [0] and all(sset_invariants(H, d) == [] for d in range(1, n + 1))
                  and len([x for r in range(n + 1) for x in H.nondegenerate(r)])
                  == len(simplicial_sets.Horn(n, i).nondegenerate_simplices()),
                  'p. 25: Delta[%d, %d] is acyclic and has the cells of Sage\'s horn' % (n, i))

    # Kan complexes (p. 26).
    D1 = delta(1, 3)
    refuted(horn_data_fill(D1, 2, 0) and horn_data_fill(D1, 2, 2),
            'p. 26: every simplicial set is a Kan complex (Delta[1] is not)')
    BZ3 = group_nerve(CyclicPermutationGroup(3), 3, 'BZ/3')
    BS3 = group_nerve(SymmetricGroup(3), 3, 'BS_3')
    for name, X in [('BZ/3', BZ3), ('BS_3', BS3)]:
        check(all(horn_data_fill(X, n, i) for n in (1, 2, 3) for i in range(n + 1)),
              'p. 26: the nerve %s fills all horns (n <= 3)' % name)
    F2D1 = free_vector_space_on(delta(1, 3), 'F2[Delta[1]]')
    check(relations_hold(F2D1)
          and all(horn_data_fill(F2D1, n, i) for n in (1, 2, 3) for i in range(n + 1)),
          'p. 26 (May, Theorem 17.1): the simplicial group F_2[Delta[1]] fills all horns '
          '(n <= 3)')

    # Homotopies (p. 26): bold d^0 : Delta[0] -> Delta[1] picks the vertex 1.
    check(delta_i(0)(0) == 1 and delta_i(1)(0) == 0,
          'p. 26: F (id x d^0) is the end 1, F (id x d^1) the end 0 of the homotopy')
    rel = set()
    for z in delta(1, 1).S[1]:
        a = z[1]
        rel.add((a[delta_i(0)(0)], a[delta_i(1)(0)]))
    check((1, 0) in rel and (0, 1) not in rel,
          'p. 26: for maps into Delta[1] (not Kan) homotopy is not symmetric')

    # Hom(X, Y) (p. 25): Hom(S[1], S[1]).
    S1 = sphere(1, 2)
    maps0, _ = simplicial_maps(S1, S1, 1)
    P1 = product(sphere(1, 2), delta(1, 2))
    maps1, image = simplicial_maps(P1, S1, 2)
    sig = (1, (0, 1))

    def end(F, v):
        return image(F, (1, (sig, (1, (v, v)))))
    edges = set((end(F, 1), end(F, 0)) for F in maps1)
    verts = set(m[sig] for m in maps0)
    comp = dict((v, v) for v in verts)
    for u, w in edges:
        cu, cw = comp[u], comp[w]
        for k in comp:
            if comp[k] == cw:
                comp[k] = cu
    check(len(maps0) == 2 and len(set(comp.values())) == 2,
          'p. 25: Hom(S[1], S[1]) has 2 vertices (id, constant) in 2 components')
    G1 = libgap(simplicial_sets.Sphere(1).fundamental_group())
    refuted(G1.Size() == len(set(comp.values())),
            'p. 25: |Hom(S[1], S[1])| -> Map(S^1, S^1) is a homotopy equivalence '
            '(pi_0: 2 against [S^1; S^1] = conjugacy classes of pi_1(S^1) = Z)')
    BZ2 = group_nerve(CyclicPermutationGroup(2), 2, 'BZ/2')
    maps0, _ = simplicial_maps(S1, BZ2, 1)
    maps1, image = simplicial_maps(P1, BZ2, 2)
    edges = set((image(F, (1, (sig, (1, (1, 1))))), image(F, (1, (sig, (1, (0, 0))))))
                for F in maps1)
    check(len(maps0) == 2 and all(u == w for u, w in edges),
          'p. 25: Hom(S[1], BZ/2) (Kan): 2 components = [S^1; BZ/2] (conjugacy classes of Z/2)')

    # S[n] and pi_n (p. 26).
    for n in range(1, 5):
        Sn = sphere(n, n + 2)
        check([len(Sn.nondegenerate(r)) for r in range(n + 3)] ==
              [1] + [0] * (n - 1) + [1, 0, 0]
              and [sset_invariants(Sn, d) for d in range(n + 2)] ==
              [[0]] + [[]] * (n - 1) + [[0], []],
              'p. 26: S[%d] has one non-degenerate 0- and %d-simplex, |S[n]| = S^n' % (n, n))
    G = SymmetricGroup(3)
    BG = group_nerve(G, 2, 'BS3')
    base1 = BG.degen(0, (0, ('*',)))
    related = set()
    for z in BG.S[2]:
        if BG.face(0, z) == base1:
            related.add((BG.face(1, z), BG.face(2, z)))
    check(all(u == w for u, w in related) and len(BG.S[1]) == 6,
          'p. 26: pi_1(BS_3, *) = S_3: the relation on 1-simplices is equality')

    # Normalized chains (p. 26-27).
    for name, X in [('Delta[2]', delta(2, 4)), ('Delta[1]xDelta[1]', product(delta(1, 4), delta(1, 4))),
                    ('S[2]', sphere(2, 4)), ('BZ/2', group_nerve(CyclicPermutationGroup(2), 4, 'BZ/2')),
                    ('BZ/3', group_nerve(CyclicPermutationGroup(3), 4, 'BZ/3')),
                    ('S[1]xS[1]', product(sphere(1, 3), sphere(1, 3))),
                    ('S S[1]', kan_suspension(sphere(1, 4), (0, '*'), 4, 'SS1'))]:
        check(degenerate_subcomplex_acyclic(X)
              and all(unnormalized_invariants(X, d) == sset_invariants(X, d) for d in range(X.N)),
              'p. 26: degenerate subcomplex acyclic, same homology as the normalized chains (%s)'
              % name)
    check(sset_invariants(group_nerve(CyclicPermutationGroup(3), 4, 'BZ/3'), 1) == [3]
          and sset_invariants(group_nerve(CyclicPermutationGroup(3), 4, 'BZ/3'), 2) == []
          and sset_invariants(group_nerve(CyclicPermutationGroup(3), 4, 'BZ/3'), 3) == [3],
          'p. 26: H_*(BZ/3) = Z, Z/3, 0, Z/3 (group homology)')

    # Eilenberg-Zilber (p. 27).
    for p in range(0, 4):
        for q in range(0, 4):
            n = p + q
            if n > 6 or n == 0:
                continue
            X, Y = delta(p, n), delta(q, n)
            P = product(X, Y)
            ip, iq = (p, tuple(range(p + 1))), (q, tuple(range(q + 1)))
            check(len(shuffles(p, q, range(n))) == binomial(n, p),
                  'p. 27: there are binomial(n, p) (p, q)-shuffles')
            refuted(eilenberg_zilber(X, Y, ip, iq, labels_shift=1) is not None,
                    'p. 27 printed: shuffles of {1, ..., n} (s_n is not defined on '
                    '(n-1)-simplices), p = %d, q = %d' % (p, q))
            nab = eilenberg_zilber(X, Y, ip, iq)
            check(nab is not None and set(nab) == set(P.nondegenerate(n)),
                  'p. 27: with shuffles of {0, ..., n-1} the terms are the top simplices of '
                  'Delta[%d] x Delta[%d]' % (p, q))
            lhs = chain_boundary(P, nab)
            rhs = {}
            for i in range(p + 1):
                if p > 0:
                    for k, v in eilenberg_zilber(X, Y, X.face(i, ip), iq).items():
                        chain_add(rhs, k, v * (-1) ** i)
            for i in range(q + 1):
                if q > 0:
                    for k, v in eilenberg_zilber(X, Y, ip, Y.face(i, iq)).items():
                        chain_add(rhs, k, v * (-1) ** (p + i))
            check(lhs == rhs, 'p. 27: nabla is a chain map (universal case p = %d, q = %d)' % (p, q))
            if p == q == 1:
                bad = eilenberg_zilber(X, Y, ip, iq, sign_rule=-1)
                rhs_bad = {}
                for i in range(2):
                    for k, v in eilenberg_zilber(X, Y, X.face(i, ip), iq, sign_rule=-1).items():
                        chain_add(rhs_bad, k, v * (-1) ** i)
                    for k, v in eilenberg_zilber(X, Y, ip, Y.face(i, iq), sign_rule=-1).items():
                        chain_add(rhs_bad, k, v * (-1) ** (1 + i))
                refuted(chain_boundary(P, bad) == rhs_bad,
                        'p. 27: (-1)^epsilon with epsilon = +-1 (all signs equal)')
            aw = {}
            for z, v in nab.items():
                for k, w in alexander_whitney(X, Y, z).items():
                    chain_add(aw, k, v * w)
            aw = dict((k, v) for k, v in aw.items()
                      if not X.is_degenerate(k[0]) and not Y.is_degenerate(k[1]))
            check(aw == {(ip, iq): 1}, 'p. 27: AW nabla = id on normalized chains (p = %d, q = %d)'
                  % (p, q))
    for n in range(1, 6):
        X = delta(n, n)
        P = product(X, X)
        z = (n, ((n, tuple(range(n + 1))), (n, tuple(range(n + 1)))))
        lhs = tensor_boundary(X, X, alexander_whitney(X, X, z))
        rhs = {}
        for i in range(n + 1):
            for k, v in alexander_whitney(X, X, P.face(i, z)).items():
                chain_add(rhs, k, v * (-1) ** i)
        check(lhs == rhs, 'p. 27: Alexander-Whitney is a chain map (universal case n = %d)' % n)
    S1 = sphere(1, 3)
    T = product(S1, S1)
    sig = (1, (0, 1))
    nab = modulo_degenerate(T, eilenberg_zilber(S1, S1, sig, sig))
    C, basis = normalized_complex(T)
    vec = vector(ZZ, [nab.get(x, 0) for x in basis[2]])
    K = C.differential(2).right_kernel()
    check(K.rank() == 1 and vec in K and K.basis()[0] in (vec, -vec)
          and sset_invariants(T, 2) == [0],
          'p. 27: nabla(sigma (x) sigma) generates H_2(S[1] x S[1]) = Z')

    # Exercise p. 27: nerves.
    for n in range(0, 4):
        objs = list(range(n + 1))
        mors = [(a, b) for a in objs for b in objs if a <= b]
        Nn = nerve(objs, mors, lambda f: f[0], lambda f: f[1], lambda g, f: (f[0], g[1]),
                   lambda c: (c, c), 4, '[%d]' % n)
        check(relations_hold(Nn) and all(len(Nn.S[r]) == binomial(n + r + 1, r + 1) for r in range(5)),
              'Exercise p. 27: the nerve of [%d] is Delta[%d]' % (n, n))
    kron = nerve(['x', 'y'], ['ix', 'iy', 'a', 'b'],
                 lambda f: 'y' if f == 'iy' else 'x', lambda f: 'x' if f == 'ix' else 'y',
                 lambda g, f: g if f in ('ix', 'iy') else f, lambda c: 'i' + c, 3, 'Kronecker')
    check(relations_hold(kron) and sset_invariants(kron, 1) == [0] and sset_invariants(kron, 2) == [],
          'Exercise p. 27: the nerve of the Kronecker category is a circle')
    check(relations_hold(BS3) and relations_hold(group_nerve(CyclicPermutationGroup(3), 4, 'BZ3')),
          'Exercise p. 27: nerves of groups satisfy the relations')
    for name, K in [('boundary of the 3-simplex', simplicial_complexes.Sphere(2)),
                    ('2-simplex', simplicial_complexes.Simplex(2)),
                    ('RP^2', simplicial_complexes.RealProjectivePlane()),
                    ('T^2', simplicial_complexes.Torus())]:
        faces = [frozenset(f) for d in range(K.dimension() + 1) for f in K.n_faces(d)]
        mors = [(a, b) for a in faces for b in faces if a <= b]
        top = K.dimension() + 1
        Nf = nerve(faces, mors, lambda f: f[0], lambda f: f[1], lambda g, f: (f[0], g[1]),
                   lambda c: (c, c), top, 'face poset')
        fv = K.barycentric_subdivision().f_vector()
        check(all(len(Nf.nondegenerate(r)) == fv[r + 1] for r in range(top))
              and not Nf.nondegenerate(top)
              and all(sset_invariants(Nf, d) == sorted(K.homology(reduced=False)[d].invariants()) for d in range(top)),
              'Exercise p. 27: the nerve of the face poset of %s is its barycentric subdivision'
              % name)


# ---------------------------------------------------------------------------
# Section 1.9

def section_1_9():
    def perm_mul(p, q):
        return tuple(p[q[i]] for i in range(len(q)))

    def perm_inv(p):
        out = [0] * len(p)
        for i, v in enumerate(p):
            out[v] = i
        return tuple(out)
    S3 = list(itertools.permutations(range(3)))
    S2 = list(itertools.permutations(range(2)))
    C3 = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]

    def sign(p):
        return (0, 1) if perm_sign(p, lambda v: v) == 1 else (1, 0)
    mult = (perm_mul, perm_inv)
    towers = [
        ('S_3 = S_3 -> S_2', [S2, S3, S3], [sign, lambda p: p], mult),
        ('C_3 -> S_3 -> S_2', [S2, S3, C3], [sign, lambda p: p], mult),
    ]
    for name, Gs, alphas, (mul, inv) in towers:
        e = [tuple(range(len(G[0]))) for G in Gs]

        def act(g, x):
            return tuple(mul(mul(g[k], x[k]), inv(alphas[k](g[k + 1]))) for k in range(len(x)))
        gs = list(itertools.product(*Gs))
        xs = list(itertools.product(*Gs[:-1]))
        ok = all(act(tuple(mul(g[k], h[k]) for k in range(3)), x) == act(g, act(h, x))
                 for g in gs for h in gs for x in xs)
        ok &= all(act(tuple(e), x) == x for x in xs)
        check(ok, 'p. 28: the formula is a left action of prod G_n on prod G_n (%s)' % name)
        stab = set(g for g in gs if act(g, tuple(e[:-1])) == tuple(e[:-1]))
        threads = set(g for g in gs if all(g[k] == alphas[k](g[k + 1]) for k in range(2)))
        check(stab == threads, 'p. 28: the stabiliser of (1, 1, ...) is lim G_n (%s)' % name)
    # abelian: Z/4 <-2- Z/4 <-2- Z/4: orbits are the cosets of Im(partial)
    m = 4
    G = list(range(m))
    gs = list(itertools.product(G, repeat=3))
    xs = list(itertools.product(G, repeat=2))
    alpha = lambda a: (2 * a) % m
    act = lambda g, x: tuple((g[k] + x[k] - alpha(g[k + 1])) % m for k in range(2))
    image = set(tuple((g[k] - alpha(g[k + 1])) % m for k in range(2)) for g in gs)
    check(all(set(act(g, x) for g in gs) == set(tuple((x[k] + d[k]) % m for k in range(2))
                                                   for d in image) for x in xs),
          'p. 28: for abelian groups the orbits are the cosets of the image of '
          'partial(g)_n = g_n - alpha(g_(n+1)), so lim^1 is the cokernel (Volume I, Section 4.1)')

    # th:milnor-exact-sequence for X = BZ/2 = RP^infinity with skeleta X_n and
    # Y = K(Z/2, k): [X_n; Y] = H^k(X_n; F_2), [S X_n; Y] = H^(k-1)(X_n; F_2).
    N = 6
    B = group_nerve(CyclicPermutationGroup(2), N, 'BZ/2')
    e = CyclicPermutationGroup(2).identity()
    F = GF(2)

    def skel(n):
        return restrict(B, lambda x: x[0] == 0 or sum(1 for g in x[1][1:] if g != e) <= n, 'X%d' % n)

    def bettis(X):
        C, basis = normalized_complex(X, ring=F)
        out = []
        for d in range(N - 1):
            dim = len(basis[d])
            r1 = C.differential(d).rank() if d > 0 else 0
            r2 = C.differential(d + 1).rank()
            out.append(dim - r1 - r2)
        return out
    skels = [skel(n) for n in range(1, N - 1)]
    table = [bettis(X) for X in skels]
    full = bettis(B)
    for k in range(1, 4):
        tower = [table[n - 1][k] for n in range(1, N - 1)]
        maps_iso = all(sset_induced_rank(skels[n - 1], skels[n], k, F) == 1
                       for n in range(k + 1, N - 2))
        check(all(tower[n - 1] == full[k] == 1 for n in range(k + 1, N - 1)) and maps_iso,
              'th:milnor-exact-sequence: H^%d(X_n; F_2) -> H^%d(X_(n-1); F_2) are isomorphisms '
              'of F_2 for n > %d + 1: lim^1 = 0 and [X; Y] = lim [X_n; Y] = H^%d(BZ/2; F_2)'
              % (k, k, k, k))


def main():
    section_1_1()
    section_1_2()
    section_1_3()
    section_1_4()
    section_1_5()
    section_1_6()
    section_1_7()
    section_1_8()
    section_1_9()
    print(f'ok chapter-1: {COUNT[0]} checks')


if __name__ == '__main__':
    main()
