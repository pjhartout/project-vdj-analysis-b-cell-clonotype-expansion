# project-vdj-analysis
Repo for the final project of STA426 to be completed by Richard Affolter, Martin Emons and Philip Hartout

## Outline
as this is a collaborative project the outline given by the collaborator is as follows

1. BraCeR workflow set-up
2. Trying to answer the question of "Clonotype frequency and clonal expansion in AP and non AP B and T cells"


## Overview of the project

Input:
- CellRanger Input
- we need to split the filtered_contigs into separate fasta files using the script below
- fasta file per cell (demultiplexed)

Processing:
- custom python script to prepare the data from CellRanger
- bracer

Output:
- sequences (assemble) + graphs of relatedness (summarize)
- output of sbracer assemble = list of BCR for each cell + quantification (reads per sample for each T/BCR) (p230)
- output of bracer summarize = clonotype network, sizes, etc. (p 233)


## Useful links
[FASTA v FASTQ][https://compgenomr.github.io/book/fasta-and-fastq-formats.html]
