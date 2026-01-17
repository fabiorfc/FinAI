# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path
from finai.readers import CSVDataReader
from finai.processing import TransactionsProcessor, TimeSeriesBuilder

# ---------------------------------------------------------------
# READ FILES
# ---------------------------------------------------------------
project_root = Path(__file__).resolve().parents[1]
assets_path = project_root / "data" / "assets"
portfolio_path = project_root / "data" / "processed"

portfolio = CSVDataReader(
    portfolio_path / "holdings_timeseries.csv"
).read_csv()

assets = CSVDataReader(
    assets_path / "assets.csv"
).read_csv()

# ---------------------------------------------------------------
# MERGE FILES
# ---------------------------------------------------------------

asset_values = assets.query("symbol == 'XPLG11.SA'")[['date','adjclose']]


print(portfolio.tail())


