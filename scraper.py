from bs4 import BeautifulSoup
import requests

url = "https://docusaurus.io/docs"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now you can work with the parsed HTML
    # For example, you can find all <a> tags and print their href attributes
    for link in soup.find_all('a'):
        print(link.get('href'))
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

# get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)
else:
    print("Failed to retrieve page:", response.status_code)