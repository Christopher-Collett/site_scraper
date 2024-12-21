import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string
        print(f"Title of the page: {title}")
        
        for p in soup.find_all('p'):
            print(p.get_text())
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
