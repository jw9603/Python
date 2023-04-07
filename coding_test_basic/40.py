def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in numbers[0:-1]:
            answer.append(i)
    else:
        for i in numbers[1:]:
            answer.append(i)
        answer.append(numbers[0])
            
            
    return answer

if __name__ =='__main__':
    print(solution([1,2,3],'right'))
    print(solution([4, 455, 6, 4, -1, 45, 6],'left'))