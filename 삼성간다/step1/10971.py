# 백준 10971. 외판원 순회 2
# https://www.acmicpc.net/problem/10971
################################## itertools 사용 ##################################
import sys
from itertools import permutations

def min_cost(N, W):
    min_cost = float('inf')
    for perm in permutations(range(N)):
        valid = True
        cost = 0
        for i in range(N - 1):
            if W[perm[i]][perm[i + 1]] == 0:
                valid = False
                break

            cost += W[perm[i]][perm[i + 1]]
        if valid and W[perm[-1]][perm[0]] != 0:
            cost += W[perm[-1]][perm[0]]
            min_cost = min(min_cost, cost)
    return min_cost

def main():
    N = int(sys.stdin.readline().strip())
    W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(min_cost(N, W))

if __name__ == '__main__':
    main()
################################# itertools 사용 ##################################

################################# 백트래킹 사용 ##################################
import sys
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

def main():
    global min_cost, N, W, visited
    N = int(sys.stdin.readline().strip())
    W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    min_cost = float('inf')
    visited = ['False'] * N

    for i in range(N):
        visited[i] = True
        tsp(0, i, 0, i)
        visited[i] = False
    print(min_cost)

if __name__ == '__main__':
    main()
################################## 백트래킹 사용 ##################################