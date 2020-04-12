# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:57:08 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    
    For example, two is written as II in Roman numeral, just two one's added 
    together. Twelve is written as, XII, which is simply X + II. 
    The number twenty seven is written as XXVII, which is XX + V + II.
    
    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is 
    written as IV. Because the one is before the five we subtract it making four. 
    The same principle applies to the number nine, which is written as IX. 
    There are six instances where subtraction is used:
    
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    
    Given a roman numeral, convert it to an integer. Input is guaranteed to be
    within the range from 1 to 3999.

Example 1:
    Input: "III"
    Output: 3

Example 2:
    Input: "IV"
    Output: 4

Example 3:
    Input: "IX"
    Output: 9

Example 4:
    Input: "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

Example 5:
    Input: "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

# For you to add a roman numeral it must be greater than the next roman numeral
    # if it is less, then that roman numeral and next roman numeral can be 
    # combined in to one and it is generally the subtraction.
    # Example:
    #         s = "MCMX"
    # 1. we start at "M" (postion 0), 
    #      "M"(pos 0) > "C"(pos 1), so we have "M" = 1000 
    # 2. then we move "C"(pos 1), 
    #      "C"(pos 1) < "M"(pos 2), so we say "M" - "C" = 1000-100 = 900.
    # 3. then we move "X"(pos 3), 
    #      "X"(pos 3) is the last roman numeral /or do not have another value 
    #       in front to compare with, 
    #      so we say "X" = 10.
    # Total = 1000 + 900 + 10 = 1910
    #
    # Note that we won't look at "M" at position 2 since we have combined it 
    # "C" at position 1. Hence we skip to roman numeral at position (2+1)

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_int = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    start = 0
    end = len(s)
    total = 0
    
    while start < end:
        curr = s[start]
        if start < end-1:
            next_ = s[start + 1]
            if roman_int[curr] >= roman_int[next_]:
                total += roman_int[curr]
                start += 1
            else:
                total += roman_int[next_] - roman_int[curr]
                start += 2
        else:
            total += roman_int[curr]
            start += 1
        
    return total

# Another solution
def roman_ToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_int = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, 
                 "M": 1000, "A": 9, "B": 4, "P": 40, "Q": 90, "R": 900, "S": 400}
    new_roman = {"IX": "A", "IV":"B", "XL":"P", "XC":"Q", "CM":"R", "CD":"S"}
    
    total = 0
    for roman in new_roman:
        if roman in s:
            s = s.replace(roman, new_roman[roman])
    for roman in s:
        total += roman_int[roman]    
    
    return total


if __name__ == "__main__":
    s = "III" # 3
    s = "IV" # 4
    s = "IX" # 9
    s = "LVIII" # 58
    s = "MCMXCIV" # 1994
    s = "DCXXI"
        
    print(romanToInt(s))
    print(roman_ToInt(s))