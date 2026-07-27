class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = float("inf")
        counter = Counter(text)
        target = Counter("balloon")
        
        for k, v in target.items():
            cnt = min(counter[k]//v, cnt)
        
        return cnt