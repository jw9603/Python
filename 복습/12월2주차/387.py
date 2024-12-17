# LeetCode 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
from collections import Counter
from collections import deque
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        count = {}
        
        for i, c in enumerate(s):
            q.append((c,i))
            count[c] = count.get(c, 0) + 1
        
        while q:
            char, idx = q.popleft()
            if count[char] == 1:
                return idx
        return -1
        
    
    
        