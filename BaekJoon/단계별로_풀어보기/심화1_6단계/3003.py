import sys

a = [1,1,2,2,2,8]
chess = list(map(int,sys.stdin.readline().split()))

for i in range(len(chess)):
    print(a[i]-chess[i],end=' ')

