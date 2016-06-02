#!/usr/bin/env python
#-*- coding: utf-8 -*-
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def _genomeresearch(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "html5lib")
    meta_data = bsObj.find("cite").get_text()
    journal_data = []
    level1 = bsObj.find("div", {"class": "level1"})
    for subject in bsObj.findAll("div", {"class": "level1"}):
        category = subject.find("h2").get_text()
        articles = []
        for article in subject.findAll("li", {"class": "toc-cit"}):
            t = article.find("h4").get_text().strip()
            abst_url = '/'.join(url.split('/')[:3]) \
                    + article.find("a", {"rel": "abstract"})['href']
            try:
                abst_html = urlopen(abst_url)
                abstObj = BeautifulSoup(abst_html.read(), "html5lib")
                abst_contents = abstObj.find("div", {"id": "abstract-1"})
                results = abst_contents.find("p").get_text()
                #results = results.split(':')[1]
                s = ' '.join(results.replace("\n", " ").split())
                articles.append((t, s))
            except AttirbuteError:
                continue
        if len(articles) > 0:
            journal_data.append((category, articles))
    return meta_data, journal_data

