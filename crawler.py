import requests
from bs4 import BeautifulSoup as BS4
from run_index import run_index

# url = "https://guardian.ng/"

# res = requests.get(url)
# # print(res.text)
# soup = BS4(res.content, "html.parser")


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
            content = stripped[500:-6000]
            # print("content:", len(content))
            # print("stripped:", len(stripped))
            category = run_index(content)
            # print(content)
            return category
        elif len(stripped) > 10000:
            content = stripped[500:-4500]
            # print("content:", len(content))
            # print("stripped:", len(stripped))
            category = run_index(content)
            # print(content)
            return category
        elif len(stripped) > 8000:
            content = stripped[500:-3000]
            # print("content:", len(content))
            # print("stripped:", len(stripped))
            category = run_index(content)
            # print(content)
            return category
        elif len(stripped) > 6000:
            content = stripped[500:-1500]
            # print("content:", len(content))
            # print("stripped:", len(stripped))
            category = run_index(content)
            # print("category:", category)
            # print(content)
            return category
        else:
            # print("stripped:", len(stripped))
            res = run_index(stripped)
            # print(stripped)
            return res

# Crawler().start("https://www.vanguardngr.com/2023/07/nigeria-practising-plutocracy-not-democracy-falana/")

# https://leadership.ng/world-youth-skills-day-stakeholders-harp-on-youth-employment-through-vocational-digital-education/

# https://dailytrust.com/gombe-gov-constitutes-committees-on-grazing-reserves-quran-recitation-competition

# https://hausa.legit.ng/mutane/1544975-auren-zaurawa-mata-sun-yalla-ido-sun-hango-yan-takara-da-jagororin-kwankwasiyya/