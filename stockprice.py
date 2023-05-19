import requests
from bs4 import BeautifulSoup
import csv

# url, req, soup
url = "https://www.techieempire.tech/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parse")
print(soup.title)

file = csv.writer(open("output.csv", "w"))
file.writerow([soup.title])

# get price of the stocks
def parseprice():
    req = requests.get('https://finance.yahoo.com/quote/YM%3DF?p=YM%3DF')
    soup = BeautifulSoup(req.text, 'lxml')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).findAll('span')
    return price[0].text

    price_div = soup.find('div', {'class': 'D(ib) Mend(20px)'})
    if price_div:
        price_spans = price_div.findAll('span')
        # ... process the price_spans ...

    else:
        print("Error: Price element not found.")
        return None

while True:
    print('The current price of the stock: ' + str(parseprice()))