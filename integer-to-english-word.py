# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:41:49 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Convert a non-negative integer to its english words representation.
    Given input is guaranteed to be less than 231 - 1.

Example 1:
    Input: 123
    Output: "One Hundred Twenty Three"

Example 2:
    Input: 12345
    Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
    Input: 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
        Seven"

Example 4:
    Input: 1234567891
    Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty
        Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    def getNumInGroups(self, num: int):  # O(1)
        """Let H be Hundred, T be Thousand, M be Million, e.t.c
                                               H          T       M
        num = 12345678 would result to [[8, 7, 6], [5, 4, 3], [2, 1]]
        """
        groups = []
        section = 0
        group = []
        while num > 0:
            group.append(num % 10)
            num //= 10
            section += 1
            if section % 3 == 0:
                groups.append(group)
                group = []
        if group:
            groups.append(group)
        return groups

    def groupHundreds(self, group):  # O(1)
        # group is stored from unit to hundred
        # that is 123 is stored as [3, 2, 1]
        english_words = []
        # start from the hundreds (i.e from the end of group)
        for i in range(len(group)-1, -1, -1):
            num = group[i]
            # Zero doesn't have an effect during counting
            # unless the "num" from "numberToWords()" is 0 which we have taken
            # care of in "numberToWords()"
            if num == 0:
                continue

            # if we can have i as 2 then we surely have a hundreds
            if i == 2:
                # num would correspond to the index in "self.tens_unit"
                # as it is designed that way
                # Hence just pick its English word and also pick its group
                # (which is Hundred)
                english_words.append(self.tens_unit[num])
                english_words.append(self.groups[0])

            # if we can have i as 1 then we surely have a tens
            if i == 1:
                # Now we have to be careful here, if we have '1' as tens, then
                # we can only have something like Ten, Eleven, Twelve and so on
                # Hence we have to consider the unit value immediately so as to
                # ascertain if we have to pick 10 (Ten) or 11(Eleven) or
                # 12(Twelve), e.t.c
                if num == 1:
                    num_with_unit = num*10 + group[0]
                    # pick the English word from "self.tens_unit" which the
                    # new num with unit correspond to its index in that array
                    english_words.append(self.tens_unit[num_with_unit])
                    break  # to avioid considering the unit afterwards
                # if num is a value that differs from '1', then it has to be
                # something like Twenty (for 2), Thirty(for 3), Fourty(for 4)
                # e.t.c. Hence pick it English word from "self.tens_tens" using
                # num as index in the array (i.e index '2' in "self.tens_tens
                # correspond to 'Twenty').
                english_words.append(self.tens_tens[num])
            # if we can have i as 0 then we surely have a unit
            if i == 0:
                # Pretty simple, just look for its English word in
                # "self.tens_unit"
                # (index '2' in "self.tens_unit correspond to 'Two')
                english_words.append(self.tens_unit[num])

        # Now that we have our complete English word for a group let's Join
        return " ".join(english_words)

    def numberToWords(self, num: int) -> str:  # O(1)
        if num == 0:
            return "Zero"

        self.tens_unit = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
        ]

        self.tens_tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]

        self.groups = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

        # Let us group 'num'
        groups = self.getNumInGroups(num)  # see output in function definition

        english_words = []

        # Get the English word for every group in groups,
        # starting from the largest (say Billion).
        for i in range(len(groups)-1, -1, -1):
            group = groups[i]
            words = self.groupHundreds(group)

            # 'words' can be empty,
            # if we have 'group' to be [0, 0, 0], [0, 0], e.t.c.
            if not len(words):
                continue

            english_words.append(words)

            # Append the type of group to the 'words'
            # (is it thousand, million, e.t.c).
            # if we have 'i' as '0', then we know that that group belongs
            # to Hundred,
            # if we have 'i' as '1', then we know that that group belongs
            # to Thousand, e.t.c.
            # Hence, if we have 'i' as '0', we know it belongs to the group
            # Hundred already so we don't append anything to avoid something
            # like 'Two Hundred Twenty Five Hundred'
            # instead of 'Two Hundred Twenty Five'.
            if i != 0:
                english_words.append(self.groups[i])

        return "'{}'".format(" ".join(english_words))


if __name__ == "__main__":
    s = Solution()
    num = 2050
    num = 12345
    num = 1234567
    num = 12345678
    # num = 1000
    # num = 1000000
    # num = 1000010
    print(s.numberToWords(num))
