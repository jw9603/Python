# LeetCode 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        알고리즘:
        1. 전체 행렬을 transpose를 한다.
        
        [[1, 2, 3],       
         [4, 5, 6],    
         [7, 8, 9]]   
         ->
        [[1, 4, 7],       
         [2, 5, 8],    
         [3, 6, 9]]

        2. 각 행을 출력할 때 뒤집어서 출력한다.
        """
        n = len(matrix)

        # 1. Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse
        for row in matrix:
            row.reverse()