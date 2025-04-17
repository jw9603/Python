# 백준 10974. 모든 순열
# https://www.acmicpc.net/problem/10974
########################## 문제 이해 ##########################
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력해라.
# 1 <= N <= 8
########################## 문제 이해 ##########################
def permutations(N):
    used = [False] * (N + 1)
    result = []

    def dfs(curr):
        if len(curr) == N:
            result.append(curr[:])
            return
        
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = True
                curr.append(i)
                dfs(curr)
                used[i] = False
                curr.pop()
    dfs([])
    return result

def main():
    N = int(input().strip())
    
    for perm in permutations(N):
        print(*perm)

if __name__ == '__main__':
    main()