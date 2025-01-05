# 백준 1302. 베스트셀러
# https://www.acmicpc.net/problem/1302
import sys
N = int(sys.stdin.readline().strip())
books = [sys.stdin.readline().strip() for _ in range(N)]
def sol(books):
    
    sell_info = {}
    for book in books:
        if book not in sell_info:
            sell_info[book] = 1
        else:
            sell_info[book] += 1
    sell_info = sorted(sell_info.items(), key=lambda x:(-x[1],x[0]))
    print(sell_info[0][0])
sol(books=books)