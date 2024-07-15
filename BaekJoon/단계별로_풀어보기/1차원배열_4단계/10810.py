import sys

N, M = map(int,sys.stdin.readline().split())
basket = [0] * (N+1)

for _ in range(M):
    i,j,k = map(int,sys.stdin.readline().split())
    
    for num in range(i,j+1):
        basket[num] = k
for i in basket[1:]:
    print(i,end=' ')