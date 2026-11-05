#import "main-defs.typ": *
#import "statements.typ": *

== Products in spectral sequences <sec:spectral-products>
#idx("products", "in spectral sequences", target: [@sec:spectral-products])#idx(
  "spectral sequence",
  "products in",
  target: [@sec:spectral-products],
)

#source(127)We shall show in this section how product structures on double
complexes or filtered complexes give rise to products in the entire spectral
sequence in a useful way. For an alternative approach to products using exact
couples, see Massey [@bib:Massey1954]. The theory of products in exact couples
is not quite as straightforward as one might hope.

#definition[
  A *pairing*#idx("pairing", "of double complexes")#idx(
    "double",
    "complexes, pairing of",
  ) of double complexes $E_0 times lprime(E)_0 -> ldprime(E)_0$ consists of maps
  $
    E_0^(p q) times.o lprime(E)_0^(p' q') -> ldprime(E)_0^(p+p', q+q') \
    x times.o y |-> x y
  $
  satisfying the identities
  $
    d_0 (x y) & = d_0 (x) y + (-1)^(p+q) x d_0 (y) \
    d_1 (x y) & = d_1 (x) y + (-1)^(p+q) x d_1 (y).
  $

  A *double complex with ring structure* is a double complex $E_0$ together with
  an associative pairing $E_0 times E_0 -> E_0$. A *module* over a double
  complex with ring structure $E_0$ is a double complex $lprime(E)_0$ together
  with a pairing $E_0 times lprime(E)_0 -> lprime(E)_0$ satisfying the usual
  associative law for the action of a ring on a module.
] <def:pairing-double-complexes>

For example, in the case of the spectral sequence of a group extension, suppose
$M_1$, $M'_1$ are $R(G slash N)$-modules with projective resolutions $bold(P)$,
$bold(P)'$, suppose $M_2$, $M'_2$ are $R G$-modules with projective resolutions
$bold(Q)$, $bold(Q)'$, and suppose $M_3$, $M'_3$ are also $R G$-modules. Setting
$
  E_0^(p q) & = Hom_(R(G slash N)) (P_p, Hom_(R N) (Q_q, M_3)) \
  lprime(E)_0^(p q) & = Hom_(R(G slash N)) (P'_p, Hom_(R N) (Q'_q, M'_3)) \
  ldprime(E)_0^(p q) & = Hom_(R(G slash N)) ((bold(P) times.o bold(P)')_p,
    Hom_(R N) ((bold(Q) times.o bold(Q)')_q, M_3 times.o M'_3))
$
there are cup product maps, as in Section~3.2 of Volume~I, giving a pairing
$E_0 times lprime(E)_0 -> ldprime(E)_0$.

If $M_1 = M_2 = M_3 = R$ then $E_0$ is a double complex with ring structure. If
$M'_1 = M'_2 = R$ and $M'_3 = M$ is arbitrary then $lprime(E)_0$ is a module
over $E_0$. We shall see that this gives the entire spectral sequence
$ H^p (G slash N, H^q (N, R)) => H^(p+q) (G, R) $
a ring structure over which the spectral sequence
$ H^p (G slash N, H^q (N, M)) => H^(p+q) (G, M) $
is a module.

We now pass from the double complex to the associated filtered complex. Recall
that
$
  F^p Tot (E_0)^(p+q) = plus.o.big_(i+j=p+q \ i >= p) E_0^(i j).
$
#source(128)Thus a pairing $E_0 times lprime(E)_0 -> ldprime(E)_0$ gives rise to
a pairing
$
  Tot (E_0)^(p+q) times.o Tot (lprime(E)_0)^(p'+q')
  -> Tot (ldprime(E)_0)^(p+p'+q+q')
$
satisfying the identity
$ d(x y) = d(x) y + (-1)^(deg(x)) x d(y) $
and with the property that the image under this map of the tensor product of
subcomplexes $F^p Tot (E_0)^(p+q) times.o F^(p') Tot (lprime(E)_0)^(p'+q')$ lies
in $F^(p+p') Tot (ldprime(E)_0)^(p+p'+q+q')$.

#definition[
  A *pairing*#idx("pairing", "of filtered complexes")#idx(
    "filtered complex",
    "pairing of",
  ) of filtered cochain complexes
  $bold(X) times lprime(bold(X)) -> ldprime(bold(X))$ consists of maps
  $
    X^m times.o lprime(X)^n -> ldprime(X)^(m+n) \
    x times.o y |-> x y
  $
  satisfying the identity
  $ d(x y) = d(x) y + (-1)^(deg(x)) x d(y) $
  and with the property that the image under this map of
  $F^p bold(X) times.o F^(p') lprime(bold(X))$ lies in
  $F^(p+p') ldprime(bold(X))$.
] <def:pairing-filtered-complexes>

Such a pairing induces maps
$
  H^(p+q) (F^p bold(X)) times H^(p'+q') (F^(p') lprime(bold(X)))
  -> H^(p+p'+q+q') (F^(p+p') ldprime(bold(X)))
$
$
  H^(p+q) (F^p bold(X), F^(p+n) bold(X))
  times H^(p'+q') (F^(p') lprime(bold(X)), F^(p'+n) lprime(bold(X))) \
  -> H^(p+p'+q+q') (F^(p+p') ldprime(bold(X)), F^(p+p'+n) ldprime(bold(X)))
$
and hence in particular with $n = 1$,
$
  D_1^(p q) times lprime(D)_1^(p' q') & -> ldprime(D)_1^(p+p', q+q') \
  E_1^(p q) times lprime(E)_1^(p' q') & -> ldprime(E)_1^(p+p', q+q').
$

The maps
$
  H^(p+q) (F^p bold(X), F^(p+n) bold(X)) -> H^(p+q) (F^p bold(X),
    F^(p+1) bold(X)) -> H^(p+q) (F^(p-n+1) bold(X), F^(p+1) bold(X))
$
take products to products, and so by Proposition~@prop:cycles-boundaries, the
image of $Z_n times lprime(Z)_n$ under this product map lies in $ldprime(Z)_n$,
and the images of $Z_n times lprime(B)_n$ and $B_n times lprime(Z)_n$ lie in
$ldprime(B)_n$. It follows that there are products
$ E_n^(p q) times lprime(E)_n^(p' q') -> ldprime(E)_n^(p+p', q+q') $
satisfying the identity
$ d_n (x y) = d_n (x) y + (-1)^(p+q) x d_n (y), $
and with the property that the product on $E_(n+1)$ is induced by the product on
$E_n$ according to the formula
$ [x][y] = [x y]. $
This then induces a product on $E_infinity$ in the obvious way. It also follows
from the above that the isomorphism given in Theorem~@th:page-as-image preserves
products. #source(129)Since the relevant maps in
Theorem~@th:filtration-quotients take products to products, it also follows that
the isomorphism given in this theorem preserves products. We summarise the
situation in the following theorem.

#theorem(closed: true)[
  A pairing $E_0 times lprime(E)_0 -> ldprime(E)_0$ of double complexes gives
  rise to a pairing $bold(X) times lprime(bold(X)) -> ldprime(bold(X))$ of
  filtered cochain complexes. Such a pairing in turn gives rise to pairings
  $ E_n^(p q) times lprime(E)_n^(p' q') -> ldprime(E)_n^(p+p', q+q') $
  satisfying $d_n (x y) = d_n (x) y + (-1)^(p+q) x d_n (y)$ and $[x][y] = [x y]$
  in $E_(n+1)$. In the limit this induces a pairing
  $
    E_infinity^(p q) times lprime(E)_infinity^(p' q')
    -> ldprime(E)_infinity^(p+p', q+q')
  $
  in such a way that the isomorphisms
  $
    E_infinity^(p q) tilde.equiv F^p H^(p+q) (bold(X)) slash F^(p+1)
    H^(p+q) (bold(X))
  $
  given in Theorem~@th:filtration-quotients preserve products.
] <th:spectral-products>

Notice that we may only deduce the product structure on $H^* (bold(X))$ modulo
terms lower down in the filtration. It may be quite hard to deduce the exact
product structure on $H^* (bold(X))$ from this information.
