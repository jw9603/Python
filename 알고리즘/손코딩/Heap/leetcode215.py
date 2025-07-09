# LeetCode 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150
from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        배열이 주어졌을 때 k번째 큰 배열을 반환해라.
        그리고 정렬을 하지말고,,,!
        k번째로 큰 배열을 뽑는다는 것은 배열의 크기를 k로 만들면 가장 작은 것임
        """
        min_heap = []

        for num in nums:
            heappush(min_heap, num)

        while len(min_heap) > k:
            heappop(min_heap)
        
        return min_heap[0]