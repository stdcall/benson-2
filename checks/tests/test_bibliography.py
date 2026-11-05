"""Compile bibliography fixtures with the production reader and renderer."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import fitz

ROOT = Path(__file__).resolve().parents[2]
BIB_KEY = re.compile(r'(?m)^@[A-Za-z]+\{([^,]+),')
HEADER = (
    '#import "content/book-style.typ": book-style\n'
    '#import "content/statements.typ": bib-item\n'
    '#import "content/bibliography-style.typ": bib-description, bib-part\n'
    '#show: book-style\n'
    '#set page(header: none, footer: none, numbering: "1")\n')
PART = '#bib-part[Further References (added since the first edition):]'
DOI = '10.1016/0022-4049(81)90079-7'


def bib_keys():
    return BIB_KEY.findall((ROOT / 'references.bib').read_text())


def items(*keys):
    return ''.join(f'#bib-item[#bib-description("{key}")] <bib:{key}>\n'
                   for key in keys)


def replace_in_record(bib, key, old, new):
    """Replace a field value inside one record of the .bib text."""
    match = re.search(r'(?ms)^@[A-Za-z]+\{' + key + r',\n.*?^\}\n', bib)
    assert match, key
    record = match[0]
    assert record.count(old) == 1, (key, old)
    return bib[:match.start()] + record.replace(old, new) + bib[match.end():]


class Bibliography(unittest.TestCase):
    def fixture(self, root, body):
        shutil.copytree(ROOT / 'content', root / 'content')
        shutil.copytree(ROOT / 'assets/fonts', root / 'assets/fonts')
        shutil.copyfile(ROOT / 'references.bib', root / 'references.bib')
        shutil.copyfile(ROOT / 'editorial.bib', root / 'editorial.bib')
        (root / 'sample.typ').write_text(HEADER + body)

    def run_typst(self, root, command, *extra):
        result = subprocess.run([
            'typst', command, '--root', str(root), '--ignore-system-fonts',
            '--font-path', str(root / 'assets/fonts'),
            *(['--in', str(root / 'sample.typ'), *extra]
              if command == 'eval' else [str(root / 'sample.typ'), *extra])],
            text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        return result.stdout

    def compile(self, root, name):
        self.run_typst(root, 'compile', str(root / name))
        with fitz.open(root / name) as doc:
            # Word joiners keep an en dash with its neighbours; in a DOI they
            # follow the hyphens, and zero-width spaces follow the slashes.
            text = ' '.join(
                ' '.join(p.get_text().replace('⁠', '')
                         .replace('​', '').split())
                for p in doc)
            # A DOI may break after a slash.
            text = text.replace('/ ', '/')
            links = [link for page in doc for link in page.get_links()]
        return text, links

    def mutate(self, root, *changes):
        bib = (root / 'references.bib').read_text()
        for key, old, new in changes:
            bib = replace_in_record(bib, key, old, new)
        (root / 'references.bib').write_text(bib)

    def test_bib_fields_control_printed_descriptions_and_doi_links(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, items('Adams1978', 'Alperin1981',
                                     'Kratzer1984'))
            before, links = self.compile(root, 'before.pdf')
            self.assertIn(
                'J. F. Adams. Infinite loop spaces. Ann. of Math. Studies 90, '
                'Princeton 1978.', before)
            self.assertIn(
                'J. L. Alperin and L. Evens. Representations, resolutions, '
                'and Quillen’s dimension theorem. J. Pure Appl. Algebra 22 '
                '(1981), 1–9.', before)
            self.assertIn('C. Kratzer et J. Thévenaz.', before)
            uris = {x.get('uri') for x in links}
            self.assertIn('https://doi.org/' + DOI, uris)
            self.assertIn('DOI: ' + DOI, before)
            self.assertNotIn('doi.org/10.1234', ' '.join(map(str, uris)))
            self.mutate(
                root,
                ('Adams1978', 'title = {Infinite loop spaces}',
                 'title = {Bibliography mutation probe}'),
                ('Adams1978', 'author = {Adams, J. F.}',
                 'author = {Changedauthor, I. and Second, J.}'),
                ('Adams1978', 'location = {Princeton}',
                 'location = {Changed place}'),
                ('Alperin1981', 'doi = {' + DOI + '}',
                 'doi = {10.1234/mutation-probe}'),
                ('Kratzer1984', 'usera = {et}', 'usera = {und}'))
            after, links = self.compile(root, 'after.pdf')
            self.assertIn('I. Changedauthor and J. Second. Bibliography '
                          'mutation probe. Ann. of Math. Studies 90, '
                          'Changed place 1978.', after)
            self.assertNotIn('Infinite loop spaces', after)
            self.assertIn('C. Kratzer und J. Thévenaz.', after)
            self.assertIn('DOI: 10.1234/mutation-probe', after)
            self.assertIn('https://doi.org/10.1234/mutation-probe',
                          {x.get('uri') for x in links})

    def test_journal_language_names_and_components_reach_pdf(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, items('Tsygan1983', 'Benson1992b',
                                     'Bogacenko1963', 'Benson1987',
                                     'Munkholm1969', 'Arnold1981',
                                     'Wall1979', 'Grayson1976'))
            before, _ = self.compile(root, 'before.pdf')
            self.assertIn('Uspekhi Mat. Nauk. 38 (1983), 217–218 (= Russ. '
                          'Math. Surveys 38: 2 (1983), 198–199).', before)
            self.assertIn('Bull. London Math. Soc. 24 (1992), 209–235. '
                          'Erratum: Bull. London Math. Soc. 25 (1993), 498.',
                          before)
            self.assertIn('symmetric group. (Russian) Izv. Akad. Nauk. SSSR '
                          'Ser. Mat. 27 (1963), 937–942.', before)
            self.assertIn('Comm. in Algebra 15 (1987), 53–121.', before)
            self.assertIn('Univ. of Illinois at Chicago Circle, June 17–28 '
                          '1968, p. 234–252.', before)
            self.assertIn('J. E. Arnold, Jr. Homological algebra', before)
            self.assertIn('C. T. C. Wall, Ed. Homological group theory.',
                          before)
            self.assertIn('D. Grayson (after D. Quillen). Higher algebraic',
                          before)
            # Fields of related components, the book's spelling of a journal
            # (userb) against the verified abbreviation, the language, an
            # event date, the names.
            self.mutate(
                root,
                ('Tsygan1983t', 'pages = {198--199}', 'pages = {9001--9002}'),
                ('Benson1993c', 'volume = {25}', 'volume = {77}'),
                ('Benson1987', '  userb = {Comm. in Algebra},\n', ''),
                ('Bogacenko1963', 'language = {russian}',
                 'language = {ukrainian}'),
                ('Munkholm1969', 'eventdate = {1968-06-17/1968-06-28}',
                 'eventdate = {1968-07-01/1968-07-12}'),
                ('Arnold1981', 'author = {Arnold, Jr, J. E.}',
                 'author = {Arnold, Sr, J. E.}'),
                ('Wall1979', 'editortype = {Ed}', 'editortype = {Eds}'),
                ('Grayson1976', 'nameaddon = {(after D. Quillen)}',
                 'nameaddon = {(after a probe)}'))
            after, _ = self.compile(root, 'after.pdf')
            self.assertIn('Russ. Math. Surveys 38: 2 (1983), 9001–9002).',
                          after)
            self.assertIn('Erratum: Bull. London Math. Soc. 77 (1993), 498.',
                          after)
            self.assertIn('Comm. Algebra 15 (1987), 53–121.', after)
            self.assertIn('(Ukrainian) Izv. Akad. Nauk. SSSR', after)
            self.assertIn('June 17–28', before)
            self.assertIn('July 1–12 1968', after)
            self.assertIn('J. E. Arnold, Sr. Homological algebra', after)
            self.assertIn('C. T. C. Wall, Eds. Homological group theory.',
                          after)
            self.assertIn('D. Grayson (after a probe). Higher algebraic',
                          after)

    def test_backlinks_are_distinct_pages_and_exclude_internal_references(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, (
                'Mention [@bib:Adams1978] and again [@bib:Adams1978].\n'
                '#footnote[Another mention [@bib:Adams1978].]\n'
                '#pagebreak()\nSecond page [@bib:Adams1978].\n'
                '#pagebreak()\n'
                '#metadata((kind: "bibliography-boundary", enter: true))\n'
                + items('Adams1978') +
                'Internal reference [@bib:Adams1978].\n'
                '#metadata((kind: "bibliography-boundary", enter: false))\n'))
            text, links = self.compile(root, 'book.pdf')
            self.assertIn('[1] J. F. Adams.', text)
            data = json.loads(self.run_typst(root, 'eval',
                'query(metadata).map(it => (value: '
                'if type(it.value) == dictionary { '
                '(..it.value, position: it.location().position()) '
                '} else { it.value }))'))
            backlinks = [x['value'] for x in data
                         if isinstance(x['value'], dict)
                         and x['value'].get('kind') == 'page-reference']
            self.assertEqual([x['description'] for x in backlinks], ['1', '2'])
            self.assertEqual([x['target-position']['page'] for x in backlinks],
                             [1, 2])
            page_links = [x for x in links
                          if x.get('kind') == fitz.LINK_GOTO
                          and x.get('page') in (0, 1)]
            self.assertGreaterEqual(len(page_links), 2)
            from pypdf import PdfWriter
            sys.path.insert(0, str(ROOT / 'scripts'))
            from check_links import check_links, set_link_descriptions
            writer = PdfWriter(root / 'book.pdf', incremental=True)
            set_link_descriptions(writer, backlinks)
            writer.write(root / 'described.pdf')
            report = check_links(root / 'described.pdf', backlinks)
            self.assertEqual(report['semantic_references_checked'], 2)
            self.assertTrue(all(x['destination-offset-pt'] == 18
                                for x in backlinks))
            wrong = [{k: v for k, v in x.items()
                      if k != 'destination-offset-pt'} for x in backlinks]
            with self.assertRaisesRegex(AssertionError, 'wrong target height'):
                check_links(root / 'described.pdf', wrong)

    def test_numbering_runs_through_the_further_references(self):
        with tempfile.TemporaryDirectory(prefix='bib-test-', dir='/tmp') as tmp:
            root = Path(tmp)
            self.fixture(root, (
                items('Adams1978', 'Adams1982') + PART + '\n'
                + items('Adem1992a')))
            text, _ = self.compile(root, 'book.pdf')
            data = json.loads(self.run_typst(root, 'eval', 'query(metadata)'))
            numbers = [x['value']['number'] for x in data
                       if isinstance(x['value'], dict)
                       and x['value'].get('family') == 'bib']
            self.assertEqual(numbers, [[1], [2], [3]])
            self.assertIn('[3] A. Adem. On the geometry', text)

    def test_keys_are_surname_and_year(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        from lint_typst import label_problem
        for key in bib_keys():
            self.assertRegex(key, r'^[A-Z][A-Za-z]*[0-9]{4}[a-z]?$')
            self.assertIsNone(label_problem('bib:' + key), key)

    def test_entry_file_contains_structure_and_keys_only(self):
        source = (ROOT / 'content/80-bibliography.typ').read_text()
        allowed = {'#heading(level: 1, numbering: none)[Bibliography]', PART}
        keys = []
        for line in source.splitlines():
            line = line.strip()
            if (not line or line.startswith(('#import', '//', '#metadata'))
                    or line in allowed):
                continue
            match = re.fullmatch(
                r'#bib-item(?:\(tag: "[0-9]+[a-z]?"\))?'
                r'\[#bib-description\("([A-Za-z][A-Za-z0-9]*)"\)\]'
                r' <bib:\1>', line)
            self.assertIsNotNone(match, line)
            keys.append(match[1])
        # The printed list: [1]-[286] and the further references [287]-[412].
        self.assertEqual(len(keys), 412)
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(keys.index('Zariski1975'), 285)
        self.assertEqual(keys.index('Adem1992a'), 286)
        self.assertLess(source.index('"Zariski1975"'), source.index(PART))
        self.assertLess(source.index(PART), source.index('"Adem1992a"'))
        db_keys = bib_keys()
        self.assertEqual(len(db_keys), len(set(db_keys)))
        related = {key.strip()
                   for group in re.findall(
                       r'(?m)^  related = \{([^}]+)\}',
                       (ROOT / 'references.bib').read_text())
                   for key in group.split(',')}
        self.assertEqual(set(db_keys), set(keys) | related,
                         'Every data record is printed or a related component')
        self.assertFalse(set(keys) & related)
        cited = {key
                 for path in (ROOT / 'content').rglob('*.typ')
                 for key in re.findall(r'@bib:([A-Za-z0-9]+)',
                                       path.read_text())}
        editorial = set(BIB_KEY.findall((ROOT / 'editorial.bib').read_text()))
        self.assertFalse(editorial & set(db_keys))
        self.assertTrue(cited <= set(keys) | editorial,
                        cited - set(keys) - editorial)

    def test_editorial_references_print_every_editorial_record(self):
        editorial = BIB_KEY.findall((ROOT / 'editorial.bib').read_text())
        path = ROOT / 'content/81-editorial-references.typ'
        if not path.exists():
            # No editorial references yet: then there is nothing to print.
            self.assertEqual(editorial, [])
            return
        source = path.read_text()
        printed = re.findall(
            r'#editorial-bib-item\[\s*#bib-description\("([A-Za-z0-9]+)", '
            r'editorial: true\)\s*\] <bib:\1>', source)
        self.assertEqual(printed, sorted(editorial))
        cited = {key
                 for path in (ROOT / 'content').rglob('*.typ')
                 if path.name != '81-editorial-references.typ'
                 for key in re.findall(r'@bib:([A-Za-z0-9]+)',
                                       path.read_text())}
        self.assertTrue(set(editorial) <= cited, set(editorial) - cited)


if __name__ == '__main__':
    unittest.main()
