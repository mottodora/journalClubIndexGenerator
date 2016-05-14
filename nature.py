import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import datetime
import argparse

parser = argparse.ArgumentParser(description='nature summary generator')
parser.add_argument('--url', '-u', \
                    default='http://www.nature.com/nature/current_issue.html',
                    help='URL you want to generate a summary')
parser.add_argument('--author', '-a',
                    default="Someone")
args = parser.parse_args()
url = args.url
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
metadata = header.get_text(" ")
research = bsObj.find("div", {"id": "research"})
author = args.author

with open("journalclub.tex", "w") as f:
    f.write('\\documentclass[a4j]{jsarticle}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{\\vspace{-1.5cm}JournalClub}\n')
    f.write('\\author{%s}\n'%(author))
    d = datetime.datetime.today()
    f.write("\date{%s年%s月%s日\\vspace{-0.3cm}}\n"%(d.year, d.month, d.day))
    f.write("\maketitle\n")
    f.write('\\noindent\n%s %s\n\\vspace{-5mm}\n'%(jounal_title, metadata))

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
            f.write('\section{%s}\n'%(category))
            for t, s in articles:
                f.write('\\noindent\\textbf{%s}\n%s\n\\vspace{3mm}\n'%(t,s))
    f.write('\end{document}\n')

print('generate summary about %s %s'%(jounal_title, metadata))
