def solution(my_string):
    my_string = my_string.lower()
    ans = []
    for i in my_string:
        ans.append(ord(i))
    return ''.join(sorted(chr(i) for i in ans))

if __name__ =='__main__':
    print(solution("heLLo"))