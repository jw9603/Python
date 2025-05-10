# 백준 2143. 두 배열의 합
# https://www.acmicpc.net/problem/2143
############################# 문제 이해 ##############################
# 한 배열에 대해 부 배열은 말 그대로 일부 배열이다.
# 각 원소가 정수인 두 배열, A[1], ... , A[n]과 B[1], ..., B[m]이 주어졌을 때,
# A의 부배열의 합에 B의 부배열의 합을 더해서 T가 되는 모든 부 배열의 쌍의 개수
############################# 문제 이해 ##############################
from collections import Counter

def get_subarr_sum(arr):
    n = len(arr)
    sub_sums = []
    for i in range(n):
        sum_val = 0
        for j in range(i, n):
            sum_val += arr[j]
            sub_sums.append(sum_val)
    return sub_sums

def sol(A, B, T):
    A_sums = get_subarr_sum(A)
    B_sums = get_subarr_sum(B)

    B_counter = Counter(B_sums)

    cnt = 0

    for a in A_sums:
        tmp = T - a
        cnt += B_counter.get(tmp, 0)
    
    return cnt


def main():
    T = int(input().strip())
    n = int(input().strip())
    A = list(map(int, input().split()))
    m = int(input().strip())
    B = list(map(int, input().split()))

    print(sol(A, B, T))

if __name__ == '__main__':
    main()