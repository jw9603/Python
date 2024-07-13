def solution(num_list,n):
    return [num_list[i-n:i] for i in range(n,len(num_list)+1,n)]


# import numpy as np
# def solution(num_list,n):
#     a = np.array(num_list).reshape(-1,n)
#     return a.tolist()

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8],2))
    print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948],3))