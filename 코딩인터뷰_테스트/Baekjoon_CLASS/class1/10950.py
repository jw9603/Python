# 백준 10950. A + B - 3
# https://www.acmicpc.net/problem/10950
def sol(a, b):
    return a + b

def main():
    T = int(input().strip())
    for _ in range(T):
        A, B = map(int, input().split())
        print(sol(A, B))

if __name__ == '__main__':
    main()