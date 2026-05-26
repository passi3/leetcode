class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = int(len(arr) * 0.05)

        return sum(arr[l:-l]) / (len(arr) - 2*l)