import sys
from crawler import Crawler
from run_index import run_index

c = Crawler()
url = sys.argv[1]

parsed = c.start(url)
# cropped = parsed[:14000]
# new = parsed[3500:-1500]

print(len(parsed))

print(f"\n\n parsed: {parsed}\n\n")

categories = run_index(f"({parsed})\n")
print(categories)

summary = c.make_summary(parsed)
print(summary)
# c.tv_rewrite(parsed)
# c.radio_rewrite(parsed)
# c.online_rewrite(parsed)