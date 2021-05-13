#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
  name = 'latexcompiler',         # How you named package folder (LatexCompiler)
  packages=find_packages(include=["latexcompiler", "latexcompiler.*"]),
  version = '1.0',     # Start with a small number and increase it with every change you make
  license='MIT',       # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A program for compiling LaTeX files the convenient way by stashing the auxiliary files into a specified folder.',   # Give a short description about library
  author = 'Amin Ranem',                   # Type in name
  author_email = 'aminranem@googlemail.com',      # Type in E-Mail
  url = 'https://github.com/amrane99/',   # Provide either the link to github or to own website
  download_url = 'https://github.com/amrane99/LatexCompiler',
  keywords = ['LaTeX', 'BibTeX', 'Python'],   # Keywords that define package best
  install_requires=[            # Same as requirements.txt
          'tqdm'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers, Users',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
  ],
  entry_points={
    'console_scripts': [
        'LatexCompiler = latexcompiler.LC:main',
    ],
  },
)
