#import "../main-defs.typ": source

#let title-page() = {
  set page(header: none, footer: none)
  set par(justify: false, first-line-indent: 0pt)
  source(3)
  v(38mm)
  align(center, {
    text(size: 15pt)[Representations and Cohomology]
    v(1mm)
    text(size: 11pt)[II. Cohomology of groups and modules]
    v(3mm)
    text(size: 11pt)[D. J. Benson]
    linebreak()
    text(size: 10.5pt, style: "italic")[University of Georgia]
    v(1fr)
    text(size: 14pt, tracking: 0.03em)[#smallcaps[Cambridge]]
    linebreak()
    text(size: 8pt, tracking: 0.06em)[UNIVERSITY PRESS]
  })
  v(14mm)
  pagebreak()
}

// The publication data on the back of the title page.
#let title-verso() = {
  set page(header: none, footer: none)
  set par(justify: false, first-line-indent: 0pt, leading: 0.45em)
  set text(size: 8.5pt)
  source(4)
  v(42mm)
  let caps(body) = text(size: 6.5pt, tracking: 0.1em, body)
  let gap = v(2.2mm)
  caps[PUBLISHED BY THE PRESS SYNDICATE OF THE UNIVERSITY OF CAMBRIDGE]
  linebreak()
  [The Pitt Building, Trumpington Street, Cambridge CB2 1RP, United Kingdom]
  gap
  caps[CAMBRIDGE UNIVERSITY PRESS]
  linebreak()
  [The Edinburgh Building, Cambridge CB2 2RU, United Kingdom \
    40 West 20th Street, New York, NY 10011-4211, USA \
    10 Stamford Road, Oakleigh, Melbourne 3166, Australia]
  gap
  [© Cambridge University Press 1991]
  gap
  [This book is in copyright. Subject to statutory exception \
    and to the provisions of relevant collective licensing agreements, \
    no reproduction of any part may take place without \
    the written permission of Cambridge University Press.]
  gap
  [First published 1991 \
    First paperback edition 1998]
  gap
  emph[A catalogue record for this book is available from the British Library]
  gap
  [ISBN 0 521 36135 4 hardback \
    ISBN 0 521 63652 3 paperback]
  v(6mm)
  text(size: 9.5pt)[Transferred to digital printing 2004]
  pagebreak()
}
