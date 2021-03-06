#!/usr/bin/env python

from distutils.core import setup

setup(
    name='git_trac',
    description='A "git trac" subcommand for git',
    author='Volker Braun',
    author_email='vbraun.name@gmail.com',
    packages=['git_trac'],
    data_files=[('share/git-trac-command', ['doc/git-cheat-sheet.pdf'])],
    scripts=['git-trac'],
    version='1.0',
    url='https://github.com/sagemath/git-trac-command',
)
