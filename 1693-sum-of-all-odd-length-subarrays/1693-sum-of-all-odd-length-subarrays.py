class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 1:
            return sum(arr)

        res = 0
        for i in range(1, len(arr)+1, 2):
            print("i: ", i)
            for j in range(l-i+1):
                print(sum(arr[j:j+i]))
                res += sum(arr[j:j+i])
        return res