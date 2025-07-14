# 백준 2439. 별 찍기 - 2
# https://www.acmicpc.net/problem/2439
def sol(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + '*' * i) 

def main():
    N = int(input().strip())
    sol(N)

if __name__ == '__main__':
    main()