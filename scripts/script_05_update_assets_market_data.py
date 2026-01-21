# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path
from finai.readers import CSVDataReader


# ---------------------------------------------------------------
# DEFINE PATHS
# ---------------------------------------------------------------
project_root = Path(__file__).resolve().parents[1]
assets_path = project_root / "data" / "raw"


# ---------------------------------------------------------------
# READ FILES
# ---------------------------------------------------------------
full_assets_list = CSVDataReader(
    assets_path / "assets.csv"
).read_csv()

#columns_list = full_assets_list['symbol']
print(full_assets_list.tail())