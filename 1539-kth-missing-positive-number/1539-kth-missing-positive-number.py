class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        num = 0
        while True :
            count += 1
            if len(arr) != 0 and count == arr[0] :
                arr.pop(0)
            else:
                num += 1
                if num == k:
                    break

        return count       