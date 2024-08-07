# 외계어 사전
def solution(spell, dic):
    for i in dic:
        if sorted(i) == sorted(spell):
            return 1
    return 2

if __name__ == '__main__':
    print(solution(["p", "o", "s"],	["sod", "eocd", "qixm", "adio", "soo"]))
    print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))
    print(solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"]))