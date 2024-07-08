def solution(num_list):
    
    even = ''
    odd = ''
    for i in num_list:
        if i %2 ==0:
            even += str(i)
        else:
            odd += str(i)
    return int(even)+int(odd)

if __name__ == '__main__':
    print(solution([3,4,5,2,1]))
    print(solution([5,7,8,3]))