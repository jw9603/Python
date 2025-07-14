# 백준 8958. OX 퀴즈
# https://www.acmicpc.net/problem/8958
def sol(ox):
    sum_score = 0
    score = 0
    
    for chr in ox:
        if chr == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    
    return sum_score

def main():
    T = int(input().strip())

    for _ in range(T):
        ox = input().strip()
        print(sol(ox))

if __name__ == '__main__':
    main()