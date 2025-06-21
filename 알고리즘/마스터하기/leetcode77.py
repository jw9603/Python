# LeetCode 77. Combinations
# https://leetcode.com/problems/combinations/
# 1. BackTracking
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        visited = [False] * (n + 1)

        def dfs(start, curr):
            # Base Case
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(start, n + 1):
                if not visited[i]:
                    visited[i] = True
                    curr.append(i)
                    dfs(i + 1, curr)
                    visited[i] = False
                    curr.pop()
        
        dfs(1, [])

        return ans
    
# 2. Itertools
from itertools import combinations
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [comb for comb in combinations(range(1, n + 1), k)]