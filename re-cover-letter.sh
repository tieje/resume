#!/usr/bin/env bash
pandoc cover_letter.md -f markdown -t latex -s -o cover_letter.tex && python3 style_cover_letter.py
