# 백준 2577. 숫자의 개수
# https://www.acmicpc.net/problem/2577
def sol(A, B, C):
    total = str(A * B * C)

    for num in '0123456789':
        print(total.count(num))

def main():
    A = int(input().strip())
    B = int(input().strip())
    C = int(input().strip())
    sol(A, B, C)

if __name__ == '__main__':
    main()