class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        target = abs(arr[0] - arr[1])
        for i in range(1, len(arr)-1):
            curr = abs(arr[i] - arr[i+1])
            if curr < target:
                target = curr

        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) == target:
                res.append([arr[i], arr[i+1]])
        
        return res