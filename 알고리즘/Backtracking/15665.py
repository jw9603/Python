# 백준 15665. N과 M (11)
# https://www.acmicpc.net/problem/15665
############################# 문제 이해 #############################
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 중복 순열 문제, 그리고 주어진 수열에 중복된 수가 있더라도 다른 수로 취급
############################# 문제 이해 #############################
def dup_permutations(M, nums):
    ans = set()
    nums.sort()
    # used = [False] * len(nums)

    def dfs(curr):
        if len(curr) == M:
            ans.add(tuple(curr))
            return
        
        for i in range(len(nums)):
            curr.append(nums[i])
            dfs(curr)
            curr.pop()
    
    dfs([])

    return sorted(ans)
        

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for perm in dup_permutations(M, nums):
        print(*perm)

if __name__ == '__main__':
    main()