# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    #1. brute force
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """

    #     longest = 0
    #     for num in nums:
    #         length = 1
    #         while num + length in nums:
    #             length+=1
    #         longest = max(length,longest)
    #     return longest

    # 2. 정렬
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     nums.sort()
    #     longest = 0
    #     length = 1

    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             continue
            
    #         if nums[i] + 1 == nums[i+1]:
    #             length += 1
            
    #         else:
    #             longest = max(length,longest)
    #             length = 1
        
    #     longest = max(length,longest)
    #     return longest

        

    # # 3. Hash Table
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     longest = 0
    #     hash_table = {}
    #     for num in nums:
    #         hash_table[num] = 1
        
    #     for num in hash_table:

    #         if num - 1 not in hash_table:
    #             cnt = 1
    #             while num + cnt in hash_table:
    #                 cnt += 1

    #             longest = max(longest,cnt)
    #     return longest

    # 4. Set
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums) # O(n)

        for num in nums: # O(n)
            if num - 1 not in nums:
                cnt = 1
                while num + cnt in nums:
                    cnt += 1
                longest = max(longest,cnt)
        return longest
    
    