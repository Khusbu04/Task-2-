# Assignment Extract All Links from a Webpage
# Problem: Extract and print all links (<a> tags) from a webpage.
import requests
from bs4 import BeautifulSoup

# URL of the Forbes page you want to scrape
url = 'https://www.forbes.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract titles and articles
    headlines = soup.find_all('h2', class_='topline-heading')
    print("Top 5 Headlines:")
    for i, headline in enumerate(headlines[:5]):
        print(f"{i+1}. {headline.get_text()}")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")
