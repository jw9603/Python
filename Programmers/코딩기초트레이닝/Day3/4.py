def solution(a, b):
    return int(str(a)+str(b)) if int(str(a)+str(b)) >= int(str(b)+str(a)) else int(str(b)+str(a))

if __name__ == '__main__':
    print(solution(9,91))