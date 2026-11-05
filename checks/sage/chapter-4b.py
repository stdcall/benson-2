"""Exact checks of Chapter 4, Sections 4.4-4.8 (Sage).

Run: sage -python checks/sage/chapter-4b.py (plain asserts; do not use -O).
The last line of the output is "ok chapter-4b: N checks".

Book: D. J. Benson, Representations and Cohomology II, Cambridge Studies in
Advanced Mathematics 31 (first paperback edition 1998), Chapter 4, Sections
4.4-4.8, printed pp. 137-152.  Our files: content/04-04-steenrod-operations.typ
... content/04-08-steenrod-spectral.typ (Sections 4.1-4.3: chapter-4a.py).
Pages are printed pages; labels are those of content/04-*.typ.  Expected
values are the book's statements read off the printed pages; where the
printed text was corrected, the printed reading is kept as a refuted check
(`refuted`) beside the corrected one.  Notation: m = (p - 1)/2,
c_r = (-1)^(m r(r+1)/2) (m!)^r (the constant of def:steenrod-powers, so that
D_((p-1)(r-2i))(x) = (-1)^i c_r P^i(x) for x of degree r).

Independent tools: Sage's SteenrodAlgebra (Milnor basis multiplication and
coproduct) for the Steenrod algebra; an explicit action on H^*(V, F_p) of
elementary abelian V (F_2[x_1, x_2, x_3]; Lambda(y_1, y_2) (x) F_p[x_1, x_2]
with beta(y_i) = x_i) defined only by Sq(x) = x + x^2, P(x) = x + x^p,
P(y) = y and the Cartan formula; mod p cohomology of p-groups computed from
minimal resolutions over F_p G (GAP for the groups), with Bocksteins
transported from the bar resolution (the 2-cocycle (y~(g) + y~(h) -
y~(gh))/p) and products by lifting cocycles to chain maps (Yoneda).

What is checked, by section:

section_4_4 (pp. 137-138): the Remark after def:steenrod-powers ((m!)^2 =
  (-1)^(m+1) = -(-1/p), (m!)^4 = 1, Wilson; p < 1000); th:steenrod-squares
  (vii) for 0 < a < 2b, a + b <= 22; th:steenrod-powers (vi) for p = 3, 5,
  7: P^a P^b for a < pb and P^a beta P^b for a <= pb (the corrected
  hypothesis; the printed "a <= b" covers only part of it and leaves for
  instance P^2 beta P^1 (p = 3), which is not admissible, without a
  relation); the Cartan formulas (v) as the coproducts of Sage's
  SteenrodAlgebra; on H^*(V): (ii)-(iv), Sq^1 = beta, and the Adem
  relations of (vii), (vi) on all monomials of degree <= 6 (p = 2, rank 3)
  and <= 8 (p = 3, 5, rank 2).
section_4_5 (pp. 138-144):
  * lem:vanishing-d-j: the classes a_j invariant under N(Z/p)/(Z/p) =
    F_p^* (twisted by the sign character for r odd) are exactly those with
    j = 2k(p-1), 2k(p-1) - 1 (r even) and (2k+1)(p-1), (2k+1)(p-1) - 1
    (r odd) (p <= 13, j <= 8p);
  * lem:bockstein-d-j: refuted as printed for p = 2 and odd degree (with
    D_j = Sq^(r-j): beta D_1(y) = beta(y) = y^2 != 0 for y in H^1(Z/2);
    beta D_(2j) = D_(2j-1) would say Sq^1 Sq^(odd) = Sq^(even)); the
    corrected statement (beta D_j = D_(j-1) if j = (p-1)r mod 2, else 0)
    against Sage's Sq^1 Sq^i (r <= 12) and the action on H^*(V);
  * lem:cartan-d-j and "the signs work out right": c_(r+s) =
    (-1)^(m r s) c_r c_s (p <= 13, r, s <= 12);
  * the constants theta_r (p. 144): with theta_(2r) = (-1)^r and
    theta_(2r+1) = (-1)^r theta_1, def:steenrod-powers gives P^0 = 1 in all
    degrees r <= 12 iff theta_1 = (-1)^m m! (= -1/m!) (all odd p < 200);
    the printed theta_1 = m! gives P^0 = -1 in odd degrees for p = 3 mod 4
    (refuted); (-1)^(p(p-1)/2) theta_1^2 = theta_2 = -1 for both signs;
    the first display of Case (ii) of Section 4.6 (p. 146) with r = 1,
    zeta = y_2 gives norm(y_2) = c_1 x_1^((p-3)/2)(x_1 y_2 - y_1 x_2), and
    c_1 = (-1)^m m! = -(m!)^-1, not the printed (m!)^-1 (refuted, p <= 200);
  * the complex X (pp. 142-143): free F_p(Z/p)-modules of ranks 6, 18, 42,
    90, 186 (p = 3); H_n(X) = 0 for 1 <= n <= 4 and H_0(X) = F_p with
    trivial action (p = 2, 3; p = 5: n <= 1); the example d(3,1,3,1,2) =
    (1,3,1,2) - (3,1,3,2) holds with the sign (-1)^(i-1) and is refuted
    with the printed (-1)^i; d^2 = 0; d h + h d = 1 holds for p = 2 in
    degrees 1-4 with (-1)^(i-1) and is refuted for p = 3 with either sign
    ((1,2,3,2) |-> 0); the corrected argument: the complex of all
    sequences with lambda_i != lambda_(i+1) has the homology F_p of a
    point (contracted by h), the subcomplex of sequences missing some j
    has the homology of the (p-2)-sphere (p = 3, 5), and X is the quotient;
  * the map xi (p. 143): the example ((3,1,3,1,2), r = 2: one admissible
    sequence of i's, the term (x_0,x_1,x_2) (x) (x_2) (x) (x_0,x_1,x_2)
    with sign +); the support statements used on pp. 143-144 (no terms in
    (C_r)^(x)p when n > (p-1)r, only +-(x_0..x_r)^(x)p when n = (p-1)r;
    p = 3, r <= 3); for p = 2, xi = psi on the alternating sequences; the
    claim that xi is a chain map is refuted for p = 3 (for both signs of
    d: d xi((1,2,1,3) (x) (x_0)) = 0, xi(d(1,2,1,3) (x) (x_0)) = +-2
    (x_0)^(x)3), also composed with a lift T -> X;
  * psi for p = 2 (p. 142): with the corrected parity (the first formula
    for n odd) psi is a chain map T (x) C(G) -> C(G) (x) C(G) over F_2
    (n <= 5, r <= 6, formal vertices), n = 0 is the Alexander-Whitney map,
    n = r gives (x_0..x_r) (x) (x_0..x_r), n > r gives 0; the printed
    parity is refuted.
section_4_6 (pp. 144-148):
  * th:symmetric-adem-relations (i) and (ii) in Sage's SteenrodAlgebra
    (p = 2: degrees n <= 12; p = 3: n <= 6; p = 5: n <= 5), with [beta, P] = beta P -
    P beta; with beta P + P beta instead, (ii) is refuted;
  * Case (i): the four lines of the display (rational functions over F_2,
    r <= 6, all j, k <= 8) and the substitution x_1^-1 = t(s+t), x_2^-1 =
    s(s+t); the residue: coefficient of t^-1 gives binom(b-1-j, a-2j);
  * Case (ii): the double norm computed formally from the first display of
    p. 146 (c_r, Lemma 4.5.3/4.5.4, prop:norm-properties (i)) equals the
    second display; with the printed norm(y_2) = (m!)^-1 ... this holds
    and the procedure of p. 146 then gives beta P^j P^i + P^j beta P^i in
    (b), which is refuted (not symmetric, above); with the corrected
    norm(y_2) = -(m!)^-1 ... the second display holds with the signs of its
    last two lines changed, and (b) = sum (-1)^(i+j) (x_2^p x_1^(1-p) -
    x_2)^(-2mi) x_1^(-2m(j-1)) (beta P^j P^i - P^j beta P^i) (p = 3, 5, 7;
    r <= 4; i, j <= 2); the substitution identities (x_1^-2m = -(t^p +
    ... + s^(p-1) t), (x_2^p x_1^(1-p) - x_2)^-2m = -s^p, u = (1-t)^(p-1));
    the specialisations P(tu)P(1) = P(u)P(t^p), [beta, P(tu)]P(1) =
    t[beta, P(u)]P(t^p), P(tu) beta P(1) = ((1-t) beta P(u) + t P(u) beta)
    P(t^p) degree by degree in Sage; the residues give the coefficients of
    th:steenrod-powers (vi).
section_4_7 (pp. 148-150):
  * group theory (GAP), all groups of order p^3 (p = 2, 3, 5, 7): |Phi(G)|
    = p iff G is Z/p^2 x Z/p or non-abelian; such G has a cyclic maximal
    subgroup or exponent p, and then G = <g, h>, z = [g, h] central of
    order p, H = <h, z> elementary abelian, and conjugation by g fixes the
    restriction of the dual of h and moves the other one (the transvection
    of p. 149); th:serre-bocksteins reductions for all groups of order
    p^n (p = 2: n <= 6, p = 3: n <= 5, p = 5: n <= 4): N of index p in
    Phi(G), normal in G, with |Phi(G/N)| = p; |Phi(G)| = p and G/Phi(G)
    cyclic => G cyclic; otherwise H >= Phi(G) of order p^3 with Phi(H) =
    Phi(G); (p+1)|G:H| = ((p+1)/p^2)|G:Phi(G)| (the printed (p + 1/p^2)
    refuted);
  * the polynomial identities prod_lambda (v_2 + lambda v_1) = v_2^p -
    v_1^(p-1) v_2 and v_1 (v_2^p - v_1^(p-1) v_2) = product over all lines
    (Lemma 4.7.1, the Remark after lem:norm-bockstein-product; p <= 13);
  * lem:serre-order-p-cubed in mod p cohomology computed from minimal
    resolutions: for the groups of order 8 with |Phi| = 2 and of order 27
    with |Phi| = 3, the product of the Bocksteins of one element from each
    of the p + 1 lines of H^1 vanishes, and for those with a cyclic maximal
    subgroup already a product prod_lambda beta(y_2 + lambda y_1) of p of
    them; for (Z/p)^2 (p = 2, 3) the product over all lines is non-zero;
    th:serre-bocksteins for the 2-generator groups of order 16 that are not
    elementary abelian (a product of at most (3/4)|G:Phi| = 3 Bocksteins
    vanishes) and for Q_8 x Z/2 (the 6 Bocksteins of the proof, of the
    elements not vanishing on Q_8, have product 0 in degree 12).
section_4_8 (pp. 150-152): the bidegrees (d_r : E^(a,b) -> E^(a+r, b-r+1);
  the transgressions of th:steenrod-transgression and Kudo's theorem, with
  the corrected E^(2np+2, 0)); H^*(K(Z/2, 2), F_2): the admissible
  sequences of excess < 2 are (2^(i-1), ..., 2, 1), giving u_i of degree
  2^i + 1 with Sq^(2^i) u_i = u_(i+1); the transgressions on small
  extensions 1 -> Z/2 -> G -> G/Z -> 1 (G = Z/4, Z/4 x Z/2, D_8, Q_8): with
  zeta computed from G (squares and commutators of lifts), d_2(u) = zeta,
  d_3(u^2) = Sq^1 zeta, d_5(u^4) = Sq^2 Sq^1 zeta give an E_infinity with
  the Poincare series of H^*(G, F_2) computed from minimal resolutions
  (degrees <= 8).

What these checks do NOT establish.  The Steenrod algebra checks are in the
listed degrees; the action on H^*(V) is a model defined by the Cartan
formula, so it does not test the Cartan formula itself, only the Adem
relations and axioms on it.  The constants theta_r: the computation shows
which value of theta_1 the book's definitions require, not the construction
of a coset order realising it.  The complex X and the maps xi, psi are
checked in the listed degrees; no corrected sign rule for xi is proposed
or checked here.  The group cohomology computations are for the listed
groups and degrees; the spectral sequence of Section 4.8 is not computed,
only the consequences of the transgression formulas compared with the
dimensions of H^*(G, F_2).  Nothing here compares our text with the
printed book.
"""
import itertools

from sage.all import (
    GF, QQ, PolynomialRing, SteenrodAlgebra, binomial, factorial,
    legendre_symbol, libgap, matrix, prime_range, vector, zero_matrix,
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


def c_const(p, r):
    """c_r = (-1)^(m r(r+1)/2) (m!)^r in F_p (def:steenrod-powers: P^i = (-1)^i c_r^-1 D_(...))."""
    m = (p - 1) // 2
    return GF(p)((-1) ** (m * r * (r + 1) // 2)) * GF(p)(factorial(m)) ** r


# ---------------------------------------------------------------------------
# An action of the Steenrod algebra on H^*(V, F_p), V elementary abelian.
# p = 2: monomials of F_2[x1..xk] as exponent tuples.  p odd: monomials of
# Lambda(y1, y2) (x) F_p[x1, x2] as (e1, e2, k1, k2), y1 before y2.

def sq_mono(k, mono):
    out = {}
    for js in itertools.product(*[range(min(e, k) + 1) for e in mono]):
        if sum(js) != k:
            continue
        c = 1
        for e, j in zip(mono, js):
            c *= binomial(e, j)
        if c % 2:
            addto(out, tuple(e + j for e, j in zip(mono, js)), 1)
    return clean(out, 2)


def sq(k, f):
    out = {}
    if k < 0:
        return out
    for mono, c in f.items():
        for m2, c2 in sq_mono(k, mono).items():
            addto(out, m2, c * c2)
    return clean(out, 2)


def beta2(f):
    """the Bockstein on F_2[x1..xk]: the derivation with beta(x_i) = x_i^2 (Example of p. 133,
    lem:bockstein-product)."""
    out = {}
    for mono, c in f.items():
        for i, e in enumerate(mono):
            if e % 2:
                m2 = list(mono)
                m2[i] += 1
                addto(out, tuple(m2), c * e)
    return clean(out, 2)


def pw_mono(p, k, mono):
    e1, e2, k1, k2 = mono
    out = {}
    for j1 in range(min(k1, k) + 1):
        j2 = k - j1
        if j2 < 0 or j2 > k2:
            continue
        c = binomial(k1, j1) * binomial(k2, j2)
        if c % p:
            addto(out, (e1, e2, k1 + (p - 1) * j1, k2 + (p - 1) * j2), c)
    return clean(out, p)


def pw(p, k, f):
    out = {}
    if k < 0:
        return out
    for mono, c in f.items():
        for m2, c2 in pw_mono(p, k, mono).items():
            addto(out, m2, c * c2)
    return clean(out, p)


def bt(p, f):
    """beta on Lambda(y1, y2) (x) F_p[x1, x2]: derivation, beta(y_i) = x_i, beta(x_i) = 0."""
    out = {}
    for (e1, e2, k1, k2), c in f.items():
        if e1:
            addto(out, (0, e2, k1 + 1, k2), c)
        if e2:
            addto(out, (e1, 0, k1, k2 + 1), c * (-1) ** e1)
    return clean(out, p)


def deg_odd(mono):
    e1, e2, k1, k2 = mono
    return e1 + e2 + 2 * (k1 + k2)


# ---------------------------------------------------------------------------
# Section 4.4

def section_4_4():
    for p in prime_range(3, 1000):
        m = (p - 1) // 2
        mf = GF(p)(factorial(m))
        check(mf * (-1) ** m * mf == GF(p)(factorial(p - 1)) == -1 and mf ** 2 == (-1) ** (m + 1)
              and mf ** 2 == -legendre_symbol(-1, p) and mf ** 4 == 1,
              'Remark after def:steenrod-powers: (m!)(-1)^m(m!) = (p-1)! = -1, (m!)^2 = (-1)^(m+1) = -(-1/p), '
              '(m!)^4 = 1 (p = %d)' % p)
    # th:steenrod-squares (vii)
    A = SteenrodAlgebra(2)
    ok = True
    for b in range(1, 22):
        for a in range(1, 2 * b):
            if a + b > 22:
                continue
            rhs = sum((binomial(b - 1 - j, a - 2 * j) % 2) * A.Sq(a + b - j) * A.Sq(j) for j in range(a // 2 + 1))
            ok = ok and A.Sq(a) * A.Sq(b) == rhs
    check(ok, 'th:steenrod-squares (vii): the Adem relations for 0 < a < 2b, a + b <= 22 (Sage, Milnor basis)')
    # th:steenrod-powers (vi)
    for p, N in ((3, 12), (5, 8), (7, 6)):
        A = SteenrodAlgebra(p)
        P, b0 = A.P, A.Q(0)
        ok1 = ok2 = ok3 = True
        good = {}
        for b in range(1, N + 1):
            for a in range(1, p * b + 1):
                if a + b > N:
                    continue
                if a < p * b:
                    rhs = sum((-1) ** (a + j) * binomial((p - 1) * (b - j) - 1, a - p * j) * P(a + b - j) * P(j)
                              for j in range(a // p + 1))
                    ok1 = ok1 and P(a) * P(b) == rhs
                rhs = (sum((-1) ** (a + j) * binomial((p - 1) * (b - j), a - p * j) * b0 * P(a + b - j) * P(j)
                           for j in range(a // p + 1)) +
                       sum((-1) ** (a + j - 1) * binomial((p - 1) * (b - j) - 1, a - p * j - 1) * P(a + b - j) * b0 * P(j)
                           for j in range((a - 1) // p + 1)))
                good[(a, b)] = P(a) * b0 * P(b) == rhs
                if a <= b:
                    ok2 = ok2 and good[(a, b)]
                ok3 = ok3 and good[(a, b)]
        check(ok1, 'th:steenrod-powers (vi): P^a P^b for a < pb, a + b <= %d (p = %d)' % (N, p))
        check(ok2, 'th:steenrod-powers (vi) as printed: P^a beta P^b for a <= b, a + b <= %d (p = %d)' % (N, p))
        check(ok3, 'th:steenrod-powers (vi) corrected: P^a beta P^b for a <= pb, a + b <= %d (p = %d)' % (N, p))
        check(good[(2, 1)] and 1 < 2 <= p * 1,
              'th:steenrod-powers (vi): P^2 beta P^1 (a = 2 > b = 1, a <= pb), not admissible (that needs '
              'a >= pb + 1), has the relation with a <= pb, which the printed a <= b does not give (p = %d)' % p)
    # Cartan formulas as coproducts
    A2 = SteenrodAlgebra(2)
    for k in range(0, 13):
        want = sum(A2.Sq(i).tensor(A2.Sq(k - i)) for i in range(k + 1))
        check(A2.Sq(k).coproduct() == want,
              'th:steenrod-squares (v): coproduct of Sq^%d is sum Sq^i (x) Sq^j (Cartan formula)' % k)
    for p in (3, 5):
        Ap = SteenrodAlgebra(p)
        for k in range(0, 7):
            want = sum(Ap.P(i).tensor(Ap.P(k - i)) for i in range(k + 1))
            check(Ap.P(k).coproduct() == want, 'th:steenrod-powers (v): coproduct of P^%d (p = %d)' % (k, p))
        check(Ap.Q(0).coproduct() == Ap.Q(0).tensor(Ap.one()) + Ap.one().tensor(Ap.Q(0)),
              'lem:bockstein-product: beta is primitive (a derivation with the sign (-1)^deg) (p = %d)' % p)

    # the action on H^*(V): p = 2, V of rank 3
    monos = [m for d in range(0, 7) for m in itertools.product(range(7), repeat=3) if sum(m) == d]
    ok_ax = ok_adem = ok_b = True
    for mono in monos:
        f = {mono: 1}
        r = sum(mono)
        ok_ax = ok_ax and sq(0, f) == f and sq(r, f) == clean({tuple(2 * e for e in mono): 1}, 2) and \
            all(sq(i, f) == {} for i in range(r + 1, r + 4))
        ok_b = ok_b and sq(1, f) == beta2(f)
        for b in range(1, 5):
            for a in range(1, 2 * b):
                lhs = sq(a, sq(b, f))
                rhs = {}
                for j in range(a // 2 + 1):
                    if binomial(b - 1 - j, a - 2 * j) % 2:
                        for k2, c in sq(a + b - j, sq(j, f)).items():
                            addto(rhs, k2, c)
                ok_adem = ok_adem and lhs == clean(rhs, 2)
    check(ok_ax, 'th:steenrod-squares (ii)-(iv) on H^*((Z/2)^3, F_2), monomials of degree <= 6')
    check(ok_b, 'th:steenrod-squares (vi): Sq^1 = beta on H^*((Z/2)^3, F_2)')
    check(ok_adem, 'th:steenrod-squares (vii) on H^*((Z/2)^3, F_2): Adem relations, b <= 4, degree <= 6')
    for p in (3, 5):
        D = 8
        monos = [(e1, e2, k1, k2) for e1 in (0, 1) for e2 in (0, 1) for k1 in range(D) for k2 in range(D)
                 if e1 + e2 + 2 * (k1 + k2) <= D]
        ok_ax = ok_adem = True
        for mono in monos:
            f = {mono: 1}
            r = deg_odd(mono)
            ok_ax = ok_ax and pw(p, 0, f) == f and all(pw(p, i, f) == {} for i in range(r // 2 + 1, r // 2 + 3))
            if r % 2 == 0 and mono[0] == mono[1] == 0:
                ok_ax = ok_ax and pw(p, r // 2, f) == {(0, 0, p * mono[2], p * mono[3]): 1}
            for b in range(1, 3):
                for a in range(1, p * b + 1):
                    if a < p * b:
                        lhs = pw(p, a, pw(p, b, f))
                        rhs = {}
                        for j in range(a // p + 1):
                            c = (-1) ** (a + j) * binomial((p - 1) * (b - j) - 1, a - p * j)
                            for k2, v in pw(p, a + b - j, pw(p, j, f)).items():
                                addto(rhs, k2, c * v)
                        ok_adem = ok_adem and lhs == clean(rhs, p)
                    lhs = pw(p, a, bt(p, pw(p, b, f)))
                    rhs = {}
                    for j in range(a // p + 1):
                        c = (-1) ** (a + j) * binomial((p - 1) * (b - j), a - p * j)
                        for k2, v in bt(p, pw(p, a + b - j, pw(p, j, f))).items():
                            addto(rhs, k2, c * v)
                    for j in range((a - 1) // p + 1):
                        c = (-1) ** (a + j - 1) * binomial((p - 1) * (b - j) - 1, a - p * j - 1)
                        for k2, v in pw(p, a + b - j, bt(p, pw(p, j, f))).items():
                            addto(rhs, k2, c * v)
                    ok_adem = ok_adem and lhs == clean(rhs, p)
        check(ok_ax, 'th:steenrod-powers (ii)-(iv) on H^*((Z/%d)^2, F_p), degree <= %d' % (p, D))
        check(ok_adem, 'th:steenrod-powers (vi) (a <= pb) on H^*((Z/%d)^2, F_p), b <= 2, degree <= %d' % (p, D))


# ---------------------------------------------------------------------------
# Section 4.5

def words(p, n):
    L = p + n
    out = []

    def rec(w):
        if len(w) == L:
            if len(set(w)) == p:
                out.append(tuple(w))
            return
        for a in range(1, p + 1):
            if not w or w[-1] != a:
                rec(w + [a])
    rec([])
    return out


def all_words(p, L, surjective=None):
    out = []

    def rec(w):
        if len(w) == L:
            if surjective is None or (len(set(w)) == p) == surjective:
                out.append(tuple(w))
            return
        for a in range(1, p + 1):
            if not w or w[-1] != a:
                rec(w + [a])
    rec([])
    return out


def valid(w, p):
    return len(set(w)) == p and all(w[i] != w[i + 1] for i in range(len(w) - 1))


def dX(w, p, shift, ok=None):
    """sum_i (-1)^(i + shift) (delete the i-th entry), i = 1..len; shift 0: printed (-1)^i,
    shift 1: (-1)^(i-1); terms failing `ok` (default: the conditions of X) are zero."""
    ok = ok or (lambda v: valid(v, p))
    out = {}
    for i in range(1, len(w) + 1):
        v = w[:i - 1] + w[i:]
        if v and ok(v):
            addto(out, v, (-1) ** (i + shift))
    return clean(out)


def hX(w):
    return {(1,) + w: 1} if w[0] != 1 else {}


def lin(f, d):
    out = {}
    for k, c in d.items():
        for k2, c2 in f(k).items():
            addto(out, k2, c * c2)
    return clean(out)


def homology_dims(basis, dfun, F, degrees):
    """dims of homology of a complex given by bases[deg] and d : deg -> deg - 1."""
    idx = {n: {w: k for k, w in enumerate(basis[n])} for n in basis}
    rk = {}
    for n in basis:
        if n - 1 in basis and basis[n] and basis[n - 1]:
            M = matrix(F, len(basis[n - 1]), len(basis[n]), sparse=True)
            for c, w in enumerate(basis[n]):
                for v, s in dfun(w).items():
                    M[idx[n - 1][v], c] += s
            rk[n] = M.rank()
        else:
            rk[n] = 0
    return {n: len(basis[n]) - rk.get(n, 0) - rk.get(n + 1, 0) for n in degrees}


def koszul(order):
    s = 0
    for a in range(len(order)):
        for b in range(a + 1, len(order)):
            if order[a][0] > order[b][0]:
                s += order[a][1] * order[b][1]
    return (-1) ** s


def xi(lam, w, p, count=None):
    """the map xi of p. 143 on lam (x) w, w an increasing tuple of vertices (x_0, ..., x_r)."""
    L = len(lam)
    r = len(w) - 1
    out = {}
    for mid in itertools.combinations_with_replacement(range(r + 1), L - 1):
        iseq = (0,) + mid + (r,)
        segs = [(iseq[k - 1], iseq[k]) for k in range(1, L + 1)]
        us, order, ok = [], [], True
        for j in range(1, p + 1):
            ks = [k for k in range(1, L + 1) if lam[k - 1] == j]
            u = []
            for t, k in enumerate(ks):
                a, b = segs[k - 1]
                if t > 0 and not segs[ks[t - 1] - 1][1] < a:
                    ok = False
                u.extend(range(a, b + 1))
                order.append((k, b - a))
            us.append(tuple(w[q] for q in u))
        if not ok:
            continue
        if count is not None:
            count.append(iseq)
        addto(out, tuple(us), koszul(order))
    return clean(out)


def dC(u):
    if len(u) <= 1:
        return {}
    out = {}
    for k in range(len(u)):
        addto(out, u[:k] + u[k + 1:], (-1) ** k)
    return out


def d_tensor(t):
    out = {}
    sign = 1
    for pos, u in enumerate(t):
        for v, c in dC(u).items():
            addto(out, t[:pos] + (v,) + t[pos + 1:], sign * c)
        if (len(u) - 1) % 2:
            sign = -sign
    return clean(out)


def psi(n, w):
    """psi(alpha_n (x) w) of p. 142 (corrected) over F_2: cut points 0 <= i_1 < ... < i_(n+1) <= r, pieces
    [0, i_1], [i_1, i_2], ..., [i_(n+1), r] alternately to the first and the second factor, so that the last
    piece goes to the first factor iff n is odd."""
    r = len(w) - 1
    out = {}
    for cuts in itertools.combinations(range(r + 1), n + 1):
        pts = (0,) + cuts + (r,)
        first, second = [], []
        for k in range(n + 2):
            (first if k % 2 == 0 else second).extend(range(pts[k], pts[k + 1] + 1))
        addto(out, (tuple(w[q] for q in first), tuple(w[q] for q in second)), 1)
    return clean(out, 2)


def section_4_5():
    # --- lem:vanishing-d-j: invariants under F_p^* (twisted by the sign character for r odd) ---
    for p in (3, 5, 7, 11, 13):
        m = (p - 1) // 2
        for rpar in (0, 1):
            inv = set()
            for j in range(1, 8 * p):
                k = (j + 1) // 2            # a_j has weight k: a_(2k) = x^k, a_(2k-1) = y x^(k-1)
                if all(pow(c, k, p) == pow(c, m * rpar, p) for c in range(1, p)):
                    inv.add(j)
            if rpar == 0:
                want = {j for j in range(1, 8 * p) for k in range(1, 9)
                        if j in (2 * k * (p - 1), 2 * k * (p - 1) - 1)}
            else:
                want = {j for j in range(1, 8 * p) for k in range(0, 9)
                        if j in ((2 * k + 1) * (p - 1), (2 * k + 1) * (p - 1) - 1)}
            check(inv == want, 'lem:vanishing-d-j: the image of res_(Sigma_p, Z/p) on H^j(Sigma_p, F_p^((r))) '
                               '(r %s, p = %d)' % ('even' if rpar == 0 else 'odd', p))

    # --- lem:bockstein-d-j: p = 2, D_j = Sq^(r - j) on H^r, tested on H^*((Z/2)^3, F_2) ---
    printed_ok = corrected_ok = True
    for mono in (m for d in range(0, 7) for m in itertools.product(range(7), repeat=3) if sum(m) == d):
        f = {mono: 1}
        r = sum(mono)

        def D(j):
            return sq(r - j, f) if 0 <= j <= r else {}
        for j in range(0, r + 2):
            lhs = beta2(D(j))
            printed = D(j - 1) if j % 2 == 0 else {}
            corrected = D(j - 1) if (j - r) % 2 == 0 else {}
            printed_ok = printed_ok and lhs == printed
            corrected_ok = corrected_ok and lhs == corrected
    check(corrected_ok, 'lem:bockstein-d-j corrected (p = 2): beta D_j = D_(j-1) if j = r mod 2 and 0 otherwise, on '
                        'H^r((Z/2)^3, F_2), r <= 6')
    refuted(printed_ok, 'lem:bockstein-d-j as printed for p = 2: beta D_0 = 0, beta D_(2j) = D_(2j-1), '
                        'beta D_(2j-1) = 0 in all degrees')
    # the instance y in H^1(Z/2, F_2) = F_2[y]: D_1(y) = Sq^0 y = y, beta D_1(y) = y^2
    y = {(1,): 1}
    refuted(beta2(sq(0, y)) == {},
            'lem:bockstein-d-j as printed (p = 2, r = 1): beta D_1(y) = beta(y) = 0 for y in H^1(Z/2, F_2)')
    check(beta2(sq(0, y)) == sq(1, y) == {(2,): 1},
          'lem:bockstein-d-j corrected (p = 2, r = 1): beta D_1(y) = D_0(y) = y^2')
    # p odd: the printed statement agrees with the uniform one (j = (p-1)r = 0 mod 2)
    check(all(((p - 1) * r) % 2 == 0 for p in (3, 5, 7) for r in range(10)),
          'lem:bockstein-d-j: for p odd, j = (p-1)r mod 2 means j even, as printed')

    # --- lem:cartan-d-j: the signs work out ---------------------------------------
    for p in (3, 5, 7, 11, 13):
        m = (p - 1) // 2
        check(all(c_const(p, r + s) == GF(p)((-1) ** (m * r * s)) * c_const(p, r) * c_const(p, s)
                  for r in range(13) for s in range(13)),
              'lem:cartan-d-j: c_(r+s) = (-1)^(m r s) c_r c_s, so the Cartan formula holds for P^k (p = %d)' % p)

    # --- the constants theta_r (p. 144) ---------------------------------------------
    for p in prime_range(3, 200):
        m = (p - 1) // 2
        F = GF(p)
        mf = F(factorial(m))

        def P0(r, th1):
            th = F((-1) ** (r // 2)) * (th1 if r % 2 else 1)
            return th / c_const(p, r)
        good = [t for t in (mf, -mf, 1 / mf, -1 / mf) if all(P0(r, t) == 1 for r in range(13))]
        check(good == [F((-1) ** m) * mf] * len(good) and len(good) >= 1,
              'p. 144: P^0 = 1 in degrees <= 12 iff theta_1 = (-1)^m m! = -1/m! (p = %d)' % p)
        check(F((-1) ** (p * (p - 1) // 2)) * mf ** 2 == -1 and mf ** 2 == -F((-1) ** m),
              'p. 144: (-1)^(p(p-1)/2) theta_1^2 = theta_2 = -1 and ((p-1)/2)!^2 = -(-1)^((p-1)/2) (p = %d)' % p)
        if p % 4 == 3:
            refuted(all(P0(r, mf) == 1 for r in range(13)),
                    'p. 144 as printed: theta_1 = ((p-1)/2)! gives P^0 = 1 (p = %d)' % p)
            check(P0(1, mf) == -1, 'p. 144 as printed: theta_1 = m! gives P^0 = -1 in degree 1 (p = %d)' % p)
        # the first display of Case (ii), p. 146, with r = 1 and zeta = y_2: the coefficient of
        # x_1^m y_2 is c_1 (P^0 = 1, P^i(y) = 0 for i > 0, beta P^0 = beta = -x)
        check(c_const(p, 1) == F((-1) ** m) * mf == -1 / mf,
              'p. 146 corrected: norm(y_2) = c_1 x_1^((p-3)/2)(x_1 y_2 - y_1 x_2), c_1 = (-1)^m m! = -(m!)^-1 (p = %d)' % p)
        refuted(c_const(p, 1) == 1 / mf, 'p. 146 as printed: norm(y_2) = (m!)^-1 x_1^((p-3)/2)(...) (p = %d)' % p)

    # --- the complex X (pp. 142-143) -------------------------------------------------
    for p, nmax in ((2, 4), (3, 4), (5, 1)):
        F = GF(p)
        basis = {n: words(p, n) for n in range(0, nmax + 2)}
        H = homology_dims(basis, lambda w: dX(w, p, 1), F, range(0, nmax + 1))
        check(H[0] == 1 and all(H[n] == 0 for n in range(1, nmax + 1)),
              'p. 142 (with the author\'s correction): H_n(X) = 0 for 1 <= n <= %d, H_0(X) = F_p (p = %d)' % (nmax, p))
        check(all(tuple(a % p + 1 for a in w) != w for n in basis for w in basis[n]) and
              all(tuple(a % p + 1 for a in w) in set(basis[n]) for n in basis for w in basis[n]),
              'p. 142: Z/p acts freely on the basis of X, so the X_n are free F_p(Z/p)-modules (p = %d)' % p)
        # H_0 trivial: the generator moves (1..p) to (2..p,1), whose difference lies in d(X_1)
        idx1 = {w: k for k, w in enumerate(basis[0])}
        M = matrix(F, len(basis[0]), len(basis[1]), sparse=True)
        for c, w in enumerate(basis[1]):
            for v, s in dX(w, p, 1).items():
                M[idx1[v], c] += s
        diff = vector(F, len(basis[0]))
        diff[idx1[tuple(range(2, p + 1)) + (1,)]] += 1
        diff[idx1[tuple(range(1, p + 1))]] -= 1
        check(diff in M.column_space(), 'p. 142: Z/p acts trivially on H_0(X) = F_p (p = %d)' % p)
    if True:
        p = 3
        check([len(words(3, n)) for n in range(5)] == [6, 18, 42, 90, 186],
              'p. 142: ranks of X_n over F_3 are 6, 18, 42, 90, 186 (n <= 4), free of rank 2, 6, 14, 30, 62 '
              'over F_3(Z/3)')
        lam = (3, 1, 3, 1, 2)
        check(dX(lam, 3, 1) == {(1, 3, 1, 2): 1, (3, 1, 3, 2): -1},
              'p. 143 example: d(3,1,3,1,2) = (1,3,1,2) - (3,1,3,2) with the sign (-1)^(i-1)')
        refuted(dX(lam, 3, 0) == {(1, 3, 1, 2): 1, (3, 1, 3, 2): -1},
                'p. 142 as printed: d with (-1)^i gives the example of p. 143')
        for pp in (2, 3):
            for sh in (0, 1):
                check(all(lin(lambda v: dX(v, pp, sh), dX(w, pp, sh)) == {} for n in range(1, 4)
                          for w in words(pp, n)), 'p. 142: d^2 = 0 on X (p = %d, either sign)' % pp)

        def dhhd(w, pp, sh):
            out = lin(lambda v: dX(v, pp, sh), hX(w))
            for v, c in dX(w, pp, sh).items():
                for u, c2 in hX(v).items():
                    if valid(u, pp):
                        addto(out, u, c * c2)
            return clean(out)
        check(all(dhhd(w, 2, 1) == {w: 1} for n in range(1, 5) for w in words(2, n)),
              'p. 142: for p = 2, d h + h d = 1 on X in degrees 1-4 with the sign (-1)^(i-1) (over Z)')
        refuted(all(dhhd(w, 2, 0) == {w: 1} for n in range(1, 5) for w in words(2, n)),
                'p. 142 as printed: d h + h d = 1 with the sign (-1)^i (it is -1 there, over Z)')
        for sh in (0, 1):
            refuted(dhhd((1, 2, 3, 2), 3, sh) == {(1, 2, 3, 2): (-1) ** (1 - sh)} or
                    dhhd((1, 2, 3, 2), 3, sh) == {(1, 2, 3, 2): 1},
                    'p. 142 as printed: d h + h d = +-1 on X for p = 3 ((1,2,3,2) |-> %s)' % dhhd((1, 2, 3, 2), 3, sh))
        # the corrected argument: X~ (all sequences with lambda_i != lambda_(i+1), lengths >= 1) has the
        # homology of a point; X' (some j missing) that of the (p-2)-sphere; X = X~ / X'.
        for pp, Lmax in ((3, 6), (5, 5)):
            F = GF(pp)
            Xt = {L: all_words(pp, L) for L in range(1, Lmax + 2)}
            Ht = homology_dims(Xt, lambda w: dX(w, pp, 1, ok=lambda v: all(v[i] != v[i + 1] for i in range(len(v) - 1))),
                               F, range(1, Lmax + 1))
            check(Ht == {L: (1 if L == 1 else 0) for L in range(1, Lmax + 1)},
                  'p. 142 corrected: the sequences with lambda_i != lambda_(i+1) form a complex with the homology '
                  'of a point (lengths <= %d, p = %d)' % (Lmax, pp))
            Xp = {L: all_words(pp, L, surjective=False) for L in range(1, Lmax + 2)}
            Hp = homology_dims(Xp, lambda w: dX(w, pp, 1, ok=lambda v: len(set(v)) < pp and
                                                all(v[i] != v[i + 1] for i in range(len(v) - 1))),
                               F, range(1, Lmax + 1))
            check(Hp == {L: (1 if L in (1, pp - 1) else 0) for L in range(1, Lmax + 1)},
                  'p. 142 corrected: the sequences missing some j form a subcomplex with the homology of the '
                  '(%d)-sphere (p = %d)' % (pp - 2, pp))

    # --- xi (p. 143) ----------------------------------------------------------------
    cnt = []
    val = xi((3, 1, 3, 1, 2), (0, 1, 2), 3, count=cnt)
    check(cnt == [(0, 0, 1, 2, 2, 2)] and val == {((0, 1, 2), (2,), (0, 1, 2)): 1},
          'p. 143 example: one admissible sequence i = (0,0,1,2,2,2), term (x_0,x_1,x_2) (x) (x_2) (x) '
          '(x_0,x_1,x_2), sign +')
    p = 3
    ok_vanish = ok_diag = True
    for r in range(1, 4):
        for n in range(0, (p - 1) * r + 3):
            s = p * r - n
            if s < 0:
                continue
            w = tuple(range(s + 1))
            for lam in words(p, n):
                terms = [t for t in xi(lam, w, p) if all(len(u) == r + 1 for u in t)]
                if n > (p - 1) * r:
                    ok_vanish = ok_vanish and not terms
                if n == (p - 1) * r:
                    ok_diag = ok_diag and all(t == (w,) * p for t in terms)
    check(ok_vanish, 'p. 143: xi(lambda (x) (x_0..x_s)) has no terms in (C_r)^(x)3 when n > (p-1)r (r <= 3)')
    check(ok_diag, 'p. 144: when n = (p-1)r every such term is +-(x_0..x_r)^(x)3 (r <= 3)')
    lam = (1, 2, 1, 3)
    for sh in (0, 1):
        lhs = lin(d_tensor, xi(lam, (0,), 3))
        rhs = lin(lambda mu: xi(mu, (0,), 3), dX(lam, 3, sh))
        refuted(lhs == rhs, 'p. 143: xi is a chain map (p = 3, d with %s; d xi((1,2,1,3) (x) (x_0)) = %s, '
                            'xi(d(1,2,1,3) (x) (x_0)) = %s)' % (('(-1)^i', '(-1)^(i-1)')[sh], lhs, rhs))
    # psi (p = 2): the corrected parity gives a chain map over F_2
    ok = True
    for n in range(0, 6):
        for r in range(0, 7):
            w = tuple(range(r + 1))
            lhs = clean(lin(d_tensor, psi(n, w)), 2)
            rhs = {}
            if n > 0:
                for (f, sc), c in psi(n - 1, w).items():
                    addto(rhs, (f, sc), c)
                    addto(rhs, (sc, f), c)
            for v, c in dC(w).items():
                for tt, c2 in psi(n, v).items():
                    addto(rhs, tt, c * c2)
            ok = ok and lhs == clean(rhs, 2)
    check(ok, 'p. 142 corrected: psi (first formula for n odd) is a chain map T (x) C(G) -> C(G)^(x)2 over F_2 '
              '(n <= 5, r <= 6)')
    # the printed assignment for n = 0 is the first formula, whose second factor is (x_(i_1), ..., x_(i_(n+1)))
    # = (x_(i_1)): its terms are not those of the Alexander-Whitney map stated in the next sentence
    for r in range(1, 6):
        aw_second = {sc for (f, sc) in psi(0, tuple(range(r + 1)))}
        printed_second = {(i1,) for i1 in range(r + 1)}
        refuted(aw_second == printed_second,
                'p. 142 as printed: psi(alpha_0 (x) -) is the first formula (second factor (x_(i_1))), the '
                'Alexander-Whitney map (r = %d)' % r)
    check(all(psi(0, tuple(range(r + 1))) == clean({(tuple(range(i + 1)), tuple(range(i, r + 1))): 1
                                                           for i in range(r + 1)}, 2) for r in range(7)),
          'p. 142: for n = 0, psi is the Alexander-Whitney map')
    check(all(psi(r, tuple(range(r + 1))) == {(tuple(range(r + 1)), tuple(range(r + 1))): 1}
              for r in range(7)), 'p. 142: psi(alpha_r (x) (x_0..x_r)) = (x_0..x_r) (x) (x_0..x_r)')
    check(all(psi(n, tuple(range(r + 1))) == {} for r in range(6) for n in range(r + 1, r + 4)),
          'p. 142: psi(alpha_n (x) (x_0..x_r)) = 0 for n > r')
    check(all(clean(xi(tuple((1, 2)[k % 2] for k in range(n + 2)), tuple(range(r + 1)), 2), 2) ==
              psi(n, tuple(range(r + 1))) for n in range(0, 5) for r in range(0, 6)),
          'p. 143: for p = 2, xi on (1,2,1,...) agrees with psi (corrected parity)')


# ---------------------------------------------------------------------------
# Section 4.6

def ymul(a, b):
    if set(a) & set(b):
        return None
    seq = list(a) + list(b)
    inv = sum(1 for s in range(len(seq)) for t in range(s + 1, len(seq)) if seq[s] > seq[t])
    return (-1) ** inv, tuple(sorted(seq))


def emul(u, v):
    out = {}
    for ya, ca in u.items():
        for (yb, s), cb in v.items():
            r = ymul(ya, yb)
            if r is not None:
                addto(out, (r[1], s), r[0] * ca * cb)
    return clean(out)


def eadd(u, v, scale=1):
    out = dict(u)
    for k, c in v.items():
        addto(out, k, scale * c)
    return clean(out)


def double_norm(p, theta, r, I, J, K):
    """norm_(1 x Z/p x G, Z/p x Z/p x G) norm_(G, 1 x Z/p x G)(zeta), computed from the first display
    of p. 146 with norm(x_2) = x_2^p - x_1^(p-1) x_2 and norm(y_2) = theta x_1^(m-1)(x_1 y_2 - y_1 x_2);
    symbols A = P^j P^i, B = beta P^j P^i, C = P^j beta P^i, D = beta P^j beta P^i."""
    x1, x2 = K.gens()
    m = (p - 1) // 2
    normx2 = x2 ** p - x1 ** (p - 1) * x2
    normy2 = {(2,): theta * x1 ** m, (1,): -theta * x1 ** (m - 1) * x2}
    total = {}
    for i in range(I + 1):
        ri = r + 4 * m * i
        a_even = {(): c_const(p, r) * (-1) ** i * normx2 ** (m * (r - 2 * i))}
        Nb = {}
        for j in range(J + 1):
            Nb = eadd(Nb, {((), ('A', i, j)): c_const(p, ri) * (-1) ** j * x1 ** (m * (ri - 2 * j)),
                           ((1,), ('B', i, j)): c_const(p, ri) * (-1) ** j * x1 ** (m * (ri - 2 * j) - 1)})
        total = eadd(total, emul(a_even, Nb))
        sgn = (-1) ** (m * (ri + 1))           # prop:norm-properties (i): deg y_2 = 1, deg beta P^i = ri + 1
        a_odd = {k: c_const(p, r) * (-1) ** i * sgn * v * normx2 ** (m * (r - 2 * i) - 1) for k, v in normy2.items()}
        Nb = {}
        for j in range(J + 1):
            Nb = eadd(Nb, {((), ('C', i, j)): c_const(p, ri + 1) * (-1) ** j * x1 ** (m * (ri + 1 - 2 * j)),
                           ((1,), ('D', i, j)): c_const(p, ri + 1) * (-1) ** j * x1 ** (m * (ri + 1 - 2 * j) - 1)})
        total = eadd(total, emul(a_odd, Nb))
    return total


def second_display(p, r, I, J, K, sign34):
    x1, x2 = K.gens()
    m = (p - 1) // 2
    Q = x2 ** p * x1 ** (1 - p) - x2
    pref = GF(p)((-1) ** ((m + 1) * r)) * x1 ** (m * r) * x2 ** (m * r) * (x2 ** (p - 1) - x1 ** (p - 1)) ** (m * r)
    out = {}
    for i in range(I + 1):
        for j in range(J + 1):
            s = GF(p)((-1) ** (i + j)) * pref
            out = eadd(out, {((), ('A', i, j)): s * Q ** (-2 * m * i) * x1 ** (-2 * m * j),
                             ((1,), ('B', i, j)): s * Q ** (-2 * m * i) * x1 ** (-2 * m * j - 1),
                             ((2,), ('C', i, j)): sign34 * s * Q ** (-2 * m * i - 1) * x1 ** (-2 * m * j),
                             ((1,), ('C', i, j)): -sign34 * s * Q ** (-2 * m * i - 1) * x1 ** (-2 * m * j - 1) * x2,
                             ((1, 2), ('D', i, j)): -sign34 * s * Q ** (-2 * m * i - 1) * x1 ** (-2 * m * j - 1)})
    return out, pref, Q


def coeffs_in_degree(p, n, poly_of, ops):
    """sum over (i, j) with i + j = n of poly_of(i, j) * ops(i, j), as a dict monomial -> Steenrod element."""
    out = {}
    for i in range(n + 1):
        j = n - i
        for mono, c in poly_of(i, j).dict().items():
            mono = tuple(mono)
            out[mono] = out.get(mono, 0) + c * ops(i, j)
    return out


def symmetric(d, zero):
    return all(v == d.get((b, a), zero) for (a, b), v in d.items())


def section_4_6():
    # th:symmetric-adem-relations (i)
    A = SteenrodAlgebra(2)
    R = PolynomialRing(GF(2), 's,t')
    s, t = R.gens()
    for n in range(0, 13):
        d = coeffs_in_degree(2, n, lambda i, j: (t ** 2 + s * t) ** j * s ** (2 * i), lambda i, j: A.Sq(j) * A.Sq(i))
        check(symmetric(d, A(0)), 'th:symmetric-adem-relations (i): Sq_(t^2+st) Sq_(s^2) symmetric, degree %d' % n)
    for p, N in ((3, 6), (5, 5)):
        Ap = SteenrodAlgebra(p)
        R = PolynomialRing(GF(p), 's,t')
        s, t = R.gens()
        w = sum(s ** k * t ** (p - k) for k in range(p))
        b0 = Ap.Q(0)
        for n in range(0, N + 1):
            d1 = coeffs_in_degree(p, n, lambda i, j: s ** (p * i) * w ** j, lambda i, j: Ap.P(j) * Ap.P(i))
            d2 = coeffs_in_degree(p, n, lambda i, j: s ** (p * i + 1) * w ** j,
                                  lambda i, j: (b0 * Ap.P(j) - Ap.P(j) * b0) * Ap.P(i))
            check(symmetric(d1, Ap(0)) and symmetric(d2, Ap(0)),
                  'th:symmetric-adem-relations (ii): P(t^p + ... + s^(p-1)t)P(s^p) and s[beta, P(..)]P(s^p) '
                  'symmetric, degree %d (p = %d)' % (n, p))
        anti = all(symmetric(coeffs_in_degree(p, n, lambda i, j: s ** (p * i + 1) * w ** j,
                                              lambda i, j: (b0 * Ap.P(j) + Ap.P(j) * b0) * Ap.P(i)), Ap(0))
                   for n in range(0, N + 1))
        refuted(anti, 'p. 146: s (beta P + P beta)(t^p + ...) P(s^p) is symmetric (what the printed constant '
                      'of norm(y_2) leads to) (p = %d)' % p)

    # Case (i): the display of p. 145 and the substitution
    K2 = PolynomialRing(GF(2), 'x1,x2').fraction_field()
    x1, x2 = K2.gens()
    ok = True
    for r in range(0, 7):
        for k in range(0, 9):
            for j in range(0, 9):
                lhs = (x1 * x2 + x2 ** 2) ** (r - k) * x1 ** (r + k - j)
                rhs = x1 ** r * x2 ** r * (x1 + x2) ** r * (x2 + x1 ** -1 * x2 ** 2) ** (-k) * x1 ** (-j)
                ok = ok and lhs == rhs
    check(ok, 'p. 145: (x_1 x_2 + x_2^2)^(r-k) x_1^(r+k-j) = x_1^r x_2^r (x_1 + x_2)^r (x_2 + x_1^-1 x_2^2)^-k x_1^-j')
    S2 = PolynomialRing(GF(2), 's,t').fraction_field()
    s, t = S2.gens()
    X1, X2 = 1 / (t * (s + t)), 1 / (s * (s + t))
    check((X2 + X1 ** -1 * X2 ** 2) ** -1 == s ** 2 and X1 ** -1 == t ** 2 + s * t
          and (X1 * X2 * (X1 + X2)) == (X1 * X2 * (X1 + X2)).subs({s: t, t: s}),
          'p. 145: x_1^-1 = t(s+t), x_2^-1 = s(s+t) give (x_2 + x_1^-1 x_2^2)^-1 = s^2, x_1^-1 = t^2 + st, '
          'and x_1^r x_2^r (x_1+x_2)^r is symmetric')
    # residue for p = 2: coefficient of t^-1 in (t+1)^(b-j-1) t^(2j-a-1) is binom(b-1-j, a-2j)
    Rt = PolynomialRing(GF(2), 't')
    T = Rt.gen()
    check(all(((T + 1) ** (b - j - 1)).monomial_coefficient(T ** (a - 2 * j)) == binomial(b - 1 - j, a - 2 * j) % 2
              for b in range(1, 12) for a in range(1, 2 * b) for j in range(a // 2 + 1)),
          'p. 145: the residue gives binom(b - 1 - j, a - 2j)')

    # Case (ii): the double norm (p. 146)
    for p in (3, 5, 7):
        m = (p - 1) // 2
        F = GF(p)
        mf = F(factorial(m))
        Kp = PolynomialRing(F, 'x1,x2').fraction_field()
        x1, x2 = Kp.gens()
        R_, I_, J_ = 4, 2, 2
        ok_print = ok_corr = ok_b = ok_b_print = True
        for r in range(R_ + 1):
            tot_print = double_norm(p, 1 / mf, r, I_, J_, Kp)
            tot_corr = double_norm(p, -1 / mf, r, I_, J_, Kp)
            disp_print, pref, Q = second_display(p, r, I_, J_, Kp, 1)
            disp_corr, _, _ = second_display(p, r, I_, J_, Kp, -1)
            ok_print = ok_print and eadd(tot_print, disp_print, -1) == {}
            ok_corr = ok_corr and eadd(tot_corr, disp_corr, -1) == {}
            for i in range(I_ + 1):
                for j in range(J_ + 1):
                    for tot, flag in ((tot_corr, 'corr'), (tot_print, 'print')):
                        cb = x1 ** p * tot.get(((1,), ('B', i, j)), 0) / pref
                        cc = (x1 ** p * tot.get(((1,), ('C', i, j)), 0) + x2 ** p * tot.get(((2,), ('C', i, j)), 0)) / pref
                        want = F((-1) ** (i + j)) * Q ** (-2 * m * i) * x1 ** (-2 * m * (j - 1))
                        if flag == 'corr':
                            ok_b = ok_b and cb == want and cc == -want
                        else:
                            ok_b_print = ok_b_print and cb == want and cc == want
        check(ok_print, 'p. 146: with the printed norm(y_2) = (m!)^-1 ... the two displays agree (p = %d)' % p)
        check(ok_corr, 'p. 146 corrected: with norm(y_2) = -(m!)^-1 ... the displays agree after changing the signs '
                       'of the last two lines (p = %d)' % p)
        check(ok_b, 'p. 146 corrected: x_1^p (coefficient of y_1) + x_2^p (coefficient of y_2) gives (b) = sum '
                    '(-1)^(i+j) (...)^(-2mi) x_1^(-2m(j-1)) (beta P^j P^i - P^j beta P^i) (p = %d)' % p)
        check(ok_b_print, 'p. 146: the printed constant would give beta P^j P^i + P^j beta P^i in (b), refuted '
                          'above (p = %d)' % p)
        # substitutions of p. 147
        S = PolynomialRing(F, 's,t')
        s, t = S.gens()
        w = sum(s ** k * t ** (p - k) for k in range(p))
        A1 = -t * (s - t) ** (p - 1)                 # x_1^-(p-1) = x_1^-2m
        B1 = -s * (t - s) ** (p - 1)                 # x_2^-(p-1)
        Sf = S.fraction_field()
        # (x_2^p x_1^(1-p) - x_2)^(-(p-1)) = x_2^(-p(p-1)) / (x_1^-(p-1) - x_2^-(p-1))^(p-1) * ... = B1^p / (A1 - B1)^(p-1)
        check(A1 == -w and Sf(B1 ** p) / Sf((A1 - B1) ** (p - 1)) == -s ** p and A1 - B1 == (s - t) ** p,
              'p. 147: x_1^-2m = -t(s-t)^2m = -(t^p + s t^(p-1) + ... + s^(p-1) t), (x_2^p x_1^(1-p) - x_2)^-2m = -s^p '
              '(p = %d)' % p)
        check(s * w == s * t * sum(s ** k * t ** (p - 1 - k) for k in range(p)),
              'p. 147: s t (s^(p-1) + ... + t^(p-1)) = s (t^p + ... + s^(p-1) t) (p = %d)' % p)
        Rt = PolynomialRing(F, 't')
        T = Rt.gen()
        u = sum(T ** k for k in range(p))
        check(u == (1 - T) ** (p - 1), 'p. 147: u = t^(p-1) + ... + 1 = (1 - t)^(p-1) (p = %d)' % p)
        # specialisations at s = 1, degree by degree in the Steenrod algebra
        Ap = SteenrodAlgebra(p)
        b0 = Ap.Q(0)
        Pp = Ap.P
        okS = True
        for n in range(0, 5):
            lhs1 = {}
            rhs1 = {}
            lhs2 = {}
            rhs2 = {}
            for a in range(n + 1):
                bb = n - a
                for e, c in enumerate(((T * u) ** a).list()):
                    lhs1[e] = lhs1.get(e, 0) + c * Pp(a) * Pp(bb)
                    lhs2[e] = lhs2.get(e, 0) + c * Pp(a) * b0 * Pp(bb)
            for j in range(n + 1):
                poly = u ** (n - j) * T ** (p * j)
                for e, c in enumerate(poly.list()):
                    rhs1[e] = rhs1.get(e, 0) + c * Pp(n - j) * Pp(j)
                for e, c in enumerate((poly * (1 - T)).list()):
                    rhs2[e] = rhs2.get(e, 0) + c * b0 * Pp(n - j) * Pp(j)
                for e, c in enumerate((poly * T).list()):
                    rhs2[e] = rhs2.get(e, 0) + c * Pp(n - j) * b0 * Pp(j)
            keys1 = set(lhs1) | set(rhs1)
            keys2 = set(lhs2) | set(rhs2)
            okS = okS and all(lhs1.get(e, Ap(0)) == rhs1.get(e, Ap(0)) for e in keys1) and \
                all(lhs2.get(e, Ap(0)) == rhs2.get(e, Ap(0)) for e in keys2)
        check(okS, 'p. 147: P(tu)P(1) = P(u)P(t^p) and P(tu) beta P(1) = ((1-t) beta P(u) + t P(u) beta) P(t^p), '
                   'degrees n <= 4 (p = %d)' % p)
        # the residues: coefficient of t^-1 gives the binomials of th:steenrod-powers (vi)
        okR = True
        for b in range(1, 6):
            for a in range(1, p * b + 1):
                for j in range(a // p + 1):
                    if a < p * b:
                        e = (p - 1) * (b - j) - 1
                        okR = okR and ((1 - T) ** e).monomial_coefficient(T ** (a - p * j)) == \
                            F((-1) ** (a + j) * binomial(e, a - p * j))
                    e = (p - 1) * (b - j)
                    okR = okR and ((1 - T) ** e).monomial_coefficient(T ** (a - p * j)) == \
                        F((-1) ** (a + j) * binomial(e, a - p * j))
                for j in range((a - 1) // p + 1):
                    e = (p - 1) * (b - j) - 1
                    okR = okR and ((1 - T) ** e).monomial_coefficient(T ** (a - p * j - 1)) == \
                        F((-1) ** (a + j - 1) * binomial(e, a - p * j - 1))
        check(okR, 'p. 148: the residues give the coefficients of th:steenrod-powers (vi) (p = %d, b <= 5)' % p)


# ---------------------------------------------------------------------------
# Mod p cohomology of p-groups from minimal resolutions

class PGroupCohomology:
    def __init__(self, G, p):
        self.G, self.p, self.F = G, p, GF(p)
        self.els = list(G.AsList())
        self.n = len(self.els)
        L = libgap.List(self.els)
        self.mult = [[int(libgap.Position(L, a * b)) - 1 for b in self.els] for a in self.els]
        self.e = [i for i, x in enumerate(self.els) if x == G.Identity()][0]
        self.gens = [int(libgap.Position(L, g)) - 1 for g in G.GeneratorsOfGroup()]
        self.ranks = [1]
        self.d = {}
        self.gen_images = {}

    def act(self, g, v, r):
        n = self.n
        out = [0] * (n * r)
        mg = self.mult[g]
        for j in range(r):
            base = j * n
            for i in range(n):
                c = v[base + i]
                if c:
                    out[base + mg[i]] += c
        return vector(self.F, out)

    def hom_matrix(self, images, r_src, r_tgt):
        cols = [self.act(i, images[j], r_tgt) for j in range(r_src) for i in range(self.n)]
        return matrix(self.F, cols).transpose() if cols else zero_matrix(self.F, self.n * r_tgt, 0)

    def extend(self, N):
        n, F = self.n, self.F
        while len(self.ranks) <= N:
            k = len(self.ranks)
            if k == 1:
                K = matrix(F, 1, n, [1] * n).right_kernel_matrix()
                r_prev = 1
            else:
                K = self.d[k - 1].right_kernel_matrix()
                r_prev = self.ranks[k - 1]
            rows = K.rows()
            IK = [self.act(g, v, r_prev) - v for g in self.gens for v in rows]
            V = F ** (n * r_prev)
            cur = V.subspace(IK)
            gens = []
            for v in rows:
                if v not in cur:
                    gens.append(v)
                    cur = V.subspace(list(cur.basis()) + [v])
            self.gen_images[k] = gens
            self.d[k] = self.hom_matrix(gens, len(gens), r_prev)
            self.ranks.append(len(gens))

    def lift(self, u, k, upto):
        F, n = self.F, self.n
        self.extend(k + upto)
        one = vector(F, [1 if i == self.e else 0 for i in range(n)])
        U = [self.hom_matrix([u[j] * one for j in range(self.ranks[k])], self.ranks[k], 1)]
        for t in range(1, upto + 1):
            Rm = matrix(F, [U[t - 1] * dv for dv in self.gen_images[k + t]]).transpose()
            X = self.d[t].solve_right(Rm)
            U.append(self.hom_matrix(X.columns(), self.ranks[k + t], self.ranks[t]))
        return U

    def product(self, v, s, U, k):
        n = self.n
        M = U[s]
        out = []
        for j in range(self.ranks[s + k]):
            col = M.column(j * n + self.e)
            out.append(sum(v[jj] * sum(col[jj * n + i] for i in range(n)) for jj in range(self.ranks[s])))
        return vector(self.F, out)

    def h1(self):
        G = self.G
        hom = libgap.NaturalHomomorphismByNormalSubgroup(G, G.FrattiniSubgroup())
        pcgs = libgap.Pcgs(libgap.Image(hom))
        return [[int(c) for c in libgap.ExponentsOfPcElement(pcgs, libgap.Image(hom, x))] for x in self.els]

    def bockstein(self, yvals):
        p, n = self.p, self.n
        self.extend(2)
        phi1 = [{h: int(v[h]) for h in range(n) if v[h]} for v in self.gen_images[1]]
        vals = []
        for v in self.gen_images[2]:
            tot = 0
            for j in range(self.ranks[1]):
                for i in range(n):
                    c = int(v[j * n + i])
                    if c:
                        for h, c2 in phi1[j].items():
                            tot += c * c2 * ((yvals[i] + yvals[h] - yvals[self.mult[i][h]]) // p)
            vals.append(tot % p)
        return vector(self.F, vals)

    def bockstein_product(self, ys):
        betas = [self.bockstein(y) for y in ys]
        v, s = betas[0], 2
        for b in betas[1:]:
            v = self.product(v, s, self.lift(b, 2, s), 2)
            s += 2
        return v


def lines_of(p, d):
    return [c for c in itertools.product(range(p), repeat=d)
            if any(c) and c[[k for k in range(d) if c[k]][0]] == 1]


def section_4_7():
    # group theory of Lemma 4.7.1 and Theorem 4.7.3 (GAP)
    for p in (2, 3, 5, 7):
        for i in range(1, int(libgap.NumberSmallGroups(p ** 3)) + 1):
            G = libgap.SmallGroup(p ** 3, i)
            Phi = G.FrattiniSubgroup()
            if int(Phi.Size()) != p:
                check(G.IsElementaryAbelian() or G.IsCyclic(),
                      'Lemma 4.7.1: |Phi(G)| != p for |G| = p^3 only if G is elementary abelian or cyclic')
                continue
            check(not G.IsAbelian() or int(libgap.Exponent(G)) == p ** 2,
                  'Lemma 4.7.1: |Phi(G)| = p: G = Z/p^2 x Z/p or non-abelian (p = %d)' % p)
            if int(libgap.Exponent(G)) == p ** 2:
                check(any(int(x.Order()) == p ** 2 for x in G.AsList()),
                      'Lemma 4.7.1 (a): G has a cyclic maximal subgroup of order p^2 (p = %d)' % p)
                continue
            # case (b): exponent p, p odd
            found = False
            for g in G.GeneratorsOfGroup():
                for h in G.AsList():
                    if int(h.Order()) != p or libgap.Subgroup(G, [g, h]).Size() != G.Size():
                        continue
                    z = libgap.Comm(g, h)
                    if z in G.Centre() and int(z.Order()) == p:
                        H = libgap.Subgroup(G, [h, z])
                        # conjugation by g on H/Phi... H = <h, z>: g^-1 h g = h z^e, z fixed
                        hg = h ** g
                        e = [k for k in range(p) if hg == h * z ** k]
                        found = H.IsElementaryAbelian() and int(H.Size()) == p ** 2 and e and e[0] != 0
                        break
                if found:
                    break
            check(p > 2 and found, 'Lemma 4.7.1 (b): G = <g, h> of exponent p, z = [g, h] central of order p, '
                                   'H = <h, z> elementary abelian, g acts on H by a transvection (p = %d)' % p)
    for p, nmax in ((2, 6), (3, 5), (5, 4)):
        for n in range(3, nmax + 1):
            ok = True
            for i in range(1, int(libgap.NumberSmallGroups(p ** n)) + 1):
                G = libgap.SmallGroup(p ** n, i)
                Phi = G.FrattiniSubgroup()
                if int(Phi.Size()) == 1:
                    continue
                Ns = [N for N in libgap.NormalSubgroups(G) if libgap.IsSubgroup(Phi, N) and
                      int(Phi.Size()) == p * int(N.Size())]
                ok = ok and len(Ns) > 0
                N = Ns[0]
                Q = libgap.FactorGroup(G, N)
                ok = ok and int(Q.FrattiniSubgroup().Size()) == p
                if int(Phi.Size()) == p:
                    if int(libgap.Index(G, Phi)) == p:
                        ok = ok and G.IsCyclic()
                    elif not G.IsCyclic():
                        Hs = [H.Representative() for H in G.ConjugacyClassesSubgroups()
                              if int(H.Representative().Size()) == p ** 3]
                        Hs = [H for H in Hs if libgap.IsSubgroup(H, Phi) and H.FrattiniSubgroup() == Phi]
                        ok = ok and len(Hs) > 0
                        if Hs:
                            idx = int(libgap.Index(G, Hs[0]))
                            iphi = int(libgap.Index(G, Phi))
                            ok = ok and QQ(p + 1) * idx == QQ(p + 1) / p ** 2 * iphi
            check(ok, 'th:serre-bocksteins: the reductions of the proof hold for all groups of order %d^%d '
                      '(N, G/Phi cyclic => G cyclic, H of order p^3 with Phi(H) = Phi(G), (p+1)|G:H| = '
                      '((p+1)/p^2)|G:Phi(G)|)' % (p, n))
    for p in (2, 3, 5):
        refuted(QQ(p) + QQ(1) / p ** 2 == QQ(p + 1) / p ** 2,
                'proof of th:serre-bocksteins as printed: (p + 1/p^2) |G : Phi(G)| (p = %d)' % p)
    for p in (2, 3, 5, 7, 11, 13):
        R = PolynomialRing(GF(p), 'v1,v2')
        v1, v2 = R.gens()
        check(R.prod(v2 + lam * v1 for lam in GF(p)) == v2 ** p - v1 ** (p - 1) * v2,
              'Lemma 4.7.1 and the Remark after lem:norm-bockstein-product: prod_lambda (v_2 + lambda v_1) = '
              'v_2^p - v_1^(p-1) v_2; times v_1 it is the product over all p + 1 lines (p = %d)' % p)

    # cohomology computations
    for (o, i), expect in (((4, 2), False), ((8, 2), True), ((8, 3), True), ((8, 4), True),
                           ((9, 2), False), ((27, 2), True), ((27, 3), True), ((27, 4), True)):
        G = libgap.SmallGroup(o, i)
        p = int(libgap.FactorsInt(o)[0])
        C = PGroupCohomology(G, p)
        coords = C.h1()
        d = len(coords[0])
        ys = {c: [sum(a * b for a, b in zip(c, coords[g])) % p for g in range(C.n)] for c in lines_of(p, d)}
        prod = C.bockstein_product([ys[c] for c in lines_of(p, d)])
        name = str(G.StructureDescription())
        if expect:
            check(not any(prod), 'lem:serre-order-p-cubed: the product of the Bocksteins of one element from each '
                                 'of the %d lines of H^1(%s, F_p) vanishes' % (p + 1, name))
            if G.IsAbelian() or any(int(x.Order()) == p ** 2 for x in G.AsList()):
                found = any(not any(C.bockstein_product([[(ys[c1][g] * lam + ys[c2][g]) % p for g in range(C.n)]
                                                          for lam in range(p)]))
                            for c1 in lines_of(p, d) for c2 in lines_of(p, d) if c1 != c2)
                check(found, 'proof of lem:serre-order-p-cubed (a): prod_lambda beta(y_2 + lambda y_1) = 0 for '
                             'suitable generators y_1, y_2 of H^1(%s, F_p)' % name)
        else:
            check(any(prod), 'Section 4.7: for (Z/%d)^2 the product of the Bocksteins over all lines of H^1 is '
                             'non-zero' % p)
    # 2-generator groups of order 16 (|G : Phi| = 4): a product of at most 3 Bocksteins vanishes
    for i in range(1, 15):
        G = libgap.SmallGroup(16, i)
        if int(libgap.Index(G, G.FrattiniSubgroup())) != 4 or G.IsCyclic():
            continue
        C = PGroupCohomology(G, 2)
        coords = C.h1()
        ys = [[sum(a * b for a, b in zip(c, coords[g])) % 2 for g in range(C.n)] for c in lines_of(2, 2)]
        check(not any(C.bockstein_product(ys)),
              'th:serre-bocksteins: for %s (|G : Phi(G)| = 4) the 3 Bocksteins of the non-zero elements of H^1 '
              'have product 0' % str(G.StructureDescription()))
    # Q_8 x Z/2: the 6 Bocksteins of the proof (elements of H^1(G) not vanishing on H = Q_8)
    G = libgap.SmallGroup(16, 12)
    C = PGroupCohomology(G, 2)
    coords = C.h1()
    H = [Hc.Representative() for Hc in G.ConjugacyClassesSubgroups()
         if int(Hc.Representative().Size()) == 8 and str(Hc.Representative().StructureDescription()) == 'Q8'][0]
    inH = [x in H for x in C.els]
    chosen = []
    for c in lines_of(2, 3):
        y = [sum(a * b for a, b in zip(c, coords[g])) % 2 for g in range(C.n)]
        if any(y[g] for g in range(C.n) if inH[g]):
            chosen.append(y)
    check(len(chosen) == 6 and not any(C.bockstein_product(chosen)),
          'th:serre-bocksteins for Q8 x C2: the 6 = ((p+1)/p^2)|G : Phi(G)| Bocksteins of the elements not '
          'vanishing on Q8 have product 0 in H^12')


# ---------------------------------------------------------------------------
# Section 4.8

def admissible_excess_lt(k, maxlen=6):
    """admissible sequences (s_1, ..., s_l) (s_i >= 2 s_(i+1), s_l >= 1) of excess
    e = s_1 - s_2 - ... - s_l < k."""
    out = []

    def rec(seq):
        if seq and 2 * seq[0] - sum(seq) < k:
            out.append(tuple(seq))
        if len(seq) >= maxlen:
            return
        last = seq[0] if seq else None
        for s in range(1, 2 ** maxlen + 1):
            if last is None or s >= 2 * last:
                if 2 * s - sum(seq) - s < k:
                    rec([s] + seq)
    rec([])
    return out


def section_4_8():
    for n in range(1, 8):
        for p in (3, 5, 7):
            # transgression d_r : E^(a,b) -> E^(a+r, b-r+1)
            a, b, rr = 2 * n + 1, 2 * n * (p - 1), 2 * n * (p - 1) + 1
            check((a + rr, b - rr + 1) == (2 * n * p + 2, 0) and 2 * n + 1 + 2 * n * (p - 1) + 1 == 2 * n * p + 2,
                  'p. 151 corrected: d_(2n(p-1)+1)(x^(p-1) y) lies in E^(2np+2, 0), the degree of beta P^n(y) '
                  '(n = %d, p = %d)' % (n, p))
            check((0 + 2 * n * p + 1, 2 * n * p - 2 * n * p - 1 + 1) == (2 * n * p + 1, 0) and
                  2 * n + 1 + 2 * n * (p - 1) == 2 * n * p + 1,
                  'p. 151: d_(2np+1)(x^p) = P^n(y) in E^(2np+1, 0) (n = %d, p = %d)' % (n, p))
        for r in range(0, 5):
            check((0 + n + r, n - 1 + r - (n + r) + 1) == (n + r, 0),
                  'th:steenrod-transgression: d_(n+r) : E^(0, n+r-1) -> E^(n+r, 0) (n = %d, r = %d)' % (n, r))
    seqs = admissible_excess_lt(2)
    want = [tuple(2 ** (i - 1 - k) for k in range(i)) for i in range(1, 7)]
    check(sorted(seqs) == sorted(want),
          'p. 151: the admissible sequences of excess < 2 are (2^(i-1), ..., 2, 1) (Serre; McCleary Thm 6.19)')
    check(all(2 + sum(s) == 2 ** len(s) + 1 for s in want) and
          all((2 ** i + 1) + 2 ** i == 2 ** (i + 1) + 1 for i in range(8)),
          'p. 151: u_i = Sq^(2^(i-1)) ... Sq^1 zeta has degree 2^i + 1 and Sq^(2^i) u_i has the degree of u_(i+1)')

    # transgressions in small central extensions 1 -> Z/2 -> G -> G/Z -> 1 (p = 2)
    for (o, i) in ((4, 1), (8, 2), (8, 3), (8, 4)):
        G = libgap.SmallGroup(o, i)
        C = PGroupCohomology(G, 2)
        C.extend(8)
        dims = C.ranks[:9]
        Z = libgap.Subgroup(G, [z for z in G.FrattiniSubgroup().AsList() if int(z.Order()) == 2][:1])
        Q = libgap.FactorGroup(G, Z)
        hom = libgap.NaturalHomomorphismByNormalSubgroup(G, Z)
        pcgs = libgap.Pcgs(libgap.Image(hom))
        k = int(libgap.Length(pcgs))
        lifts = [libgap.PreImagesRepresentative(hom, pcgs[j]) for j in range(k)]
        zgen = list(Z.GeneratorsOfGroup())[0]
        # zeta = sum q(e_j) x_j^2 + sum_(j<l) b(e_j, e_l) x_j x_l (squares and commutators of lifts)
        R = PolynomialRing(GF(2), k, 'x')     # multivariate even when k = 1
        X = R.gens()
        zeta = sum((1 if lifts[j] ** 2 == zgen else 0) * X[j] ** 2 for j in range(k)) + \
            sum((1 if libgap.Comm(lifts[j], lifts[l]) == zgen else 0) * X[j] * X[l]
                for j in range(k) for l in range(j + 1, k))

        def sq_poly(kk, f):
            out = R(0)
            for mono, c in f.dict().items():
                for m2, c2 in sq_mono(kk, tuple(mono)).items():
                    out += c * c2 * R.monomial(*m2)
            return out
        sq1z = sq_poly(1, zeta)
        sq21z = sq_poly(2, sq1z)
        # E_3 = F_2[x]/(zeta) (x) F_2[u^2] (zeta a non-zero-divisor); d_3(u^2) = Sq^1 zeta;
        # if Sq^1 zeta = 0 mod zeta, everything survives; otherwise E_4 = F_2[x]/(zeta, Sq^1 zeta) (x) F_2[u^4]
        # and d_5(u^4) = Sq^2 Sq^1 zeta (zero here for degree reasons)
        I1 = R.ideal([zeta])
        I2 = R.ideal([zeta, sq1z])

        def hilb(I, N):
            return [len([m for m in (R.monomial(*e) for e in itertools.product(range(N + 1), repeat=k)
                                     if sum(e) == dd) if I.reduce(m) == m]) if k else 1 for dd in range(N + 1)]
        if I1.reduce(sq1z) == 0:
            base, per = hilb(I1, 8), 2
        else:
            check(I2.dimension() == 0 and I2.reduce(sq21z) == 0,
                  'th:steenrod-transgression: zeta, Sq^1 zeta is a regular sequence and d_5(u^4) = Sq^2 Sq^1 zeta = 0 '
                  'in E_5^(5,0) (%s)' % str(G.StructureDescription()))
            base, per = hilb(I2, 8), 4
        series = [sum(base[dd - per * j] for j in range(dd // per + 1)) for dd in range(9)]
        check(series == list(dims),
              'th:steenrod-transgression: for %s, d_2(u) = zeta = %s, d_3(u^2) = Sq^1 zeta = %s give dim H^n = %s '
              '(n <= 8), as computed from a minimal resolution' % (str(G.StructureDescription()), zeta, sq1z, dims))


def main():
    section_4_4()
    section_4_5()
    section_4_6()
    section_4_7()
    section_4_8()
    print('ok chapter-4b: %d checks' % COUNT[0])


if __name__ == '__main__':
    main()
