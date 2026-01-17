from yahooquery import Ticker

class ExtractAssets:

    def __init__(self, assets_list):
        self.assets_list = assets_list

    def extract(self):

        full_assets_list = []

        for counter, asset in enumerate(self.assets_list.values, start=1):

            print(f'\rExtraindo {counter} / {len(self.assets_list)}: {asset}', end='')

            ticker = Ticker(asset + ".SA")
            data = ticker.history(start='2020-01-10')
            data.reset_index(inplace = True)

            full_assets_list.append(data)

        return full_assets_list