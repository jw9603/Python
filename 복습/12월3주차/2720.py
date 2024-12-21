# 백준 2720. 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    charge = int(sys.stdin.readline().strip())
    result = []
    for i in [25, 10, 5, 1]:
        result.append(charge // i)
        charge %= i
    print(' '.join(map(str, result)))