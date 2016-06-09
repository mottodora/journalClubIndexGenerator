#!/usr/bin/env python
#-*- coding: utf-8 -*-
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def _development(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")

    bsObj = BeautifulSoup(html.read(), "html5lib")

    meta_data = bsObj.find("div", {"class": "highwire-cite-metadata"}).get_text().\
            strip()
    journal_data = []
    for sub in bsObj.findAll("div", {"class": "issue-toc-section"}):
        category = sub.find("h2").get_text()
        articles = []
        for article in sub.findAll("div", {"class": "highwire-cite"}):
            t = article.find("span", {"id": "page-title"}).get_text()
            try:
                s = article.find("div", {"id": "abstract-2"}).get_text().\
                        split(':')[1].strip()
                articles.append((t, s))
            except AttributeError:
                continue
        if len(articles) > 0:
            journal_data.append((category, articles))
    return meta_data, journal_data


