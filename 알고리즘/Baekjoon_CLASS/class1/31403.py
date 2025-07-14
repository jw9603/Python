# 백준 31403. A + B - C
# https://www.acmicpc.net/problem/31403
def main():
    A = input()
    B = input()
    C = input()

    print(int(A) + int(B) - int(C))
    print(int(A + B) - int(C))

if __name__ == '__main__':
    main()