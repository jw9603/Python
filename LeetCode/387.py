# 387. First Unique Character in a String
from collections import Counter
from collections import deque
class Solution(object):
    # 1. Counter사용
    def firstUniqChar1(self, s):
        # https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1473939522
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
    # 2. hash, queue 사용
    def firstUniqChar2(self, s):
        # https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1473938334
        """
        :type s: str
        :rtype: int
        """
        
        q = deque()
        char_count = {}
        
        for i, c in enumerate(s):
            q.append((c, i))
            char_count[c] = char_count.get(c, 0) + 1
        
        while q:
            c, idx = q.popleft()
            if char_count[c] == 1:
                return idx
        return -1
    
if __name__ == '__main__':
    a = Solution()
    example1 = "leetcode"
    example2 = "loveleetcode"
    example3 = "aabb"
    
    print(f"example1 result method1: {a.firstUniqChar1(example1)}")
    print(f"example1 result method2: {a.firstUniqChar2(example1)}")
    print(f"example2 result method1: {a.firstUniqChar1(example2)}")
    print(f"example2 result method2: {a.firstUniqChar2(example2)}")
    print(f"example3 result method1: {a.firstUniqChar1(example3)}")
    print(f"example3 result method2: {a.firstUniqChar2(example3)}")
    