# 백준 2438. 별 찍기 - 1
# https://www.acmicpc.net/problem/2438
def sol(n):
    for i in range(1, n + 1):
        print('*' * i)

def main():
    N = int(input().strip())
    sol(N)

if __name__ == '__main__':
    main()