from collections import Counter
import sys
alph = sys.stdin.readline().strip().lower()

res = Counter(alph).most_common()
if len(res) == 1:
    print(res[0][0].upper())
elif res[0][1] == res[1][1]:
    print("?")
else:
    print(res[0][0].upper())