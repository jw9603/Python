# 백준 30802. 웰컴 키트
# https://www.acmicpc.net/problem/30802
####################################### 문제 이해 #######################################
# 참가자들에게 티셔츠 한 장과 펜 한 자루가 포함된 웰컴 키트를 나눠줄 예정
# 티셔츠는 S, M, L, XL, XXL, XXXL의 6가지 사이즈가 있고, 티셔츠는 같은 사이즈의 T장 묶음으로만 주문
# 펜은 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있음.

# 총 N명의 참가자 중 S, M, L, XL, XXL, XXXL 사이즈의 티셔츠를 신청한 사람은 각각
# S, M, L, XL, XXL, XXXL명입니다.
# 티셔츠는 남아도 되지만 부족해서는 안되고 신청한 사이즈대로 나눠주어야 한다.
# 펜은 남거나 부족해서는 안된다.
# 티셔츠를 T장씩 최소 몇 묶음으로 주문해야 하는 지, 펜을 P자루씩 최대 몇 묶음을 주문할 수 있고, 그 때
# 펜을 한 자루씩 몇 개 주문하는지 구해라.

# 입력:
# 첫째 줄에 참가자 수 N
# 둘째 줄에 티셔트의 사이즈별 신청자의 수가 주어짐
# 셋째 줄에는 정수 티셔츠와 펜의 묶음 수를 의미하는 T와 P가 주어짐
# 출력: 
# 첫 줄에 티셔츠를 T장씩 최소 몇 묶음으로 주문해야 하는지 출력
# 다음줄에 펜을 P자루씩 최대 몇 묶음을 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문해야하는지

####################################### 문제 이해 #######################################
from math import ceil
def sol(sizes, T, P):
    # 티셔츠 묶음 수
    tshirt_bundles = sum(ceil(size / T) for size in sizes)

    # 펜 묶음 수와 개수
    total_people = sum(sizes)
    pen_bundles =  total_people // P
    pen_remainder = total_people % P   

    return tshirt_bundles, pen_bundles, pen_remainder

def main():
    N = int(input().strip())
    sizes = list(map(int, input().strip().split()))
    T, P = map(int, input().strip().split())

    tshirt_bundles, pen_bundles, pen_remainder = sol(sizes, T, P)
    print(tshirt_bundles)
    print(pen_bundles, pen_remainder)

if __name__ == "__main__":
    main()