# 백준 3052. 나머지
# https://www.acmicpc.net/problem/3052
def main():
    nums = [int(input().strip()) for _ in range(10)]
    print(len(set([num % 42 for num in nums])))

if __name__ == '__main__':
    main()