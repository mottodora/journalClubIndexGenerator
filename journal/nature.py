#!/usr/bin/env python
#-*- coding: utf-8 -*-
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def _nature(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")

    bsObj = BeautifulSoup(html.read(), "html5lib")

    meta = bsObj.find("div", {"id": "issue-meta"})\
            .find("div", {"class": "subsection"})
    header = meta.find("header")
    meta_data = header.get_text(" ")
    research = bsObj.find("div", {"id": "research"})

    jounal_data = []

    for sub in research.findAll("div", {"class": "subsection"}):
        category = sub.find("span").get_text()
        article_list = sub.find("ul", {"class": "article-list"})
        articles = []

        for article in article_list\
                       .findAll("div", {"class": "standard-teaser"}):
            title = article.hgroup.get_text()
            try:
                summary = article.p.get_text()
                articles.append((title, summary))
            except AttributeError:
                continue
        if len(articles) > 0:
            jounal_data.append((category, articles))

    return meta_data, jounal_data

def _nbt(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "html5lib")

    meta_data = bsObj.find("h2", {"class": "issue"}).get_text()

    tmp = bsObj.find("div", {"class": "subject", "id": "re"})

    jounal_data = []
    while tmp.next_sibling.name != "div":
        category = tmp.next_sibling.get_text()
        articles = []
        obj_articles = tmp.next_sibling.next_sibling
        for article in obj_articles.findAll("div", {"class": None}):
            try:
                t = article.find("h4").get_text()
                s = article.find("p", {"class":"annotation"}).get_text()
                articles.append((t, s))
            except AttributeError:
                continue
        if len(articles) > 0:
            jounal_data.append((category, articles))
        tmp = tmp.next_sibling.next_sibling
    return meta_data, jounal_data

def _ng(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "html5lib")
    meta_data = bsObj.find("h2", {"class": "issue"}).get_text()

    jounal_data = []
    for subject in bsObj.findAll("div", {"class":"subject"}):
        category = subject.find("h3", {"class": "subject"}).get_text()
        articles = []
        for article in subject.findAll("div", {"class": None}):
            try:
                t = article.find("h4").get_text()
                s = article.find("p", {"class":"annotation"}).get_text()
                articles.append((t, s))
            except AttributeError:
                continue
        if len(articles) > 0:
            jounal_data.append((category, articles))
    return meta_data, jounal_data
