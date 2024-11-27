# 이코테 - 그리디 곱하기 혹은 더하기

import sys

S = sys.stdin.readline().strip()
result = int(S[0])
for i in range(1,len(S)):
    
    num = int(S[i])
    
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)
    
    
    
 