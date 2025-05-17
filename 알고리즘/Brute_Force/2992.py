# 백준 2992. 크면서 작은 수
# https://www.acmicpc.net/problem/2992
############################# 문제 이해 #############################
# 정수 X가 주어졌을 때, X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력
# 구성이 같다는 말: 수를 이루고 있는 각 자리수가 같다는 뜻.
############################# 문제 이해 #############################
from itertools import permutations
def sol(X):
    list_x = sorted(list(permutations(X)))
    
    for x in list_x:
        if X < ''.join(x):
            print(''.join(x))
            return
    
    print(0)

def main():
    X = input().strip()
    sol(X)
    

if __name__ == '__main__':
    main()