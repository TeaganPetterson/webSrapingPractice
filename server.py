import requests
from bs4 import BeautifulSoup
import time

# URL of the website you want to scrape
url = 'https://backoffice.linqqs.com/#nbc'  

# Replace this with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

time.sleep(5)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the titles of articles (modify as needed)
    article_titles = soup.find_all('h1') 
    body = soup.body
    first = body.find(id='main-wrapper')
    second = first.find(class_="MBanimate fadeInDown splash background-white")
    
    print(body)
    
    for title in article_titles:
        print(body)
        
    # for input in inputs:
    #     print("input")

else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
