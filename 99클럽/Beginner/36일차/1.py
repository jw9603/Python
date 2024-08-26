# 1145번 백준. 적어도 대부분의 배수 
# https://www.acmicpc.net/problem/1145
# 적어도 대부분의 배수 : 주어진 수 중 적어도 세 개로 나누어지는 가장 작은 자연수


######################## 브루트포스 ##############################
# import sys
# import time
# a = time.time()
# integer_list = list(map(int,sys.stdin.readline().split()))

# i = min(integer_list)
# while True:
#     cnt = 0
    
#     for n in integer_list:
#         if i % n == 0:
#             cnt += 1
#     if cnt >= 3:
#         print(i)
#         break
    
#     i += 1
# print(time.time()-a) # 2.7800538539886475 about test case 1
######################## 브루트포스 ##############################

####################### 조합 #################################
import math
from itertools import combinations
import sys
import time
a = time.time()
def lcm(a,b):
    return abs(a * b) // math.gcd(a,b)

def lcm_multiple(numbers):
    lcm_value = numbers[0]
    for num in numbers[1:]:
        lcm_value = lcm(lcm_value,num)
    return lcm_value

numbers = list(map(int,sys.stdin.readline().split()))

min_lcm = float('inf')

for r in range(3,6):
    for comb in combinations(numbers,r):
        min_lcm = min(min_lcm,lcm_multiple(comb))
print(min_lcm)
print(time.time()-a) # 0.6261699199676514 about test case1
####################### 조합 #################################
