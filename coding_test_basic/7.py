import math
def solution(numer1, denom1, numer2, denom2):
    num = denom1 * numer2 + denom2 * numer1
    denom = denom1 * denom2
    gcd = math.gcd(denom, num)
    return [num//gcd, denom//gcd]

if __name__ == "__main__":
    print(solution(1,2,3,4))
    # print(solution(3,5))
    # print(solution(4,4))