import sys

A, B = map(int,sys.stdin.readline().split())

C = int(sys.stdin.readline().strip())

print((A*60+B+C)//60%24 ,(A*60+B+C)%60)

# 시간은 0시부터 24시까지만 표기할 수 있다. 처음에 틀렸던 이유는 아래 코드 처럼 24시일 때만 0으로 하고 그 이후(새벽1시~~)는 25, 26시로 처리된다.
# 따라서, 24시로 나눈 나머지로 진행해야 한다.
# print((A*60+B+C)//60 if (A*60+B+C)//60 != 24 else 0 ,(A*60+B+C)%60)