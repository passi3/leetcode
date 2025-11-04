class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        combined = list(zip(names, heights))
        combined.sort(key=lambda x: x[1], reverse=1)
        return [name for name, _ in combined]