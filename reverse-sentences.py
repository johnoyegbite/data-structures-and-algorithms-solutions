# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:05:17 2019

@author: USER
"""
# SOLVED!


def reverse_sentences(sentence):
    sentence_list = sentence.split(" ")
    reversed_senctence_list = [word[::-1] for word in sentence_list]
    return ' '.join(reversed_senctence_list)


if __name__ == "__main__":
    sentence = "Merry Chritmas and a Happy New Year in Advance"
    print(reverse_sentences(sentence))
