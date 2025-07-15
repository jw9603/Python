# 백준 1978. 소수 찾기
# https://www.acmicpc.net/problem/1978
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def sol(nums):
    cnt = 0

    for num in nums:
        if is_prime(num):
            cnt += 1
    
    return cnt

def main():
    N = int(input().strip())
    nums = list(map(int, input().split()))

    print(sol(nums))

if __name__ == '__main__':
    main()