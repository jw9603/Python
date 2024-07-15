import sys

N = int(sys.stdin.readline().strip())
n_list = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline().strip())
print(n_list.count(v))