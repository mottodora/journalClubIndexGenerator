#!/usr/bin/env python
#-*- coding: utf-8 -*-
from six.moves.urllib.request import urlopen
from six.moves.urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

from collections import defaultdict

def _genomebiology(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html.read(), "html5lib")
    meta_data = bsObj.find("p", {"class": "ResultsList_journal"})\
            .get_text().strip().split(":")[0]

    journal_data = defaultdict(list)

    for subject in bsObj.findAll("li", {"class":"ResultsList_item"}):
        category = subject.find("p", {"class":"ResultsList_type"}).get_text()
        t = subject.find("a",{"class":"fulltexttitle"}).get_text()
        abst_url = '/'.join(url.split('/')[:3]) \
                + subject.find("a",{"class":"fulltexttitle"})['href']
        if category == "Research Highlight":
            continue

        try:
            abst_html = urlopen(abst_url)
            abstObj = BeautifulSoup(abst_html.read(), "html5lib")
            s = abstObj.find("section").findAll("p", {"class":"Para"})[-1]\
                    .get_text()
            journal_data[category].append((t, s))
        except AttributeError:
            continue
        except IndexError:
            continue
    journal_data = [(a, b) for a, b in journal_data.items()]
    return meta_data, journal_data




