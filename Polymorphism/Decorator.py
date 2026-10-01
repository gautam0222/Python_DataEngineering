def mydecorator(fx):

    def main(*args):
        print("Before calling the function")
        result = fx(*args)
        print("After calling the function")
        return result
    return main

@mydecorator
def myfunction(url:str, path:str):
    return f"Fetching data from {url}{path}"

response = myfunction("https://example.com", "/api/data")
print(response)