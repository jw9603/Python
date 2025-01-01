# 백준 19941. 햄버거 분배
# https://www.acmicpc.net/problem/19941
import sys
N, K = map(int, sys.stdin.readline().split())
table = sys.stdin.readline().strip()
def sol(N, K, table):
    people = []
    hamburgers = []
    for i in range(N):
        if table[i] == 'P':
            people.append(i)
        else:
            hamburgers.append(i)
    
    cnt = 0
    i, j = 0, 0
    while i < len(people) and j < len(hamburgers):
        if abs(people[i] - hamburgers[j]) <= K:
            cnt += 1
            i += 1
            j += 1
        elif people[i] < hamburgers[j]:
            i += 1
        else:
            j += 1
    return cnt
print(sol(N=N, K=K, table=table))