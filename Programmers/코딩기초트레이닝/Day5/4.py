def solution(num_list):
    a=1
    for i in num_list:
        a *= i
    return 1 if a < sum(num_list)**2 else 0 

if __name__ =='__main__':
    print(solution([3,4,5,2,1],1))
    print(solution([5,7,8,3],0))