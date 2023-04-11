def solution(my_string):
    
    return sum([int(i) for i in my_string if ord(i)>= 48 and ord(i) <= 57])

if __name__ =='__main__':
    print(solution("aAb1B2cC34oOp"))