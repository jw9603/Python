###################### 1부터 n까지의 합을 활용한 풀이 ########################
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        return len(nums)*(len(nums)+1) // 2 - sum(nums)
###################### 1부터 n까지의 합을 활용한 풀이 ########################

###################### 1부터 n까지의 합을 활용한 풀이 (max) ########################
class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        return max(nums)*(max(nums)+1) // 2 - sum(nums)
###################### 1부터 n까지의 합을 활용한 풀이 (max) ########################



######################### 이진 탐색 풀이 (재귀함수) #########################
class Solution_bs1(object):
    def missingNumber(self,nums):
        
        nums.sort()
        
        return self.binarySearch(nums,0,len(nums)-1)
        
    
    def binarySearch(self,nums,left,right):
        
        if left > right:
            return left
        
        med = (left + right) // 2
        
        if nums[med] > med:
            return self.binarySearch(nums,left,med-1)
        else:
            return self.binarySearch(nums, med+1, right)
######################### 이진 탐색 풀이 (재귀함수) #########################


######################### 이진 탐색 풀이 (반복문) #########################
class Solution_bs2(object):
    def missingNumber(self,nums):
        
        nums.sort()
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            med = (left + right) // 2
            
            if nums[med] > med:
                right = med -1
            else:
                left = med + 1
        return left
######################### 이진 탐색 풀이 (재귀함수) #########################



####################### Hash 풀이 ####################################
class Solution_hash(object):
    
    def missingNumber(self,nums):
        
        nums_dict = {}
        
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
    
        for i in range(len(nums)+1):
            return i
####################### Hash 풀이 ####################################


###################### 비트 연산자 (XOR) 풀이 #############################
class Solution_xor(object):
    def missingNumber(self, nums):
        xor_all = 0
        xor_nums = 0

        # 1. 0부터 n까지의 숫자를 모두 XOR합니다.
        for i in range(len(nums) + 1):
            xor_all ^= i

        # 2. nums 배열에 있는 모든 숫자를 XOR합니다.
        for num in nums:
            xor_nums ^= num

        # 3. 두 XOR의 결과를 다시 XOR하여 누락된 숫자를 찾습니다.
        return xor_all ^ xor_nums

###################### 비트 연산자 (XOR) 풀이 #############################


if __name__ == '__main__':
    
    import time
    
    a = time.time()
    # 1. 1부터 n까지의 합을 활용한 풀이 (len)
    a1 = Solution1()
    a2 = Solution1()
    a3 = Solution1()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using sum: {res1}')
    print(f'TestCase2 using sum: {res2}') 
    print(f'TestCase3 using sum: {res3}')     
    
    print(f'{time.time()-a:.4f}')
    
    # 2. 1부터 n까지의 합을 활용한 풀이 (max)
    a = time.time()
    
    a1 = Solution2()
    a2 = Solution2()
    a3 = Solution2()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using sum (max): {res1}')
    print(f'TestCase2 using sum (max): {res2}') 
    print(f'TestCase3 using sum (max): {res3}')   
    
    print(f'{time.time()-a:.8f}')
    
    # 3. 이진 탐색 풀이 (재귀함수)
    a = time.time()
    
    a1 = Solution_bs1()
    a2 = Solution_bs1()
    a3 = Solution_bs1()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using binary search (recursive): {res1}')
    print(f'TestCase2 using binary search (recursive): {res2}') 
    print(f'TestCase3 using binary search (recursive): {res3}')   
    
    print(f'{time.time()-a:.8f}')
    
    # 3. 이진 탐색 풀이 (반복문)
    a = time.time()
    
    a1 = Solution_bs2()
    a2 = Solution_bs2()
    a3 = Solution_bs2()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using binary search (iterative): {res1}')
    print(f'TestCase2 using binary search (iterative): {res2}') 
    print(f'TestCase3 using binary search (iterative): {res3}')   
    
    print(f'{time.time()-a:.8f}')
    
    # 4. Hash
    a = time.time()
    
    a1 = Solution_hash()
    a2 = Solution_hash()
    a3 = Solution_hash()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using Hash Table: {res1}')
    print(f'TestCase2 using Hash Table: {res2}') 
    print(f'TestCase3 using Hash Table: {res3}')   
    
    print(f'{time.time()-a:.8f}')
    
    # 5. 비트 연산자 (XOR)
    a = time.time()
    
    a1 = Solution_xor()
    a2 = Solution_xor()
    a3 = Solution_xor()
    
    res1 = a1.missingNumber([3,0,1])
    res2 = a2.missingNumber([0,1])
    res3 = a3.missingNumber([9,6,4,2,3,5,7,0,1])
    
    print(f'TestCase1 using XOR: {res1}')
    print(f'TestCase2 using XOR: {res2}') 
    print(f'TestCase3 using XOR: {res3}')   
    
    print(f'{time.time()-a:.8f}')
