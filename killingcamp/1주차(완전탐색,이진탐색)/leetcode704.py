# Leetcode74. Binary Search
# https://leetcode.com/problems/binary-search/description/
# https://leetcode.com/problems/binary-search/submissions/1563743003
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