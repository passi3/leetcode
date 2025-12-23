class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        titleSplit = title.split()

        
        return " ".join([word[0].upper()+word[1:] if len(word) > 2 else word for word in titleSplit])