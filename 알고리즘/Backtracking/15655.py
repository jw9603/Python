# 백준 15655. N과 M (6)
# https://www.acmicpc.net/problem/15655
############################### 문제 이해 ###############################
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
# N개의 자연수 중에서 M개를 고른 수열, 고른 수열은 오름차순
# 오름차순의 조합
############################### 문제 이해 ###############################
def dup_comb(N, M, nums):
    ans = []
    nums.sort()
    def dfs(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

    dfs(0, [])
    return ans

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for comb in dup_comb(N, M, nums):
        print(*comb)

if __name__ == '__main__':
    main()