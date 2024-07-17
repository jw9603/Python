def solution(num_list, n):
    return num_list[n:] + num_list[:n]

if __name__ == '__main__':
    print(solution([2,1,6],1))
    print(solution([5,2,1,7,5],3))