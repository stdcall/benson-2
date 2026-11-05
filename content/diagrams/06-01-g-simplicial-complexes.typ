#import "@preview/cetz:0.5.2"

// Section 6.1: the barycentric subdivision of a 2-simplex, an equilateral
// triangle on its base. The new vertex in the middle of the triangle is
// joined to its three vertices and to the new vertices in the middle of its
// three edges.
#let barycentric-subdivision = cetz.canvas(length: 27.5mm, {
  import cetz.draw: line, set-style
  set-style(stroke: 0.45pt)
  let corners = ((0, 0), (1, 0), (1 / 2, calc.sqrt(3) / 2))
  // The barycentre of some points of the plane.
  let mean(..points) = {
    let points = points.pos()
    range(2).map(i => points.map(p => p.at(i)).sum() / points.len())
  }
  let centre = mean(..corners)
  line(..corners, close: true)
  for (i, corner) in corners.enumerate() {
    let next = corners.at(calc.rem(i + 1, corners.len()))
    line(centre, corner)
    line(centre, mean(corner, next))
  }
})
