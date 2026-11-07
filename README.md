# latex-author

An agent skill for writing, compiling, and reviewing LaTeX documents, with evidence-aware reporting and Vietnamese/English support.

## Install

Download or clone this repository anywhere accessible to your agent. Keep the entire folder together: `SKILL.md` references the bundled scripts, documentation, and templates by relative location.

Tell your agent: “Read `/path/to/latex-author/SKILL.md` and use it to write an experimental report from this project's results.” This explicit loading method does not depend on a particular agent's skill discovery mechanism.

For automatic discovery, follow your agent's own skill installation instructions and install the entire folder. Installation paths and invocation syntax vary by agent; no agent-specific runtime or SDK is required. The agent needs file access, command execution, and image viewing to complete the full workflow. You can also run all helpers directly without an agent.

Install Python 3.9+, a TeX distribution, latexmk, and Poppler. See [platform setup and asset requirements](references/setup.md) for installation commands. The helpers do not install system packages automatically.

```sh
python3 scripts/latex_author.py doctor
python3 scripts/latex_author.py init /path/to/new-report
python3 scripts/latex_author.py build /path/to/new-report/main.tex
python3 scripts/latex_author.py review /path/to/new-report/build/main.pdf
```

Ask for the document language explicitly when needed, for example: “Write the report in Vietnamese” or “Review this existing LaTeX document and fix its layout.”

## Included

- [Skill instructions](SKILL.md) for discovery, writing, compilation, and visual review.
- An editable XeLaTeX report template in English, a table, a vector figure, and a real bibliographic reference.
- Read-only environment checks, non-overwriting project initialization, compilation, and PDF rendering helpers.
- [English demonstration source and PDF](examples/demo/), using explicitly illustrative measurements.
- A separate [Vietnamese example](examples/vietnamese/) for Unicode and diacritic coverage.

`review` generates page images and extracted text; an agent or human must inspect them. Passing automated checks does not certify factual accuracy or visual quality. Existing templates take precedence over the bundled starter.

The repository does not include third-party font binaries, private project data, or an automatic publishing workflow. Source code, template, and example are licensed under MIT; installed dependencies retain their own licenses.

## Academic template references

Use these publisher and venue resources when a document needs an established academic format. Follow the target venue's current author instructions, including the required year, track, review/anonymization mode, page limits, and final submission format. A supplied venue template takes precedence over the bundled starter.

| Format / venue | Template source | Typical use |
| --- | --- | --- |
| IEEE | [IEEE Author Center: authoring tools and templates](https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/) | IEEE conference papers; select the template required by the conference. |
| ACM (`acmart`) | [ACM proceedings templates](https://www.acm.org/publications/proceedings-template) | ACM proceedings; choose the class options specified by the venue. |
| Springer LNCS | [LNCS author instructions and LaTeX proceedings template](https://link.springer.com/series/558/information-for-authors-and-editors) | Computer science conference proceedings in LNCS and related series. |
| Springer Nature (`sn-jnl`) | [Official Springer Nature template on Overleaf](https://www.overleaf.com/latex/templates/springer-nature-latex-template/gsvvftmrppwq) | Journal manuscripts; check the individual journal's instructions and reference style. |
| ACL | [Official ACL style files](https://github.com/acl-org/acl-style-files) | Papers for Association for Computational Linguistics venues; check venue-specific requirements. |
| NeurIPS | [NeurIPS 2026 call for papers and author resources](https://neurips.cc/Conferences/2026/CallForPapers) | Machine learning conference papers; use the style files for the intended edition and track. |

These links are references, not bundled or preinstalled templates. Download the required author kit separately, retain its license, and use its documented engine and build procedure. The `init` command creates only this repository's general report template; it does not select or install the formats above.

## Development verification

```sh
python3 -m unittest discover -s tests -v
```

The integration check compiles and renders a report in a path containing spaces, checks English and Vietnamese text extraction, verifies existing destinations are preserved, and verifies compiler failures are returned. Rendering tools must be runnable, not merely present on PATH. The helper returns 1 for command/dependency failures and 2 when compilation succeeds with log findings requiring review.

Builds ignore ambient latexmk configuration (`-norc`) and disable shell escape. If an existing project depends on custom build rules, inspect those rules and use its understood build command instead of assuming this helper covers it.
