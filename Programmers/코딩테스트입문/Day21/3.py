# 삼각형의 완성 조건 (2)
def solution(sides):
    answer = 0
    max_len = max(sides)
    min_len = min(sides)
    
    # sides에 있는 변이 가장 긴 경우
    for i in range(max_len-min_len+1, max_len+1): 
        answer += 1
        
    # 새로운 변이 가장 긴 경우
    for i in range(max_len+1, min_len + max_len):
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution([1,2]))
    print(solution([3,6]))
    print(solution([11,7]))