import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def _bioinformatics(url):
    try:
        html = urllib.request.urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "lxml")
    meta_data = ' '.join(bsObj.find("cite")\
                        .get_text().replace("\n", "").split())
    jounal_data = []
    original = bsObj.find("div", {"class": "pub-section-ORIGINALPAPERS"})
    for subject in original.findAll("div", {"class": "level2"}):
        category = subject.find("h3").get_text()
        articles = []
        for article in subject.findAll("li", {"class": "cit"}):
            t = article.find("h4").get_text()
            abst_url = '/'.join(url.split('/')[:3]) \
                    + article.find("a", {"rel": "abstract"})['href']
            try:
                abst_html = urllib.request.urlopen(abst_url)
                abstObj = BeautifulSoup(abst_html.read(), "lxml")
                abst_contents = abstObj.find("div", {"id": "abstract-1"})
                results = abst_contents.findAll("p")[1].get_text()
                results = results.split(':')[1]
                s = ' '.join(results.replace("\n", " ").split())
                articles.append((t, s))
            except AttirbuteError:
                continue
        if len(articles) > 0:
            jounal_data.append((category, articles))
    return meta_data, jounal_data

