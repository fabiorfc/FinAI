# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path
from finai.readers import CSVDataReader
from finai.market import AssetsMarketDataFetcher

# ---------------------------------------------------------------
# DEFINE PATHS
# ---------------------------------------------------------------
project_root = Path(__file__).resolve().parents[1]
assets_path = project_root / "data" / "raw"
output_path = project_root / "data" / "assets"


# ---------------------------------------------------------------
# READ FILES
# ---------------------------------------------------------------
full_assets_list = CSVDataReader(
    assets_path / "assets.csv"
).read_csv()


# ---------------------------------------------------------------
# FETCH ASSETS AND EXTRACT VALUES
# ---------------------------------------------------------------
fetcher = AssetsMarketDataFetcher(full_assets_list)
full_adjclose_assets_list = fetcher.get_assets_timeseries('adjclose')


# ---------------------------------------------------------------
# WRITE FILES
# ---------------------------------------------------------------
output = output_path / "assets_adlclose.csv"
full_adjclose_assets_list.to_csv(output_path)