class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]

        """
        sorted_score = sorted(score,reverse=True)

        rank = {}
        ans = []

        for i in range(len(sorted_score)):
            rank[sorted_score[i]] = i

        for i in range(len(score)):
            if rank[score[i]] == 0:
                ans.append('Gold Medal')
            elif rank[score[i]] == 1:
                ans.append('Silver Medal')
            elif rank[score[i]] == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(rank[score[i]]+1))

        return ans