# N개 (N은 홀수)의 파이프
# 파이프들이 헛간에 뿌리를 둔 트리 구조를 형성하며, 모든 기지점에서 두 개의 파이프가 나감 (이진트리)
# 파이프의 길이는 1
# 지도에는 C개의 연결?이 있으며, 각 연결은 세 개의 정수로 구성된다.
# 파이프 E_i (1 <= E_i <= N)의 끝점과 두 개의 가지 파이프 B1_i (2 <= B1_i <= N; 2 <= B2_i <= N). 
# 파이프 번호 1은 헛간과 연결되며, 헛간에서 끝점까지의 거리는 1입니다.

# 입력:
# 첫 번째 줄: 두 개의 정수 N과 C (파이프의 수와 연결의 수)
# 두 번째 줄부터 C+1번째 줄까지: i+1번째 줄에는 세 개의 정수 E_i, B1_i, B2_i가 주어지며, 이는 파이프 i의 끝점과 두 개의 가지 파이프를 설명합니다.

# 출력:

# 1번 파이프부터 N번 파이프까지의 끝점까지 헛간으로부터의 거리를 각 줄에 출력합니다.



######################## BFS ###################################
from collections import deque, defaultdict
import sys

def calculate_distances(N,C,connections):
    
    tree = defaultdict(list)
    
    for E, B1, B2 in connections:
        tree[E].append(B1)
        tree[E].append(B2)
        
    print('tree',tree)
    distances = [-1] * (N+1)
    
    queue = deque([1])
    
    distances[1] = 1
    
    while queue:
        current_pipe = queue.popleft()
        current_distance = distances[current_pipe]
        
        for neighbor in tree[current_pipe]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    for i in range(1,N+1):
        print(distances[i])
        

N, C = map(int,sys.stdin.readline().split())
connections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(C)]

calculate_distances(N, C, connections)
    
    
########################## DFS (recursive) #############################
from collections import defaultdict
import sys

def calculate_distances_dfs_recursive(N, C, connections):
    # 트리를 나타내는 인접 리스트
    tree = defaultdict(list)
    
    # 트리 구조를 만듭니다
    for E, B1, B2 in connections:
        tree[E].append(B1)
        tree[E].append(B2)
    
    # 각 파이프의 거리를 저장할 리스트, 초기값은 -1로 설정
    distances = [-1] * (N + 1)
    
    # 재귀적으로 DFS 구현
    def dfs(pipe, distance):
        distances[pipe] = distance
        for neighbor in tree[pipe]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
                dfs(neighbor, distance + 1)
    
    # DFS 시작: 파이프 1에서 출발 (헛간)
    dfs(1, 1)
    
    # 결과 출력
    for i in range(1, N + 1):
        print(distances[i])

# 입력을 받아서 처리
N, C = map(int,sys.stdin.readline().split())
connections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(C)]

calculate_distances_dfs_recursive(N, C, connections)

########################## DFS (recursive) #############################
        


######################### DFS (stack) ################################
from collections import defaultdict

def calculate_distances_dfs_stack(N, C, connections):
    # 트리를 나타내는 인접 리스트
    tree = defaultdict(list)
    
    # 트리 구조를 만듭니다
    for E, B1, B2 in connections:
        tree[E].append(B1)
        tree[E].append(B2)
    
    # 각 파이프의 거리를 저장할 리스트, 초기값은 -1로 설정
    distances = [-1] * (N + 1)
    
    # 스택을 사용한 DFS 구현
    stack = [(1, 1)]  # (현재 파이프, 현재까지의 거리)
    
    while stack:
        current_pipe, current_distance = stack.pop()
        distances[current_pipe] = current_distance
        
        # 자식 파이프들을 스택에 추가 (방문하지 않은 경우)
        for neighbor in tree[current_pipe]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
                stack.append((neighbor, current_distance + 1))
    
    # 결과 출력
    for i in range(1, N + 1):
        print(distances[i])

N, C = map(int,sys.stdin.readline().split())
connections = [tuple(map(int, sys.stdin.readline().split())) for _ in range(C)]
calculate_distances_dfs_stack(N,C,connections)
######################### DFS (stack) ################################