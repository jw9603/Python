# 백준 10828. 스택
# https://www.acmicpc.net/problem/10828
def main():
    N = int(input().strip())
    commands = [list(input().split()) for _ in range(N)]
    stack = []

    for command in commands:
        if command[0] == 'push':
            stack.append(int(command[1]))
        elif command[0] == 'pop':
            print(stack.pop() if stack else -1)
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            print(1 if not stack else 0)
        else:
            print(stack[-1] if stack else -1)

if __name__ == '__main__':
    main()