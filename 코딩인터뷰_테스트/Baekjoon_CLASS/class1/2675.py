# 백준 2675. 문자열 반복
# https://www.acmicpc.net/problem/2675
def sol(R, S):
    R = int(R)
    res = ''
    for s in S:
        res += s * R
    
    return res

def main():
    T = int(input().strip())
    for _ in range(T):
        R, S = input().split()
        print(sol(R, S))

if __name__ == '__main__':
    main()