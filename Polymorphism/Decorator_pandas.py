def pandas_decorator(fx):

    def main(*args):
        response = fx(*args)
        print("Data fetched from pandas")
        response.to_parquet("Polymorphism\\Files\\orders.parquet", index=False)
        return response
    return main

@pandas_decorator
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

response = csv_to_parquet("Polymorphism\\Files\\orders.csv")
print(response.head())