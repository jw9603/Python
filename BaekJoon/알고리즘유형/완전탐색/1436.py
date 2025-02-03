# 백준 1436. 영화감독 숌
# https://www.acmicpc.net/problem/1436
import sys
N = int(sys.stdin.readline().strip())
def sol(N):
    cnt = 0
    final_num = 666
    while True:
        
        if '666' in str(final_num):
            cnt += 1
            
        if cnt == N:
            break
        
        final_num += 1
    return final_num

print(sol(N=N))
    