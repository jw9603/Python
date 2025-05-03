# 백준 15652. N과 M (4)
# https://www.acmicpc.net/problem/15652
############################## 문제 이해 ##############################
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 비 내림차순이여야 한다.
# 이 문제는 중복 조합을 구하는 문제이다.
############################## 문제 이해 ##############################
def dup_combinations(N, M):
    ans = []
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for i in range(start, N + 1):
            curr.append(i)
            backtrack(i, curr)
            curr.pop()
    
    backtrack(1, [])
    return ans

def main():
    N, M = map(int, input().split())
    for comb in dup_combinations(N, M):
        print(*comb)

if __name__ == '__main__':
    main()