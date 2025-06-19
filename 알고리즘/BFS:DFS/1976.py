# 백준 1976. 여행 가자
# https://www.acmicpc.net/problem/1976
################################## 문제 이해 ##################################
# 한국에는 N개의 도시가 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다.
# 동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자.
# 중간에 다른 도시를 경유해서 여행을 할 수도 있다.

# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때
# 가능한지 여부를 판별하는 프로그램을 작성하시오. 같은 도시를 여러번 방문하는 것도 가능

# 입력
# 첫 줄에 도시의 수 N, 둘째 줄에 여행 계획에 속한 도시들의 수 M
# 그 다음줄엔 인접 행렬 느낌으로 주어짐, 1은 연결 0은 연결 x

# 알고리즘
# 일단, BFS로 가능해보임,,,
# graph를 defaultdict로 받고, key가 노드, value는 해당 Key와 연결된 노드들의 리스트
# 그러면, 결국 경로가 중요하다기 보다는 여행이 가능한지 아닌지를 판별하는 것이기 때문에
# 여행 계획된 곳이 모두 방문한다면 가능하다는 뜻
################################## 문제 이해 ##################################
from collections import defaultdict, deque
def bfs(start_v, graph, visited):
    queue = deque([start_v])
    visited[start_v] = True

    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

def sol(N, plans, graph):
    visited = [False] * (N + 1)

    bfs(plans[0], graph, visited)

    if all(visited[i] for i in plans):
        return 'YES'
    else:
        return 'NO'

def main():
    N = int(input().strip())
    M = int(input().strip())
    graph = defaultdict(list)

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                graph[i + 1].append(j + 1)

    plans = list(map(int, input().split()))

    print(sol(N, plans, graph))

if __name__ == '__main__':
    main()