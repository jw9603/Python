def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))


if __name__ =='__main__':
    print(solution(29423))