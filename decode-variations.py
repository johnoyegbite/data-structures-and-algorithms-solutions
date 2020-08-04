# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:05:21 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    A message containing letters from A-Z is being encoded to numbers using the
    following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

    Given a non-empty string containing only digits, determine the total number
    of ways to decode it.

Example 1:
    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6),
                or "BBF" (2 2 6).


Solution Visualization:
Input: "1226"
Output: 5 [=> (ABBF), (ABZ), (AVF), (LBF), (LZ)]

1226 => 1,2,2,6 (ABBF)| 1,2,26 (ABZ)| 1,22,6 (AVF)| 12,2,6 (LBF)| 12,26 (LZ)


                          .
                          1 2 2 6
                          ---
                     /              \
                .                       .
              1 2 2 6               1 2 2 6
                ---                     ---
             /      \               /      \
         .               .           .
     1 2 2 6       1 2 2 6     1 2 2 6      P
       ---             ---           -
    /      \       /      \     /     \
       .
 1 2 2 6    P    P          F  P        F
       -
/       \
P        F

Where P represent a vaild path
      F represent a failed path
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # To memoize, comment the path, result aspect.
        def decode_help(s, i, path, result, memo={}):
            # if i in memo:
            #     return memo[i]
            if i == len(s):
                result.append(",".join(path[:]))
                return 1
            if i > len(s):
                return 0

            left, right = 0, 0
            if 0 < int(s[i]) < 10:
                path.append(s[i])
                left = decode_help(s, i+1, path, result, memo)
                path.pop()
            if 10 <= int(s[i:i+2]) <= 26:
                path.append(s[i:i+2])
                right = decode_help(s, i+2, path, result, memo)
                path.pop()

            total = left + right
            # memo[i] = total
            return total
        path = []
        result = []
        total = decode_help(s, 0, path, result)
        print(result)
        print()
        return total
        

if __name__ == "__main__":
    s = Solution()
    S = "2263"
    # S = "1226"
    # S = "1206"
    S = "122121"
    print(s.numDecodings(S))
