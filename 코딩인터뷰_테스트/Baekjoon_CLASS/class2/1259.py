# 백준 1259. 팰린드롬수
# https://www.acmicpc.net/problem/1259
def is_palindrome(val):
    return val == val[::-1]

def main():
    while 1:
        val = input().strip()
        if int(val) == 0:
            break
        
        print('yes' if is_palindrome(val) else 'no')

if __name__ == '__main__':
    main()