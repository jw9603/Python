# 백준 11050. 이항 계수 1
# https://www.acmicpc.net/problem/11050
def combinations(N, K):
    ans = []

    def dfs(start, curr):
        if len(curr) == K:
            ans.append(curr[:])
            return
        
        for i in range(start, N + 1):
            curr.append(i)
            dfs(i + 1, curr)
            curr.pop()
    
    dfs(1, [])

    return ans

def main():
    N, K = map(int, input().split())

    print(len(combinations(N, K)))

if __name__ == '__main__':
    main()