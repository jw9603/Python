def solution(slice, n):
    return n // slice + 1 if n % slice != 0 else n // slice

if __name__ =='__main__':
    print(solution(7,10))
    print(solution(4,12))