#import "main-defs.typ": *
#import "statements.typ": *

== Smith's theorem and universal coefficient systems <sec:smith-theorem>
#idx("Smith's theorem", target: [@th:smith])#idx(
  "theorem",
  "Smith's",
  target: [@th:smith],
)#idx("coefficient system", "universal", target: [@sec:smith-theorem])#idx(
  "local",
  "system, universal",
  target: [@sec:smith-theorem],
)#idx("universal", "local system", target: [@sec:smith-theorem])

Much of the representation theory of Chevalley groups#idx(
  "Chevalley group",
)#idx("group", "Chevalley") in their own characteristic can be understood in
terms of the representation theory of the corresponding algebraic group. The
interested reader should consult the work of R.~Steinberg, J.~C. Jantzen, J.~E.
Humphreys and H.~H. Andersen, among others. We shall instead try to see what
information we can get out of the approach using local coefficient systems,
following Ronan and Smith. The basic input for this theory is the following
theorem.

Let $k$ be an algebraically closed field of characteristic $p$.

#theorem(title: [Smith [@bib:Smith1982]])[
  #source(259)Suppose $G$ is a Chevalley group in characteristic $p$, $H$ a
  parabolic subgroup and $M$ an irreducible $k G$-module. Then the fixed point
  space $M^(O_p (H))$ is an irreducible $k(H slash O_p (H))$-module. If
  $M tilde.equiv.not N$ are non-isomorphic irreducible $k G$-modules then there
  exists a minimal parabolic subgroup $H$ with
  $M^(O_p (H)) tilde.equiv.not N^(O_p (H))$.
] <th:smith>

#proof[
  It would take us too far afield to give the proof of this theorem. The proof
  is very short, but uses the theory of weight spaces for modules for a
  Chevalley group, see S.~D. Smith [@bib:Smith1982]. An alternative proof may be
  found in M.~Cabanes [@bib:Cabanes1984].
]

#example(kind: "Examples")[
  + Let $B$ be a Borel subgroup (which is the same as a Sylow $p$-normaliser).
    Then $B slash O_p (B)$ is an abelian $p'$-group, and so its irreducible
    modules are one dimensional. So for any irreducible $k G$-module, the fixed
    points of a Sylow $p$-subgroup are one dimensional.
  + If $q = 2$ then a Borel subgroup is the same as a Sylow 2-subgroup, and the
    minimal parabolics $H supset.eq B$ have
    $ H slash O_2 (H) tilde.equiv SL_2 (2) tilde.equiv cal(S)_3, $
    the symmetric group#idx("symmetric", "group", "$cal(S)_3$")#idx(
      "group",
      "symmetric",
      "$cal(S)_3$",
    ) of degree three, and so the simple modules for $H slash O_2 (H)$ have
    dimensions one and two. Thus associated to each irreducible module is an
    assignment of ones and twos to the vertices of the Dynkin diagram, and by
    Smith's theorem this assignment completely determines the module. It turns
    out that every possible assignment occurs, and so there are exactly $2^r$
    isomorphism classes of irreducible modules, where $r$ is the semisimple
    rank. The Steinberg module is the one corresponding to putting a 2 on each
    vertex.

  More generally for any value of $q$, if $H$ is a minimal parabolic then there
  is a natural map $SL_2 (FF_q) -> H slash O_p (H)$#idx("$SL_2 (FF_q)$")#idx(
    "special",
    "linear group",
    "$SL_2 (FF_q)$",
  )#idx("group", "special linear", "$SL_2 (FF_q)$") whose kernel is central and
  whose cokernel is an abelian group which acts on the image via diagonal
  matrices. For $SL_2 (p)$ there are $p$ simple modules, namely the symmetric
  powers#idx("power, symmetric")#idx("symmetric", "power") of the natural 2
  dimensional module with dimensions 1 up to $p$. Steinberg's tensor product
  theorem#idx("Steinberg's tensor product theorem")#idx(
    "tensor product",
    "theorem, Steinberg's",
  )#idx("theorem", "Steinberg's tensor product") gives the irreducible modules
  for $SL_2 (FF_q)$ when $q = p^e$ in terms of these. It turns out that if two
  modules have isomorphic fixed points when pulled back to each of these
  $SL_2 (FF_q)$'s then they are related by tensoring with a one dimensional
  representation. A Chevalley group is of *universal type*#idx(
    "type",
    "universal",
  )#idx("universal", "type") if every configuration of pulled back fixed points
  occurs for some irreducible $k G$-module. In this case the number of
  isomorphism classes of irreducible modules is $|G : G'| . q^r$. For any
  Chevalley group the universal $p'$-central extension is a Chevalley group of
  universal type. Thus for example $SL_n (FF_q)$ is of universal type and has
  $q^(n-1)$ isomorphism classes of irreducible modules. $PGL_n (FF_q)$ is not of
  universal type, but its universal $p'$-central extension $GL_n (FF_q)$ is; it
  has $(q - 1) q^(n-1)$ irreducibles. Proofs of all these remarks are outside
  the scope of this book, but the remarks are included for the orientation of
  the reader.
]

#remark(kind: "Comment")[
  Smith's theorem is far from being true for a non-Chevalley group. For example
  for the alternating group $A_7$#idx("alternating group", "$A_7$")#idx(
    "group",
    "alternating",
    "$A_7$",
  ) in characteristic two, there #source(260)is a 20 dimensional simple module.
  The fixed points of a Sylow 2-subgroup (which has order eight) are therefore
  more than one dimensional, whereas the Sylow 2-subgroup is self normalising.
  The sporadic group $J_4$#idx("$J_4$")#idx("sporadic group $J_4$")#idx(
    "group",
    "sporadic, $J_4$",
  ) looks more like a Chevalley group in characteristic two, but the 112
  dimensional irreducible module has fixed points $1 plus.o 5$ under the action
  of the maximal 2-local subgroup $2^10 L_5 (2)$.
]

#corollary(closed: true)[
  Suppose $M$ is an irreducible $k G$-module as above. Then the fixed point
  coefficient system $cal(F)_M$ on the building $Delta(G)$ has the property that
  $cal(F)_M (sigma)$ is irreducible for each simplex $sigma$.
] <cor:fixed-points-irreducible>

#lemma[
  If $M$ and $N$ are irreducible $k G$-modules for $G$ a Chevalley group, then
  $ Hom_(Delta, G) (cal(F)_M, cal(F)_N) tilde.equiv Hom_(k G) (M, N) $
  where $Delta$ denotes the building of $G$.
] <lem:fixed-point-systems-hom>

#proof[
  Suppose we are given a homomorphism from $cal(F)_M$ to $cal(F)_N$. By Smith's
  theorem, at each simplex the homomorphism is a homomorphism of irreducible
  modules. By Schur's lemma it is therefore determined up to multiplication by a
  scalar. By compatibility with the restriction maps and conjugations, any one
  scalar determines the rest (since $Delta slash G$ is connected). If
  $M tilde.equiv.not N$ then there is some simplex on which the values are not
  isomorphic, so in this case the scalar has to be zero. If $M tilde.equiv N$
  then of course any scalar can happen.
]

#proposition[
  If $M$ is an irreducible $k G$-module for $G$ a Chevalley group, then
  $H_0 (cal(F)_M)$ has a unique maximal submodule, and the quotient is naturally
  isomorphic to $M$.
] <prop:fixed-point-homology-head>

#proof[
  Suppose $N$ is a simple $k G$-module. Then
  $
    #aligned-rows(
      (
        $Hom_(k G) (H_0 (cal(F)_M), N)$,
        $tilde.equiv Hom_(Delta, G) (cal(F)_M, kappa_N)$,
      ),
      (
        $$,
        $= Hom_(Delta, G) (cal(F)_M, cal(F)_N) tilde.equiv Hom_(k G) (M, N).$,
      ),
    )
  $
]

#remark(kind: "Comment")[
  The module $H_0 (cal(F)_M)$ should not be confused with the *Weyl module*#idx(
    "Weyl module",
  )#idx("module", "Weyl") $W_M$ which also has a unique maximal submodule, which
  again has quotient isomorphic to $M$. In fact, both of these modules are
  quotients of a universal coefficient system constructed as follows.

  Let $cal(B)_p^((1)) (G)$#idx("$cal(B)_p^((1)) (G)$") be the subset of
  $cal(B)_p (G)$ consisting of the Sylow $p$-subgroups together with the maximal
  points lying below them; these correspond to the simplices of the building
  associated to the Borel and minimal parabolic subgroups, i.e., the simplices
  of dimension $r - 1$ and $r - 2$. Denote by
  $ i_G : cal(B)_p^((1)) (G) arrow.r.hook cal(B)_p (G) $
  the inclusion.
]

#definition[
  The coefficient system $cal(U)_M = (i_G)_! i_G^(-1) cal(F)_M$ is the
  *universal coefficient system*#idx("universal", "coefficient system")
  associated to the irreducible $k G$-module $M$.
] <def:universal-coefficient-system>

#proposition[
  #source(261)The module $H_0 (cal(U)_M)$ has a unique maximal submodule, and
  the quotient is isomorphic to $M$. If $N$ is a $k G$-module such that for a
  minimal parabolic subgroup $H$, $N^(O_p (H)) tilde.equiv M^(O_p (H))$, and $N$
  is generated by these fixed points, then $N$ is a quotient of $H_0 (cal(U)_M)$
  (this is true in particular if $N$ is the Weyl module $W_M$).
] <prop:universal-coefficient-homology>

#proof[
  Just as in the last proposition, we have
  $
    #aligned-rows(
      (
        $Hom_(k G) (H_0 (cal(U)_M), N)$,
        $tilde.equiv Hom_(Delta, G) (cal(U)_M, kappa_N)
        = Hom_(Delta, G) ((i_G)_! i_G^(-1) cal(F)_M, kappa_N)$,
      ),
      (
        $$,
        $tilde.equiv Hom_(cal(B)_p^((1)) (G), G) (i_G^(-1) cal(F)_M,
          i_G^(-1) kappa_N)$,
      ),
      (
        $$,
        $= Hom_(cal(B)_p^((1)) (G), G) (i_G^(-1) cal(F)_M, i_G^(-1) cal(F)_N)$,
      ),
      ($$, $tilde.equiv Hom_(k G) (M, N).$),
    )
  $
]

#subhead[An algorithm for constructing the irreducible modules] If $M$ is an
irreducible $k G$-module, we write $hat(M)$ for $H_0 (cal(F)_M)$ and $J(hat(M))$
for the unique maximal submodule of $hat(M)$.

#lemma[
  If $N$ is a quotient of $hat(M)$ then there is a canonical splitting
  $cal(F)_N tilde.equiv cal(F)_M plus.o cal(F)_(J(N))$.
] <lem:fixed-point-system-splitting>

#proof[
  We have maps
  $ hat(M) = H_0 (cal(F)_M) -> N -> M $
  whose composite is the natural map $H_0 (cal(F)_M) -> M$, and hence associated
  maps
  $ cal(F)_M -> cal(F)_N -> cal(F)_M $
  whose composite is the identity. The kernel of the second of these maps is
  just $cal(F)_(J(N))$.
]

Ronan and Smith had the following idea for turning this into an inductive
construction of the irreducible modules. The coefficient system $cal(F)_M$ can
be constructed entirely from a knowledge of the representation theory of
$H slash O_p (H)$ for $H$ parabolic. These groups are Chevalley groups of
strictly smaller rank, and so we may assume their representation theory is
known. This means we can construct $hat(M)$. By the above lemma, we have
$ cal(F)_(hat(M)) = cal(F)_M plus.o cal(F)_(J(hat(M))). $
So the next step is to find the complementary coefficient system
$cal(F)_(J(hat(M)))$. The image of the natural map
$ H_0 (cal(F)_(J(hat(M)))) -> hat(M) $
has non-zero image contained in $J(hat(M))$. Quotienting by this image gives us
a closer approximation to $M$, and we may use it to replace $hat(M)$ in the
above construction and start again. In a finite number of steps (often just
one!) this process must terminate.

It is not quite clear from this description that this is really a practical
process for calculation. In their paper [@bib:Ronan1985], Ronan and Smith
describe in detail how to turn this into an effective algorithm for calculation.
