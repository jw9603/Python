# 백준 2828. 사과 담기 게임
# https://www.acmicpc.net/problem/2828
import sys
N, M = map(int, sys.stdin.readline().split()) # N: 스크린, M: 바구니
J = int(sys.stdin.readline().strip()) # 떨어지는 사과의 개수
apples = [int(sys.stdin.readline().strip()) for _ in range(J)]
def sol(N, M, J, apples):
    left = 1
    right = M
    total = 0
    for apple in apples:
        if apple == left & apple == right:
            continue
        elif apple < left:
            total += left - apple
            left = apple
            right = left + M - 1
        elif apple > right:
            total += apple - right
            right = apple
            left = right - M + 1
    return total
print(sol(N=N, M=M, J=J, apples=apples))