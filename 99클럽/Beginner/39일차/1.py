class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 아이 1명당 1개의 쿠키를 줄 수 있음.
        # g[i]는 아이i마다 만족할 수 있는 최소 쿠키 크기
        # 각 쿠키j의 크기는 s[j]
        # 만약 s[j] >= g[i]라면, 쿠키 j를 아이 i에게 줄 수 있음, 아이는 만족
        # return : 만족한 아이들의 수를 최대화 하는 것.
        # 만족도가 낮은 아이에게 작은 쿠키를 주는것, 그래서 만족할 수 있는 아이를 최대화 하기

        g.sort()
        s.sort()
        i = 0
        for k in s:
            if k >= g[i]:
                i += 1
            if i == len(g):
                break
        return i


if __name__ == '__main__':
    a = Solution()
    
    res1 = a.findContentChildren([1,2,3],[1,1])
    res2 = a.findContentChildren([1,2],[1,2,3])
    
    
    print(f'Test Case1 result: {res1}')
    print(f"Test Case2 result: {res2}")