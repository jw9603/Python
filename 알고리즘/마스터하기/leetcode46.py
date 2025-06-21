# LeetCode 46. Permutations
# https://leetcode.com/problems/permutations/description/

# 1. BackTracking
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        서로 다른 정수로 이루어진 배열 nums가 주어졌을 때, 생성될 수 있는 모든 순열을 반환
        """
        ans = []
        visited = [False] * (len(nums) + 1)

        def dfs(curr):
            # Base Case
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    curr.append(nums[i])
                    dfs(curr)
                    visited[i] = False
                    curr.pop()
        dfs([])

        return ans
# 2. Itertools
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        서로 다른 정수로 이루어진 배열 nums가 주어졌을 때, 생성될 수 있는 모든 순열을 반환
        """
        return [perm for perm in permutations(nums)]
