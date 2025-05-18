from bs4 import BeautifulSoup
import csv
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
import random

# URL of the Trustpilot page to scrape
URL = 'https://uk.trustpilot.com/review/paystream.co.uk'
# Total number of pages to scrape
TOTAL_PAGES: int = 167
reviews = []

# Initialize undetected Chrome browser to avoid bot detection
driver = uc.Chrome(log_level=0)

# Loop through each review page
for page in range(1, TOTAL_PAGES + 1):
    driver.get(URL + '?page=' + str(page))
    sleep(1)

    # Scroll down to load more reviews (simulate user behavior)
    for i in range(1, 6):
        driver.execute_script("window.scrollBy(0, 700);")
        sleep(0.03)

    # Parse the loaded page with BeautifulSoup
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    divs = soup.find_all('div', class_='styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ')
    
    # Extract data from each review card
    for div in divs:
        try:
            title = div.find('h2').get_text().strip()
            description = div.find('section').find('p').get_text().strip()
            rating = div.find_all('img')[-1]['alt'][6]
            travel_date = div.find('section').find('p', attrs={'data-service-review-date-of-experience-typography': 'true'}).get_text().replace('"', '')
            review_date = div.find('time').get_text().strip()
            reviews.append({
                'title': title,
                'description': description,
                'rating': rating,
                'travel_date': travel_date,
                'review_date': review_date
            })
        except:
            # Skip this review if any field is missing or parsing fails
            pass
    print(f'Page: {page}')  # Progress indicator

# Save all collected reviews to a CSV file
with open(f'{URL.split("/")[-1]}_trustpilot.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description', 'rating', 'travel_date', 'review_date'])
    writer.writeheader()
    for review in reviews:
        writer.writerow(review)
