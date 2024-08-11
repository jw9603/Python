class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1] * (i+1) for i in range(numRows)]
        

        for i in range(2,numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        
        return pascal
    
if __name__ == '__main__':
    
    a = Solution()
    
    res1 = a.generate(5)
    
    res2 = a.generate(1)
    
    print('res1',res1)
    print('res2',res2)