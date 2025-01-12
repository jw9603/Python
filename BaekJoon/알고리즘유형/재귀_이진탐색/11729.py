# 백준 11729. 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
import sys
N = int(sys.stdin.readline().strip())
def hanoi(N, start, target, mid):
    # 1. base case
    if N == 1:
        print(start, target)
        return
    
    # 2. 재귀 호출
    hanoi(N - 1, start, mid, target)
    print(start, target)
    hanoi(N - 1, mid, target, start)

print(2 ** N - 1)
hanoi(N, 1, 3, 2)