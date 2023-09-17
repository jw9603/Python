def solution(line):
    answer = []
    pos = []
    n = len(line)
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    for i in range(n): # 3
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            
            if a*d - b*c == 0:
                continue
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)
            
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                if x_min > x:
                    x_min = x
                if y_min > y:
                    y_min = y
                if x_max < x:
                    x_max = x
                if y_max < y:
                    y_max = y
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    # print(x_len) 
    # print(y_len)
    point = [['.']* x_len for _ in range(y_len)]
    # print(pos)
    for s_x,s_y in pos:
        nx = s_x + abs(x_min) if x_min <0 else s_x - x_min
        ny = s_y +abs(y_min) if y_min < 0 else s_y - y_min
        point[ny][nx] = '*'
    for result in point:
        answer.append(''.join(result))
        
    
    return answer[::-1]


if __name__ =='__main__':
    
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))