# 백준 1676. 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676
############################## 문제 이해 ##############################
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구해라
# 0 <= N <= 500

# 알고리즘
# 0! = 1
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6
# 4! = 1 * 2 * 3 * 4 = 24
# 5! = 1 * 2 * 3 * 4 * 5 = 120 -> 1개
# 6! = 1 * 2 * 3 * 4* 5 * 6 = 720 -> 1개
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040 -> 1개
# 8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = 40320 -> 1개
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 = 362880 -> 1개
# 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800 -> 2개
############################## 문제 이해 ##############################
# 1. O(NlogN)
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def sol(N):
    value = factorial(N)
    value = str(value)[::-1]
    cnt = 0

    for val in value:
        if val == '0':
            cnt += 1
        else:
            break
    
    return cnt

def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()

# 2. O(N)
def sol(N):
    cnt = 0

    while N >= 5:
        N //= 5
        cnt += N
    
    return cnt

def main():
    N = int(input().strip())
    print(sol(N))

if __name__ == '__main__':
    main()