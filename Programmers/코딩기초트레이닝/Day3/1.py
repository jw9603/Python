def solution(str1, str2):
    return ''.join(str1[i]+str2[i] for i in range(len(str1)))

if __name__ =='__main__':
    print(solution("aaaaa",	"bbbbb"))