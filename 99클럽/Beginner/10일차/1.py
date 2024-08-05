class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums,reverse=True)[:k]
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums = sorted(self.nums,reverse=True)[:self.k]
        
        return self.nums[-1]
        



# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k=3, nums=[4,5,8,2])
param_1 = obj.add(3)

print(param_1)