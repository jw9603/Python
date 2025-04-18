# 백준 1697. 숨바꼭질
# https://www.acmicpc.net/workbook/view/22734
################################ 문제 이해 ################################
# 수빈이는 현재 점 N에 위치
# 동생은 K에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 걷는다면 1초 후에 x - 1 or x + 1로 이동
# 순간이동을 하는 경우에는 1초에 2 * x의 위치로 이동하게 된다.

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구해라
################################ 문제 이해 ################################
from collections import deque
def bfs(N, K):
    queue = deque([(N, 0)])
    visited = [False] * 100001

    while queue:
        cur_v, cur_t = queue.popleft()
        if cur_v == K:
            return cur_t
        
        for next_v in [cur_v - 1, cur_v + 1, cur_v * 2]:
            if 0 <= next_v <= 100000 and not visited[next_v]:
                queue.append((next_v, cur_t + 1))
                visited[next_v] = True
                
def main():
    N, K = map(int, input().split())
    print(bfs(N, K))

if __name__ == '__main__':
    main()