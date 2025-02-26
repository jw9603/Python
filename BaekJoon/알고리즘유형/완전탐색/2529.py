# 백준 2529. 부등호
# https://www.acmicpc.net/problem/2529
import sys
def is_valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

def main():
    k = int(sys.stdin.readline().strip())
    inequalities = sys.stdin.readline().strip().split()
    
    visited = [False] * 10
    result = []
    
    def dfs(depth, num_list):
        
        if depth == k + 1:
            result.append(''.join(map(str, num_list)))
            return
        
        for i in range(10):
            if not visited[i]:
                if depth == 0 or is_valid(num_list[-1], i, inequalities[depth - 1]):
                    visited[i] = True
                    dfs(depth + 1, num_list + [i])
                    visited[i] = False
    
    dfs(0, [])
    print(max(result), min(result), sep='\n')
main()