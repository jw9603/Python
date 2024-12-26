# 백준 7568. 덩치
# https://www.acmicpc.net/problem/7568
import sys
N = int(sys.stdin.readline().strip())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def sol(N, people):
    result = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
        result.append(cnt + 1)
    print(' '.join(map(str, result)))
sol(N=N, people=people)