def solution(n):
    answer = 0
    num = []
    for i in range(2,n+1): # i == 2
        for j in range(1,i+1): # j == 1, 2
            if i % j == 0:
                num.append(i)
        if num.count(i) >= 3:
            answer += 1
                
    return answer

if __name__ == '__main__':
    print(solution(10))
    print(solution(15))