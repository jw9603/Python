# LeetCode 69. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.values()