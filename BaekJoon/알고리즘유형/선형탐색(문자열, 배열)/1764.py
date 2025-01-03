# 1764. 듣보잡
# https://www.acmicpc.net/problem/1764
import sys
N, M = map(int, sys.stdin.readline().split())
unseen = set()
unlisten = set()
for _ in range(N):
    unlisten.add(sys.stdin.readline().strip())
for _ in range(M):
    unseen.add(sys.stdin.readline().strip())
print(len(sorted(list(unlisten & unseen))),'\n'.join(sorted(list(unlisten & unseen))),sep='\n')