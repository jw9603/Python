# 백준 10814. 나이순 정렬
# https://www.acmicpc.net/problem/10814
def main():
    N = int(input().strip())
    members = [list(input().split()) for _ in range(N)]

    members.sort(key=lambda x: int(x[0]))

    for member in members:
        print(*member)

if __name__ == '__main__':
    main()