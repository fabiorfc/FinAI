import pandas as pd

class TimeSeriesBuilder:

    def __init__(self, df):
        self.df = df.copy()


    def complete_dates(self, start=None, end=None):
        start = start or self.df.index.min()
        end = end or self.df.index.max()

        full_range = pd.date_range(start, end, freq='D')
        self.df = self.df.reindex(full_range)

        return self


    def cumulative_positions(self):
        self.df = self.df.cumsum().ffill()
        return self

    def get(self):
        return self.df