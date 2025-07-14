# 백준 10871. X보다 작은 수
# https://www.acmicpc.net/problem/10871
def sol(A, X): 
    return [a for a in A if a < X]

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    print(*sol(A, X))

if __name__ == '__main__':
    main()