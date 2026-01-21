import numpy as np
import pandas as pd

class AssetsMarketDataFetcher:

    def __init__(self, assets):
        self.assets = assets.copy()
    
    def get_assets_timeseries(self, col_value='adjclose') -> pd.DataFrame:
        if col_value not in self.assets.columns:
            raise ValueError(f"Column '{col_value}' not found")
        dfs = []

        assets_list = self.assets['symbol'].dropna().unique()

        for asset in assets_list:
            asset_df = (
                self.assets
                .loc[self.assets['symbol'] == f'{asset}', ['date', col_value]]
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