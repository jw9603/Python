def solution(my_string):
    
    return sorted([int(i) for i in my_string if ord(i)>= 48 and ord(i) <= 57])

if __name__=='__main__':
    print(solution("p2o4i8gj2"))