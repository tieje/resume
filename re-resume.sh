#!/usr/bin/env bash
pandoc README.md -f markdown -t latex -s -o resume.tex && python3 style_resume.py
