class api_fetch:
    def fetch_data(self):
        print("Fetching data from API")
        return "API data"

class database_fetch:
    def fetch_data(self):
        print("Fetching data from Database")
        return "Database data"

class data_fetch(api_fetch, database_fetch):
    def fetch_data(self):
        response= api_fetch.fetch_data(self)
        print(f"Data fetched: {response}")

obj= data_fetch()
obj.fetch_data()