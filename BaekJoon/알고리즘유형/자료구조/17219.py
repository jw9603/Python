# 백준 17219. 비밀번호 찾기
# https://www.acmicpc.net/problem/17219
import sys
N, M = map(int, sys.stdin.readline().split())
site_info = {}
for _ in range(N):
    site_address, password = sys.stdin.readline().split()
    site_info[site_address] = password

for _ in range(M):
    print(site_info[sys.stdin.readline().strip()])
        
