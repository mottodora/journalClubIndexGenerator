import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = "http://www.nature.com/nature/journal/v533/n7602/index.html"
if url.split('/')[2] == "www.nature.com":
    if url.split('/')[3] == 'nature':
        jounal_title = 'Nature'

try:
    html = urllib.request.urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
bsObj = BeautifulSoup(html.read(), "lxml")

meta = bsObj.find("div", {"id": "issue-meta"})\
        .find("div", {"class": "subsection"})
header = meta.find("header")
metadata = header.get_text()
print(jounal_title)
print(metadata)
research = bsObj.find("div", {"id": "research"})
#for a in article_list.find("div", {"class": "standard-teaser"}):
for sub in research.findAll("div", {"class": "subsection"}):
    print(sub.find("span").get_text())
    article_list = sub.find("ul", {"class": "article-list"})
    #for article in article_list.findAll("article"):
    for article in article_list.findAll("div", {"class": "standard-teaser"}):
        #title = article.find("hgroup").find("a").get_text()
        title = article.hgroup.get_text()
        print('title: ' + title)
        try:
            summary = article.p.get_text()
            print(summary)
        except AttributeError:
            continue
