# 11650 - 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline().strip())

dot_list = []

for _ in range(N):
        x, y = map(int,sys.stdin.readline().split())
        dot_list.append([x,y])
        
def sol(dot_list):
    dot_list.sort(key=lambda x: (x[0],x[1]))

    for x,y in dot_list:
        print(x,y)

sol(dot_list=dot_list)
    