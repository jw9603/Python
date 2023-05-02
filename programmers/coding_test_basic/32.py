def solution(n):
    cnt = 0
    for i in range(1,n//2+1):
        if n%i==0:
            cnt +=1
    return cnt+1

if __name__ =='__main__':
    print(solution(30))