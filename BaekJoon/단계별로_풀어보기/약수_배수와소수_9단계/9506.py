# 9506 - 약수들의 합 
# https://www.acmicpc.net/problem/9506

import sys

while True:
    n = int(sys.stdin.readline().strip())
    
    if n == -1:
        break
    
    arr = []
    for i in range(1,n):
        if n % i == 0:
            arr.append(i)
    
    if sum(arr) == n:
        print(f"{n} = " + ' + '.join(str(i) for i in arr))
    else:
        print(f"{n} is NOT perfect.")