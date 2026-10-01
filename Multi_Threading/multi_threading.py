import time
from concurrent.futures import ThreadPoolExecutor

def url_function(url:str):
    print(f"Fetching data from {url}")
    time.sleep(5)
    print(f"Data fetched from {url}",end="\n")
    return f"Data from {url}"

urls = ["https://example.com/api/data1", "https://example.com/api/data2", "https://example.com/api/data3", "https://example.com/api/data4", "https://example.com/api/data5"]

results=[]
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = executor.map(url_function, urls)
    results.extend(futures)

print(results)