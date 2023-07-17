import requests
from bs4 import BeautifulSoup as BS4
from run_index import run_index
# from news_parser import NewsParser

url = "https://guardian.ng/"

res = requests.get(url)
# print(res.text)

soup = BS4(res.content, "html.parser")
# print(f"{soup} \n\n\n\n\n\n\n\n\n")
# np = NewsParser()

class Crawler():
    """ Crawler class """
    def start(self, url):
        """ Start the crawler and run the indexer """

        res = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1237803624181784694 t2919217341348717815"
        })
        # print(res.text)

        soup = BS4(res.content, "html.parser")

        cleaned = soup.get_text()
        stripped = str(cleaned).strip().replace('\n', '')
        if len(stripped) > 12000:
            content = stripped[1000:-9000]
            category = run_index(content)
            print(stripped)
            return category
        else:
            return run_index(stripped)

# Crawler().start("https://www.vanguardngr.com/2023/07/nigeria-practising-plutocracy-not-democracy-falana/")