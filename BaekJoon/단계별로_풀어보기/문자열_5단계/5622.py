import sys

a = sys.stdin.readline().strip()

phone = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
ans = 0
for i in a:
    for j in phone:
        if i in j:
            ans += phone.index(j) + 3
            
print(ans)
