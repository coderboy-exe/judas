import requests
from bs4 import BeautifulSoup as BS4

url = "https://guardian.ng/"

res = requests.get(url)
# print(res.text)

soup = BS4(res.content, "html.parser")
print(soup)

results = soup.find(id="in-the-news")
# print(results)
# print(results.prettify())

class NewsParser():
    data = []

    def clean_url(self, item):
        """clean the data"""
        item_url = item.find("a")
        link = item_url.get("href")
        try:
            item_name = str(link).split('/')[-2]
            if len(item_name) <= 12:
                return {item_name: link}
            else:
                return [item_name, link]
        except IndexError:
            item_name = str(link).split('/')[-1]
            if len(item_name) <= 12:
                return {item_name: link}
            else:
                return [item_name, link]
        # print(item_name, end="\n"*2)
        # print({item_name: link}, end="\n"*2)

    def clean_content(self, item):
        content = item.get_text()
        return content


    def parse(self):
        categories = results.find_all("div", class_="category")
        for category in categories:
            # print(category, end="\n"*2)
            cleaned = self.clean_url(item=category)
            # print(cleaned)
            # category_url = category.find("a")
            # link = category_url.get("href")
            # cat_name = str(link).split('/')[-2]
            # print(cat_name, end="\n"*2)
            # print({cat_name: link}, end="\n"*2)

            if isinstance(cleaned, dict):
                for item_name, link in cleaned.items():
                    item_url = str(link)
                    cat = item_name

                    resp = requests.get(item_url)
                    # print(res.text)

                    item_soup = BS4(resp.content, "html.parser")

                    articles = item_soup.find_all("div", class_="content")

                    for article in articles:
                        # print(article)
                        content = self.clean_url(article)
                        # print({cat: content})

                        # for li in content:
                        if len(content) > 1 and not isinstance(content, dict):
                            item_url = str(content[-1])
                        else:
                            continue

                        resp = requests.get(item_url)
                        # print(res.text)

                        text_soup = BS4(resp.content, "html.parser")

                        # text = item_soup.find_all("div", class_="content")
                        cleaned_content = self.clean_content(text_soup)
                        formatted = str(cleaned_content).strip().replace('\n', '')
                        # print({cat: formatted})

                    self.data.append({item_name: formatted})
            else:
                print(f"No response: {cleaned}")

        with open('data/data.txt', 'w') as f:
            f.write(str(self.data))

NewsParser().parse()
