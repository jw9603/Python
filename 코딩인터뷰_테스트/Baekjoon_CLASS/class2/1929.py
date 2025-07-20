# 백준 1929. 소수 구하기
# https://www.acmicpc.net/problem/1929
def sol(M, N):
    is_prime = [False] * 2 + [True] * (N + 1)

    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    return '\n'.join(map(str, [i for i in range(M, N + 1) if is_prime[i]]))

def main():
    M, N = map(int, input().split())
    print(sol(M, N))

if __name__ == '__main__':
    main()