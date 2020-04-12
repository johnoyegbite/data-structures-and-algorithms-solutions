# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:37:14 2019

@author: John Oyegbite
"""
# SOLVED!
"""
Problem:
    Determine whether an integer is a palindrome. 
    An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, 
                 it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
Follow up:
    Coud you solve it without converting the integer to a string?
"""
# The reverse of the last half of the palindrome should be the same as 
# the first half of the number, if the number is a palindrome.
# For example, if the input is 1221, if we can revert the last part of the number
# "1221" from "21" to "12", and compare it with the first half of the number "12",
# since 12 is the same as 12, we know that the number is a palindrome.

# Now let's think about how to revert the last half of the number. 
# For number 1221, if we do 1221 % 10, we get the last digit 1, 
# to get the second to the last digit, we need to remove the last digit from 1221,
# we could do so by dividing it by 10, 1221 / 10 = 122. 
# Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, 
# and if we multiply the last digit by 10 and add the second last digit, 
# 1 * 10 + 2 = 12, it gives us the reverted number we want. 
# Continuing this process would give us the reverted number with more digits.

# Now the question is, how do we know that we've reached the half of the number?

# Since we divided the number by 10, and multiplied the reversed number by 10,
# when the original number is less than the reversed number, it means we've 
# processed half of the number digits.
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        
        reverted = 0
        while x > reverted:
            remainder, x = x % 10, x // 10
            reverted = reverted * 10 + remainder
            
        # When the length is an odd number, we can get rid of the middle digit
        # by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop 
        # we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome
        # (it will always equal to itself), we can simply get rid of it.
        return x == reverted or x == (reverted // 10)

if __name__ == "__main__":
    x = 1221
    print(isPalindrome(x))
        