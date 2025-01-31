import requests
# URL of the public API
url = "https://www.freetestapi.com/api/v1/movies"
# Send a GET request to the API
response = requests.get(url)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Data fetched successfully!\n")
    # Prase the JSON data
    data = response.json()
    #Display the first 3 posts
    for post in data[:3]:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Failed to retrieve data. Status Code: (response.sstatus_code)")
