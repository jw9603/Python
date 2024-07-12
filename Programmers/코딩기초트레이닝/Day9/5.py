def solution(my_string, is_suffix):
    ans = sorted(my_string[i:] for i in range(len(my_string)))
    if is_suffix in ans:
        return 1
    return 0

########## 다른 풀이 ##########
# def solution(my_string, is_suffix):
#     return int(my_string.endswith(is_suffix))
########## 다른 풀이 ##########

if __name__ =='__main__':
    print(solution("banana","ana"))
    print(solution("banana","nan"))
    print(solution("banana","wxyz"))
    print(solution("banana","abanana"))