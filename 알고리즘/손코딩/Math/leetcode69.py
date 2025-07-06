# LeetCode 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left, right = 0, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            target = mid ** 2

            if target == x:
                return mid
            elif target < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result