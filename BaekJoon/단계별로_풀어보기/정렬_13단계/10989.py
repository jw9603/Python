# 10989 - 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys



###################### 메모리 초과 #########################
# def sol(n_list):
    
#     n_list.sort()
    
#     for i in n_list:
#         print(i)


# N = int(sys.stdin.readline().strip())
# n_list = []
# for _ in range(N):
#     n_list.append(int(sys.stdin.readline().strip()))

# sol(n_list)
###################### 메모리 초과 #########################
import sys

N = int(sys.stdin.readline().strip())
n_list = [0] * 10001

for _ in range(N):
    n_list[int(sys.stdin.readline().strip())] += 1

print(n_list)

for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)