# Vietnamese example

This companion example checks UTF-8 Vietnamese text and translated abstract, figure, table, and reference labels. The default template and primary demo remain in English. Measurements are illustrative, not empirical.

```sh
python3 scripts/latex_author.py build examples/vietnamese/main.tex
python3 scripts/latex_author.py review examples/vietnamese/build/main.pdf
```

The committed PDF was built with XeLaTeX / TeX Live 2022 and latexmk 4.76 on Linux. Its page was visually checked for diacritics, table/figure layout, references, and clipping.

Bibliography metadata source: https://www.latex-project.org/help/books/ (Leslie Lamport, second edition, 1994, ISBN 978-0201529838).
