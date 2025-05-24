# 백준 15666. N과 M (12)
# https://www.acmicpc.net/problem/15666
####################### 문제 이해 #######################
# 주어진 문제는 중복 조합 문제
# 하지만 중복된 조합은 제거, 수열은 사전 순으로 증가하는 순서로 출력
####################### 문제 이해 #######################
def dup_comb(N, M, nums):
    ans = set()
    nums.sort()
    
    def dfs(start, curr):
        if len(curr) == M:
            ans.add(tuple(curr))
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            dfs(i, curr)
            curr.pop()
    
    dfs(0, [])

    return sorted(ans)

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for comb in dup_comb(N, M, nums):
        print(*comb)

if __name__ == '__main__':
    main()