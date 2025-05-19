# 백준 3182. 한동이는 공부가 하기 싫어!
# https://www.acmicpc.net/problem/3182
###################################### 문제 이해 ######################################
# 공부도 하지 않으면서 어려운 시험은 통과하고 싶어한다.
# 다른 누군가는 시험의 정답을 알고 있다.
# 한동이는 택민이에게 시험 정답을 물어보았다. 택민이는 답을 모른다고 했지만 택민이는 상준이가 답을 알고 있을 것 같다고 하였다. 그 후, 한동이는 상준이에게 물어보고 그리고..
# -> 이 부분이 뭔가 그래프 느낌
# 한동이가 한 사람에게만 시험문제를 물어볼 수 있다고 할 때, 최대한 많은 선배들을 만날 수 있게
# 하기 위해서 누구에게 시험문제를 물어 볼 것인지를 알려주는 것

# 입력
# 정수 N: 선배들은 1부터 N까지 번호지어져 있다.
# 다음 N줄에 하나의 숫자가 주어진다. 첫 번째 줄은 첫 번째 선배의 대답이고
# 두 번째 줄은 두 번째 선배의 대답. 이렇게 N번째 선배의 대답까지 입력이 주어진다.
###################################### 문제 이해 ######################################
from collections import defaultdict
def dfs(node, cnt, visited):
    global graph
    visited[node] = True
    n = graph[node][0]

    if not visited[n]:
        cnt = dfs(n, cnt + 1, visited)
    
    return cnt

def sol(N):  
    result = [0] * (N + 1)

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        result[i] = dfs(i, 1, visited)

    return result.index(max(result))

def main():
    global graph
    N = int(input().strip())
    graph = defaultdict(list)

    for u in range(1, N + 1):
        v = int(input().strip())
        graph[u].append(v)
    
    print(sol(N=N))
    
if __name__ == '__main__':
    main()