def solution(emergency):
    tmp=sorted(emergency,reverse=True)
    return [tmp.index(i)+1 for i in emergency]

if __name__ == '__main__':
    print(solution([3, 76, 24]))