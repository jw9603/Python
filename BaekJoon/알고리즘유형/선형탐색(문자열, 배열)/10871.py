# 백준 10871. X보다 작은 수
# https://www.acmicpc.net/problem/10871
import sys
N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(' '.join(map(str, [i for i in A if i < X])))