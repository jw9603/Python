# 백준 15651. N과 M (3)
# https://www.acmicpc.net/problem/15651
############################## 문제 이해 ##############################
# 자연수 N과 M이 주어졌다.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 이 문제는 중복 순열을 구하는 문제라고 볼 수 있다.
############################## 문제 이해 ##############################
def dup_permutations(N, M):
    ans = []

    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(1, N + 1):
            curr.append(i)
            backtrack(curr)
            curr.pop()
            
    backtrack([])

    return ans

def main():
    N, M = map(int, input().split())

    for perm in dup_permutations(N, M):
        print(*perm)

if __name__ == '__main__':
    main()