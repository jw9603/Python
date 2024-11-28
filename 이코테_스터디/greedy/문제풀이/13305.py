# 13305. 주유소
# https://www.acmicpc.net/problem/13305

import sys

N = int(sys.stdin.readline().strip())
distance = list(map(int,sys.stdin.readline().split())) # 2 3 1
price = list(map(int,sys.stdin.readline().split()))    # 5 2 4 1

def sol(N, distance, price):
    min_price = price[0]
    result = 0
    
    for i in range(N-1):
        if min_price > price[i]:
            min_price = price[i]
        
        result += min_price * distance[i]
    
    return result

print(sol(N=N, distance=distance, price=price))