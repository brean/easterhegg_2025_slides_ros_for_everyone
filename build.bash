#!/bin/bash
python3 easter.py 
pdflatex main.tex
# run pdflatex again to use pre-calculated values like page numbers or references
pdflatex main.tex
