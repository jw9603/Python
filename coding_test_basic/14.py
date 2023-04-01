def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):  # 최소공배수
    return a * b / gcd(a, b)

def solution(n):
    return int(lcm(n,6) / 6)

if __name__ == '__main__':
    print(solution(15))

