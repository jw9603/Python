def solution(spell, dic):
    spell = set(spell)
    for i in dic:
        if spell.issubset(set(i)):
            return 1
    return 2

if __name__ =='__main__':
    print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))