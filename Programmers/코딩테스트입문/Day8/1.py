def solution(numbers, num1, num2):

    return numbers[num1:num2+1]

if __name__ == '__main__':
    print(solution([1,2,3,4,5],1,3))
    print(solution([1,3,5],1,2))