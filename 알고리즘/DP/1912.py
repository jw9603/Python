# 백준 1912. 연속합
# https://www.acmicpc.net/problem/1912
################################ 문제 이해 ################################
# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 이 중에서 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.  

# 연속된이라,,,
# tab[n] = n번째 인덱스에서 연속된 합의 최댓값
# 점화식: tab[n] = max(tab[n - 1] + arr[n], arr[n])
################################ 문제 이해 ################################
def sol(nums, n):
    tab = [0] * n
    tab[0] = nums[0]
    for i in range(1, n):
        tab[i] = max(tab[i - 1] + nums[i], nums[i])
    
    return max(tab)

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sol(nums, n))

if __name__ == '__main__':
    main()