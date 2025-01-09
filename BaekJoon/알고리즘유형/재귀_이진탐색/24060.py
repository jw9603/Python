# 백준 24060. 알고리즘 수업 - 병합 정렬 1
# https://www.acmicpc.net/problem/24060
import sys

def merge(left, right, A, p):
    global count, result
    merged = []
    left_index, right_index = 0, 0

    # 1. left/right 둘 다 있을 때
    while len(left) > left_index and len(right) > right_index: 
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    # 2. left만 남아있을 때
    while len(left) > left_index:
        merged.append(left[left_index])
        left_index += 1
    # 3. right만 남아있을 때
    while len(right) > right_index:
        merged.append(right[right_index])
        right_index += 1

    print('merged',merged)
    # 병합된 결과를 원래 배열에 저장하며 저장 작업 추적
    for i in range(len(merged)):
        A[p + i] = merged[i]  # 원래 배열에 저장
        count += 1
        if count == K:  # K번째 저장 작업인 경우 값 기록
            result = A[p + i]

    return A[p:p + len(merged)]


def merge_sort(A, p, r): # 배열 A의 부분 구간 [p, r]에 대해 병합 정렬을 수행합니다.
    if p < r:
        q = (p + r) // 2 # q == medium
        left = merge_sort(A, p, q)
        right = merge_sort(A, q + 1, r)
        return merge(left, right, A, p)
    else:
        return [A[p]]


# 입력 처리
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

count = 0
result = -1

merge_sort(A, 0, N - 1)

# 결과 출력
print(result if count >= K else -1)
