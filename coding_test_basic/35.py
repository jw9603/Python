def solution(rsp):
    rsp = rsp.strip(',')
    ans = []
    for i in rsp:
        if i == '2':
            ans.append('0')
        elif i == '0':
            ans.append('5')
        
        elif i == '5':
            ans.append('2')
        else:
            continue
            
    return ''.join(ans)