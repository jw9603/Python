# 이코테 그리디 - 숫자 카드 게임
import sys

N, M = map(int,sys.stdin.readline().split())

result = 0
for i in range(N): # O(N*M)
    card = list(map(int,sys.stdin.readline().split()))
    
    min_val = min(card)
    
    result = max(result,min_val)

print(result)