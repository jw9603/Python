def solution(park, routes):
    directions = {"E":(0,1),'W':(0,-1),'S':(1,0),'N':(-1,0)}
    
    x, y = 0, 0
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i,j
    for route in routes:
        direction, steps = route.split()
        dx, dy = directions[direction] # op에 해당하는 n값
        
        nx = x
        ny = y
        valid = True
        for _ in range(int(steps)):
            nx += dx
            ny += dy
            
            # 좌표가 벗어나는 경우 : 해당 명령을 제외하고 다음 명령으로 넘어가야 한다.
            if not (0 <= nx < len(park) and 0 <= ny < len(park[0])) or park[nx][ny] == 'X':
                valid = False
                break
        if valid:
            x, y = nx, ny
            
    return [x,y]

if __name__ == '__main__':
    print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
    print(solution(["SOO","OXX","OOO"],	["E 2","S 2","W 1"]))
    print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))