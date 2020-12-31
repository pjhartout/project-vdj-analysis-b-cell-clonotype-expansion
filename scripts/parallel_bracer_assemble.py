#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""parallel_bracer.py

This executes multiple instances of docker in parallel to execute the bracer pipeline
"""

import subprocess
import os
import dotenv
from joblib import Parallel, delayed

# Load values from .env
DOTENV_KEY2VAL = dotenv.dotenv_values()

N_JOBS = -1


def execute_docker_bracer(row, list_of_cells, patient):
    """Call docker in a subprocess for each cell

    Args:
        row (list): row containing the cell to be processed
        list_of_cells (list): list of cells containing all UMIs belonging to
        patients
        patient (str): patient to be processed
    Returns:
        None
    """
    cell = list_of_cells[row].split(".")[0:1]
    os.chdir(
        f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/{patient}/{patient}-out"
    )
    subprocess.call(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"$PWD:/scratch",
            "-w",
            "/scratch",
            "teichlab/bracer",
            "summarise",
            f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/{patient}/{patient}-out",
        ]
    )


def files(path):
    list_of_files = list()
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            list_of_files.append(file)
    return list_of_files


def main():
    """Main function - lists patients and loop through patients. Each cell is
    processed in parallel using joblib

    Args:
        None

    Returns:
        None
    """
    list_of_patients = os.listdir(
        DOTENV_KEY2VAL["HOME_DIR"] + "/data/demultiplexed"
    )
    for patient in list_of_patients:
        list_of_cells = files(
            DOTENV_KEY2VAL["HOME_DIR"] + f"/data/demultiplexed/{patient}"
        )
        Parallel(n_jobs=N_JOBS, verbose=1)(
            delayed(execute_docker_bracer)(row, list_of_cells, patient)
            for row in range(len(list_of_cells))
        )


if __name__ == "__main__":
    main()
