def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i in range(len(my_string)):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        elif my_string[i] == '-':
            answer -= int(my_string[i+1])
        else:
            continue
    return answer


############### 다른 풀이 #######################
def solution(my_string):
    return eval(my_string)
############### 다른 풀이 #######################
if __name__ == '__main__':
    print(solution("3 + 4"))