# LeetCode 283. Move Zeros
# https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1