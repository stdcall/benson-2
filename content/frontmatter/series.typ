#import "../main-defs.typ": source

// The publisher's list of the series, facing the title page.
#let series-page() = {
  set page(header: none, footer: none)
  set par(justify: false, first-line-indent: 0pt, leading: 0.3em)
  source(2)
  v(12mm)
  emph[Already published]
  v(1mm)
  set text(size: 7.5pt)
  let volumes = (
    (1, [W.M.L. Holcombe _Algebraic automata theory_]),
    (2, [K. Petersen _Ergodic theory_]),
    (3, [P.T. Johnstone _Stone spaces_]),
    (4, [W.H. Schikhof _Ultrametric calculus_]),
    (5, [J.-P. Kahane _Some random series of functions, 2nd edition_]),
    (6, [H. Cohn _Introduction to the construction of class fields_]),
    (
      7,
      [J. Lambek & P.J. Scott _Introduction to higher-order categorical logic_],
    ),
    (8, [H. Matsumura _Commutative ring theory_]),
    (
      9,
      [C.B. Thomas _Characteristic classes and the cohomology of finite
        groups_],
    ),
    (10, [M. Aschbacher _Finite group theory_]),
    (11, [J.L. Alperin _Local representation theory_]),
    (12, [P. Koosis _The logarithmic integral I_]),
    (13, [A. Pietsch _Eigenvalues and s-numbers_]),
    (
      14,
      [S.J. Patterson _An introduction to the theory of the Riemann
        zeta-function_],
    ),
    (15, [H.J. Baues _Algebraic homotopy_]),
    (
      16,
      [V.S. Varadarajan _Introduction to harmonic analysis on semisimple Lie
        groups_],
    ),
    (17, [W. Dicks & M. Dunwoody _Groups acting on graphs_]),
    (
      18,
      [L.J. Corwin & F.P. Greenleaf _Representations of nilpotent Lie groups and
        their applications_],
    ),
    (19, [R. Fritsch & R. Piccinini _Cellular structures in topology_]),
    (20, [H. Klingen _Introductory lectures on Siegel modular forms_]),
    (22, [M.J. Collins _Representations and characters of finite groups_]),
    (24, [H. Kunita _Stochastic flows and stochastic differential equations_]),
    (25, [P. Wojtaszczyk _Banach spaces for analysts_]),
    (
      26,
      [J.E. Gilbert & M.A.M. Murray _Clifford algebras and Dirac operators in
        harmonic analysis_],
    ),
    (27, [A. Fröhlich & M.J. Taylor _Algebraic number theory_]),
    (28, [K. Goebel & W.A. Kirk _Topics in metric fixed point theory_]),
    (29, [J.F. Humphreys _Reflection groups and Coxeter groups_]),
    (30, [D.J. Benson _Representations and cohomology I_]),
    (31, [D.J. Benson _Representations and cohomology II_]),
    (
      32,
      [C. Allday & V. Puppe _Cohomological methods in transformation groups_],
    ),
    (33, [C. Soulé et al _Lectures on Arakelov geometry_]),
    (34, [A. Ambrosetti & G. Prodi _A primer of nonlinear analysis_]),
    (
      35,
      [J. Palis & F. Takens _Hyperbolicity, stability and chaos at homoclinic
        bifurcations_],
    ),
    (37, [Y. Meyer _Wavelets and operators I_]),
    (38, [C. Weibel _An introduction to homological algebra_]),
    (39, [W. Bruns & J. Herzog _Cohen-Macaulay rings_]),
    (40, [V. Snaith _Explicit Brauer induction_]),
    (41, [G. Laumon _Cohomology of Drinfeld modular varieties I_]),
    (42, [E.B. Davies _Spectral theory and differential operators_]),
    (43, [J. Diestel, H. Jarchow & A. Tonge _Absolutely summing operators_]),
    (44, [P. Mattila _Geometry of sets and measures in Euclidean spaces_]),
    (45, [R. Pinsky _Positive harmonic functions and diffusion_]),
    (
      46,
      [G. Tenenbaum _Introduction to analytic and probabilistic number theory_],
    ),
    (
      47,
      [C. Peskine _An algebraic introduction to complex projective geometry I_],
    ),
    (48, [Y. Meyer & R. Coifman _Wavelets and operators II_]),
    (49, [R. Stanley _Enumerative combinatorics_]),
    (50, [I. Porteous _Clifford algebras and the classical groups_]),
    (51, [M. Audin _Spinning tops_]),
    (52, [V. Jurdjevic _Geometric control theory_]),
    (53, [H. Voelklein _Groups as Galois groups_]),
    (54, [J. Le Potier _Lectures on vector bundles_]),
    (55, [D. Bump _Automorphic forms_]),
    (56, [G. Laumon _Cohomology of Drinfeld modular varieties II_]),
    (60, [M. Brodmann & R. Sharp _Local cohomology_]),
  )
  grid(
    columns: (2em, 75mm),
    row-gutter: 0.3em,
    ..volumes
      .map(((n, entry)) => (
        str(n),
        par(hanging-indent: 0pt, entry),
      ))
      .flatten(),
  )
  pagebreak()
}
