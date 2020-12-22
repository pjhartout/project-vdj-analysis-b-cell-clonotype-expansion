#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""parallel_bracer.py

This executes multiple instances of docker in parallel to execute the bracer pipeline
"""

import subprocess
import os
from joblib import Parallel, delayed

N_JOBS = -1
HOME_DIR = "/home/pjh/Documents/Git/project-vdj-analysis"


def execute_docker_bracer(row, list_of_cells, patient):
    """

    Args:
        row:
        list_of_cells:

    Returns:

    """
    cell = list_of_cells[row].split(".")[0:1]
    os.chdir(f"{HOME_DIR}/data/demultiplexed/{patient}")
    subprocess.call(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{HOME_DIR}/data/demultiplexed/{patient}:/scratch",
            "-w",
            "/scratch",
            "teichlab/bracer",
            "assemble",
            f"{cell[0]}",
            f"{cell[0]}_output",
            "--assembled_file",
            f"{cell[0]}.fasta",
        ]
    )


def main():
    """Description

    Args:
        input_shape (type): description
        num_classes (type): description

    Returns:
        type: description
    """
    list_of_patients = os.listdir(HOME_DIR + "/data/demultiplexed")
    for patient in list_of_patients:
        list_of_cells = os.listdir(f"{HOME_DIR}/data/demultiplexed/{patient}")
        Parallel(n_jobs=N_JOBS, verbose=1)(
            delayed(execute_docker_bracer)(row, list_of_cells, patient)
            for row in range(len(list_of_cells))
        )


if __name__ == "__main__":
    main()
