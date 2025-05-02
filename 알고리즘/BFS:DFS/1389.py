# 백준 1389. 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
############################# 문제 이해 #############################
# 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
# 케빈 베이컨은 단계의 총 합이 가장 적은 사람이라고 한다.

############################# 문제 이해 #############################
from collections import deque, defaultdict
def bfs(start, N, graph):
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    total_dist = 0

    while queue:
        cur_friend, cur_step = queue.popleft()
        total_dist += cur_step

        for next_friend in graph[cur_friend]:
            if not visited[next_friend]:
                visited[next_friend] = True
                queue.append((next_friend, cur_step + 1))
    
    return total_dist

def min_kevin_backon(N, graph):
    min_kevin = float('inf')
    ans = -1

    for i in range(1, N + 1):
        kevin_number = bfs(i, N, graph)
        if kevin_number < min_kevin:
            min_kevin = kevin_number
            ans = i

    return ans

def main():
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(min_kevin_backon(N, graph))

if __name__ == '__main__':
    main()