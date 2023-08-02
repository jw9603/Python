def solution(lines):
    table = [set([]) for _ in range(200)]
    
    for i,l in enumerate(lines):
        x1,x2 = l
        for x in range(x1,x2):
            table[x+100].add(i)
           
    ans = 0
    for line in table:
        print(line)
        if len(line) > 1:
            ans +=1
    
    return ans

if __name__ =='__main__':
    print(solution([[0, 1], [2, 5], [3, 9]]))