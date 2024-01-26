#!/usr/bin/env bash
pandoc fin-resume.md -f markdown -t latex -s -o fin-resume.tex -V colorlinks=true -V linkcolor=blue -V urlcolor=blue && python3 style_fin_resume.py
