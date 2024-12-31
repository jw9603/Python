# 백준 2810. 컵홀더
# https://www.acmicpc.net/problem/2810
import sys
N = int(sys.stdin.readline().strip())
seat = sys.stdin.readline().strip()
def sol(N, seats):
    cnt = 0
    i = 0
    while i < N:
        if seats[i] == 'S':
            cnt += 1
            i += 1
        else:
            i += 2
            cnt += 1
    return min(N, cnt + 1)
print(sol(N=N, seats=seat))