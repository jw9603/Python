def solution(a, b, flag):
    return a+b if flag==True else a-b

if __name__ =='__main__':
    print(solution(-4,7,'true'))
    print(solution(-4,7,'false'))