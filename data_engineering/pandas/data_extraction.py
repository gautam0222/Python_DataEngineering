from pathlib import Path

import pandas as pd


class DataExtractor:
    def __init__(self, data: str | Path):
        self.data = Path(data)

    def fetch_csv(self, separator: str = ",") -> pd.DataFrame:
        df = pd.read_csv(self.data, sep=separator)
        print(df.head(5))
        return df

    def fetch_json(self) -> pd.DataFrame:
        df = pd.read_json(self.data)
        print(df.head(5))
        return df

    def fetch_parquet(self) -> pd.DataFrame:
        df = pd.read_parquet(self.data)
        print(df.head(5))
        return df

    def fetch_tsv(self, separator: str = "\t") -> pd.DataFrame:
        df = pd.read_csv(self.data, sep=separator)
        print(df.head(5))
        return df

def main() -> None:
    sample_data = Path(__file__).parent / "sample_data"
    DataExtractor(sample_data / "orders.csv").fetch_csv()
    DataExtractor(sample_data / "orders.json").fetch_json()
    DataExtractor(sample_data / "orders.parquet").fetch_parquet()
    DataExtractor(sample_data / "orders.tsv").fetch_tsv()


if __name__ == "__main__":
    main()
