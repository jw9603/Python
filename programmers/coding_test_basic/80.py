def solution(polynomial):
    polynomial = polynomial.replace(' ', '').split('+')
    a, b = 0, 0
    for i in polynomial:
        if 'x' in i:
            if len(i) > 1:
                a += int(i[:-1])
            else:
                a +=1
        else:
            b += int(i)
    
    if a == 0:
        return '{}'.format(b)
    elif a == 1:
        if b == 0:
            return 'x'
        elif b != 0:
            return 'x + {}'.format(b)
    elif a > 1:
        if b == 0:
            return '{}x'.format(a)
        elif b != 0:
            return '{}x + {}'.format(a, b)
        
if __name__ =='__main__':
    print(solution("3x + 7 + x"))
            