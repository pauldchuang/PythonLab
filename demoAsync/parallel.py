import asyncio
import aiohttp
import time

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Fetched {url}, Status code: {response.status}")
            return await response.text()

async def main():
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
    await asyncio.gather(*(fetch_url(url) for url in urls))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

asyncio.run(main())