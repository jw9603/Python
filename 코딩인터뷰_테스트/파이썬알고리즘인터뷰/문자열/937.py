# LeetCode 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/description/
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        
        1. 로그의 가장 앞부분은 식별자다.
        2. 두 개의 타입이 있다.
        3. 문자 로그: 식별자를 제외한 모든 문자는 소문자 영어로 구성되어 있다.
        4. 숫자 로그: 식별자를 제외한 모든 숫자는 10

        재정렬 조건:
        1. 문자로 구성된 로그가 숫자로그보다 앞에 온다.
        2. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
        3. 숫자 로그는 입력 순서대로 한다.
        """
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits