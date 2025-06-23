# LeetCode 78. Subsets
# https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(start, curr):
            # Base Case
            ans.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])

        return ans

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(start, curr):
            # Base Case
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()

        for k in range(len(nums) + 1):
            dfs(0, [])
        
        return ans