# LeetCode 819. Most Common Word
# https://leetcode.com/problems/most-common-word/description/
from collections import Counter
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        문자열 paragraph와 문자열 배열 banned가 주어진다.
        금지 단어가 아닌 단어 중 가장 많이 등장하는 단어를 반환하세요.

        """
        banned_set = set(word.lower() for word in banned)
        word = []
        words = []
        
        for ch in paragraph.lower():
            if 'a' <= ch <= 'z':
                word.append(ch)
            else:
                if word:
                    words.append(''.join(word))
                    word = []
        
        if word:
            words.append(''.join(word))

        print(words)
        
        counts = Counter(word for word in words if word not in banned_set)
        
        return counts.most_common(1)[0][0]

if __name__ == '__main__':
    sol = Solution()
    print("Result1:", sol.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))