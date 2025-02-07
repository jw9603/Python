# 백준 10448. 유레카 이론
# https://www.acmicpc.net/problem/10448
import sys
T = int(sys.stdin.readline().strip())
triangle = [i * (i + 1) // 2 for i in range(1, 46)]
eureka = [0] * 1001 
def make_tri(triangle, eureka):  
    for i in triangle:
        for j in triangle:
            for k in triangle:
                num = i + j + k
                if num <= 1000:
                    eureka[num] = 1
make_tri(triangle=triangle, eureka=eureka)
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    print(eureka[k])