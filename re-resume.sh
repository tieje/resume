#!/usr/bin/env bash
pandoc README.md -f markdown -t latex -s -o resume.tex -V colorlinks=true -V linkcolor=blue -V urlcolor=blue && python3 style_resume.py
