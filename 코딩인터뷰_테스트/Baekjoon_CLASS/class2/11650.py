# 백준 11650. 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
def sol(dots):
    return sorted(dots, key=lambda x:(x[0], x[1]))

def main():
    N = int(input().strip())
    dots = [list(map(int, input().split())) for _ in range(N)]
    
    result = sol(dots)

    for dot in result:
        print(*dot)

if __name__ == '__main__':
    main()