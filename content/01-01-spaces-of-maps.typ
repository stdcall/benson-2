#import "main-defs.typ": *
#import "statements.typ": *

== Spaces of maps <sec:spaces-of-maps>

First we recall a basic fact from general topology about spaces of maps. If $X$
and $Y$ are topological spaces, we write $Map(X, Y)$ or $Y^X$ for the space of
(continuous) maps from $X$ to $Y$ with the compact-open topology. This is the
topology for which the typical sub-basic open set is the set of maps taking a
given compact set in $X$ into a given open set in $Y$.

#proposition[
  If $X$ and $Y$ are Hausdorff and $Y$ is locally compact, then the natural map
  $ Map(X times Y, Z) -> Map(X, Map(Y, Z)) $
  sending $f$ to the map $f'$ defined by $f'(x)(y) = f(x, y)$ is a
  homeomorphism.
] <prop:exponential>

#proof[
  See for example Hu [@bib:Hu1964, Section V.3].
]

This isomorphism is called the *exponential isomorphism*#idx(
  "exponential isomorphism",
)#idx("isomorphism, exponential"). This terminology becomes clearer if we write
it in the form
$ Z^(Y times X) tilde.equiv (Z^Y)^X. $

We shall also work with spaces $X$ with a _basepoint_#idx("basepoint") $x_0$,
which we shall denote by $(X, x_0)$, and with pairs of spaces $A subset.eq X$
and a basepoint $x_0 in A$, which we shall denote by $(X, A, x_0)$. Maps of
spaces should take the basepoint to the basepoint.

If $(X, x_0)$ and $(Y, y_0)$ are based spaces, we write $Map_* (X, Y)$ for the
subspace of $Map(X, Y)$ consisting of those maps taking $x_0$ to $y_0$. This is
a based space with the constant map as basepoint. If $(Z, z_0)$ is another based
space, then under the above correspondence, it is easy to see that the subspace
of $Map(X times Y, Z)$ corresponding to the subspace
$ Map_* (X, Map_* (Y, Z)) subset.eq Map(X, Map(Y, Z)) $
consists of those maps sending $(X times y_0) union (x_0 times Y)$ to $z_0$.

#definition[
  #source(14)If $(X, x_0)$ and $(Y, y_0)$ are based spaces, we write $X or Y$
  ($X$ *wedge*#idx("wedge") $Y$) for the subspace
  $(X times y_0) union (x_0 times Y)$ of $X times Y$, and $X and Y$ ($X$
  *smash*#idx("smash") $Y$) for the quotient space of $X times Y$ formed by
  identifying all points of $X or Y$ to a single basepoint $*$.
] <def:wedge-smash>

Thus we have the following:

#proposition(closed: true)[
  If $(X, x_0)$ and $(Y, y_0)$ are Hausdorff and $(Y, y_0)$ is locally compact,
  then the natural map
  $ Map_* (X and Y, Z) -> Map_* (X, Map_* (Y, Z)) $
  defined above is a homeomorphism.
] <prop:based-exponential>
