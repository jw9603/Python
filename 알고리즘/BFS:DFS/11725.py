# 백준 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
########################### 문제 이해 ###########################
# 루트 없는 트리가 주어진다.
# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구해라.
# 노드의 개수: N개, 
########################### 문제 이해 ###########################

############################ BFS ############################
from collections import deque, defaultdict
def bfs(start, tree, parents):
    queue = deque([start])
    parents[start] = -1

    while queue:
        cur_node = queue.popleft()

        for next_node in tree[cur_node]:
            if parents[next_node] == 0:
                parents[next_node] = cur_node
                queue.append(next_node)
    
    return parents[2:]

def main():
    N = int(input().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    parents = [0] * (N + 1)
    
    print(*bfs(1, tree, parents), sep='\n')

if __name__ == '__main__':
    main()
############################ BFS ############################

############################ DFS ############################
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
def dfs(node, tree, parents):

    for next_node in tree[node]:
        if parents[next_node] == 0:
            parents[next_node] = node
            dfs(next_node, tree, parents)

def main():
    N = int(input().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    parents = [0] * (N + 1)
    parents[1] = -1

    dfs(1, tree, parents)
    print(*parents[2:], sep='\n')

if __name__ == '__main__':
    main()
############################ DFS ############################