class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            ele = heapq.heappop(gifts)
            heapq.heappush(gifts,-int(sqrt(-ele)))
        return -sum(gifts)