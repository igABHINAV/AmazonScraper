import csv
import requests
from bs4 import BeautifulSoup

n = input()
url = f"https://www.amazon.com/s?k={n}&crid=245VMT1RXU1H9&sprefix=rocke%2Caps%2C491&ref=nb_sb_noss_2"
headers = {
    'user-agent': '',
    'Accept-Language': 'en-US,en;q=0.5'
}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.content, 'html.parser')
output = soup.find_all('span', attrs={"class": "a-size-base-plus a-color-base a-text-normal"})

# Specify the CSV file name which here is output.csv
csv_filename = "output.csv"

# Write the scraped data to the CSV file
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Title"])  # Write header row

    for item in output:
        writer.writerow([item.text.strip()])
