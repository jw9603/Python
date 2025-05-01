# 백준 10971. 외판원 순회 2
# https://www.acmicpc.net/problem/10971
############################# 문제 풀이 #############################
# 1번부터 N번까지 번호가 매겨져 있는 도시들이 있다.
# 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회
# 단, 한 번 갔던 도시로는 다시 갈 수 없다.
# 각 도시간에 이동하는 데 드는 비용은 행렬 W[i][j]형태로 주어진다.
# W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 의미
# W[i][j] == 0

############################# 문제 풀이 #############################
def tsp(depth, curr, cost, start):
    global min_cost, N, W, visited

    if cost >= min_cost:
        return
    
    if depth == N - 1:
        if W[curr][start] != 0:
            min_cost = min(min_cost, cost + W[curr][start])
        return
    
    for next_city in range(N):
        if not visited[next_city] and W[curr][next_city] != 0:
            visited[next_city] = True
            tsp(depth + 1, next_city, cost + W[curr][next_city], start)
            visited[next_city] = False

def sol(N):
    global min_cost, visited
    min_cost = float('inf')
    visited = [False] * N

    for i in range(N):
        visited[i] = True
        tsp(0, i, 0, i)
        visited[i] = False
    return min_cost

def main():
    global N, W
    N = int(input().strip())
    W = [list(map(int, input().split())) for _ in range(N)]

    print(sol(N))

if __name__ == '__main__':
    main()