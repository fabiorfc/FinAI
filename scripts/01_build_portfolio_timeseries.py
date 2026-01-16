# ---------------------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------------------
from pathlib import Path

from finai.readers.csv_data_reader import CSVDataReader
from finai.processing import TransactionsProcessor, TimeSeriesBuilder

def main():
    # ---------------------------------------------------------------
    # PATH
    # ---------------------------------------------------------------
    project_root = Path(__file__).resolve().parents[1]
    
    raw_data_path = project_root / "data" / "raw"
    processed_data_path = project_root / "data" / "processed"

    processed_data_path.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------------
    # LOAD RAW DATA
    # ---------------------------------------------------------------
    raw_dataframe = CSVDataReader(
        raw_data_path / "fiis.csv"
    ).read_csv()


    # ---------------------------------------------------------------
    # PROCESS TRANSACTIONS
    # ---------------------------------------------------------------
    df_processed = (
        TransactionsProcessor(raw_dataframe)
        .parse_dates("Data")
        .aggregate_by_day("Data","Papel","Quantidade")
        .pivot("Data","Papel","Quantidade")
        .get()
    )


    # ---------------------------------------------------------------
    # BUILD TIME SERIES
    # ---------------------------------------------------------------
    df_time_series = (
        TimeSeriesBuilder(df_processed)
        .complete_dates()
        .cumulative_positions()
        .get()
    )


    # ---------------------------------------------------------------
    # WRITE CSV
    # ---------------------------------------------------------------
    output_file = processed_data_path / "holdings_timeseries.csv"
    df_time_series.to_csv(output_file)



if __name__ == "__main__":
    main()
