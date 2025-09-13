# web_scraping.py
"""
Web Scraping Example - ICC Cricket Website
This script uses requests + BeautifulSoup to scrape
headings and text content from the ICC Cricket website.
"""

import requests
from bs4 import BeautifulSoup

# Step 1: Send GET request to the ICC Cricket homepage
url = "https://www.icc-cricket.com/"
response = requests.get(url)

# Step 2: Check if request was successful (status 200 = OK)
if response.status_code == 200:
    print("I Successfully Connected to ICC Cricket website!!!")
    soup = BeautifulSoup(response.content, "html.parser") ## Parse the HTML content of the page

    # Extract <title> tag -
    print("\n=== Page Title ===")
    print(soup.title.get_text(strip=True))

    #  Extract all <h1> tags (main headings) -
    print("\n--- H1 Tags (Main Headings) ---")
    for h1 in soup.find_all("h1"):
        print(h1.get_text(strip=True))

    # - Extract all <h2> tags (subheadings) -
    print("\n--- H2 Tags (Subheadings) ---")
    for h2 in soup.find_all("h2")[:10]:  # limit to top 10
        print(h2.get_text(strip=True))

    # -- Extract first few <p> tags (paragraphs) --
    print("\n--- P Tags (Paragraphs) ---")
    for p in soup.find_all("p")[:15]:  # limit to first 15
        print(p.get_text(strip=True))

else:
    print(f"Failed to retrieve page,maybe try a different url!?!, status code: {response.status_code}")
