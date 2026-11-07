"""Behavioral checks; integration test requires the documented TeX/Poppler tools."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'latex_author.py'


class CliTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True)

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'report with spaces'
            self.assertEqual(self.call('init', target).returncode, 0)
            source = target / 'main.tex'
            source.write_text('user content')
            self.assertNotEqual(self.call('init', target).returncode, 0)
            self.assertEqual(source.read_text(), 'user content')

    def test_missing_source_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertNotEqual(self.call('build', Path(tmp) / 'missing.tex').returncode, 0)

    @unittest.skipUnless(all(shutil.which(x) for x in ('xelatex', 'latexmk', 'pdftoppm', 'pdftotext')),
                         'TeX and Poppler required')
    def test_build_render_and_compiler_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'report with spaces'
            self.assertEqual(self.call('init', target).returncode, 0)
            result = self.call('build', target / 'main.tex')
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            pdf = target / 'build' / 'main.pdf'
            self.assertTrue(pdf.read_bytes().startswith(b'%PDF'))
            output = Path(tmp) / 'render'
            result = self.call('review', pdf, '--output', output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(list(output.glob('page-*.png')))
            self.assertIn('Mục tiêu', (output / 'text.txt').read_text())
            self.assertNotEqual(self.call('review', pdf, '--output', output).returncode, 0)
            (target / 'main.tex').write_text('\\documentclass{article}\\begin{document}\\undefinedcommand\\end{document}')
            self.assertNotEqual(self.call('build', target / 'main.tex').returncode, 0)


if __name__ == '__main__':
    unittest.main()
