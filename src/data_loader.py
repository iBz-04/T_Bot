import pandas as pd
import os
from config import CSV_PATH

_df = None

def get_data():
    global _df
    if _df is None:
        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(f"CSV file not found at: {CSV_PATH}")
        
        _df = pd.read_csv(CSV_PATH)
        # Ensure column names exist before renaming
        if all(col in _df.columns for col in ['ENLEM', 'BOYLAM', 'AD']):
            _df = _df.rename(columns={'ENLEM': 'lat', 'BOYLAM': 'lon', 'AD': 'name'})
        else:
            print("Warning: Expected columns not found in CSV. Available columns:", _df.columns)
            
    return _df
