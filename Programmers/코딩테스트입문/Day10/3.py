def solution(numbers, k):
    return numbers[2 * (k-1) % len(numbers)]

if __name__ == '__main__':
    print(solution([1,2,3,4],2))
    print(solution([1,2,3,4,5,6],5))
    print(solution([1,2,3],3))