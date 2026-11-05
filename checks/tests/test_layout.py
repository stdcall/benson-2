"""Compile small documents with the book's style and check its layout rules:
numbering and references, lists of parts, the end of a proof, paragraph
indents, right-hand chapter openings and blank pages."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import fitz

ROOT = Path(__file__).resolve().parents[2]

PREAMBLE = (
    '#import "/content/book-style.typ": book-style, recto-break\n'
    '#import "/content/statements.typ": *\n'
    '#import "/content/main-defs.typ": *\n'
    '#show: book-style\n'
)


class Layout(unittest.TestCase):
    def compile(self, body):
        with tempfile.TemporaryDirectory(prefix='benson-layout-',
                                         dir='/tmp') as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'content', root / 'content')
            shutil.copytree(ROOT / 'assets/fonts', root / 'assets/fonts')
            shutil.copyfile(ROOT / 'references.bib', root / 'references.bib')
            (root / 'sample.typ').write_text(PREAMBLE + body)
            result = subprocess.run([
                'typst', 'compile', '--root', str(root),
                '--ignore-system-fonts', '--font-path',
                str(root / 'assets/fonts'), '--input', 'stage=draft',
                str(root / 'sample.typ'), str(root / 'out.pdf')],
                text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, '')
            with fitz.open(root / 'out.pdf') as doc:
                return [(page.get_text('words'), page.get_text())
                        for page in doc]

    def test_numbering_and_references(self):
        pages = self.compile(
            '#counter(heading).update((1,))\n'
            '= Chapter <ch:two>\n'
            '== First <sec:first>\n'
            '#definition[A.] <def:a>\n\n'
            '#lemma[B.] <lem:b>\n\n'
            '#remark[Unnumbered.]\n\n'
            '#theorem[C.] <th:c>\n\n'
            '== Second <sec:second>\n'
            '#corollary[D.] <cor:d>\n\n'
            'See Theorem~@th:c, Corollary~@cor:d, Section~@sec:second and '
            'Chapter~@ch:two.\n')
        text = ' '.join(t for _, t in pages).split()
        joined = ' '.join(text)
        for printed in ('Definition 2.1.1.', 'Lemma 2.1.2.',
                        'Theorem 2.1.3.', 'Corollary 2.2.1.', 'Remark.'):
            self.assertIn(printed.lower(), joined.lower())
        self.assertIn('Theorem 2.1.3, Corollary 2.2.1, Section 2.2 and '
                      'Chapter 2.', joined)

    def test_list_runs_on_after_head_and_proof_mark(self):
        pages = self.compile(
            '#counter(heading).update((0,))\n'
            '= Chapter <ch:one>\n'
            '== Section <sec:one>\n'
            '#lemma[\n  + First part.\n  + Second part.\n] <lem:parts>\n\n'
            '#proof[\n  We have\n  $ a = b. $\n]\n')
        words, text = pages[-1]
        lines = {}
        for w in words:
            lines.setdefault(round(w[1]), []).append(w[4])
        heads = [' '.join(ws) for ws in lines.values()]
        self.assertTrue(any('1.1.1.' in h and '(i)' in h for h in heads),
                        heads)
        square = [w for w in words if w[4] == '□']
        display = [w for w in words if '𝑏' in w[4]]
        self.assertEqual(len(square), 1, text)
        self.assertEqual(len(display), 1, text)
        # The square stands on the line of the closing display.
        self.assertLess(abs(square[0][3] - display[0][3]), 4)

    def test_new_paragraph_indent_after_statement(self):
        pages = self.compile(
            '#counter(heading).update((0,))\n'
            '= Chapter <ch:one>\n'
            '== Section <sec:one>\n'
            '#new-paragraphs[\n'
            '#lemma[Statement.] <lem:one>\n\n'
            'Fresh paragraph after the lemma.\n\n'
            '$ x = y $\n'
            'continuing the sentence.\n]\n')
        words, _ = pages[-1]
        left = min(w[0] for w in words)
        fresh = next(w for w in words if w[4] == 'Fresh')
        cont = next(w for w in words if w[4] == 'continuing')
        self.assertGreater(fresh[0] - left, 5)
        self.assertLess(cont[0] - left, 1)

    def test_chapters_open_on_right_hand_pages(self):
        pages = self.compile(
            '#page(numbering: none)[Cover]\n'
            '#set page(numbering: "1")\n'
            '#counter(page).update(1)\n'
            '#counter(heading).update((0,))\n'
            '= One <ch:one>\n'
            'Text.\n'
            '= Two <ch:two>\n'
            'More text.\n')
        # Cover, 1 (chapter one), 2 (blank), 3 (chapter two).
        self.assertEqual(len(pages), 4)
        self.assertEqual(pages[2][1].strip(), '')
        self.assertIn('Two', pages[3][1])


if __name__ == '__main__':
    unittest.main()
