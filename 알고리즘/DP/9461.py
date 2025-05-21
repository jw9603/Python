# 백준 9461. 파도반 수열
# https://www.acmicpc.net/problem/9461
################################# 문제 풀이 #################################
# 각 테스트 케이스마다 P(N)을 출력한다.
# P(N)은 나선에 있는 정삼각형의 변의 길이이다.
################################# 문제 풀이 #################################
def sol(n):
    tab = [0] * 101
    tab[1] = tab[2] = tab[3] = 1

    for i in range(0, 98):
        tab[i + 3] = tab[i] + tab[i + 1]

    return tab[n] 

def main():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(sol(N))

if __name__ == '__main__':
    main()