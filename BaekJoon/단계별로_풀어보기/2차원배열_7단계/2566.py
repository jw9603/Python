# 최댓값 2566번
# https://www.acmicpc.net/problem/2566

# import sys

# max_num = -1
# x, y = 0, 0

# for i in range(9):
#     row = list(map(int,sys.stdin.readline().split()))
    
#     for j in range(9):
#         if row[j] > max_num:
#             max_num = row[j]
#             x = i + 1
#             y = j + 1

# print(max_num)
# print(x,y)


import sys

max_num = 0
x, y = 0, 0

for i in range(9):
    row = list(map(int,sys.stdin.readline().split()))
    
    max_row = max(row)
    
    if max_row >= max_num:
        max_num = max_row
        x = i + 1
        y = row.index(max_row) + 1

print(max_num)
print(x,y)
         
        
    