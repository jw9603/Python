# 백준 9012. 괄호
# https://www.acmicpc.net/problem/9012
def sol(ps):
    stack = []
    for s in ps:
        if s == '(':
            stack.append(s)
        else: # s == ')'
            if stack:
                stack.pop()
            else:
                stack.append(')')
                break
    return 'YES' if not stack else 'NO'

def main():
    T = int(input().strip())

    for _ in range(T):
        ps = input().strip()
        print(sol(ps))

if __name__ == '__main__':
    main()