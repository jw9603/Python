# 백준 9663. N-Queen
# https://www.acmicpc.net/problem/9663
######################## 뭔가 백트래킹에 직접적인 코드 ##########################
import sys
def is_available(candidate, current_col):
    current_row = len(candidate)
    
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == abs(current_row - queen_row):
            return False
    return True

def dfs(N, current_row, current_candidate):
    global cnt
    if current_row == N:
        cnt += 1
        return
    
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(N, current_row + 1, current_candidate)
            current_candidate.pop()

def main():
    global grid, cnt
    N = int(sys.stdin.readline().strip())
    grid = [0] * N
    cnt = 0
    dfs(N=N, current_row=0, current_candidate=[])
    print(cnt)

if __name__ == '__main__':
    main()
######################## 뭔가 백트래킹에 직접적인 코드 ##########################