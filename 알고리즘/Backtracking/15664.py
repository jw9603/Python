# 백준 15664. N과 M (10)
# https://www.acmicpc.net/problem/15664
############################# 문제 이해 #############################
# N개의 자연수 중에서 M개를 고르는 수열
# 고른 수열은 비 내림차순
# ex) nums = [1, 7, 9, 9]
# result -> (1, 7), (1, 9), (7, 9), (9, 9)
# 비내림차순 이기 때문에 조합 문제,
############################# 문제 이해 #############################
def combinations(N, M, nums):
    ans = set()
    nums.sort()
    used = [False] * len(nums)
    def dfs(start, curr):
        if len(curr) == M:
            ans.add(tuple(curr))
            return
        
        for i in range(start, N):
            if not used[i]:
                used[i] = True
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
                used[i] = False
    
    dfs(0, [])

    return sorted(ans)

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for comb in combinations(N, M, nums):
        print(*comb)

if __name__ == '__main__':
    main()