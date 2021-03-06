#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Probleme extra."""

from __future__ import print_function
import os


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def search_dir(cautare, adresa):
    """Functia cauta toate fisierele care au <cautarea> in nume"""
    if os.path.isdir(adresa):
        for director in os.listdir(adresa):
            path = os.path.join(adresa, director)
            if os.path.isfile(path) and (cautare in director):
                print("Fisierul care contine litera %s se gaseste "
                      "la adresa %s" % (cautare, path))
            else:
                search_dir(cautare, path)


def copac(adresa, depth):
    """Afișarea unui director într-o structură arborescentă."""
    depth += 1
    if os.path.isdir(adresa):
        for director in os.listdir(adresa):
            forward = os.path.join(adresa, director)
            if os.path.isdir(forward):
                print(depth * "   " + HEADER + director + ENDC)
                copac(forward, depth)
            else:
                print(depth * "   " + OKBLUE + director + ENDC)


if __name__ == '__main__':
    copac(".", -1)
