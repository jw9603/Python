def solution(num, k):
    return str(num).find(str(k))+1 if str(num).find(str(k))+1 else -1

if __name__ =='__main__':
    print(solution(29183,1))