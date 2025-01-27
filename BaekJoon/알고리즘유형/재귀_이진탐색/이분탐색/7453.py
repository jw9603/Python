# # 백준 7453. 합이 0인 네 정수
# # https://www.acmicpc.net/problem/7453

# #################### 이분 탐색 (시간 초과) ######################
import sys
from bisect import *
N = int(sys.stdin.readline().strip())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

def sol(N, AB, CD):
    cnt = 0
    
    for ab in AB:
        target = -ab
        left_idx = bisect_left(CD, target)
        right_idx = bisect_right(CD, target)
        cnt += (right_idx - left_idx)
        
    return cnt
print(sol(N=N, AB=AB, CD=CD))
# #################### 이분 탐색 (시간 초과) ######################

# ##################### 투 포인터 풀이 (시간 초과)############################
import sys
N = int(sys.stdin.readline().strip())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

def sol(N, AB, CD):
    cnt = 0
    left, right = 0, len(CD) - 1
    
    while left < len(AB) and right >= 0:
        current_sum = AB[left] + CD[right]
        
        if current_sum == 0:
            left_count, right_count = 1, 1
            
            while left + 1 < len(AB) and AB[left] == AB[left + 1]:
                left += 1
                left_count += 1
                
            while right - 1 >= 0 and CD[right] == CD[right - 1]:
                right -= 1
                right_count += 1
            
            cnt += left_count * right_count
            left += 1
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1
    return cnt
print(sol(N=N, AB=AB, CD=CD))
##################### 투 포인터 풀이 (시간초과)############################

##################### 딕셔너리 풀이 ############################
import sys
N = int(sys.stdin.readline().strip())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

def sol(N, A, B, C, D):
    cnt = 0
    ab = dict()
    for a in A:
        for b in B:
            v = a + b
            if v not in ab:
                ab[v] = 1
            else:
                ab[v] += 1
    for c in C:
        for d in D:
            target = -1 * (c + d)
            if target in ab:
                cnt += ab[target]
    return cnt

print(sol(N=N, A=A, B=B, C=C, D=D))
##################### 딕셔너리 풀이 ############################