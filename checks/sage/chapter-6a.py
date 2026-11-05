"""Exact checks of Chapter 6, Sections 6.1-6.6 (Sage, GAP through libgap).

Run: sage -python checks/sage/chapter-6a.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-6a: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 6, Sections
6.1-6.6, printed pp. 215-226.  Our files: content/06-01-g-simplicial-complexes.typ
... content/06-06-subgroup-complexes.typ (Sections 6.7-6.9: chapter-6b.py).
Pages are printed pages; labels are those of content/06-*.typ.  Expected
values are the book's statements read off the printed pages; where the
printed text was corrected, the printed reading is kept as a refuted check
(`refuted`) beside the corrected one.

Conventions.  A poset X is realised by its order complex |X| (chains
x_0 < ... < x_n, oriented by the order); chi is the Euler characteristic and
chi~ = chi - 1 the reduced one; for a G-poset X the marks of the Lefschetz
invariant are chi(X^H) (p. 220).  Subgroup posets S_p(G), A_p(G), B_p(G)
(p. 218) and Z_p(G) (Exercise of Section 6.6) are computed in GAP from the
subgroups of a Sylow p-subgroup and their G-conjugates; G acts by
conjugation.  "Acyclic" means that the reduced homology vanishes with the
stated coefficients (Z where the matrices are small, else F_p and F_l for
the prime l of the docstring); this is what a computation can see of
"contractible".  The group range RANGE is: all groups of order at most 100
in GAP's library of small groups except those of order 96 and the groups of
prime-power order bigger than 16 (each of which has O_p(G) = G), for every
prime p dividing the order (455 groups, 943 pairs (G, p)).

What is checked, by section:

section_6_1 (pp. 215-217): Definition 6.1.1 (def:g-simplicial-complex) on
  the examples of the text (Z/2 swapping the ends of an edge, Z/3 rotating a
  triangle: not G-simplicial; their barycentric subdivisions and the boundary
  of the triangle: G-simplicial) and for every subgroup of S_n acting on the
  simplex and its boundary (n <= 4): the subdivision is always G-simplicial;
  the chain group C_n (def:chain-group) is a permutation module in the
  G-simplicial case and is not one in the example of the edge (C_1 is the
  sign representation); d o d = 0 and d is G-linear; reduced homology
  (def:augmented-chain-complex) of two points and of a circle.
section_6_2 (pp. 217-218): the order complex and its boundary; S(Delta) and
  sd(Delta) = |S(Delta)| (def:barycentric-subdivision) against Sage's
  barycentric subdivision (f-vectors, integral homology) for the 2-sphere,
  the torus, RP^2 and the Klein bottle; the Exercise (sd(Delta) and Delta are
  G-homeomorphic) through the Lefschetz numbers: chi(S(Delta)^g) =
  sum (-1)^i tr(g, H_i(Delta; Q)) for all g in S_4 on the boundary of the
  tetrahedron and for the examples of section_6_1 (where the pointwise fixed
  subcomplex of the edge is empty, but |Delta|^g is the midpoint); the
  subgroup posets: A_p(G), B_p(G) are subposets of S_p(G) containing the
  Sylow subgroups (B_p) and S_p(G) u {1} has chi = 1 (it is a cone);
  invertible systems (def:invertible-system): on the poset of a circle
  (a, b < c, d) the system with monodromy a shift of Z/n gives a connected
  poset X~ whose realisation is a 4n-cycle (a connected n-fold covering),
  the trivial one n copies of X.
section_6_3 (pp. 218-220): prop:euler-characteristic-zero by characters
  over Q: the characters of the homology H_i(Delta; Q) computed from the
  induced action on cycles mod boundaries, against the permutation
  characters of the chain groups, for S_4 on sd of the boundary of the
  tetrahedron, S_4 on S_2(S_4), A_5 on S_2(A_5), GL_3(2) on B_2(GL_3(2));
  chi = sum (-1)^i dim H_i; the Lefschetz invariant (def:lefschetz-invariant)
  computed as sum (-1)^i [G/Stab(sigma)] over the orbits of chains and
  mapped to marks (fixed cosets) equals the vector chi(X^H) computed from the
  fixed subposets (p. 220), for X = S_p, A_p, B_p of S_4, A_5, GL_2(3),
  GL_3(2), S_5 (all classes of subgroups H); Exercise 1 (Brauer characters):
  for GL_3(2) on B_2(GL_3(2)) over F_2 the alternating products of the
  characteristic polynomials of the elements of odd order on H_i and on C_i
  agree; Exercise 2: Lambda of a disjoint union is the sum, of a product of
  G-posets the product (marks; S_4 and A_5).
section_6_4 (pp. 220-222):
  * prop:g-homotopy-invariants, (ii) => (i): refuted as printed ("X^H ~ Y^H
    for all H" without a G-map): G = Z/2 acting freely on the triangulated
    torus by a translation (X) and by a glide reflection (Y); both are free
    G-simplicial complexes, X^1 = Y^1 is the torus and X^G = Y^G is empty,
    but the orbit spaces (computed as the coinvariants of the chains) have
    H_1 = Z^2 and Z + Z/2 (torus, Klein bottle), so no G-homotopy
    equivalence X -> Y exists (it would induce a homotopy equivalence of
    the orbit spaces); (iii)-(v) hold for this pair;
  * prop:hypo-elementary-lefschetz (Conlon): G = A_4, p = 3, the G-sets
    X = G/1 + G/V_4 + G/A_4 and Y = 2 G/C_2 + G/C_3 have chi(X^H) = chi(Y^H)
    for the 3-hypo-elementary H (1, C_2, C_3) but not for V_4, and the
    permutation modules over F_3 are isomorphic (MeatAxe indecomposition,
    the isomorphism of each pair of summands verified); the same for
    G = Z/3 x Z/3 in characteristic 2 (G/1 + 3 G/G and the sum of the
    G/C over the four subgroups C of order 3);
  * |X^op| = |X| and |X x Y| = |X| x |Y| (integral homology of products of
    circles and of the interval, Kuenneth); lem:comparable-maps-homotopic
    through (0 < 1) x X; def:conically-contractible and the Example: S of a
    cone is conically contractible (the map sigma -> sigma u {x_0}) and
    acyclic over Z.
section_6_5 (pp. 222-224): lem:quillen on the inclusion A_p(G) -> S_p(G)
  (the fibres i/P = A_p(P) conically contractible; the homology agrees) and
  the double complex of the proof (pairs of chains): its horizontal and
  vertical differentials anticommute only with the sign (-1)^p, the total
  homology is H_*(X) in all examples and H_*(Y) when the fibres f/y are
  contractible (the inclusion A_2(S_4) -> S_2(S_4)), but not for a map of the
  circle onto (0 < 1) with non-contractible fibres; the Remark (Conjecture of
  Webb, proved by Symonds): the orbit space |S_p(G)|/G (and |A_p(G)|/G,
  |B_p(G)|/G), computed as the coinvariants of the chains, is acyclic over
  Z for the 112 pairs (G, p) of RANGE with O_p(G) = 1 and for the pairs with
  p <= 5 and O_p(G) = 1 of S_4, A_5, S_5, A_6, S_6, GL_2(3), GL_3(2), PSL_2(8),
  PSL_2(11) (B_p(G) only for the groups of order > 360); the Exercise
  X ~_G S(|X|): the H-invariant chains of X are the chains of X^H (so |X| is
  G-simplicial) and the marks agree (S_4, A_5).
section_6_6 (pp. 224-226): for every (G, p) of RANGE and every class of
  subgroups H: chi(A_p(G)^H) = chi(S_p(G)^H) = chi(B_p(G)^H) = chi(Z_p(G)^H)
  (th:quillen-equivalence, th:bouc-equivalence, the Exercise, through
  prop:g-homotopy-invariants (ii) => (iii)); chi(S_p(G)) = 1 mod |G|_p
  (cor:ken-brown, here as a consequence); the proof of
  th:quillen-equivalence: for every class of p-subgroups P, P_0 = Omega_1
  Z(P) != 1 and A P_0 is elementary abelian for every elementary abelian
  A <= P; the Comment: O_p(G) != 1 => P -> P O_p(G) is a map of posets with
  P <= P O_p(G) >= O_p(G); S_p(G)^G is non-empty iff O_p(G) != 1; for the
  soluble G with O_p(G) = 1, H~(A_p(G); Q) != 0 (Quillen); Bouc's
  observation (Q >= N_Q(P) <= N_Q(P) O_p N_G(P) >= O_p N_G(P) for P not in
  B_p and all Q > P) for all classes P; for S_4, A_5, S_5, A_6, S_6, GL_2(3),
  GL_3(2), PSL_2(8), PSL_2(11), p = 2, 3, and the subgroups H (all classes for
  |G| <= 120, else the cyclic subgroups), over F_p:
  lem:contractible-intervals (f_X(B) for X = S_p(G), B = B_p(G) and
  e_X(A_p(G)) = S_p(G), for |S_p(G)| <= 300), prop:bouc-bounded-height on
  X = S_p(G)^H (X^* is contained in B_p(G)^H and X^* c B_p(G)^H c X have
  the same homology), and
  the author's correction of p. 226: the inclusion (b, -)_(X^*) -> (b, -)_X
  is defined for all b, the printed (b, -)_X -> (b, -)_(X^*) is not (there
  are b with (b, -)_X not inside X^*).

What these checks do NOT establish.  Homotopy equivalences and
contractibility are seen only through homology (with the coefficients
stated) and through the explicit conical contractions of the book;
Theorem 6.4.2 and Quillen's Lemma are not proved here.  The counterexample
to prop:g-homotopy-invariants (ii) => (i) uses, besides the computation,
that a G-homotopy equivalence induces a homotopy equivalence of orbit
spaces and that homotopy equivalent spaces have isomorphic homology.  The
covering spaces of Section 6.2, the Example of Delta(X) on p. 224 and the
Remark after Theorem 6.4.2 are not checked.  Group statements are checked
on the groups listed (RANGE and the named groups), not in general.
Nothing here compares our text with the printed book.
"""
import itertools
import sys
import time

from sage.all import (GF, QQ, ZZ, ChainComplex, SimplicialComplex, factor,
                      identity_matrix, is_prime_power, libgap, matrix,
                      simplicial_complexes, vector)

SCOPE = 'chapter-6a'
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


# ===========================================================================
# Posets, order complexes, homology
# ===========================================================================


class Poset:
    """A finite poset on 0..n-1 given by the strict up-sets."""

    def __init__(self, n, up):
        self.n = n
        self.up = [frozenset(u) for u in up]
        self.down = [set() for _ in range(n)]
        for i in range(n):
            for j in self.up[i]:
                self.down[j].add(i)
        self.order = sorted(range(n), key=lambda i: len(self.down[i]))

    def lt(self, a, b):
        return b in self.up[a]

    def euler(self, S=None):
        """chi(|X_S|) by chains with largest element x: h(x) = 1 - sum h(y), y < x."""
        S = set(range(self.n)) if S is None else set(S)
        h = {}
        for x in self.order:
            if x in S:
                h[x] = 1 - sum(h[y] for y in self.down[x] if y in S)
        return sum(h.values())

    def chains(self, S=None, top=None):
        S = set(range(self.n)) if S is None else set(S)
        out = {}

        def ext(c):
            out.setdefault(len(c) - 1, []).append(tuple(c))
            if top is not None and len(c) > top:
                return
            for y in self.up[c[-1]]:
                if y in S:
                    ext(c + [y])
        for x in sorted(S):
            ext([x])
        return out

    def interval_up(self, x, S=None):
        """(x, -) inside S."""
        S = set(range(self.n)) if S is None else set(S)
        return [y for y in self.up[x] if y in S]

    def interval_down(self, x, S=None, closed=False):
        S = set(range(self.n)) if S is None else set(S)
        out = [y for y in self.down[x] if y in S]
        if closed and x in S:
            out.append(x)
        return out


def poset_from_relation(elems, less):
    n = len(elems)
    return Poset(n, [[j for j in range(n) if j != i and less(elems[i], elems[j])]
                     for i in range(n)])


def boundary_mats(by, F):
    pos = {k: {c: i for i, c in enumerate(v)} for k, v in by.items()}
    mats = {}
    for k in range(1, (max(by) if by else -1) + 1):
        d = {}
        for j, c in enumerate(by[k]):
            for i in range(len(c)):
                d[(pos[k - 1][c[:i] + c[i + 1:]], j)] = F((-1) ** i)
        mats[k] = matrix(F, len(by[k - 1]), len(by[k]), d, sparse=True)
    return mats


def reduced_betti(by, F):
    """Reduced Betti numbers over the field F of the complex with simplices by[k]."""
    if not by or not by.get(0):
        return {-1: 1}
    mats = boundary_mats(by, F)
    top = max(by)
    rk = {0: 1, top + 1: 0}
    for k in range(1, top + 1):
        rk[k] = mats[k].rank()
    b = {k: len(by[k]) - rk[k] - rk[k + 1] for k in range(top + 1)}
    return {k: v for k, v in b.items() if v}


def acyclic(by, F):
    return all(v == 0 for v in reduced_betti(by, F).values())


def chain_complex_ZZ(by, augmented=True):
    mats = boundary_mats(by, ZZ)
    data = {k: mats[k] for k in mats}
    if augmented:
        data[0] = matrix(ZZ, 1, len(by[0]), [1] * len(by[0]), sparse=True)
    return ChainComplex(data, degree=-1)


def reduced_homology_ZZ(by):
    """Reduced integral homology as a dict k -> (rank, torsion list)."""
    if not by or not by.get(0):
        return {-1: (1, [])}
    H = chain_complex_ZZ(by).homology()
    out = {}
    for k, A in H.items():
        inv = list(A.invariants())
        out[k] = (inv.count(0), sorted(x for x in inv if x != 0))
    return out


def is_acyclic_ZZ(by):
    return all(v == (0, []) for v in reduced_homology_ZZ(by).values())


def euler_from_chains(by):
    return sum((-1) ** k * len(v) for k, v in by.items())


# ===========================================================================
# Subgroup posets in GAP
# ===========================================================================

GAP_PSUB = r'''
function(G, p, kind)
  local P, subs, reps, S, all, keys, n, up;
  P := SylowSubgroup(G, p);
  if Size(P) = 1 then
    return rec(n := 0, subs := [], keys := [], up := [], sizes := []);
  fi;
  subs := Filtered(Concatenation(List(ConjugacyClassesSubgroups(P), AsList)),
                   S -> Size(S) > 1);
  if kind = "A" or kind = "Z" then subs := Filtered(subs, IsElementaryAbelian); fi;
  reps := [];
  for S in subs do
    if ForAll(reps, R -> Size(R) <> Size(S) or not IsConjugate(G, R, S)) then
      Add(reps, S);
    fi;
  od;
  if kind = "B" then
    reps := Filtered(reps, R -> PCore(Normalizer(G, R), p) = R);
  elif kind = "Z" then
    reps := Filtered(reps, R ->
      Omega(PCore(Centre(Centralizer(G, R)), p), p, 1) = R);
  fi;
  all := Concatenation(List(reps, R ->
           List(RightTransversal(G, Normalizer(G, R)), g -> R^g)));
  keys := List(all, S -> Set(AsList(S)));
  SortParallel(keys, all);
  n := Length(all);
  up := List([1..n], i -> Filtered([1..n], j ->
          Length(keys[j]) > Length(keys[i]) and IsSubset(keys[j], keys[i])));
  return rec(n := n, subs := all, keys := keys, up := up,
             sizes := List(keys, Length), nreps := Length(reps));
end
'''

GAP_FIXED = r'''
function(data, H)
  local gens;
  gens := GeneratorsOfGroup(H);
  return Filtered([1..data.n], i -> ForAll(gens, h ->
    ForAll(GeneratorsOfGroup(data.subs[i]), x -> x^h in data.keys[i])));
end
'''

GAP_PERMS = r'''
function(data, gens)
  return List(gens, g -> List(data.keys, k ->
    PositionSorted(data.keys, Set(List(k, x -> x^g)))));
end
'''

GAP_POSITION = r'''
function(data, S)
  local k, i;
  k := Set(AsList(S));
  i := PositionSorted(data.keys, k);
  if i <= data.n and data.keys[i] = k then return i; fi;
  return 0;
end
'''

PSUB = libgap.eval(GAP_PSUB)
FIXED = libgap.eval(GAP_FIXED)
PERMS = libgap.eval(GAP_PERMS)
POSITION = libgap.eval(GAP_POSITION)


def perm_group(G):
    return libgap.Image(libgap.IsomorphismPermGroup(G))


class SubPoset:
    """A subgroup poset of G (kind S, A, B or Z) with its conjugation action."""

    def __init__(self, G, p, kind):
        self.G, self.p, self.kind = G, p, kind
        self.data = PSUB(G, p, kind)
        self.n = int(self.data['n'])
        self.X = Poset(self.n, [[int(j) - 1 for j in u] for u in self.data['up']])
        self.sizes = [int(s) for s in self.data['sizes']]
        self._perms = None

    def subgroup(self, i):
        return self.data['subs'][i]

    def fixed(self, H):
        return [int(i) - 1 for i in FIXED(self.data, H)]

    def position(self, S):
        return int(POSITION(self.data, S)) - 1

    def perms(self):
        if self._perms is None:
            gens = self.G.GeneratorsOfGroup()
            self._perms = [[int(i) - 1 for i in pp] for pp in PERMS(self.data, gens)]
        return self._perms


def subgroup_classes(G):
    return [c.Representative() for c in G.ConjugacyClassesSubgroups()]


def orbit_ids(items, index, perms, act):
    """Union-find orbits of items (with positions index) under generator maps."""
    parent = list(range(len(items)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for k, it in enumerate(items):
        for pm in perms:
            j = index[act(pm, it)]
            a, b = find(k), find(j)
            if a != b:
                parent[a] = b
    roots = {}
    return [roots.setdefault(find(k), len(roots)) for k in range(len(items))], len(roots)


def orbit_chain_complex(by, perms):
    """Coinvariants C_*(|X|)_G of the order complex of a G-poset (G permutes
    the elements, so preserves the order and acts on chains without signs);
    returns the augmented chain complex over Z of the orbit space."""
    act = lambda pm, c: tuple(pm[x] for x in c)
    oid = {}
    nor = {}
    for k, v in by.items():
        index = {c: i for i, c in enumerate(v)}
        ids, m = orbit_ids(v, index, perms, act)
        oid[k] = {c: ids[i] for i, c in enumerate(v)}
        nor[k] = m
    data = {0: matrix(ZZ, 1, nor[0], [1] * nor[0], sparse=True)}
    for k in range(1, max(by) + 1):
        d = {}
        seen = set()
        for c in by[k]:
            o = oid[k][c]
            if o in seen:
                continue
            seen.add(o)
            for i in range(len(c)):
                key = (oid[k - 1][c[:i] + c[i + 1:]], o)
                d[key] = d.get(key, 0) + (-1) ** i
        data[k] = matrix(ZZ, nor[k - 1], nor[k], d, sparse=True)
    return ChainComplex(data, degree=-1), nor


GROUPS = {}
POSETS = {}


def group_range():
    """RANGE of the docstring: names 'SmallGroup(o, k)' (the groups as
    permutation groups are kept in GROUPS)."""
    out = []
    for order in range(2, 101):
        if order == 96 or (is_prime_power(order) and order > 16):
            continue
        for k in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            name = 'SmallGroup(%d, %d)' % (order, k)
            if name not in GROUPS:
                GROUPS[name] = perm_group(libgap.SmallGroup(order, k))
            out.append(name)
    return out


def subposet(name, p, kind):
    key = (name, p, kind)
    if key not in POSETS:
        POSETS[key] = SubPoset(GROUPS[name], p, kind)
    return POSETS[key]


def class_reps_of_elements(P):
    """One element of each G-orbit on the elements of a SubPoset."""
    ids, m = orbit_ids(list(range(P.n)), {i: i for i in range(P.n)}, P.perms(),
                       lambda pm, i: pm[i])
    first = {}
    for i, o in enumerate(ids):
        first.setdefault(o, i)
    return sorted(first.values())


def named_groups():
    names = {'S_4': lambda: libgap.SymmetricGroup(4),
             'A_5': lambda: libgap.AlternatingGroup(5),
             'S_5': lambda: libgap.SymmetricGroup(5),
             'A_6': lambda: libgap.AlternatingGroup(6),
             'S_6': lambda: libgap.SymmetricGroup(6),
             'GL_2(3)': lambda: perm_group(libgap.GL(2, 3)),
             'GL_3(2)': lambda: perm_group(libgap.GL(3, 2)),
             'PSL_2(8)': lambda: libgap.PSL(2, 8),
             'PSL_2(11)': lambda: libgap.PSL(2, 11)}
    for k, f in names.items():
        if k not in GROUPS:
            GROUPS[k] = f()
    return list(names)


def ppart(n, p):
    n = int(n)
    r = 1
    while n % p == 0:
        n //= p
        r *= p
    return r


# ===========================================================================
# Section 6.1
# ===========================================================================


def closure(facets):
    S = set()
    for F in facets:
        F = tuple(sorted(F))
        for k in range(1, len(F) + 1):
            for c in itertools.combinations(F, k):
                S.add(c)
    return S


def is_g_simplicial(simplices, group):
    """def:g-simplicial-complex: g stabilising sigma setwise fixes it pointwise."""
    for s in simplices:
        for g in group:
            img = set(g[v] for v in s)
            if img == set(s) and any(g[v] != v for v in s):
                return False
    return True


def sd_action(simplices, group):
    """The poset S(Delta) of simplices and the induced action on it."""
    elems = sorted(simplices, key=lambda s: (len(s), s))
    idx = {s: i for i, s in enumerate(elems)}
    X = poset_from_relation(elems, lambda a, b: set(a) < set(b))
    acts = [[idx[tuple(sorted(g[v] for v in s))] for s in elems] for g in group]
    return elems, X, acts


def oriented_action(s, g):
    """g applied to the oriented simplex s (vertices in increasing order):
    returns the sorted image and the sign of the reordering."""
    img = [g[v] for v in s]
    srt = sorted(img)
    sgn = 1
    for a in range(len(img)):
        for b in range(a + 1, len(img)):
            if img[a] > img[b]:
                sgn = -sgn
    return tuple(srt), sgn


def perm_group_elements(n, gens):
    """All elements of the permutation group generated by gens (tuples on 0..n-1)."""
    e = tuple(range(n))
    seen = {e}
    frontier = [e]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = tuple(g[x[i]] for i in range(n))
                if y not in seen:
                    seen.add(y)
                    new.append(y)
        frontier = new
    return sorted(seen)


def section_6_1():
    # the edge with Z/2 swapping its ends (the picture of p. 215)
    edge = closure([(0, 1)])
    swap = [(0, 1), (1, 0)]
    check(not is_g_simplicial(edge, swap),
          'def:g-simplicial-complex: Z/2 swapping the ends of an edge stabilises '
          'the edge setwise but not pointwise')
    # its chain group C_1 is the sign representation: not a permutation module
    s, sgn = oriented_action((0, 1), swap[1])
    check(s == (0, 1) and sgn == -1,
          'def:chain-group: the swap sends the oriented edge (0, 1) to (1, 0) = '
          '-(0, 1)')
    fix = (matrix(QQ, 1, 1, [sgn]) - identity_matrix(QQ, 1)).right_kernel().dimension()
    check(fix == 0,
          'p. 216: C_1 of the edge is the sign representation (no non-zero fixed '
          'vector over Q), while a non-zero permutation module has the orbit sums '
          'as fixed vectors: the G-simplicial condition is needed')
    elems, X, acts = sd_action(edge, swap)
    sd = X.chains()
    sdg = [tuple(a[x] for x in range(len(elems))) for a in acts]
    check(is_g_simplicial(set(c for v in sd.values() for c in v), sdg),
          'p. 215: the barycentric subdivision of the edge is G-simplicial')
    # Z/3 rotating a triangle
    tri = closure([(0, 1, 2)])
    rot = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    check(not is_g_simplicial(tri, rot),
          'Z/3 rotating a 2-simplex stabilises it setwise, not pointwise')
    bdry = set(s for s in tri if len(s) < 3)
    check(is_g_simplicial(bdry, rot),
          'the boundary of the triangle with the rotation is G-simplicial (free)')
    # every subgroup of S_n acting on the simplex and its boundary (n <= 4)
    ncases = 0
    for n in (2, 3, 4):
        Sn = list(itertools.permutations(range(n)))
        full = closure([tuple(range(n))])
        bd = set(s for s in full if len(s) < n)
        subgroups = set()
        for gens in itertools.combinations_with_replacement(Sn, 2):
            subgroups.add(tuple(perm_group_elements(n, list(gens))))
        for grp in subgroups:
            for cx in (full, bd):
                elems, X, acts = sd_action(cx, grp)
                chains = X.chains()
                allc = set(c for v in chains.values() for c in v)
                ok = True
                for a in acts:
                    for c in allc:
                        img = set(a[x] for x in c)
                        if img == set(c) and any(a[x] != x for x in c):
                            ok = False
                # the chain modules of sd are permutation modules: g maps the
                # oriented chain (x_0 < ... < x_k) to the chain (g x_0 < ... < g x_k)
                for a in acts:
                    for c in allc:
                        img = tuple(a[x] for x in c)
                        ok = ok and all(X.lt(img[i], img[i + 1]) for i in range(len(img) - 1))
                check(ok, 'p. 215: sd of the %d-simplex%s under a subgroup of S_%d '
                      'of order %d is G-simplicial, with C_n a permutation module'
                      % (n - 1, '' if cx is full else ' boundary', n, len(grp)))
                ncases += 1
    check(ncases == 2 * (2 + 6 + 30), 'all subgroups of S_2, S_3, S_4 were covered '
          '(2, 6, 30 subgroups; got %d cases)' % ncases)
    # d o d = 0 and G-linearity on sd of the boundary of the tetrahedron, over Z
    S4 = list(itertools.permutations(range(4)))
    bd = set(s for s in closure([(0, 1, 2, 3)]) if len(s) < 4)
    elems, X, acts = sd_action(bd, S4)
    by = X.chains()
    mats = boundary_mats(by, ZZ)
    for k in range(2, max(by) + 1):
        check((mats[k - 1] * mats[k]).is_zero(),
              'p. 216: d_(n) o d_(n+1) = 0 on sd(boundary of the tetrahedron), n = %d'
              % (k - 1))
    pos = {k: {c: i for i, c in enumerate(v)} for k, v in by.items()}
    ok = True
    for a in acts:
        P = {}
        for k in by:
            P[k] = matrix(ZZ, len(by[k]), len(by[k]),
                          {(pos[k][tuple(a[x] for x in c)], i): 1
                           for i, c in enumerate(by[k])}, sparse=True)
        for k in range(1, max(by) + 1):
            ok = ok and (P[k - 1] * mats[k] == mats[k] * P[k])
    check(ok, 'p. 216: the boundary maps are kG-module homomorphisms (all 24 '
          'elements of S_4 on sd of the boundary of the tetrahedron)')
    # reduced homology
    two = {0: [(0,), (1,)]}
    check(reduced_betti(two, QQ) == {0: 1},
          'def:augmented-chain-complex: two points have H_0 = k^2 and H~_0 = '
          'Ker(H_0 -> k) = k')
    circ = {0: [(0,), (1,), (2,)], 1: [(0, 1), (0, 2), (1, 2)]}
    check(reduced_betti(circ, QQ) == {1: 1},
          'def:augmented-chain-complex: the circle has H~_0 = 0, H~_1 = k')


# ===========================================================================
# Section 6.2
# ===========================================================================


def torus_facets(m, n):
    def corner(i, j):
        return ('v', i % m, j % n)

    def centre(i, j):
        return ('c', i % m, j % n)
    tris = []
    for i in range(m):
        for j in range(n):
            a, b, c, d = corner(i, j), corner(i + 1, j), corner(i + 1, j + 1), corner(i, j + 1)
            z = centre(i, j)
            for e in [(a, b), (b, c), (c, d), (d, a)]:
                tris.append((z, e[0], e[1]))
    return tris


def relabel(facets):
    verts = sorted(set(v for f in facets for v in f))
    idx = {v: i for i, v in enumerate(verts)}
    return [tuple(sorted(idx[v] for v in f)) for f in facets], verts, idx


def section_6_2():
    # sd(Delta) = |S(Delta)| against Sage's barycentric subdivision
    tf, _, _ = relabel(torus_facets(4, 3))
    cases = [('S^2', SimplicialComplex([s for s in itertools.combinations(range(4), 3)])),
             ('torus', SimplicialComplex(tf)),
             ('RP^2', simplicial_complexes.RealProjectivePlane()),
             ('Klein bottle', simplicial_complexes.KleinBottle())]
    for name, K in cases:
        faces = [tuple(sorted(f)) for f in K.face_iterator() if f.dimension() >= 0]
        elems = sorted(faces, key=lambda s: (len(s), s))
        X = poset_from_relation(elems, lambda a, b: set(a) < set(b))
        by = X.chains()
        sdK = K.barycentric_subdivision()
        fv = sdK.f_vector()[1:]
        check([len(by[k]) for k in sorted(by)] == list(fv),
              'def:barycentric-subdivision: |S(Delta)| has the f-vector of the '
              'barycentric subdivision (%s: %s)' % (name, fv))
        H = reduced_homology_ZZ(by)
        HK = K.homology()
        ours = {k: v for k, v in H.items()}
        theirs = {}
        for k, A in HK.items():
            inv = list(A.invariants())
            theirs[k] = (inv.count(0), sorted(x for x in inv if x != 0))
        check(all(ours.get(k, (0, [])) == theirs.get(k, (0, [])) for k in set(ours) | set(theirs)),
              'p. 217: sd(Delta) and Delta have the same integral homology (%s: %s)'
              % (name, theirs))
    # the Exercise via Lefschetz numbers: chi(|Delta|^g) = chi(S(Delta)^g) = L(g)
    S4 = list(itertools.permutations(range(4)))
    bd = sorted(set(s for s in closure([(0, 1, 2, 3)]) if len(s) < 4), key=lambda s: (len(s), s))
    by = {}
    for s in bd:
        by.setdefault(len(s) - 1, []).append(s)
    mats = boundary_mats(by, QQ)
    pos = {k: {c: i for i, c in enumerate(v)} for k, v in by.items()}

    def lefschetz(g):
        tot = 0
        for k in by:
            tot += (-1) ** k * sum(oriented_action(s, g)[1] for s in by[k]
                                   if oriented_action(s, g)[0] == s)
        return tot
    elems = bd
    X = poset_from_relation(elems, lambda a, b: set(a) < set(b))
    ok = True
    for g in S4:
        fixedS = [i for i, s in enumerate(elems) if set(g[v] for v in s) == set(s)]
        # Lefschetz number from homology: trace on H_0 = 1, on H_2 = sign of g
        sign = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if g[a] > g[b]:
                    sign = -sign
        L = 1 + sign
        ok = ok and X.euler(fixedS) == L == lefschetz(g)
    check(ok, 'Exercise p. 217: for all 24 elements g of S_4 on the boundary of the '
          'tetrahedron, chi(S(Delta)^g) = sum (-1)^i tr(g, C_i) = L(g) = 1 + sign(g) '
          '(the fixed points of |Delta| are those of sd(Delta))')
    # the edge: the pointwise fixed subcomplex is empty, |Delta|^g is the midpoint
    edge = [(0,), (1,), (0, 1)]
    Xe = poset_from_relation(edge, lambda a, b: set(a) < set(b))
    g = (1, 0)
    fixed_pointwise = [s for s in edge if all(g[v] == v for v in s)]
    fixedS = [i for i, s in enumerate(edge) if set(g[v] for v in s) == set(s)]
    check(fixed_pointwise == [] and Xe.euler(fixedS) == 1,
          'p. 215: for the edge with the swap the fixed subcomplex of Delta is empty '
          'but chi(S(Delta)^g) = 1 = L(g) (the midpoint): one must subdivide')
    # subgroup posets
    for name, G in [('S_4', libgap.SymmetricGroup(4)), ('A_5', libgap.AlternatingGroup(5)),
                    ('GL_3(2)', perm_group(libgap.GL(3, 2)))]:
        for p in (2, 3):
            S = SubPoset(G, p, 'S')
            A = SubPoset(G, p, 'A')
            B = SubPoset(G, p, 'B')
            subA = all(S.position(A.subgroup(i)) >= 0 for i in range(A.n))
            subB = all(S.position(B.subgroup(i)) >= 0 for i in range(B.n))
            syl = G.SylowSubgroup(p)
            check(subA and subB and B.position(syl) >= 0,
                  'p. 218: A_p(G) and B_p(G) are subposets of S_p(G), the Sylow '
                  'subgroups lie in B_p(G) (%s, p = %d)' % (name, p))
            # S_p(G) u {1} is a cone
            n = S.n
            up = [list(S.X.up[i]) for i in range(n)] + [list(range(n))]
            Xc = Poset(n + 1, up)
            check(Xc.euler() == 1,
                  'p. 218: with the trivial subgroup the poset is a cone, chi = 1 '
                  '(%s, p = %d)' % (name, p))
    # invertible systems on the circle a, b < c, d
    for nn in (2, 3, 5):
        for shift in (0, 1):
            elems = [(x, u) for x in 'abcd' for u in range(nn)]

            def less(e, f):
                x, u = e
                y, v = f
                if x not in 'ab' or y not in 'cd':
                    return False
                t = shift if (x, y) == ('a', 'c') else 0
                return v == (u + t) % nn
            Xt = poset_from_relation(elems, less)
            by = Xt.chains()
            comps = reduced_betti(by, QQ)
            if shift:
                check(comps == {1: 1} and len(by[1]) == 4 * nn,
                      'def:invertible-system: the system Z/%d with one transition a '
                      'shift gives X~ connected, a %d-cycle (a connected %d-fold cover '
                      'of the circle)' % (nn, 4 * nn, nn))
            else:
                check(comps == {0: nn - 1, 1: nn},
                      'def:invertible-system: the constant system Z/%d gives %d copies '
                      'of the circle' % (nn, nn))


# ===========================================================================
# Section 6.3
# ===========================================================================


def character_of_subquotient(by, acts, F):
    """Traces of the elements (acts: permutations of the chains of each degree,
    without signs) on H_k = Z_k / B_k over the field F of characteristic 0."""
    mats = boundary_mats(by, F)
    top = max(by)
    out = []
    for k in range(top + 1):
        n = len(by[k])
        V = F ** n
        Z = V if k == 0 else mats[k].right_kernel()
        B = V.subspace([]) if k == top else mats[k + 1].column_space()
        out.append((Z, B))
    traces = []
    for a in acts:
        tr = []
        for k in range(top + 1):
            Z, B = out[k]
            pm = a[k]

            def act(v):
                w = [0] * len(v)
                for i, x in enumerate(v):
                    if x:
                        w[pm[i]] = x
                return vector(F, w)

            def tr_on(W):
                if W.dimension() == 0:
                    return 0
                return sum(W.coordinate_vector(act(b))[i] for i, b in enumerate(W.basis()))
            tr.append(tr_on(Z) - tr_on(B))
        traces.append(tr)
    return traces


def chain_actions(by, elem_perm):
    """For a permutation of the poset elements, the permutation of each by[k]."""
    out = {}
    for k, v in by.items():
        pos = {c: i for i, c in enumerate(v)}
        out[k] = [pos[tuple(elem_perm[x] for x in c)] for c in v]
    return out


def section_6_3():
    # prop:euler-characteristic-zero by characters over Q
    S4 = list(itertools.permutations(range(4)))
    bd = set(s for s in closure([(0, 1, 2, 3)]) if len(s) < 4)
    elems, X, acts = sd_action(bd, S4)
    cases = [('S_4 on sd(boundary of the tetrahedron)', X, acts)]
    for name, G, p, kind in [('S_4', libgap.SymmetricGroup(4), 2, 'S'),
                             ('A_5', libgap.AlternatingGroup(5), 2, 'S'),
                             ('GL_3(2)', perm_group(libgap.GL(3, 2)), 2, 'B')]:
        P = SubPoset(G, p, kind)
        reps = [c.Representative() for c in G.ConjugacyClasses()]
        perms = PERMS(P.data, reps)
        cases.append(('%s on %s_%d' % (name, kind, p), P.X,
                      [[int(i) - 1 for i in pm] for pm in perms]))
    for name, Xp, elem_acts in cases:
        by = Xp.chains()
        ca = [chain_actions(by, a) for a in elem_acts]
        tr = character_of_subquotient(by, ca, QQ)
        ok = True
        for a, t in zip(ca, tr):
            perm_char = [sum(1 for i in range(len(a[k])) if a[k][i] == i) for k in sorted(by)]
            ok = ok and sum((-1) ** k * t[k] for k in range(len(t))) == \
                sum((-1) ** k * perm_char[k] for k in range(len(perm_char)))
        check(ok, 'prop:euler-characteristic-zero: sum (-1)^i H_i = sum (-1)^i C_i in '
              'a(G) over Q (characters at %d elements; %s)' % (len(ca), name))
        b = reduced_betti(by, QQ)
        check(sum((-1) ** k * v for k, v in b.items()) + 1 == euler_from_chains(by),
              'p. 219: chi = sum (-1)^i dim H_i and chi~ = chi - 1 (%s)' % name)
    # Lefschetz invariant: orbits and stabilisers -> marks, against fixed points
    STABS = libgap.eval(r'''
    function(G, data, chains)
      # the stabilisers of the chains (intersections of normalisers)
      local K, c, i, out;
      out := [];
      for c in chains do
        K := G;
        for i in c do K := Intersection(K, Normalizer(G, data.subs[i])); od;
        Add(out, K);
      od;
      return out;
    end''')
    ORB = libgap.eval(r'''
    function(G, stabs, signs, H)
      # the mark at H of sum signs[i] [G/stabs[i]]: fixed right cosets
      local tot, i;
      tot := 0;
      for i in [1..Length(stabs)] do
        tot := tot + signs[i] *
          Number(RightTransversal(G, stabs[i]), r -> IsSubset(stabs[i], H^(r^-1)));
      od;
      return tot;
    end''')
    for name, G in [('S_4', libgap.SymmetricGroup(4)), ('A_5', libgap.AlternatingGroup(5)),
                    ('GL_2(3)', perm_group(libgap.GL(2, 3))), ('GL_3(2)', perm_group(libgap.GL(3, 2))),
                    ('S_5', libgap.SymmetricGroup(5))]:
        reps = subgroup_classes(G)
        for p in (2, 3):
            for kind in 'SAB':
                P = SubPoset(G, p, kind)
                by = P.X.chains()
                perms = P.perms()
                orbit_reps = []
                for k, v in by.items():
                    index = {c: i for i, c in enumerate(v)}
                    ids, m = orbit_ids(v, index, perms, lambda pm, c: tuple(pm[x] for x in c))
                    first = {}
                    for i, o in enumerate(ids):
                        first.setdefault(o, v[i])
                    orbit_reps += [[x + 1 for x in c] for c in first.values()]
                stabs = STABS(G, P.data, orbit_reps)
                signs = [(-1) ** (len(c) - 1) for c in orbit_reps]
                ok = True
                for H in reps:
                    m1 = int(ORB(G, stabs, signs, H))
                    m2 = P.X.euler(P.fixed(H))
                    ok = ok and m1 == m2
                check(ok, 'p. 220: Lambda_G(Delta) = sum (-1)^i c_i(Delta) maps to the '
                      'marks chi(Delta^H) for all %d classes of H (%s, %s_%d, %d chain '
                      'orbits)' % (len(reps), name, kind, p, len(orbit_reps)))
    # Exercise 1 (Brauer characters) for GL_3(2) on B_2(GL_3(2)) over F_2
    G = perm_group(libgap.GL(3, 2))
    P = SubPoset(G, 2, 'B')
    by = P.X.chains()
    F = GF(2)
    mats = boundary_mats(by, F)
    reps = [c.Representative() for c in G.ConjugacyClasses() if int(c.Representative().Order()) % 2]
    from sage.all import PolynomialRing
    R = PolynomialRing(F, 't')
    def restricted_charpoly(Pm, W):
        if W.dimension() == 0:
            return R(1)
        M = matrix(F, [W.coordinate_vector(Pm * b) for b in W.basis()])
        return R(M.charpoly().list())
    ok = True
    for g in reps:
        a = chain_actions(by, [int(i) - 1 for i in PERMS(P.data, [g])[0]])
        num_C, num_H = R(1), R(1)
        den_C, den_H = R(1), R(1)
        for k in sorted(by):
            n = len(by[k])
            Pm = matrix(F, n, n, {(a[k][i], i): 1 for i in range(n)})
            cp = R(Pm.charpoly().list())
            Z = (F ** n) if k == 0 else mats[k].right_kernel()
            B = (F ** n).subspace([]) if k == max(by) else mats[k + 1].column_space()
            cz, cb = restricted_charpoly(Pm, Z), restricted_charpoly(Pm, B)
            ch, rem = cz.quo_rem(cb)
            ok = ok and rem == 0 and B.is_subspace(Z)
            if k % 2 == 0:
                num_C *= cp
                num_H *= ch
            else:
                den_C *= cp
                den_H *= ch
        ok = ok and num_C * den_H == num_H * den_C
    check(ok, 'Exercise 1 p. 220: sum (-1)^i H_i and sum (-1)^i C_i have the same '
          'Brauer character (characteristic polynomials of the %d classes of '
          'elements of odd order of GL_3(2) on B_2(GL_3(2)) over F_2)' % len(reps))
    # Exercise 2: disjoint unions and products (marks)
    for name, G in [('S_4', libgap.SymmetricGroup(4)), ('A_5', libgap.AlternatingGroup(5))]:
        X1 = SubPoset(G, 3, 'S')
        X2 = SubPoset(G, 2, 'B')
        reps = subgroup_classes(G)
        n1, n2 = X1.n, X2.n
        # product poset
        elems = [(a, b) for a in range(n1) for b in range(n2)]
        idx = {e: i for i, e in enumerate(elems)}
        up = []
        for (a, b) in elems:
            up.append([idx[(c, d)] for (c, d) in elems
                       if (c == a or X1.X.lt(a, c)) and (d == b or X2.X.lt(b, d)) and (c, d) != (a, b)])
        Xp = Poset(len(elems), up)
        upu = [list(X1.X.up[i]) for i in range(n1)] + [[n1 + j for j in X2.X.up[i]] for i in range(n2)]
        Xu = Poset(n1 + n2, upu)
        okp = oku = True
        for H in reps:
            f1, f2 = X1.fixed(H), X2.fixed(H)
            c1, c2 = X1.X.euler(f1), X2.X.euler(f2)
            fp = [idx[(a, b)] for a in f1 for b in f2]
            okp = okp and Xp.euler(fp) == c1 * c2
            oku = oku and Xu.euler(f1 + [n1 + j for j in f2]) == c1 + c2
        check(oku, 'Exercise 2 (i) p. 220: Lambda_G of a disjoint union is the sum '
              '(marks; %s, S_3 and B_2)' % name)
        check(okp, 'Exercise 2 (ii) p. 220: Lambda_G(X x Y) = Lambda_G(X) Lambda_G(Y) '
              '(marks multiply; %s, S_3 x B_2)' % name)


# ===========================================================================
# Section 6.4
# ===========================================================================


def free_action_homology(facets, g):
    """The orbit space of the free involution g of the complex: integral
    homology of the coinvariants of the chains (orientation by sorting)."""
    S = closure(facets)
    by = {}
    for s in S:
        by.setdefault(len(s) - 1, []).append(s)
    for k in by:
        by[k].sort()
    group = [tuple(range(len(g))), tuple(g)]

    def canon(s):
        best = None
        for h in group:
            t, sg = oriented_action(s, h)
            if best is None or t < best[0]:
                best = (t, sg)
        return best
    reps = {k: sorted(set(canon(s)[0] for s in v)) for k, v in by.items()}
    pos = {k: {s: i for i, s in enumerate(v)} for k, v in reps.items()}
    data = {}
    for k in range(1, max(by) + 1):
        d = {}
        for j, s in enumerate(reps[k]):
            for i in range(len(s)):
                r, sg = canon(s[:i] + s[i + 1:])
                key = (pos[k - 1][r], j)
                d[key] = d.get(key, 0) + (-1) ** i * sg
        data[k] = matrix(ZZ, len(reps[k - 1]), len(reps[k]), d, sparse=True)
    H = ChainComplex(data, degree=-1).homology()
    out = {}
    for k, A in H.items():
        inv = list(A.invariants())
        out[k] = (inv.count(0), sorted(x for x in inv if x != 0))
    return out, by


def section_6_4():
    # --- prop:g-homotopy-invariants (ii) => (i): the torus and the Klein bottle
    m, n = 4, 3
    tf, verts, idx = relabel(torus_facets(m, n))

    def trans(v):
        t, i, j = v
        return (t, (i + m // 2) % m, j)

    def glide(v):
        t, i, j = v
        if t == 'v':
            return ('v', (i + m // 2) % m, (-j) % n)
        return ('c', (i + m // 2) % m, (-j - 1) % n)
    K = SimplicialComplex(tf)
    HK = K.homology()
    check(K.is_pseudomanifold() and str(HK[1]) == 'Z x Z' and str(HK[2]) == 'Z',
          'the triangulated torus (4 x 3 squares coned at their centres) has '
          'H_1 = Z^2, H_2 = Z')
    S = closure(tf)
    res = {}
    for name, f in [('translation', trans), ('glide reflection', glide)]:
        g = [idx[f(v)] for v in verts]
        free = all(set(g[v] for v in s) != set(s) for s in S) and \
            all(tuple(sorted(g[v] for v in s)) in S for s in S) and \
            all(g[g[v]] == v for v in range(len(g)))
        check(free and is_g_simplicial(S, [tuple(range(len(g))), tuple(g)]),
              'p. 221: the %s is a free simplicial involution of the torus (no simplex '
              'is stabilised), so X is a finite G-simplicial complex, G = Z/2, with '
              'X^G empty' % name)
        res[name], by = free_action_homology(tf, g)
    check(res['translation'][1] == (2, []) and res['translation'][2] == (1, []),
          'p. 221: the orbit space of the translation has H_1 = Z^2, H_2 = Z (a torus)')
    check(res['glide reflection'][1] == (1, [2]) and res['glide reflection'][2] == (0, []),
          'p. 221: the orbit space of the glide reflection has H_1 = Z + Z/2, H_2 = 0 '
          '(a Klein bottle)')
    refuted(res['translation'] == res['glide reflection'],
            'prop:g-homotopy-invariants as printed, (ii) => (i): X^H ~ Y^H for all H '
            '(the torus for H = 1, empty for H = G) but X and Y are not G-homotopy '
            'equivalent, since the orbit spaces have different homology')
    check(euler_from_chains(by) == 0,
          'p. 221: (iii)-(v) hold for this pair: chi(X) = chi(Y) = 0 and '
          'X^G = Y^G = empty, so Lambda_G(X) = Lambda_G(Y) = 0 (free of Euler '
          'characteristic 0)')
    # --- prop:hypo-elementary-lefschetz (Conlon) for A_4, p = 3 and E_9, p = 2
    CONLON = libgap.eval(r'''
    function(G, plus, minus, q)
      local permmod, sum, A, B, sa, sb, used, s, i, iso, ok, gs, gb;
      permmod := function(K)
        local hom, n;
        hom := ActionHomomorphism(G, RightCosets(G, K), OnRight);
        n := Index(G, K);
        return List(GeneratorsOfGroup(G), g -> PermutationMat(Image(hom, g), n, GF(q)));
      end;
      sum := function(L)
        local mats, K, i, M;
        mats := List(GeneratorsOfGroup(G), g -> []);
        for K in L do
          M := permmod(K);
          for i in [1..Length(mats)] do
            if mats[i] = [] then mats[i] := M[i];
            else mats[i] := DirectSumMat(mats[i], M[i]); fi;
          od;
        od;
        return GModuleByMats(List(mats, m -> ImmutableMatrix(GF(q), m)), GF(q));
      end;
      A := sum(plus); B := sum(minus);
      if MTX.Dimension(A) <> MTX.Dimension(B) then return false; fi;
      sa := List(MTX.Indecomposition(A), x -> x[2]);
      sb := List(MTX.Indecomposition(B), x -> x[2]);
      if Length(sa) <> Length(sb) then return false; fi;
      used := List(sb, x -> false);
      for s in sa do
        ok := false;
        for i in [1..Length(sb)] do
          if not used[i] and MTX.Dimension(sb[i]) = MTX.Dimension(s) then
            iso := MTX.IsomorphismModules(s, sb[i]);
            gs := MTX.Generators(s); gb := MTX.Generators(sb[i]);
            if iso <> fail and RankMat(iso) = MTX.Dimension(s) and
               (ForAll([1..Length(gs)], j -> gs[j] * iso = iso * gb[j]) or
                ForAll([1..Length(gs)], j -> iso * gs[j] = gb[j] * iso)) then
              used[i] := true; ok := true; break;
            fi;
          fi;
        od;
        if not ok then return false; fi;
      od;
      return true;
    end''')
    G = libgap.AlternatingGroup(4)
    C2 = libgap.Group(libgap.eval('(1,2)(3,4)'))
    C3 = libgap.Group(libgap.eval('(1,2,3)'))
    V4 = libgap.Group(libgap.eval('(1,2)(3,4)'), libgap.eval('(1,3)(2,4)'))
    one = libgap.TrivialSubgroup(G)
    plus = [one, V4, G]
    minus = [C2, C2, C3]

    fixcos = libgap.eval('function(G, K, H) return Number(RightTransversal(G, K), '
                         'r -> IsSubset(K, H^(r^-1))); end')

    def marks(L, H, grp=None):
        return sum(int(fixcos(G if grp is None else grp, K, H)) for K in L)
    hypo = [one, C2, C3]
    check(all(marks(plus, H) == marks(minus, H) for H in hypo),
          'prop:hypo-elementary-lefschetz: X = A_4/1 + A_4/V_4 + A_4/A_4 and '
          'Y = 2 A_4/C_2 + A_4/C_3 have chi(X^H) = chi(Y^H) for the 3-hypo-elementary '
          'H = 1, C_2, C_3')
    check(marks(plus, V4) != marks(minus, V4),
          'p. 221: but chi(X^V_4) = %d != %d = chi(Y^V_4), so Lambda_G(X) != '
          'Lambda_G(Y) in b(A_4)' % (marks(plus, V4), marks(minus, V4)))
    check(bool(CONLON(G, plus, minus, 3)),
          'prop:hypo-elementary-lefschetz: L_G(X, F_3) = L_G(Y, F_3): the permutation '
          'modules F_3[X] and F_3[Y] are isomorphic (indecomposable summands matched '
          'by verified isomorphisms)')
    E = libgap.eval('Group((1,2,3), (4,5,6))')
    ones = libgap.TrivialSubgroup(E)
    subs3 = [libgap.Group(libgap.eval(x)) for x in ['(1,2,3)', '(4,5,6)', '(1,2,3)(4,5,6)', '(1,2,3)(4,6,5)']]
    plusE = [ones, E, E, E]
    check(all(marks(plusE, H, E) == marks(subs3, H, E) for H in [ones] + subs3) and
          marks(plusE, E, E) == 3 and marks(subs3, E, E) == 0 and
          bool(CONLON(E, plusE, subs3, 2)),
          'prop:hypo-elementary-lefschetz for E = Z/3 x Z/3, p = 2 (hypo-elementary = '
          'cyclic): E/1 + 3 E/E and the sum of E/C over the four C of order 3 agree on '
          'the cyclic subgroups, differ at E (3 != 0), and the permutation modules over '
          'F_2 are isomorphic')
    # --- |X^op| = |X|, |X x Y| = |X| x |Y|, lem:comparable-maps-homotopic
    crown = ['a', 'b', 'c', 'd']
    cl = lambda x, y: x in 'ab' and y in 'cd'
    interval = [0, 1]

    def product(A, la, B, lb):
        elems = [(a, b) for a in A for b in B]
        return elems, poset_from_relation(
            elems, lambda e, f: e != f and (e[0] == f[0] or la(e[0], f[0])) and (e[1] == f[1] or lb(e[1], f[1])))
    Xc = poset_from_relation(crown, cl)
    Xop = poset_from_relation(crown, lambda x, y: cl(y, x))
    check(set(frozenset(c) for v in Xc.chains().values() for c in v) ==
          set(frozenset(c) for v in Xop.chains().values() for c in v),
          'p. 222: |X^op| = |X| (the same chains; X a circle)')
    _, T2 = product(crown, cl, crown, cl)
    HT = reduced_homology_ZZ(T2.chains())
    check(HT.get(0) == (0, []) and HT.get(1) == (2, []) and HT.get(2) == (1, []),
          'p. 222: |X x Y| = |X| x |Y|: the product of two circle posets has the '
          'homology of the torus (Kuenneth)')
    _, Cyl = product(interval, lambda a, b: a < b, crown, cl)
    HC = reduced_homology_ZZ(Cyl.chains())
    check(HC.get(1) == (1, []) and all(v == (0, []) for k, v in HC.items() if k != 1),
          'lem:comparable-maps-homotopic: |(0 < 1) x X| is the cylinder I x |X| '
          '(homology of the circle)')
    # the Example: S of a cone is conically contractible
    hexcone = [(0, 1, 6), (1, 2, 6), (2, 3, 6), (3, 4, 6), (4, 5, 6), (5, 0, 6)]
    for name, facets, apex in [('a cone over a hexagon', hexcone, 6),
                               ('the 3-simplex', [(0, 1, 2, 3)], 0)]:
        elems = sorted(closure(facets), key=lambda s: (len(s), s))
        idx2 = {s: i for i, s in enumerate(elems)}
        X = poset_from_relation(elems, lambda a, b: set(a) < set(b))
        f = [idx2[tuple(sorted(set(s) | {apex}))] for s in elems]
        x0 = idx2[(apex,)]
        mono = all(f[a] == f[b] or X.lt(f[a], f[b]) for a in range(X.n) for b in X.up[a])
        cone = all((f[x] == x or X.lt(x, f[x])) and (f[x] == x0 or X.lt(x0, f[x])) for x in range(X.n))
        check(mono and cone and is_acyclic_ZZ(X.chains()),
              'def:conically-contractible, Example p. 222: for %s, sigma -> sigma u {x_0} '
              'is a map of posets with sigma <= f(sigma) >= x_0, and S(Delta) is acyclic '
              'over Z' % name)


# ===========================================================================
# Section 6.5
# ===========================================================================


def double_complex(X, Y, f, F, sign=True):
    """The double complex of the proof of lem:quillen: E_(p, q) spanned by pairs
    ((y_0 < ... < y_p), (x_0 < ... < x_q)) with f(x_q) <= y_0; returns the
    total boundary matrices (dict) and the bases."""
    cy = Y.chains()
    cx = X.chains()
    le = lambda a, b: a == b or Y.lt(a, b)
    basis = {}
    for p, ys in cy.items():
        for q, xs in cx.items():
            for y in ys:
                for x in xs:
                    if le(f[x[-1]], y[0]):
                        basis.setdefault(p + q, []).append((y, x))
    pos = {n: {b: i for i, b in enumerate(v)} for n, v in basis.items()}
    D, D0, D1 = {}, {}, {}
    for n in range(1, max(basis) + 1):
        d, d0, d1 = {}, {}, {}
        for j, (y, x) in enumerate(basis[n]):
            p = len(y) - 1
            for i in range(len(y)):
                if len(y) > 1:
                    key = (pos[n - 1][(y[:i] + y[i + 1:], x)], j)
                    d1[key] = d1.get(key, 0) + (-1) ** i
            for i in range(len(x)):
                if len(x) > 1:
                    key = (pos[n - 1][(y, x[:i] + x[i + 1:])], j)
                    d0[key] = d0.get(key, 0) + (-1) ** i * ((-1) ** p if sign else 1)
        for key in set(d0) | set(d1):
            d[key] = d0.get(key, 0) + d1.get(key, 0)
        r, c = len(basis[n - 1]), len(basis[n])
        D[n] = matrix(F, r, c, {k: F(v) for k, v in d.items()}, sparse=True)
        D0[n] = matrix(F, r, c, {k: F(v) for k, v in d0.items()}, sparse=True)
        D1[n] = matrix(F, r, c, {k: F(v) for k, v in d1.items()}, sparse=True)
    return basis, D, D0, D1


def betti_total(basis, D):
    top = max(basis)
    rk = {0: 0, top + 1: 0}
    for k in range(1, top + 1):
        rk[k] = D[k].rank()
    return {k: len(basis[k]) - rk[k] - rk[k + 1] for k in range(top + 1)}


def unreduced(b):
    b = dict(b)
    b[0] = b.get(0, 0) + 1
    return b


def section_6_5():
    F = GF(2)
    # lem:quillen on A_p(G) -> S_p(G): the fibres and the homology
    for name, G, p in [('S_4', libgap.SymmetricGroup(4), 2), ('GL_3(2)', perm_group(libgap.GL(3, 2)), 2),
                       ('S_5', libgap.SymmetricGroup(5), 2), ('A_6', libgap.AlternatingGroup(6), 3)]:
        S = SubPoset(G, p, 'S')
        A = SubPoset(G, p, 'A')
        posA = [S.position(A.subgroup(i)) for i in range(A.n)]
        ok = True
        for P in range(S.n):
            fib = [i for i in range(A.n) if posA[i] == P or S.X.lt(posA[i], P)]
            # conical contraction of i/P = A_p(P) through P_0 = Omega_1 Z(P)
            P0 = libgap.Omega(libgap.Centre(S.subgroup(P)), p, 1)
            j0 = A.position(P0)
            for i in fib:
                prod = libgap.ClosureGroup(A.subgroup(i), P0)
                j = A.position(prod)
                ok = ok and j in fib and j0 in fib and \
                    (j == i or A.X.lt(i, j)) and (j == j0 or A.X.lt(j0, j))
        check(ok, 'lem:quillen, hypothesis for i : A_p(G) -> S_p(G): every fibre i/P '
              '= A_p(P) is conically contractible via A <= A P_0 >= P_0 (%s, p = %d, '
              '%d fibres)' % (name, p, S.n))
        Fp = GF(p)
        check(reduced_betti(A.X.chains(), Fp) == reduced_betti(S.X.chains(), Fp),
              'lem:quillen: A_p(G) and S_p(G) have the same homology over F_%d (%s: %s)'
              % (p, name, reduced_betti(A.X.chains(), Fp)))
    # the double complex of the proof (over Q: over F_2 the sign is invisible)
    F = QQ
    G = libgap.SymmetricGroup(4)
    S = SubPoset(G, 2, 'S')
    A = SubPoset(G, 2, 'A')
    f = [S.position(A.subgroup(i)) for i in range(A.n)]
    basis, D, D0, D1 = double_complex(A.X, S.X, f, F)
    ok = all((D[k - 1] * D[k]).is_zero() for k in range(2, max(basis) + 1))
    check(ok, 'p. 223: with the sign (-1)^p on the vertical differential the squares '
          'anticommute and d^2 = 0 on the total complex')
    _, Dn, _, _ = double_complex(A.X, S.X, f, F, sign=False)
    refuted(all((Dn[k - 1] * Dn[k]).is_zero() for k in range(2, max(basis) + 1)),
            'p. 223: without the sign (-1)^p the total differential does not square '
            'to zero')
    bt = betti_total(basis, D)
    bx = unreduced(reduced_betti(A.X.chains(), F))
    by_ = unreduced(reduced_betti(S.X.chains(), F))
    check(all(bt.get(k, 0) == bx.get(k, 0) == by_.get(k, 0) for k in set(bt) | set(bx) | set(by_)),
          'lem:quillen, proof: the total homology of the double complex is H_*(X) = '
          'H_*(Y) for i : A_2(S_4) -> S_2(S_4) (contractible fibres): %s' % bt)
    # a map with non-contractible fibres: the circle onto (0 < 1)
    Xc = poset_from_relation(['a', 'b', 'c', 'd'], lambda x, y: x in 'ab' and y in 'cd')
    Y2 = poset_from_relation([0, 1], lambda a, b: a < b)
    fc = [0, 0, 1, 1]
    basis, D, _, _ = double_complex(Xc, Y2, fc, F)
    bt = betti_total(basis, D)
    check(bt == {0: 1, 1: 1},
          'lem:quillen, proof: without the hypothesis (f/0 = two points) the total '
          'homology is still H_*(X) (the circle), not H_*(Y) (a point)')
    # Webb's conjecture (Symonds): the orbit space |S_p(G)|/G is acyclic over Z
    cases = []
    for name in group_range():
        G = GROUPS[name]
        for p, _ in factor(int(G.Size())):
            if int(libgap.Size(libgap.PCore(G, p))) == 1:
                cases.append((name, p))
    ng = len(cases)
    for name in named_groups():
        G = GROUPS[name]
        for p, _ in factor(int(G.Size())):
            if p <= 5 and int(libgap.Size(libgap.PCore(G, p))) == 1:
                cases.append((name, p))
    nall = 0
    for name, p in cases:
        G = GROUPS[name]
        kinds = 'SAB' if int(G.Size()) <= 360 else 'B'
        for kind in kinds:
            P = subposet(name, p, kind)
            by = P.X.chains()
            C, nor = orbit_chain_complex(by, P.perms())
            H = C.homology()
            ok = all(A.order() == 1 for A in H.values())
            check(ok, 'Conjecture (Webb) p. 224, proved by Symonds [404]: |%s_%d(G)|/G is '
                  'acyclic over Z (%s; %s orbits of chains)' % (kind, p, name, nor))
            nall += 1
    check(ng == 112, 'Webb\'s conjecture: %d pairs (G, p) of RANGE with O_p(G) = 1 '
          'and the named groups covered' % ng)
    # Exercise (i): X ~_G S(|X|): invariant chains are the chains of X^H
    for name, G in [('S_4', libgap.SymmetricGroup(4)), ('A_5', libgap.AlternatingGroup(5))]:
        P = SubPoset(G, 2, 'S')
        by = P.X.chains()
        ok = True
        for H in subgroup_classes(G):
            fx = set(P.fixed(H))
            perms = [[int(i) - 1 for i in pm] for pm in PERMS(P.data, H.GeneratorsOfGroup())]
            inv = [c for v in by.values() for c in v
                   if all(set(pm[x] for x in c) == set(c) for pm in perms)]
            ok = ok and all(all(x in fx for x in c) for c in inv) and \
                len(inv) == sum(len(v) for v in P.X.chains(fx).values())
            # chi(S(|X|)^H) = chi(X^H): the poset of invariant chains
            elems = inv
            Xs = poset_from_relation(elems, lambda a, b: set(a) < set(b))
            ok = ok and Xs.euler() == P.X.euler(fx)
        check(ok, 'Exercise (i) p. 224: an H-invariant chain of S_2(G) consists of '
              'H-fixed points (|X| is G-simplicial), and chi(S(|X|)^H) = chi(X^H) for '
              'all H (%s)' % name)


# ===========================================================================
# Section 6.6
# ===========================================================================


def section_6_6():
    # the broad loop over RANGE
    npairs = 0
    ngroups = 0
    nsolv = 0
    bouc = 0
    for name in group_range():
        G = GROUPS[name]
        order, k = [int(x) for x in name[len('SmallGroup('):-1].split(',')]
        ngroups += 1
        reps = subgroup_classes(G)
        for p, _ in factor(order):
            npairs += 1
            post = {kind: subposet(name, p, kind) for kind in 'SABZ'}
            mk = {kind: [post[kind].X.euler(post[kind].fixed(H)) for H in reps] for kind in 'SABZ'}
            check(mk['S'] == mk['A'] == mk['B'] == mk['Z'],
                  'th:quillen-equivalence, th:bouc-equivalence, Exercise p. 226: '
                  'chi(S_p^H) = chi(A_p^H) = chi(B_p^H) = chi(Z_p^H) for all H '
                  '(SmallGroup(%d, %d), p = %d)' % (order, k, p))
            S = post['S']
            chi = S.X.euler()
            check((chi - 1) % ppart(order, p) == 0,
                  'cor:ken-brown: chi(S_p(G)) = 1 mod |G|_p (SmallGroup(%d, %d), p = %d: '
                  'chi = %d)' % (order, k, p, chi))
            Op = libgap.PCore(G, p)
            fixedG = S.fixed(G)
            check((len(fixedG) > 0) == (int(Op.Size()) > 1),
                  'p. 225: S_p(G)^G is non-empty iff O_p(G) != 1')
            # Theorem 6.6.1, proof: P_0 = Omega_1 Z(P) and A P_0
            A = post['A']
            okq = True
            for c in libgap.ConjugacyClassesSubgroups(G.SylowSubgroup(p)):
                P = c.Representative()
                if int(P.Size()) == 1:
                    continue
                P0 = libgap.Omega(libgap.Centre(P), p, 1)
                okq = okq and int(P0.Size()) > 1 and bool(libgap.IsElementaryAbelian(P0))
                for d in P.ConjugacyClassesSubgroups():
                    Aa = d.Representative()
                    if int(Aa.Size()) > 1 and bool(Aa.IsElementaryAbelian()):
                        okq = okq and bool(libgap.ClosureGroup(Aa, P0).IsElementaryAbelian())
            check(okq, 'th:quillen-equivalence, proof: P_0 = Omega_1 Z(P) != 1 and A P_0 '
                  'is elementary abelian for elementary abelian A <= P (all P up to '
                  'conjugacy in a Sylow subgroup; SmallGroup(%d, %d), p = %d)' % (order, k, p))
            if int(Op.Size()) > 1:
                okc = True
                o = S.position(Op)
                for i in range(S.n):
                    j = S.position(libgap.ClosureGroup(S.subgroup(i), Op))
                    okc = okc and j >= 0 and (j == i or S.X.lt(i, j)) and (j == o or S.X.lt(o, j))
                    for i2 in S.X.up[i]:
                        j2 = S.position(libgap.ClosureGroup(S.subgroup(i2), Op))
                        okc = okc and (j2 == j or S.X.lt(j, j2))
                check(okc, 'Comment p. 225: O_p(G) != 1 => P -> P O_p(G) is a map of posets '
                      'with P <= P O_p(G) >= O_p(G) (SmallGroup(%d, %d), p = %d)' % (order, k, p))
            elif bool(G.IsSolvable()):
                nsolv += 1
                by = A.X.chains()
                b = reduced_betti(by, QQ) if A.n <= 400 else reduced_betti(by, GF(10007))
                check(any(v != 0 for v in b.values()),
                      'Comment p. 225 (Quillen): G soluble with O_p(G) = 1 => '
                      'A_p(G) is not contractible: H~(A_p(G); Q) = %s (SmallGroup(%d, %d), '
                      'p = %d)' % (b, order, k, p))
            # Bouc's observation for all classes of P not in B_p
            B = post['B']
            for i in class_reps_of_elements(S):
                P = S.subgroup(i)
                if B.position(P) >= 0:
                    continue
                N = libgap.Normalizer(G, P)
                OpN = libgap.PCore(N, p)
                okb = int(OpN.Size()) > int(P.Size())
                for j in S.X.up[i]:
                    Q = S.subgroup(j)
                    NQ = libgap.Normalizer(Q, P)
                    R = libgap.ClosureGroup(NQ, OpN)
                    a, b2, c = S.position(NQ), S.position(R), S.position(OpN)
                    okb = okb and a >= 0 and b2 >= 0 and c >= 0 and S.X.lt(i, a) and \
                        (a == j or S.X.lt(a, j)) and (a == b2 or S.X.lt(a, b2)) and \
                        (c == b2 or S.X.lt(c, b2)) and S.X.lt(i, c)
                check(okb, 'p. 225, Bouc\'s observation: for P not in B_p(G), every Q > P '
                      'has Q >= N_Q(P) <= N_Q(P) O_p N_G(P) >= O_p N_G(P) > P (SmallGroup(%d, '
                      '%d), p = %d, |P| = %d)' % (order, k, p, int(P.Size())))
                bouc += 1
    check(ngroups == 455 and npairs == 943,
          'RANGE: %d groups, %d pairs (G, p)' % (ngroups, npairs))
    check(nsolv > 50, 'Quillen\'s theorem for soluble groups: %d pairs (G, p) with '
          'O_p(G) = 1 checked' % nsolv)
    # Lemma 6.6.3, Proposition 6.6.5 and the author's correction on a list of groups
    check(bouc > 500, 'Bouc\'s observation: %d classes of non-radical P checked' % bouc)
    printed_fails = 0
    for name in named_groups():
        G = GROUPS[name]
        if int(G.Size()) > 720:
            continue
        for p in (2, 3):
            S = subposet(name, p, 'S')
            A = subposet(name, p, 'A')
            B = subposet(name, p, 'B')
            Fp = GF(p)
            inB = set(S.position(B.subgroup(i)) for i in range(B.n))
            inA = set(S.position(A.subgroup(i)) for i in range(A.n))
            if S.n <= 300:
                # e_X(A_p) = X: (-, x] n A_p = A_p(x) is acyclic for every x
                okE = all(acyclic(S.X.chains(set(S.X.interval_down(x, closed=True)) & inA), Fp)
                          for x in range(S.n))
                check(okE, 'lem:contractible-intervals: e_X(A_p(G)) = S_p(G) (%s, p = %d), '
                      'whence A_p(G) ~ S_p(G)' % (name, p))
                fXB = [x for x in range(S.n)
                       if acyclic(S.X.chains((set(S.X.up[x]) | {x}) & inB), Fp)]
                check(inB <= set(fXB) and reduced_betti(S.X.chains(fXB), Fp) ==
                      reduced_betti(S.X.chains(inB), Fp),
                      'lem:contractible-intervals: B_p(G) c f_X(B_p(G)) (%d of %d elements) '
                      'have the same homology over F_%d (%s)' % (len(fXB), S.n, p, name))
            hreps = subgroup_classes(G) if int(G.Size()) <= 120 else \
                [libgap.Group(c.Representative()) for c in G.ConjugacyClasses()]
            for H in hreps:
                Xh = S.fixed(H)
                if not Xh or len(Xh) > 300:
                    continue
                Xs = set(Xh)
                star = [x for x in Xh if not acyclic(S.X.chains(set(S.X.up[x]) & Xs), Fp)]
                Bh = [x for x in Xh if x in inB]
                check(set(star) <= set(Bh),
                      'th:bouc-equivalence, proof: (S_p(G)^H)^* c B_p(G)^H (%s, p = %d, '
                      '|H| = %d)' % (name, p, int(H.Size())))
                bs = reduced_betti(S.X.chains(star), Fp)
                check(bs == reduced_betti(S.X.chains(Bh), Fp) == reduced_betti(S.X.chains(Xh), Fp),
                      'prop:bouc-bounded-height: X^* c B_p(G)^H c X = S_p(G)^H have the same '
                      'homology over F_%d (%s, |H| = %d: %s)' % (p, name, int(H.Size()), bs))
                Ss = set(star)
                okc = True
                for b in Xh:
                    if b in Ss:
                        continue
                    upX = set(S.X.up[b]) & Xs
                    upS = upX & Ss
                    okc = okc and upS <= upX and acyclic(S.X.chains(upS), Fp)
                    if not upX <= Ss:
                        printed_fails += 1
                check(okc, 'prop:bouc-bounded-height, proof with the author\'s correction '
                      '(p. 226): for b not in X^*, (b, -)_(X^*) c (b, -)_X and both are '
                      'acyclic (%s, |H| = %d)' % (name, int(H.Size())))
    refuted(printed_fails == 0,
            'p. 226 as printed: "the inclusion (b, -)_X -> (b, -)_(X^*)": there are b '
            '(%d cases) with (b, -)_X not contained in X^*, so it is not an inclusion'
            % printed_fails)


def main():
    sections = [section_6_1, section_6_2, section_6_3, section_6_4, section_6_5,
                section_6_6]
    only = sys.argv[1:]
    for f in sections:
        if not only or f.__name__ in only:
            f()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
