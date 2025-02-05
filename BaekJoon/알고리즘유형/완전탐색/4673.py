# 백준 4673. 셀프 넘버
# https://www.acmicpc.net/problem/4673
def d(n):
    return n + sum(int(i) for i in str(n))
def find_self_numbers(limit):
    generated = set()
    
    for i in range(1, limit + 1):
        generated.add(d(i))
        
    for i in range(1, limit + 1):
        if i not in generated:
            print(i)
find_self_numbers(10000)