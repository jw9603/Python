# LeetCode 1. TwoSum
# https://leetcode.com/problems/two-sum/
# 1. 완전 탐색: O(n^2)
# https://leetcode.com/problems/two-sum/submissions/1570206224
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
# 2. 해시: O(n)
# https://leetcode.com/problems/two-sum/submissions/1570206032
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in num_dict:
                return [i, num_dict[target_num]]
            num_dict[nums[i]] = i

# 3. Two-Pointer O(NlogN)
# https://leetcode.com/problems/two-sum/submissions/1570209822
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(i, num) for i, num in enumerate(nums)]
        nums.sort(key=lambda x:x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left][1] + nums[right][1]

            if current_sum == target:
                return [nums[left][0], nums[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# 4. DFS: O(N^2) : 메모리 초과
# https://leetcode.com/problems/two-sum/submissions/1570211031
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
        return dfs(0, [])
