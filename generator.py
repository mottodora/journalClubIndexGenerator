#!/usr/bin/env python
#-*- coding: utf-8 -*-
import datetime
import argparse

from gs import generate

def main():
    parser = argparse.ArgumentParser(description='nature summary generator')
    parser.add_argument('--url', '-u', \
                        default='http://www.nature.com/nature/current_issue.html',
                        help='URL you want to generate a summary')
    parser.add_argument('--author', '-a',
                        default="Someone")
    args = parser.parse_args()
    url = args.url
    author = args.author

    journal_title, meta_data, journal_data = generate(url)

    with open("journalclub.tex", "w") as f:
        f.write('\\documentclass[a4j]{jsarticle}\n')
        f.write('\\begin{document}\n')
        f.write('\\title{\\vspace{-1.5cm}JournalClub}\n')
        f.write('\\author{%s}\n'%(author))
        d = datetime.datetime.today()
        f.write("\date{%s年%s月%s日\\vspace{-0.3cm}}\n"%(d.year, d.month, d.day))
        f.write("\maketitle\n")
        f.write('\\noindent\n%s %s\n\\vspace{-5mm}\n'%(journal_title, meta_data))

        for category, articles in journal_data:
            f.write('\section{%s}\n'%(category))
            for t, s in articles:
                f.write('\\noindent\\textbf{%s}\n\n%s\n\n\\vspace{3mm}\n'\
                        %(t.encode("utf-8"),s.encode("utf-8")))
        f.write('\end{document}\n')
    print('generate summary about %s %s'%(journal_title, meta_data))

if __name__ == '__main__':
    main()
