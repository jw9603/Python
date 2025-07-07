# LeetCode 172. Factorial Trailing Zeros
# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution(object):
    # 1. O(logn)
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        n!값의 뒤에 붙은 0의 개수
        5! = 120, 1개 
        6! = 6 * 5 * 4 * 3 * 2 * 1 = 720, 1개
        7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040, 1개
        8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320, 1개
        9! = 9 * 7 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 362880, 1개
        10! = 10 * 9 * 7 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800, 2개

        즉, 10의 개수 == (2 * 5)의 개수
        """
        cnt = 0

        while n >= 5:
            n //= 5
            cnt += n
        
        return cnt
    
    # 2. O(nlogn)
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def factorial(n):
            if n == 0:
                return 1
            
            return n * factorial(n - 1)
            
        res = str(factorial(n))[::-1]
        cnt = 0
        
        for char in res:
            if char == '0':
                cnt += 1
            else:
                break
        
        return cnt