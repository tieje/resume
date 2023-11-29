# TODO

6/26/2023

```tex
\documentclass[letterpaper]{article}

\usepackage[margin=1in]{geometry} % Set 1 inch margins on all sides
\usepackage{fancyhdr} % For customizing headers and footers
```

- [x] convert docx to markdown
- [x] increase width of markdown resume to 8 &frac12;"x11" paper width
- [x] convert markdown to latex
- [x] convert latex to pdf
- [x] work on script to replace certain things automatically
- [x] replace linkedIn resume
- [ ] replace portfolio resume

## Instructions

1. Run commands
```bash
pandoc README.md -f markdown -t latex -s -o resume.tex && python3 style_resume.py
```
2. Copy contents of `resume.tex` to [overleaf.com](https://www.overleaf.com), convert to PDF, and save here.
