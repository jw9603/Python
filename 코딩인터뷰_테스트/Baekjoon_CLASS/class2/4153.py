# 백준 4153. 직각삼각형
# https://www.acmicpc.net/problem/4153
def sol(side_list):
    max_val = max(side_list)
    side_list.remove(max_val)

    if max_val ** 2 == sum([val ** 2 for val in side_list]):
        return True
    return False

def main():
    while 1:
        side_list = list(map(int, input().split()))
        if sum(side_list) == 0:
            break
        
        print("right" if sol(side_list) else "wrong")

if __name__ == '__main__':
    main()