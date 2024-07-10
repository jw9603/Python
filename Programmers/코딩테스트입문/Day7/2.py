def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1
    
if __name__ =='__main__':
    print(solution(70))
    print(solution(91))
    print(solution(180))