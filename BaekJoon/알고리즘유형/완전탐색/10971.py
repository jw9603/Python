# 백준 10971. 외판원 순회 2
# https://www.acmicpc.net/problem/10971
############################# 완전 탐색 ###############################
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(N, W):
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
print(sol(N=N, W=W))
############################# 완전 탐색 ###############################

############################# 백트래킹 ###############################
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [False] * N
min_cost = float('inf')

def tsp(depth, current, cost, start):
    global min_cost
    
    if cost >= min_cost:
        return
    
    if depth == N - 1:
        if W[current][start] != 0:
            min_cost = min(min_cost, cost + W[current][start])
        return
    for next_city in range(N):
        if not visited[next_city] and W[current][next_city] != 0:
            visited[next_city] = True
            tsp(depth + 1, next_city, cost + W[current][next_city], start)
            visited[next_city] = False # 백 트래킹

for start in range(N):
    visited[start] = True
    tsp(0, start, 0, start)
    visited[start] = False

print(min_cost)
############################# 백트래킹 ###############################