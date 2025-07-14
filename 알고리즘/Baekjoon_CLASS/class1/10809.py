# 백준 10809. 알파벳 찾기
# https://www.acmicpc.net/problem/10809
def sol(S):
    return [S.find(char) for char in 'abcdefghijklmnopqrstuvwxyz']

def main():
    S = input().strip()
    print(*sol(S))

if __name__ == '__main__':
    main()