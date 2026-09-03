class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        counter = defaultdict(list)

        for i, v in enumerate(groupSizes):
            counter[v].append(i)
        
        for k in sorted(counter.keys()):
            if len(counter[k]) >= k:
                res.extend(counter[k][i:i+k] for i in range(0, len(counter[k]), k))
            else:
                res.append(counter[k])
        
        print(res)
        return res
            