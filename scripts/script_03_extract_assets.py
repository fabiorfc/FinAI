import pandas as pd
from pathlib import Path
from finai.readers import CSVDataReader
from finai.extractors import ExtractAssets


# ---------------------------------------------------------------
# PATH
# ---------------------------------------------------------------
project_root = Path(__file__).resolve().parents[1]

processed_data_path = project_root / "data" / "processed"
output_path = project_root / "data" / "raw"

# ---------------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------------
assets_list = CSVDataReader(
    processed_data_path / "assets_list.csv"
).read_csv()


# ---------------------------------------------------------------
# EXTRACT ASSETS
# ---------------------------------------------------------------
full_assets_list = ExtractAssets(assets_list).extract()
full_assets_list = pd.concat(full_assets_list)


# ---------------------------------------------------------------
# WRITE ASSETS
# ---------------------------------------------------------------
output = output_path / "assets.csv"
full_assets_list.to_csv(output, index=False)
