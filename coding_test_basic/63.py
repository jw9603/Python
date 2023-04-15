def solution(my_string):
    my_string = my_string.split()
    ans = int(my_string[0])
    for i in range(1,len(my_string),2):
        if my_string[i] == '+':
            ans += int(my_string[i+1])
        else:
            ans -= int(my_string[i+1])
    return ans

if __name__ == '__main__':
    print(solution("3 - 4 + 10"))