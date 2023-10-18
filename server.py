import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://backoffice.linqqs.com/#nbc'

# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

# Send an HTTP GET request to the URL using the headless browser
driver.get(url)

# Wait for a specific element to load (you can modify this to fit your needs)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'main-wrapper')))

# Get the page source after it has loaded
page_source = driver.page_source

# Close the headless browser
driver.quit()

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

# Find and extract the titles of articles (modify as needed)
article_titles = soup.find_all('div')

inputForm = driver.find_element(By.ID, "loginName")

for title in article_titles:
    print(title.text)
    
if inputForm:
    print("Found Input")
