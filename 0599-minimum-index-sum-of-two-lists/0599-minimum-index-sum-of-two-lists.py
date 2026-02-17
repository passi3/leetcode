class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        shortestIdx = 2000
        setList = set(list1).intersection(set(list2))
        print(setList)
        if len(setList) == 1:
            return list(setList)
        for string in setList:
            minIdx = list1.index(string) + list2.index(string)
            if minIdx < shortestIdx:
                shortestIdx = minIdx
                res = [string]
            elif minIdx == shortestIdx:
                res.append(string)
        
        return res
