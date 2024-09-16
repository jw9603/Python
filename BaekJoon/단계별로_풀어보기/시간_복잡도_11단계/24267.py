# 24267 - 알고리즘 수업 - 알고리즘의 수행 시간 6
# https://www.acmicpc.net/problem/24267

import sys
n = int(sys.stdin.readline().strip())

print(n*(n-1)*(n-2)//6,3,sep='\n')