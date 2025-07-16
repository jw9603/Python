# 백준 1181. 단어 정렬
# https://www.acmicpc.net/problem/1181
##################################### 문제 이해 #####################################
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬
# 길이가 짧은것부터, 같으면 사전순
# 중복된 단어는 하나만 남기고 제고
# 
##################################### 문제 이해 #####################################
def sol(words):
    return sorted(list(set(words)), key=lambda x:(len(x), x))

def main():
    N = int(input().strip())
    words = [input().strip() for _ in range(N)]
    print(*sol(words), sep='\n')

if __name__ == '__main__':
    main()