def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
        
    return True
def solution(n):
    ans = []
    for i in range(2,n+1):
        if n %i ==0:
            ans.append(i)
    ans1 = []
    for i in ans:
        if is_prime(i):
            ans1.append(i)
        else:
            continue
    
    return ans1

if __name__=='__main__':
    print(solution(420))