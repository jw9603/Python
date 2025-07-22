# 백준 28702. FizzBuzz
# https://www.acmicpc.net/problem/28702
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    elif n % 3 != 0 and n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def main():
    for i in range(3, 0, -1):
        x = input().strip()
        if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
            n = int(x) + i
    print(fizzbuzz(n))
    
if __name__ == '__main__':
    main()