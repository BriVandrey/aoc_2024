import numpy as np
import pandas as pd

# read in .txt file from specified path as a list
def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]  # remove new line characters

    return lines