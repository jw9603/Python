# LeetCode 912
# https://leetcode.com/problems/sort-an-array/
class Solution(object):
    # 1. Quick Sort - Memory Limit Exceeded
    # def sortArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     if len(nums) <= 1:
    #         return nums
        
    #     pivot = nums[0]
    #     tail = nums[1:]

    #     left = [x for x in tail if x <= pivot]
    #     right = [x for x in tail if x > pivot]

    #     return self.sortArray(left) + [pivot] + self.sortArray(right)
    # 2. Merge Sort
    def merge(self, left, right):
        merged = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])

        return merged

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)