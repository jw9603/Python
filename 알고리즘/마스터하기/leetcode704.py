# LeetCode 704. Binary Search
# https://leetcode.com/problems/binary-search/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        result = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                result = mid
                return result
        return -1

from bisect import *
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = bisect_left(nums, target)
        if index != len(nums) and nums[index] == target:
            return index
        return -1