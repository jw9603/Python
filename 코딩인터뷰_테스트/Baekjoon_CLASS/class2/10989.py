# 백준 10989. 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys
def sorting(N):
    count = [0] * 10001

    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        count[num] += 1

    for i in range(1, 10001):
        if count[i] > 0:
            for _ in range(count[i]):
                print(i)
    
def main():
    N = int(sys.stdin.readline().strip())
    sorting(N)
    
if __name__ == '__main__':
    main()