# 백준 1330. 두 수 비교하기
# https://www.acmicpc.net/problem/1330
def sol(a, b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '=='
    
def main():
    a, b = map(int, input().split())

    print(sol(a, b))

if __name__ == '__main__':
    main()