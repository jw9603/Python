from collections import Counter
import sys

dice = list(map(int,sys.stdin.readline().split()))
a = Counter(dice).most_common()

if len(a) == 1:
    print(10000 + a[0][0] * 1000)
elif len(a) ==2:
    print(1000 + a[0][0] * 100)
else:
    print(max(dice)*100)
    


