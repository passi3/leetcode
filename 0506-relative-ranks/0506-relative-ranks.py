class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score,reverse=True)
        res = {}
        for i, s in enumerate(rank):
            if i == 0:
                res[s]="Gold Medal"
            elif i==1:
                res[s]="Silver Medal"
            elif i==2:
                res[s]="Bronze Medal"
            else:
                res[s]=str(i+1)
        return [res[s] for s in score]