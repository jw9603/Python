# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

class MyHashSet(object):

    def __init__(self):
        self.table = [False] * 10000001
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.table[key] = True

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.table[key] = False
 

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return True if self.table[key] else False
