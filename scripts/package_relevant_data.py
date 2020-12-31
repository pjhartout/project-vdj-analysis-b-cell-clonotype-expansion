#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""package_relevant_data.py

This script packages the relevant data from the filtered_BCR_summary folder
to a separate archive.

"""

import os
import dotenv
from tqdm import tqdm
from shutil import copyfile, rmtree

# Load values from .env
DOTENV_KEY2VAL = dotenv.dotenv_values()


def main():
    """Main function
    """
    patients = os.listdir(f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/")
    output_folder = f"{DOTENV_KEY2VAL['HOME_DIR']}/data/summarise_data/"

    if os.path.exists(output_folder):
        rmtree(output_folder)

    os.mkdir(output_folder)

    for patient in tqdm(patients):
        if os.path.exists(output_folder + f"/{patient}"):
            rmtree(output_folder + f"/{patient}")

        src = (
            f"{DOTENV_KEY2VAL['HOME_DIR']}/data/demultiplexed/{patient}/"
            f"{patient}-out/filtered_BCR_summary"
        )

        destination = output_folder + f"{patient}/"

        if not os.path.exists(destination):
            os.mkdir(destination)

        files_to_copy = ["BCR_summary.txt", "clonotype_sizes.txt"]
        for file in files_to_copy:
            copyfile(src + "/" + file, destination + "/" + file)


if __name__ == "__main__":
    main()
