rating = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]
total = 0
res = 0
for _ in range(20):
    s,c,g = input().split()
    c = float(c)
    if g!= 'P':
        total += c
        res += c * grade[rating.index(g)]
        
print(f'{(res/total):.6f}')