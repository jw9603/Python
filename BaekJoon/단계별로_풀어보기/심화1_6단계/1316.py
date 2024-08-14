import sys

N = int(sys.stdin.readline().strip())

ans = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    
    if list(word) == sorted(word,key=word.find): # 그룹 단어인지 판별
        ans += 1
    
print(ans)