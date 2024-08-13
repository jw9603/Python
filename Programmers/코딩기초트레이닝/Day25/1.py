# https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 정수를 나선형으로 배치하기
def solution(n):
    ans = [[0]*n for _ in range(n)]
    
    move = 1 # 우 = 1, 하 = 2, 좌 = 3, 상 = 4
    x = 0
    y = 0
    
    if n == 1:
        return [[1]]
    for i in range(n**2):
        ans[x][y] = i+1
        if move % 4 == 1: # 우
            y += 1
            if y == n-1 or ans[x][y+1] != 0: 
                move += 1
        elif move % 4 == 2: # 하
            x += 1
            if x == n-1 or ans[x+1][y] != 0:
                move += 1
        elif move % 4 == 3: # 좌
            y -= 1
            if y == n-1 or ans[x][y-1] != 0:
                move += 1
        else: # 상
            x -= 1
            if x == n-1 or ans[x-1][y] != 0:
                move += 1
    return ans

if __name__ == '__main__':
    print(solution(4))
    print(solution(5))