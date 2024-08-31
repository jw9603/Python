# 9012 (괄호)
# https://www.acmicpc.net/problem/9012



################ 스택을 활용한 풀이 ###########
# import time
# import sys
# t = time.time()
# T = int(sys.stdin.readline().strip())

# for _ in range(T):
    
#     ps = sys.stdin.readline().strip()
#     stack = []
#     for i in ps:
        
#         if i == '(':
#             stack.append(i)
#         else:
#             if stack:
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
    
#     if len(stack):
#         print('NO')
#     else:
#         print('YES')
# print(time.time()-t)
        
################ 스택을 활용한 풀이 ###########



############# 카운팅을 이용한 풀이 ###########
import sys
import time
t = time.time()
T = int(sys.stdin.readline().strip())

for _ in range(T):
    ps = sys.stdin.readline().strip()
    
    total = 0
    
    for i in ps:
        if i == '(':
            total += 1
        else:
            total -= 1
        
        if total < 0:
            print("NO")
            break
    
    if total > 0:
        print("NO")
    elif total == 0:
        print('YES')
print(time.time()-t)
############# 카운팅을 이용한 풀이 ###########