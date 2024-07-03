def solution(numbers):
    return [i*2 for i in numbers]

if __name__ =='__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1, 2, 100, -99, 1, 2, 3]))