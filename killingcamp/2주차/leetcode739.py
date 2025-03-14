# LeetCode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# https://leetcode.com/problems/daily-temperatures/submissions/1573285605
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                result[prev_day] = day - prev_day
            stack.append((day, temp))
        return result
    
if __name__ == '__main__':
    temperatures1 = [73,74,75,71,69,72,76,73]
    sol = Solution()
    print(f"Result1: {sol.dailyTemperatures(temperatures=temperatures1)}")