import sys

N, M = map(int,sys.stdin.readline().split())
basket = [i for i in range(N+1)]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    
    basket[i], basket[j] = basket[j], basket[i]
for i in basket[1:]:
    print(i,end=' ')