def solution(myStr):
    ans = myStr.replace('a',' ').replace('b',' ').replace('c',' ')
    return ans.split() or ['EMPTY']