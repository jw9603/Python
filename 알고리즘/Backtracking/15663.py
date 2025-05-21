# 백준 15663. N과 M (9)
# https://www.acmicpc.net/problem/15663
##################################### 문제 이해 #####################################
# N개의 자연수 중에서 M개를 고른 수열
# 순열 문제이다. 하지만, 기존의 순열 처리 방식처럼 문제를 풀면 안된다.
# 왜냐하면, 주어지는 자연수 배열에 같은 수가 반복되면 이전 풀이 방식대로 하면 중복으로 판별하여
# 제거된다. 하지만 해당 문제는 주어진 배열에 중복되는 숫자가 있더라도 이것을 다른수로 판별하고 해야 한다.
##################################### 문제 이해 #####################################
def permutations(N, M, nums):
    ans = set()
    nums.sort()
    used = [False] * (N + 1)

    def dfs(curr):
        if len(curr) == M:
            ans.add(tuple(curr))
            return
        
        for i in range(N):
            if not used[i]:
                used[i] = True
                curr.append(nums[i])
                dfs(curr)
                curr.pop()
                used[i] = False
    dfs([])

    return sorted(ans)

def main():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for perm in permutations(N, M, nums):
        print(*perm)
    
if __name__ == '__main__':
    main()