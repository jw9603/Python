# 백준 4659. 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
import sys
def sol(password):
    vowels = {'a','e','i','o','u'}
    if not any(char in vowels for char in password):
        return False
    
    cnt = 1
    for i in range(1, len(password)):
        if (password[i] in vowels) == (password[i - 1] in vowels):
            cnt += 1
            if cnt >= 3:
                return False
        else:
            cnt = 1
            
    for i in range(1, len(password)):
        if password[i] == password[i - 1] and password[i] not in 'eo':
            return False
    return True
    
while True:
    password = sys.stdin.readline().strip()
    if password == 'end':
        break
    if sol(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")    