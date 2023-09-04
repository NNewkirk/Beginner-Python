from bs4 import BeautifulSoup

# with open, opens the html file and the 'r' lets me read through it
with open('president.html', 'r') as html_file:

# Content stores the function to read my html file
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    presidents = soup.find_all('a')

    for president in presidents:
        print(president.text)
