# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:09:28 2019

@author: USER
"""
# SOLVED!
def run_length_encoding(string):
   if string == "":
        return "n/a"
   string_encoded = []
   to_encode = []
   for s in string:
       if to_encode and s != to_encode[-1]:
           string_encoded.append(str(len(to_encode)) + to_encode[-1])
           to_encode = []
           to_encode.append(s)
       else:
           to_encode.append(s)
   string_encoded.append(str(len(to_encode)) + to_encode[-1])
   return ''.join(string_encoded)


if __name__ == "__main__":
    string = "aaAAbbBBccCC"
    print(run_length_encoding(string))