# 백준 10989. 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys
N = int(sys.stdin.readline().strip())
def sol(N):
    n_list = [0] * 10001
    for _ in range(N): # 10^7
        n_list[int(sys.stdin.readline().strip())] += 1
    for i in range(len(n_list)): # 10^4
        if n_list[i] != 0:
            for j in range(n_list[i]):
                print(i)
sol(N=N)
