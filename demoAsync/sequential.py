import requests
import time

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url}, Status code: {response.status_code}")

def main():
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com",                
    ]
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

main()