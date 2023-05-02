def solution(num_list, n):

    return [num_list[i:i+n] for i in range(0,len(num_list),n)]

if __name__ =='__main__':
    print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))