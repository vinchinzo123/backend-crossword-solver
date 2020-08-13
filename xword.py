#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Vincent Newsom"

# YOUR HELPER FUNCTION GOES HERE
import re


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = input(
        '''Please enter a word to solve.
        \nUse spaces to signify unknown letters: ''').lower()

    # YOUR ADDITIONAL CODE HERE
    test_word = test_word.replace(" ", ".")
    pattern = re.compile(test_word)
    same_len_words = [word for word in words if pattern.match(
        word) and len(word) == len(test_word)]
    print(same_len_words)
    for word in same_len_words:
        print(word)


if __name__ == '__main__':
    main()
