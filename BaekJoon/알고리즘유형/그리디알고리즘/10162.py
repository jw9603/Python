# 백준 10162. 전자레인지
# https://www.acmicpc.net/problem/10162
import sys
T = int(sys.stdin.readline().strip())
def sol(T):
    if T % 10 != 0:
        return -1
    result = []
    # A, B, C = [300, 60, 10]
    for t in [300, 60, 10]:
        result.append(T // t)
        T %= t
    return ' '.join(map(str, result))
print(sol(T=T))
        