# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/description/?envType=problem-list-v2&envId=linked-list&difficulty=EASY

class MyHashMap(object):

    def __init__(self):
        self.map = [-1] * 10000001

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.map[key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.map[key] = -1
  
        