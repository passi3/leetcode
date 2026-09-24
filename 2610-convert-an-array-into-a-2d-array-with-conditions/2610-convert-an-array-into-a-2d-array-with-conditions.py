class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counter = Counter(nums)
        pivot, n = [(k, v) for k, v in counter.items() if v == max(counter.values())][0]

        res = [[pivot] for _ in range(n)]

        for num in nums:
            if num == pivot:
                continue
            for i in range(n):
                if num not in res[i]:
                    res[i].append(num)
                    break
        
        return res