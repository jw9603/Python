# 백준 1198. 삼각형으로 자르기
# https://www.acmicpc.net/problem/1198
############################# 문제 이해 #############################
# 블록 다각형이 있다.
# 여기서 3개의 연속된 점을 선택해서 삼각형을 만든다. 그 다음 만든 삼각형을 다각형에서 제외
# 원래 다각형이 N개의 점이 있었다면, 이제 N - 1개의 점으로 구성된 볼록 다각형이 됩니다.
# 위의 과정은 남은 다각형이 삼각형이 될 때까지 반복

############################# 문제 이해 #############################
from itertools import combinations
def areas(a, b, c):

    return 1/2 * abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))

def sol(dots):
    max_areas = -1

    for comb in combinations(dots, 3):
        a, b, c = comb[0], comb[1], comb[2]
        max_areas = max(max_areas, areas(a, b, c))
    
    return max_areas

def main():
    N = int(input().strip())
    dots = [list(map(int, input().split())) for _ in range(N)]

    print(sol(dots))

if __name__ == '__main__':
    main()