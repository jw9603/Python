import math
def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    return [num//math.gcd(num,denom),denom//math.gcd(num,denom)]

if __name__ =='__main__':
    print(solution(1,2,3,4))
    print(solution(9,2,1,3))