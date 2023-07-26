import requests
from bs4 import BeautifulSoup as BS4
from run_index import run_index, summarize, rewrite_tv, rewrite_online, rewrite_radio

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

        # print(stripped)
        return stripped


    def categorize(self, stripped):
        """ Run indexer to categorize articles """
        if len(stripped) > 12000:
            content = stripped[500:-6000]
            category = run_index(content)
            # print("content: ", content)
            # print("category: ", category)
            return category
        elif len(stripped) > 10000:
            content = stripped[500:-4500]
            category = run_index(content)
            # print("content: ", content)
            # print("category: ", category)
            # print(content)
            return category
        elif len(stripped) > 8000:
            content = stripped[500:-3000]
            category = run_index(content)
            # print("content: ", content)
            # print("category: ", category)
            # print(content)
            return category
        elif len(stripped) > 6000:
            content = stripped[500:-1500]
            category = run_index(content)
            # print("content: ", content)
            # print("category: ", category)
            # print(content)
            return category
        elif len(stripped) > 4000:
            content = stripped[500:-1200]
            category = run_index(content)
            # print("content: ", content)
            # print("category: ", category)
            # print(content)
            return category
        else:
            # print("stripped:", len(stripped))
            res = run_index(stripped)
            # print(stripped)
            return res


    def make_summary(self, content):
        """ Create summary for text content """
        # if len(content) > 12000:
        #     stripped = content[500:-6000]
        #     res = summarize(stripped)
        # elif len(content) > 10000:
        #     stripped = content[500:-4500]
        #     res = summarize(stripped)
        # elif len(content) > 8000:
        #     stripped = content[500:-3000]
        #     res = summarize(stripped)
        # elif len(content) > 6000:
        #     stripped = content[500:-1500]
        #     res = summarize(stripped)
        # elif len(content) > 4000:
        #     stripped = content[500:-1200]
        #     res = summarize(stripped)
        # print("content_length:\n", len(content))
        # print("content:\n", stripped)
        # print("summary:\n", res)
        res = summarize(content)

        return str(res).strip()


    def tv_rewrite(self, content):
        """ Rewrite article for TV """
        # if len(content) > 12000:
        #     stripped = content[500:-6000]
        #     print("len_stripped:", len(stripped))
        #     res = rewrite_tv(stripped)
        # elif len(content) > 10000:
        #     stripped = content[500:-4500]
        #     print("len_stripped:", len(stripped))
        #     res = rewrite_tv(stripped)
        # elif len(content) > 8000:
        #     stripped = content[500:-3000]
        #     print("len_stripped:", len(stripped))
        #     res = rewrite_tv(stripped)
        # elif len(content) > 6000:
        #     stripped = content[500:-1500]
        #     print("len_stripped:", len(stripped))
        #     res = rewrite_tv(stripped)
        # elif len(content) > 4000:
        #     stripped = content[500:-1200]
        #     print("len_stripped:", len(stripped))
        #     res = rewrite_tv(stripped)
        # stripped = content[500:-1200]
        res = rewrite_tv(content)
        print("tv:", res)
        return str(res).strip().strip('Register')
    

    def radio_rewrite(self, content):
        """ Rewrite article for Radio """
        # if len(content) > 12000:
        #     stripped = content[500:-6000]
        #     res = rewrite_radio(stripped)
        # elif len(content) > 10000:
        #     stripped = content[500:-4500]
        #     res = rewrite_radio(stripped)
        # elif len(content) > 8000:
        #     stripped = content[500:-3000]
        #     res = rewrite_radio(stripped)
        # elif len(content) > 6000:
        #     stripped = content[500:-1500]
        #     res = rewrite_radio(stripped)
        # elif len(content) > 4000:
        #     stripped = content[500:-1200]
        #     res = rewrite_radio(stripped)
        # # stripped = content[500:-1200]
        res = rewrite_radio(content)
        print("radio:", res)
        return str(res).strip().strip('Register')
    
    
    def online_rewrite(self, content):
        """ Rewrite article for Online presentation """
        # if len(content) > 12000:
        #     stripped = content[500:-6000]
        #     res = rewrite_online(stripped)
        # elif len(content) > 10000:
        #     stripped = content[500:-4500]
        #     res = rewrite_online(stripped)
        # elif len(content) > 8000:
        #     stripped = content[500:-3000]
        #     res = rewrite_online(stripped)
        # elif len(content) > 6000:
        #     stripped = content[500:-1500]
        #     res = rewrite_online(stripped)
        # elif len(content) > 4000:
        #     stripped = content[500:-1200]
        #     res = rewrite_online(stripped)
        # stripped = content[500:-1200]
        res = rewrite_online(content)
        print("online:", res)
        return str(res).strip().strip('Register')