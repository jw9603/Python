# LeetCode 66. Plus One
# https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = str(int(''.join(map(str, digits))) + 1)
        return map(int, [i for i in res])