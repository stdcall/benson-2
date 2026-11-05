#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/01-04-whitehead.typ": cylinder-square

== The Whitehead theorem <sec:whitehead>

#idx("Whitehead theorems", target: [@sec:whitehead])There is a way of turning
any map into an inclusion, as follows:

#definition[
  If $f : X -> Y$, we define the *mapping cylinder*#idx(
    "cylinder, mapping",
  )#idx(
    "mapping cone, cylinder",
  ) $M_f$#idx("$M_f$") of $f$ as the quotient space
  $ M_f = frac((X times I) dot(union) Y, (x, 1) tilde f(x)) $
  (with the quotient topology).
] <def:mapping-cylinder>

We have maps $i : X -> M_f$ sending $x |-> (x, 0)$ and $j : Y -> M_f$ sending
$y |-> (y)$.

#lemma[
  The inclusion $j : Y -> M_f$ is a homotopy equivalence.
] <lem:cylinder-equivalence>

#proof[
  Define a map $pi : M_f -> Y$ via $(x, t) |-> f(x)$, $y |-> (y)$. Then
  $pi compose j = id_Y$, and there is a homotopy
  $F : j compose pi tilde.eq id_(M_f)$ given by $F((y), t') = (y)$,
  $F((x, t), t') = (x, 1 - t'(1 - t))$.
]

Thus we may regard $i : X -> M_f$ as an inclusion which is "$f$ up to homotopy"
in the sense of the following diagram:
$ #cylinder-square $
We define the *mapping cone*#idx("cone", "mapping") $C_f$#idx("$C_f$") to be the
space obtained from $M_f$ by identifying the image of $i$ to a single point.
Thus for example $tilde(H)_n (C_f) tilde.equiv H_n (M_f, X)$.

Since $j_* : pi_n (Y, y_0) tilde.equiv pi_n (M_f, y_0) tilde.equiv
pi_n (M_f, x_0)$, we may use this construction to obtain long exact sequences in
homotopy and homology from any map as follows:
$
  dots.c -> pi_(n+1) (M_f, X, x_0) -> pi_n (X, x_0)
  limits(arrow.r.long)^(f_*) pi_n (Y, y_0) -> pi_n (M_f, X, x_0) -> dots.c
$
$
  #source(24)dots.c --> H_(n+1) (M_f, X) --> H_n (X)
  limits(arrow.r.long)^(f_*) H_n (Y) --> H_n (M_f, X) --> dots.c
$
The Hurewicz map connects these long exact sequences to make a commutative
diagram as in Theorem~@th:hurewicz-diagram.

#theorem(title: [Whitehead])[
  Suppose $X$ and $Y$ are path connected, and $f : (X, x_0) -> (Y, y_0)$.
  Suppose that for some $n >= 1$,
  #enum(numbering: "(A)")[
    $f_* : pi_i (X, x_0) -> pi_i (Y, y_0)$ is
    $cases(italic("iso") quad i < n, italic("epi") quad i = n.)$
  ]
  Then
  #enum(numbering: "(A)", start: 2)[
    $f_* : H_i (X) -> H_i (Y)$ is
    $cases(italic("iso") quad i < n, italic("epi") quad i = n.)$
  ]

  Conversely if $X$ and $Y$ are simply connected, or more generally simple
  spaces, then #statement-comment[(B)] $=>$ #statement-comment[(A)].
] <th:whitehead-homology>

#proof[
  By the above long exact sequence, (A) is equivalent to the statement that
  $pi_i (M_f, X, x_0) = 0$ for $i <= n$, and (B) is equivalent to the statement
  that $H_i (M_f, X) = 0$ for $i <= n$. Thus the theorem follows from the
  relative Hurewicz theorem.
]
