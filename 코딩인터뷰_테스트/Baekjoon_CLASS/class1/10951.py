# 백준 10951. A + B - 4
# https://www.acmicpc.net/problem/10951
def sol(a, b):
    return a + b

def main():
    while 1:
        try:
            A, B = map(int, input().split())
            print(sol(A, B))
        except:
            break

if __name__ == '__main__':
    main()