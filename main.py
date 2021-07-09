
import requests
from bs4 import BeautifulSoup

URL = ("https://babylonbee.com/news")
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
# r.content: raw html content. html5lib: Specifying the HTML parser. Parse tree


headlines = soup.find_all('article-card')

headlineList = []

for headline in headlines:
        text = str(headline).partition(":title='")[2].partition("'>")[0]
        if (text != ''):
                headlineList.append(text)
                #print(text) - to print out full list of articles in NEWS section

print("\nLatest article: ", headlineList[0])







