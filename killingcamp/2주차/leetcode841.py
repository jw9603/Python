# LeetCode 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/

# https://leetcode.com/problems/keys-and-rooms/submissions/1573317807
# 1. dfs 풀이
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        def dfs(node, rooms, visited):
            visited[node] = True
            for next_v in rooms[node]:
                if not visited[next_v]:
                    dfs(next_v, rooms, visited)
        dfs(0, rooms, visited)
        return all(visited)

# https://leetcode.com/problems/keys-and-rooms/submissions/1573319290
# 2. BFS 풀이
from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)

        def bfs(node):
            visited[node] = True
            queue = deque([node])

            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        queue.append(next_v)
        bfs(0)
        return all(visited)  

if __name__ == '__main__':
    rooms1, rooms2 = [[1],[2],[3],[]], [[1,3],[3,0,1],[2],[0]]
    sol = Solution()

    print(f"Resul1: {sol.canVisitAllRooms(rooms=rooms1)}")
    print(f"Resul2: {sol.canVisitAllRooms(rooms=rooms2)}")