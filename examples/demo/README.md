# Demonstration

All table measurements are illustrative, not empirical. The template and demo source intentionally match so the checked PDF shows exactly what `init` creates.

Rebuild from the repository root:

```sh
python3 scripts/latex_author.py build examples/demo/main.tex
python3 scripts/latex_author.py review examples/demo/build/main.pdf
```

The committed `main.pdf` was built with XeLaTeX / TeX Live 2022 and latexmk 4.76 on Linux. Its single page was rendered and visually checked for Vietnamese glyphs, table/figure layout, references, and clipping. Other operating systems have documented setup instructions but have not been exercised here.

The bibliography record was checked against https://www.latex-project.org/help/books/ (Leslie Lamport, second edition, 1994, ISBN 978-0201529838).

If a bundled tool shadows a working system executable but fails to run, doctor reports it. Select a working installation through PATH and rerun; do not treat executable presence as success.
