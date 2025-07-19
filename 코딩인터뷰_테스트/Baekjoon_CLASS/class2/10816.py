# 백준 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816
################################### 문제 이해 ###################################
# 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구해라

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 셋째 줄에는 M이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어진다.

# 알고리즘
# N개의 숫자 카드들을 키는 숫자, value는 개수로 해시 맵을 만든다.
# 그 다음 M개의 숫자를 카운트하면서 해당 값(value)를 반환한다.
################################### 문제 이해 ###################################
# 1. Hash Table
from collections import Counter
def sol(cards, nums):
    counts = Counter(cards)

    return [counts[num] if num in counts else 0 for num in nums]
def main():
    N = int(input().strip())
    cards = list(map(int, input().split()))
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(cards, nums))

if __name__ == '__main__':
    main()

# 2. Binary Search
from bisect import *
def count_by_binary_search(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    return right - left

def sol(cards, nums):
    cards.sort()
    return [count_by_binary_search(cards, num) for num in nums]

def main():
    N = int(input().strip())
    cards = list(map(int, input().split()))
    M = int(input().strip())
    nums = list(map(int, input().split()))

    print(*sol(cards, nums))

if __name__ == '__main__':
    main()