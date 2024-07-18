def solution(order):
    answer = 0
    for i in str(order):
        print(i)
        if int(i) % 3 == 0 and i != '0':
            answer +=1
    return answer

if __name__ == '__main__':
    print(solution(3))
    print(solution(29423))