# 이코테 그리디 - 큰 수의 법칙
import sys

N, M, K = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))


def sol(N,M,K,num_list):

    num_list.sort() # O(NlogN)

    a = num_list[-1]
    b = num_list[-2]


    result = 0

    while 1: # O(M)
        for _ in range(K): # O(K)
            if M == 0:
                break
            result += a
            M -= 1
        if M == 0:
            break
        
        result += b
        M -= 1
    return result

print(sol(N=N,M=M,K=K,num_list=num_list))

    
    