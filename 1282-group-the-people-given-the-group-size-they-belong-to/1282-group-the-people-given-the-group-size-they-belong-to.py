class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        counter = defaultdict(list)

        for i, v in enumerate(groupSizes):
            counter[v].append(i)

            if len(counter[v]) == v:
                res.append(counter.pop(v))
        return res
            