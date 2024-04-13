import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page {url}: {response.status_code}")
        return None

def scrape_page(html):
    # Your scraping logic here
    # Use BeautifulSoup to extract the data you need from the HTML
    pass

def main(root_url):
    current_page = root_url
    while current_page:
        html = fetch_page(current_page)
        if html:
            scrape_page(html)
            # Example: Find next page URL
            # Assuming pagination link is in <a> tag with class "next"
            soup = BeautifulSoup(html, 'html.parser')
            next_link = soup.find('a', class_='next')
            if next_link:
                current_page = next_link['href']
            else:
                current_page = None
        else:
            break

if __name__ == "__main__":
    root_url = 'https://docusaurus.io/docs'  # Replace with the root page URL
    main(root_url)