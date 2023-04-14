def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i].islower():
            my_string[i].upper()
            answer += my_string[i].upper()
        else:
            
            answer += my_string[i].lower()
    return answer


## using swapcase ##
def solution(my_string):
    return my_string.swapcase()

if __name__ =='__main__':
    print(solution("abCdEfghIJ"))