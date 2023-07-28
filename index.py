import sys
from crawler import Crawler
from run_index import run_index

c = Crawler()
url = sys.argv[1]

parsed = c.start(url)

print(f"parsed: {parsed}\n\n")

categories = run_index(f"({parsed})")
print(categories)

# c.make_summary(parsed)
# c.tv_rewrite(parsed)
# c.radio_rewrite(parsed)
# c.online_rewrite(parsed)