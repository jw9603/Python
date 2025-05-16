# 백준 15654. N과 M (5) 
# https://www.acmicpc.net/problem/15654
############################### 문제 이해 ###############################
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 해당 문제는 순열을 구하는 문제
############################### 문제 이해 ###############################
def permutations(nums, M):
    ans = []
    nums.sort()
    used = [False] * len(nums)
    
    def dfs(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                curr.append(nums[i])
                dfs(curr)
                curr.pop()
                used[i] = False
    dfs([])
    return ans


def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for perm in permutations(nums, M):
        print(*perm)

if __name__ == '__main__':
    main()