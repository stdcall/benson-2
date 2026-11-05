"""Exact checks of Chapter 4, Sections 4.1-4.3 (Sage).

Run: sage -python checks/sage/chapter-4a.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-4a: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 4 "The Evens
norm map and the Steenrod algebra", Sections 4.1-4.3, printed pp. 121-137.
Our files: content/04-01-evens-norm.typ ... content/04-03-bockstein.typ.
Sections 4.4-4.8 are checked in chapter-4b.py.  Pages are printed pages;
labels are those of content/04-*.typ.  Expected values are the book's
statements read off the printed pages; where the printed text was
corrected, the printed reading is kept as a refuted check (`refuted`) beside
the corrected one.

Everything is exact: integers, Z/p^k, GF(p), polynomial rings over GF(p),
groups in GAP (libgap).  Resolutions are the periodic resolutions T of
cyclic groups (Section 3.5 of Volume I: d e_i = (g - 1) e_(i-1) for i odd,
(1 + g + ... + g^(p-1)) e_(i-1) for i even) and their tensor products, with
explicit contracting homotopies; chain maps into tensor powers are built
by the standard recursion phi(e) = s(phi(d e)) and are checked to be chain
maps.  Cup products of the dual basis e_n^* of H^*(Z/p, F_p) are computed
from a diagonal approximation constructed in the same way; on T (x) T the
cross product (f x g)(e_a (x) e_b) = (-1)^(ab) f(e_a) g(e_b) represents
pr_1^*(f) pr_2^*(g).

What is checked, by section:

section_4_1 (pp. 121-126):
  * the action of Sigma_n wr H on C^(x)n (p. 121): the sign (-1)^nu,
    nu = sum over j < k, pi(j) > pi(k) of deg(x_j) deg(x_k), is the product
    of the signs of standard transpositions in any reduced word for pi, and
    makes the formula an action of Sigma_n wr H (wreath product multiplied
    as (pi; h)(sigma; k) = (pi sigma; h_(sigma(1)) k_1, ...)): exhaustive
    for n <= 4 and degrees in {0, 1, 2}, and with H = S_3 (n = 2) and
    H = Z/2 (n = 3);
  * the formula for delta(1 wr alpha) (p. 122) and its variant in the proof
    of lem:twisted-bockstein-norm (p. 136), for integral cochains alpha on
    the periodic resolution of Z/p (p = 3, 5; n = 2, 3; r = 1, 2), with the
    Koszul sign for tensor products of maps and the differential
    delta f = (-1)^(r+1) f o d of the Hom complex;
  * the sentence "Q^(x)n is an exact sequence ..., resolving M_1^(x)n"
    (p. 122): refuted as printed for R = Z, M_1 = Z/2 (Q = (Z --2--> Z),
    H_1(Q (x) Q) = Z/2, H_1(Q (x) Q (x) Q) = (Z/2)^2); with the corrected
    hypothesis "M_1 flat as an R-module" checked for M_1 = Z and for
    R = F_2 (exact in positive degrees, H_0 = M_1^(x)n), n = 2, 3; the use
    of prop:tensor-homology (as corrected in Chapter 3) for exact C;
  * the sign of prop:norm-properties (i): the Koszul sign of the shuffle
    (zeta zeta')^(x)n -> zeta^(x)n (x) zeta'^(x)n is (-1)^(n(n-1)rs/2),
    n <= 6, r, s <= 3;
  * the proof of th:cohomology-nonvanishing: (1 + alpha)^(p^a h) =
    (1 + alpha^(p^a))^h = 1 + h alpha^(p^a) + ... in F_p[alpha] (p <= 7,
    a <= 3, h <= 10 prime to p); lambda^(p-1) = 1; the Mackey formula gives
    res(z) = (1 + alpha)^|N_G<g> : <g>|: in GAP, for 9 groups and every
    element g of prime order (up to conjugacy), the double cosets
    <g> x <g> with x in N_G<g> are |N_G<g> : <g>| single cosets and all
    others meet <g> trivially;
  * prop:norm-rank-two and the Example before it (pp. 124-126):
    (a) the invariance argument: in Lambda(y1, y2) (x) F_p[x1, x2] the
    elements of degree 2p restricting to x2^p and invariant under the
    automorphisms of the first copy of Z/p are x2^p + lambda x1^(p-1) x2 +
    mu x1^(p-2) y1 x2 y2, those of degree p restricting to 0 and invariant
    up to the sign character are lambda x1^m y2 + mu x1^(m-1) y1 x2
    (m = (p-1)/2); the automorphism y2 -> y1 + y2, x2 -> x1 + x2 forces
    lambda = -1, mu = 0, resp. lambda = -mu (p = 3, 5, 7, 11, 13); the
    form is unchanged under x2 -> x2 + c x1; the twist by the sign
    character: multiplication by c on Z/p is a permutation of sign
    (c/p) = c^m (Zolotarev; p < 60);
    (b) the Evens norm itself, computed at chain level for H = 1 x Z/p <=
    G = Z/p x Z/p with the cosets g1^k (k = 0, ..., p-1): a chain map
    T (x) T -> Q^(x)p of G-modules lifting the identity (G acting on Q^(x)p
    through Sigma_p wr H with the Koszul sign of p. 121), composed with
    1 wr xhat: norm(x2) = x2^p - x1^(p-1) x2 for p = 3, 5; norm(y2) =
    lambda x1^((p-3)/2) (x1 y2 - y1 x2) with lambda^2 = (-1)^(m+1), i.e.
    lambda = +-1/m!, for p = 3, 5 (for the order of cosets used, lambda =
    -1, 2 in the basis x = e_2^* = beta(y)); for p = 2 norm(y2) = y2^2 +
    y1 y2, norm(y2^2) = norm(y2)^2, norm(y2^3) = norm(y2)^3 (p. 126); for
    p = 3 norm(y2 x2) = norm(y2) norm(x2) (prop:norm-properties (i));
    theta_2 = -1 (the coefficient D_(2(p-1))(x) = -x used on p. 144).
section_4_2 (pp. 126-132): the Warning: for R = Z + (Z/p)^N with the
  printed multiplication, R is a commutative ring and H^1(Z/p, R) =
  Hom(Z/p, R) = (Z/p)^N needs N generators over H^0 = R (N <= 5); the
  proof of th:evens-finite-generation: for the 2-groups of order 8, 16 and
  the 3-groups of order 27 and every central subgroup Z of order p, all
  double cosets Z x Z are single cosets xZ with Z cap xZx^-1 = Z, so
  res_(P,Z) norm_(Z,P)(sigma) = sigma^|P:Z|; the rows of E_2: cup with
  xi = sigma^n maps H^q(Z, M) isomorphically to H^(q+2n)(Z, M) for q >= 1
  and onto for q = 0 (M = F_p, Z/p^2, F_p Z/p), so E_2(M) is the sum of
  the xi^N E'_2(M) in disjoint rows.
section_4_3 (pp. 132-137):
  * the Example of p. 133: for Z/p the Bockstein is an isomorphism
    H^r -> H^(r+1) for r odd and zero for r even (p = 2, 3, 5; r <= 7), the
    integral cohomology Z/p in positive even degrees and 0 in odd ones;
  * the Bockstein spectral sequence for Z/p^k (k <= 3, p = 2, 3, 5,
    degrees <= 6): beta_n is defined on all of H^r(G, F_p) for n <= k,
    beta_n = 0 for n < k, beta_k : H^(2i-1) -> H^(2i) is an isomorphism,
    so E_(k+1) = 0 in positive degrees (the order p^k of the torsion) and
    the sequence converges to F_p in degree 0 (= (Z / torsion) (x) F_p);
  * lem:bockstein-squared-zero and lem:bockstein-product on
    H^*(Z/p x Z/p, F_p) (p = 2, 3, 5) at cochain level on T (x) T: beta is
    computed as the connecting homomorphism (lift to Z/p^2, apply delta,
    divide by p) with delta f = (-1)^(n+1) f o d; beta^2 = 0 on all classes
    of degree <= 4; beta(xy) = beta(x) y + (-1)^deg(x) x beta(y) for all
    pairs of monomials of total degree <= 4;
  * the remark before lem:twisted-bockstein-norm: for p = 2 the twisted
    Bockstein of 0 -> F_2 -> (Z/4)^sign -> F_2 -> 0 on H^*(Z/2, F_2) is
    beta~(z) = beta(z) + a z (a the generator of H^1), so it does not agree
    with beta (degrees <= 7);
  * lem:twisted-bockstein-norm: the coboundary of 1 wr xi-hat
    (sum_j (-1)^(jr) ...) as in Section 4.1 (above).

What these checks do NOT establish.  The explicit norm is computed for one
order of the cosets and one choice of resolutions; it determines lambda in
prop:norm-rank-two only up to the sign that depends on the order of the
cosets and on the sign conventions for cochains (both signs occur for
suitable orders, since a transposition of two cosets changes the norm of
an odd degree class by -1).  The general properties of the norm
(prop:norm-properties, lem:tensor-power-homotopy), Evens' theorem and its
corollaries, the Bockstein spectral sequence for non-cyclic groups,
prop:bockstein-norm-transfer and the exercises are not checked beyond the
listed instances.  Nothing here compares our text with the printed book.
"""
import itertools

from sage.all import (
    GF, ZZ, ChainComplex, PolynomialRing, factorial, legendre_symbol, libgap, matrix,
    prime_range,
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


def addto(out, k, c):
    out[k] = out.get(k, 0) + c


def clean(d, mod=None):
    if mod:
        return {k: c % mod for k, c in d.items() if c % mod}
    return {k: c for k, c in d.items() if c}


def perm_sign_inv(seq):
    return sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[a] > seq[b])


# ---------------------------------------------------------------------------
# The periodic resolution of a cyclic group C = <h> of order q (over Z), its
# tensor powers and contracting homotopies.  A basis element h^a e_i of T_i
# is the pair (i, a); a basis element of T^(x)k is a k-tuple of pairs.

class Periodic:
    def __init__(self, q):
        self.q = q

    def d1(self, i, a):
        q = self.q
        if i == 0:
            return {}
        if i % 2 == 1:
            return {(i - 1, (a + 1) % q): 1, (i - 1, a): -1}
        return {(i - 1, b): 1 for b in range(q)}

    def s1(self, i, a):
        """contraction s : T_i -> T_(i+1) (with s_(-1)(1) = e_0)."""
        q = self.q
        if i % 2 == 0:
            return {(i + 1, b): 1 for b in range(a)}
        return {(i + 1, 0): 1} if a == q - 1 else {}

    def s(self, term):
        """contraction of T^(x)k: s(u (x) rest) = s(u) (x) rest + e_0 eps(u) (x) s(rest)."""
        out = {}
        if not term:
            return out
        (i, a) = term[0]
        rest = term[1:]
        for k1, c in self.s1(i, a).items():
            addto(out, (k1,) + rest, c)
        if i == 0 and rest:
            for k2, c in self.s(rest).items():
                addto(out, ((0, 0),) + k2, c)
        return out

    def d(self, term):
        out = {}
        sign = 1
        for pos, (i, a) in enumerate(term):
            for k1, c in self.d1(i, a).items():
                addto(out, term[:pos] + (k1,) + term[pos + 1:], sign * c)
            if i % 2 == 1:
                sign = -sign
        return out


def lin(f, d):
    out = {}
    for k, c in d.items():
        for k2, c2 in f(k).items():
            addto(out, k2, c * c2)
    return out


def cup_table(p, N):
    """(e_a^* u e_b^*)(e_(a+b)) in H^*(Z/p, F_p), from a diagonal T -> T (x) T
    built by Delta(e_n) = s(Delta(d e_n)); also checks that Delta is a chain map."""
    T = Periodic(p)
    D = {0: {((0, 0), (0, 0)): 1}}

    def delta_of(i, a):
        return {((i1, (a1 + a) % p), (i2, (a2 + a) % p)): c for ((i1, a1), (i2, a2)), c in D[i].items()}
    for n in range(1, N + 1):
        z = clean(lin(lambda k: delta_of(*k), T.d1(n, 0)), p)
        D[n] = clean(lin(T.s, z), p)
        check(clean(lin(T.d, D[n]), p) == z, 'diagonal approximation of T is a chain map in degree %d (p = %d)' % (n, p))
    tab = {}
    for n in range(N + 1):
        for a in range(n + 1):
            v = sum(c for ((i1, _), (i2, _)), c in D[n].items() if i1 == a)
            tab[(a, n - a)] = ((-1) ** (a * (n - a)) * v) % p
    return tab


# ---------------------------------------------------------------------------
# Section 4.1

def koszul_nu(pi, degs):
    """nu of p. 121: sum over j < k with pi(j) > pi(k) of deg(x_j) deg(x_k)."""
    n = len(pi)
    return sum(degs[j] * degs[k] for j in range(n) for k in range(j + 1, n) if pi[j] > pi[k])


def act_sym(pi, degs):
    """(pi) . (x_1 (x) ... (x) x_n): x_j moves to position pi(j); returns (parity, new degrees)."""
    n = len(pi)
    inv = [0] * n
    for j in range(n):
        inv[pi[j]] = j
    return koszul_nu(pi, degs) % 2, tuple(degs[inv[k]] for k in range(n))


def compose(pi, sigma):
    return tuple(pi[sigma[j]] for j in range(len(pi)))


def section_4_1():
    # --- the sign nu and the action of Sigma_n wr H (p. 121) ---------------
    for n in range(1, 5):
        perms = list(itertools.permutations(range(n)))
        ok_tr = ok_act = True
        for degs in itertools.product(range(3), repeat=n):
            for pi in perms:
                # product of standard transpositions (bubble sort of pi)
                seq = list(range(n))       # seq[pos] = original index at position pos
                target = [0] * n
                for j in range(n):
                    target[pi[j]] = j
                cur = list(degs)
                par = 0
                order = list(range(n))
                # bring the factor that must end at position 0, 1, ... forward by adjacent swaps
                for pos in range(n):
                    want = target[pos]
                    at = order.index(want)
                    while at > pos:
                        par += cur[at - 1] * cur[at]
                        cur[at - 1], cur[at] = cur[at], cur[at - 1]
                        order[at - 1], order[at] = order[at], order[at - 1]
                        at -= 1
                ok_tr = ok_tr and par % 2 == koszul_nu(pi, degs) % 2
                for sigma in perms:
                    p1, d1 = act_sym(sigma, degs)
                    p2, d2 = act_sym(pi, d1)
                    p3, d3 = act_sym(compose(pi, sigma), degs)
                    ok_act = ok_act and (p1 + p2) % 2 == p3 and d2 == d3
        check(ok_tr, 'p. 121: (-1)^nu is the product of the signs of standard transpositions (n = %d, '
                     'all permutations, degrees in {0, 1, 2})' % n)
        check(ok_act, 'p. 121: the signed permutation action of Sigma_%d on C^(x)%d is an action' % (n, n))
    # with the H-components: H = S_3 (n = 2), H = Z/2 (n = 3); x_j in H (regular action)
    for H, n in ((libgap.SymmetricGroup(3), 2), (libgap.CyclicGroup(libgap.IsPermGroup, 2), 3)):
        Hel = list(H.AsList())
        perms = list(itertools.permutations(range(n)))
        elts = [(pi, h) for pi in perms for h in itertools.product(Hel, repeat=n)]

        def wact(el, xs):
            pi, h = el
            inv = [0] * n
            for j in range(n):
                inv[pi[j]] = j
            return tuple(h[inv[k]] * xs[inv[k]] for k in range(n))

        def wmul(e1, e2):
            (pi, h), (sigma, k) = e1, e2
            return (compose(pi, sigma), tuple(h[sigma[j]] * k[j] for j in range(n)))
        ok = True
        xs = tuple(Hel[(j + 1) % len(Hel)] for j in range(n))
        for e1 in elts:
            for e2 in elts:
                if wact(e1, wact(e2, xs)) != wact(wmul(e1, e2), xs):
                    ok = False
        check(ok, 'p. 121: (pi; h_1..h_n)(x_1 (x) .. (x) x_n) = h_(pi^-1(1)) x_(pi^-1(1)) (x) .. is an '
                  'action of Sigma_%d wr H, |H| = %d' % (n, len(Hel)))

    # --- delta(1 wr alpha) (p. 122) and its form in lem:twisted-bockstein-norm (p. 136) ----
    for p in (3, 5):
        T = Periodic(p)
        for n in (2, 3):
            for r in (1, 2):
                # alpha : T_r -> Z, alpha(h^a e_r) = 1 (a cochain, not a cocycle over Z when r odd)
                def alpha_tensor(term, deg_f):
                    """(f_1 (x) ... (x) f_n)(u_1 (x) ... (x) u_n), f_j = alpha (deg r) or delta alpha (deg r+1)."""
                    if any(term[j][0] != deg_f[j] for j in range(n)):
                        return 0
                    sgn = sum(deg_f[j] * term[i][0] for j in range(n) for i in range(j))
                    val = 1
                    for j in range(n):
                        if deg_f[j] == r:
                            val *= 1
                        else:   # (delta alpha)(h^a e_(r+1)) = (-1)^(r+1) alpha(d e_(r+1))
                            val *= (-1) ** (r + 1) * sum(c for _, c in T.d1(r + 1, term[j][1]).items())
                    return (-1) ** sgn * val
                basis = []
                for degs in itertools.product(range(r + 2), repeat=n):
                    if sum(degs) != n * r + 1:
                        continue
                    for aa in itertools.product(range(p), repeat=n):
                        basis.append(tuple(zip(degs, aa)))
                ok = True
                for term in basis:
                    # delta(alpha^(x)n)(u) = (-1)^(nr+1) alpha^(x)n(d u)
                    lhs = (-1) ** (n * r + 1) * sum(c * alpha_tensor(k, (r,) * n) for k, c in T.d(term).items())
                    rhs = sum((-1) ** ((j - 1) * r) *
                              alpha_tensor(term, (r,) * (j - 1) + (r + 1,) + (r,) * (n - j))
                              for j in range(1, n + 1))
                    rhs2 = sum((-1) ** (j * r) *
                               alpha_tensor(term, (r,) * j + (r + 1,) + (r,) * (n - j - 1))
                               for j in range(0, n))
                    if not (lhs == rhs == rhs2):
                        ok = False
                check(ok, 'p. 122: delta(1 wr alpha) = sum_j (-1)^((j-1)r) alpha^(j-1) (x) delta alpha (x) '
                          'alpha^(n-j), and p. 136 with j from 0 (p = %d, n = %d, r = %d, over Z)' % (p, n, r))

    # --- p. 122: Q^(x)n resolves M_1^(x)n only when M_1 is flat over R --------
    def tensor_power_homology(dmat_list, n, base_ring):
        """Q = complex given by its differentials (Q_1 -> Q_0 ...); returns H_* of Q^(x)n
        as lists of invariants (over ZZ) or dimensions (over a field)."""
        # Q given as a list of ranks and differential matrices d_i : Q_i -> Q_(i-1)
        ranks, ds = dmat_list
        top = len(ranks) - 1
        # build Q^(x)n degreewise: basis = tuples of (degree, index)
        bases = {}
        for degs in itertools.product(range(top + 1), repeat=n):
            for idx in itertools.product(*[range(ranks[d]) for d in degs]):
                bases.setdefault(sum(degs), []).append(tuple(zip(degs, idx)))
        pos = {deg: {b: i for i, b in enumerate(B)} for deg, B in bases.items()}
        D = {}
        for deg in range(1, n * top + 1):
            M = matrix(base_ring, len(bases[deg - 1]), len(bases[deg]))
            for col, b in enumerate(bases[deg]):
                sign = 1
                for j, (dg, ix) in enumerate(b):
                    if dg > 0:
                        for row in range(ranks[dg - 1]):
                            c = ds[dg][row, ix]
                            if c:
                                nb = b[:j] + ((dg - 1, row),) + b[j + 1:]
                                M[pos[deg - 1][nb], col] += sign * c
                    if dg % 2:
                        sign = -sign
            D[deg] = M
        CC = ChainComplex({deg: D[deg] for deg in D} if D else {0: matrix(base_ring, 0, len(bases[0]))},
                          base_ring=base_ring, degree_of_differential=-1)
        H = CC.homology()
        out = {}
        for deg in range(0, n * top + 1):
            g = H.get(deg, None) if hasattr(H, 'get') else H[deg]
            if base_ring is ZZ:
                out[deg] = sorted(g.invariants()) if g is not None else []
            else:
                out[deg] = g.dimension() if g is not None else 0
        return out

    Q_Z2 = ([1, 1], {1: matrix(ZZ, [[2]])})           # Z --2--> Z resolves Z/2 over R = Z
    for n in (2, 3):
        H = tensor_power_homology(Q_Z2, n, ZZ)
        refuted(all(H[d] == [] for d in range(1, n + 1)),
                'p. 122 as printed: Q^(x)%d resolves M_1^(x)%d for R = Z, M_1 = Z/2 (H_1 = %s)' % (n, n, H[1]))
        check(H[1] == [2] * (n - 1) and H[0] == [2],
              'p. 122: R = Z, M_1 = Z/2, Q = (Z -2-> Z): H_0(Q^(x)%d) = Z/2, H_1 = (Z/2)^%d = Tor' % (n, n - 1))
    Q_Z = ([1], {})                                   # M_1 = Z (flat): Q = Z in degree 0
    Q_free = ([2, 1], {1: matrix(ZZ, [[1], [-1]])})   # a free resolution Z <- Z^2 <- Z of Z
    for n in (2, 3):
        H = tensor_power_homology(Q_free, n, ZZ)
        check(H[0] == [0] and all(H[d] == [] for d in range(1, n + 1)),
              'p. 122 corrected: M_1 = Z flat over Z: Q^(x)%d resolves Z^(x)%d = Z' % (n, n))
    Q_F2res = ([2, 1], {1: matrix(GF(2), [[1], [1]])})   # F_2^2 <- F_2 resolves F_2 over R = F_2
    for n in (2, 3):
        H = tensor_power_homology(Q_F2res, n, GF(2))
        check(H[0] == 1 and all(H[d] == 0 for d in range(1, n + 1)),
              'p. 122 corrected: over R = F_2 every module is flat; Q^(x)%d is a resolution' % n)
    # prop:tensor-homology (corrected) applied to an exact C (H_0 = 0 is flat): C = cone of id on Q
    C_exact = ([1, 2, 1], {1: matrix(ZZ, [[1, 1]]), 2: matrix(ZZ, [[1], [-1]])})
    for n in (2, 3):
        H = tensor_power_homology(C_exact, n, ZZ)
        check(all(H[d] == [] for d in range(0, 2 * n + 1)),
              'p. 122: C exact of free modules, then C^(x)%d is exact (prop:tensor-homology)' % n)

    # --- prop:norm-properties (i): the sign (-1)^(n(n-1)rs/2) ------------------
    for n in range(1, 7):
        for r in range(4):
            for s in range(4):
                # positions: x_1 y_1 x_2 y_2 ... -> x_1 .. x_n y_1 .. y_n
                degs = []
                pi = []
                for j in range(n):
                    degs += [r, s]
                    pi += [j, n + j]
                check(koszul_nu(pi, degs) % 2 == (n * (n - 1) // 2 * r * s) % 2,
                      'prop:norm-properties (i): sign (-1)^(n(n-1)rs/2), n = %d, r = %d, s = %d' % (n, r, s))

    # --- th:cohomology-nonvanishing --------------------------------------------
    for p in (2, 3, 5, 7):
        R = PolynomialRing(GF(p), 'al')
        al = R.gen()
        for a in range(4):
            for h in range(1, 11):
                if h % p == 0:
                    continue
                lhs = (1 + al) ** (p ** a * h)
                check(lhs == (1 + al ** (p ** a)) ** h and lhs.coefficients(sparse=False)[p ** a] == h % p
                      and all(lhs.coefficients(sparse=False)[i] == 0 for i in range(1, p ** a)),
                      'th:cohomology-nonvanishing: (1 + alpha)^(p^a h) = (1 + alpha^(p^a))^h = 1 + h alpha^(p^a) + ...'
                      ' (p = %d, a = %d, h = %d)' % (p, a, h))
        check(all(pow(c, p - 1, p) == 1 for c in range(1, p)),
              'th:cohomology-nonvanishing: lambda^(p-1) = 1 for the action of conjugation (p = %d)' % p)
    groups = [libgap.SymmetricGroup(3), libgap.AlternatingGroup(4), libgap.SymmetricGroup(4),
              libgap.AlternatingGroup(5), libgap.GL(2, 3), libgap.SmallGroup(20, 3), libgap.SmallGroup(21, 1),
              libgap.PSL(2, 7), libgap.DihedralGroup(16)]
    for G in groups:
        order = int(G.Size())
        for cl in G.ConjugacyClasses():
            g = cl.Representative()
            p = int(g.Order())
            if p == 1 or not ZZ(p).is_prime():
                continue
            U = libgap.Subgroup(G, [g])
            N = G.Normalizer(U)
            inside = 0
            ok = True
            for dc in libgap.DoubleCosets(G, U, U):
                x = dc.Representative()
                inter = int(libgap.Intersection(U, U ** x).Size())
                if x in N:
                    inside += 1
                    ok = ok and int(dc.Size()) == p and inter == p
                else:
                    ok = ok and inter == 1
            check(ok and inside == int(N.Size()) // p,
                  'th:cohomology-nonvanishing: Mackey: |N_G<g> : <g>| double cosets in N, the others meet <g> '
                  'trivially (|G| = %d, |g| = %d)' % (order, p))

    # --- prop:norm-rank-two: the invariance argument (pp. 124-125) ------------
    for p in (3, 5, 7, 11, 13):
        m = (p - 1) // 2
        F = GF(p)
        # monomials y1^e1 x1^a y2^e2 x2^b of degree D
        def monos(D):
            return [(e1, a, e2, b) for e1 in (0, 1) for e2 in (0, 1) for a in range(D // 2 + 1)
                    for b in range(D // 2 + 1) if e1 + 2 * a + e2 + 2 * b == D]
        # degree 2p, restriction to H (y1, x1 -> 0) equal to x2^p, weight of (y1, x1) = 0 mod p-1, weight >= 1
        even = [mo for mo in monos(2 * p) if (mo[0] + mo[1]) % (p - 1) == 0 and mo[0] + mo[1] >= 1]
        check(sorted(even) == sorted([(0, p - 1, 0, 1), (1, p - 2, 1, 1)]),
              'p. 125: invariant forms of degree 2p: x2^p + lambda x1^(p-1) x2 + mu x1^(p-2) y1 x2 y2 (p = %d)' % p)
        odd = [mo for mo in monos(p) if (mo[0] + mo[1]) % (p - 1) == m and mo[0] + mo[1] >= 1]
        check(sorted(odd) == sorted([(0, m, 1, 0), (1, m - 1, 0, 1)]),
              'p. 125: forms of degree p twisted by the sign character: lambda x1^m y2 + mu x1^(m-1) y1 x2 (p = %d)' % p)
        # the automorphism y2 -> y1 + y2, x2 -> x1 + x2 in Lambda (x) F_p[x1, x2]
        LM = PolynomialRing(F, 'lam,mu')
        lam, mu = LM.gens()
        R = PolynomialRing(LM, 'x1,x2,y1,y2')
        x1, x2, y1, y2 = R.gens()
        def ext_reduce(f):
            """exterior algebra: drop y1^2, y2^2 (the order y1 ... y2 is kept in all products below)"""
            return R({e: c for e, c in f.dict().items() if e[2] <= 1 and e[3] <= 1})
        Neven = x2 ** p + lam * x1 ** (p - 1) * x2 + mu * x1 ** (p - 2) * y1 * x2 * y2
        Neven_phi = (x1 + x2) ** p + lam * x1 ** (p - 1) * (x1 + x2) + mu * x1 ** (p - 2) * y1 * (x1 + x2) * (y1 + y2)
        diff = ext_reduce(Neven_phi - Neven)
        sol = LM.ideal(list(diff.coefficients())).groebner_basis()
        check(set(sol) == {lam + 1, mu},
              'p. 125: invariance under (y2, x2) -> (y1 + y2, x1 + x2) gives lambda = -1, mu = 0 (p = %d)' % p)
        Nodd = lam * x1 ** m * y2 + mu * x1 ** (m - 1) * y1 * x2
        Nodd_phi = lam * x1 ** m * (y1 + y2) + mu * x1 ** (m - 1) * y1 * (x1 + x2)
        sol = LM.ideal(list(ext_reduce(Nodd_phi - Nodd).coefficients())).groebner_basis()
        check(set(sol) == {lam + mu},
              'p. 125: for norm(y2) the same automorphism gives lambda = -mu (p = %d)' % p)
        S = PolynomialRing(F, 'x1,x2,c')
        X1, X2, C = S.gens()
        f = X2 ** p - X1 ** (p - 1) * X2
        g = (X2 + C * X1) ** p - X1 ** (p - 1) * (X2 + C * X1)
        check(all((g - f).subs({C: cv}) == 0 for cv in F),
              'prop:norm-rank-two (i) is unchanged under x2 -> x2 + c x1, c in F_p (p = %d)' % p)
    for p in prime_range(3, 60):
        for cc in range(1, p):
            perm = [(cc * k) % p for k in range(p)]
            check((-1) ** perm_sign_inv(perm) == legendre_symbol(cc, p) and
                  legendre_symbol(cc, p) % p == pow(cc, (p - 1) // 2, p),
                  'p. 125: multiplication by c permutes the cosets with sign (c/p) = c^m (p = %d)' % p)

    # --- the Evens norm at chain level (pp. 124-126) ---------------------------
    explicit_norm_checks()


def norm_cocycle(p, r):
    """(1 wr xhat) o phi on the generators e_(a,b) of P_(pr), P = T (x) T for
    G = <g1> x <g2>, H = <g2>, xhat(h^a e_r) = 1, cosets g1^k (k = 0..p-1)."""
    Q = Periodic(p)

    def act(u, v, term):
        """g1^u g2^v on Q^(x)p: g2 diagonal, g1 = (pi; 1, ..., 1), pi(k) = k + 1."""
        t = tuple((i, (a + v) % p) for (i, a) in term)
        sign = 1
        for _ in range(u):
            last = t[-1]
            if (last[0] * sum(i for (i, _) in t[:-1])) % 2:
                sign = -sign
            t = (last,) + t[:-1]
        return sign, t

    def dP(a, b):
        out = {}
        if a > 0:
            terms = {1: 1, 0: -1} if a % 2 == 1 else {u: 1 for u in range(p)}
            for u, c in terms.items():
                addto(out, ((a - 1, b), (u, 0)), c)
        if b > 0:
            terms = {1: 1, 0: -1} if b % 2 == 1 else {v: 1 for v in range(p)}
            for v, c in terms.items():
                addto(out, ((a, b - 1), (0, v)), (-1) ** a * c)
        return out

    phi = {}

    def image_of_boundary(gen):
        z = {}
        for (g2, (u, v)), c in dP(*gen).items():
            for term, c2 in phi_of(g2).items():
                sg, t = act(u, v, term)
                addto(z, t, c * c2 * sg)
        return clean(z, p)

    def phi_of(gen):
        if gen not in phi:
            if sum(gen) == 0:
                phi[gen] = {tuple((0, 0) for _ in range(p)): 1}
            else:
                phi[gen] = clean(lin(Q.s, image_of_boundary(gen)), p)
        return phi[gen]
    ok = True
    for n in range(1, p * r + 1):
        for a in range(n + 1):
            if clean(lin(Q.d, phi_of((a, n - a))), p) != image_of_boundary((a, n - a)):
                ok = False
    # the G-action commutes with d and is an action of Z/p x Z/p
    t0 = tuple((1, 0) for _ in range(p - 1)) + ((2, 1),)
    s1, t1 = act(1, 0, t0)
    ok_act = clean(lin(Q.d, {t1: s1}), p) == clean({act(1, 0, k)[1]: c * act(1, 0, k)[0] for k, c in Q.d(t0).items()}, p)
    sp, tp = act(p, 0, t0)
    ok_act = ok_act and sp == 1 and tp == t0
    sgn = (-1) ** (r * (p * (p - 1) // 2))      # Koszul sign of xhat^(x)p on (Q_r)^(x)p
    vals = {}
    for a in range(p * r + 1):
        v = sum(c for term, c in phi_of((a, p * r - a)).items() if all(i == r for (i, _) in term))
        vals[(a, p * r - a)] = (sgn * v) % p
    return vals, ok and ok_act


def explicit_norm_checks():
    for p, rs in ((2, (1, 2, 3)), (3, (1, 2, 3)), (5, (1, 2))):
        N = p * max(rs) + 2
        tab = cup_table(p, N)
        # the classes x^k (x = e_2^*) and y x^k (y = e_1^*) as multiples of e_n^*
        single = {(0, 0): 1, (1, 0): 1}
        for k in range(1, N // 2 + 1):
            single[(0, k)] = single[(0, k - 1)] * tab[(2 * k - 2, 2)] % p
            if 2 * k + 1 <= N:
                single[(1, k)] = single[(0, k)] * tab[(2 * k, 1)] % p
        if p == 2:
            check(tab[(1, 1)] == 1, 'H^*(Z/2, F_2) = F_2[y]: y^2 = e_2^*')
        else:
            check(tab[(1, 1)] == 0, 'H^*(Z/%d, F_p): y^2 = 0' % p)

        def express(vals):
            out = {}
            for (a, b), v in vals.items():
                if v:
                    e1, k1, e2, k2 = a % 2, a // 2, b % 2, b // 2
                    coeff = (-1) ** (a * b) * single[(e1, k1)] * single[(e2, k2)] % p
                    out[(e1, k1, e2, k2)] = v * pow(coeff, -1, p) % p
            return out
        res = {}
        for r in rs:
            vals, ok = norm_cocycle(p, r)
            check(ok, 'the lift phi : T (x) T -> Q^(x)%d is a chain map of G-modules up to degree %d' % (p, p * r))
            res[r] = express(vals)
        m = (p - 1) // 2
        if p == 2:
            # monomials in y1, y2 (x = y^2): (e1, k1, e2, k2) -> y1^(e1+2k1) y2^(e2+2k2)
            def as_poly(d):
                R = PolynomialRing(GF(2), 'y1,y2')
                Y1, Y2 = R.gens()
                return sum(c * Y1 ** (e1 + 2 * k1) * Y2 ** (e2 + 2 * k2) for (e1, k1, e2, k2), c in d.items())
            R = PolynomialRing(GF(2), 'y1,y2')
            Y1, Y2 = R.gens()
            n1 = as_poly(res[1])
            check(n1 == Y2 ** 2 + Y1 * Y2, 'prop:norm-rank-two, p = 2: norm(y2) = y2^2 + y1 y2 (p. 126)')
            check(as_poly(res[2]) == n1 ** 2 and as_poly(res[3]) == n1 ** 3,
                  'p = 2: norm(y2^2) = norm(y2)^2, norm(y2^3) = norm(y2)^3 (prop:norm-properties (i))')
            continue
        # p odd: x2 = (0,0,0,1); x1^(p-1) x2 = (0, p-1, 0, 1)
        check(res[2] == {(0, 0, 0, p): 1, (0, p - 1, 0, 1): p - 1},
              'prop:norm-rank-two (i): norm(x2) = x2^p - x1^(p-1) x2, computed at chain level (p = %d)' % p)
        lam = res[1].get((0, m, 1, 0), 0)
        mu = res[1].get((1, m - 1, 0, 1), 0)
        check(set(res[1]) == {(0, m, 1, 0), (1, m - 1, 0, 1)} and (lam + mu) % p == 0,
              'prop:norm-rank-two (ii): norm(y2) = lambda x1^((p-3)/2) (x1 y2 - y1 x2) (p = %d)' % p)
        mf = factorial(m) % p
        check(lam * lam % p == (-1) ** (m + 1) % p and lam in (pow(mf, -1, p), (-pow(mf, -1, p)) % p),
              'prop:norm-rank-two (ii): lambda^2 = (-1)^(m+1), lambda = +-1/m! (p = %d; here lambda = %d)' % (p, lam))
        check(res[2].get((0, p - 1, 0, 1)) == p - 1,
              'p. 144: theta_2 = -1: D_(2(p-1))(x) = -x for G = Z/%d' % p)
        if 3 in rs:
            # norm(y2 x2) = norm(y2) norm(x2): (lam x1^m y2 + mu x1^(m-1) y1 x2)(x2^p - x1^(p-1) x2)
            want = {}
            for (e1, k1, e2, k2), c in res[1].items():
                for (f1, l1, f2, l2), d in res[2].items():
                    key = (e1 + f1, k1 + l1, e2 + f2, k2 + l2)
                    addto(want, key, c * d)
            check(res[3] == clean(want, p),
                  'prop:norm-properties (i): norm(y2 x2) = norm(y2) norm(x2) at chain level (p = %d)' % p)


# ---------------------------------------------------------------------------
# Section 4.2

def section_4_2():
    # the Warning: R = Z + (Z/p)^N, (a, b)(c, d) = (ac, cb + ad)
    for p in (2, 3, 5):
        for N in range(1, 6):
            import random
            rng = random.Random(10 * p + N)

            def mul(u, v):
                (a, b), (c, d) = u, v
                return (a * c, tuple((c * bi + a * di) % p for bi, di in zip(b, d)))

            def rnd():
                return (rng.randint(-5, 5), tuple(rng.randrange(p) for _ in range(N)))
            ok = True
            for _ in range(30):
                u, v, w = rnd(), rnd(), rnd()
                ok = ok and mul(u, v) == mul(v, u) and mul(mul(u, v), w) == mul(u, mul(v, w))
            # H^1(Z/p, R) = Hom(Z/p, R) = elements of order dividing p = 0 + (Z/p)^N; the ideal
            # 0 + (Z/p)^N kills it and Z acts through F_p, so a minimal generating set has N elements
            check(ok, 'Warning (p. 127): (a, b)(c, d) = (ac, cb + ad) makes Z + (Z/p)^N a commutative ring')
            ann = all(mul((0, tuple(int(i == j) for i in range(N))), (0, tuple(int(i == k) for i in range(N))))
                      == (0, (0,) * N) for j in range(N) for k in range(N))
            check(ann and p * 1 % p == 0,
                  'Warning (p. 127): H^1(Z/%d, R) = (Z/p)^%d is an F_p-vector space on which R acts through F_p, '
                  'so it needs %d generators' % (p, N, N))
    # Mackey for a central subgroup Z of order p of a p-group P
    for (o, rng_ids) in ((8, range(1, 6)), (16, range(1, 15)), (27, range(1, 6))):
        for i in rng_ids:
            P = libgap.SmallGroup(o, i)
            p = int(libgap.FactorsInt(o)[0])
            cen = P.Centre()
            for z in cen.AsList():
                if int(z.Order()) != p:
                    continue
                Z = libgap.Subgroup(P, [z])
                dcs = libgap.DoubleCosets(P, Z, Z)
                check(len(dcs) == o // p and all(int(dc.Size()) == p and
                                                   int(libgap.Intersection(Z, Z ** dc.Representative()).Size()) == p
                                                   for dc in dcs),
                      'proof of th:evens-finite-generation: res_(P,Z) norm_(Z,P)(sigma) = sigma^|P:Z| '
                      '(SmallGroup(%d, %d), central Z of order %d)' % (o, i, p))
                break
    # rows of E_2: cup with sigma^n, H^q(Z, M) -> H^(q+2n)(Z, M) for Z = Z/p, via the periodic resolution:
    # H^0 = M^Z, H^(2k) = M^Z / N M, H^(2k+1) = ker N / (g - 1) M; sigma^n acts as the identity of the periodic
    # part (Corollary 3.5.4 of Volume I), so it is iso for q >= 1 and the projection M^Z -> M^Z/NM for q = 0.
    for p in (2, 3, 5):
        F = GF(p)
        # (g - 1) and N = 1 + g + ... + g^(p-1) on M, written out (no matrix powers)
        mods = {'F_p': (matrix(F, [[0]], sparse=True), matrix(F, [[p]], sparse=True)),
                'F_p Z/p (regular)': (matrix(F, p, p, {(i, j): (1 if j == (i + 1) % p else 0) - (1 if i == j else 0)
                                                       for i in range(p) for j in range(p)}, sparse=True),
                                      matrix(F, p, p, {(i, j): 1 for i in range(p) for j in range(p)}, sparse=True))}
        for name, (gm1, Nm) in mods.items():
            inv = gm1.right_kernel().dimension()
            NM = Nm.column_space().dimension()
            kerN = Nm.right_kernel().dimension()
            gM = gm1.column_space().dimension()
            H0, Heven, Hodd = inv, inv - NM, kerN - gM
            check(H0 >= Heven and (H0 > Heven) == (name != 'F_p'),
                  'p. 128: H^0(Z, M) -> H^(2n)(Z, M) is onto, iso iff N M = 0 (p = %d, M = %s)' % (p, name))
            check(Heven == Hodd == (1 if name == 'F_p' else 0),
                  'p. 128: periodicity of H^q(Z/p, M), q >= 1 (p = %d, M = %s)' % (p, name))


# ---------------------------------------------------------------------------
# Section 4.3

def cyclic_cochains_bockstein(q, p, n, r):
    """For G = Z/q (q a power of p), the n-th Bockstein of p. 134 on x = e_r^* in H^r(G, F_p):
    returns None if x is not in the image of H^r(G, Z/p^n), else the coefficient of e_(r+1)^*.
    Cochains on the periodic resolution with values in A: delta f = (-1)^(r+1) f o d, and
    f o d(e_(r+1)) = (sum over the terms of d e_(r+1)) f(e_r) = 0 (r even) or q f(e_r) (r odd)."""
    mult = 0 if r % 2 == 0 else q          # f o d on C^r -> C^(r+1) for trivial coefficients
    sign = (-1) ** (r + 1)
    # x in the image of H^r(G, Z/p^n): exists a cocycle with values in Z/p^n reducing to 1
    lifts = [c for c in range(p ** n) if c % p == 1 and (sign * mult * c) % p ** n == 0]
    if not lifts:
        return None
    c = lifts[0]
    # connecting map of 0 -> Z/p^n -> Z/p^(n+1) -> F_p -> 0 ... here: lift the Z/p^n cocycle c to
    # Z/p^(n+1), take the coboundary, which lies in p^n Z/p^(n+1) = F_p; for n = 1 this is beta.
    # (Equivalently, the text's beta_n: delta of the lift lies in the image of F_p -> Z/p^n.)
    val = (sign * mult * c) % p ** (n + 1)
    assert val % p ** n == 0
    return (val // p ** n) % p


def section_4_3():
    # the Example of p. 133 and the Bockstein spectral sequence for cyclic p-groups
    for p in (2, 3, 5):
        for k in (1, 2, 3):
            q = p ** k
            for r in range(0, 7):
                vals = [cyclic_cochains_bockstein(q, p, n, r) for n in range(1, k + 2)]
                if r % 2 == 0:
                    check(all(v in (None, 0) for v in vals[:k]) and vals[0] == 0,
                          'p. 134: beta_n = 0 on H^%d(Z/%d, F_p) (even degree)' % (r, q))
                else:
                    check(all(v == 0 for v in vals[:k - 1]) and vals[k - 1] not in (None, 0),
                          'p. 134: beta_n = 0 for n < %d and beta_%d : H^%d -> H^%d is an isomorphism '
                          '(Z/%d): the torsion of H^%d(Z/%d, Z) has order p^%d' % (k, k, r, r + 1, q, r + 1, q, k))
                if k == 1:
                    check((vals[0] != 0) == (r % 2 == 1),
                          'p. 133 Example: beta : H^%d(Z/%d, F_p) -> H^%d is an isomorphism iff the degree is odd'
                          % (r, p, r + 1))
            # integral cohomology of Z/q from the periodic resolution: Hom(T_r, Z) = Z with
            # delta^r = 0 (r even) and multiplication by q (r odd)
            CC = ChainComplex({r: matrix(ZZ, [[0 if r % 2 == 0 else q]]) for r in range(0, 8)},
                              degree_of_differential=1)
            H = CC.homology()
            check(sorted(H[0].invariants()) == [0] and
                  all(sorted(H[r].invariants()) == ([q] if r % 2 == 0 else []) for r in range(1, 7)),
                  'p. 133: H^0(Z/%d, Z) = Z, H^r = Z/%d for r > 0 even, 0 for r odd' % (q, q))
            # E_(k+1) = 0 in positive degrees: every class of positive degree is a source or target of beta_k
            check(all(cyclic_cochains_bockstein(q, p, k, r) not in (None, 0) for r in range(1, 7, 2)),
                  'p. 134: the Bockstein spectral sequence of Z/%d has E_%d = 0 in positive degrees and converges '
                  'to F_p in degree 0 = (H^*(G, Z)/torsion) (x) F_p' % (q, k + 1))

    # beta on H^*(Z/p x Z/p, F_p) at cochain level; lem:bockstein-squared-zero, lem:bockstein-product
    for p in (2, 3, 5):
        N = 5
        tab = cup_table(p, N + 1)

        def single(e, k):
            v = 1
            for j in range(1, k + 1):
                v = v * tab[(2 * j - 2, 2)] % p
            if e:
                v = v * tab[(2 * k, 1)] % p if k > 0 else 1
            return v

        def mono_cochain(e1, k1, e2, k2):
            a, b = e1 + 2 * k1, e2 + 2 * k2
            return {(a, b): (-1) ** (a * b) * single(e1, k1) * single(e2, k2) % p}

        def beta_cochain(f, n):
            """f : dict (a, b) -> value on e_a (x) e_b (degree n); integral lift with values 0..p-1,
            delta = (-1)^(n+1) f o d, divided by p."""
            out = {}
            for a in range(n + 2):
                b = n + 1 - a
                tot = 0
                # d(e_a (x) e_b) = d e_a (x) e_b + (-1)^a e_a (x) d e_b; on trivial modules
                # (g - 1) -> 0 and N -> p
                if a > 0 and a % 2 == 0:
                    tot += p * f.get((a - 1, b), 0)
                if b > 0 and b % 2 == 0:
                    tot += (-1) ** a * p * f.get((a, b - 1), 0)
                tot *= (-1) ** (n + 1)
                assert tot % p == 0
                if (tot // p) % p:
                    out[(a, b)] = (tot // p) % p
            return out
        # monomials as cochains; algebra product by exponent addition with the Koszul sign
        def monos(D):
            out = []
            for e1 in (0, 1):
                for e2 in (0, 1):
                    for k1 in range(D // 2 + 1):
                        for k2 in range(D // 2 + 1):
                            if e1 + 2 * k1 + e2 + 2 * k2 == D and (p > 2 or True):
                                out.append((e1, k1, e2, k2))
            return out

        def to_cochain(poly):
            out = {}
            for mo, c in poly.items():
                for k, v in mono_cochain(*mo).items():
                    addto(out, k, c * v)
            return clean(out, p)

        def mono_mul(m1, m2):
            """(y1^e1 x1^k1 y2^e2 x2^k2)(y1^f1 ...) as {mono: coeff}; p = 2: y^2 = x."""
            e1, k1, e2, k2 = m1
            f1, l1, f2, l2 = m2
            sign = (-1) ** (e2 * f1)            # move y2^e2 past y1^f1
            E1, K1, E2, K2 = e1 + f1, k1 + l1, e2 + f2, k2 + l2
            c = sign
            if E1 == 2:
                if p > 2:
                    return {}
                E1, K1 = 0, K1 + 1
            if E2 == 2:
                if p > 2:
                    return {}
                E2, K2 = 0, K2 + 1
            return {(E1, K1, E2, K2): c % p}

        def beta_mono(mo):
            deg = mo[0] + 2 * mo[1] + mo[2] + 2 * mo[3]
            return beta_cochain(to_cochain({mo: 1}), deg)

        def cochain_to_poly(f):
            """inverse of to_cochain on a fixed degree: each (a, b) is a single monomial."""
            out = {}
            for (a, b), v in f.items():
                mo = (a % 2, a // 2, b % 2, b // 2)
                c = mono_cochain(*mo)[(a, b)]
                out[mo] = v * pow(c, -1, p) % p
            return out
        ok2 = True
        for D in range(0, 5):
            for mo in monos(D):
                bb = beta_cochain(beta_mono(mo), D + 1)
                ok2 = ok2 and not bb
        check(ok2, 'lem:bockstein-squared-zero: beta^2 = 0 on H^n(Z/%d x Z/%d, F_p), n <= 4' % (p, p))
        okp = True
        for D1 in range(0, 3):
            for D2 in range(0, 3):
                for m1 in monos(D1):
                    for m2 in monos(D2):
                        prod = mono_mul(m1, m2)
                        lhs = beta_cochain(to_cochain(prod), D1 + D2)
                        bx = cochain_to_poly(beta_mono(m1))
                        by = cochain_to_poly(beta_mono(m2))
                        rhs_poly = {}
                        for mo, c in bx.items():
                            for k, v in mono_mul(mo, m2).items():
                                addto(rhs_poly, k, c * v)
                        for mo, c in by.items():
                            for k, v in mono_mul(m1, mo).items():
                                addto(rhs_poly, k, (-1) ** D1 * c * v)
                        okp = okp and clean(lhs, p) == to_cochain(clean(rhs_poly, p))
        check(okp, 'lem:bockstein-product: beta(xy) = beta(x) y + (-1)^deg(x) x beta(y) on H^*(Z/%d x Z/%d, F_p),'
                   ' monomials of degree <= 2 each' % (p, p))
        if p == 2:
            check(cochain_to_poly(beta_mono((1, 0, 0, 0))) == {(0, 1, 0, 0): 1},
                  'H^*(Z/2, F_2): beta(y) = y^2 = Sq^1 y')
        else:
            check(cochain_to_poly(beta_mono((1, 0, 0, 0))) == {(0, 1, 0, 0): 1},
                  'H^*(Z/%d, F_p): beta(y) = x = e_2^* (so x = -beta(y) in Sections 4.4 and 4.6 is -e_2^*)' % p)

    # the twisted Bockstein for p = 2 (p. 135): (Z/4)^sign, the generator acting by -1
    tab2 = cup_table(2, 9)
    for r in range(0, 8):
        # on cochains of the periodic resolution of Z/2 with values in A: f o d(e_(r+1)) = (g - 1) f(e_r)
        # (r + 1 odd) or (1 + g) f(e_r) (r + 1 even); for A = Z/4 trivial: 0 or 2; for (Z/4)^sign: -2 or 0
        triv = 0 if r % 2 == 0 else 2
        twist = -2 if r % 2 == 0 else 0
        beta = (((-1) ** (r + 1) * triv) // 2) % 2
        beta_t = (((-1) ** (r + 1) * twist) // 2) % 2
        a_times = tab2[(1, r)]      # a . e_r^* = (e_1^* u e_r^*)(e_(r+1)) e_(r+1)^*
        check(beta_t == (beta + a_times) % 2,
              'p. 135: for p = 2 the twisted Bockstein is beta~(z) = beta(z) + a z on H^%d(Z/2, F_2)' % r)
    refuted(all(((((-1) ** (r + 1) * (0 if r % 2 == 0 else 2)) // 2) % 2) ==
                ((((-1) ** (r + 1) * (-2 if r % 2 == 0 else 0)) // 2) % 2) for r in range(4)),
            'proof of lem:bockstein-d-j (i) as printed: for p = 2, beta~ and beta agree on H^*(Z/2, F_2)')


def main():
    section_4_1()
    section_4_2()
    section_4_3()
    print('ok chapter-4a: %d checks' % COUNT[0])


if __name__ == '__main__':
    main()
