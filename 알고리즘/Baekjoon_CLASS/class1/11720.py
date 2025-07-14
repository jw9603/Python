# 백준 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720
def main():
    N = int(input().strip())
    nums = list(map(int, input().strip()))
    print(sum(nums))

if __name__ == '__main__':
    main()