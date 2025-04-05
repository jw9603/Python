# 백준 16235. 나무 재테크
# https://www.acmicpc.net/problem/16235
def season(N, K, A, trees, directions):

    nutrients = [[5] * N for _ in range(N)]

    for _ in range(K):
        # 봄
        # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
        # 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
        # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
        # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
        
        dead = [[[] for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not trees[i][j]:
                    continue
                
                trees[i][j].sort()
                
                survived = []
                for age in trees[i][j]:
                    if nutrients[i][j] >= age:
                        nutrients[i][j] -= age
                        survived.append(age + 1)
                    else:
                        dead[i][j].append(age)
                trees[i][j] = survived
            
        # 여름: 봄에 죽은 나무가 양분으로 변하게 된다. 
        # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
        for i in range(N):
            for j in range(N):
                for dead_age in dead[i][j]:
                    nutrients[i][j] += dead_age // 2
        
        # 가을: 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 
        # 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
        for i in range(N):
            for j in range(N):
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for dx, dy in directions:
                            next_i, next_j = i + dx, j + dy
                            if 0 <= next_i < N and 0 <= next_j < N:
                                trees[next_i][next_j].insert(0, 1)
        
        # 겨울: S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
        # 각 칸에 추가되는 양분의 양은 A[r][c]
        for i in range(N):
            for j in range(N):
                nutrients[i][j] += A[i][j]

    result = 0
    for i in range(N):
        for j in range(N):
            result += len(trees[i][j])
    
    return result

def main():
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    trees = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().split()) # z는 나이
        trees[x - 1][y - 1].append(z)
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    print(season(N, K, A, trees, directions))

if __name__ == '__main__':
    main()