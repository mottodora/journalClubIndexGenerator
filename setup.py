#!/usr/bin/env python
#-*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name="indexGen",
      version="0.1.0",
      description="journal club index generator",
      author="motoki",
      author_email="motoki@dna.bio.keio.ac.jp",
      packages=find_packages(),
      install_requires=[
          'beautifulsoup4',
          'lxml',
          'six',
      ],
      entry_points="""
      [console_scripts]
      generateIndex = generator:main
      """,
      )
