# 백준 11725. 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
####################### BFS #######################
import sys
from collections import defaultdict, deque
def bfs(node, tree, parents):
    queue = deque([node])
    parents[node] = -1

    while queue:
        cur_node = queue.popleft()

        for next_node in tree[cur_node]:
            if parents[next_node] == 0:
                parents[next_node] = cur_node
                queue.append(next_node)
    return parents[2:]


def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    
    print(*bfs(1, tree, parents), sep='\n')

if __name__ == '__main__':
    main()
####################### BFS #######################

####################### DFS #######################
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def dfs(node, tree, parents):

    for next_node in tree[node]:
        if parents[next_node] == 0:
            parents[next_node] = node
            dfs(next_node, tree, parents)
def main():
    N = int(sys.stdin.readline().strip())
    tree = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)
    parents = [0] * (N + 1)
    parents[1] = -1
    dfs(1, tree, parents)
    print(*parents[2:], sep='\n')

if __name__ == '__main__':
    main()
####################### DFS #######################