# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    # 1. iterative
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    # 2. Two pointer
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [[n,i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x:x[0])
        l = 0
        r = len(nums) - 1
        
        while l < r:
            
            num_sum = nums[l][0] + nums[r][0]
            
            if num_sum == target:
                return [nums[l][1], nums[r][1]]
            elif num_sum < target:
                l += 1
            else:
                r -= 1
    
    # 3. Hash Table
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_dict = {}
        
        for i, num in enumerate(nums):
            
            target_needed = target - num
            if target_needed in num_dict:
                return [i,num_dict[target_needed]]
            
            num_dict[num] = i
            
            