def solution(start_num, end_num):
    return [i for i in range(start_num,end_num-1,-1)]

if __name__ == '__main__':
    print(solution(10,3))