# 백준 1339. 단어 수학
# https://www.acmicpc.net/problem/1339
import sys
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]

weights = {}
for word in words:
    length = len(word)
    for i, char in enumerate(word):
        power = 10 ** (length - i -1)
        if char in weights:
            weights[char] += power
        else:
            weights[char] = power
weights = sorted(weights.items(), key=lambda x:x[1], reverse=True)

assign_numbers = {}
num = 9
for char, _ in weights:
    assign_numbers[char] = num
    num -= 1

total = 0
for word in words:
    num_value = 0
    for char in word:
        num_value = 10 * num_value + assign_numbers[char]
    total += num_value
print(total)