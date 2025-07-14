# 백준 10818. 최소, 최대
# https://www.acmicpc.net/problem/10818
def main():
    N = int(input().strip())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))

if __name__ =='__main__':
    main()