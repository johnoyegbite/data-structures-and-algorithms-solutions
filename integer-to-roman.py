# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:08:09 2020

@author: johnoyegbite
"""
# SOLVED!


def getRoman(num):
    roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 
                      100: "C", 500: "D", 1000: "M", 4: "IV", 
                      9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    if num == 0:
        return ""
    if num in roman_dict:
        return roman_dict[num]
    if num > 1000:
        return roman_dict[1000] * int(num/1000.0)
    elif num > 100:
        if num <= 300:
              return roman_dict[100] * int(num/100.0)
        elif num > 500:
              num = num / 100.0
              num = num - 5
              return roman_dict[500] + roman_dict[100]*int(num)
    elif num >= 10:
        if num <= 30:
              return roman_dict[10] * int(num/10.0)
        elif num > 50:
              num = num / 10.0
              num = num - 5
              return roman_dict[50] + roman_dict[10]*int(num)
    elif num >= 1:
        if num <= 3:
              return roman_dict[1] * int(num/1.0)
        elif num > 5:
              num = num / 1.0
              num = num - 5
              return roman_dict[5] + roman_dict[1]*int(num)


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # say num = 3520
    # => num_str = 0253
    num_str = str(num)[::-1]
    num_len = len(num_str) - 1
    result = ""
    for i in range(num_len, -1, -1):
        pow_10 = (pow(10, i) * int(num_str[i]))
        result += getRoman(pow_10)

    return result


if __name__ == "__main__":
    num = 3900
    print(intToRoman(num))