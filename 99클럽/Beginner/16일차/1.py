# 최소 직사각형

def solution(sizes):
    # w = 가로, h = 세로
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

def solution(sizes):
    max_width = max_height = 0 # 가로, 세로 최댓값 초기화
    
    for size in sizes:
        width, height = size
        
        
        max_width = max(max_width, width, height) # 전체 명함 중에서 가장 큰 최대값을 찾는다.
         
        max_height = max(max_height,min(width,height)) # 명함 하나하나의 가로 길이와 세로 길이 중 더 작은 값들을 모아 그 중에서 가장 큰 최대 값을 찾는다.
        
    return max_width * max_height

def solution(sizes):
    w = [] # 큰 것들
    h = [] # 작은 것들
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0]) 
            h.append(sizes[i][1]) 
        else: 
            h.append(sizes[i][0])
            w.append(sizes[i][1])
            
    return max(w) * max(h)


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))