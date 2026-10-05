import time
from concurrent.futures import ThreadPoolExecutor

def url_function(url:str):
    print(f"Fetching data from {url}")
    time.sleep(5)
    print(f"Data fetched from {url}",end="\n")
    return f"Data from {url}"

def main() -> None:
    urls = [
        f"https://example.com/api/data{number}"
        for number in range(1, 6)
    ]
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(url_function, urls))
    print(results)


if __name__ == "__main__":
    main()
