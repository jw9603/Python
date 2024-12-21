# 백준 2751. 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys
N = int(sys.stdin.readline().strip())
print('\n'.join(map(str,sorted([int(sys.stdin.readline().strip()) for _ in range(N)]))))
