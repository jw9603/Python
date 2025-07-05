# LeetCode 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_dict = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in nums_dict:
                if abs(i - nums_dict[nums[i]]) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i
            else:
                nums_dict[nums[i]] = i
        
        return False