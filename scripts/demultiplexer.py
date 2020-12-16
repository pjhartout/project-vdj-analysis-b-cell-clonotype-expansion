#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""demultiplexer.py

This script demultiplex the data, i.e. it creates a separate file for each
cell containing the contigs.

DO NOT RUN MORE THAN ONCE!!!
From: https://github.com/Teichlab/bracer/issues/21

"""
import os

list_of_cells = list()


def main():
    for folder in os.listdir("../data/"):
        if "preprocessed" in folder:
            os.removedirs(folder)

    for folder in os.listdir("../data/"):
        with open(
            f"../data/{folder}/outs/filtered_contig.fasta", "r"
        ) as input:
            for line in input:
                if line.startswith(">"):
                    cell = line.split("-1_contig")[0][1:]
                    list_of_cells.append(cell)

                if not os.path.exists(f"../data/{folder}-preprocessed/"):
                    os.mkdir(f"../data/{folder}-preprocessed/")

                with open(
                    f"../data/{folder}-preprocessed/{cell}.fasta", "a"
                ) as output:
                    output.write(line)

        with open(
            f"../data/{folder}-preprocessed/list_of_cells.txt", "w"
        ) as file:
            file.write(str(list_of_cells))


if __name__ == "__main__":
    main()
