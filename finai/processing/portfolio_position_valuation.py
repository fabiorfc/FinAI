import pandas as pd

class PortfolioPositionValuation:

    def __init__(self, portfolio, assets):
        self.portfolio = portfolio.copy()
        self.assets = assets.copy()
    
    def get_assets_values(self,col_value='adjclose') -> pd.DataFrame:
        dfs = []

        for asset in self.portfolio.columns.drop('Date'):
            asset_df = (
                self.assets
                .loc[self.assets['symbol'] == f'{asset}.SA', ['date', col_value]]
                .rename(columns={'date': 'Date', col_value: asset})
                .copy()
            )

            if asset_df.empty:
                continue

            asset_df['Date'] = (
                pd.to_datetime(asset_df['Date'], format='mixed', utc=True)
                .dt.tz_localize(None)
                .dt.normalize()
            )

            asset_df.set_index('Date', inplace=True)
            dfs.append(asset_df)

        if not dfs:
            raise ValueError('Nenhum ativo encontrado')

        return pd.concat(dfs, axis=1).sort_index()

    def portfolio_valuation(self, col_value = 'adjclose') -> pd.DataFrame:
        prices = self.get_assets_values(col_value)

        portfolio = self.portfolio.copy()
        portfolio['Date'] = pd.to_datetime(portfolio['Date'])
        portfolio.set_index('Date', inplace=True)

        common_dates = portfolio.index.intersection(prices.index)

        return portfolio.loc[common_dates] * prices.loc[common_dates]
