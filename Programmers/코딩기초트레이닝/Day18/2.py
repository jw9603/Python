def solution(myString):

    return sorted([i for i in myString.split('x') if i!=''])

if __name__ == '__main__':
    print(solution("axbxcxdx"))
    print(solution("dxccxbbbxaaaa"))