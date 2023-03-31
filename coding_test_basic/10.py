def solution(array):
    array = sorted(array)
    return array[(len(array)-1)//2]

if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([2,4,41,0,2]))