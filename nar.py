import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import datetime
import argparse

parser = argparse.ArgumentParser(description='nature summary generator')
parser.add_argument('--url', '-u', \
                    default='http://nar.oxfordjournals.org/content/current',
                    help='URL you want to generate a summary')
parser.add_argument('--author', '-a',
                    default="Someone")
args = parser.parse_args()
url = args.url

if url.split('/')[2] == "nar.oxfordjournals.org":
    jounal_title = 'Nucleic Acids Research'

try:
    html = urllib.request.urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
bsObj = BeautifulSoup(html.read(), "lxml")
metadata = ' '.join(bsObj.find("cite").get_text().replace("\n", "").split())
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
            f.write('\section{%s}\n'%(category))
            for t, s in articles:
                f.write('\\noindent\\textbf{%s}\n\n%s\n\n\\vspace{3mm}\n'%(t,s))
    f.write('\end{document}\n')
print('generate summary about %s %s'%(jounal_title, metadata))

