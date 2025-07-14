# 백준 2739. 구구단
# https://www.acmicpc.net/problem/2739
def sol(n):
    for i in range(1, 10):
        print(f"{n} * {i} = {n * i}")

def main():
    N = int(input().strip())

    sol(N)

if __name__ == '__main__':
    main()