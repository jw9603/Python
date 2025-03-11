# LeetCode 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/
# https://leetcode.com/problems/sudoku-solver/submissions/1568804351

# 시간 초과: O(9 * 9^(N^2))
class Solution1(object):
    def is_valid(self, r, c, num, board):
        for i in range(9):
            if board[r][i] == num:
                return False
            if board[i][c] == num:
                return False
            
            # 3 x 3 check
            box_r, box_c = 3 * (r // 3), 3 * (c // 3)
            if board[box_r + i // 3][box_c + i % 3] == num:
                return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in map(str, range(1, 10)):
                            if self.is_valid(r, c, num, board):
                                board[r][c] = num
                                if dfs():
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        
        dfs()

# O(1 * 9^(N^2)))
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
        
        def dfs(index):
            # 1. base case
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if dfs(index + 1):
                        return True
                    
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            return False
        dfs(0)

if __name__ == '__main__':
    import time
    sol = Solution()
    sol1 = Solution1()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    
    board1 = [row[:] for row in board]

    start_time = time.time()
    print(f"Result:{sol1.solveSudoku(board=board1)}")
    print(board1)

    end_time = time.time()
    print(f"실패코드 실행 시간: {end_time - start_time:.4f} 초")

    start_time = time.time()
    print(f"Result:{sol.solveSudoku(board=board)}")
    print(board)
    end_time = time.time()
    print(f"통과코드 실행 시간: {end_time - start_time:.4f} 초")