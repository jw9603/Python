# 백준 15649. N과 M (1)
# https://www.acmicpc.net/problem/15649
############################# 문제 이해 #############################
# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을
# 모두 구해라

# 즉, 길이 M의 모든 순열을 구하라는 뜻
############################# 문제 이해 #############################
def permutations(N, M):
    ans = []
    used = [False] * (N + 1)

    def dfs(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = True
                curr.append(i)
                dfs(curr)
                used[i] = False
                curr.pop()
    dfs([])

    return ans
    
def main():
    N, M = map(int, input().split())
    for perm in permutations(N, M):
        print(*perm)

if __name__ == '__main__':
    main()