"""Exact checks of Chapter 6, Sections 6.7-6.9 (Sage, GAP through libgap).

Run: sage -python checks/sage/chapter-6b.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-6b: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 6, Sections
6.7-6.9, printed pp. 226-235.  Our files: content/06-07-steinberg-module.typ,
content/06-08-chevalley-groups.typ, content/06-09-alperin-conjecture.typ
(Sections 6.1-6.6: chapter-6a.py).  Pages are printed pages; labels are
those of content/06-*.typ.  Expected values are the book's statements read
off the printed pages and the author's corrections ("Author's comments and
corrections", 8 September 2010) as applied in our text; where the printed
text was corrected, the printed reading is kept as a refuted check
(`refuted`) beside the corrected one.

Conventions as in chapter-6a.py: posets are realised by their order
complexes, chi is the Euler characteristic, chi~ = chi - 1, and the marks of
Lambda~_G(X) are chi~(X^H).  St_p(G) = L~_G(|S_p(G)|) (Definition 6.7.1); its
character at g is chi~(S_p(G)^<g>) (the trace of g on the alternating sum of
the permutation modules of chains).  Buildings of classical groups are
computed in Sage as posets of proper non-zero (totally isotropic, totally
singular) subspaces of F_q^n with the forms named below; linear algebra in
odd characteristic is done with sparse matrices.  SMALL is the set of all
groups of order at most 60 in GAP's library except those of prime-power
order bigger than 16, with every prime divisor p of the order (240 groups,
474 pairs (G, p)).

What is checked, by section:

section_6_7 (pp. 226-228):
  * th:steinberg-virtual-projective and lem:hypo-elementary-conically-contractible
    for all (G, p) of SMALL and S_5, A_6, GL_3(2), PSL_2(8), PSL_2(11),
    SL_2(5): for every class of p-hypo-elementary subgroups H with
    O_p(H) != 1, P -> P O_p(H) is a map of posets on S_p(G)^H with
    P <= P O_p(H) >= O_p(H), and chi~(S_p(G)^H) = 0; in particular the
    character of St_p(G) vanishes on the p-singular elements (Quillen's
    statement; with Brauer's characterisation of the generalised characters
    vanishing off the p-regular elements this makes it the character of a
    virtual projective module); cor:ken-brown, chi(S_p(G)) = 1 mod |G|_p,
    for the same groups and for S_6, A_7, PSL_2(q) (q = 13, 16, 17, 19, 25,
    27), PSL_3(3), M_11;
  * the module statement where the homology is concentrated in one degree:
    H~_(r-1) of the building of GL_n(F_q) (n = 2: q <= 9; n = 3: q <= 4;
    GL_4(2), GL_4(3)) and of Sp_4(2), Sp_4(3) is a free module over
    a Sylow p-subgroup U of rank one (dim M/JM = 1, dim M = |U|), so it is
    projective;
  * Alperin's example (p. 228) with p = 3, q = 7: H = Z/7 x| Z/3, G = H wr
    Z/3, |G| = p^(p+1) q^p = 27783; every elementary abelian subgroup of
    order > p^2 lies in H^p; the complex |A_3(G)| has dimension 2 and all its
    2-simplices lie in |A_3(H^3)|, so H~_2(A_3(G)) = H~_2(A_3(H^3)); over F_3,
    H~_*(A_3(G)) = (0, 2646, 216) and chi~ = -2430 = 0 mod 81; the corrected
    reading ("So long as p > 2 the (p - 1)st homology ... has dimension
    (q - 1)^p"): dim H~_2 = 216 = 6^3, and since the 3-part of
    p (q - 1)^p = 3 * 216 is 81 = |G|_3, which does not divide 216, the
    module is not projective; independently, the generator t of the top
    group Z/3 has a fixed space of dimension 76 != 216/3 on H~_2, so it is
    not even free over <t>; the printed reading ("as long as p > 3, the
    pth homology ... has dimension p^p ... divisible by p^(p+1)") is
    refuted: elementary abelian subgroups outside the base have order at
    most p^2 (checked in Z/p wr Z/p for p = 3, 5, 7), so |A_p(G)| has
    dimension p - 1 and H~_p = 0 != p^p; the restriction p > 2: for p = 2,
    q = 3 (G = S_3 wr Z/2) H~_1(A_2(G)) has dimension 16, not (q - 1)^2 = 4 =
    dim H~_1(A_2(H^2)); the author's reason "divisible by the p-part of
    p(q - 1)^p" uses p^2 not dividing q - 1: for p = 3, q = 19 the 3-part of
    3 * 18^3 is 3^7, which does not divide |G| = 3^4 19^3 (the regular module
    is projective), while 3^4 divides 18^3; the conclusion still holds there
    (the model H~_(p-1)(A_p(H^p)) = H~_0(A_p(H))^(x)p, confirmed for q = 7,
    gives t-fixed points of dimension 1956 != 5832/3).
section_6_8 (pp. 228-233):
  * root systems (Sage): numbers of roots, positive roots and ranks of A_l,
    B_l, C_l, D_l, E_6, E_7, E_8, F_4, G_2; B_2 = C_2, D_3 = A_3,
    D_2 = A_1 x A_1, B_l != C_l (l >= 3) (Cartan matrices up to
    relabelling), so the list "A_l, l >= 1; B_l, l >= 2; C_l, l >= 3;
    D_l, l >= 4" has no repetitions; GL_n: the eigenvalue of
    diag(x_1, ..., x_n) on E_ij is x_i/x_j, the roots e_i - e_j lie in
    sum r_i = 0 and form a system of type A_(n-1) (Cartan matrix), dim gl_n =
    n + |Phi|; dim so_(2n+1), sp_(2n), so_(2n) = n + |Phi| for B_n, C_n, D_n;
  * "The subscript refers to the (Lie) rank" after the author's correction
    of p. 229: for GL_n the Lie rank is n (the diagonal torus) but the type is
    A_(n-1): refuted for "Lie", true for the semisimple rank n - 1 (the Lie
    rank of the derived group SL_n);
  * orders: |G|_p = q^N with N = |Phi^+| for GL_n(q), SL_n(q), Sp_2n(q),
    SO_(2n+1)(q), Omega^+_2n(q) (GAP, small n and q; the full orthogonal group
    GO^+_2n(q) is not connected and has a factor 2 more in characteristic 2);
  * parabolic subgroups: the overgroups of B = N_G(U) (U a Sylow
    p-subgroup) are 2^r in number, r the semisimple rank (GL_2(q), q <= 5;
    GL_3(2), GL_3(3), GL_4(2), Sp_4(2), Sp_4(3)); th:borel-tits for GL_n(q)
    (GL_2(q), q <= 7; GL_3(2), GL_3(3), GL_4(2)): with the flag of fixed
    spaces V_1 < V_2 < ... of a p-subgroup U and H(U) the group of the
    proof, U <= H(U) always and U = O_p N(U) iff U = H(U); the radical
    p-subgroups correspond bijectively to the flags, U <= U' iff the flag
    of U is contained in that of U' (B_p(G) is the opposite of the poset of
    parabolics), and N_G(U) is the stabiliser of the flag;
  * the Tits building and th:solomon-tits: for GL_n(q) (as above),
    Sp_4(2), Sp_4(3), Sp_6(2) (standard alternating form), O^+_4(2),
    O^+_4(3), O^+_6(2) (x_1 x_2 + x_3 x_4 + ...) and O_5(3)
    (x_1 x_2 + x_3 x_4 + x_5^2) the poset of proper non-zero subspaces
    (totally isotropic, totally singular) has dimension r - 1, r the
    semisimple rank, every chain lies in one of maximal length, and its
    reduced homology over F_p is concentrated in degree r - 1 of dimension
    q^N; over Z for the smaller cases; the printed "r is the Lie rank" is
    refuted for GL_n (dimension n - 2, not n - 1); Quillen's proof for
    GL_n(q): the hyperplanes complementary to a line L are q^(n-1) in
    number, Y = Subsp(V) - H is acyclic, q : Y -> Subsp(V/L) u {0} is
    well defined with fibres q/W having the maximal element W~, Link(H) =
    Subsp(H), and H~_(n-2) has rank q^(n-1) rank H~_(n-3)(Subsp(H));
  * the Steinberg module: St_p(G) = (-1)^(r-1) St; its character
    chi~(B_p(G)^<g>) is 0 at p-singular g and +-|C_G(g)|_p at p-regular g
    (Carter, Finite groups of Lie type, Theorem 6.4.7), with value
    (-1)^(r-1) q^N at 1, for GL_2(q) (q <= 7), GL_3(2), GL_3(3), Sp_4(2),
    Sp_4(3); the same characters from S_p(G) for GL_2(q) (q <= 4), GL_3(2).
section_6_9 (pp. 233-235):
  * prop:lefschetz-invariant-inversion in b(G): the marks of Lambda_G(X) and
    of - sum_x ind Lambda~_(Stab x)((x, -)) (induction by fixed cosets) agree
    at all classes of H, for X = S_p(G), S_p(G) u {1}, B_p(G) of S_4, A_5,
    S_5, GL_2(3), GL_3(2);
  * prop:upper-interval-equivalence: for every class of p-subgroups P
    (including 1) the maps r(Q) = N_Q(P) and i(R) = R satisfy r(Q) > P,
    r o i = id, i o r(Q) <= Q, are monotone and N_G(P)-equivariant, and the
    marks of (P, -) and of S_p(N_G(P)/P) (computed in the quotient group)
    agree at every subgroup of N_G(P): the identities hold in b(N_G(P)) (the
    corrected reading; both sides are N_G(P)-posets);
  * th:steinberg-inversion in b(G): 1 = - sum_P ind Lambda~(S_p(N_G(P)/P))
    at all classes of H, with S_p(N_G(P)/P) computed in the quotient group,
    for S_4, A_5, S_5, GL_2(3), GL_3(2), SL_2(5), A_6 (p = 2, 3, 5); for all
    (G, p) of SMALL in the form sum_(P in (S_p(G) u {1})^H) chi~((P, -)^H) =
    -1; the Remarks (i): P != O_p N_G(P) => O_p(N_G(P)/P) != 1 and all marks
    of Lambda~(S_p(N_G(P)/P)) vanish;
  * length functions: l(G) = number of p-regular classes = l(G/O_p(G));
    prop:length-function-equivalence: with alpha = l and with alpha(G) =
    k(G/O_p(G)) (number of classes), beta defined by (i) recursively
    satisfies (ii) for all (G, p) of SMALL and the named groups of order
    <= 720; with alpha = k (number of classes), which violates the
    hypothesis, (ii) fails (S_3, p = 3); Alperin's conjecture
    l(G) = sum_P f_0(N_G(P)/P) for SMALL and
    S_5, A_6, GL_3(2), GL_2(3), SL_2(5), PSL_2(8), PSL_2(11), A_7, M_11, and
    Robinson's reformulation f_0(G) = -l(Lambda~_G(S_p(G))) (also with B_p(G)
    and A_p(G); B_p(G) only above order 360) for those of order <= 720.

What these checks do NOT establish.  Homotopy statements are seen through
homology; Brauer's characterisation of virtual projective characters is
used, not checked; projectivity is checked only for the modules listed.
For Alperin's example only q = 7 (p = 3) and q = 3 (p = 2) are computed in
full; q = 19 rests on arithmetic and on the tensor model, which is
confirmed for q = 7 only.  The theory of algebraic groups of Section 6.8
(tori, Borel subgroups, the Frobenius morphism) is not computed; only finite
groups, root systems and the stated counts.  Lusztig's theorem (p. 233) is
not checked.  Group statements are checked on the groups listed, not in
general.  Nothing here compares our text with the printed book.
"""
import itertools
import sys
import time

from sage.all import (GF, QQ, ZZ, ChainComplex, CartanMatrix, FractionField,
                      PolynomialRing, RootSystem, VectorSpace, binomial,
                      factor, identity_matrix, is_prime_power, libgap, matrix,
                      vector)

SCOPE = 'chapter-6b'
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
# Posets, order complexes, homology (as in chapter-6a.py)
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
        S = set(range(self.n)) if S is None else set(S)
        h = {}
        for x in self.order:
            if x in S:
                h[x] = 1 - sum(h[y] for y in self.down[x] if y in S)
        return sum(h.values())

    def chains(self, S=None):
        S = set(range(self.n)) if S is None else set(S)
        out = {}

        def ext(c):
            out.setdefault(len(c) - 1, []).append(tuple(c))
            for y in self.up[c[-1]]:
                if y in S:
                    ext(c + [y])
        for x in sorted(S):
            ext([x])
        return out


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
    if not by or not by.get(0):
        return {-1: 1}
    mats = boundary_mats(by, F)
    top = max(by)
    rk = {0: 1, top + 1: 0}
    for k in range(1, top + 1):
        rk[k] = mats[k].rank()
    b = {k: len(by[k]) - rk[k] - rk[k + 1] for k in range(top + 1)}
    return {k: v for k, v in b.items() if v}


def reduced_homology_ZZ(by):
    mats = boundary_mats(by, ZZ)
    data = {k: mats[k] for k in mats}
    data[0] = matrix(ZZ, 1, len(by[0]), [1] * len(by[0]), sparse=True)
    H = ChainComplex(data, degree=-1).homology()
    out = {}
    for k, A in H.items():
        inv = list(A.invariants())
        out[k] = (inv.count(0), sorted(x for x in inv if x != 0))
    return out


def ppart(n, p):
    n = int(n)
    r = 1
    while n % p == 0:
        n //= p
        r *= p
    return r


# ===========================================================================
# Subgroup posets in GAP (as in chapter-6a.py)
# ===========================================================================

libgap.eval(r'''
BensonCh6PSub := function(G, p, kind)
  local P, subs, reps, S, all, keys, n, up;
  P := SylowSubgroup(G, p);
  if Size(P) = 1 then
    return rec(n := 0, subs := [], keys := [], up := [], sizes := []);
  fi;
  subs := Filtered(Concatenation(List(ConjugacyClassesSubgroups(P), AsList)),
                   S -> Size(S) > 1);
  if kind = "A" then subs := Filtered(subs, IsElementaryAbelian); fi;
  reps := [];
  for S in subs do
    if ForAll(reps, R -> Size(R) <> Size(S) or not IsConjugate(G, R, S)) then
      Add(reps, S);
    fi;
  od;
  if kind = "B" then
    reps := Filtered(reps, R -> PCore(Normalizer(G, R), p) = R);
  fi;
  all := Concatenation(List(reps, R ->
           List(RightTransversal(G, Normalizer(G, R)), g -> R^g)));
  keys := List(all, S -> Set(AsList(S)));
  SortParallel(keys, all);
  n := Length(all);
  up := List([1..n], i -> Filtered([1..n], j ->
          Length(keys[j]) > Length(keys[i]) and IsSubset(keys[j], keys[i])));
  return rec(n := n, subs := all, keys := keys, up := up,
             sizes := List(keys, Length));
end''')
PSUB = libgap.eval('BensonCh6PSub')
FIXED = libgap.eval(r'''
function(data, H)
  local gens;
  gens := GeneratorsOfGroup(H);
  return Filtered([1..data.n], i -> ForAll(gens, h ->
    ForAll(GeneratorsOfGroup(data.subs[i]), x -> x^h in data.keys[i])));
end''')
PERMS = libgap.eval(r'''
function(data, gens)
  return List(gens, g -> List(data.keys, k ->
    PositionSorted(data.keys, Set(List(k, x -> x^g)))));
end''')
POSITION = libgap.eval(r'''
function(data, S)
  local k, i;
  k := Set(AsList(S));
  i := PositionSorted(data.keys, k);
  if i <= data.n and data.keys[i] = k then return i; fi;
  return 0;
end''')
FIXCOS = libgap.eval('function(G, K, H) return Number(RightTransversal(G, K), '
                     'r -> IsSubset(K, H^(r^-1))); end')


def perm_group(G):
    return libgap.Image(libgap.IsomorphismPermGroup(G))


class SubPoset:
    def __init__(self, G, p, kind):
        self.G, self.p, self.kind = G, p, kind
        self.data = PSUB(G, p, kind)
        self.n = int(self.data['n'])
        self.X = Poset(self.n, [[int(j) - 1 for j in u] for u in self.data['up']])
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


def chain_orbit_reps(P):
    """Representatives of the G-orbits of chains of a SubPoset."""
    by = P.X.chains()
    reps = []
    for k, v in by.items():
        index = {c: i for i, c in enumerate(v)}
        ids, m = orbit_ids(v, index, P.perms(), lambda pm, c: tuple(pm[x] for x in c))
        first = {}
        for i, o in enumerate(ids):
            first.setdefault(o, v[i])
        reps += list(first.values())
    return reps


GROUPS = {}
POSETS = {}


def small_range():
    out = []
    for order in range(2, 61):
        if is_prime_power(order) and order > 16:
            continue
        for k in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            name = 'SmallGroup(%d, %d)' % (order, k)
            if name not in GROUPS:
                GROUPS[name] = perm_group(libgap.SmallGroup(order, k))
            out.append(name)
    return out


def named(names):
    makers = {'S_4': lambda: libgap.SymmetricGroup(4),
              'A_5': lambda: libgap.AlternatingGroup(5),
              'S_5': lambda: libgap.SymmetricGroup(5),
              'A_6': lambda: libgap.AlternatingGroup(6),
              'S_6': lambda: libgap.SymmetricGroup(6),
              'A_7': lambda: libgap.AlternatingGroup(7),
              'GL_2(3)': lambda: perm_group(libgap.GL(2, 3)),
              'SL_2(5)': lambda: perm_group(libgap.SL(2, 5)),
              'GL_3(2)': lambda: perm_group(libgap.GL(3, 2)),
              'PSL_2(8)': lambda: libgap.PSL(2, 8),
              'PSL_2(11)': lambda: libgap.PSL(2, 11),
              'PSL_2(13)': lambda: libgap.PSL(2, 13),
              'PSL_2(16)': lambda: libgap.PSL(2, 16),
              'PSL_2(17)': lambda: libgap.PSL(2, 17),
              'PSL_2(19)': lambda: libgap.PSL(2, 19),
              'PSL_2(25)': lambda: libgap.PSL(2, 25),
              'PSL_2(27)': lambda: libgap.PSL(2, 27),
              'PSL_3(3)': lambda: libgap.PSL(3, 3),
              'M_11': lambda: libgap.MathieuGroup(11)}
    for k in names:
        if k not in GROUPS:
            GROUPS[k] = makers[k]()
    return list(names)


def subposet(name, p, kind):
    key = (name, p, kind)
    if key not in POSETS:
        POSETS[key] = SubPoset(GROUPS[name], p, kind)
    return POSETS[key]


def primes_of(G):
    return [p for p, _ in factor(int(G.Size()))]


# ===========================================================================
# Section 6.7
# ===========================================================================

HYPO = libgap.eval(r'''
function(G, p)
  # classes of p-hypo-elementary subgroups H (H/O_p(H) cyclic) with O_p(H) <> 1
  return Filtered(List(ConjugacyClassesSubgroups(G), Representative), H ->
    Size(PCore(H, p)) > 1 and IsCyclic(H / PCore(H, p)));
end''')


def section_6_7_virtual_projective():
    names = small_range() + named(['S_5', 'A_6', 'GL_3(2)', 'PSL_2(8)', 'PSL_2(11)', 'SL_2(5)'])
    npairs = nh = 0
    for name in names:
        G = GROUPS[name]
        for p in primes_of(G):
            S = subposet(name, p, 'S')
            ok = True
            for H in HYPO(G, p):
                O = libgap.PCore(H, p)
                fx = S.fixed(H)
                fs = set(fx)
                o = S.position(O)
                ok = ok and o in fs
                for i in fx:
                    j = S.position(libgap.ClosureGroup(S.subgroup(i), O))
                    ok = ok and j in fs and (j == i or S.X.lt(i, j)) and (j == o or S.X.lt(o, j))
                ok = ok and S.X.euler(fx) - 1 == 0
                nh += 1
            check(ok, 'lem:hypo-elementary-conically-contractible: for every p-hypo-elementary '
                  'H with O_p(H) != 1, S_p(G)^H is conically contractible via P <= P O_p(H) '
                  '>= O_p(H) and chi~(S_p(G)^H) = 0 (%s, p = %d)' % (name, p))
            # the character of St_p(G) at p-singular elements
            sing = [libgap.Group(c.Representative()) for c in G.ConjugacyClasses()
                    if int(c.Representative().Order()) % p == 0]
            check(all(S.X.euler(S.fixed(C)) == 1 for C in sing),
                  'th:steinberg-virtual-projective (Quillen): the character of St_p(G) '
                  'vanishes at the %d classes of p-singular elements (%s, p = %d)'
                  % (len(sing), name, p))
            chi = S.X.euler()
            check((chi - 1) % ppart(G.Size(), p) == 0,
                  'cor:ken-brown: chi(S_p(G)) = %d = 1 mod |G|_p = %d (%s)'
                  % (chi, ppart(G.Size(), p), name))
            npairs += 1
    check(npairs >= 480 and nh > 1000,
          'th:steinberg-virtual-projective: %d pairs (G, p), %d classes of '
          'hypo-elementary H' % (npairs, nh))
    for name in named(['S_6', 'A_7', 'PSL_2(13)', 'PSL_2(16)', 'PSL_2(17)', 'PSL_2(19)',
                       'PSL_2(25)', 'PSL_2(27)', 'PSL_3(3)', 'M_11']):
        G = GROUPS[name]
        for p in primes_of(G):
            P = subposet(name, p, 'B')
            chi = P.X.euler()
            check((chi - 1) % ppart(G.Size(), p) == 0,
                  'cor:ken-brown (with B_p(G) ~_G S_p(G)): chi = %d = 1 mod |G|_p = %d '
                  '(%s, p = %d)' % (chi, ppart(G.Size(), p), name, p))


# --------------------------------------------------------------------------
# buildings of classical groups over F_q


def space_key(W):
    E = W.echelonized_basis_matrix()
    return tuple(tuple(r) for r in E.rows())


def isotropic(B, J):
    return (B * J * B.transpose()).is_zero()


def singular(B, Q):
    rows = B.rows()
    if any(Q(v) != 0 for v in rows):
        return False
    return all(Q(v + w) - Q(v) - Q(w) == 0 for v, w in itertools.combinations(rows, 2))


class Building:
    """Proper non-zero subspaces of F^n (totally isotropic for J, totally
    singular for Q) ordered by inclusion; the group acts on row vectors."""

    def __init__(self, F, n, maxdim, J=None, Q=None):
        V = VectorSpace(F, n)
        self.F, self.n = F, n
        spaces = []
        for k in range(1, maxdim + 1):
            for W in V.subspaces(k):
                B = W.basis_matrix()
                if J is not None and not isotropic(B, J):
                    continue
                if Q is not None and not singular(B, Q):
                    continue
                spaces.append(W)
        self.spaces = spaces
        self.key = {space_key(W): i for i, W in enumerate(spaces)}
        vecs = [frozenset(tuple(v) for v in W) for W in spaces]
        dims = [W.dimension() for W in spaces]
        up = [[j for j in range(len(spaces)) if dims[j] > dims[i] and vecs[i] <= vecs[j]]
              for i in range(len(spaces))]
        self.dims = dims
        self.X = Poset(len(spaces), up)
        self.by = self.X.chains()

    def act(self, g):
        """The permutation of the elements induced by the matrix g (rows)."""
        sp = self.F.characteristic() != 2
        return [self.key[space_key((matrix(self.F, W.basis_matrix(), sparse=sp) * g).row_space())]
                for W in self.spaces]


def gap_mats(gens, F):
    """GAP matrices as Sage matrices (sparse in odd characteristic: dense
    products over GF(p), p odd, stop with SIGILL in the local OpenBLAS build)."""
    sp = F.characteristic() != 2
    return [matrix(F, [[F(x) for x in row] for row in g.sage()], sparse=sp) for g in gens]


def top_module_free(Bd, F, sylow_gens):
    """M = H~_top = Ker(d_top) inside the top chains; returns (dim M, dim M/JM)."""
    top = max(Bd.by)
    chains = Bd.by[top]
    pos = {c: i for i, c in enumerate(chains)}
    n = len(chains)
    if top == 0:
        D = matrix(F, 1, n, [1] * n, sparse=True)
    else:
        D = boundary_mats(Bd.by, F)[top]
    K = D.right_kernel_matrix().transpose().sparse_matrix()
    d = K.ncols()
    cols = []
    for g in sylow_gens:
        a = Bd.act(g)
        Pm = matrix(F, n, n, {(pos[tuple(a[x] for x in c)], i): 1 for i, c in enumerate(chains)},
                    sparse=True)
        cols.append((Pm - identity_matrix(F, n, sparse=True)) * K)
    JM = cols[0]
    for c in cols[1:]:
        JM = JM.augment(c)
    return d, d - JM.rank()


def section_6_7_steinberg_projective():
    cases = []
    for q in (2, 3, 4, 5, 7, 8, 9):
        cases.append(('GL_2(%d)' % q, 2, q))
    for q in (2, 3, 4):
        cases.append(('GL_3(%d)' % q, 3, q))
    cases += [('GL_4(2)', 4, 2), ('GL_4(3)', 4, 3)]
    for name, n, q in cases:
        F = GF(q, 'a')
        Bd = Building(F, n, n - 1)
        G = libgap.GL(n, q)
        p = int(F.characteristic())
        U = libgap.SylowSubgroup(G, p)
        gens = gap_mats(U.GeneratorsOfGroup(), F)
        d, top = top_module_free(Bd, F, gens)
        N = n * (n - 1) // 2
        check(d == q ** N and top == 1 and int(U.Size()) == q ** N,
              'th:steinberg-virtual-projective, Chevalley case: H~_(r-1) of the building '
              'of %s has dimension q^N = %d and is free of rank one over a Sylow '
              'p-subgroup (dim M/JM = %d), hence projective' % (name, q ** N, top))
    for (nn, q) in ((2, 2), (2, 3)):
        F = GF(q)
        G = libgap.Sp(2 * nn, q)
        J = matrix(F, [[F(x) for x in r] for r in libgap.InvariantBilinearForm(G)['matrix'].sage()])
        Bd = Building(F, 2 * nn, nn, J=J)
        U = libgap.SylowSubgroup(G, q)
        d, top = top_module_free(Bd, F, gap_mats(U.GeneratorsOfGroup(), F))
        check(d == q ** (nn * nn) and top == 1,
              'th:steinberg-virtual-projective, Chevalley case: the Steinberg module of '
              'Sp_%d(%d) (GAP\'s form) has dimension %d and is free over a Sylow '
              '%d-subgroup' % (2 * nn, q, q ** (nn * nn), q))


# --------------------------------------------------------------------------
# Alperin's example


def section_6_7_alperin():
    p, q = 3, 7
    Hq = libgap.eval('Group((1,2,3,4,5,6,7), (2,3,5)(4,7,6))')
    check(int(Hq.Size()) == p * q and not bool(Hq.IsAbelian()),
          'p. 228: H = Z/7 x| Z/3 with a non-trivial action (3 | 7 - 1)')
    G = libgap.WreathProduct(Hq, libgap.CyclicGroup(libgap.IsPermGroup, 3))
    check(int(G.Size()) == p ** (p + 1) * q ** p == 27783,
          'p. 228: |G| = p^(p+1) q^p = 27783 for G = H wr Z/3')
    base = libgap.Group([libgap.Image(libgap.Embedding(G, i), h)
                         for i in (1, 2, 3) for h in Hq.GeneratorsOfGroup()])
    t = libgap.Image(libgap.Embedding(G, 4)).GeneratorsOfGroup()[0]
    check(int(base.Size()) == (p * q) ** p and bool(libgap.IsNormal(G, base)),
          'p. 228: H^p is a normal subgroup of G')
    A = SubPoset(G, p, 'A')
    sizes = [len(A.data['keys'][i]) for i in range(A.n)]
    inbase = [bool(libgap.IsSubset(base, A.subgroup(i))) for i in range(A.n)]
    check(all(inbase[i] for i in range(A.n) if sizes[i] > p ** 2) and max(sizes) == p ** 3,
          'p. 228: every elementary abelian subgroup of G of order bigger than p^2 is '
          'contained in H^p (%d elementary abelian subgroups)' % A.n)
    by = A.X.chains()
    check(max(by) == p - 1 and all(all(inbase[x] for x in c) for c in by[p - 1]),
          'p. 228: |A_3(G)| has dimension p - 1 = 2 and all its 2-simplices lie in '
          '|A_3(H^3)|, so H~_2(A_3(G)) = H~_2(A_3(H^3)) (the kernel of d_2)')
    F = GF(p)
    mats = boundary_mats(by, F)
    r1, r2 = mats[1].rank(), mats[2].rank()
    h = (len(by[0]) - 1 - r1, len(by[1]) - r1 - r2, len(by[2]) - r2)
    check(h == (0, 2646, 216),
          'Alperin\'s example: H~_*(A_3(G); F_3) = %s' % (h,))
    chit = A.X.euler() - 1
    check(chit == h[0] - h[1] + h[2] == -2430 and chit % 81 == 0,
          'cor:ken-brown for G: chi~(A_3(G)) = -2430 = 0 mod |G|_3 = 81')
    # the corrected reading (author's list, p. 228)
    check(h[2] == (q - 1) ** p,
          'p. 228 (author\'s correction): the (p - 1)st homology has dimension '
          '(q - 1)^p = 216')
    pp = ppart(p * (q - 1) ** p, p)
    check(pp == ppart(G.Size(), p) == 81 and h[2] % pp != 0,
          'p. 228 (author\'s correction): the p-part of p (q - 1)^p is 81 = |G|_3, which '
          'does not divide 216: the module is not projective')
    # independently: fixed points of the top generator t on H~_2
    gimg = libgap.eval('function(data, t) return List(data.keys, k -> '
                       'PositionSorted(data.keys, Set(List(k, x -> x^t)))); end')(A.data, t)
    gimg = [int(i) - 1 for i in gimg]
    pos2 = {c: i for i, c in enumerate(by[2])}
    seen = set()
    orbs = []
    for c in by[2]:
        if c in seen:
            continue
        orb = [c]
        d = tuple(gimg[x] for x in c)
        while d != c:
            orb.append(d)
            d = tuple(gimg[x] for x in d)
        seen.update(orb)
        orbs.append(orb)
    # (Ker d_2)^t = Ker of d_2 on the span of the t-orbit sums of 2-chains
    S = matrix(F, len(by[2]), len(orbs), {(pos2[e], j): 1 for j, o in enumerate(orbs) for e in o},
               sparse=True)
    fixdim = len(orbs) - (mats[2] * S).rank()
    check(fixdim == 76 and fixdim != h[2] // p,
          'p. 228: the generator t of the top group Z/3 has a fixed space of dimension '
          '%d != 216/3 on H~_2, so H~_2 is not free over <t>, hence not projective' % fixdim)
    check(fixdim == (q - 1) + ((q - 1) ** p - (q - 1)) // p,
          'p. 228: the fixed points agree with the model H~_0(A_3(H))^(x)3 permuted by t '
          '(q - 1 diagonal tensors and free orbits)')
    # the printed reading
    refuted(h[2] == p ** p or (p > 3 and len(by.get(p, [])) > 0),
            'p. 228 as printed: the homology in the critical degree has dimension p^p '
            '(27 != 216; and H~_3 = 0 since the complex has dimension 2)')
    for pr in (3, 5, 7):
        W = libgap.WreathProduct(libgap.CyclicGroup(libgap.IsPermGroup, pr),
                                 libgap.CyclicGroup(libgap.IsPermGroup, pr))
        B = libgap.Group([libgap.Image(libgap.Embedding(W, i)).GeneratorsOfGroup()[0]
                          for i in range(1, pr + 1)])
        ok = True
        for c in W.ConjugacyClasses():
            x = c.Representative()
            if int(x.Order()) == pr and not bool(libgap.IsSubset(B, libgap.Group(x))):
                ok = ok and int(libgap.Centralizer(B, x).Size()) == pr
        check(ok and int(B.Size()) == pr ** pr,
              'p. 228: in the Sylow subgroup Z/%d wr Z/%d, an element of order p outside '
              'the base centralises only the diagonal (order p) of the base, so the '
              'elementary abelian subgroups not in the base have order <= p^2 and '
              '|A_p(G)| has dimension p - 1: H~_p = 0, not of dimension p^p' % (pr, pr))
    # p = 2: the restriction p > 2
    H2 = libgap.SymmetricGroup(3)
    G2 = libgap.WreathProduct(H2, libgap.CyclicGroup(libgap.IsPermGroup, 2))
    base2 = libgap.Group([libgap.Image(libgap.Embedding(G2, i), h)
                          for i in (1, 2) for h in H2.GeneratorsOfGroup()])
    A2 = SubPoset(G2, 2, 'A')
    inb = [i for i in range(A2.n) if bool(libgap.IsSubset(base2, A2.subgroup(i)))]
    hG = reduced_betti(A2.X.chains(), GF(2))
    hB = reduced_betti(A2.X.chains(inb), GF(2))
    check(hB == {1: 4} and hG == {1: 16},
          'p. 228: for p = 2, q = 3 (G = S_3 wr Z/2) H~_1(A_2(H^2)) has dimension '
          '(q - 1)^2 = 4 but H~_1(A_2(G)) has dimension 16: the restriction p > 2 is needed')
    # q = 19: the author's divisibility statement needs p^2 not dividing q - 1
    q2 = 19
    order = p ** (p + 1) * q2 ** p
    refuted(order % ppart(p * (q2 - 1) ** p, p) == 0,
            'p. 228 (author\'s wording) for q = 19: "the dimension of a projective '
            'module is divisible by the p-part of p(q - 1)^p = 3^7"; the regular module '
            'kG has dimension 3^4 19^3')
    check(((q2 - 1) ** p) % ppart(order, p) == 0 and
          (q2 - 1) + ((q2 - 1) ** p - (q2 - 1)) // p != (q2 - 1) ** p // p,
          'p. 228 for q = 19: 3^4 = |G|_3 divides 18^3, so the dimension does not decide, '
          'but the model gives t-fixed points of dimension 1956 != 5832/3: still not '
          'projective')


# ===========================================================================
# Section 6.8
# ===========================================================================


def cartan_iso(t1, t2):
    A = CartanMatrix(t1)
    B = CartanMatrix(t2)
    if A.nrows() != B.nrows():
        return False
    n = A.nrows()
    for s in itertools.permutations(range(n)):
        if all(A[i, j] == B[s[i], s[j]] for i in range(n) for j in range(n)):
            return True
    return False


def section_6_8_roots():
    expected = {}
    for l in range(1, 8):
        expected[('A', l)] = l * (l + 1)
    for l in range(2, 8):
        expected[('B', l)] = 2 * l * l
    for l in range(3, 8):
        expected[('C', l)] = 2 * l * l
    for l in range(4, 8):
        expected[('D', l)] = 2 * l * (l - 1)
    expected.update({('E', 6): 72, ('E', 7): 126, ('E', 8): 240, ('F', 4): 48, ('G', 2): 12})
    for (t, l), nroots in expected.items():
        R = RootSystem([t, l]).root_lattice()
        roots = list(R.roots())
        pos = list(R.positive_roots())
        check(len(roots) == nroots and 2 * len(pos) == nroots and len(R.simple_roots()) == l,
              'p. 229: %s_%d has %d roots, half of them positive, rank %d' % (t, l, nroots, l))
    check(cartan_iso(['B', 2], ['C', 2]) and cartan_iso(['D', 3], ['A', 3]),
          'p. 229: B_2 = C_2 and D_3 = A_3 (whence C_l, l >= 3 and D_l, l >= 4)')
    check(len(list(RootSystem(['D', 2]).root_lattice().roots())) == 4 and
          CartanMatrix(['D', 2]) == matrix(ZZ, [[2, 0], [0, 2]]),
          'p. 229: D_2 = A_1 x A_1 is decomposable')
    check(all(not cartan_iso(['B', l], ['C', l]) for l in range(3, 7)),
          'p. 229: B_l and C_l are not isomorphic for 3 <= l <= 6')
    names = [('A', l) for l in range(1, 7)] + [('B', l) for l in range(2, 7)] + \
        [('C', l) for l in range(3, 7)] + [('D', l) for l in range(4, 7)]
    ok = all(not cartan_iso(list(a), list(b)) for a, b in itertools.combinations(names, 2))
    check(ok, 'p. 229: the classical names A_l (l >= 1), B_l (l >= 2), C_l (l >= 3), D_l '
          '(l >= 4) are pairwise non-isomorphic (ranks <= 6)')
    # GL_n: eigenvalues of the torus on E_ij, roots of type A_(n-1)
    for n in (2, 3, 4):
        Rx = PolynomialRing(QQ, ['x%d' % i for i in range(1, n + 1)])
        K = FractionField(Rx)
        x = Rx.gens()
        T = matrix(K, n, n, {(i, i): x[i] for i in range(n)})
        ok = True
        roots = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                E = matrix(K, n, n, {(i, j): 1})
                ok = ok and T * E * T.inverse() == (x[i] / x[j]) * E
                r = [0] * n
                r[i], r[j] = 1, -1
                roots.append(vector(ZZ, r))
        check(ok and all(sum(r) == 0 for r in roots) and len(roots) == n * (n - 1),
              'p. 229: diag(x) acts on E_ij by x_i/x_j: the roots of GL_%d are e_i - e_j, '
              'in the hyperplane sum r_i = 0, n(n - 1) = %d of them' % (n, n * (n - 1)))
        simple = [vector(ZZ, [1 if k == i else -1 if k == i + 1 else 0 for k in range(n)])
                  for i in range(n - 1)]
        C = matrix(ZZ, n - 1, n - 1, lambda i, j: 2 * simple[i].dot_product(simple[j]) //
                   simple[j].dot_product(simple[j]))
        check(n == 1 or C == CartanMatrix(['A', n - 1]),
              'p. 229: the root system of GL_%d is of type A_%d' % (n, n - 1))
        lie_rank = n
        ss_rank = n - 1
        refuted(n - 1 == lie_rank,
                'p. 229 "The subscript refers to the (Lie) rank": GL_%d has Lie rank %d '
                '(the diagonal torus) but type A_%d' % (n, lie_rank, n - 1))
        check(n - 1 == ss_rank and n * n == lie_rank + len(roots),
              'p. 229: the subscript is the semisimple rank (the Lie rank %d of SL_%d), '
              'and dim gl_%d = Lie rank + number of roots' % (n - 1, n, n))
    for n in range(2, 6):
        check(n * (2 * n + 1) == n + len(list(RootSystem(['B', n]).root_lattice().roots())) and
              n * (2 * n + 1) == n + len(list(RootSystem(['C', n]).root_lattice().roots())),
              'p. 229: dim so_(2n+1) = dim sp_(2n) = n(2n + 1) = n + |Phi| for B_%d, C_%d' % (n, n))
    for n in range(4, 7):
        check(n * (2 * n - 1) == n + len(list(RootSystem(['D', n]).root_lattice().roots())),
              'p. 229: dim so_(2n) = n(2n - 1) = n + |Phi| for D_%d' % n)


def section_6_8_groups():
    # |G|_p = q^N
    cases = []
    for n in (2, 3, 4):
        for q in (2, 3, 4, 5):
            if n == 4 and q > 3:
                continue
            N = n * (n - 1) // 2
            cases.append(('GL_%d(%d)' % (n, q), libgap.GL(n, q), q, N))
            cases.append(('SL_%d(%d)' % (n, q), libgap.SL(n, q), q, N))
    for n in (1, 2, 3):
        for q in (2, 3, 4, 5):
            if n == 3 and q > 3:
                continue
            cases.append(('Sp_%d(%d)' % (2 * n, q), libgap.Sp(2 * n, q), q, n * n))
    for n in (1, 2, 3):
        for q in (3, 5):
            cases.append(('SO_%d(%d)' % (2 * n + 1, q), libgap.SO(2 * n + 1, q), q, n * n))
    for n in (2, 3, 4):
        for q in (2, 3):
            cases.append(('Omega+_%d(%d)' % (2 * n, q), libgap.Omega(1, 2 * n, q), q, n * (n - 1)))
    for name, G, q, N in cases:
        p = int(GF(q, 'a').characteristic())
        check(ppart(G.Size(), p) == q ** N,
              'p. 230-233: |%s|_p = q^N = %d, N the number of positive roots' % (name, q ** N))
    # parabolic subgroups: the overgroups of B = N_G(U)
    OVER = libgap.eval(r'''
    function(G, p)
      local U, B, I;
      U := SylowSubgroup(G, p);
      B := Normalizer(G, U);
      I := IntermediateSubgroups(G, B);
      return Length(I.subgroups) + 2;
    end''')
    for name, G, p, r in [('GL_2(2)', libgap.GL(2, 2), 2, 1), ('GL_2(3)', libgap.GL(2, 3), 3, 1),
                          ('GL_2(4)', libgap.GL(2, 4), 2, 1), ('GL_2(5)', libgap.GL(2, 5), 5, 1),
                          ('GL_3(2)', libgap.GL(3, 2), 2, 2), ('GL_3(3)', libgap.GL(3, 3), 3, 2),
                          ('GL_4(2)', libgap.GL(4, 2), 2, 3), ('Sp_4(2)', libgap.Sp(4, 2), 2, 2),
                          ('Sp_4(3)', libgap.Sp(4, 3), 3, 2)]:
        Gp = perm_group(G)
        check(int(OVER(Gp, p)) == 2 ** r,
              'p. 230: the subgroups containing the Borel subgroup B = N_G(U) of %s '
              'are 2^r = %d (the subsets of the %d vertices of the Dynkin diagram; the '
              'proper ones are the proper parabolics)' % (name, 2 ** r, r))
    # th:borel-tits for GL_n(q)
    for n, q in [(2, 2), (2, 3), (2, 4), (2, 5), (2, 7), (3, 2), (3, 3)]:
        F = GF(q, 'a')
        p = int(F.characteristic())
        Gm = libgap.GL(n, q)
        iso = libgap.IsomorphismPermGroup(Gm)
        Gp = libgap.Image(iso)
        S = SubPoset(Gp, p, 'S')
        V = VectorSpace(F, n)

        def flag(i):
            U = libgap.PreImage(iso, S.subgroup(i))
            gens = gap_mats(U.GeneratorsOfGroup(), F)
            W = V.subspace([])
            fl = []
            while W.dimension() < n:
                A = W.basis_matrix() if W.dimension() else matrix(F, 0, n)
                sp = p != 2
                Ann = matrix(F, A.right_kernel_matrix().transpose(), sparse=sp) if W.dimension() \
                    else identity_matrix(F, n, sparse=sp)
                M = matrix(F, n, 0, sparse=sp)
                for g in gens:
                    M = M.augment((g - identity_matrix(F, n, sparse=sp)) * Ann)
                W2 = M.left_kernel()
                fl.append(W2)
                W = W2
            dims = [w.dimension() for w in fl]
            sizeH = q ** sum(a * b for a, b in itertools.combinations(
                [dims[0]] + [dims[k] - dims[k - 1] for k in range(1, len(dims))], 2))
            return tuple(space_key(w) for w in fl[:-1]), sizeH, U
        ok = True
        rad_flags = {}
        for i in range(S.n):
            fl, sizeH, U = flag(i)
            Ui = int(U.Size())
            radical = bool(libgap.PCore(libgap.Normalizer(Gp, S.subgroup(i)), p) == S.subgroup(i))
            ok = ok and sizeH % Ui == 0 and (radical == (Ui == sizeH))
            if radical:
                rad_flags[i] = fl
        nflags = sum(len(v) for v in Building(F, n, n - 1).by.values())
        check(ok, 'th:borel-tits, proof for GL_%d(%d): U <= H(U) for all %d p-subgroups, and '
              'U = O_p N(U) iff U = H(U)' % (n, q, S.n))
        check(len(rad_flags) == nflags == len(set(rad_flags.values())),
              'th:borel-tits for GL_%d(%d): the %d radical p-subgroups correspond '
              'bijectively to the flags of proper subspaces' % (n, q, nflags))
        rl = list(rad_flags)
        ok2 = all(((i == j or S.X.lt(i, j)) == set(rad_flags[i]).issubset(set(rad_flags[j])))
                  for i in rl for j in rl)
        check(ok2, 'p. 231: U <= U\' iff the flag of U is contained in that of U\' (B_p(G) is '
              'the opposite of the poset of parabolic subgroups; GL_%d(%d))' % (n, q))


def section_6_8_buildings():
    cases = []
    for q in (2, 3, 4, 5, 7, 8, 9):
        cases.append(('GL_2(%d)' % q, GF(q, 'a'), 2, 1, None, None, q, 1))
    for q in (2, 3, 4):
        cases.append(('GL_3(%d)' % q, GF(q, 'a'), 3, 2, None, None, q, 3))
    cases += [('GL_4(2)', GF(2), 4, 3, None, None, 2, 6), ('GL_4(3)', GF(3), 4, 3, None, None, 3, 6),
              ('GL_5(2)', GF(2), 5, 4, None, None, 2, 10)]
    for nn, q in ((2, 2), (2, 3), (3, 2)):
        F = GF(q)
        J = matrix(F, 2 * nn, 2 * nn, {(2 * i, 2 * i + 1): 1 for i in range(nn)})
        J = J - J.transpose()
        cases.append(('Sp_%d(%d)' % (2 * nn, q), F, 2 * nn, nn, J, None, q, nn * nn))
    for nn, q in ((2, 2), (2, 3), (3, 2)):
        F = GF(q)
        Qf = (lambda nn: (lambda v: sum(v[2 * i] * v[2 * i + 1] for i in range(nn))))(nn)
        cases.append(('O+_%d(%d)' % (2 * nn, q), F, 2 * nn, nn, None, Qf, q, nn * (nn - 1)))
    F3 = GF(3)
    cases.append(('O_5(3)', F3, 5, 2, None,
                  lambda v: v[0] * v[1] + v[2] * v[3] + v[4] ** 2, 3, 4))
    for name, F, n, r, J, Qf, q, N in cases:
        maxdim = n - 1 if J is None and Qf is None else r
        Bd = Building(F, n, maxdim, J=J, Q=Qf)
        p = int(F.characteristic())
        Fp = GF(p)
        h = reduced_betti(Bd.by, Fp)
        top = max(Bd.by)
        check(top == r - 1, 'p. 231 (author\'s correction): the simplices of maximal '
              'dimension of the building of %s have dimension r - 1 = %d, r the semisimple '
              'rank' % (name, r - 1))
        if name.startswith('GL'):
            refuted(top == (n) - 1,
                    'p. 231 as printed, "r is the Lie rank": the Lie rank of GL_%d is %d, '
                    'but the building has dimension %d' % (n, n, top))
        maxi = set(c for c in Bd.by[top])
        pure = all(any(set(c) <= set(m) for m in maxi) for v in Bd.by.values() for c in v)
        check(pure, 'p. 231: every simplex of the building of %s lies in one of maximal '
              'dimension' % name)
        check(h == {top: q ** N},
              'th:solomon-tits: the building of %s has reduced homology over F_%d only in '
              'degree r - 1 = %d, of dimension q^N = %d' % (name, p, r - 1, q ** N))
        if sum(len(v) for v in Bd.by.values()) < 400:
            H = reduced_homology_ZZ(Bd.by)
            check(all(H.get(k, (0, [])) == ((q ** N, []) if k == top else (0, []))
                      for k in range(-1, top + 1)),
                  'th:solomon-tits over Z: H~_*(%s) = Z^%d in degree %d' % (name, q ** N, top))
    # Quillen's proof for GL_n(q)
    for n, q in ((3, 2), (3, 3), (4, 2), (4, 3)):
        F = GF(q)
        Bd = Building(F, n, n - 1)
        V = VectorSpace(F, n)
        L = V.subspace([V.gen(0)])
        Li = Bd.key[space_key(L)]
        hyper = [i for i, W in enumerate(Bd.spaces) if W.dimension() == n - 1 and
                 not L.is_subspace(W)]
        check(len(hyper) == q ** (n - 1),
              'th:solomon-tits, proof: %d = q^(n-1) hyperplanes of F_%d^%d are '
              'complementary to a line L' % (len(hyper), q, n))
        Y = [i for i in range(Bd.X.n) if i not in set(hyper)]
        check(all(v == 0 for v in reduced_betti(Bd.X.chains(Y), GF(q)).values()),
              'th:solomon-tits, proof: Y = Subsp(V) - H is acyclic (n = %d, q = %d)' % (n, q))
        ok = True
        for i in Y:
            W = Bd.spaces[i]
            S = W + L
            ok = ok and S.dimension() < n
        check(ok, 'th:solomon-tits, proof: q(U) = (U + L)/L is a proper subspace of V/L for '
              'U in Y (zero for U = L), and q/W has the maximal element W~ = the preimage')
        hl = reduced_betti(Building(F, n - 1, n - 2).by, GF(q))
        hb = reduced_betti(Bd.by, GF(q))
        check(hb.get(n - 2, 0) == q ** (n - 1) * hl.get(n - 3, 0),
              'th:solomon-tits, proof: the building is the wedge of the suspensions of the '
              'links Link(H) = Subsp(H): rank %d = q^(n-1) * %d' % (hb.get(n - 2, 0), hl.get(n - 3, 0)))
        H0 = hyper[0]
        link = set()
        for c in itertools.chain.from_iterable(Bd.by.values()):
            if H0 in c:
                continue
            if all(x == H0 or Bd.X.lt(x, H0) or Bd.X.lt(H0, x) for x in c):
                link.add(c)
        below = set(c for c in itertools.chain.from_iterable(Bd.by.values())
                    if all(Bd.X.lt(x, H0) for x in c))
        check(link == below, 'th:solomon-tits, proof: Link(H) is the complex of proper '
              'subspaces of H (n = %d, q = %d)' % (n, q))


def section_6_8_steinberg_character():
    cases = [('GL_2(%d)' % q, libgap.GL(2, q), q, 1, 1) for q in (2, 3, 4, 5, 7)]
    cases += [('GL_3(2)', libgap.GL(3, 2), 2, 2, 3), ('GL_3(3)', libgap.GL(3, 3), 3, 2, 3),
              ('Sp_4(2)', libgap.Sp(4, 2), 2, 2, 4), ('Sp_4(3)', libgap.Sp(4, 3), 3, 2, 4)]
    for name, Gm, q, r, N in cases:
        G = perm_group(Gm)
        p = int(GF(q, 'a').characteristic())
        B = SubPoset(G, p, 'B')
        vals = []
        ok = True
        for c in G.ConjugacyClasses():
            g = c.Representative()
            v = B.X.euler(B.fixed(libgap.Group(g))) - 1
            if int(g.Order()) % p == 0:
                ok = ok and v == 0
            else:
                ok = ok and abs(v) == ppart(libgap.Centralizer(G, g).Size(), p)
            vals.append(v)
        st1 = B.X.euler() - 1
        check(ok and st1 == (-1) ** (r - 1) * q ** N,
              'p. 233: St_p(%s) = (-1)^(r-1) St: its character is 0 at p-singular elements, '
              '+-|C_G(g)|_p at p-regular g (Carter, Theorem 6.4.7) and (-1)^(r-1) q^N = %d at 1'
              % (name, st1))
        if int(G.Size()) <= 200:
            S = SubPoset(G, p, 'S')
            check(all(S.X.euler(S.fixed(libgap.Group(c.Representative()))) - 1 == v
                      for c, v in zip(G.ConjugacyClasses(), vals)),
                  'p. 227: the same character from S_p(%s) (Remarks: S_p ~_G B_p)' % name)


# ===========================================================================
# Section 6.9
# ===========================================================================


def section_6_9_inversion():
    for name in named(['S_4', 'A_5', 'S_5', 'GL_2(3)', 'GL_3(2)']):
        G = GROUPS[name]
        reps = subgroup_classes(G)
        for p in (2, 3):
            for kind in ('S', 'S1', 'B'):
                P = subposet(name, p, 'B' if kind == 'B' else 'S')
                n = P.n
                if kind == 'S1':
                    # add the trivial subgroup as the element n (below everything)
                    X = Poset(n + 1, [list(P.X.up[i]) for i in range(n)] + [list(range(n))])
                    subs = [P.subgroup(i) for i in range(n)] + [libgap.TrivialSubgroup(G)]

                    def fixed(H):
                        return P.fixed(H) + [n]
                else:
                    X = P.X
                    subs = [P.subgroup(i) for i in range(n)]
                    fixed = P.fixed
                # orbit representatives of elements with stabilisers N_G(x)
                perms = P.perms()
                if kind == 'S1':
                    perms = [pm + [n] for pm in perms]
                ids, m = orbit_ids(list(range(X.n)), {i: i for i in range(X.n)}, perms,
                                   lambda pm, i: pm[i])
                orep = {}
                for i, o in enumerate(ids):
                    orep.setdefault(o, i)
                ok = True
                for H in reps:
                    lhs = X.euler(fixed(H))
                    rhs = 0
                    for x in orep.values():
                        K = libgap.Normalizer(G, subs[x])
                        for rr in libgap.RightTransversal(G, K):
                            Hc = libgap.ConjugateSubgroup(H, rr ** -1)
                            if bool(libgap.IsSubset(K, Hc)):
                                fx = set(fixed(Hc))
                                rhs -= X.euler([y for y in X.up[x] if y in fx]) - 1
                    ok = ok and lhs == rhs
                check(ok, 'prop:lefschetz-invariant-inversion: Lambda_G(X) = - sum_x '
                      'ind Lambda~_(Stab x)((x, -)) in b(G) (marks at %d classes; %s, X = %s, '
                      'p = %d)' % (len(reps), name, {'S': 'S_p', 'S1': 'S_p u {1}', 'B': 'B_p'}[kind], p))


QUOT = libgap.eval(r'''
function(G, P)
  local N, hom;
  N := Normalizer(G, P);
  hom := NaturalHomomorphismByNormalSubgroup(N, P);
  return rec(N := N, hom := hom, Q := Image(hom));
end''')


def section_6_9_upper_interval_and_steinberg_inversion():
    for name in named(['S_4', 'A_5', 'S_5', 'GL_2(3)', 'GL_3(2)', 'SL_2(5)', 'A_6']):
        G = GROUPS[name]
        reps = subgroup_classes(G)
        for p in primes_of(G):
            S = subposet(name, p, 'S')
            n = S.n
            # classes of p-subgroups including 1
            ids, m = orbit_ids(list(range(n)), {i: i for i in range(n)}, S.perms(),
                               lambda pm, i: pm[i])
            orep = {}
            for i, o in enumerate(ids):
                orep.setdefault(o, i)
            classes = [libgap.TrivialSubgroup(G)] + [S.subgroup(i) for i in orep.values()]
            data = []
            for P in classes:
                R = QUOT(G, P)
                N, hom, Q = R['N'], R['hom'], R['Q']
                SQ = SubPoset(Q, p, 'S') if int(Q.Size()) > 1 else None
                data.append((P, N, hom, Q, SQ))
                # Prop 6.9.2: the maps r and i
                ip = S.position(P) if int(P.Size()) > 1 else -1
                above = [j for j in range(n) if ip < 0 or S.X.lt(ip, j)]
                ok = True
                for j in above:
                    Qj = S.subgroup(j)
                    NQ = libgap.Normalizer(Qj, P)
                    a = S.position(NQ)
                    ok = ok and a >= 0 and a in above and (a == j or S.X.lt(a, j))
                    ok = ok and bool(libgap.IsSubset(N, NQ))
                    if bool(libgap.IsSubset(N, Qj)):
                        ok = ok and a == j     # r o i = id
                    for j2 in S.X.up[j]:
                        a2 = S.position(libgap.Normalizer(S.subgroup(j2), P))
                        ok = ok and (a2 == a or S.X.lt(a, a2))
                check(ok, 'prop:upper-interval-equivalence: r(Q) = N_Q(P) > P lies in N_G(P), '
                      'is monotone, r o i = id and i o r(Q) <= Q (%s, p = %d, |P| = %d)'
                      % (name, p, int(P.Size())))
                # marks in b(N_G(P)): (P, -) against S_p(N_G(P)/P) in the quotient group
                okm = True
                Nreps = subgroup_classes(N) if int(N.Size()) <= 1000 else []
                for K in Nreps:
                    fx = set(S.fixed(K))
                    left = S.X.euler([j for j in above if j in fx]) - 1
                    if SQ is None:
                        right = -1
                    else:
                        right = SQ.X.euler(SQ.fixed(libgap.Image(hom, K))) - 1
                    okm = okm and left == right
                check(okm, 'prop:upper-interval-equivalence: Lambda~((P, -)) = Lambda~(S_p(N_G(P)/P)) '
                      'in b(N_G(P)) (marks at %d classes of subgroups of N_G(P); %s, p = %d, '
                      '|P| = %d)' % (len(Nreps), name, p, int(P.Size())))
                # Remarks (i)
                if int(P.Size()) > 1 and not bool(libgap.PCore(N, p) == P):
                    check(SQ is not None and int(libgap.PCore(Q, p).Size()) > 1 and
                          all(SQ.X.euler(SQ.fixed(libgap.Image(hom, K))) == 1 for K in Nreps),
                          'th:steinberg-inversion, Remarks (i): P != O_p N_G(P) => '
                          'S_p(N_G(P)/P) is contractible (O_p != 1) and its Lambda~ vanishes '
                          '(%s, p = %d, |P| = %d)' % (name, p, int(P.Size())))
            # Theorem 6.9.3 in b(G)
            ok = True
            for H in reps:
                tot = 0
                for P, N, hom, Q, SQ in data:
                    for rr in libgap.RightTransversal(G, N):
                        Hc = libgap.ConjugateSubgroup(H, rr ** -1)
                        if bool(libgap.IsSubset(N, Hc)):
                            tot += (SQ.X.euler(SQ.fixed(libgap.Image(hom, Hc))) - 1) if SQ else -1
                ok = ok and tot == -1
            check(ok, 'th:steinberg-inversion: 1 = - sum_P ind_(N_G(P), G) '
                  'Lambda~_(N_G(P))(S_p(N_G(P)/P)) in b(G) (marks at %d classes; %s, p = %d, '
                  '%d classes of p-subgroups)' % (len(reps), name, p, len(classes)))
    # the cone form for SMALL
    npairs = 0
    for name in small_range():
        G = GROUPS[name]
        for p in primes_of(G):
            S = subposet(name, p, 'S')
            n = S.n
            X = Poset(n + 1, [list(S.X.up[i]) for i in range(n)] + [list(range(n))])
            ok = True
            for H in subgroup_classes(G):
                Y = set(S.fixed(H) + [n])
                ok = ok and sum(X.euler([y for y in X.up[x] if y in Y]) - 1 for x in Y) == -1
            check(ok, 'th:steinberg-inversion at the level of marks: sum over the p-subgroups '
                  'P normalised by H of chi~((P, -)^H) = -1 for all H (%s, p = %d)' % (name, p))
            npairs += 1
    check(npairs == 474, 'SMALL: %d pairs (G, p)' % npairs)


LEN = libgap.eval(r'''
rec(
  l := function(G, p)
    return Number(ConjugacyClasses(G), c -> Order(Representative(c)) mod p <> 0);
  end,
  f0 := function(G, p)
    local pp;
    pp := 1;
    while Size(G) mod (pp * p) = 0 do pp := pp * p; od;
    return Number(Irr(CharacterTable(G)), chi -> (chi[1] mod pp) = 0);
  end,
  kOp := function(G, p)
    return NrConjugacyClasses(G / PCore(G, p));
  end,
  k := function(G, p)
    return NrConjugacyClasses(G);
  end
)''')


def section_6_9_length_functions():
    names = small_range() + named(['S_5', 'A_6', 'GL_3(2)', 'GL_2(3)', 'SL_2(5)', 'PSL_2(8)',
                                   'PSL_2(11)', 'A_7', 'M_11'])
    STAB = libgap.eval(r'''
    function(G, data, chains)
      local out, c, K, i;
      out := [];
      for c in chains do
        K := G;
        for i in c do K := Intersection(K, Normalizer(G, data.subs[i])); od;
        Add(out, K);
      od;
      return out;
    end''')
    memo = {}

    def id_of(Q):
        if int(Q.Size()) in (512, 768, 1024, 1536) or int(Q.Size()) > 2000:
            return None
        return tuple(int(x) for x in libgap.IdGroup(Q))

    def pclass_reps(G, p):
        """Classes of p-subgroups of G (including 1), as GAP subgroups."""
        reps = []
        P = G.SylowSubgroup(p)
        for c in P.ConjugacyClassesSubgroups():
            R = c.Representative()
            if all(int(R.Size()) != int(T.Size()) or not bool(libgap.IsConjugate(G, R, T))
                   for T in reps):
                reps.append(R)
        return reps

    def beta(alpha, G, p):
        """beta defined by (i): beta(G) = alpha(G) - sum_(P != 1) beta(N_G(P)/P)."""
        key = (alpha, id_of(G), p)
        if key[1] is not None and key in memo:
            return memo[key]
        val = int(LEN[alpha](G, p))
        for P in pclass_reps(G, p):
            if int(P.Size()) == 1:
                continue
            Q = libgap.FactorGroup(libgap.Normalizer(G, P), P)
            val -= beta(alpha, Q, p)
        if key[1] is not None:
            memo[key] = val
        return val

    def alpha_lambda(alpha, name, p, kind):
        """alpha(Lambda~_G(X)) = sum over chain orbits (-1)^dim alpha(Stab) - alpha(G)."""
        G = GROUPS[name]
        P = subposet(name, p, kind)
        reps = chain_orbit_reps(P)
        stabs = STAB(G, P.data, [[x + 1 for x in c] for c in reps])
        tot = sum((-1) ** (len(c) - 1) * int(LEN[alpha](K, p)) for c, K in zip(reps, stabs))
        return tot - int(LEN[alpha](G, p))
    nAl = 0
    failed_k = []
    for name in names:
        G = GROUPS[name]
        for p in primes_of(G):
            l = int(LEN['l'](G, p))
            check(l == int(LEN['l'](libgap.FactorGroup(G, libgap.PCore(G, p)), p)),
                  'p. 235: l(G) = l(G/O_p(G)) (%s, p = %d)' % (name, p))
            # Alperin's conjecture
            tot = 0
            for P in pclass_reps(G, p):
                tot += int(LEN['f0'](libgap.FactorGroup(libgap.Normalizer(G, P), P), p))
            check(l == tot, 'Alperin\'s conjecture p. 235: l(G) = %d = sum_P f_0(N_G(P)/P) '
                  '(%s, p = %d)' % (l, name, p))
            nAl += 1
            if int(G.Size()) > 720:
                continue
            f0 = int(LEN['f0'](G, p))
            kinds = 'SAB' if int(G.Size()) <= 360 else 'B'
            for kind in kinds:
                check(f0 == -alpha_lambda('l', name, p, kind),
                      'p. 235, Robinson\'s reformulation: f_0(G) = %d = -l(Lambda~_G(%s_p(G))) '
                      '(%s, p = %d)' % (f0, kind, name, p))
            for alpha in ('l', 'kOp'):
                b = beta(alpha, G, p)
                check(b == -alpha_lambda(alpha, name, p, 'B'),
                      'prop:length-function-equivalence, (i) => (ii) for alpha = %s: beta(G) = '
                      '%d = -alpha(Lambda~(S_p(G))) (%s, p = %d)' % (alpha, b, name, p))
                if alpha == 'l':
                    check(b == f0, 'prop:length-function-equivalence with alpha = l: beta = f_0 '
                          '(%s, p = %d)' % (name, p))
            if beta('k', G, p) != -alpha_lambda('k', name, p, 'B'):
                failed_k.append((name, p))
    check(nAl >= 440, 'Alperin\'s conjecture: %d pairs (G, p)' % nAl)
    check(('SmallGroup(6, 1)', 3) in failed_k,
          'prop:length-function-equivalence: the hypothesis alpha(G) = alpha(G/O_p(G)) is '
          'needed: for alpha = k (number of classes) (ii) fails for S_3, p = 3 (%d pairs fail)'
          % len(failed_k))


def main():
    sections = [section_6_7_virtual_projective, section_6_7_steinberg_projective,
                section_6_7_alperin, section_6_8_roots, section_6_8_groups,
                section_6_8_buildings, section_6_8_steinberg_character,
                section_6_9_inversion,
                section_6_9_upper_interval_and_steinberg_inversion,
                section_6_9_length_functions]
    only = sys.argv[1:]
    for f in sections:
        if not only or f.__name__ in only:
            f()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
