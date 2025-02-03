import requests
from bs4 import BeautifulSoup
#URL of a news website (Example: BBC News)
url = "https://www.bbc.com/news"
# Send GET request to the URL
response = requests.get(url)
# print(response.text)
# Check if the requests was successful
if response.status_code == 200:
   print("Page fetched successfully!\n")
   # Parse the HTML content of the page using BeautifulSoup
   soup = BeautifulSoup(response.text, 'html.parser')
   #print (soap)
    # Find headlines (Example: Find all<h3> tags with class 'gs-c-promo-heading__title')
   headlines = soup.find_all('h2', class_='sc-8ea7699c-3')
    #print(headlines)
    #Display the first 5 headlines
   print("Top 5 Headlines:")
   for i, headline in enumerate(headlines[:5]):
        print(f"{i+1}. {headline.get_text()}")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")