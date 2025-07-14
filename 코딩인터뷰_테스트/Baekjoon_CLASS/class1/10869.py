# 백준 10869. 사칙연산
# https://www.acmicpc.net/problem/10869
def sol(A, B):
    print(A + B, A - B, A * B, A // B, A % B, sep='\n')
    
def main():
    A, B = map(int, input().split())
    sol(A, B)

if __name__ == '__main__':
    main()