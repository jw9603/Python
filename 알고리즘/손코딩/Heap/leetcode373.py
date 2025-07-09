# LeetCode 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150
from heapq import *
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        if not nums1 or not nums2 or k == 0:
            return result
        
        min_heap = []

        for i in range(min(len(nums1), k)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while min_heap and len(result) < k:
            _, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i , j + 1))
        
        return result
    
    # 정렬 풀이: Memory Limit Exceeded
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        
        for i in nums1:
            for j in nums2:
                result.append([i, j])
        result.sort(key=lambda x: x[0] + x[1])
        
        return result[:k]