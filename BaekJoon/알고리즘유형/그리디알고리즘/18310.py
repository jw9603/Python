# 백준 18310. 안테나
# https://www.acmicpc.net/problem/18310
import sys
N = int(sys.stdin.readline().strip())
house = list(map(int, sys.stdin.readline().split()))
def sol(N, house):
    house.sort()
    return house[(N - 1) // 2]
print(sol(N=N, house=house))