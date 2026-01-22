import numpy as np

class AssetReturns():

    def __init__(self, asset_table):
        self.asset_table = asset_table.copy()

    def get_simple_return(self, date_col):
        self.asset_table.set_index(date_col, inplace=True)
        return self.asset_table.pct_change()

    def get_log_return(self, date_col):
        self.asset_table.set_index(date_col, inplace=True)
        return np.log(self.asset_table / self.asset_table.shift(1))
