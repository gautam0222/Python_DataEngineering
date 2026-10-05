from functools import wraps
from pathlib import Path


def pandas_decorator(fx):

    @wraps(fx)
    def main(*args):
        response = fx(*args)
        print("Data fetched from pandas")
        output_path = Path(__file__).parent / "output" / "orders.parquet"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        response.to_parquet(output_path, index=False)
        return response
    return main

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    input_path = Path(__file__).parent / "decorator_data" / "orders.csv"
    response = csv_to_parquet(str(input_path))
    print(response.head())
