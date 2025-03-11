# LeetCode 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
# https://leetcode.com/problems/valid-parentheses/submissions/1570221085
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char:
                return False
        return not stack
    
if __name__ == '__main__':
    sol = Solution()
    s1, s2, s3, s4 = "()", "()[]{}", "(]", "([])"

    print(f"Result1: {sol.isValid(s=s1)}")
    print(f"Result2: {sol.isValid(s=s2)}")
    print(f"Result3: {sol.isValid(s=s3)}")
    print(f"Result4: {sol.isValid(s=s4)}")
