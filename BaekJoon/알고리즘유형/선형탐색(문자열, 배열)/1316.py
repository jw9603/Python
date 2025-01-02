# 백준 1316. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316


############################ 1번째 풀이 #####################
import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
def sol(word):
    seen = set()
    prev_char = ''
    for char in word: 
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True
print(sum(sol(word) for word in words))
############################ 1번째 풀이 #####################

############################ 2번째 풀이 #####################
import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]

def sol(word):
    
    return list(word) == sorted(word,key=lambda x: word.find(x))
print(sum(sol(word) for word in words))
############################ 2번째 풀이 #####################
    