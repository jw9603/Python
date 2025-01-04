# 백준 20291. 파일 정리
# https://www.acmicpc.net/problem/20291
import sys
N = int(sys.stdin.readline().strip())
files = [sys.stdin.readline().strip() for _ in range(N)]

def sol(files):
    file_name = {}
    for file in files:
        file = file.split('.')[1]
        if file not in file_name:
            file_name[file] = 1
        else:
            file_name[file] += 1
    result = sorted(file_name.items())
    
    for extend, cnt in result:
        print(f"{extend} {cnt}")
sol(files=files)
    