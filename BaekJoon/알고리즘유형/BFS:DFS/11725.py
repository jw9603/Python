# 백준 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
############################# BFS 풀이 #################################
import sys
from collections import defaultdict, deque

def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    def bfs(node, tree, parents):
        q = deque([node])
        parents[node] = -1
        
        while q:
            cur_node = q.popleft()
            for child_node in tree[cur_node]:
                if parents[child_node] == 0:
                    parents[child_node] = cur_node
                    q.append(child_node)
        return parents[2:]
    print(*bfs(node=1, tree=tree, parents=parents), sep='\n')
main()
############################# BFS 풀이 #################################


############################# DFS 풀이 #################################
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    
    def dfs(node, tree, parents):
        for child_node in tree[node]:
            if parents[child_node] == 0:
                parents[child_node] = node
                dfs(child_node, tree, parents)
    dfs(node=1, tree=tree, parents=parents)
    print(*parents[2:], sep='\n')
main()        
############################# DFS 풀이 #################################