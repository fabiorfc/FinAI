# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path
from finai.readers import CSVDataReader
from finai.processing import TransactionsProcessor, TimeSeriesBuilder, PortfolioPositionValuation


# ---------------------------------------------------------------
# DEFINE PATHS
# ---------------------------------------------------------------
project_root = Path(__file__).resolve().parents[1]
assets_path = project_root / "data" / "assets"
portfolio_path = project_root / "data" / "processed"


# ---------------------------------------------------------------
# READ FILES
# ---------------------------------------------------------------
portfolio = CSVDataReader(
    portfolio_path / "holdings_timeseries.csv"
).read_csv()

assets = CSVDataReader(
    assets_path / "assets.csv"
).read_csv()

# ---------------------------------------------------------------
# MERGE FILES
# ---------------------------------------------------------------
get_portfolio_adjclose = (
    PortfolioPositionValuation(portfolio, assets)
    .portfolio_valuation(col_value = 'adjclose')
)

output = assets_path / "assets_adlclose.csv"
get_portfolio_adjclose.to_csv(output)


