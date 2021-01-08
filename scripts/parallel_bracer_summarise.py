#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""parallel_bracer_summarise.py

This executes multiple instances of docker in parallel to execute the bracer
summarise pipeline
"""

import subprocess
import os
import dotenv
from joblib import Parallel, delayed
from tqdm import tqdm


# Load values from .env
DOTENV_KEY2VAL = dotenv.dotenv_values()

N_JOBS = -1


def execute_docker_bracer(patient):
    """Call docker in a subprocess for each cell

    Args:
        row (list): row containing the cell to be processed
        list_of_cells (list): list of cells containing all UMIs belonging to
        patients
        patient (str): patient to be processed
    Returns:
        envokes docker instance for summarise
    """
    os.chdir(f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/{patient}/")
    subprocess.call(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/"
            f"{patient}/:/scratch",
            "-w",
            "/scratch",
            "teichlab/bracer",
            "summarise",
            f"{patient}-out",
            "--no_networks",
        ]
    )


def main():
    """Main function - lists patients and run summarise via docker in parallel
    for each patient.

    """
    list_of_patients = os.listdir(
        DOTENV_KEY2VAL["HOME_DIR"] + "/data/demultiplexed"
    )
    Parallel(n_jobs=N_JOBS, verbose=1)(
        delayed(execute_docker_bracer)(row) for row in list_of_patients
    )


if __name__ == "__main__":
    main()
