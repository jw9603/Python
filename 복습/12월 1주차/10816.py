# 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys

N = int(sys.stdin.readline().strip())
card = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().split()))

result = {}
result2 = []
for i in card:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for i in num:
    if i in result:
        result2.append(result[i])
    else:
        result2.append(0)
print(' '.join([str(i) for i in result2]))
        