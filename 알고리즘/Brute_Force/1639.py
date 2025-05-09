# 백준 1639. 행운의 티켓
# https://www.acmicpc.net/problem/1639
############################## 문제 이해 ##############################
# 야구장에 오는 손님에게 티켓을 나누어 준ㅏ.
# 그 티켓 중 다음과 같은 규칙을 가진 티켓을 행운의 티켓이라고 하며, 그 티켓을 가진 사람들에게
# 상품을 나눠준다.
# 행운의 티켓은 정확하게 2N자리로 이루어진 티켓이다.

############################## 문제 이해 ##############################
def max_lucky_ticket_len(s):
    n = len(s)
    max_len = 0
    
    for length in range(2, n + 1, 2):
        for start in range(n - length + 1):
            mid = start + length // 2
            left = s[start:mid]
            right = s[mid:start + length]
            left_sum = sum(int(l) for l in left)
            right_sum = sum(int(r) for r in right)

            if left_sum == right_sum:
                max_len = max(max_len, length)
    
    return max_len

def main():
    s = input().strip()
    print(max_lucky_ticket_len(s))

if __name__ == '__main__':
    main()