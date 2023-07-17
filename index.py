import sys
from crawler import Crawler

c = Crawler()
url = sys.argv[1]

c.start(url)
