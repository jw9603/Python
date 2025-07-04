# 백준 1316. 그룹 단어 체키
# https://www.acmicpc.net/problem/1316
############################### 문제 이해 ###############################
# 그룹 단어: 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력

# 입력: 첫째 줄에 단어의 개수 N이 들어온다.
# 둘째 줄부터 N개의 단어가 들어온다.
# 출력: 그룹 단어의 개수

# 알고리즘:
# 흠,,,,
# 단어를 정렬햇을 때
# aabbbbcc / aabbbccb
############################### 문제 이해 ###############################
# 1. 정렬 활용
def sol(N, word):
    if list(word) == sorted(word, key=word.find):
        return True
    return False
    
def main():
    N = int(input().strip())
    cnt = 0

    for _ in range(N):
        word = input().strip()

        if sol(N, word):
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()

# 2. 다른 풀이
def sol(N, word):
    seen = set()
    prev = ''
    for char in word:
        if char != prev:
            if char in seen:
                return False
            seen.add(char)
        prev = char
    return True

def main():
    N = int(input().strip())
    cnt = 0

    for _ in range(N):
        word = input().strip()

        if sol(N, word):
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()