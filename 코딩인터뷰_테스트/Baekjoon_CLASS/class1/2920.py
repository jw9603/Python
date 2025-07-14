# 백준 2920. 음계
# https://www.acmicpc.net/problem/2920
def main():
    nums = list(map(int, input().split()))
    
    if nums == sorted(nums):
        return 'ascending'
    elif nums == sorted(nums, reverse=True):
        return 'descending'
    else:
        return 'mixed'

if __name__ == '__main__':
    print(main())