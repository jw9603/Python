def solution(slice, n):
    return n // slice if n% slice == 0 else n // slice + 1

if __name__ =='__main__':
    print(solution(5,12))