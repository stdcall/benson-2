#import "@preview/cetz:0.5.2"

// Section 7.4: the Dynkin diagram of type $C_n$ of the symplectic group, its
// vertices labelled by the dimensions of the isotropic subspaces whose
// stabilisers are the corresponding maximal parabolic subgroups. The vertices
// are the simple roots along the chain, given by their squared lengths;
// consecutive roots are joined by a bond whose multiplicity is the ratio of
// their squared lengths, with an arrowhead pointing to the shorter root. The
// omitted middle of the chain, after the vertex `gap`, is shown by dots.
#let dynkin-chain(lengths, labels, gap: none, title: none) = cetz.canvas(
  length: 1mm,
  {
    import cetz.draw: circle, content, line, set-style
    assert(lengths.len() == labels.len())
    set-style(stroke: 0.45pt)
    // Distance between vertices, the separation of the lines of a multiple
    // bond and the half-length and half-width of its arrowhead.
    let step = 9.1
    let separation = 0.5
    let (head, spread) = (1.6, 0.65)
    let point(i) = (i * step, 0)
    for i in range(lengths.len() - 1) {
      let (a, b) = (lengths.at(i), lengths.at(i + 1))
      let middle = (i + 0.5) * step
      if i == gap {
        content((middle, 0), $dots.c$)
        continue
      }
      let multiplicity = calc.quo(calc.max(a, b), calc.min(a, b))
      assert(multiplicity in (1, 2, 3))
      for k in range(multiplicity) {
        let offset = (k - (multiplicity - 1) / 2) * separation
        line((i * step, offset), ((i + 1) * step, offset))
      }
      if multiplicity > 1 {
        // The arrowhead points from the longer root to the shorter one.
        let direction = if a > b { 1 } else { -1 }
        let tip = (middle + direction * head, 0)
        line((middle - direction * head, spread), tip)
        line((middle - direction * head, -spread), tip)
      }
    }
    for i in range(lengths.len()) {
      circle(point(i), radius: 0.42, fill: black, stroke: none)
    }
    // The labels in smaller type under the vertices, each over the word
    // "space", and the title on the left of the first line.
    let label-size = 0.72em
    for (i, label) in labels.enumerate() {
      content(
        (i * step, -3.4),
        anchor: "north",
        text(size: label-size, align(center)[#label \ space]),
      )
    }
    if title != none {
      content((-step, -3.4), anchor: "north", text(size: label-size, title))
    }
  },
)

// The maximal parabolic subgroups of $Sp_(2n) (FF_q)$ as stabilisers of the
// isotropic $n$-, $(n-1)$-, $(n-2)$-, …, 2- and 1-spaces: the long root
// $alpha_n$ first, then the short roots.
#let isotropic-dynkin = dynkin-chain(
  (2, 1, 1, 1, 1),
  ([$n$-], [$n$–1-], [$n$–2-], [2-], [1-]),
  gap: 2,
  title: [isotropic],
)
