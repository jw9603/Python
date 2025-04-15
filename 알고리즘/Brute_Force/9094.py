# 백준 9094. 수학적 호기심
# https://www.acmicpc.net/problem/9094
def solve_math(n, m):
    cnt = 0

    for a in range(1, n):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1
    
    return cnt

def main():
    T = int(input().strip())
    for _ in range(T):
        n, m = map(int, input().split())
        print(solve_math(n, m))

if __name__ == '__main__':
    main()