# 11653 - 소인수분해
# https://www.acmicpc.net/problem/11653

import sys

N = int(sys.stdin.readline().strip())

i = 2

while N!= 1:
    
    if N % i == 0:
        print(i)
        N /= i
    else:
        i += 1