import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_single_page(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text()
                return data
    except Exception as e:
        raise e
    
async def fetch_all_pages(root_url):
    text = []
    current_page = root_url
    while current_page:
        print(current_page)
        data = await fetch_single_page(current_page)

        soup = BeautifulSoup(data, "html.parser")
        for link in soup.find_all("a", href=True):
            if link["href"].startswith("/"):
                current_page = f"{root_url}{link['href']}"
            else:
                current_page = None
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        text.extend(soup.get_text())

    return "".join(text)

if __name__ == "__main__":
    root_url = 'https://docusaurus.io/docs'  # Replace with the root page URL
    text = asyncio.run(fetch_all_pages(root_url))
    print(text)  # Pass the root URL