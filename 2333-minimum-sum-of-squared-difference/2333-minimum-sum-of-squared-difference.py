class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a-b) for a, b in zip(nums1, nums2)]
        
        if sum(diff) <= k:
            return 0

        counter = Counter(diff)
        max_diff = max(diff)

        for d in range(max_diff, 0, -1):
            if k == 0:
                break
            
            cnt = counter[d]
            if cnt == 0:
                continue
            
            used = min(k, cnt)
            counter[d] -= used
            counter[d-1] += used
            k -= used
        
        return sum(d * d * cnt for d, cnt in counter.items())