#import "@preview/cetz:0.5.2"
#import "common.typ": grid-diagram
#import "../main-defs.typ": *

// Section 3.1: the guide to the topics of the chapter. Each group of topics,
// one to a line, is gathered by a brace and leads to its target; all the
// targets are gathered by one brace and lead to the chain on the right,
// whose first entry stands at the tip of that brace and whose entries are
// joined by downward arrows. The lines of the groups and of the chain share
// one line spacing; a blank line separates the groups.
#let topic-guide = {
  let groups = (
    (([Hurewicz fibration], [fibre bundle]), [Serre fibration]),
    (
      (
        [group extension],
        [composite functor],
        [pullback of fibrations],
        [(Eilenberg–Moore)],
      ),
      [double complex],
    ),
  )
  let chain = ([filtered complex], [exact couple], [spectral sequence])
  let skip = 1.15em
  // A brace over `n` lines.
  let gather(n) = $stretch(\}, size: #(n * skip))$
  let cells = ()
  let row = 0
  for (topics, target) in groups {
    let n = topics.len()
    for (k, topic) in topics.enumerate() {
      cells.push(grid.cell(x: 0, y: row + k, topic))
    }
    cells.push(grid.cell(x: 1, y: row, rowspan: n, gather(n)))
    cells.push(grid.cell(x: 2, y: row, rowspan: n, [$->$ #target]))
    row += n + 1
  }
  let lines = row - 1
  assert(calc.odd(lines), message: "The large brace points at a line")
  let tip = calc.quo(lines, 2)
  cells.push(grid.cell(x: 3, y: 0, rowspan: lines, gather(lines)))
  cells.push(grid.cell(x: 4, y: tip, $->$))
  for (k, entry) in chain.enumerate() {
    if k > 0 { cells.push(grid.cell(x: 5, y: tip + 2 * k - 1, $arrow.b$)) }
    cells.push(grid.cell(x: 5, y: tip + 2 * k, entry))
  }
  set text(font: "Libertinus Serif")
  grid(
    columns: 6,
    rows: skip,
    column-gutter: (0.3em, 1.5em, 0.3em, 0.4em, 1.2em),
    align: (x, y) => (left, left, left, left, center, center).at(x) + horizon,
    ..cells,
  )
}

// Section 3.1, (iii): the pullback of fibrations of the Eilenberg–Moore
// spectral sequence.
#let pullback-fibrations = grid-diagram(
  (($F$, $E'$, $B'$), ($F$, $E$, $B$)),
  down: (("=", "->", "->"),),
  gap: 9mm,
  row: 9mm,
)

// A page of a first quadrant spectral sequence as the book draws it: a dot at
// each place (p, q) with p < rows.at(q), the axes p and q, and the
// differential of bidegree `degree` from each dot to the dot it reaches.
#let spectral-page(rows, degree) = cetz.canvas(length: 9.3mm, {
  import cetz.draw: *
  let places = rows
    .enumerate()
    .map(((q, n)) => range(n).map(p => (p, q)))
    .join()
  let right = calc.max(..rows) - 1
  let top = rows.len() - 1
  let dot = 0.06
  let gap = 0.3
  set-style(stroke: 0.45pt)
  line((-2 / 3, 0), (right + 1 / 3, 0))
  line((0, -2 / 3), (0, top + 4 / 3))
  content((right + 1 / 3 + gap, 0), $p$, anchor: "west")
  content((0, top + 4 / 3 + gap), $q$, anchor: "south")
  let (a, b) = degree
  let length = calc.sqrt(a * a + b * b)
  for (p, q) in places {
    if (p + a, q + b) in places {
      // The head of the arrow touches the dot it reaches.
      let end = (p + a - dot * a / length, q + b - dot * b / length)
      line(
        (p, q),
        end,
        stroke: 0.4pt,
        mark: (end: ">", fill: black, scale: 0.7),
      )
    }
  }
  for place in places { circle(place, radius: dot, fill: black, stroke: none) }
})

// Section 3.1: the differentials d_2 of bidegree (2, -1) and d_3 of bidegree
// (3, -2) in cohomology, and d^2 of bidegree (-2, 1) in homology.
#let second-page = spectral-page((4, 3, 3), (2, -1))
#let third-page = spectral-page((5, 4, 3), (3, -2))
#let second-homology-page = spectral-page((4, 3, 3), (-2, 1))
