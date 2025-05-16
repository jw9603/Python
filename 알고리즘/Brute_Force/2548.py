# 백준 2548. 대표 자연수
# https://www.acmicpc.net/problem/2548
######################## 문제 이해 ########################
# 대표 자연수는 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의
# 합을 최소
# N <= 2 * 10^4
# 
######################## 문제 이해 ########################
# 1. 반복문: O(N^2) -> 시간 초과 예상
# def represent_num(nums):
#     min_num = float('inf')
#     min_num_sum = float('inf')
#     min_list = []
#     for i in range(len(nums)):
#         temp_sum = 0
#         for j in range(len(nums)):
#             diff = abs(nums[i] - nums[j])
#             temp_sum += diff
#         if temp_sum <= min_num_sum:
#             min_num_sum = temp_sum
#             min_num = nums[i]
#             min_list.append(nums[i])

#     return min(min_list)
            
# def main():
#     N = int(input().strip())
#     nums = list(map(int, input().split()))

#     print(represent_num(nums))

# if __name__ == '__main__':
#     main()

# 2. 다른 풀이
def represent_num(nums):
    nums.sort()
    return nums[(len(nums) + 1) // 2 - 1]

def main():
    N = int(input().strip())
    nums = list(map(int, input().split()))

    print(represent_num(nums))

if __name__ == '__main__':
    main()