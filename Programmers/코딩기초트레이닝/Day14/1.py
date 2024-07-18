def solution(num_list):
    return sum(num_list[0::2]) if sum(num_list[0::2]) > sum(num_list[1::2]) else sum(num_list[1::2])

if __name__ == '__main__':
    print(solution([4, 2, 6, 1, 7, 6]))
    print(solution([-1, 2, 5, 6, 3]))