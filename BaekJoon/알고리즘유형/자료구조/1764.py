# 백준 1764. 듣보잡
# https://www.acmicpc.net/problem/1764
import sys
N, M = map(int, sys.stdin.readline().split())
unlisten = set([sys.stdin.readline().strip() for _ in range(N)])
unseen = set([sys.stdin.readline().strip() for _ in range(M)])
result = list(unlisten & unseen)
print(len(result), *sorted(result),sep='\n')
