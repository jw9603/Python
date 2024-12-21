# 백준 2750. 수 정렬하기
# https://www.acmicpc.net/problem/2750
import sys
N = int(sys.stdin.readline().strip())
print('\n'.join(map(str,sorted([int(sys.stdin.readline().strip()) for _ in range(N)]))))

