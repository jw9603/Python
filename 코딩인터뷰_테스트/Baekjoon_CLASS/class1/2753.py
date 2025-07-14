# 백준 2753. 윤년
# https://www.acmicpc.net/problem/2753
def is_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def sol(year):
    return 1 if is_year(year) else 0

def main():
    year = int(input().strip())

    print(sol(year))

if __name__ == '__main__':
    main()