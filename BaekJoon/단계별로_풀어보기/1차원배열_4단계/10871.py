import sys

A, X =map(int,sys.stdin.readline().split())
n_list = list(map(int,input().split()))

print(' '.join([str(i) for i in n_list if i < X]))