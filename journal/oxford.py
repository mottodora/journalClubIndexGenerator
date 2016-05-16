#!/usr/bin/env python
#-*- coding: utf-8 -*-
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def _bioinformatics(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "lxml")
    meta_data = ' '.join(bsObj.find("cite")\
                        .get_text().replace("\n", "").split())
    journal_data = []
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
            journal_data.append((category, articles))
    return meta_data, journal_data

def _nar(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "lxml")
    meta_data = ' '.join(bsObj.find("cite")\
                        .get_text().replace("\n", "").split())

    journal_data = []
    for subject in bsObj.findAll("div", {"class": "level1"})[:-3]:
        category = subject.find("h2").get_text()
        articles = []
        for article in subject.findAll("li", {"class": "cit"}):
            t = ' '.join(article.find("h4").get_text().split())
            abst_url = '/'.join(url.split('/')[:3]) \
                    + article.find("a", {"rel": "abstract"})['href']
            try:
                abst_html = urllib.request.urlopen(abst_url)
                abstObj = BeautifulSoup(abst_html.read(), "lxml")
                abst_contents = abstObj.find("div", {"id": "abstract-1"})
                results = abst_contents.find("p", {"id": "p-2"}).get_text()
                s = ' '.join(results.replace("\n", " ").split())
                articles.append((t, s))
            except AttributeError:
                continue
        if len(articles) > 0:
            journal_data.append((category, articles))
    return meta_data, journal_data
