class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        hash = dict()
        for i in range(len(boxTypes)):
            numBox, numUnits = boxTypes[i][0], boxTypes[i][1]
            hash[numUnits] = hash.get(numUnits, 0) + numBox
        
        print(hash)
        sortedHash = sorted(hash.keys(), reverse=True)
        for k in sortedHash:
            loaded = min(truckSize, hash[k])
            truckSize -= loaded
            res += loaded * k
        
        return res