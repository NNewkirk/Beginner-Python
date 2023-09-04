from bs4 import BeautifulSoup
import requests

# the request asks the website owner if I can scrape information off the website (200 means yes)
html_text = requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states').text

# now its using lxml as my parser in order to take the html code of the website and read it
soup = BeautifulSoup(html_text, 'lxml')

country = soup.find_all('table')

print(country)

