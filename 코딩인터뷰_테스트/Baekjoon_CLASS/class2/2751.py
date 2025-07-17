# 백준 2751. 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys
def main():
    N = int(input().strip())
    nums = list(int(sys.stdin.readline().strip()) for _ in range(N))
    print(*sorted(nums), sep='\n')

if __name__ == '__main__':
    main()