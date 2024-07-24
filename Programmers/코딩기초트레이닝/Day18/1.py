def solution(myString):
    return [len(i) for i in myString.split('x')]

if __name__ == '__main__':
    print(solution("oxooxoxxox"))
    print(solution("xabcxdefxghi"))