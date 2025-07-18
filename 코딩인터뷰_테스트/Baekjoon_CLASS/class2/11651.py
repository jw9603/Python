# 백준 11651. 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
def sol(dots):
    return sorted(dots, key=lambda x:(x[1], x[0]))

def main():
    N = int(input().strip())
    dots = [list(map(int, input().split())) for _ in range(N)]
    
    result = sol(dots)

    for dot in result:
        print(*dot)

if __name__ == '__main__':
    main()