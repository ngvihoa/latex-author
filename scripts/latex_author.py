#!/usr/bin/env python3
"""Portable helpers for latex-author; Python standard library only."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
PACKAGES = ('fontspec.sty', 'geometry.sty', 'graphicx.sty', 'booktabs.sty',
            'hyperref.sty', 'texgyretermes-regular.otf')


def run(args, **kwargs):
    return subprocess.run([str(x) for x in args], check=True, **kwargs)


def doctor(engine):
    missing = []
    for name in ('latexmk', engine, 'bibtex', 'kpsewhich', 'pdftoppm', 'pdftotext'):
        found = shutil.which(name)
        print(f'{name}: {found or "MISSING"}')
        if not found:
            missing.append(name)
        elif name != 'kpsewhich':
            flag = '-v' if name in ('pdftoppm', 'pdftotext') else '--version'
            probe = subprocess.run([found, flag], capture_output=True, text=True)
            if probe.returncode:
                print(f'  Cannot run {name}: {(probe.stderr or probe.stdout).strip()}')
                missing.append(name + ' (not runnable)')
    if shutil.which('kpsewhich'):
        for package in PACKAGES:
            result = subprocess.run(['kpsewhich', package], capture_output=True, text=True)
            ok = result.returncode == 0 and bool(result.stdout.strip())
            print(f'{package}: {"OK" if ok else "MISSING"}')
            if not ok:
                missing.append(package)
    if missing:
        print('See references/setup.md. Missing: ' + ', '.join(missing))
    return bool(missing)


def initialize(destination):
    destination = destination.resolve()
    if destination.exists():
        raise ValueError(f'Destination already exists: {destination}')
    shutil.copytree(ROOT / 'assets' / 'report', destination)
    print(f'Created {destination}; replace illustrative content before delivery.')


def build(source, engine):
    source = source.resolve(strict=True)
    if source.suffix.lower() != '.tex':
        raise ValueError('Expected a .tex entrypoint')
    # Ignore ambient latexmk rc files; preserve document assets beside the source.
    mode = {'xelatex': '-xelatex', 'pdflatex': '-pdf', 'lualatex': '-lualatex'}[engine]
    run(['latexmk', '-norc', mode, '-no-shell-escape', '-interaction=nonstopmode',
         '-halt-on-error', '-file-line-error', '-outdir=build', source.name], cwd=source.parent)
    log = source.parent / 'build' / (source.stem + '.log')
    warnings = ('Overfull', 'undefined', 'Missing character:', 'multiply defined')
    lines = log.read_text(errors='replace').splitlines()
    findings = [line for line in lines if any(word in line for word in warnings)]
    for line in findings:
        print(line)
    print(f'PDF: {source.parent / "build" / (source.stem + ".pdf")}')
    if findings:
        print('Resolve or disclose the log findings before delivery.')
        return 2
    return 0


def review(pdf, destination):
    pdf = pdf.resolve(strict=True)
    destination = destination.resolve() if destination else pdf.parent / 'review' / pdf.stem
    destination.mkdir(parents=True, exist_ok=False)
    run(['pdftotext', '-layout', pdf, destination / 'text.txt'])
    run(['pdftoppm', '-r', '110', '-png', pdf, destination / 'page'])
    print(f'Review files: {destination}. Open every page image; rendering is not visual approval.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    check = commands.add_parser('doctor', help='Check tools and bundled template dependencies')
    check.add_argument('--engine', choices=('xelatex', 'pdflatex', 'lualatex'), default='xelatex')
    init = commands.add_parser('init', help='Copy template to a new directory')
    init.add_argument('destination', type=Path)
    compile_cmd = commands.add_parser('build', help='Compile into build/ beside the entrypoint')
    compile_cmd.add_argument('source', type=Path)
    compile_cmd.add_argument('--engine', choices=('xelatex', 'pdflatex', 'lualatex'), default='xelatex')
    render = commands.add_parser('review', help='Render every PDF page and extract text')
    render.add_argument('pdf', type=Path)
    render.add_argument('--output', type=Path, help='New output directory; must not already exist')
    args = parser.parse_args()
    try:
        if args.command == 'doctor':
            return int(doctor(args.engine))
        if args.command == 'init':
            initialize(args.destination)
        elif args.command == 'build':
            return build(args.source, args.engine)
        elif args.command == 'review':
            review(args.pdf, args.output)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
