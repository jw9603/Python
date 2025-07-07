# LeetCode 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        
        def power(base, exp):
            if exp == 0:
                return 1.0
            
            half = power(base, exp // 2)

            return half * half if exp % 2 == 0 else half * half * base