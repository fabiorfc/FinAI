import pandas as pd

class ExtractAssets:

    def __init__(self, df, assets_col):
        self.df = df.copy()
        self.assets_col = assets_col
    
    def get_assets_list(self):
        return self.df[self.assets_col]