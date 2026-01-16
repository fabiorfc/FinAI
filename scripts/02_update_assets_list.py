# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path

from finai.readers.csv_data_reader import CSVDataReader
from finai.processing import ExtractAssets


def main():
    # ---------------------------------------------------------------
    # IMPORT PATH
    # ---------------------------------------------------------------
    project_root = Path(__file__).resolve().parents[1]

    assets_path = project_root / "data" / "raw"
    write_Path = project_root / "data" / "processed"

    assets_path.mkdir(parents=True, exist_ok=True)


    # ---------------------------------------------------------------
    # LOAD DATA
    # ---------------------------------------------------------------
    raw_dataframe = CSVDataReader(
        assets_path / "Lista_FII.csv"
    ).read_csv()


    # ---------------------------------------------------------------
    # GET ASSETS LIST
    # ---------------------------------------------------------------
    assets_list = ExtractAssets(raw_dataframe, 'Código').get_assets_list()


    # ---------------------------------------------------------------
    # WRITE ASSETS
    # ---------------------------------------------------------------
    #print(assets_list)
    output_file = write_Path / "assets_list.csv"
    assets_list.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()

