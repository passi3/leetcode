class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        def digit_sum(num):
            return sum(int(d) for d in str(num))
        
        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {num: i for i, num in enumerate(target)}

        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            
            curr = i
            cycle = 0

            while not visited[curr]:
                visited[curr] = True
                curr = pos[nums[curr]]
                cycle += 1
            
            if cycle > 1:
                res += cycle - 1
        
        return res