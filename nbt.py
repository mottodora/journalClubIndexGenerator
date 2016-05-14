import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import datetime
import argparse

parser = argparse.ArgumentParser(description='nature summary generator')
parser.add_argument('--url', '-u', \
                    default='http://www.nature.com/nbt/current_issue/',
                    help='URL you want to generate a summary')
parser.add_argument('--author', '-a',
                    default="Someone")
args = parser.parse_args()

author = args.author
url = args.url

if url.split('/')[2] == "www.nature.com":
    if url.split('/')[3] == 'nature':
        jounal_title = 'Nature'
    elif url.split('/')[3] == 'nbt':
        jounal_title = 'Nature Biotechnology'

try:
    html = urllib.request.urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
bsObj = BeautifulSoup(html.read(), "lxml")

metadata = bsObj.find("h2", {"class": "issue"}).get_text()

with open("journalclub.tex", "w") as f:
    f.write('\\documentclass[a4j]{jsarticle}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{\\vspace{-1.5cm}JournalClub}\n')
    f.write('\\author{%s}\n'%(author))
    d = datetime.datetime.today()
    f.write("\date{%s年%s月%s日\\vspace{-0.3cm}}\n"%(d.year, d.month, d.day))
    f.write("\maketitle\n")
    f.write('\\noindent\n%s %s\n\\vspace{-5mm}\n'%(jounal_title, metadata))
