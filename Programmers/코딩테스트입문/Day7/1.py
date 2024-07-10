def solution(my_string, letter):
    return my_string.replace(letter,'')
# remove 메서드는 가장 앞에 있는 값만을 삭제함. 리스트, 문자열 내에 있는 모든 값을 제거하려면 replace

if __name__== '__main__':
    print(solution("abcdef","f"))
    print(solution("BCBdbe","B"))