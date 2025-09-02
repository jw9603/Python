# LeetCode 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1