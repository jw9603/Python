# Leetcode 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
# 1. Exhaustive Search (완전 탐색): O(N^2)
# https://leetcode.com/problems/two-sum/submissions/1562559543
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2. Hash Table (Dict): O(N)
# https://leetcode.com/problems/two-sum/submissions/1562563184/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict = {}

        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in target_dict:
                return [i, target_dict[target_num]]
            target_dict[nums[i]] = i

# 3. Two-Pointer: O(NlogN)
# https://leetcode.com/problems/two-sum/submissions/1562572545
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x:x[0])
        
        left, right = 0, len(nums) - 1
        while left < right:
            expected_target = nums[left][0] + nums[right][0]
            
            if expected_target == target:
                return [nums[left][1], nums[right][1]]
            elif expected_target < target:
                left += 1
            else:
                right -= 1

# 4. BackTracking: O(2^N), 실패
# https://leetcode.com/problems/two-sum/submissions/1562616623
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 

        def backtrack(start, curr):
            if len(curr) == 2 and sum(nums[i] for i in curr) == target:
                return curr
       
            for i in range(start, len(nums)):
                curr.append(i)
                res = backtrack(i + 1, curr)
                if res:
                    return res
                curr.pop()
            return None
        return backtrack(0, [])
        