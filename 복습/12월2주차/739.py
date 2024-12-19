# LeetCode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                prev_day, _ = stack.pop()
                ans[prev_day] = i - prev_day

            stack.append((i, t))
        return ans