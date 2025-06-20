# LeetCode 79. Word Search
# https://leetcode.com/problems/word-search/description/
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # m x n board와 문자열 word가 주어졌을 때, word가 board에 있는지 없는지 반환해라.
        # 단어는 연속적으로 인접한 셀로부터 구성될 수 있고, 인접은 수평, 수직 이웃 다 적용.

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, depth):
            # Base Case
            if depth == len(word):
                return True
            
            if not(0 <= r < m and 0 <= c < n) or visited[r][c] or board[r][c] != word[depth]:
                return False
            
            visited[r][c] = True
            for dr, dc in directions:
                if dfs(r + dr, c + dc, depth + 1):
                    return True
            visited[r][c] = False
            
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False  