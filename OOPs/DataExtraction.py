import pandas as pd

class DataExt:
    def __init__(self, data:str):
        self.data = data

    def fetch_csv(self, seperator:str):
        df=pd.read_csv(self.data, sep=seperator)
        print(df.head(5))

    def fetch_json(self):
        df=pd.read_json(self.data)
        print(df.head(5))

    def fetch_parquet(self):
        df=pd.read_parquet(self.data)
        print(df.head(5))

    def fetch_tsv(self, seperator:str):
        df=pd.read_csv(self.data, sep=seperator)
        print(df.head(5))

obj1= DataExt("OOPs\\Files\\orders.csv")
obj1.fetch_csv(",")
obj2= DataExt("OOPs\\Files\\orders.json")
obj2.fetch_json()
obj3= DataExt("OOPs\\Files\\orders.parquet")
obj3.fetch_parquet()
obj4= DataExt("OOPs\\Files\\orders.tsv")
obj4.fetch_tsv("\t")