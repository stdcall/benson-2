#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/04-06-adem-relations.typ": norm-square

== Adem relations <sec:adem-relations>

The Adem relations#idx("Adem relations", target: [@sec:adem-relations])
essentially correspond to the fact that the following square commutes.
$ #norm-square $
So we first prove a symmetric form of the Adem relations, due to Bullett and
Macdonald [@bib:Bullett1982], which goes as follows. For $p = 2$ we denote by
$Sq_t$ the formal power series $sum_(i >= 0) t^i Sq^i$, where $t$ is an
indeterminate. For $p$ odd we denote by $P(t)$ the formal power series
$sum_(i >= 0) t^i P^i$.

#theorem[
  + For $p = 2$ we have
    $ Sq_(t^2 + s t) Sq_(s^2) = Sq_(s^2 + s t) Sq_(t^2). $
  + For $p$ odd the formal power series
    $ P(t^p + s t^(p-1) + dots.c + s^(p-1) t) . P(s^p) $
    and
    $ s . [beta, P(t^p + s t^(p-1) + dots.c + s^(p-1) t)] . P(s^p) $
    are symmetric in $s$ and $t$, where $[beta, P] = beta P - P beta$.
] <th:symmetric-adem-relations>

#source(157)We shall treat the cases $p = 2$ and $p$ odd separately. Although
most of the proof is exactly parallel, it helps to understand the case $p = 2$
first because there are fewer technical complications.

#subhead[Case (i) : $p = 2$] Let
$H^* (ZZ slash 2 times ZZ slash 2, FF_2) = FF_2 [x_1, x_2]$ with
$deg(x_1) = deg(x_2) = 1$. If $zeta in H^r (G, FF_2)$ then
$
  norm_(1 times ZZ slash 2 times G, ZZ slash 2 times ZZ slash 2 times G)
  norm_(G, 1 times ZZ slash 2 times G) (zeta)
  = norm(sum_k x_2^(r-k) Sq^k (zeta)) \
  = sum_k norm(x_2)^(r-k) norm Sq^k (zeta)
  = sum_(j,k) (x_1 x_2 + x_2^2)^(r-k) x_1^(r+k-j) Sq^j Sq^k (zeta) \
  = x_1^r x_2^r (x_1 + x_2)^r sum_(j,k) (x_2 + x_1^(-1) x_2^2)^(-k) x_1^(-j)
  Sq^j Sq^k (zeta) \
  = x_1^r x_2^r (x_1 + x_2)^r Sq_(x_1^(-1)) Sq_((x_2 + x_1^(-1) x_2^2)^(-1))
  (zeta).
$
We make the substitution $x_1^(-1) = t(s + t)$, $x_2^(-1) = s(s + t)$ so that
$(x_2 + x_1^(-1) x_2^2)^(-1) = s^2$ to deduce that $Sq_(t^2 + s t) Sq_(s^2)$ is
symmetric in $s$ and $t$. This proves part~(i) of
Theorem~@th:symmetric-adem-relations.

We now put $s = 1$ (no information is lost by this substitution since the
relation is homogeneous) to obtain
$ Sq_(t^2 + t) Sq_1 = Sq_(t+1) Sq_(t^2). $
Separating out terms which increase cohomological degree by $n$, we have
$
  sum_(a+b=n) (t^2 + t)^a Sq^a Sq^b
  = sum_j (t + 1)^(n-j) t^(2j) Sq^(n-j) Sq^j.
$
Thus $Sq^a Sq^b$ is equal to the residue at $t^2 + t = 0$ (or in particular at
$t = 0$) of
$
  scaled((sum_j (t + 1)^(a+b-j) t^(2j) Sq^(a+b-j) Sq^j d(t^2 + t)))
  slash (t^2 + t)^(a+1) \
  = sum_j (t + 1)^(b-j-1) t^(2j-a-1) Sq^(a+b-j) Sq^j d t,
$
namely the coefficient of $t^(-1)$ in
$ sum_j (t + 1)^(b-j-1) t^(2j-a-1) Sq^(a+b-j) Sq^j, $
which is
$ sum_j binom(b - 1 - j, a - 2j) Sq^(a+b-j) Sq^j. $
This completes the proof of the Adem relations for $p = 2$.

#subhead[#source(158)Case (ii) : $p$ odd] Let
$H^* (ZZ slash p times ZZ slash p, FF_p)$ have generators $y_1$ and $y_2$ in
degree one and $x_1 = -beta(y_1)$, $x_2 = -beta(y_2)$ in degree two. If
$zeta in H^r (G, FF_p)$ then $P^i (zeta) in H^(r+2i(p-1)) (G, FF_p)$, and
$
  & norm_(G, 1 times ZZ slash p times G) (zeta) \
  & quad = (-1)^(m r(r+1) slash 2) (m!)^r sum_i (-1)^i
    [x_2^(m(r-2i)) P^i (zeta) + x_2^(m(r-2i)-1) y_2 beta P^i (zeta)]
$
where $m = (p - 1) slash 2$ as usual. We have
$
  norm_(1 times ZZ slash p, ZZ slash p times ZZ slash p) (x_2)
  & = x_2^p - x_1^(p-1) x_2 \
  norm_(1 times ZZ slash p, ZZ slash p times ZZ slash p) (y_2)
  & = -(m!)^(-1) x_1^((p-3) slash 2) (x_1 y_2 - y_1 x_2)
$
(see the example at the end of Section~@sec:evens-norm and the discussion of the
constants $theta_r$ at the end of the last section), and so
$
  norm_(1 times ZZ slash p times G, ZZ slash p times ZZ slash p times G)
  norm_(G, 1 times ZZ slash p times G) (zeta) = \
  (-1)^(m r(r+1) slash 2) (m!)^r sum_(i,j) (-1)^(i+j)
  \[norm(x_2)^(m(r-2i)) (-1)^(m r(r+1) slash 2)
  (m!)^(r+2i(p-1)) \
  \{x_1^(m(r+2i(p-1)-2j)) P^j P^i (zeta)
  + x_1^(m(r+2i(p-1)-2j)-1) y_1 beta P^j P^i (zeta)\} + \
  (-1)^(m(r+1)) norm(x_2)^(m(r-2i)-1) norm(y_2)
  (-1)^(m(r+1)(r+2) slash 2) (m!)^(r+2i(p-1)+1) \
  \{x_1^(m(r+2i(p-1)+1-2j)) P^j beta P^i (zeta)
  + x_1^(m(r+2i(p-1)+1-2j)-1) y_1 beta P^j beta P^i (zeta)\}\]
$
$
  = (-1)^((m+1)r) x_1^(m r) x_2^(m r) (x_2^(p-1) - x_1^(p-1))^(m r)
  sum_(i,j) (-1)^(i+j) \{(x_2^p x_1^(1-p) - x_2)^(-2m i) \
  x_1^(-2m j) P^j P^i (zeta) + (x_2^p x_1^(1-p) - x_2)^(-2m i)
  x_1^(-2m j-1) y_1 beta P^j P^i (zeta) \
  - (x_2^p x_1^(1-p) - x_2)^(-2m i-1) x_1^(-2m j-1) (x_1 y_2 - y_1 x_2)
  P^j beta P^i (zeta) \
  - (x_2^p x_1^(1-p) - x_2)^(-2m i-1) x_1^(-2m j-1) y_2 y_1 beta P^j beta P^i
  (zeta)\}.
$

The terms in the above expression not involving $y_1$ or $y_2$ show that the
expression #symbol-display(
  "a",
  parens: true,
  $
    sum_(i,j) (-1)^(i+j) (x_2^p x_1^(1-p) - x_2)^(-2m i) x_1^(-2m j) P^j P^i
  $,
) <eq:adem-symmetric-a>
is symmetric in $x_1$ and $x_2$.

Similarly if we multiply the coefficient of $y_1$ by $x_1^p$, multiply the
coefficient of $y_2$ by $x_2^p$ and add, the resulting expression
#symbol-display(
  "b",
  parens: true,
  $
    sum_(i,j) (-1)^(i+j) (x_2^p x_1^(1-p) - x_2)^(-2m i) x_1^(-2m(j-1))
    (beta P^j P^i - P^j beta P^i)
  $,
) <eq:adem-symmetric-b>
is symmetric in $x_1$ and $x_2$.

We now make the substitution
$
  x_1^(-1) = (-t)^(1 slash (p-1)) (s - t), quad
  x_2^(-1) = (-s)^(1 slash (p-1)) (t - s)
$
#source(159)so that
$ x_1^(-2m) = -t(s - t)^(2m) = -(t^p + s t^(p-1) + dots.c + s^(p-1) t) $
and
$ (x_2^p x_1^(1-p) - x_2)^(-2m) = -s^p. $
Making this substitution in @eq:adem-symmetric-a we see that
$ sum_(i,j) s^(p i) (t^p + s t^(p-1) + dots.c + s^(p-1) t)^j P^j P^i $
is symmetric in $s$ and $t$. Making the same substitution in
@eq:adem-symmetric-b and then multiplying by
$s t(s^(p-1) + s^(p-2) t + dots.c + t^(p-1))$, we see that
$
  sum_(i,j) s^(p i+1) (t^p + s t^(p-1) + dots.c + s^(p-1) t)^j [beta, P^j]
  P^i
$
is symmetric in $s$ and $t$. This completes the proof of part~(ii) of
Theorem~@th:symmetric-adem-relations.

We now put $s = 1$ and write $u$ for
$(t^(p-1) + t^(p-2) + dots.c + 1) = (1 - t)^(p-1)$ to obtain
$
          P(t u) P(1) & = P(u) P(t^p) \
  [beta, P(t u)] P(1) & = t[beta, P(u)] P(t^p),
$
so that
$ P(t u) beta P(1) = ((1 - t) beta P(u) + t P(u) beta) P(t^p). $
Separating out terms increasing cohomological degree by $2n(p - 1)$ in the first
case and $2n(p - 1) + 1$ in the second, we have
$
  sum_(a+b=n) (t u)^a P^a P^b & = sum_j u^(n-j) t^(p j) P^(n-j) P^j \
  sum_(a+b=n) (t u)^a P^a beta P^b
  & = sum_j u^(n-j) t^(p j) ((1 - t) beta P^(n-j) P^j + t P^(n-j) beta P^j).
$

Thus $P^a P^b$ (resp. $P^a beta P^b$) is equal to the residue at $t = 0$ of the
right-hand side of the first (resp. second) equation multiplied by
$ frac(d(t u), (t u)^(a+1)) = frac((1 - t)^(p-2) d t, (t u)^(a+1)). $
Hence $P^a P^b$ is equal to the coefficient of $t^(-1)$ in
$ sum_j (1 - t)^((p-1)(b-j)-1) t^(p j-a-1) P^(a+b-j) P^j $
while $P^a beta P^b$ is equal to the coefficient of $t^(-1)$ in
$
  sum_j (1 - t)^((p-1)(b-j)-1) t^(p j-a-1)
  ((1 - t) beta P^(a+b-j) P^j + t P^(a+b-j) beta P^j).
$
This completes the proof of the Adem relations for $p$ odd.
