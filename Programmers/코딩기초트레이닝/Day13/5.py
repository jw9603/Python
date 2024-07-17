def solution(num_list, n):
    return num_list[::n]

if __name__ == '__main__':
    print(solution([4, 2, 6, 1, 7, 6],2))
    print(solution([4, 2, 6, 1, 7, 6],4))
    