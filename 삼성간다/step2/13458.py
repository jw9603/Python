# 백준 13458. 시험 감독
# https://www.acmicpc.net/problem/13458
import sys
def sol(A, B, C):
    cnt = 0

    for students in A:
        cnt += 1
        students -= B

        if students > 0:
            cnt += students // C
            if students % C != 0:
                cnt += 1
    
    return cnt

def main():
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    B, C = map(int, sys.stdin.readline().split())

    print(sol(A, B, C))

if __name__ == '__main__':
    main()