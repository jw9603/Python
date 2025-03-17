# LeetCode 32. Longest Valid Parntheses
# https://leetcode.com/problems/longest-valid-parentheses/submissions/1576249268
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else: # char == ')'
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)
        return max_length

if __name__ == '__main__':
    sol = Solution()
    s1, s2, s3 = "(()", ")()())", ""
    print(f"Result1: {sol.longestValidParentheses(s=s1)}")
    print(f"Result2: {sol.longestValidParentheses(s=s2)}")
    print(f"Result3: {sol.longestValidParentheses(s=s3)}")