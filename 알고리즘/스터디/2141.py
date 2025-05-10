# 백준 2143. 우체국
# https://www.acmicpc.net/problem/2141
################################## 문제 이해 ###########################
# 일직선상에 N개의 마을이 있다. i번째 마을은 X[i]에 위치해 있으며, A[i]명의 사람이 살고 있다.
# 이 마을들을 위해 우체국을 하나 세우려고 하는데, 그 위치는?
# 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정
# 각 마을까지의 거리의 합이 아니라, 각 사람까지의 거리의 합!!
# 그렇기 때문에, 각 사람까지의 거리의 합이 최소가 될려면 전체 사람의 절반 이상이 위치하는 거리가 최소 거리다.

################################## 문제 이해 ###########################'
def make_post_office(villages):
    villages.sort()
    total_people = sum(a for x, a in villages)

    people_sum = 0
    for x, a in villages:
        people_sum += a
        if people_sum >= (total_people + 1) // 2:
            return x

def main():
    N = int(input().strip())
    villages = []

    for _ in range(N):
        x, a = map(int, input().split())
        villages.append((x, a))
    
    print(make_post_office(villages))

if __name__ == '__main__':
    main()