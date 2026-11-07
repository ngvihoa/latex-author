# Installation and environment

## Install the skill

Download or clone the entire repository into a location accessible to the agent. Point the agent to `/path/to/latex-author/SKILL.md`; keep scripts, references, and assets together. This explicit loading route requires no vendor-specific skill directory, invocation syntax, SDK, or runtime.

If your agent supports automatic skill discovery, use its documented installation location and refresh procedure. Those conventions are optional integrations, not dependencies of this skill. File access and command execution are needed for authoring/building; image viewing is needed for visual PDF review. Without image viewing, render the pages and disclose that visual review remains incomplete.

Python 3.9+ runs the helpers with no third-party Python dependencies. Run:

```sh
python3 /path/to/latex-author/scripts/latex_author.py doctor
```

Doctor is read-only and exits nonzero if a required component is missing. Review its output before installing anything. Reuse an existing working TeX distribution rather than installing a second one.

## Debian / Ubuntu

For the bundled template and PDF inspection:

```sh
sudo apt-get update
sudo apt-get install latexmk texlive-xetex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended tex-gyre poppler-utils
```

The template uses BibTeX (included in TeX Live). Install `biber` only for documents using biblatex with its Biber backend. No global Python package installation is required.

## macOS

Install MacTeX from its official distribution (or an existing maintained TeX Live installation), then install Poppler via `brew install poppler`. A minimal TeX installation needs latexmk, XeTeX, fontspec, geometry, graphicx, booktabs, hyperref, TeX Gyre fonts, and BibTeX. Run doctor afterward.

## Windows

Install MiKTeX or TeX Live, Python 3, and a Poppler build; add their executable directories to PATH. With MiKTeX, allow required package installation according to local policy, then run doctor. Use native paths supported by Python; the helper does not require Bash. Automatic system installation is deliberately not hidden inside the helper.

## Assets and reproducibility

Bundled assets are original LaTeX source; no font binaries or third-party images are redistributed. TeX Gyre fonts come from the user's TeX distribution. Use only project-provided or appropriately licensed logos, figures, fonts, and data. Record external asset sources and license conditions with the project.

After installing missing packages, rerun doctor and compile a small document. Doctor checks the bundled template's package/font files; it cannot certify every custom document's dependencies. Consult the compiler log for project-specific requirements. Do not silently download replacement fonts or change a mandatory template.

Doctor also runs version probes to catch installed tools that cannot execute (for example, an incompatible binary earlier on PATH). Choose the working TeX/Poppler installation through PATH, then rerun doctor. The helper does not silently replace a failing executable.
