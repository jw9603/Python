# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

import timeit
class Solution_bruteforce(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution_twopointer(object):        
    def twoSum(self,nums,target):

        nums = [[n,i] for i,n in enumerate(nums)]
        nums.sort(key=lambda x:x[0])
        l = 0
        r = len(nums)-1

        while l < r:
            num_sum = nums[l][0] + nums[r][0]

            if num_sum == target:
                return [nums[l][1],nums[r][1]]
            elif num_sum < target:
                l += 1
            else:
                r -= 1
                

if __name__ == '__main__':
    # Initialize instances of each solution
    solution_bruteforce = Solution_bruteforce()
    solution_twopointer = Solution_twopointer()
    
    nums = [[2,7,11,15], [3,2,4], [3,3],[3,1,4,5,6,7,8,5,75,756,32,1]]
    target = [9, 6, 6,15]

    for c,(i,j) in enumerate(zip(nums,target)):
        # Measure the execution time for the bruteforce solution
        bruteforce_time = timeit.timeit(lambda: solution_bruteforce.twoSum(i, j), number=10000)

        # Measure the execution time for the two-pointer solution
        twopointer_time = timeit.timeit(lambda: solution_twopointer.twoSum(i, j), number=10000)

        print(f" Case {c+1}의 완전탐색: {bruteforce_time}과 투포인터: {twopointer_time}")

                
                
