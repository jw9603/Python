# LeetCode 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

# 1. Brute Force (iterative) - O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 정수배열 nums가 주어지고, 정수 target이 주어졌을 때,
        # nums배열에서 두 개의 값을 선택하여 target을 만드는 두 개의 값의 인덱스를 리턴

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2. Hash - O(n)
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

# 3. Two Pointer - O(nlogn)
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
# 4. BackTrack - Memory Limit Exceeded
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def dfs(start, curr):
            if len(curr) == 2 and sum(nums[i] for i in curr) == target:
                return curr

            for i in range(start, len(nums)):
                curr.append(i)
                res = dfs(i + 1, curr)
                if res:
                    return res
                curr.pop()

            return None

        return dfs(0, [])