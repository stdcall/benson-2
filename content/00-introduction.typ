#import "main-defs.typ": *
#import "statements.typ": *

#heading(level: 1, numbering: none)[Introduction]

#source(9)This is the second of two volumes which have grown out of about seven
years of graduate courses on various aspects of representation theory and
cohomology of groups, given at Yale, Northwestern and Oxford. In this second
volume, we concentrate on cohomology of groups and modules. We try to develop
everything from both an algebraic and a topological viewpoint, and demonstrate
the connection between the two approaches. Having in mind the die-hard
algebraist who refuses to have anything to do with topology, we have tried to
make sure that if the reader omits all sections involving topology, the rest is
still a coherent treatment of the subject. But by trying to present the topology
with as few prerequisites as possible, we hope to entice such a reader to a more
broad-minded point of view. Thus Chapter~@ch:topology consists of a predigested
summary of the topology required to understand what is happening in
Chapter~@ch:group-cohomology.

In Chapter~@ch:group-cohomology, we give an overview of the algebraic topology
and K-theory associated with cohomology of groups, and especially the
extraordinary work of Quillen which has led to his definition of the higher
algebraic K-groups of a ring.

The algebraic side of the cohomology of groups mirrors the topology, and we have
always tried to give algebraic proofs of algebraic theorems. For example, in
Chapter~@ch:spectral-sequences you will find B. Venkov's topological proof of
the finite generation of the cohomology ring of a finite group, while in
Chapter~@ch:evens-steenrod you will find L. Evens' algebraic proof. Also in
Chapter~@ch:evens-steenrod, we give a detailed account of the construction of
Steenrod operations in group cohomology using the Evens norm map, a topic
usually treated from a topological viewpoint.

One of the most exciting developments in recent years in group cohomology is the
theory of varieties for modules, expounded in Chapter~@ch:varieties. In a sense,
this is the central chapter of the entire two volumes, since it shows how
inextricably intertwined representation theory and cohomology really are.

I would like to record my thanks to the people, too numerous to mention
individually, whose insights I have borrowed in order to write these volumes;
who have pointed out infelicities and mistakes in the exposition; who have
supplied me with quantities of coffee that would kill an average horse; and who
have helped me in various other ways. I would especially like to thank Ken Brown
for allowing me to explain his approach to induction theorems in I, Chapter 5;
Jon Carlson for collaborating with me over a number of years, and without whom
these volumes would never have been written; Ralph Cohen for helping me
understand the free loop space and its rôle in cyclic homology
(Chapter~@ch:group-cohomology of Volume II); Peter Webb for supplying me with an
early copy of the notes for his talk at the 1986 Arcata conference on
Representation Theory of Finite Groups, on which Chapter~@ch:group-actions of
Volume II is based; David Tranah of Cambridge University Press for sending me a
free copy of Tom Körner's wonderful book on Fourier analysis, and being
generally helpful in #source(
  10,
)various ways you have no interest in hearing about unless you happen to be
David Tranah.

There is a certain amount of overlap between this volume and my Springer lecture
notes volume [@bib:Benson1984c]. Wherever I felt it appropriate, I have not
hesitated to borrow from the presentation of material there. This applies
particularly to parts of Chapters 1, 4 and 5 of Volume I and
Chapter~@ch:varieties of Volume II.

#subhead[The Second Edition] In preparing the paperback edition, I have taken
the liberty of completely retypesetting the book using the enhanced features of
#LaTeX~2#sub[$epsilon$], #AMS\-#LaTeX 1.2 and #XYpic 3.5. Apart from this, I
have corrected those errors of which I am aware. I would like to thank the many
people who have sent me lists of errors, particularly Bill Crawley-Boevey, Steve
Donkin, Jeremy Rickard and Steve Siegel.

The most extensively changed sections are Section 2.2 and 3.1 of Volume I and
Section~@sec:rank-varieties of Volume II, which contained major flaws in the
original edition. In addition, in Section 3.1 of Volume I, I have changed to the
more usual definition of Hopf algebra in which an antipode is part of the
definition, reserving the term bialgebra for the version without an antipode. I
have made every effort to preserve the numbering of the sections, theorems,
references, and so on from the first edition, in order to avoid reference
problems. The only exception is that in Volume I, Definition 3.1.5 has
disappeared and there is now a Proposition 3.1.5. I have also updated the
bibliography and improved the index. If you find further errors in this edition,
please email me at djb\@byrd.math.uga.edu.

#signature[Dave Benson, Athens, September 1997]

#source(11)#subhead[Conventions and Notations]

- Maps will usually be written on the left. In particular, we use the left
  notation for conjugation and commutation: $lconj(g, h) = g h g^(-1)$,
  $[g, h] = g h g^(-1) h^(-1)$, and $lconj(g, H) = g H g^(-1)$.
- We write $G slash H$ to denote the action of $G$ as a transitive permutation
  group on the left cosets of $H$.#idx("$G slash H$")
- We write $H lt.eq_G K$ to denote that "$H$ is $G$-conjugate to a subgroup of
  $K$".#idx("$scripts(lt.eq)_G$") Similarly $h in_G K$ means "$h$ is
  $G$-conjugate to an element of $K$".#idx("$scripts(in)_G$") Thus we write for
  example $limits(plus.o.big)_(g in_G G)$ to denote a direct sum over conjugacy
  classes of elements of $G$.
- The symbol #sym.square.stroked denotes the end of a proof.#idx(
    "$square.stroked$",
  )
- We shall use the usual notations $O_p (G)$ for the largest normal $p$-subgroup
  of $G$, $O^p (G)$ for the smallest normal subgroup of $G$ for which the
  quotient is a $p$-group,#idx("$O_p (G)$, $O^p (G)$") $G^((oo))$ for the
  smallest normal subgroup of $G$ for which the quotient is soluble,#idx(
    "$G^infinity$",
  ) $Phi(P)$ for the _Frattini subgroup_#idx("Frattini subgroup")#idx("$Phi$")
  of a $p$-group $P$, i.e., the smallest normal subgroup for which the quotient
  is elementary abelian, $Z(G)$ for the centre of $G$,#idx("$Z(G)$")
  $Omega_1 (G)$ for the subgroup of an abelian $p$-group $G$ generated by the
  elements of order $p$,#idx("$Omega_1 (G)$") and so on. The _$p$-rank_#idx(
    "$p$-rank",
  )#idx("$r_p (G)$") $r_p (G)$ is defined to be the maximal rank of an
  elementary abelian $p$-subgroup of $G$.
- If $H$ and $K$ are subgroups of a group $G$, then $sum_(H g K)$ will denote a
  sum over a set of double coset#idx("double", "cosets") representatives#idx(
    "$scripts(sum)_(H g K)$",
  ) $g$ of $H$ and $K$ in $G$.
- We shall write $lmodule(Lambda, M_Gamma)$ to denote that $M$ is a
  $Lambda$-$Gamma$-bimodule#idx("bimodule"), i.e., a left $Lambda$-module which
  is simultaneously a right $Gamma$-module in such a way that
  $(lambda m) gamma = lambda(m gamma)$ for all $lambda in Lambda$, $m in M$ and
  $gamma in Gamma$.
- If $G$ is a group of permutations on the set ${1, dots, n}$ and $H$ is another
  group, we write $G wreath H$ for the _wreath product_;#idx("wreath product")
  namely the semidirect product of $G$ with a direct product of $n$ copies of
  $H$. Thus elements of $G wreath H$ are of the form $(pi; h_1, dots, h_n)$ with
  $pi in G$, $h_1, dots, h_n in H$ and multiplication given by
  $
    (pi'; h'_1, dots, h'_n)(pi; h_1, dots, h_n)
    = (pi' pi; h'_(pi(1)) h_1, dots, h'_(pi(n)) h_n).
  $
- If $X$ is a set with a right $G$-action and $Y$ is a set with a left
  $G$-action, then we write $X times_G Y$ for the quotient of $X times Y$ by the
  equivalence relation $(x g, y) tilde (x, g y)$ for all $x in X$, $g in G$,
  $y in Y$.
