// The front cover of the paperback in the design of the series: white
// lettering on grey, the author in crimson, and a crimson band with white
// edges and a thin dark centre line, rising at 45° from the foot of the page
// to its right edge.
// Positions are those of the cover, given on a grid of 667 × 1000 units
// over the 6 × 9 in page. A group of lines takes the type size that gives
// its longest line the width it has on the cover.
#let cover() = {
  let w = 6in
  let h = 9in
  let unit = w / 667
  let grey = rgb("797b76")
  let crimson = rgb("b10439")
  let dark = rgb("050000")
  let white = rgb("fffffd")

  // A boundary of the band is the line x + y = c (in units); it meets the
  // foot of the page and its right edge at these points.
  let ends(c) = (((c - 1000) * unit, h), (w, (c - 667) * unit))
  let band(c1, c2, fill) = {
    let (foot1, edge1) = ends(c1)
    let (foot2, edge2) = ends(c2)
    polygon(fill: fill, stroke: none, foot1, edge1, edge2, foot2)
  }
  let rule(c, thickness) = {
    let (foot, edge) = ends(c)
    line(start: foot, end: edge, stroke: thickness + dark)
  }

  // Lines of lettering `(baseline, body)` from the left edge `x`, in the
  // size that sets `widest` to `width` units.
  let lettering(
    x,
    width,
    widest,
    lines,
    weight: "bold",
    fill: white,
  ) = context {
    let style = (font: "Cabin", weight: weight)
    let probe = measure(text(..style, size: 10pt, widest)).width
    let size = 10pt * (width * unit / probe)
    for (baseline, body) in lines {
      place(top + left, dx: x * unit, dy: baseline * unit, text(
        ..style,
        size: size,
        fill: fill,
        top-edge: "baseline",
        bottom-edge: "baseline",
        body,
      ))
    }
  }

  page(
    width: w,
    height: h,
    margin: 0pt,
    fill: grey,
    header: none,
    footer: none,
    numbering: none,
  )[
    #place(top + left, band(1227.5, 1387, white))
    #place(top + left, band(1238, 1369, crimson))
    #place(top + left, rule(1306.5, 0.8pt))
    #let series = [Cambridge studies in advanced mathematics]
    #lettering(39, 444, series, ((137, series),), weight: "regular")
    #lettering(553, 444, series, ((137, [31]),), weight: "regular")
    #lettering(42, 582, [Representations], (
      (244, [Representations]),
      (332, [and]),
      (416, [cohomology]),
    ))
    #lettering(42, 550, [II: Cohomology of groups], (
      (505, [II: Cohomology of groups]),
      (559, [and modules]),
    ))
    #lettering(41, 305, [D. J. BENSON], ((659, [D. J. BENSON]),), fill: crimson)
  ]
}
