# LeetCode 703. Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
from heapq import *
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.min_heap, val)
        
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        
        return self.min_heap[0]

