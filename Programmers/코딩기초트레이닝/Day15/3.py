def solution(num_list):
    cnt = 0
    for i in num_list:
        while i != 1:
            if i % 2 ==0:
                i = i / 2
                cnt += 1
            else:
                i = (i-1) / 2
                cnt += 1
                
    return cnt

if __name__ == '__main__':
    print(solution([12,4,15,1,14]))