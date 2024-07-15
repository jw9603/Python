import sys
a = []
for _ in range(9):
    a.append(int(sys.stdin.readline().strip()))
print(max(a),a.index(max(a))+1,sep='\n')