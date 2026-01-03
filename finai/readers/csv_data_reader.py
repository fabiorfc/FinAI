from pathlib import Path
import pandas as pd


class CSVDataReader:

    def __init__(self, filename: str):
        self.filename = filename

    def read_csv(self):
        project_root = Path(__file__).resolve().parents[2]
        path = project_root / "data" / "raw" / self.filename
        return pd.read_csv(path)
