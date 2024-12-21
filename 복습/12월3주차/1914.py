# 백준 1914. 하노이 탑
# https://www.acmicpc.net/problem/1914
import sys
N = int(sys.stdin.readline().strip())

# 점화식: p(n) = 2 * p(n - 1) + 1
def sol(N, start, target, middle):
    # base case
    if N == 1:
        print(start, target)
        return
    
    # n-1 개의 원판을 처음에서 중간으로 이동
    sol(N - 1, start, middle, target)
    # 가장 큰 원판을 start -> target
    print(start, target)
    # n -1 개의 원판을 중간에서 target으로 이동
    sol(N - 1, middle, target, start)

if N > 20:
    print(2 ** N - 1)
else:
    print(2 ** N - 1)
    sol(N, 1, 3, 2)