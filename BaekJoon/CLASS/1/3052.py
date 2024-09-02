cnt = []
for _ in range(10):
    cnt.append(int(input()) % 42)
print(len(set(cnt)))