# 2720 - 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    c = int(sys.stdin.readline().strip())
    
    for i in [25,10,5,1]:
        print(c // i, end=' ')
        c %= i
    print()
    
    
    
    
    