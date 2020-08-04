# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:37:13 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7
"""


class Solution:
    def isPrime(self, n):
        '''Assumes n is a +ve integer and 1 <= n <= 2*10^9
        Returns True is n is prime otherwise False
        '''
        starting_primes = set([2, 3, 5, 7])
        if n == 1:
            return False
        if n in starting_primes:
            return True
        if any([n % prime == 0 for prime in starting_primes]):
            return False

        start = 11
        while start*start <= n:
            if n % start == 0 or n % (start + 2) == 0:
                return False
            start += 6
        return True

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime_count = 1
        primes = []
        num = 3

        while num < n:
            if self.isPrime(num):
                primes.append(num)
                prime_count += 1
            if num % primes[-1] + 2 == 0:
                num += 6
            else:
                num += 2

        return prime_count
