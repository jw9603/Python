# 백준 11727. 2xn 타일링 2
# https://www.acmicpc.net/problem/11727
################################# 문제 이해 #################################
# 2 x n 직사각형을 1 x 2, 2 x 1, 2 x 2 타일로 채우는 방법의 수를 구하는 프로그램을 작성
# 점화식: f(n) = f(n - 1) + 2 * f(n - 2)
################################# 문제 이해 #################################
def sol(n):
    tab = [0] * (n + 1)
    if n == 1:
        return 1
    if n == 2:
        return 3
    tab[1] = 1
    tab[2] = 3
    
    for i in range(3, n + 1):
        tab[i] = tab[i - 1] + 2 * tab[i - 2]

    return tab[n] % 10007

def main():
    n = int(input().strip())
    print(sol(n))

if __name__ == '__main__':
    main()