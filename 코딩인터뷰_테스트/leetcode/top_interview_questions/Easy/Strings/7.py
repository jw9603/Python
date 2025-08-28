# LeetCode 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_val, min_val = 2 ** 31 - 1, -2 ** 31
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        rev = int(s[::-1]) * sign

        if rev < min_val or rev > max_val:
            return 0
        return rev
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_val, min_val = 2 ** 31 - 1, -2 ** 31
        rev, sign = 0, -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        rev *= sign
        return rev if min_val <= rev <= max_val else 0