def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if not(set(str(i)) - set(['0','5'])):
            answer.append(i)
    #         print(set(str(i)))
    #         print('hi',set(str(i)) - set(['0','5']))
    # # print(set(['0','5']))
        
    return answer if answer else [-1]

if __name__ =='__main__':
    print(solution(5,555))
    print(solution(10,20))