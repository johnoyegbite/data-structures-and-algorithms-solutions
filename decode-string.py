# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:19:04 2019

@author: John Oyegbite
"""
# SOLVED
"""
Problem:
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside
    the square brackets is being repeated exactly k times. Note that k is
    guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces,
    square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any
    digits and that digits are only for those repeat numbers, k.
    For example, there won't be input like 3a or 2[4].

Examples:
    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


def decodeString(s):
    stack = []
    for i, char in enumerate(s):
        if char != "]":
            stack.append(char)
        else:
            # Pop all the characters till you see a '['
            curr_chars = []
            while stack and stack[-1] != "[":
                popped_char = stack.pop()
                curr_chars.append(popped_char)

            # remove the "["
            stack.pop()

            # Pop all the digit becase we have multiple digit behind a '['
            curr_digits = []  # we can have "100[abc]"
            while stack and stack[-1].isdigit():
                popped_digit = stack.pop()
                curr_digits.append(popped_digit)
            digit = int("".join(curr_digits[::-1]) or 1)

            stack.extend(curr_chars[::-1] * digit)
    return "".join(stack)


if __name__ == "__main__":
    s = "3[a]2[bc]"  # return "aaabcbc".
    s = "3[a2[c]]"  # return "accaccacc".
    s = "[abc][cd]ef"  # return "abcabccdcdcdef".
    s = "100[leetcode]"

    print(decodeString(s))
