# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path
from finai.readers import CSVDataReader
from finai.metrics import AssetReturns

# ---------------------------------------------------------------
# DEFINE PATHS
# ---------------------------------------------------------------
project_path = Path(__file__).resolve().parents[1]
assets_path = project_path / "data" / "assets"
output_path = project_path / "data" / "amazonia"

# ---------------------------------------------------------------
# READ FILES
# ---------------------------------------------------------------
portfolio_assets = CSVDataReader(
    assets_path / "portfolio_assets_adjclose.csv"
).read_csv()

assets = CSVDataReader(
    assets_path / "assets_adjclose.csv"
).read_csv()

# ---------------------------------------------------------------
# CALCULATE RETURNS
# ---------------------------------------------------------------
fii_simple_return = AssetReturns(portfolio_assets).get_simple_return('Date')
fii_log_return = AssetReturns(portfolio_assets).get_log_return('Date')

# ---------------------------------------------------------------
# WRITE TABLE
# ---------------------------------------------------------------
fii_simple_return.to_csv(output_path / "portfolio_fii_simple_return.csv")
fii_log_return.to_csv(output_path / "portfolio_fii_log_return.csv")

