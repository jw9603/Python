# Leetcode 79. Word Search
# https://leetcode.com/problems/word-search/description/
# https://leetcode.com/problems/word-search/submissions/1563717945
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0]) 
        visited = [[False] * n for _ in range(m)]
        
        # dfs를 만든다.
        def dfs(depth, r, c):
            # 1. base case
            if depth == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c] or board[r][c] != word[depth]:
                return False

            visited[r][c] = True
            # 상, 하, 좌, 우 갔다가 안되면 다시 돌아와야 하므로 한 방향으로 간 것이 False 가 나온다면 다시 시작(BT)
            move = (
                dfs(depth + 1, r - 1, c) or # 상
                dfs(depth + 1, r + 1, c) or # 하
                dfs(depth + 1, r, c - 1) or # 좌
                dfs(depth + 1, r, c + 1)    # 우
            )
           
            visited[r][c] = False
            return move

        # Board를 돌면서 word의 한 문자씩 비교한다.
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        return False

if __name__ == '__main__':
    sol = Solution()
    board1, word1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
    board2, word2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"
    board3, word3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"
    
    print(f"Result1: {sol.exist(board=board1, word=word1)}")
    print(f"Result2: {sol.exist(board=board2, word=word2)}")
    print(f"Result3: {sol.exist(board=board3, word=word3)}")
    