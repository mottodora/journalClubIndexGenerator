Jounal Club Index Generator
===============

URLと名前を入れるだけで、ジャーナルクラブの目次を作ってくれます。

## dependency

* python 2,3
* BeautifulSoup
* html5lib
* six

## 対応雑誌

* Nature / Nature Genetics / Nature Biotechnology
* Bioinformatics / Nucleic Acids Research
* Genome Research
* Genome Biology
* Development

## 使い方

```
$ git clone https://github.com/mottodora/journalClubIndexGenerator.git
$ cd journalClubIndexGenerator
$ pip install -e .
$ generateIndex --url http://www.nature.com/ng/journal/v48/n5/index.html --author "testuser"
$ platex journalclub.tex
$ dvipdfmx journalclub.dvi
```

## Known Problems

* BioinformaticsのIndexを生成した時にplatexすると一つerrorが出る(pdf生成には問題ない).
* NARのIndexを生成した時にファイルが長い.