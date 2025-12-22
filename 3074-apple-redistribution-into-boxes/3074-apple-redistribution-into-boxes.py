class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        if sum(capacity) == apples:
            return len(capacity)
        
        cnt = 0
        capacity.sort(reverse=True)
        for box in capacity:
            apples -= box
            cnt += 1
            if apples <= 0:
                return cnt