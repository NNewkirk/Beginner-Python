# This program is from a tutorial by "Tech With Tim", I added a few things I wanted to try
from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-3x-12g-oc/p/N82E16814137631?Item=N82E16814137631"

result = requests.get(url)

# html.parser is built in to BeauitfulSoup, but lxml is faster

# doc = BeautifulSoup(result.text, "html.parser")
doc = BeautifulSoup(result.text, 'lxml')

# This searches for the dollar signs on the website, which pulls up the 4 different prices for gpu choices
prices = doc.find_all(string='$')

# This chose the first price, as it is the price for the specific GPU I am looking for
parent = prices[0].parent

# Finally this removes all the fluff except for the strong portion of the code
strong = parent.find("strong")

# adding .string removes <strong> </strong>, leaving just the price ie
print("The price for this GPU is $", strong.string)
