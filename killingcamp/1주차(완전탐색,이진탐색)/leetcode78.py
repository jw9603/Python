# Leetcode78. Subsets
# https://leetcode.com/problems/subsets/description/
# https://leetcode.com/problems/subsets/submissions/1563735154
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, curr):
            # 1. base case
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

if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3], [0]
    sol = Solution()
    print(f"Result1: {sol.subsets(nums=nums1)}")
    print(f"Result2: {sol.subsets(nums=nums2)}")
        