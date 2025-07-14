# 백준 2562. 최댓값
# https://www.acmicpc.net/problem/2562
def main():
    nums = [int(input().strip()) for _ in range(9)]
    print(max(nums))
    print(nums.index(max(nums)) + 1)

if __name__ == '__main__':
    main()