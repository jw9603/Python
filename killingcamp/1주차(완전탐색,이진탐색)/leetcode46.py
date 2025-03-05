# Leetcode 46. Permutations
# https://leetcode.com/problems/permutations/
# https://leetcode.com/problems/word-search/submissions/1563717945
# 시간 복잡도: O(N!)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(curr):
            # 1. base case
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(curr)
                    curr.pop()
        dfs([])
        return ans
        
        
if __name__ == '__main__':
    nums1, nums2, nums3 = [1, 2, 3], [0, 1], [1]
    sol = Solution()
    print(f"Result1: {sol.permute(nums=nums1)}")
    print(f"Result2: {sol.permute(nums=nums2)}")
    print(f"Result3: {sol.permute(nums=nums3)}")