# LeetCode 202. Happy Number
# https://leetcode.com/problems/happy-number/description/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # happy number 함수
        def get_happy(num):
            total_sum = 0
            
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num //= 10
            
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_happy(n)
        
        return n == 1   