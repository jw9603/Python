def solution(array, n):
    array.sort(key=lambda x: (abs(x-n),x-n))
    return array[0]

if __name__ == '__main__':
    print(solution([3,10,28],20))
    print(solution([10,11,12],13))