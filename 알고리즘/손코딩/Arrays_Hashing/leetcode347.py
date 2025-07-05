# LeetCode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# 1. 해싱과 정렬을 활용한 풀이
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_cnt = Counter(nums)
        nums_cnt = sorted(nums_cnt.items(), key=lambda x: x[1], reverse=True)

        return [items[0] for items in nums_cnt[:k]]

# 2. Heap
from heapq import *
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. 숫자 빈도 계산
        count = Counter(nums)

        # 2. (빈도, 숫자) 튜플을 최소 힙에 넣음
        heap = []
        for num, freq in count.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        
        return [num for _, num in heap]