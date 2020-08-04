# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 00:51:49 2020

@author: johnoyegbite
"""
import numpy as np

# SOLVED! Re-check
"""
Problem:
    Given two words word1 and word2, find the minimum number of operations
    required to convert word1 to word2.

    You have the following 3 operations permitted on a word:
        Insert a character
        Delete a character
        Replace a character

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')

Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
"""

"""
Iterative Solution Explanation:

                   |@1 | h | o | r | s | e |
                @2 | 0 | 1 | 2 | 3 | 4 | 5 |
                r  | 1 | 0 | 0 | 0 | 0 | 0 |
                o  | 2 | 0 | 0 | 0 | 0 | 0 |
                s  | 3 | 0 | 0 | 0 | 0 | 0 |

The first row and column of the table has known values since if one string is
empty, we simply add the length of the non-empty string since that is the
minimum number of edits necessary to arrive at equivalent strings.

Note that @ means if string is empty, which implies that the numbers in the
coordinate point where both @1 and @2 meets means the minimum distance of the
two strings (word1 and word2) would be 0 if both string are empty.

(@2, @1) = 0 => if both strings are empty, minimum distance is 0

(@2, h) = 1 => if string2 is empty and string1 has just one char "h" then the
               minimum distance is 1 (i.e. just DELETE "h" from both string to
               be empty or INSERT 'h' to string2 so they would both have 'h')
(@2, o) = 2 => if string2 is empty and string1 has just two chars "h o" then
               the minimum distance is 2 (i.e. just DELETE "h" and "o" from
               both string to be empty or INSERT 'h' and 'o' to string2 so they
               would both have 'h' and 'o')

               .
               .
               .

(@2, e) = 5 => if string2 is empty and string1 has five chars "h o r s e" then
               the minimum distance is 5 (i.e. just DELETE "h" to "o" from
               both string to be empty or INSERT 'h' to 'o' to string2 so they
               would both have 'h o r s e')
Similarly,

(r, @1) = 1 => if string2 has just one char 'r' and string 1 is empty then the
               minimum distance is 1 (i.e. just DELETE "r" from both string to
               be empty or INSERT 'r' to string1 so they would both have 'r')
(o, @1) = 2 => if string2 has two char 'r o' and string 1 is empty then the
               the minimum distance is 2 (i.e. just DELETE "r" and "o" from
               both string to be empty or INSERT 'r' and 'o' to string1 so they
               would both have 'r' and 'o')

(s, @1) = 3 => if string2 has three char 'r o s' and string 1 is empty then the
               the minimum distance is 3 (i.e. just DELETE "r" to "s" from
               both string to be empty or INSERT 'r' to 's' to string2 so they
               would both have 'r o s')

Performing operation on other coordinates:

                   |@1 | h | o | r | s | e |
                @2 | 0 | 1 | 2 | 3 | 4 | 5 |
                r  | 1 | 1 | 2 | 2 | 3 | 4 | <---- row 1
                o  | 2 | 0 | 0 | 0 | 0 | 0 |
                s  | 3 | 0 | 0 | 0 | 0 | 0 |

Now working on row 1 above:
    (r, h) = 1: =>
        if string2 has just a value 'r' and string1 has just a char "h" then
        the minimum distance is 1 (i.e. just REPLACE "h" with "r" or the
        reverse to make both strings equal which is just 1 operation, hence we
        put 1)
    (r, o) = 2: =>
        if string2 has just a value 'r' and string1 has 2 chars "h o" then
        the minimum distance is 2.
        i.e. DELETE "o" and REPLACE "h" with 'r' to make both strings equal
        which is 2 operations, hence we put 2 OR we DELETE "o" (1 operation)
        plus the value from (r, h).
    (r, r) = 2: =>
        if string2 has just a value 'r' and string1 has 3 chars "h o r" but
        notice that (r, r) are the same hence we don't perform any operation
        and the minimum distance is 2.
        i.e. 2 is gotten from (@2, o), the diagonal value. We can't pick the
        value in either (@2, r) or (r, o) because both coordinate conains 'r'

    Summary:
        For a given coordinate,
        1. the upper coordinate represent INSERT
        2. the left coordinate represent DELETE
        3. the diagonal coordinate represent REPLACE or DO NOTHING

                   |@1 | h | o | r | s | e |
                @2 | 0 | 1 | 2 | 3 | 4 | 5 |
                r  | 1 | 1 | 2 | 2 | 3 | 4 |
                o  | 2 | 2 | 1 | 2 | 3 | 4 |
                s  | 3 | 3 | 2 | 2 | 2 | 3 |

"""


class Solution:
    # https://www.youtube.com/watch?v=MiqoA-yF-0M
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        dp = np.array(dp)

        # Insert now values for word1 and word2 just in case eithr string is
        # empty as explained above.
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j

        for i in range(1, len(dp)):
            char2 = word2[i-1]
            for j in range(1, len(dp[0])):
                char1 = word1[j-1]
                if char1 == char2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]]) + 1
        print(dp)
        return dp[-1][-1]


# Recursive solution
def minDistance(word1: str, word2: str, i=0, j=0, memo={}) -> int:
    # if both strings are empty or reached the end of both strings,
    # then the minimum distance is 0. i.e. no character to operate on.
    if i == len(word1) and j == len(word2):
        return 0

    # if word1 is empty and word2 is not empty or we have reached the end of
    # word1, then we return the length of the remaining string in word2
    if i == len(word1):
        return len(word2) - j

    # if word2 is empty and word1 is not empty or we have reached the end of
    # word2, then we return the length of the remaining string in word1
    if j == len(word2):
        return len(word1) - i

    if (i, j) in memo:
        return memo[(i, j)]

    if word1[i] == word2[j]:
        ans = minDistance(word1, word2, i+1, j+1)
    else:
        # to insert a char in word1, we simulate that by adding a char and also
        # maintain the length of word1. Operation to perform this is:
        # 1. i+1 (add a char)
        # 2. (1) - 1 => i (make sure you maintain the length of the word1)
        # also since the char in word2 was looked up to know the char to insert
        # in word1, hence we move to the next char for the next recursive
        # comparison.
        insert = 1 + minDistance(word1, word2, i, j+1)

        # to delete a char from word1, we simulate that by moving to the next
        # char (i+1) in word1 while also maintaining char in word2 (j) for next
        # comparison in the next recursive loop)
        delete = 1 + minDistance(word1, word2, i+1, j)

        # to replace a char in word1, we simulate that by just moving to the
        # next char in both words (i+1, j+1). We move to the next char because
        # we have successfully simulate by comparison.
        replace = 1 + minDistance(word1, word2, i+1, j+1)

        ans = min(insert, delete, replace)
    memo[(i, j)] = ans
    return ans


if __name__ == "__main__":
    s = Solution()
    word1 = "horse"
    word2 = "ros"
    print(s.minDistance(word1, word2))
