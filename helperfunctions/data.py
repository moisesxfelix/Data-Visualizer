import pandas as pd
import numpy as np

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error Loading CSV File: {e}")
        return None

def count_total_na(data):
    if data is not None:
        return data.isna().sum()
    else:
        return -1
