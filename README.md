# latex-author

An agent skill for writing, compiling, and reviewing LaTeX documents, with evidence-aware reporting and Vietnamese/English support.

## Install

Copy or clone this repository as `latex-author` inside your agent's skills directory. For Codex this is `${CODEX_HOME:-$HOME/.codex}/skills/latex-author`. Keep the entire folder together, then refresh skill discovery.

Install Python 3.9+, a TeX distribution, latexmk, and Poppler. See [platform setup and asset requirements](references/setup.md) for installation commands. The helpers do not install system packages automatically.

```sh
python3 scripts/latex_author.py doctor
python3 scripts/latex_author.py init /path/to/new-report
python3 scripts/latex_author.py build /path/to/new-report/main.tex
python3 scripts/latex_author.py review /path/to/new-report/build/main.pdf
```

Ask your agent: “Use $latex-author to write a Vietnamese experimental report from this project's results” or “Review this existing LaTeX document and fix its layout.”

## Included

- [Skill instructions](SKILL.md) for discovery, writing, compilation, and visual review.
- An editable XeLaTeX report template with Vietnamese text, a table, a vector figure, and a real bibliographic reference.
- Read-only environment checks, non-overwriting project initialization, compilation, and PDF rendering helpers.
- [Demonstration source and PDF](examples/demo/), using explicitly illustrative measurements.

`review` generates page images and extracted text; an agent or human must inspect them. Passing automated checks does not certify factual accuracy or visual quality. Existing templates take precedence over the bundled starter.

The repository does not include third-party font binaries, private project data, or an automatic publishing workflow. Source code, template, and example are licensed under MIT; installed dependencies retain their own licenses.
