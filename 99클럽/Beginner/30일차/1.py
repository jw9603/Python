################### 수학적 풀이 #########################
import math
class Solution_math(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int((-1 + math.sqrt(1 + 8 * n)) // 2)
################### 수학적 풀이 #########################

################### Binary Search (iterative) ###################
class Solution_iterative(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        low, high = 1, n

        while low <= high:

            mid = (low + high) // 2

            current = mid * (mid+1) // 2

            if current == n:
                return mid
            elif current < n:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
################### Binary Search (iterative) ###################


################### Binary Search (recursive) ###################
class Solution_recursive(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(n,1,n)

    def binarySearch(self,n,low,high):

        if low > high:
            return high
        
        mid = (low + high) // 2
        current = mid * (mid + 1) // 2

        if current == n:
            return mid
        elif current < n:
            return self.binarySearch(n,mid+1,high)
        else:
            return self.binarySearch(n,low,mid-1)
################### Binary Search (recursive) ###################


if __name__ == '__main__':
    
    import time
    
    # 1. 수학적 풀이
    a = time.time()
    
    a1 = Solution_math()
    
    res1 = a1.arrangeCoins(5)
    res2 = a1.arrangeCoins(8)
    
    print(f'TestCase1 using math: {res1}')
    print(f'TestCase2 using math: {res2}') 
    
    print(f'{time.time()-a:.8f}')
    
    
    # 2. Binary Search using Recursive
    a = time.time()
    
    a1 = Solution_recursive()
    
    res1 = a1.arrangeCoins(5)
    res2 = a1.arrangeCoins(8)
    
    print(f'TestCase1 using recursive: {res1}')
    print(f'TestCase2 using recursive: {res2}') 
    
    print(f'{time.time()-a:.8f}')
    
    
    # 3. Binary Search using iterative
    a = time.time()
    
    a1 = Solution_iterative()
    
    res1 = a1.arrangeCoins(5)
    res2 = a1.arrangeCoins(8)
    
    print(f'TestCase1 using iterative: {res1}')
    print(f'TestCase2 using iterative: {res2}') 
    
    print(f'{time.time()-a:.8f}')