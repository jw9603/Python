# 백준 15650. N과 M (2)
# https://www.acmicpc.net/problem/15650
############################## 문제 이해 ############################## 
# N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 수열이 오름차순 형태!!
# 조합문제이다
############################## 문제 이해 ############################## 
def combinations(N, M):
    ans = []
    visited = [False] * (N + 1)
    def dfs(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, N + 1):
            if not visited[i]:
                visited[i] = True
                curr.append(i)
                dfs(i + 1, curr)
                visited[i] = False
                curr.pop()
    
    dfs(1, [])
    return ans

def main():
    N, M = map(int, input().split())
    for comb in combinations(N, M):
        print(*comb)

if __name__ == '__main__':
    main()