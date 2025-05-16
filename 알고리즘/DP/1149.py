# 백준 1149. RGB거리
# https://www.acmicpc.net/problem/1149
############################# 문제 이해 #############################
# 집이 N개있다. 거리는 선분으로 나타낼 수 있고, 1번부터 N번집이 순서대로 있음.
# 집은 R, G, B중 하나의 색으로 칠해야 한다.
# 각각의 집을 R, G, B로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을
# 칠하는 비용의 최솟값을 구해보자.
# 아래 규칙:
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N - 1번 집의 색과 같지 않아야 한다.
# i번의 집은 i - 1번, i + 1번 집의 색과 같지 않아야 한다.

############################# 문제 이해 #############################
def min_cost(costs, N):
    '''
    costs[i][0]: i번집을 R로 칠하는데 드는 비용
    tab[i][0]: i번집의 R로 칠하는데 드는 최소 비용
    tab[i][1]: i번집의 G로 칠하는데 드는 최소 비용
    tab[i][2]: i번집의 B로 칠하는데 드는 최소 비용
    '''
    tab = [[0] * 3 for _ in range(N)]

    tab[0][0], tab[0][1], tab[0][2] = costs[0][0], costs[0][1], costs[0][2]

    for i in range(1, N):
        tab[i][0] = min(tab[i - 1][1]+ costs[i][0], tab[i - 1][2] + costs[i][0])
        tab[i][1] = min(tab[i - 1][0]+ costs[i][1], tab[i - 1][2] + costs[i][1])
        tab[i][2] = min(tab[i - 1][0] + costs[i][2], tab[i - 1][1] + costs[i][2])
    
    return min(tab[N - 1][0], tab[N - 1][1], tab[N - 1][2])

def main():
    N = int(input().strip())
    costs = [list(map(int, input().split())) for _ in range(N)]

    print(min_cost(costs, N))

if __name__ == '__main__':
    main()