# 백준 1389. 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
################################### 문제 이해 ###################################
# 케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결
# 될 수 있다. 
# 이 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.


# 천민호는 이강호와 같은 학교에 다니는 사이, 천민호와 최백준는 백준 온라인저지,
# 최백준과 김선영은 같은 스타링크, 김선영과 김도현은 같은 학교 동아리 소속,
# 김도현과 민세희는 같은 학교 사이, == 이강호 - 천민호 - 최백준 - 김선영 - 김도현 - 민세희

# 케빈 베이컨은 미국 헐리우드 영화배우들 끼리 케빈 베이컨 게임을 했을때 나오는 단계의 총 합이 가장 적은 사람
# 오늘은 백준 온라인 저지의 유저 중에서 케빈 베이컨의 수가 가장 적은 사람을 찾으려고 한다.
# 케빈 베이컨수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나는 단계의 합이다.

# BOJ의 유저가 5명, 1과 3, 1과 4, 2와 3, 3과 4, 4와 5가 친구인 경우를 생각해보자.
# 1 <-> 3 <-> 4
# 1 <-> 4 <-> 5
# 2 <-> 3 <-> 4 <-> 5

# 1은 2까지 2단계
# 3까지는 1단계, 4까지는 1단계, 5까지는 2단계 --> 6

# 5명의 유저 중에서 케빈 베이컨의 수가 가장 적은 사람은 3과 4이다.
# BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 작성해라.

# 입력:
# 첫째 줄에 유저의 수 N과 친구 관계의 수 M이 주어진다.
# 둘째 줄부터 M개의 줄에 친구 관계가 주어진다.

# 출력: 
# 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다.
# 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.

# 알고리즘:
# 케빈 베이컨의 수가 가장 작다는 것은 가장 자신으로부터 나머지 사람들과의 거리의 합이 가장 작다는 것을
# 의미하고 거리는 최단 거리가 되어야 유리하다. 즉, BFS!!

################################### 문제 이해 ###################################
from collections import defaultdict, deque
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

def sol(graph, N):
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
    
    print(sol(graph, N))

if __name__ == '__main__':
    main()