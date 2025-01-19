"""Contains commonly used functions, eg. working with csv files."""

import pandas as pd

def open_csv(file):
    """Opens the dataset"""
    try:
        df = pd.read_csv(file, sep=",")
        return df
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Error: File '{file}' not found. Please provide a valid file path."
        ) from exc
