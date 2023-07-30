import sys
from crawler import Crawler
from run_index import run_index

c = Crawler()
url = sys.argv[1]

parsed = c.start(url)
cropped = parsed[:14000]

print(len(cropped))

print(f"\n\n parsed: {cropped}\n\n")

categories = run_index(f"({cropped})")
print(categories)

# c.make_summary(parsed)
# c.tv_rewrite(parsed)
# c.radio_rewrite(parsed)
# c.online_rewrite(parsed)