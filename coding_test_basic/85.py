def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 ==0 or '3' in str(answer):
            answer +=1
       
    return answer

if __name__ == '__main__':
    print(solution(15))