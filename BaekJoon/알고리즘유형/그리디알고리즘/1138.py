# 백준 1138. 한 줄로 서기
# https://www.acmicpc.net/problem/1138
import sys
N = int(sys.stdin.readline().strip())
conditions = list(map(int, sys.stdin.readline().split()))

def sol(N, conditions):
    result = [0] * N
    
    for height in range(1, N + 1): # if N = 4, then height: 1, 2, 3, 4
        cnt = conditions[height - 1] # cnt = 2, 1, 1, 0
        empty_cnt = 0
        for i in range(N):
            if result[i] == 0:
                if empty_cnt == cnt:
                    result[i] = height
                    break
                empty_cnt += 1
    return result
print(*sol(N=N, conditions=conditions))
                

                
    
