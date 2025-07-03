# LeetCode 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/
# 1. DP
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i]: i번째 원소를 마지막으로 하는 LIS길이
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# 2. Binary Search
# 1. DP
from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sub[i]: 길이 i + 1인 증가 부분 수열의 마지막 원소의 최솟값
        sub = []

        for num in nums:
            idx = bisect_left(sub, num)

            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        
        return len(sub)