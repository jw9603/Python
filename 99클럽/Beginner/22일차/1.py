class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        
        ######################## Sol1 ##############################
        # pascal = [[1]* (i+1) for i in range(rowIndex+1)]

        # for i in range(2,rowIndex+1):
        #     for j in range(1,i):
        #         pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        # return pascal[rowIndex]
        ######################## Sol1 ##############################

        ###################### Sol2 ##########################
        pascal = [1] * (rowIndex+1) # [1,1,1,1]
        # print(pascal)

        for i in range(1,rowIndex+1): # i = 1,2,3
            for j in range(i-1,0,-1): # j = (i=1, j= X), (i=2,j = 1), (i=3, j=2, 1)
                pascal[j] += pascal[j-1]

        return pascal
        ###################### Sol2 ##########################


if __name__ =='__main__':
    
    a =Solution()
    
    res1 = a.getRow(3)
    res2 = a.getRow(0)
    res3 = a.getRow(1)
    
    print('res1',res1)
    print('res2',res2)
    print('res3',res3)
  