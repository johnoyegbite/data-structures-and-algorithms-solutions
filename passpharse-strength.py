# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:28:06 2019

@author: USER
"""
# SOLVED!
import re


def passphrase_strength(passphrase):
    # reduce multiple spaces to a space
    passphrase = re.sub(" +", " ", passphrase).lower()
    
    if not len(passphrase) or passphrase == " ":
        return "n/a"
    
    passphrase_list = passphrase.split(" ")
    passphrase_dict = {}
    
    for passphrase in passphrase_list:
        if passphrase in passphrase_dict:
            return "weak"
        else:
            passphrase_dict[passphrase] = passphrase_dict.get(passphrase, 0) + 1
    return "strong"
            

if __name__ == "__main__":
    passphrase = "aa bb cc dd ee" 
    passphrase = "aa bb aa             dd ff"
    print(passphrase_strength(passphrase))