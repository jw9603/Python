# 백준 4690. 완전 세제곱
# https://www.acmicpc.net/problem/4690
for a in range(6, 101):
    for b in range(2, 101):
        for c in range(b + 1, 101):
            for d in range(c + 1, 101):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                if a ** 3 < b ** 3 + c ** 3 + d ** 3:
                    break