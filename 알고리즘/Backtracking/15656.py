# 백준 15656. N과 M (7)
# https://www.acmicpc.net/problem/15656
############################# 문제 이해 #############################
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다 -> 중복
# 즉, 이 문제는 중복 순열을 구하는 문제
# 입력
# N과 M이 주어진다.
# 둘째 줄에 N개의 수가 주어진다. 
# 출력
# 수열은 사전 순으로 증가하는 순서로 출력! -> 정렬
############################# 문제 이해 #############################
def dup_permutations(N, M, nums):
    ans = []
    nums.sort()

    def dfs(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(len(nums)):
            curr.append(nums[i])
            dfs(curr)
            curr.pop()
    
    dfs([])

    return ans

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for perm in dup_permutations(N, M, nums):
        print(*perm)

if __name__ == '__main__':
    main()