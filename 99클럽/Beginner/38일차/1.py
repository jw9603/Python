# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/


################### Counter 모듈 사용 ######################
from collections import Counter
class Solution1(object):
    
    def longestPalindrome(self,s):
        cnt = Counter(s)
        odd_cnt = 0
        
        for key,value in cnt.items():
            if value % 2 != 0:
                cnt[key] = value - 1
                odd_cnt = 1
                
        return sum(list(cnt.values())) + odd_cnt 

################### Counter 모듈 사용 ######################


################# hash (Counter 모듈 사용 X) #################
class Solution2(object):
    
    def longestPalindrome(self,s):
        
        cnt = {}
        
        for char in s:
            cnt[char] = cnt.get(char,0) + 1
            
        
        length = 0
        odd_found = False
        
        for c in cnt.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd_found = True
                
        return length + 1 if odd_found else length
################# hash (Counter 모듈 사용 X) #################


if __name__ == '__main__':
    import time
    
    t = time.time()
    
    a = Solution1()
    
    res1 = a.longestPalindrome("abccccdd")
    res2 = a.longestPalindrome("a")
    
    print(f"Test Case1 result: {res1}")
    print(f"Test Case2 result: {res2}")
    
    print(f"time: {time.time()-t:.5f}s")
    
    
    t = time.time()
    
    a = Solution2()
    
    res1 = a.longestPalindrome("abccccdd")
    res2 = a.longestPalindrome("a")
    
    print(f"Test Case1 result: {res1}")
    print(f"Test Case2 result: {res2}")
    
    print(f"time: {time.time()-t:.5f}s")