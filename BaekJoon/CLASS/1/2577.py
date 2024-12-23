# 백준 2577. 숫자의 개수
# https://www.acmicpc.net/problem/2577
import sys
total = 1
for _ in range(3):
    total *= int(sys.stdin.readline().strip())
result = list(str(total))
print('\n'.join([str(result.count(str(i))) for i in range(10)]))