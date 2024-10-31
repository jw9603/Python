# 10814 - 나이순 정렬
# https://www.acmicpc.net/problem/10814

import sys

N = int(sys.stdin.readline().strip())

information = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    information.append([int(age),name])

information.sort(key=lambda x: x[0])    

for i in information:
    print(i[0],i[1])