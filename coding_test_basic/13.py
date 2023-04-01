def solution(n):
    return n // 7  if n%7==0 else n // 7 + 1

if __name__ == '__main__':
    print(solution(29))