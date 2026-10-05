from functools import wraps


def mydecorator(fx):

    @wraps(fx)
    def main(*args, **kwargs):
        print("Before calling the function")
        result = fx(*args, **kwargs)
        print("After calling the function")
        return result
    return main

@mydecorator
def myfunction(url:str, path:str):
    return f"Fetching data from {url}{path}"

if __name__ == "__main__":
    response = myfunction("https://example.com", "/api/data")
    print(response)
