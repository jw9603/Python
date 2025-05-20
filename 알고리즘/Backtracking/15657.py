# 백준 15657. N과 M (8)
# https://www.acmicpc.net/problem/15657
########################## 문제 이해 ##########################
# N개의 자연수 중에서 M개를 고른 수열, 같은 수를 여러 번 골라도 된다. -> 중복
# 고른 수열은 비내림차순, 같거나 오름차순이란 뜻 -> 중복 조합
# 결국 이 문제는 중복 조합 문제
########################## 문제 이해 ##########################
def dup_combinations(N, M, nums):
    ans = []
    nums.sort()

    def dfs(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            dfs(i, curr)
            curr.pop()
    
    dfs(0, [])
    return ans

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for comb in dup_combinations(N, M, nums):
        print(*comb)

if __name__ == '__main__':
    main()