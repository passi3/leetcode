class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        counter = Counter(bulbs)

        return sorted([i for i,v in counter.items() if v % 2 == 1])