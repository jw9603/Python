def solution(arr, delete_list):

    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

if __name__ == '__main__':
    
    print(solution([293, 1000, 395, 678, 94],[94, 777, 104, 1000, 1, 12]))
    print(solution([110, 66, 439, 785, 1],	[377, 823, 119, 43]))
    print(solution([1,2,3,4],[1,2,3,4,5]))
    print(solution([1,2,3,4,5],[1,2,3,4]))