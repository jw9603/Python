# LeetCode 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
from collections import deque
class Solution(object):
    # 1. 리스트 활용
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True    

    # 2. Deque 활용
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
    
    # 3. Two Pointer
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True