# LeetCode 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
from collections import Counter
from bisect import *
class Solution(object):
    # 1. Hash Table: O(n)
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        result = []

        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))
        
        return result

    # 2. Two Pointer
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        i = j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result

    # 3. Binary Search
    def intersect3(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2.sort()
        result = []

        for num in nums1:
            idx = bisect_left(nums2, num)

            if idx < len(nums2) and nums2[idx] == num:
                result.append(num)
                nums2.pop(idx)
        
        return result

if __name__ == '__main__':
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]

    a = Solution()

    print(f"Hash Table Method: {a.intersect1(nums1, nums2)}")
    print(f"Two Pointer Method: {a.intersect2(nums1, nums2)}")
    print(f"Binary Search Method: {a.intersect3(nums1, nums2)}")