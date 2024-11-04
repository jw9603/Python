# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for p in s:
            if p == '[':
                stack.append(']')
            elif p == '{':
                stack.append('}')
            elif p == '(':
                stack.append(')')
            elif not stack or stack.pop() != p:
                return False
        return not stack 
    
if __name__ == '__main__':
    
    a = Solution()
    
    print(a.isValid('()'))
    print(a.isValid("()[]{}"))
    print(a.isValid("(]"))
    print(a.isValid("([])"))
    