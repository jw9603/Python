# 백준 10952. A + B - 5
# https://www.acmicpc.net/problem/10952
def sol(a, b):
    return a + b

def main():
    while 1:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        print(sol(A, B))
        
if __name__ == '__main__':
    main()