class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
    
    
if __name__ == '__main__':
    a = Solution()
    
    TestCase1 = a.arrayPairSum([1,4,3,2])
    TestCase2 = a.arrayPairSum([6,2,6,5,1,2])
    
    print('TestCase1',TestCase1)
    print('TestCase2',TestCase2)