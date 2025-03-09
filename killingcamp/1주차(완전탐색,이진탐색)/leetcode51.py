# LeetCode 51. N-Queens
# https://leetcode.com/problems/n-queens/description/
# https://leetcode.com/problems/n-queens/submissions/1567831650
class Solution(object):
    def is_available(self, candidate, current_col):
        current_row = len(candidate)

        for queen_row in range(current_row):
            if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == abs(queen_row - current_row):
                return False
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        def dfs(n, current_row, current_candidate):
            # 1. base case
            if current_row == n:
                board = []
                for row in range(n):
                    line = ["."] * n 
                    line[current_candidate[row]] = "Q"
                    board.append("".join(line))
                ans.append(board)
                return
            
            for current_col in range(n):
                if self.is_available(current_candidate, current_col):
                    current_candidate.append(current_col)
                    dfs(n, current_row + 1, current_candidate)
                    current_candidate.pop()

        dfs(n, 0, [])
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    n1, n2 = 4, 1
    print(f"Result1: {sol.solveNQueens(n=n1)}")
    print(f"Result2: {sol.solveNQueens(n=n2)}")