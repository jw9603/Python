# 백준 9498. 시험 성적
# https://www.acmicpc.net/problem/9498
def sol(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

def main():
    score = int(input().strip())
    
    print(sol(score))

if __name__ == '__main__':
    main()