# 백준 11723. 집합
# https://www.acmicpc.net/problem/11723
################################## 문제 이해 ##################################

################################## 문제 이해 ##################################
import sys

def main():
    M = int(sys.stdin.readline())
    set_val = set()

    for _ in range(M):
        command = sys.stdin.readline().strip().split()

        if command[0] == 'add':
            set_val.add(int(command[1]))
        elif command[0] == 'remove':
            set_val.discard(int(command[1]))  # discard: 없는 값 제거해도 에러 없음
        elif command[0] == 'check':
            print(1 if int(command[1]) in set_val else 0)
        elif command[0] == 'toggle':
            x = int(command[1])
            if x in set_val:
                set_val.remove(x)
            else:
                set_val.add(x)
        elif command[0] == 'all':
            set_val = set(range(1, 21))
        elif command[0] == 'empty':
            set_val.clear()

if __name__ == '__main__':
    main()