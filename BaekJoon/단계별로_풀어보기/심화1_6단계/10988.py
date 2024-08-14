import sys

word = sys.stdin.readline().strip()

def pend(word):
    if len(word) <= 1:
        return 1
    
    if word[0] == word[-1]:
        return pend(word[1:-1])
    else:
        return 0
    
print(pend(word))
    
    