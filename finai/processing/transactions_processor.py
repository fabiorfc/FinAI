import pandas as pd

class TransactionsProcessor:

    def __init__(self, df):
        self.df = df.copy()


    def parse_dates(self, col : str, fmt : str = '%d/%m/%Y'):
        self.df[col] = pd.to_datetime(self.df[col], format = fmt, errors = 'coerce')
        return self


    def aggregate_by_day(self, date_col, asset_col, qty_col):
        self.df = self.df[[asset_col, date_col, qty_col]].groupby([date_col, asset_col], as_index=False).sum()
        return self


    def pivot(self, index, columns, values):
        self.df = self.df.pivot(index=index, columns=columns, values=values)
        return self

    def get(self):
        return self.df
