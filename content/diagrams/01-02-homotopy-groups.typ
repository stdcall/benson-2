#import "@preview/cetz:0.5.2"
#import "common.typ": cd, node
#import "../main-defs.typ": *

// Proof of Proposition 1.2.3: the commutative law in π_n for n ≥ 2. Each
// square is I^n in its first two coordinates, the first horizontal and the
// second vertical, divided into the regions sent by the composite to f_1, to
// f_2 or to the basepoint (∗); each square is homotopic to the next.
#let commutative-law = {
  let width = 13mm
  let height = 10mm
  // The regions of one square, row by row from the top.
  let square(..rows) = {
    let rows = rows.pos()
    let columns = rows.first().len()
    grid(
      columns: (width / columns,) * columns,
      rows: (height / rows.len(),) * rows.len(),
      stroke: 0.45pt,
      align: center + horizon,
      ..rows.flatten(),
    )
  }
  let squares = (
    square(($f_1$, $f_2$)),
    square(($f_1$, $*$), ($*$, $f_2$)),
    square(($*$, $f_1$), ($f_2$, $*$)),
    square(($f_2$, $f_1$)),
  )
  let row = squares.map(it => (it, $tilde.eq$)).flatten().slice(0, -1)
  cd(spacing: 1mm, ..row.enumerate().map(((x, it)) => node((x, 0), it)))
}

// Figure 1: the map θ : I^n × I → I^n × I, drawn for n = 2 in cabinet
// projection. The front face is I^n: its edges C^(n-1) on the left, top and
// right, the face I^(n-1) at the bottom with its two end points; the depth is
// the factor I. On the left the slices I^n × {t}, t = 0, 1/4, …, 1; on the
// right their images under θ, the planes through the edge I^(n-1) × {0} and
// the point a fraction t of the way along the rest of the boundary of the
// side face: over the top edge, then down the back edge.
#let theta-figure = {
  let slices = (1 / 4, 1 / 2, 3 / 4)
  // The depth axis on the page, per unit of the side of I^n.
  let depth = 0.82
  // Between the back of the left box and the front of the right one.
  let gap = 2.84
  // The point a fraction t of the way along the edges y = 1 and z = 1 of
  // the side face, as (y, z).
  let image-point(t) = if t <= 1 / 2 { (1, 2 * t) } else { (2 - 2 * t, 1) }
  // The face of the unit cube where the coordinate `axis` is `value`.
  let face(axis, value) = {
    let (i, j) = range(3).filter(k => k != axis)
    ((0, 0), (1, 0), (1, 1), (0, 1)).map(((a, b)) => {
      let p = (0, 0, 0)
      p.at(axis) = value
      p.at(i) = a
      p.at(j) = b
      p
    })
  }
  cetz.canvas(length: 9.2mm, z: (depth, depth), {
    import cetz.draw: *
    set-style(
      stroke: 0.5pt,
      line: (mark: (fill: black, scale: 0.55)),
      content: (padding: 0.12),
    )
    // The visible faces, front, top and right, with the labels and the
    // marked end points of I^(n-1).
    let box(shift, traces) = group({
      translate((shift, 0, 0))
      for (axis, value) in ((2, 0), (1, 1), (0, 1)) {
        line(..face(axis, value), close: true)
      }
      traces
      for x in (0, 1) { circle((x, 0, 0), radius: 0.05, fill: black) }
      content((0.5, 0.5, 0), $I^n$)
      content((0, 0.5, 0), $C^(n-1)$, anchor: "east")
      // The factor I, alongside the upper left edge, with its name in a
      // break of the line.
      let (a, b) = ((-0.5, 1, 0), (-0.5, 1, 1))
      content((a, 50%, b), $I$)
      line((a, 38%, b), a, mark: (end: "stealth"))
      line((a, 62%, b), b, mark: (end: "stealth"))
    })
    box(0, for t in slices {
      line((0, 1, t), (1, 1, t), (1, 0, t))
    })
    box(1 + depth + gap, for t in slices {
      let (y, z) = image-point(t)
      line((1, 0, 0), (1, y, z))
      if y == 1 and z < 1 { line((0, 1, z), (1, 1, z)) }
    })
    let middle = (1 + depth + (1 + depth + gap)) / 2
    let height = (1 + depth) / 2
    line(
      (middle - 0.27, height),
      (middle + 0.27, height),
      mark: (end: "stealth"),
      name: "theta",
    )
    content("theta.mid", $theta$, anchor: "south")
  })
}

// Section 1.2: C^(n-1) for n = 2, the boundary of the square I^2 without
// the interior of its lower edge I^1, whose end points are marked.
#let open-square = cetz.canvas(length: 16mm, baseline: (0, 0.5), {
  import cetz.draw: *
  set-style(stroke: 0.5pt)
  line((0, 0), (0, 1), (1, 1), (1, 0))
  for x in (0, 1) { circle((x, 0), radius: 0.03, fill: black) }
})
