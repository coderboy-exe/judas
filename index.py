import sys
from crawler import Crawler

c = Crawler()
url = sys.argv[1]

parsed = c.start(url)

c.make_summary(parsed)
c.tv_rewrite(parsed)
c.radio_rewrite(parsed)
c.online_rewrite(parsed)