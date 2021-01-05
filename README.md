# project-vdj-analysis
This repository contains the final project of STA426, completed by Richard Affolter, Martin
Emons and Philip Hartout. The goal of this project is to investigate clonal
expansion among B cells donated by patients affected by RRMS (treated with
Natalizumab and untreated), as well as healthy donors. Prior to being subject to
single-cell RNA sequencing, the B cells were incubated with CFSE to assess _in
vitro_ autoproliferation.

## Outline
This project is set up as follows:

1. Introduction
2. EDA
3. Bracer workflow setup details
4. Clonal expansion analysis
5. Conclusion

A full overview, analysis and summary of this project can be found in the [workbooks  directory](/workbooks/).

## Dependencies

### R
Most dependencies are managed through [Packrat](https://rstudio.github.io/packrat/). Use `packrat::restore()` to install R dependencies.

### Python

Python dependencies are managed through [poetry](https://python-poetry.org/). Use `poetry install` to install python dependencies.

## Acknowledgments

The scRNA-seq data was provided by [F. Hoffmann-La Roche Ltd](https://www.roche.com/) and supervised by [Prof. Dr. Mark Robinson](https://www.sib.swiss/mark-robinson-group).
