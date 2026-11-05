#import "common.typ": edge, grid-diagram
#import "../main-defs.typ": *

// Proof of Lemma 4.5.1: the norm map from G to ℤ/p × G, factored through
// the wreath product, is natural in G.
#let norm-naturality = grid-diagram(
  (
    (
      $H^* (G', FF_p)$,
      $H^* (Sigma_p wreath G', FF_p)$,
      $H^* (ZZ slash p times G', FF_p)$,
    ),
    (
      $H^* (G, FF_p)$,
      $H^* (Sigma_p wreath G, FF_p)$,
      $H^* (ZZ slash p times G, FF_p)$,
    ),
  ),
  across: (
    ((label: $1 wreath -$), (label: $res$)),
    ((label: $1 wreath -$), (label: $res$)),
  ),
  down: (
    (
      (label: $phi.alt^*$),
      (label: $1 wreath phi.alt$),
      (label: $(id times phi.alt)^*$),
    ),
  ),
  gap: 9mm,
  row: 9mm,
)

// Proof of Lemma 4.5.3: the norm map from G to ℤ/p × G factored through
// Σ_p ≀ G and Σ_p × G, with the element x followed down the first two maps.
#let norm-factorisation = grid-diagram(
  (
    ($H^r (G, FF_p)$, $x$, none),
    ($H^(p r) (Sigma_p wreath G, FF_p^((r)))$, $1 wreath x$, none),
    (
      $H^(p r) (Sigma_p times G, FF_p^((r)))$,
      none,
      $H^(p r) (ZZ slash p times G, FF_p)$,
    ),
    (
      $plus.o.big_j H^j (Sigma_p, FF_p^((r))) times.o H^(p r-j) (G, FF_p)$,
      none,
      $plus.o.big_j H^j (ZZ slash p, FF_p) times.o H^(p r-j) (G, FF_p).$,
    ),
  ),
  across: none,
  down: (
    ("->", "|->", none),
    ((label: $res$), none, none),
    ("=", none, "="),
  ),
  extra: (
    edge((0, 2), (2, 2), $res$, "->", label-side: left),
    edge((0, 3), (2, 3), "->"),
  ),
  // The wide lowest row fills the measure: narrow gaps between the columns.
  gap: 3mm,
  row: 9mm,
)
