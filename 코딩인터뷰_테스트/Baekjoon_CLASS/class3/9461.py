# 백준 9461. 파도반 수열
# https://www.acmicpc.net/problem/9461
############################## 문제 이해 ##############################
# 파도반 수열 P(N)은 다음과 같이 정의된다.

# P(1) = P(2) = P(3) = 1
# P(N) = P(N  - 1) + P(N - 5) (N ≥ 4)
############################## 문제 이해 ##############################
def sol(n):
    if n <= 3:
        return 1
    if n == 4 or n == 5:
        return 2
    tab = [0] * (n + 1)
    tab[1], tab[2], tab[3], tab[4], tab[5] = 1, 1, 1, 2, 2
    for i in range(6, n + 1):
        tab[i] = tab[i - 1] + tab[i - 5]
    
    return tab[n]
    
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sol(N))

if __name__ == '__main__':
    main()