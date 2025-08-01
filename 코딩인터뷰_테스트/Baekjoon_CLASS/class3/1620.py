# 백준 1620. 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
###################################### 문제 이해 ######################################
# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 몬제의 개수 M이 주어집니다.
# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어온다.
# 포켓몬의 이름은 모두 영어로만 이루어져있고, 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있다.
# 일부 포켓몬은 마지막 문자만 대문자일수도있다.

# 그 다음줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어온다.
# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야함.

# 출력:
# 첫째 줄부터 차례대로 M개의 줄에 각각의 문제애 대한 답

# 알고리즘
# 전형적인 해시를 사용하라는 문제
###################################### 문제 이해 ######################################
def make_dogam(pokemons):
    name_dict, number_dict = {}, {}
    for i, pokemon in enumerate(pokemons):
        name_dict[pokemon] = i + 1
        number_dict[i + 1] = pokemon

    return name_dict, number_dict

def sol(name_dict, number_dict, to_solve_pokemons):

    for x in to_solve_pokemons:
        if x.isdigit():
            print(number_dict[int(x)])
        else:
            print(name_dict[x])

def main():
    N, M = map(int, input().split())
    pokemons = [input().strip() for _ in range(N)]
    to_solve_pokemons = [input().strip() for _ in range(M)]
    name_dict, number_dict = make_dogam(pokemons)

    sol(name_dict, number_dict, to_solve_pokemons)

if __name__ == '__main__':
    main()