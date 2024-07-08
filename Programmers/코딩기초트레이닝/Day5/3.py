def solution(a, b, c):
    ans = [a,b,c]
    if len(set(ans)) == 1:
        return sum(ans) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    elif len(set(ans)) == 2:
        return sum(ans) * (a**2+b**2+c**2)
    else:
        return sum(ans)
    
if __name__ =='__main__':
    print(solution(2,6,1))
    print(solution(5,3,3))
    print(solution(4,4,4))