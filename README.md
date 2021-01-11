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
5. Isotype analysis
6. Discussion
7. Summary

A full overview, analysis and summary of this project can be found in the [workbooks  directory](/workbooks/).

The project was organised via the `bookdown` package from R. The chapters (as defined above) were added as children to the `index.Rmd`. Knitting this project yields the entire project with chapters. Alternatively you can select the first html `1-introduction.html` which should allow you to navigate through the project via the outline at the top of the page.

## Dependencies

### R
Most dependencies are managed through [renv](https://rstudio.github.io/renv). Use `renv::restore()` to install R dependencies. Make sure you enable `Bioc software` in `setRepositories()` to allow to install `Bioconductor` packages using `install.packages()`.

### Python

Python dependencies are managed through [poetry](https://python-poetry.org/). Use `poetry install` in the project home directory to install python dependencies.

### .env support

All the scripts in this project use a `.env` file for host-agnostic execution.

## Acknowledgments

The scRNA-seq data was provided by [F. Hoffmann-La Roche Ltd](https://www.roche.com/) and supervised by [Prof. Dr. Mark Robinson](https://www.sib.swiss/mark-robinson-group).
