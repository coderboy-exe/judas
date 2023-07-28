import requests
from bs4 import BeautifulSoup as BS4
from run_index import run_index, summarize, rewrite_tv, rewrite_online, rewrite_radio

from helpers import (
    clean_leadership,
    clean_punch_or_sun,
    clean_pmnews,
    clean_dailytrust,
    clean_thisday,
    )
from constants import (
    LEADERSHIP,
    PUNCH,
    PMNEWS,
    SUN,
    DAILYTRUST,
    THISDAY,
    )


class Crawler():
    """ Crawler class """
    def start(self, url):
        """ Start the crawler and run the indexer """

        # try:
        res = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1237803624181784694 t2919217341348717815"
        })
        # print(res.text)

        soup = BS4(res.content, "html.parser")

        if url.startswith(LEADERSHIP):
            print("leadership\n\n")
            cleaned = clean_leadership(soup)
            # print(cleaned)
        elif url.startswith(PUNCH) or url.startswith(SUN):
            print("punch or sunnews\n\n")
            cleaned = clean_punch_or_sun(soup)
            # print(cleaned)
        elif url.startswith(PMNEWS):
            print("pmnews\n\n")
            cleaned = clean_pmnews(soup)
            # print(cleaned)
        elif url.startswith(DAILYTRUST):
            print("dailytrust\n\n")
            cleaned = clean_dailytrust(soup)
            # print(cleaned)
        elif url.startswith(THISDAY):
            print("thisday\n\n")
            cleaned = clean_thisday(soup)
            # print(cleaned)

        else:
            print("This news source is not supported yet :( ")
            raise Exception("Sorry, this news source is not supported yet :(")

        # cleaned = main.get_text()
        stripped = str(cleaned).strip().replace('\n', '')

        # print(stripped)
        return stripped


    def categorize(self, stripped):
        """ Run indexer to categorize articles """
        print("stripped:", len(stripped))
        res = run_index(stripped)
        # print(stripped)
        return res


    def make_summary(self, content):
        """ Create summary for text content """
        res = summarize(content)
        # print("summary:", res)

        return str(res).strip()


    def tv_rewrite(self, content):
        """ Rewrite article for TV """
        res = rewrite_tv(content)
        # print("tv:", res)
        return str(res).strip()

    def radio_rewrite(self, content):
        """ Rewrite article for Radio """
        res = rewrite_radio(content)
        # print("radio:", res)
        return str(res).strip()
    
    
    def online_rewrite(self, content):
        """ Rewrite article for Online presentation """
        res = rewrite_online(content)
        # print("online:", res)
        return str(res).strip()