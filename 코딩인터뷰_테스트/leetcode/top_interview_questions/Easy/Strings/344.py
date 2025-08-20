# LeetCode 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/
class Solution(object):
    # 1. Python reverse 메서드
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse() 
    # 2. Two Pointer  
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1;right-=1